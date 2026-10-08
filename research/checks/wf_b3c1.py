"""Helpers for R4 checks B3b/B3c (overlapping generations) and C1 (aDNA panel ascertainment).

THROWAWAY, non-product. Does not modify wf.py. Reuses nothing from it except conventions.

Part 1: age-structured neutral model after Balloux & Lehmann 2012 (B&L), Evolution 66:605-611.
  Haploid population, discrete time steps t = 0,1,2,...; demographic state j has size N_j.
  A transition i -> j keeps round(N_i * s_ij) survivors (uniformly sampled), and the remaining
  N_j - survivors slots are filled by newborns whose parent is drawn uniformly from the N_i
  pre-transition individuals (exchangeable, no senescence). Mutations occur at birth, infinite
  sites, unlinked: Poisson(U * births) new single-copy mutants per step (U = genome-wide mutation
  probability per newborn, mu in B&L).
  B&L eq (3): k = mu * sum_j p_j n_j pi_j with pi_j = 1/N_j  ->  k/mu = sum_i p_i sum_j P_ij (N_j - N_i s_ij)/N_j.

Part 2: exact Wright-Fisher Markov chain machinery (2N gene copies) for the aDNA calculation.
"""
import numpy as np
from scipy import stats


# --------------------------------------------------------------------------- B&L analytic
def stationary(P):
    w, v = np.linalg.eig(P.T)
    i = np.argmin(np.abs(w - 1))
    p = np.real(v[:, i])
    return p / p.sum()


def realize_survival(Ns, S):
    """Round survivors to integers exactly as the simulation does; returns effective S matrix."""
    Ns = np.asarray(Ns, dtype=float)
    S2 = np.round(Ns[:, None] * S) / Ns[:, None]
    return S2


def bl_k_over_mu(Ns, P, S, check=True):
    """B&L eq (3)/(4): k/mu per time step for Markov demography (Ns sizes, P transitions, S survival)."""
    Ns = np.asarray(Ns, dtype=float)
    n = Ns[None, :] - Ns[:, None] * S          # n_ij = N_j - N_i s_ij  (births)
    if check and (n < -1e-9).any() and (P > 0).any():
        bad = (n < -1e-9) & (P > 0)
        if bad.any():
            raise ValueError("negative births for a possible transition")
    p = stationary(P)
    return float((p[:, None] * P * n / Ns[None, :]).sum())


def bl_births_and_size(Ns, P, S):
    """Stationary mean births per step and mean N (for generation-time accounting)."""
    Ns = np.asarray(Ns, dtype=float)
    p = stationary(P)
    n = Ns[None, :] - Ns[:, None] * S
    return float((p[:, None] * P * n).sum()), float((p * Ns).sum())


def bl_two_state_eq8(N1, N2, a1, a2, s11, s22, s12, s21):
    """B&L eq (8), transcribed from the paper text, for cross-checking bl_k_over_mu."""
    pref = 1.0 / (2 - a2 - a1)
    br = (a1 * (1 - a2) * s11 + (1 - a1) * a2 * s22
          + (1 - a1) * (1 - a2) * (N1 * s12 / N2 + N2 * s21 / N1))
    return 1 - pref * br


def two_state(N1, N2, a1, a2, s11, s22, s12, s21):
    P = np.array([[a1, 1 - a1], [1 - a2, a2]])
    S = np.array([[s11, s12], [s21, s22]])
    return np.array([N1, N2]), P, S


# --------------------------------------------------------------------------- B&L simulation
def sim_overlap(Ns, P, S, U, T, burn, rng, state0=0):
    """Individual-based neutral simulation (see module docstring).

    Returns dict: fix (fixations counted in the T measured steps), arrival (sum over measured steps of
    U*births/N_j = expected number of eventual fixers born), births (sum), T.
    """
    Ns = np.asarray(Ns, dtype=np.int64)
    c = len(Ns)
    S = realize_survival(Ns, S)
    surv_tab = np.rint(Ns[:, None] * S).astype(np.int64)
    cum = np.cumsum(P, axis=1)
    cnt = np.empty(0, dtype=np.int64)
    i = state0
    fix = 0
    arrival = 0.0
    births_sum = 0
    for t in range(burn + T):
        u = rng.random()
        j = min(int(np.searchsorted(cum[i], u, side="right")), c - 1)
        Ni, Nj = int(Ns[i]), int(Ns[j])
        sv = int(surv_tab[i, j])
        births = Nj - sv
        if births < 0:
            raise ValueError("negative births")
        if cnt.size:
            ks = rng.hypergeometric(cnt, Ni - cnt, sv) if sv > 0 else 0
            kb = rng.binomial(births, cnt / Ni) if births > 0 else 0
            cnt = ks + kb
        nm = rng.poisson(U * births)
        if nm:
            cnt = np.concatenate([cnt, np.ones(nm, dtype=np.int64)])
        fixed = cnt == Nj
        keep = (cnt > 0) & (cnt < Nj)
        if t >= burn:
            fix += int(fixed.sum())
            arrival += U * births / Nj
            births_sum += births
        cnt = cnt[keep]
        i = j
    return dict(fix=fix, arrival=arrival, births=births_sum, T=T)


def _rep(args):
    Ns, P, S, U, T, burn, seed = args
    rng = np.random.default_rng(seed)
    return sim_overlap(Ns, P, S, U, T, burn, rng)


