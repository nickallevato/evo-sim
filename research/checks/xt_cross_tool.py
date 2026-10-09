"""XT: cross-tool replication of the k-vs-mu and fixation-time results in fwdpy11 (THROWAWAY research check).

PLAN.md "Verification": "the k-vs-mu and fixation-time results are reproduced in both the numpy WF and SLiM/fwdpy11".
Only F2 had been cross-checked (f2_fwdpy11.py). This script re-does B0, B1/B1b/B1c, B3/B3b/B3c and B2a in
fwdpy11 (diploid, individual-based, tree-sequence engine), an implementation that shares no code with wf.py/wf2.py.

Run:  research/.venv/bin/python -I research/checks/xt_cross_tool.py <stage> [workers]
      stage in {smoke, b0n, b0s, b3, b1, b1b, b1c, fluct, cohort, all, analyze}   (default workers 6, never more)
      results -> research/checks/results/raw/xt_<stage>.json (chunk-level data + analysis), report -> stdout.
SLiM 4: NOT available on the workstation or na-workhorse (no binary on PATH on either; not built from source:
not trivial). So fwdpy11 0.24.7 is the independent tool. Overlapping generations are not expressible in fwdpy11
(see "NOT RUN" at the bottom of this docstring).

Model used. fwdpy11 DiploidPopulation, Wright-Fisher (both parents drawn with replacement, residual selfing
allowed), genome length 1, recombination PoissonInterval(0,1,R). Mutations are "selected" mutations with
S = 1e-10 (ConstantS refuses 0): neutral to ~1e-7 of 1/(4N); this is the only way to read fixation times,
because prune_selected=True + track_mutation_counts=True records (origin generation m.g, fixation generation)
for every fixation in pop.fixations / pop.fixation_times. Selected cases use ConstantS(0,1,1,2s,0.5), i.e.
fitness 1, 1+s, 1+2s (per-copy s; the F2 spec error, S=s giving half, is not repeated). Mutation rate U is per
gamete per generation, so 2 N_t U mutants arrive per generation, same as the numpy convention (U = genome-wide
rate). Offspring-variance cases: fecundity noise via Multiplicative(1, GaussianStabilizingSelection(opt 0, VS=1),
GaussianNoise(sd=sqrt(a))), i.e. w = exp(-z^2/2), z ~ N(0, a), redrawn per individual per generation (not
heritable; pure reproductive-variance noise). Estimates are ratio-of-sums over independent chunks (separate
seeds); SE and CI are BETWEEN-chunk (t, df = chunks-1), so linkage / shared-genealogy correlations are
honoured. P_fix = (fixations whose origin generation is in the arrival window) / (expected arrivals
2 N U G_arr in that window); unresolved mutants at the end are counted and reported.
Convention: a mutant arises as 1 copy in offspring generation g and fixes at generation g + t_fix (t_fix =
number of reproduction steps, as in wf.single_locus). Because numpy mutates and samples in the same step, the
empty-start expectation differs by one generation of F: fwdpy11 target U*sum_{u=0}^{T-1}F(u) (numpy sums 1..T).

PRE-REGISTERED PREDICTIONS (written before any run of the main stages; thresholds are |z| < 3 on the
between-chunk SE unless stated, plus the numpy values recorded in RESULTS.md / R4 files compared at combined SE):
 B0.1 neutral P_fix = 1/(2N), N = 50, 100, 200 (numpy: 0.009893 at N=50, 0.00246 at N=200).
 B0.2 neutral conditional mean t_fix = exact-chain value (3.935 N at N=50; ~3.98 N for N>=100; -> 4N);
      SD of t_fix = exact chain (diffusion 2.15 N; numpy 2.105 N, 2.108 N, i.e. ~2% under diffusion).
 B0.3 Kimura u(s,N), per-copy s: (N=100, s=.01) 0.020171; (500, .01) 0.019801; (1000, .005) 0.009950, tolerance
      |z|<3 OR |relative difference| <= 2%; the 2% allowance is the diffusion-vs-exact-diploid approximation,
      and a result that passes only by that allowance will be reported as such, not as MC agreement.
 B0.4 mean conditional beneficial t_fix = diffusion integral (5% tolerance, numpy: 698+-3 at N=500,s=.01 vs 703;
      1405+-9 at N=1000,s=.005 vs 1407), and well BELOW Day's (2/s)ln(2N) (1382; 3040). At Day's own N=1e4, s=.001:
      diffusion 8480 vs (2/s)ln(2N) = 19807; prediction: simulated within 10% of 8480 and below 19807 by >2x
      (n ~ 100, wide CI; the 10% allowance reflects the small number of fixations).
 B0.5 neutral k = U at equilibrium (burn-in 20N): k/U = 1 for N = 50, 100, 200.
 B1   N=100, U=0.5: empty-start fixations by T = U*sum_{u<T}F_X(u) (exact-chain F_X) at T = 200, 400, 1000,
      2000 (numpy 2.8, 41.3, 304.4, 802.5); equilibrium-start count = U*T (numpy 99.3, 198.5, 501.0, 1005.1).
 B1b  N0=500, U=0.04, T=12 N0: contraction to N0/5 cum/UT = 1.267 (numpy 1.259); expansion N0/5 -> N0 = 0.733
      (numpy 0.733); constant control 1.000.
 B1c  anc Ne 1.98e5 scaled to N_anc_sim = 500 (f=396, T=636 gens, wf2.schedule): K/UT H0 = 1.000, H1 = 3.984
      (numpy 3.986+-0.012), H2 = 3.905 (3.904), H3 = 3.984 (3.975); analytic = 1 + 4 dN/T. Excess, not deficit.
 B3   N=100, noise a in {0, 3, 15, 100} (predicted Ne/N = 1/(1+CV^2) = 1, .661, .348, .140; also measured by Monte
      Carlo offspring variance Vk, Ne=(4N-2)/(Vk+2)): P_fix = 1/(2N) at every Ne (P_fix*2N = 1), NOT 1/(2Ne)
      (Day's N/Ne would be 1.51, 2.87, 7.1); mean t_fix = 4 Ne within 10% (scales with Ne, not N); k/U = 1.
 B3b  fluctuating N, NON-overlapping (random {50,150}; cycle 40,60,90,135,160): k/U = 1 (B&L "do not affect").
 B3c(e) mutant born in cohort of sizes 25,40,61,82 diploids (then constant 82): P_fix*M_i = 1 for every cohort
      (numpy 0.989, 0.973, 1.018, 0.986), not M_i/164 (0.305, 0.488, 0.744, 1.000).
 B2a  fwdpy11 F_cond(G) = exact-chain F_cond(G) at G/N = 1, 1.5, 2, 4 (N=100; N=50, 200 too), so (G/N) ln F ->
      the exact-chain values (-5.78 at r=1, N=100); r=0.5 and below are too rare to sample (F ~ 1e-6) and are
      reported only as an upper bound. Day's exp(-pi^2 N/G) is an exponent, not a probability.
 AGREEMENT CRITERION: the claim "fwdpy11 reproduces numpy" holds for an item if fwdpy11 is within tolerance of the
 analytic/exact target AND within 3 combined SE of the recorded numpy value.
 WHAT A DISAGREEMENT WOULD MEAN.
  - For the CRITICS' side (k = mu for any N or Ne, P_fix = 1/(2N), Day's formula is the empty-start boundary
    case, Ne sets time not probability): a disagreement in B0/B3/B1-equilibrium would mean the repo's numpy WF
    (wf.py) has a bug or an unrecognised convention that the critics' rebuttal numbers inherit; the critic-side
    numbers (e.g. B3 table, B1c excess 1.9-4.0) would then need to be redone before use.
  - For DAY's side (k = mu N/Ne, a deficit of ~4Ne after any size history, t_fix = (2/s)ln(2N)): a disagreement
    with numpy in the direction of his formulas (P_fix = 1/(2Ne), equilibrium deficit, long t_fix) would be
    evidence that standard-theory outputs depend on implementation details he could cite; agreement in the
    direction of numpy means his formulas fail in an independent tool too, while the places where numpy
    CONFIRMED him (empty-start formula U*int F_X exact; Ne sets the time scale; the sign of B&L and expansion
    lag) would be confirmed in an independent tool as well.
  - A disagreement in one tool only is a bug in that tool until localised; it is never resolved by choosing
    whichever tool favours a side. Any post-run analysis change goes in a separate commit labelled "post hoc".
 NOT RUN (not expressible in fwdpy11 0.24.7): overlapping generations / survival fraction s>0 (B3b scenarios A1,
 A2, C1, C2, C1x3, C3 and B3c-e2; B&L eq. 3 with s>0); fwdpy11 is Wright-Fisher with discrete, non-overlapping
 generations (no nonWF/Moran model; SLiM 4 nonWF would be the tool). Those B3b rows stay numpy-only
 (verified there against B&L eq. 3, |z|<1.6) and remain a gap in cross-tool replication.
"""
import os, sys, time, json, zlib, copy, warnings, platform
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multiprocessing import Pool

