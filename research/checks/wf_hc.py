"""Helpers for the R4 H (cost of selection) and C2 (turnover coefficient d) checks.
THROWAWAY research code; does not modify wf.py.

Contents
  Haldane cost D (deterministic recursions)
  treadmill_run   : individual-based diploid population on a moving optimum, HARD or SOFT regulation,
                    Nunney-style (reconstructed; see docstring for what differs from Nunney 2003)
  mutload_run     : individual-based deleterious-load model (Keightley U), HARD or SOFT regulation
  age-structured helpers (Siler life table, Euler-Lotka, Day's d, cohort-binomial IBM)
"""
import numpy as np
from scipy.optimize import brentq

# ---------------------------------------------------------------- Haldane cost D
def haldane_D_haploid(p0):
    """D = sum_t (w_max - wbar)/wbar for haploid selection p0 -> 1. Exact value is ln(1/p0) as s -> 0."""
    return float(np.log(1.0 / p0))

def haldane_D_diploid(p0, s, h=0.5, dom_fitness="additive"):
    """Deterministic diploid recursion from p0 to 1-p0; D = sum_t (1-wbar/wmax)/(wbar/wmax)  (units of N).
    Fitness of aa,Aa,AA = 1, 1+2hs, 1+2s (so s is per-copy for h=1/2). Cost is nearly independent of s."""
    p = p0
    wmax = 1 + 2 * s
    D = 0.0
    for _ in range(10**7):
        q = 1 - p
        waa, wAa, wAA = 1.0, 1 + 2 * h * s, 1 + 2 * s
        wbar = q * q * waa + 2 * p * q * wAa + p * p * wAA
        D += (wmax - wbar) / wbar
        p = (p * p * wAA + p * q * wAa) / wbar
        if p > 1 - p0:
            break
    return D