def run_reps(Ns, P, S, U, T, burn, reps, seed0, pool=None):
    seeds = np.random.SeedSequence(seed0).spawn(reps)
    jobs = [(Ns, P, S, U, T, burn, s) for s in seeds]
    res = pool.map(_rep, jobs) if pool is not None else [_rep(j) for j in jobs]
    return res


def summarize(res, U):
    fix = np.array([r["fix"] for r in res], float)
    arr = np.array([r["arrival"] for r in res], float)
    T = res[0]["T"]
    k = fix / (U * T)
    a = arr / (U * T)
    n = len(res)
    return dict(k=k.mean(), k_se=k.std(ddof=1) / np.sqrt(n), arr=a.mean(), arr_se=a.std(ddof=1) / np.sqrt(n),
                fix_total=int(fix.sum()))


def single_mutant_pfix(Ns_path, surv_path, reps, rng, tail_N=None, max_steps=10**6):
    """P(fix) of a single neutral mutant newborn present at step 0 (carriers = 1 of Ns_path[0]).

    Ns_path[t] = size at time t; surv_path[t] = survivors from t to t+1 (0 -> non-overlapping).
    After the path ends, size stays at Ns_path[-1] with survival fraction surv_path[-1]/Ns_path[-2]... we
    require the caller to pass a long constant tail in Ns_path/surv_path instead (see calls).
    Returns fixed fraction and count.
    """
    cnt = np.ones(reps, dtype=np.int64)
    fixed_total = 0
    alive = np.ones(reps, dtype=bool)
    T = len(Ns_path) - 1
    for t in range(T):
        Ni, Nj = int(Ns_path[t]), int(Ns_path[t + 1])
        sv = int(surv_path[t])
        births = Nj - sv
        idx = np.flatnonzero(alive)
        if idx.size == 0:
            break
        c = cnt[idx]
        ks = rng.hypergeometric(c, Ni - c, sv) if sv > 0 else 0
        kb = rng.binomial(births, c / Ni)
        c = ks + kb
        cnt[idx] = c
        done_fix = c == Nj
        done_loss = c == 0
        fixed_total += int(done_fix.sum())
        alive[idx[done_fix | done_loss]] = False
    return fixed_total / reps, fixed_total


# --------------------------------------------------------------------------- RRME arithmetic
def rrme(Nseries):
    N = np.asarray(Nseries, float)
    return (N ** 2).sum() / N.sum() / N[-1]


def rrme_geometric(g_per_cohort, ncoh):
    """RRME k/mu for a geometric growth series with ratio g per cohort, ncoh cohorts, last = current."""
    N = g_per_cohort ** np.arange(-(ncoh - 1), 1, dtype=float)
    return rrme(N)


# --------------------------------------------------------------------------- exact WF chain (C1)
def wf_matrix(M):
    """Row-stochastic WF transition matrix on k = 0..M copies (binomial resampling, neutral)."""
    k = np.arange(M + 1)
    P = stats.binom.pmf(k[None, :], M, (k / M)[:, None])
    return P / P.sum(axis=1, keepdims=True)


def mat_pow(P, n):
    n = int(n)
    R = np.eye(P.shape[0])
    B = P.copy()
    while n:
        if n & 1:
            R = R @ B
        n >>= 1
        if n:
            B = B @ B
    return R


def sample_all_prob(M, nsamp_copies):
    """For each y_k = k/M: P(all sampled copies carry the allele) = y^n ; and the complement allele."""
    y = np.arange(M + 1) / M
    return y ** nsamp_copies, (1 - y) ** nsamp_copies


def maf_include(M, nd, thr):
    """P(discovery sample of nd diploids shows MAF >= thr) as function of true freq y_k = k/M."""
    y = np.arange(M + 1) / M
    K = np.arange(2 * nd + 1)
    maf = np.minimum(K, 2 * nd - K) / (2 * nd)
    ok = maf >= thr - 1e-12
    pm = stats.binom.pmf(K[None, :], 2 * nd, y[:, None])
    return (pm * ok[None, :]).sum(axis=1)


def band_matrix(M, n0, edges):
    """Neolithic-sample band probabilities for allele a given true freq x_k=k/M.

    Returns (Bder, Banc), each shape (M+1, nb): P(freq of derived (resp. ancestral) allele in the sample
    lies in band b AND is not exactly 100%). bands: [edges[b], edges[b+1]).
    """
    x = np.arange(M + 1) / M
    K = np.arange(2 * n0 + 1)
    pm = stats.binom.pmf(K[None, :], 2 * n0, x[:, None])
    fder = K / (2 * n0)
    nb = len(edges) - 1
    Bd = np.zeros((M + 1, nb))
    Ba = np.zeros((M + 1, nb))
    for b in range(nb):
        lo, hi = edges[b], edges[b + 1]
        sel_d = (fder >= lo - 1e-12) & (fder < hi - 1e-12) & (K != 2 * n0)
        fanc = 1 - fder
        sel_a = (fanc >= lo - 1e-12) & (fanc < hi - 1e-12) & (K != 0)
        Bd[:, b] = (pm * sel_d[None, :]).sum(axis=1)
        Ba[:, b] = (pm * sel_a[None, :]).sum(axis=1)
    return Bd, Ba