import numpy as np
from scipy import stats
from scipy.stats import binom

import wf as W
import wf2 as W2

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
S_NEUTRAL = 1e-10          # ConstantS refuses 0; 4N*S << 1 for every N used
SIMPL = 100


def seed_of(*parts):
    return zlib.crc32("|".join(str(p) for p in parts).encode()) & 0x7FFFFFFF


# ----------------------------------------------------------------------------- fwdpy11 plumbing
def _fp():
    import fwdpy11, demes
    return fwdpy11, demes


def make_graph(sizes):
    """sizes[g] = diploid size in generation g (g = 0 is the initial population; offspring generation g has
    sizes[g]). Run-length encoded demes graph, burnin 0. final_generation = len(sizes)-1."""
    fwdpy11, demes = _fp()
    # generation 0 (the initial population) is always its own epoch: a demes graph's first epoch is the
    # ancestral one and counts as one forward generation however long it is declared.
    runs = [[int(sizes[0]), 1]]
    for z in sizes[1:]:
        z = int(z)
        if runs[-1][0] == z and len(runs) > 1:
            runs[-1][1] += 1
        else:
            runs.append([z, 1])
    n = len(sizes)
    b = demes.Builder()
    epochs, i0 = [], 0
    for z, L in runs:
        epochs.append(dict(start_size=z, end_time=n - i0 - L))
        i0 += L
    b.add_deme("A", epochs=epochs)
    return fwdpy11.ForwardDemesGraph.from_demes(b.resolve(), burnin=(n - 1 if len(runs) == 1 else 0), burnin_is_exact=True)


def make_params(graph, simlen, U, S2, R, noise_a=0.0):
    fwdpy11, _ = _fp()
    if noise_a > 0:
        gv = fwdpy11.Multiplicative(1.0, fwdpy11.GaussianStabilizingSelection.single_trait(
            [fwdpy11.Optimum(0.0, 1.0)]), fwdpy11.GaussianNoise(mean=0.0, sd=float(np.sqrt(noise_a))))
    else:
        gv = fwdpy11.Multiplicative(1.0)
    return fwdpy11.ModelParams(
        nregions=[], sregions=[fwdpy11.ConstantS(0, 1, 1, S2, 0.5)], recregions=[fwdpy11.PoissonInterval(0, 1, R)],
        rates=(0, U, None), gvalue=gv, demography=graph, simlen=simlen, prune_selected=True)