# ---------------------------------------------------------------- treadmill IBM (H, part b)
def treadmill_run(K, n, T, s, R, u, regime, cycles, rng, stagger=False, burn=1):
    """Diploid sexual population (N adults), n unlinked loci, integer alleles, optimum A*_j(t)=floor((t+off_j)/T).

    Survival prob of a juvenile = (1-s)^(sum over loci and both copies of |A*_j - allele|)  (<=1, absolute).
    Mutation: life cycle = reproduction -> mutation of juvenile gametes (rate u*K/J, so M = 2*K*u per locus per gen under both regimes) -> selection.
    HARD : fecundity per female f = min(R, 2 exp(r(1-N/K))), r = ln(R/2) (Nunney 2003 Eq.3-4 reconstruction:
           f(0)=R=2e^r, f(K)=2; density dependence acts BEFORE selection); juveniles survive independently
           with probability w. Selective deaths therefore reduce N (no compensation beyond f).
    SOFT : every female bears R offspring (density-independent); K adults are then drawn from the
           juveniles with probability proportional to w (competition for K slots; relative fitness only).
    Differences from Nunney: his survival function is Gaussian in time/allele (Eq. 5, not recoverable from the
    text extraction); here selection is a constant per-step s. The Haldane-type accounting is the same.
    Returns dict(extinct, lag, Nfrac, subs) ; success = (not extinct) and (mean pre-shift lag < 0.5).
    """
    off = (np.arange(n) * T / n).astype(int) if stagger else np.zeros(n, dtype=int)
    lns = np.log1p(-s)
    r = np.log(R / 2.0)
    N = K
    G = np.zeros((N, n, 2), dtype=np.int8)
    sex = rng.integers(0, 2, N)
    lags, Ns = [], []
    ngen = cycles * T
    for t in range(ngen):
        fem = np.flatnonzero(sex == 1)
        mal = np.flatnonzero(sex == 0)
        if len(fem) == 0 or len(mal) == 0:
            return dict(extinct=True, lag=np.nan, Nfrac=0.0)
        if regime == "hard":
            f = min(R, 2.0 * np.exp(r * (1 - N / K)))
        else:
            f = R
        fl = np.floor(f)
        cnt = (fl + (rng.random(len(fem)) < (f - fl))).astype(np.int64)
        mothers = np.repeat(fem, cnt)
        J = len(mothers)
        if J == 0:
            return dict(extinct=True, lag=np.nan, Nfrac=0.0)
        fathers = mal[rng.integers(0, len(mal), J)]
        ar = np.arange(n)
        gm = G[mothers[:, None], ar[None, :], rng.integers(0, 2, (J, n))]
        gf = G[fathers[:, None], ar[None, :], rng.integers(0, 2, (J, n))]
        child = np.stack([gm, gf], axis=2)
        if u > 0:
            # LIFE CYCLE (review fix): reproduction -> mutation of the J juvenile gametes -> selection/regulation.
            # Per-gamete rate is rescaled to u*K/J so the juvenile cohort receives M = 2*K*u new mutations per
            # locus per generation under BOTH hard (J ~ K*f) and soft (J = R*N/2) regimes. Previously a flat u per
            # juvenile gamete made effective M = (J/K)*M, i.e. inflated by ~R/2 under soft selection.
            child += (rng.random((J, n, 2)) < u * K / J).astype(np.int8)
        astar = (t + 1 + off) // T          # optimum experienced by the juveniles (next generation)
        dev = np.abs(astar[None, :, None] - child).sum(axis=(1, 2))
        w = np.exp(dev * lns)
        if regime == "hard":
            keep = rng.random(J) < w
        else:
            if J <= K:
                keep = np.ones(J, dtype=bool)
            else:
                keys = -np.log(rng.random(J)) / w
                keep = np.zeros(J, dtype=bool)
                keep[np.argpartition(keys, K)[:K]] = True
        G = child[keep]
        N = len(G)
        if N < 4:
            return dict(extinct=True, lag=np.nan, Nfrac=0.0)
        sex = rng.integers(0, 2, N)
        Ns.append(N / K)
        # pre-shift lag of locus j: record at the last generation before its optimum increments
        if t >= burn * T:
            sh = ((t + 2 + off) // T) > astar          # optimum will increment for the next juveniles
            if sh.any():
                mean_allele = G.mean(axis=(0, 2))
                lags.extend((astar[sh] - mean_allele[sh]).tolist())
    lag = float(np.mean(lags)) if lags else np.nan
    return dict(extinct=False, lag=lag, Nfrac=float(np.mean(Ns[len(Ns) // 2:])))

def treadmill_success(**kw):
    out = treadmill_run(**kw)
    return (not out["extinct"]) and out["lag"] < 0.5, out

def gauss_run(K, n, T, R, u, regime, cycles, rng):
    """Nunney-2003-style fitness (RECONSTRUCTED; his Eq. 3 and 5 are lost in the text extraction):
    f = 2 exp(r(1-N/K)), r = ln(R/2) (hard) ; juvenile survival w = exp(-r * mean_j (Av_j - t/T)^2) where Av_j is the
    mean allele value at locus j and the optimum moves continuously, t/T. (A population fixed for allele A at
    t = (A+1)T has w = exp(-r) = 2/R, matching his 'w < exp(-r)' remark.) SOFT: same w, but K adults drawn
    from R*N/2 juveniles with prob proportional to w.
    Returns dict(extinct, dev2) with dev2 = mean over the last half of the run of adult mean squared deviation."""
    r = np.log(R / 2.0)
    N = K
    G = np.zeros((N, n, 2), dtype=np.int8)
    sex = rng.integers(0, 2, N)
    dev2 = []
    ar = np.arange(n)
    for t in range(cycles * T):
        fem = np.flatnonzero(sex == 1); mal = np.flatnonzero(sex == 0)
        if len(fem) == 0 or len(mal) == 0:
            return dict(extinct=True, dev2=np.nan)
        f = min(R, 2.0 * np.exp(r * (1 - N / K))) if regime == "hard" else R
        fl = np.floor(f)
        cnt = (fl + (rng.random(len(fem)) < (f - fl))).astype(np.int64)
        mothers = np.repeat(fem, cnt)
        J = len(mothers)
        if J == 0:
            return dict(extinct=True, dev2=np.nan)
        fathers = mal[rng.integers(0, len(mal), J)]
        gm = G[mothers[:, None], ar[None, :], rng.integers(0, 2, (J, n))]
        gf = G[fathers[:, None], ar[None, :], rng.integers(0, 2, (J, n))]
        child = np.stack([gm, gf], axis=2)
        if u > 0:
            # LIFE CYCLE (review fix): reproduction -> mutation of the J juvenile gametes -> selection/regulation.
            # Per-gamete rate is rescaled to u*K/J so the juvenile cohort receives M = 2*K*u new mutations per
            # locus per generation under BOTH hard (J ~ K*f) and soft (J = R*N/2) regimes. Previously a flat u per
            # juvenile gamete made effective M = (J/K)*M, i.e. inflated by ~R/2 under soft selection.
            child += (rng.random((J, n, 2)) < u * K / J).astype(np.int8)
        astar = (t + 1) / T
        Av = child.mean(axis=2)
        w = np.exp(-r * ((Av - astar) ** 2).mean(axis=1))
        if regime == "hard":
            keep = rng.random(J) < w
        elif J <= K:
            keep = np.ones(J, bool)
        else:
            keys = -np.log(rng.random(J)) / w
            keep = np.zeros(J, bool); keep[np.argpartition(keys, K)[:K]] = True
        G = child[keep]; N = len(G)
        if N < 4:
            return dict(extinct=True, dev2=np.nan)
        sex = rng.integers(0, 2, N)
        dev2.append(float(((G.mean(axis=2) - astar) ** 2).mean()))
    return dict(extinct=False, dev2=float(np.mean(dev2[len(dev2) // 2:])))

# ---------------------------------------------------------------- deleterious load IBM (H, part d)
def mutload_run(K, U, s, Fmax, regime, gens, rng, epistasis=0.0):
    """Each individual carries k deleterious mutations (genic, free recombination, infinite sites).
    Offspring k = Binomial(k_mum,1/2)+Binomial(k_dad,1/2)+Poisson(U) (U per diploid genome per generation).
    Fitness w = exp(-(s k + epistasis*s*k^2/2... )) -> w = exp(-s*k - e*k^2) (multiplicative if e=0).
    HARD: each female has Fmax offspring (f=min(Fmax, 2exp(ln(Fmax/2)(1-N/K)))), survive w.p. w.
    SOFT: each female has Fmax offspring, K adults drawn with prob ∝ w.
    Returns time-averaged (last third) N/K, mean w among adults, mean k. Extinct -> N/K=0.
    """
    k = rng.poisson(0.0, K)          # start mutation-free
    N = K
    rF = np.log(Fmax / 2.0)
    recN, recW, recK = [], [], []
    for t in range(gens):
        if N < 4:
            return dict(Nfrac=0.0, w=np.nan, kbar=np.nan, extinct=True)
        nf = N // 2
        if regime == "hard":
            f = min(Fmax, 2.0 * np.exp(rF * (1 - N / K)))
        else:
            f = Fmax
        fl = np.floor(f)
        J = int((fl * nf) + (rng.random(nf) < (f - fl)).sum())
        mum = rng.integers(0, N, J)
        dad = rng.integers(0, N, J)
        kc = rng.binomial(k[mum], 0.5) + rng.binomial(k[dad], 0.5) + rng.poisson(U, J)
        w = np.exp(-s * kc - epistasis * kc.astype(float) ** 2)
        if regime == "hard":
            keep = rng.random(J) < w
        else:
            if J <= K:
                keep = np.ones(J, bool)
            else:
                keys = -np.log(rng.random(J)) / np.maximum(w, 1e-300)
                keep = np.zeros(J, bool)
                keep[np.argpartition(keys, K)[:K]] = True
        k = kc[keep]
        N = len(k)
        if t >= gens * 2 // 3:
            recN.append(N / K); recW.append(np.mean(np.exp(-s * k - epistasis * k.astype(float) ** 2))); recK.append(k.mean())
    return dict(Nfrac=float(np.mean(recN)), w=float(np.mean(recW)), kbar=float(np.mean(recK)), extinct=False)

# ---------------------------------------------------------------- age-structured helpers (C2)
AGES = np.arange(0, 111)

def siler_hazard(scale, a1=0.15, b1=0.7, a2=0.004, a3=2.5e-5, b3=0.095):
    x = AGES + 0.5
    return scale * (a1 * np.exp(-b1 * x) + a2 + a3 * np.exp(b3 * x))

def e0_of(mu):
    l = np.concatenate([[1.0], np.exp(-np.cumsum(mu))])[:-1]
    Lx = l * (1 - np.exp(-mu)) / np.maximum(mu, 1e-12)
    return float(Lx.sum())

def life_table_for_e0(e0, **kw):
    sc = brentq(lambda c: e0_of(siler_hazard(c, **kw)) - e0, 0.05, 20)
    return siler_hazard(sc, **kw)

def fert_schedule(mu, a_lo=15, a_hi=45):
    """Constant fertility a_lo<=x<a_hi, scaled so that R0=1 (stationary)."""
    l = np.concatenate([[1.0], np.exp(-np.cumsum(mu))])[:-1]
    b = ((AGES >= a_lo) & (AGES < a_hi)).astype(float)
    b = b / (l * b).sum()
    return b

def lx_of(mu):
    return np.concatenate([[1.0], np.exp(-np.cumsum(mu))])[:-1]

def R0_of(mu, b):
    return float((lx_of(mu) * b).sum())

def euler_lotka_r(mu, b):
    """Solve sum_x l(x) b(x) exp(-r (x+1)) = 1. Convention (matches project_types/cohort_ibm): a mother in age
    class x gives birth during the step, the newborn appears in class 0 one step later, hence x+1."""
    l = lx_of(mu)
    f = lambda r: (l * b * np.exp(-r * (AGES + 1.0))).sum() - 1.0
    return brentq(f, -0.5, 0.5)

def gen_time(mu, b):
    l = lx_of(mu)
    return float(((AGES + 1.0) * l * b).sum() / (l * b).sum())

def day_d(mu, b):
    """Day's eq. 3.3 on the yearly grid: d = T * sum(mu l v)/sum(l v), v(x)=(1/l(x)) sum_{y>=x} l(y)b(y)."""
    l = lx_of(mu)
    lb = l * b
    tail = np.cumsum(lb[::-1])[::-1]
    v = np.where(l > 1e-12, tail / np.maximum(l, 1e-300), 0.0)
    T = gen_time(mu, b)
    # per-year mortality force via mu (hazard already per year)
    return T * float((mu * l * v).sum() / (l * v).sum()), T

def mean_cum_hazard(mu, b):
    """H_bar = sum_x l(x) b(x) H(x) / sum l b, H(x)=cumulative hazard to age x  (= -E[ln l] over mothers)."""
    l = lx_of(mu)
    H = np.concatenate([[0.0], np.cumsum(mu)])[:-1] + 0.5 * mu  # cumulative hazard at mid-class
    return float((l * b * H).sum() / (l * b).sum())

def project_types(mu_list, b_list, years, N0=1e6):
    """Deterministic two-type clonal projection, yearly; returns logit freq of type 1 vs year."""
    na = len(AGES)
    pops = []
    l0 = lx_of(mu_list[0])
    for _ in mu_list:
        pops.append(0.5 * N0 * l0 / l0.sum())
    out = []
    for yr in range(years):
        tot = sum(p.sum() for p in pops)
        out.append(np.log(pops[1].sum() / pops[0].sum()))
        new = []
        for p, mu, b in zip(pops, mu_list, b_list):
            births = (p * b).sum()
            surv = p * np.exp(-mu)
            q = np.empty(na)
            q[0] = births
            q[1:] = surv[:-1]
            new.append(q)
        pops = new
    return np.array(out)

def cohort_ibm(mu_list, b_list, years, N0, rng):
    """Stochastic age-class IBM (exact for independent individuals): survivors ~ Binomial, births ~ Poisson.
    Types are clonal lineages. Returns logit of type-1 frequency each year."""
    na = len(AGES)
    pops = []
    l0 = lx_of(mu_list[0])
    for _ in mu_list:
        pops.append(np.round(0.5 * N0 * l0 / l0.sum()).astype(np.int64))
    out = np.empty(years)
    for yr in range(years):
        out[yr] = np.log(pops[1].sum() / pops[0].sum())
        new = []
        for p, mu, b in zip(pops, mu_list, b_list):
            births = rng.poisson((p * b).sum())
            surv = rng.binomial(p, np.exp(-mu))
            q = np.empty(na, dtype=np.int64)
            q[0] = births
            q[1:] = surv[:-1]
            new.append(q)
        pops = new
    return out