def evolve(pop, rng, graph, simlen, U, S2, R, noise_a=0.0):
    fwdpy11, _ = _fp()
    p = make_params(graph, simlen, U, S2, R, noise_a)
    fwdpy11.evolvets(rng, pop, p, max(1, min(SIMPL, simlen)), track_mutation_counts=True)


def fixations(pop):
    return np.array([m.g for m in pop.fixations], dtype=np.int64), np.array(pop.fixation_times, dtype=np.int64)


def run_const(N, U, G_arr, tail, R, S2, noise_a, seed):
    """Constant-N run of G_arr + tail generations from an empty population."""
    fwdpy11, _ = _fp()
    pop = fwdpy11.DiploidPopulation(N, 1.0)
    rng = fwdpy11.GSLrng(seed)
    gr = make_graph([N] * (G_arr + tail + 1))
    evolve(pop, rng, gr, G_arr + tail, U, S2, R, noise_a)
    assert pop.generation == G_arr + tail
    g0, ft = fixations(pop)
    unres = int(sum(1 for m in pop.mutations if m.g <= G_arr))
    return g0, ft, unres


# ----------------------------------------------------------------------------- tasks
def task_const(a):
    """B0 neutral / selected and B3 noise chunks. Returns small summaries."""
    N, U, G, tail, R, S2, na = a["N"], a["U"], a["G"], a["tail"], a["R"], a["S2"], a["noise_a"]
    g0, ft, unres = run_const(N, U, G, tail, R, S2, na, a["seed"])
    inwin = g0 <= G
    t = (ft - g0)[inwin]
    B = a.get("burn", 20 * N)
    nwin = int(((ft > B) & (ft <= G + tail)).sum())
    out = dict(a, nfix=int(inwin.sum()), lam=2.0 * N * U * G, unres=unres, nwin=nwin, lenwin=G + tail - B,
               tsum=float(t.sum()), tsq=float((t.astype(float) ** 2).sum()),
               hist=np.bincount(t).tolist() if len(t) else [])
    return out


def task_b1(a):
    N, U, B, T, R = a["N"], a["U"], a["B"], a["T"], a["R"]
    g0, ft, unres = run_const(N, U, B + T, 0, R, S_NEUTRAL, 0.0, a["seed"])
    return dict(a, ft=ft.tolist())


def _stage_pop(Nstart, U, burn, R, seed):
    fwdpy11, _ = _fp()
    pop = fwdpy11.DiploidPopulation(Nstart, 1.0)
    rng = fwdpy11.GSLrng(seed)
    evolve(pop, rng, make_graph([Nstart] * (burn + 1)), burn, U, S_NEUTRAL, R)
    return pop


def task_demog(a):
    """Burn-in at N_start (equilibrium), then each scenario (array of sizes for generations burn+1..burn+T) on a
    deep copy. Counts fixations occurring after the burn-in, split by origin (<= burn: ancestral; > burn: new)."""
    fwdpy11, _ = _fp()
    Ns, U, burn, R = a["Nstart"], a["U"], a["burn"], a["R"]
    pop0 = _stage_pop(Ns, U, burn, R, a["seed"])
    res = {}
    for k, (name, sizes) in enumerate(a["scen"].items()):
        pop = copy.deepcopy(pop0)
        rng = fwdpy11.GSLrng(seed_of(a["seed"], name))
        gr = make_graph([Ns] * (burn + 1) + [int(z) for z in sizes])
        evolve(pop, rng, gr, len(sizes), U, S_NEUTRAL, R)
        g0, ft = fixations(pop)
        m = ft > burn
        res[name] = dict(K=int(m.sum()), Kanc=int((m & (g0 <= burn)).sum()), Knew=int((m & (g0 > burn)).sum()),
                         T=len(sizes))
    return dict(seed=a["seed"], res=res)


def task_fluct(a):
    fwdpy11, _ = _fp()
    rng_np = np.random.default_rng(a["seed"])
    kind, U, burn, T, R = a["kind"], a["U"], a["burn"], a["T"], a["R"]
    n = burn + T
    if kind == "random2":
        sizes = rng_np.choice([50, 150], size=n + 1)
    elif kind == "cycle5":
        sizes = np.tile([40, 60, 90, 135, 160], n // 5 + 2)[: n + 1]
    else:
        sizes = np.full(n + 1, 100)
    pop = fwdpy11.DiploidPopulation(int(sizes[0]), 1.0)
    rng = fwdpy11.GSLrng(a["seed"])
    evolve(pop, rng, make_graph(sizes), n, U, S_NEUTRAL, R)
    g0, ft = fixations(pop)
    K = int(((ft > burn) & (ft <= n)).sum())
    arr = float((2 * sizes[burn + 1: n + 1] * U).sum())      # expected arrivals in the window (for information)
    return dict(kind=kind, seed=a["seed"], K=K, UT=U * T, arr=arr, meanN=float(sizes[burn + 1:].mean()))


def task_cohort(a):
    fwdpy11, _ = _fp()
    U, reps, tail = a["U"], a["reps"], a["tail"]
    seq = [25, 25, 40, 61, 82] + [82] * tail
    gr = make_graph(seq)
    cnt = np.zeros(4, dtype=np.int64)
    unres = 0
    for r in range(reps):
        pop = fwdpy11.DiploidPopulation(25, 1.0)
        rng = fwdpy11.GSLrng(seed_of(a["seed"], r))
        evolve(pop, rng, gr, 4, U, S_NEUTRAL, a["R"])
        evolve(pop, rng, gr, gr.final_generation - 4, 0.0, S_NEUTRAL, a["R"])
        g0, ft = fixations(pop)
        for c in range(4):
            cnt[c] += int((g0 == c + 1).sum())
        unres += len(pop.mutations)
    return dict(seed=a["seed"], reps=reps, U=U, cnt=cnt.tolist(), unres=unres)


def task_dispatch(a):
    return {"const": task_const, "b1": task_b1, "demog": task_demog, "fluct": task_fluct,
            "cohort": task_cohort}[a["task"]](a)


# ----------------------------------------------------------------------------- reference computations
def exact_chain(N, Gmax_mult=60):
    """Exact WF chain absorption at M=2N from 1 copy: returns F_cond(G) array (G=1..Gmax), mean, sd of t_fix|fix."""
    M = 2 * N
    st = np.arange(M + 1)
    P = binom.pmf(st[None, :], M, st[:, None] / M)
    v = np.zeros(M + 1)
    v[1] = 1.0
    Gmax = Gmax_mult * N
    cum = np.empty(Gmax)
    prev = 0.0
    pmf = np.empty(Gmax)
    for g in range(Gmax):
        v = v @ P
        cum[g] = v[M]
        pmf[g] = v[M] - prev
        prev = v[M]
    u = 1.0 / M
    t = np.arange(1, Gmax + 1)
    mean = float((t * pmf).sum() / pmf.sum())
    sd = float(np.sqrt((t ** 2 * pmf).sum() / pmf.sum() - mean ** 2))
    return cum / u, mean, sd, float(pmf.sum() * M)


def t_ci(vals, conf=0.95):
    vals = np.asarray(vals, float)
    n = len(vals)
    m = vals.mean()
    se = vals.std(ddof=1) / np.sqrt(n)
    h = stats.t.ppf(0.5 + conf / 2, n - 1) * se
    return m, se, m - h, m + h


def cp_ci(k, n, conf=0.95):
    lo = 0.0 if k == 0 else stats.beta.ppf((1 - conf) / 2, k, n - k + 1)
    hi = 1.0 if k == n else stats.beta.ppf(1 - (1 - conf) / 2, k + 1, n - k)
    return lo, hi


def line(name, est, se, target, extra=""):
    z = (est - target) / se if se > 0 else float("nan")
    return "%-52s %10.5g +- %-9.3g target %-10.5g z=%+5.2f %s" % (name, est, se, target, z, extra)


def zc(a, sa, b, sb):
    return (a - b) / np.hypot(sa, sb)


# ----------------------------------------------------------------------------- configurations
def cfg(stage, smoke):
    k = 0.02 if smoke else 1.0
    c = {}
    c["b0n"] = [dict(task="const", N=50, U=0.05, G=int(4e5 * k), tail=15 * 50, R=1.0, S2=S_NEUTRAL, noise_a=0.0, chunks=12),
                dict(task="const", N=100, U=0.025, G=int(6e5 * k), tail=15 * 100, R=1.0, S2=S_NEUTRAL, noise_a=0.0, chunks=12),
                dict(task="const", N=200, U=0.0125, G=int(3e5 * k), tail=15 * 200, R=1.0, S2=S_NEUTRAL, noise_a=0.0, chunks=12)]
    c["b0s"] = [dict(task="const", N=100, s=0.01, U=0.0025, G=int(2e5 * k), tail=3000, R=5.0, noise_a=0.0, chunks=12),
                dict(task="const", N=500, s=0.01, U=0.0005, G=int(1e5 * k), tail=4000, R=5.0, noise_a=0.0, chunks=12),
                dict(task="const", N=1000, s=0.005, U=0.00025, G=int(6e4 * k), tail=9000, R=5.0, noise_a=0.0, chunks=16),
                dict(task="const", N=10000, s=0.001, U=0.00002, G=int(1.5e4 * k), tail=50000, R=1.0, noise_a=0.0, chunks=8)]
    for x in c["b0s"]:
        x["S2"] = 2 * x["s"]
        x["tail"] = int(x["tail"] * max(k, 0.1))
    c["b3"] = [dict(task="const", N=100, U=0.025, G=int(1.5e5 * k), tail=1500, R=1.0, S2=S_NEUTRAL, noise_a=aa, chunks=12)
               for aa in (0.0, 3.0, 15.0, 100.0)]
    c["b1"] = [dict(task="b1", N=100, U=0.5, B=2000, T=2000, R=1.0, reps=int(120 * max(k, 0.05)))]
    c["b1b"] = [dict(task="demog", kind="b1b", N0=500, U=0.04, reps=int(48 * max(k, 0.05)))]
    c["b1c"] = [dict(task="demog", kind="b1c", N_anc_sim=500, U=0.04, reps=int(120 * max(k, 0.05)))]
    c["fluct"] = [dict(task="fluct", kind=kd, U=0.1, burn=2000, T=int(6000 * max(k, 0.1)), R=1.0, reps=int(24 * max(k, 0.1)))
                  for kd in ("const100", "random2", "cycle5")]
    c["cohort"] = [dict(task="cohort", U=1.0, reps=int(200 * max(k, 0.05)), tail=2500, R=1.0, chunks=max(2, int(30 * k)))]
    return c[stage]


def expand(stage, smoke):
    """Turn configurations into task dicts (one per chunk / replicate)."""
    tasks = []
    for ci, c in enumerate(cfg(stage, smoke)):
        t = c["task"]
        if t == "const":
            for i in range(c["chunks"]):
                d = {kk: vv for kk, vv in c.items() if kk != "chunks"}
                d.update(stage=stage, ci=ci, i=i, seed=seed_of("xt", stage, ci, i, smoke))
                tasks.append(d)
        elif t == "b1":
            for i in range(c["reps"]):
                d = dict(c, stage=stage, ci=ci, i=i, seed=seed_of("xt", stage, ci, i, smoke))
                tasks.append(d)
        elif t == "demog":
            for i in range(c["reps"]):
                if c["kind"] == "b1b":
                    N0, T = c["N0"], 12 * c["N0"]
                    cont = dict(stage=stage, ci=ci, i=i, task="demog", U=c["U"], R=1.0, Nstart=N0, burn=20 * N0,
                                seed=seed_of("xt", stage, "cont", i, smoke),
                                scen={"constant": np.full(T, N0), "contraction N0->N0/5": np.full(T, N0 // 5)})
                    expn = dict(stage=stage, ci=ci, i=i, task="demog", U=c["U"], R=1.0, Nstart=N0 // 5, burn=20 * N0 // 5,
                                seed=seed_of("xt", stage, "exp", i, smoke),
                                scen={"expansion N0/5->N0": np.full(T, N0)})
                    tasks += [cont, expn]
                else:
                    Nanc = c["N_anc_sim"]
                    anc = 1.98e5
                    f = anc / Nanc
                    pieces = {"H0 const at ancestral": [(0, anc)],
                              "H1 step to 1.0e4": [(0, 1.0e4)],
                              "H2 step to 1.5e4": [(0, 1.5e4)],
                              "H3 1e5 first half then 1e4": [(0, 1.0e5), (126_000, 1.0e4)]}
                    scen = {nm: W2.schedule(p, f, 252_000) for nm, p in pieces.items()}
                    tasks.append(dict(stage=stage, ci=ci, i=i, task="demog", U=c["U"], R=1.0, Nstart=Nanc, burn=20 * Nanc,
                                      seed=seed_of("xt", stage, i, smoke), scen=scen))
        elif t == "fluct":
            for i in range(c["reps"]):
                tasks.append(dict(c, stage=stage, ci=ci, i=i, seed=seed_of("xt", stage, ci, i, smoke)))
        elif t == "cohort":
            for i in range(c["chunks"]):
                tasks.append(dict(c, stage=stage, ci=ci, i=i, seed=seed_of("xt", stage, ci, i, smoke)))
    return tasks


def run_stage(stage, workers, smoke=False):
    tasks = expand(stage, smoke)
    # heaviest first for load balance (selected N=1e4 chunks are the slowest)
    tasks.sort(key=lambda d: -(d.get("N", 0) * (d.get("G", 0) + d.get("tail", 0))) if d["task"] == "const" else 0)
    t0 = time.time()
    out = []
    with Pool(workers) as pool:
        for r in pool.imap_unordered(task_dispatch, tasks):
            out.append(r)
            if len(out) % 10 == 0 or len(out) == len(tasks):
                print("  [%s] %d/%d done, %.0fs" % (stage, len(out), len(tasks), time.time() - t0), flush=True)
    return out


# ----------------------------------------------------------------------------- analysis
NUMPY = {
    "B0.1": {50: (0.009893, np.sqrt(0.009893 * 0.990107 / 4e5)), 200: (0.00246, np.sqrt(0.00246 * 0.99754 / 4e5))},
    "B0.2": {50: (3.908, 0.0335), 200: (4.006, 0.069)},
    "B0.3": {(100, 0.01): (0.019995, 3.1e-4), (500, 0.01): (0.019745, 3.1e-4), (1000, 0.005): (0.010225, 2.25e-4)},
    "B0.4": {(500, 0.01): (698, 3), (1000, 0.005): (1405, 9)},
    "B0.5": {50: (0.05018, 0.0014), 200: (0.04964, 0.0056)},
    "B1_emp": {200: (2.8, 0.2), 400: (41.3, 0.8), 1000: (304.4, 1.8), 2000: (802.5, 3.4)},
    "B1_eq": {200: (99.3, 1.5), 400: (198.5, 2.0), 1000: (501.0, 3.3), 2000: (1005.1, 4.3)},
    "B1c": {"H0 const at ancestral": (1.000, 0.005), "H1 step to 1.0e4": (3.986, 0.012), "H2 step to 1.5e4": (3.904, 0.011),
            "H3 1e5 first half then 1e4": (3.975, 0.011)},
    "B1b": {"constant": (0.996, None), "contraction N0->N0/5": (1.259, None), "expansion N0/5->N0": (0.733, None)},
    "B3": {1.0: (0.00250, 3.98), 1.99: (0.00257, 3.97), 4.94: (0.00248, 4.01)},
    "B3b": {"const100": (1.0016, 0.0049), "random2": (1.0006, 0.0061), "cycle5": (1.0092, 0.0067)},
    "B3c": [(0.989, 0.011), (0.973, 0.014), (1.018, 0.014), (0.986, 0.020)],
}


def chunks_of(res, ci):
    return sorted([r for r in res if r["ci"] == ci], key=lambda r: r["i"])


def pooled_tstats(ch):
    n = np.array([c["nfix"] for c in ch], float)
    tm = np.array([c["tsum"] / c["nfix"] for c in ch])
    wmean = (n * tm).sum() / n.sum()
    # between-chunk SE of the weighted mean (chunk sizes ~equal)
    se = tm.std(ddof=1) / np.sqrt(len(ch))
    tot_sq = sum(c["tsq"] for c in ch)
    sd = np.sqrt(tot_sq / n.sum() - wmean ** 2)
    sds = np.array([np.sqrt(c["tsq"] / c["nfix"] - (c["tsum"] / c["nfix"]) ** 2) for c in ch])
    return wmean, se, sd, sds.std(ddof=1) / np.sqrt(len(ch))


def pad_hist(ch, L=None):
    L = L or max(len(c["hist"]) for c in ch)
    H = np.zeros((len(ch), L))
    for i, c in enumerate(ch):
        h = np.array(c["hist"])[:L]
        H[i, : len(h)] = h
    return H


def analyze_b0n(res, lines, smoke=False):
    C = cfg("b0n", smoke)
    for ci, c in enumerate(C):
        N = c["N"]
        ch = chunks_of(res, ci)
        F, mean_ex, sd_ex, norm = exact_chain(N)
        lines.append("--- B0 neutral, N=%d (U=%g, %d chunks x %d arrival gens; exact chain mean %.4f N, SD %.4f N; chain mass %.5f)" %
                     (N, c["U"], len(ch), c["G"], mean_ex / N, sd_ex / N, norm))
        nf = sum(x["nfix"] for x in ch)
        unres = sum(x["unres"] for x in ch)
        p = np.array([x["nfix"] / x["lam"] for x in ch])
        m, se, lo, hi = t_ci(p)
        pe = sum(x["nfix"] for x in ch) / sum(x["lam"] for x in ch)
        ref = NUMPY["B0.1"].get(N)
        lines.append(line("B0.1 P_fix (n_fix=%d, unresolved=%d)" % (nf, unres), pe, se, 1 / (2 * N),
                          "CI95 [%.5g, %.5g]" % (lo - (m - pe), hi - (m - pe)) + (" numpy %.5g z_cross=%+.2f" % (ref[0], zc(pe, se, *ref)) if ref else "")))
        tm, tse, tsd, tsdse = pooled_tstats(ch)
        ref = NUMPY["B0.2"].get(N)
        lines.append(line("B0.2 mean t_fix/N", tm / N, tse / N, mean_ex / N, "CI95 [%.4f, %.4f]" % tuple((np.array(t_ci([x['tsum'] / x['nfix'] for x in ch])[2:]) / N)) +
                          (" numpy %.4g z_cross=%+.2f" % (ref[0], zc(tm / N, tse / N, *ref)) if ref else "")))
        lines.append(line("B0.2 SD t_fix/N", tsd / N, tsdse / N, sd_ex / N, "(diffusion 2.15)"))
        kr = np.array([x["nwin"] / (x["U"] * x["lenwin"]) for x in ch])
        m, se, lo, hi = t_ci(kr)
        ref = NUMPY["B0.5"].get(N)
        lines.append(line("B0.5 k/U at equilibrium (window >20N)", kr.mean(), se, 1.0, "CI95 [%.4f, %.4f]" % (lo, hi)))
        # B2a: F_cond(G)
        H = pad_hist(ch, max(len(F), max(len(x["hist"]) for x in ch)))
        for r in (0.5, 1, 1.5, 2, 3, 4):
            G = int(round(r * N))
            cnt = H[:, 1: G + 1].sum(axis=1)
            tot = H.sum(axis=1)
            k, n = int(cnt.sum()), int(tot.sum())
            est = k / n
            ex = F[G - 1]
            day = np.exp(-np.pi ** 2 / r)
            perc = cnt / tot
            if k >= 30:
                se = perc.std(ddof=1) / np.sqrt(len(ch))
                lo, hi = est - 2.2 * se, est + 2.2 * se
                lines.append("   B2a G/N=%-4g F_cond sim %.4g [%.4g,%.4g] (k=%d/%d)  exact %.4g  z=%+.2f  | r ln F: sim %+.3f exact %+.3f (Day exponent -9.870)  Day exp(-pi^2/r)=%.3g" %
                             (r, est, lo, hi, k, n, ex, (est - ex) / se, r * np.log(est), r * np.log(ex), day))
            else:
                lo, hi = cp_ci(k, n)
                lines.append("   B2a G/N=%-4g F_cond sim k=%d/%d  CP95 [%.3g,%.3g]  exact %.4g (expected count %.2f)  Day %.3g" %
                             (r, k, n, lo, hi, ex, ex * n, day))


def analyze_b0s(res, lines, smoke=False):
    C = cfg("b0s", smoke)
    for ci, c in enumerate(C):
        N, s = c["N"], c["s"]
        ch = chunks_of(res, ci)
        nf = sum(x["nfix"] for x in ch)
        unres = sum(x["unres"] for x in ch)
        p = np.array([x["nfix"] / x["lam"] for x in ch])
        pe = sum(x["nfix"] for x in ch) / sum(x["lam"] for x in ch)
        m, se, lo, hi = t_ci(p)
        u = W.kimura_u(N, s)
        ref = NUMPY["B0.3"].get((N, s))
        rel = (pe - u) / u
        z = (pe - u) / se
        ok = abs(z) < 3 or abs(rel) <= 0.02
        lines.append("--- B0.3/B0.4 selected N=%d s=%g (per-copy), %d chunks, U=%g" % (N, s, len(ch), c["U"]))
        lines.append(line("B0.3 u(s,N) (n_fix=%d, unresolved=%d)" % (nf, unres), pe, se, u,
                          "rel %+.2f%% %s CI95 [%.5g, %.5g]" % (100 * rel, "PASS" if abs(z) < 3 else ("PASS-by-2%-allowance" if ok else "FAIL"), lo - (m - pe), hi - (m - pe)) +
                          (" numpy %.5g z_cross=%+.2f" % (ref[0], zc(pe, se, *ref)) if ref else "")))
        tm, tse, tsd, _ = pooled_tstats(ch)
        diff = W.diffusion_cond_fix_time(N, s)
        day = 2 / s * np.log(2 * N)
        sto = 2 / s * (np.log(4 * N * s) + 0.5772)
        ref = NUMPY["B0.4"].get((N, s))
        lo, hi = t_ci([x["tsum"] / x["nfix"] for x in ch])[2:]
        lines.append(line("B0.4 mean t_fix", tm, tse, diff, "CI95 [%.0f, %.0f] rel %+.1f%%; Day (2/s)ln2N=%.0f (ratio Day/sim %.2f); (2/s)(ln4Ns+g)=%.0f" %
                          (lo, hi, 100 * (tm - diff) / diff, day, day / tm, sto) +
                          (" numpy %.0f+-%.0f z_cross=%+.2f" % (ref[0], ref[1], zc(tm, tse, *ref)) if ref else "")))


def vk_mc(N, a, rng, reps=3000):
    """Monte Carlo offspring variance per individual (two parent slots per offspring, fecundity-proportional)."""
    vs = []
    for _ in range(reps):
        z = rng.normal(0, np.sqrt(a), N) if a > 0 else np.zeros(N)
        w = np.exp(-z * z / 2)
        p = w / w.sum()
        vs.append(rng.multinomial(2 * N, p).var())
    return float(np.mean(vs))


def analyze_b3(res, lines, smoke=False):
    C = cfg("b3", smoke)
    rng = np.random.default_rng(20261011)
    for ci, c in enumerate(C):
        N, a = c["N"], c["noise_a"]
        ch = chunks_of(res, ci)
        cv2 = (1 + a) / np.sqrt(1 + 2 * a) - 1 if a > 0 else 0.0
        Ne_cv = N / (1 + cv2)
        vk = vk_mc(N, a, rng)
        Ne_v = (4 * N - 2) / (vk + 2)
        p = np.array([x["nfix"] / x["lam"] for x in ch])
        pe = sum(x["nfix"] for x in ch) / sum(x["lam"] for x in ch)
        m, se, lo, hi = t_ci(p)
        nf = sum(x["nfix"] for x in ch)
        lines.append("--- B3 offspring variance, N=%d, noise a=%g: CV^2=%.3f, Ne(CV)=%.1f, Vk(MC)=%.3f, Ne(Vk)=%.1f (Ne/N=%.3f)" %
                     (N, a, cv2, Ne_cv, vk, Ne_v, Ne_v / N))
        lines.append(line("P_fix*2N (martingale: 1; Day N/Ne = %.3f) n_fix=%d" % (N / Ne_v, nf), pe * 2 * N, se * 2 * N, 1.0,
                          "CI95 [%.4f, %.4f]; z vs Day: %+.1f" % ((lo - (m - pe)) * 2 * N, (hi - (m - pe)) * 2 * N, (pe * 2 * N - N / Ne_v) / (se * 2 * N))))
        tm, tse, _, _ = pooled_tstats(ch)
        lines.append(line("mean t_fix / (4 Ne(Vk))", tm / (4 * Ne_v), tse / (4 * Ne_v), 1.0, "t_fix/N=%.3f; Day-cens (t=4N) would be 1/(Ne/N)=%.2f" % (tm / N, N / Ne_v)))
        kr = np.array([x["nwin"] / (x["U"] * x["lenwin"]) for x in ch])
        m, se, lo, hi = t_ci(kr)
        lines.append(line("k/U at equilibrium (Day: N/Ne=%.2f)" % (N / Ne_v), kr.mean(), se, 1.0, "CI95 [%.4f, %.4f]" % (lo, hi)))


def analyze_b1(res, lines, smoke=False):
    c = cfg("b1", smoke)[0]
    N, U, B, T = c["N"], c["U"], c["B"], c["T"]
    F, mean_ex, sd_ex, _ = exact_chain(N, Gmax_mult=60)
    Ffull = np.concatenate([[0.0], F])            # F(u), u = 0..
    cumF = np.cumsum(Ffull)                        # sum_{u=0}^{T-1} F(u) = cumF[T-1]
    ft = [np.array(r["ft"]) for r in res]
    lines.append("--- B1 N=%d U=%g reps=%d (burn %d = 20N for the equilibrium window)" % (N, U, len(ft), B))
    for Tg in (200, 400, 1000, 2000):
        emp = np.array([(f <= Tg).sum() for f in ft], float)
        eq = np.array([((f > B) & (f <= B + Tg)).sum() for f in ft], float)
        pred_e = U * cumF[Tg - 1]
        pred_n = U * (Ffull[1: Tg + 1].sum())
        me, se_e, lo, hi = t_ci(emp)
        mq, se_q, lo2, hi2 = t_ci(eq)
        re_, rq = NUMPY["B1_emp"][Tg], NUMPY["B1_eq"][Tg]
        lines.append("T=%4d empty: %8.2f +- %-5.2f CI95[%.1f,%.1f]  Day U*intF(fwd conv.)=%.2f z=%+.2f (numpy-conv. %.2f; numpy sim %.1f z_cross=%+.2f; UT-4NU=%.1f)" %
                     (Tg, me, se_e, lo, hi, pred_e, (me - pred_e) / se_e, pred_n, re_[0], zc(me, se_e, *re_), max(U * (Tg - 4 * N), 0)))
        lines.append("        equil: %8.2f +- %-5.2f CI95[%.1f,%.1f]  U*T=%.1f z=%+.2f (numpy sim %.1f z_cross=%+.2f); deficit vs UT: %.1f%%" %
                     (mq, se_q, lo2, hi2, U * Tg, (mq - U * Tg) / se_q, rq[0], zc(mq, se_q, *rq), 100 * (U * Tg - mq) / (U * Tg)))


def analyze_demog(res, stage, lines, smoke=False):
    scen_vals = {}
    for r in res:
        for nm, d in r["res"].items():
            scen_vals.setdefault(nm, []).append(d)
    if stage == "b1b":
        c = cfg("b1b", smoke)[0]
        N0 = c["N0"]
        T = 12 * N0
        anal = {"constant": 1.0, "contraction N0->N0/5": 1 + 4 * (N0 - N0 // 5) / T, "expansion N0/5->N0": 1 - 4 * (N0 - N0 // 5) / T}
        lines.append("--- B1b N0=%d U=%g T=%d reps=%d" % (N0, c["U"], T, len(scen_vals["constant"])))
        for nm, vals in scen_vals.items():
            K = np.array([v["K"] for v in vals], float) / (c["U"] * T)
            m, se, lo, hi = t_ci(K)
            ref = NUMPY["B1b"][nm][0]
            lines.append(line(nm + " cum K/(UT)", m, se, anal[nm], "CI95 [%.3f, %.3f]; numpy %.3f (z_cross, no numpy SE: %+.2f using this SE only)" % (lo, hi, ref, (m - ref) / se)))
    else:
        c = cfg("b1c", smoke)[0]
        Nanc = c["N_anc_sim"]
        f = 1.98e5 / Nanc
        ends = {"H0 const at ancestral": 1.98e5, "H1 step to 1.0e4": 1.0e4, "H2 step to 1.5e4": 1.5e4, "H3 1e5 first half then 1e4": 1.0e4}
        lines.append("--- B1c (anc 1.98e5 -> N_anc_sim=%d, f=%.0f, U=%g) reps=%d" % (Nanc, f, c["U"], len(scen_vals["H0 const at ancestral"])))
        for nm, vals in scen_vals.items():
            T = vals[0]["T"]
            K = np.array([v["K"] for v in vals], float) / (c["U"] * T)
            Ka = np.array([v["Kanc"] for v in vals], float) / (c["U"] * T)
            Kn = np.array([v["Knew"] for v in vals], float) / (c["U"] * T)
            an = 1 + 4 * (1.98e5 - ends[nm]) / 252000
            m, se, lo, hi = t_ci(K)
            ref = NUMPY["B1c"][nm]
            lines.append(line(nm + " K/UT", m, se, an, "CI95 [%.3f, %.3f]; anc %.3f new %.3f; numpy %.3f+-%.3f z_cross=%+.2f" %
                              (lo, hi, Ka.mean(), Kn.mean(), ref[0], ref[1], zc(m, se, *ref))))


def analyze_fluct(res, lines, smoke=False):
    for kd in ("const100", "random2", "cycle5"):
        r = [x for x in res if x["kind"] == kd]
        k = np.array([x["K"] / x["UT"] for x in r])
        m, se, lo, hi = t_ci(k)
        ref = NUMPY["B3b"][kd]
        lines.append(line("B3b NON-overlap %s k/U (reps=%d, meanN=%.1f)" % (kd, len(r), np.mean([x["meanN"] for x in r])), m, se, 1.0,
                          "CI95 [%.4f, %.4f]; numpy %.4f+-%.4f z_cross=%+.2f" % (lo, hi, ref[0], ref[1], zc(m, se, *ref))))


def analyze_cohort(res, lines, smoke=False):
    sizes = [25, 40, 61, 82]
    lines.append("--- B3c(e) cohorts (non-overlap): P_fix*M_i, reps=%d" % sum(x["reps"] for x in res))
    for c in range(4):
        M = 2 * sizes[c]
        per = np.array([x["cnt"][c] / (x["reps"] * M * x["U"]) * M for x in res])
        m, se, lo, hi = t_ci(per)
        ref = NUMPY["B3c"][c]
        lines.append(line("cohort %d (M=%d) P_fix*M_i  [Day M_i/164 = %.3f]" % (c, M, M / 164), m, se, 1.0,
                          "CI95 [%.3f, %.3f]; numpy %.3f+-%.3f z_cross=%+.2f; unresolved total %d" % (lo, hi, ref[0], ref[1], zc(m, se, *ref), sum(x["unres"] for x in res))))


ANALYZERS = {"b0n": analyze_b0n, "b0s": analyze_b0s, "b3": analyze_b3, "b1": analyze_b1,
             "b1b": lambda r, l, s=False: analyze_demog(r, "b1b", l, s),
             "b1c": lambda r, l, s=False: analyze_demog(r, "b1c", l, s),
             "fluct": analyze_fluct, "cohort": analyze_cohort}
STAGES = ["b0n", "b0s", "b3", "b1", "b1b", "b1c", "fluct", "cohort"]


def provenance():
    import fwdpy11, demes, tskit, scipy
    return dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, fwdpy11=fwdpy11.__version__,
                demes=demes.__version__, tskit=tskit.__version__, host=platform.node(), platform=platform.platform(),
                slim="not available (no binary on workstation or na-workhorse; not built)")


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    workers = min(6, int(sys.argv[2]) if len(sys.argv) > 2 else 6)
    smoke = stage == "smoke"
    prov = provenance()
    print("XT cross-tool", json.dumps(prov), flush=True)
    stages = STAGES if stage in ("smoke", "all") else [stage]
    for st in stages:
        if stage == "analyze":
            continue
        t0 = time.time()
        res = run_stage(st, workers, smoke)
        lines = []
        ANALYZERS[st](res, lines, smoke)
        print("=== stage %s (%.0fs) ===" % (st, time.time() - t0))
        print("\n".join(lines), flush=True)
        if not smoke:
            with open(os.path.join(RAW, "xt_%s.json" % st), "w") as fh:
                json.dump(dict(prov=prov, stage=st, res=res, report=lines), fh, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    if stage == "analyze":
        for st in STAGES:
            p = os.path.join(RAW, "xt_%s.json" % st)
            if not os.path.exists(p):
                continue
            d = json.load(open(p))
            lines = []
            ANALYZERS[st](d["res"], lines, False)
            print("=== stage %s ===" % st)
            print("\n".join(lines))


if __name__ == "__main__":
    main()
