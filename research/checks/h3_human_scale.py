"""H3 (H-human): can the ADAPTIVE substitutions actually required on the human lineage be paid for under the
cost of selection, at human-like reproductive excess R, per-substitution cost D, deleterious load and linkage?
THROWAWAY research code (no simulator product code). Imports nothing from other check files (python -I drops
the script directory from sys.path); the diploid model extends h2_hard_selection_multilocus.run().
Run:   research/.venv/bin/python -I research/checks/h3_human_scale.py analytic|wfD|V|A|B|C|S|smoke
Seeds: numpy SeedSequence([SEED, stage_code, cell_index, rep])  -- never hash().
Output: research/checks/results/raw/h3_<stage>.jsonl (one JSON row per run) and h3_<stage>.out (stdout copy).

Written 2026-10-08, BEFORE any main run (only a <30 s smoke test, output discarded). Predictions below are fixed.

=====================================================================================================
CLAIMS UNDER TEST (verbatim; locators are the claim files in docs/research/claims/)
  H  (Day, Z18168236 Abstract): "Haldane calculated that mammals could fix no more than approximately one
      beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes
      on a population."
  H  (Day, Z18168236 s2.3): "The 10% selective mortality is a total budget for the population, not a per-locus
      allocation."
  H  (Day, Z18168236 s4.2): "Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations"
  H1 (Day, blog 2026-05-07 para 4): "Once corrected, Term 3 still limits adaptive substitution rate at ~10^-12,
      but total substitution rate is only governed by Terms 1 and 2"
  H8 (Day, Z19984826 s4.3): "ksel = smax . d / [2L . ln(2Ne)] = 1 . 0.45 / [2 . 3.1 x 10^9 . ln(6,600)] ...
      ~ 8.3 x 10^-12"  (= 0.0256 adaptive substitutions per genome per generation)
  H8 (Day, Z19984826 s3.3.1): "None of them raises smax above order unity, and the reason is the same in all
      three cases."  (truncation, soft selection, composite fitness)
  H5 (Hossjer, ally, 2026-09-14 p.3): "the number of fixations with a selective advantage along the supposed
      human lineage is far less than what equation (4) predicts, perhaps more in line with equation (3)."
  H2 (Nunney 2003, Discussion): "This relatively large population will become extinct if the environmental
      change requires allelic substitution faster than about every 300 generations"  (K=1e4, M=0.1)
  H7 (Keightley 2012, Abstract): "A genome-wide deleterious mutation rate of 2.2 seems higher than humans could
      tolerate if natural selection is "hard," but could be tolerated if selection acts on relative fitness
      differences between individuals or if there is synergistic epistasis."
  H6 (Nesslig20, 2026-10-05): "Haldane's reproductive cost limit does not apply to drift, but can it account for
      most of the genomic differences between humans and chimps?"
  Targets (GAP-01, docs/research/ledgers/gaps.md; all `derived:` there): adaptive count per lineage K_a:
      coding-only ~1.3e3-6e3 (alpha 0.1-0.2), up to ~1.2e4 (alpha 0.4 x 3e4); with noncoding adaptive share
      a_nc = 0 / 0.1% / 1% / 5%: ~3e3 / 2e4 / 1.7e5 / 9e5.  Day's requirements: 17.5M (A3b), 20M (A3), 205M (A3a).
  Time (claim files A1, A4, A4d, A3): 146,250 (Day 2025 d-adjusted), 202,500 (450,000 x 0.45), 252,000
      (MITTENS 3.0), 325,000 (2025), 450,000 (2019); 6-7 My at 20-29 y = 206,897-350,000.

MODEL (simulation layer; extends H2-hard to diploid, low R, deleterious background and a finite map)
  * K diploid adults (cap), N_t adults. Treadmill (Haldane's setting): the environment opens a new adaptive locus
    at Poisson(lam) per generation, at a uniform random map position; the ancestral allele now costs a factor
    exp(-s) PER COPY (log-additive: anc/anc exp(-2s), het exp(-s), der/der 1); 'inf' supply seeds ONE beneficial
    copy (p0 = 1/2N) and re-seeds a lost copy; finite supply (stage C): a waiting locus costs everyone exp(-2s)
    until a mutant arises (Nunney's M = 2Ku new copies per locus per generation, scaled by N/K).
  * Reproduction: J = f N juveniles, f = min(R, K/N) (ceiling regulation; the critics' compensatory-reproduction
    premise, see R4-H2-hard review).  Each juvenile has two distinct random parents (no selfing).
    Parents are chosen uniformly, except under SOFT load where parent weight ~ exp(-s_d k) (relative fecundity:
    selection changes who reproduces, not how many juveniles there are).
  * Gametes: map = 23 chromosomes of equal length (coarse; total 36.8 M = 23 x 1.6 M, inside the 35-38 M
    sex-averaged range of gaps.md GAP-04 / prior-art PA-21), Haldane map function (Poisson crossovers, no
    interference).  'free' = r = 0.5 between all loci and bins.  'short' = 23 x 0.16 M = 3.68 M (sensitivity only).
    Adaptive loci have exact positions.  Deleterious mutations are counted per haplotype per BIN (16 bins per
    chromosome: 0.1 M bins on the 36.8 M map; within a bin no recombination -> background selection somewhat
    OVERSTATED relative to a continuous map, the direction that favours Day).
  * Deleterious load: Poisson(U/2) new mutations per gamete, s_d = 0.02 each, multiplicative.  'hard' load:
    juvenile survival multiplied by exp(-s_d k).  'soft' load: relative-fecundity weighting only (above).
  * HARD viability for the adaptive part: juvenile survives with probability exp(-s * #ancestral copies at open
    loci [-2s per waiting locus]) [x exp(-s_d k) if load hard].  Extinct if N < 20 (as H2).
  Measured (after burn-in): persistence over the record window, extinction time, k_obs = fixations / gen,
  D_obs = sum_t(-ln mean_j exp(-s anc_j)) / fixations (adaptive cost only, in log-mean-fitness units),
  N/K, open loci, per-seed fixation probability p_fix = fixed/(fixed+lost) (compare Kimura 2s; BGS lowers it).
  Persistence CIs: Wilson 95%.  lam50 = interpolated lam at 50% persistence (bracket reported).

SCALING (audit rule E4).  N is scaled down (K = 1000; human Ne ~1e4-1e5).  Map length, s, s_d and U are NOT
  scaled (the r/s and U/map ratios that drive interference and background selection are kept at human values).
  N enters the cap through D ~ 2 ln(2N) (diploid, p0 = 1/2N).  That N-dependence is itself standard theory, so it
  is VALIDATED, not assumed: stage V runs K = 1000 and K = 4000 at the same R and reports D_obs(K) and the
  persistence of lam = x ln R / D_pred(K).  Extrapolation to human N uses D(N) only if V passes (see P-V).

PRE-REGISTERED PREDICTIONS (fixed before any main run)
  Notation: lam* = (ln R - U_hard) / D  (Nei 1971 / Felsenstein 1971 spacing n = -ln p0 / ln k, generalised to
  diploid D and a hard deleterious load; = H2-hard's ln R / D).  D_pred(K) = 2 ln(2K) (15.2 at K=1000; 18.0 at
  4000; 19.8 at 1e4; 24.4 at 1e5; 29.0 at 1e6.  Haldane's D = 30 needs p0 ~ 3e-7, i.e. N ~ 1.6e6).
  P-Std (standard theory / Nei-Felsenstein; the critics' side insofar as any critic made it):
    S1  D_obs = 2 ln(2N) within +-15% (K=1000: 13-17.5), independent of R and of s (s=0.01 vs 0.03 within 15%).
    S2  Wherever the population persists, k_obs = lam within 15% (no rate saturation below lam*).
    S3  Mean-field lam* is an UPPER bound: sweep load arrives in discrete packets (each costs D), so at low R the
        population is driven extinct by load fluctuations before the mean reaches ln R.  Predicted lam50/lam*
        (record window 10,000 gens, K=1000): 0.3-0.9 for R <= 1.2; 0.7-1.1 for R >= 1.5.  lam50 increases
        monotonically with R (roughly with ln R).
    S4  Linkage (36.8 M map, no load) changes lam50 by < 20% vs free recombination (few concurrent sweeps).
        With soft U = 2.2 on the map: p_fix lowered by background selection by 5-25% vs free; lam50 within 20%
        of the no-load value (re-seeding means BGS mostly does not enter D).  Short map (3.68 M): p_fix lowered
        by 25-60%; lam50 still within 30%.
    S5  Hard load subtracts: U_hard = 0.35 -> extinct at any lam for R = 1.2 (ln 1.2 = 0.18 < 0.35);
        lam50 ~ S3-factor x (ln R - 0.35)/D for R = 1.5, 2, 3.  U_hard = 2.2 -> extinct at R = 3 and at lam ~ 0
        (ln 3 < 2.2); R = 10 marginal (ln 10 - 2.2 = 0.10; N/K ~ 0.11); R = 20 persists at small lam.
    S6  Finite supply (Nunney M): D_eff ~ D + 1/M (waiting cost 2s x 1/(M x 2s)).  M = 1 -> ~16; M = 0.1 -> ~25.
        So lam50 at M = 0.1 is ~0.6x the infinite-supply value (Nunney's 'fixed cost rises as M falls').
    S7  Weak selection (part wfD, single-locus WF, conditioned on fixation): D(2Ns) ~ 2 ln(2N) for 2Ns >= 100
        (within 20%); D falls well below for 2Ns <= 10 (predicted D(2Ns=1) in 1.5-5; D(2Ns=10) in 5-11).
  P-Day (Day's model, read literally; operationalised in this model):
    D1  Haldane literal: the sustainable adaptive rate is ~1/300 = 0.0033 per generation regardless of R
        ("10% is a total budget"); parallelism does not raise it.  Falsified IN THIS MODEL if lam50 >= 2 x 1/300
        with Wilson lower bound of persistence > 0.5 at some R <= 3, or if lam50 rises with R.
    D2  Term 3 (H8's own pre-registered form): with hard selection and R = 2, sustainable rate = s_max d /
        (2 ln 2Ne) = 0.45 / (2 ln 2000) = 0.0296 at K = 1000 (d = 0.45), or 0.0658 with d = 1.  Standard
        predicts ln 2 / 15.2 = 0.046 x S3-factor.  The stage A grid includes lam = 0.0296 at every R.
    D3  Day-favourable outcomes that would count: lam50 at R = 1.05-1.1 at or below ~1/300 (this is ALSO what
        P-Std predicts at D = 30: ln 1.1 / 30 = 0.0032; at K = 1000, D ~ 15 gives 0.0063 x S3-factor), and any
        R at which load + cost exceed ln R (extinction).  These are reported as Day-favourable regardless.
  Flip (analytic, part 'analytic'): the required adaptive count K_a fits in T generations iff
        ln R >= U_hard + D K_a / T    i.e.  R_min = exp(U_hard + D K_a / T).
    Predicted from that formula before running: coding-only K_a (~3e3) at T = 252,000, D = 20: R_min ~ 1.27
    (soft load), so it FITS for R >~ 1.3; a_nc = 1% (1.7e5): R_min ~ e^13 -> does NOT fit for any plausible R;
    Day's 17.5M: R_min ~ e^1389 -> does not fit by any measure.  With U_hard = 2.2 added, even coding-only needs
    R >~ 11.  So the flip lies at noncoding adaptive share a_nc ~ 0.01-0.2% for R in 1.5-10 (D 10-30).
  FALSIFIERS (pre-stated):
    F-Std: S1 fails (D_obs outside 13-17.5 at K=1000), or lam50 does not increase with R, or persistence at
           lam >= 1.5 lam* in >= 50% of reps at any R (would mean the cap is not ln R / D).
    F-Day: D1 above; D2 if the observed R = 2 lam50 is outside 0.02-0.04 (D2 d=0.45 form) and outside
           0.05-0.08 (d=1 form).
    F-Scaling (P-V): D_obs(4000) - D_obs(1000) must be 2 ln 4 = 2.77 +- 1.0, and persistence at x = 0.5 of
           lam*(K) must hold at both K (>= 50%).  If not, no extrapolation to human N is made.
  Anything run after seeing results is labelled post hoc in results/R4-H3-human.md.
=====================================================================================================
"""
import os
import sys
import json
import math
import time
import numpy as np
from multiprocessing import Pool

SEED = 20261050
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
N_CHR = 23
CHR_BIG = 10.0          # chromosome offset in the global coordinate (> any chromosome length)
NB_PER_CHR = 16
EXT_N = 20


# =========================================================================================== analytic layer
def D_det(p0, s=0.01):
    """Deterministic diploid log-additive sweep cost: sum_t -ln wbar_t (wbar relative to der/der = 1),
    from p0 to 1 - p0, genic recursion p' = p / (p + q e^-s) (HWE).  ~ 2 ln(1/p0)."""
    p, D = p0, 0.0
    es = math.exp(-s)
    while p < 1 - p0:
        m = p + (1 - p) * es
        D += -2.0 * math.log(m)
        p = p / m
    return D


GENS = [("Day 2025 d-adj (325k x 0.45)", 146250), ("450k x 0.45 (TW-01)", 202500),
        ("6 My / 29 y", 206897), ("MITTENS 3.0 (6.3 My / 25 y)", 252000), ("Day 2025 (6.5 My / 20 y)", 325000),
        ("7 My / 20 y", 350000), ("Day 2019 (9 My / 20 y)", 450000)]
TARGETS = [("coding, alpha~0.1 low (GAP-01)", 1.3e3), ("coding+a_nc=0 (GAP-01 central)", 3e3),
           ("coding, alpha=0.2 high end (GAP-01)", 6e3), ("coding max (alpha 0.4 x 3e4)", 1.2e4),
           ("a_nc = 0.1% (GAP-01)", 2e4), ("a_nc = 1% (GAP-01)", 1.7e5), ("a_nc = 5% (GAP-01)", 9e5),
           ("Day SNV-only 17.5M (A3b)", 1.75e7), ("Day 20M (A3)", 2e7), ("Day 205M (A3a)", 2.05e8)]
DAYCOUNTS = [("Haldane + d, 146,250/300 (H)", 487), ("Haldane, 252,000/300", 840),
             ("Haldane, 450,000/300 (H5)", 1500), ("Term 3, 260,000 x 0.0256 (H1/H8)", 6650),
             ("Hossjer 'perhaps' eq.(3) (H5)", 15800)]


def analytic():
    out = {}
    print("== A0. Haldane D (deterministic, diploid log-additive, s=0.01): D = sum -ln wbar ~ 2 ln(1/p0)")
    rows = []
    for lab, p0 in [("N=1e3 new mut", 1 / 2e3), ("N=4e3", 1 / 8e3), ("N=1e4", 1 / 2e4), ("N=1e5", 1 / 2e5),
                    ("N=1e6", 1 / 2e6), ("standing p0=1e-2", 1e-2), ("standing p0=1e-3", 1e-3),
                    ("standing p0=1e-4", 1e-4), ("Haldane D=30 equiv p0=3e-7", 3e-7)]:
        d = D_det(p0)
        rows.append(dict(case=lab, p0=p0, D=d, two_ln=2 * math.log(1 / p0)))
        print(f"  {lab:28s} p0={p0:.2e}  D_det={d:6.2f}  2ln(1/p0)={2*math.log(1/p0):6.2f}")
    out["D"] = rows
    print("\n== A1. Nei/Felsenstein check (PA-07): n = -ln p0 / ln k, k = 1.1, p0 = 1e-4 ->",
          round(math.log(1e4) / math.log(1.1), 1), "generations;  252,000 /", round(math.log(1e4) / math.log(1.1), 1),
          "=", round(252000 / (math.log(1e4) / math.log(1.1))))
    print("   Haldane's 10% budget as ln R: -ln(0.9) =", round(-math.log(0.9), 4), " (R = 1/0.9 = 1.111); ln 1.1 =",
          round(math.log(1.1), 4))
    print("\n== A2. Sustainable adaptive substitutions per generation lam* = (ln R - U_hard)/D  [per lineage over 252,000 gens]")
    Rs = [1.05, 1.1, 1.2, 1.5, 2, 3, 5, 10, 20]
    caps = []
    for U in (0.0, 0.35, 2.2):
        print(f"  U_hard = {U}  ({'load soft' if U == 0 else 'load hard'})")
        print("    R     " + "  ".join(f"D={D:<2d} rate   per-252k" for D in (10, 20, 30)))
        for R in Rs:
            cells = []
            for D in (10, 20, 30):
                lam = (math.log(R) - U) / D
                caps.append(dict(U=U, R=R, D=D, lam=lam, per252k=lam * 252000))
                cells.append(f"{lam:8.5f} {lam*252000:9.0f}" if lam > 0 else f"{'extinct':>8s} {'-':>9s}")
            print(f"    {R:<5}  " + "  ".join(cells))
    out["caps"] = caps
    print("\n== A3. Required rate K_a / T (per generation), by target and generation count")
    print("    " + " ".join(f"{g[1]:>9d}" for g in GENS))
    req = []
    for lab, K in TARGETS + DAYCOUNTS:
        print(f"  {lab:38s} " + " ".join(f"{K/g[1]:9.2e}" for g in GENS))
        for g in GENS:
            req.append(dict(target=lab, K=K, T=g[1], rate=K / g[1]))
    out["req"] = req
    print("\n== A4. FLIP: minimum reproductive excess  R_min = exp(U_hard + D K_a / T); shown as R_min (or ln R_min if huge)")
    flips = []
    for T in (146250, 252000, 450000):
        for U in (0.0, 0.35, 2.2):
            print(f"  T = {T}, U_hard = {U}:   " + "   ".join(f"D={D}" for D in (10, 20, 30)))
            for lab, K in TARGETS:
                cells = []
                for D in (10, 20, 30):
                    lnR = U + D * K / T
                    flips.append(dict(target=lab, K=K, T=T, U=U, D=D, lnRmin=lnR))
                    cells.append(f"{math.exp(lnR):9.3g}" if lnR < 20 else f"ln={lnR:7.3g}")
                print(f"    {lab:38s} " + "  ".join(cells))
    out["flip"] = flips
    print("\n== A5. FLIP in the noncoding adaptive share: K_max = T (ln R - U)/D;  a_nc,max = (K_max - 3e3)/1.7e7")
    anc = []
    for T in (146250, 252000, 450000):
        for U in (0.0, 0.35):
            print(f"  T = {T}, U_hard = {U}")
            for R in (1.1, 1.5, 2, 3, 10):
                cells = []
                for D in (10, 20, 30):
                    Kmax = T * (math.log(R) - U) / D
                    a = (Kmax - 3e3) / 1.7e7
                    anc.append(dict(T=T, U=U, R=R, D=D, Kmax=Kmax, a_nc_max=a))
                    cells.append(f"K_max={Kmax:8.0f} a_nc<={100*a:7.3f}%" if Kmax > 0 else "    extinct              ")
                print(f"    R={R:<4} " + " | ".join(cells))
    out["a_nc"] = anc
    print("\n== A6. Day's own figures expressed in the same formula")
    print("  Haldane 1/300 = ln R / D at (D=30, R=e^0.1=1.105);  Term 3 0.0256/gen at Ne=3300 = 0.45/(2 ln 6600):"
          " equals ln R / D with D = 2 ln 2Ne = 17.6 and ln R = 0.45 (R = 1.57), or d=1: R = e = 2.72")
    print("  0.0256 x 252,000 =", round(0.0256 * 252000), "; 1/300 x 252,000 =", 840)
    json.dump(out, open(os.path.join(RAW, "h3_analytic.json"), "w"), indent=1)


# =========================================================================================== weak-selection D
def wf_D(N, S2N, reps, rng, s=None):
    """Single-locus diploid WF (genic, log-additive), 2N copies, start 1 copy; returns mean D conditioned on fixation,
    D = sum_t 2 s q_t (log-load relative to der/der).  Vectorised over replicates."""
    M = 2 * N
    s = S2N / M if s is None else s
    k = np.ones(reps, dtype=np.int64)
    cost = np.zeros(reps)
    alive = np.ones(reps, bool)
    fixed = np.zeros(reps, bool)
    es = math.exp(-s)
    t = 0
    while alive.any():
        p = k[alive] / M
        cost[alive] += 2 * s * (1 - p)
        pp = p / (p + (1 - p) * es)
        k[alive] = rng.binomial(M, pp)
        a_idx = np.flatnonzero(alive)
        fx = k[a_idx] == M
        ls = k[a_idx] == 0
        fixed[a_idx[fx]] = True
        alive[a_idx[fx | ls]] = False
        t += 1
    nf = int(fixed.sum())
    return dict(N=N, twoNs=S2N, s=s, reps=reps, nfix=nf, D_fix=float(cost[fixed].mean()) if nf else float("nan"),
                D_fix_sd=float(cost[fixed].std()) if nf else float("nan"),
                D_lost_mean=float(cost[~fixed].mean()), pfix=nf / reps,
                D_total_per_fix=float(cost.sum() / nf) if nf else float("nan"))


def wfD_stage():
    rows = []
    for i, (N, S) in enumerate([(1000, 1), (1000, 4), (1000, 10), (1000, 40), (1000, 100), (1000, 400),
                                (1000, 2000), (10000, 10), (10000, 100), (10000, 2000)]):
        rng = np.random.default_rng(np.random.SeedSequence([SEED, 9, i]))
        reps = 200000 if S <= 10 else 40000
        r = wf_D(N, S, reps, rng)
        r["D_pred_2ln2N"] = 2 * math.log(2 * N)
        rows.append(r)
        print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}), flush=True)
    with open(os.path.join(RAW, "h3_wfD.jsonl"), "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


# =========================================================================================== IBM
def make_map(kind):
    if kind == "free":
        Lc = 1.6
    elif kind == "map36":
        Lc = 1.6
    elif kind == "short":
        Lc = 0.16
    else:
        raise ValueError(kind)
    return Lc


def run(K, s, lam, R, U, load, linkage, gens, burn, rng, M_sup=None, s_d=0.02, max_open=3000):
    """One replicate.  load in {'none','soft','hard'}; linkage in {'free','map36','short'}."""
    Lc = make_map(linkage)
    free = linkage == "free"
    N = K
    G = np.zeros((0, 2 * N), dtype=np.uint8)          # adaptive loci x haplotypes (1 = beneficial)
    lpos = np.zeros(0)                                  # global coordinate of each segregating locus
    lchr = np.zeros(0, dtype=np.int64)
    t_open = []
    waiting = []                                        # finite supply: (t_open, pos, chr)
    use_bins = load != "none"
    B = N_CHR * NB_PER_CHR
    bchr = np.repeat(np.arange(N_CHR), NB_PER_CHR)
    bpos = bchr * CHR_BIG + (np.tile(np.arange(NB_PER_CHR), N_CHR) + 0.5) * (Lc / NB_PER_CHR)
    if use_bins:
        Dl = rng.poisson(U / (2 * s_d * B), size=(2 * N, B)).astype(np.uint16)
    soft_w = None
    if use_bins and load == "soft":
        kd0 = Dl.reshape(N, 2, B).sum(axis=(1, 2))
        soft_w = np.exp(-s_d * kd0)
    acc = dict(rec=0, La=0.0, Ld=0.0, nfrac=0.0, nopen=0.0)
    fixes_rec = 0
    n_fix = 0
    n_lost = 0
    n_seed = 0
    ttf = []
    ext = False
    t_ext = None
    mu_w = 0.0
    for t in range(burn + gens):
        rec = t >= burn
        # ---- environment opens loci
        nnew = rng.poisson(lam)
        for _ in range(nnew):
            c = int(rng.integers(N_CHR))
            x = c * CHR_BIG + rng.random() * Lc
            if M_sup is None:
                col = np.zeros((1, 2 * N), dtype=np.uint8)
                col[0, rng.integers(0, 2 * N)] = 1
                G = np.vstack([G, col])
                lpos = np.append(lpos, x)
                lchr = np.append(lchr, c)
                t_open.append(t)
                n_seed += 1
            else:
                waiting.append((t, x, c))
        if G.shape[0] + len(waiting) > max_open:
            ext, t_ext = True, t
            break
        # ---- reproduction
        f = min(R, K / N)
        J = int(f * N)
        J += int(rng.random() < f * N - J)
        if J < 2:
            ext, t_ext = True, t
            break
        if soft_w is not None:
            pw = soft_w / soft_w.sum()
            pa = rng.choice(N, size=J, p=pw)
            # second parent drawn with the same soft weights; redraw where equal to the first (no selfing)
            pb = rng.choice(N, size=J, p=pw)
            same = pb == pa
            while same.any():
                pb[same] = rng.choice(N, size=int(same.sum()), p=pw)
                same = pb == pa
        else:
            pa = rng.integers(0, N, J)
            pb = (pa + rng.integers(1, N, J)) % N
        par = np.empty(2 * J, dtype=np.int64)
        par[0::2] = pa
        par[1::2] = pb
        nG = 2 * J
        nl = G.shape[0]
        # ---- crossover origins for all points (bins + adaptive loci), sorted along the genome
        if use_bins:
            P = np.concatenate([bpos, lpos])
            C = np.concatenate([bchr, lchr])
        else:
            P, C = lpos, lchr
        npnt = len(P)
        if npnt > 0:
            order = np.argsort(P, kind="stable")
            Ps, Cs = P[order], C[order]
            if free:
                pfl = np.full(npnt, 0.5)
            else:
                d = np.diff(Ps)
                r = 0.5 * (1 - np.exp(-2 * d))
                r[Cs[1:] != Cs[:-1]] = 0.5
                pfl = np.concatenate([[0.5], r])
            flips = rng.random((nG, npnt), dtype=np.float32) < pfl.astype(np.float32)
            o_sorted = np.cumsum(flips, axis=1, dtype=np.uint8) & 1
            o = np.empty_like(o_sorted)
            o[:, order] = o_sorted
            hap = 2 * par[:, None] + o                 # nG x npnt haplotype index in parent generation
        if nl > 0:
            hl = hap[:, -nl:] if use_bins else hap
            Cg = G[np.arange(nl)[None, :], hl]          # nG x nl
            anc = 2 * nl - Cg.reshape(J, 2, nl).sum(axis=(1, 2), dtype=np.int64)
        else:
            Cg = np.zeros((nG, 0), dtype=np.uint8)
            anc = np.zeros(J, dtype=np.int64)
        anc = anc + 2 * len(waiting)
        logwa = -s * anc
        wa = np.exp(logwa)
        wbar_a = float(wa.mean())
        if use_bins:
            Dc = Dl[hap[:, :B], np.arange(B)[None, :]]
            nm = rng.poisson(U / 2, nG)
            tot = int(nm.sum())
            if tot:
                np.add.at(Dc, (np.repeat(np.arange(nG), nm), rng.integers(0, B, tot)), 1)
            kd = Dc.reshape(J, 2, B).sum(axis=(1, 2), dtype=np.int64)
            wd = np.exp(-s_d * kd)
            Ld = -math.log(float(wd.mean()))
            w = wa * wd if load == "hard" else wa
        else:
            Ld = 0.0
            w = wa
        keep = rng.random(J) < w
        surv = np.flatnonzero(keep)
        N = len(surv)
        if N < EXT_N:
            ext, t_ext = True, t
            break
        gidx = (2 * surv[:, None] + np.arange(2)[None, :]).ravel()
        G = np.ascontiguousarray(Cg[gidx].T) if nl > 0 else np.zeros((0, 2 * N), dtype=np.uint8)
        if use_bins:
            Dl = Dc[gidx]
            if load == "soft":
                soft_w = wd[surv]
        # ---- finite supply: mutation at waiting and segregating loci
        if M_sup is not None:
            mu = M_sup / (2 * K)
            if waiting:
                p_first = 1.0 - math.exp(-2 * N * mu)
                hit = rng.random(len(waiting)) < p_first
                if hit.any():
                    keepw = []
                    for wt, h in zip(waiting, hit):
                        if h:
                            col = np.zeros((1, 2 * N), dtype=np.uint8)
                            col[0, rng.integers(0, 2 * N)] = 1
                            G = np.vstack([G, col])
                            lpos = np.append(lpos, wt[1])
                            lchr = np.append(lchr, wt[2])
                            t_open.append(wt[0])
                            n_seed += 1
                        else:
                            keepw.append(wt)
                    waiting = keepw
            if G.shape[0] > 0:
                nold = 2 * N - G.sum(axis=1, dtype=np.int64)
                nmu = rng.binomial(nold, mu)
                for j in np.flatnonzero(nmu):
                    idx = np.flatnonzero(G[j] == 0)
                    G[j, rng.choice(idx, size=min(int(nmu[j]), len(idx)), replace=False)] = 1
        # ---- fixation / loss
        if G.shape[0] > 0:
            cnt = G.sum(axis=1, dtype=np.int64)
            fixed = cnt == 2 * N
            lost = cnt == 0
            if fixed.any() or lost.any():
                keep_rows = []
                for j in range(G.shape[0]):
                    if fixed[j]:
                        n_fix += 1
                        fixes_rec += int(rec)
                        ttf.append(t - t_open[j])
                    elif lost[j]:
                        n_lost += 1
                        if M_sup is None:
                            G[j, rng.integers(0, 2 * N)] = 1
                            n_seed += 1
                            keep_rows.append(j)
                        else:
                            waiting.append((t_open[j], lpos[j], lchr[j]))
                    else:
                        keep_rows.append(j)
                kr = np.array(keep_rows, dtype=np.int64)
                G = G[kr] if len(kr) else np.zeros((0, 2 * N), dtype=np.uint8)
                lpos = lpos[kr] if len(kr) else np.zeros(0)
                lchr = lchr[kr] if len(kr) else np.zeros(0, dtype=np.int64)
                t_open = [t_open[j] for j in keep_rows]
        if rec:
            acc["rec"] += 1
            acc["La"] += -math.log(max(wbar_a, 1e-300))
            acc["Ld"] += Ld
            acc["nfrac"] += N / K
            acc["nopen"] += G.shape[0] + len(waiting)
    n = max(acc["rec"], 1)
    return dict(ext=ext, t_ext=t_ext, gens_rec=acc["rec"], k=fixes_rec / gens if not ext else fixes_rec / n,
                fixes_rec=fixes_rec, D=(acc["La"] / fixes_rec) if fixes_rec else float("nan"),
                La=acc["La"] / n, Ld=acc["Ld"] / n, nfrac=acc["nfrac"] / n, nopen=acc["nopen"] / n,
                pfix=n_fix / (n_fix + n_lost) if (n_fix + n_lost) else float("nan"), n_fix=n_fix, n_lost=n_lost,
                n_seed=n_seed, ttf=float(np.mean(ttf)) if ttf else float("nan"))


# =========================================================================================== grid
def Dpred(K):
    return 2 * math.log(2 * K)


def build(stage):
    """Cells: (stage, cell, K, s, lam, R, U, load, linkage, M_sup, x_label, reps, gens, burn)."""
    cells = []
    if stage == "V":
        for K, reps in ((1000, 6), (4000, 4)):
            for R in (1.1, 2.0):
                for x in (0.5, 1.0, 1.25):
                    lam = x * math.log(R) / Dpred(K)
                    cells.append((K, 0.01, lam, R, 0.0, "none", "free", None, f"x={x}", reps, 10000, 2000))
    if stage == "A":
        for R in (1.05, 1.1, 1.2, 1.5, 2.0, 3.0):
            lams = [(x * math.log(R) / Dpred(1000), f"x={x}") for x in (0.25, 0.5, 0.75, 1.0, 1.25)]
            lams += [(1 / 300, "1/300"), (0.45 / (2 * math.log(2000)), "Term3 d=.45")]
            for link in ("free", "map36"):
                for lam, lab in lams:
                    cells.append((1000, 0.01, lam, R, 0.0, "none", link, None, lab, 8, 10000, 2000))
    if stage == "B":
        for R in (1.1, 1.5, 2.0, 3.0):
            for x in (0.5, 1.0):
                lam = x * math.log(R) / Dpred(1000)
                cells.append((1000, 0.01, lam, R, 2.2, "soft", "map36", None, f"x={x}", 4, 8000, 1500))
        for x in (0.5, 1.0):
            lam = x * math.log(1.5) / Dpred(1000)
            cells.append((1000, 0.01, lam, 1.5, 2.2, "soft", "free", None, f"x={x}", 4, 8000, 1500))
            cells.append((1000, 0.01, lam, 1.5, 2.2, "soft", "short", None, f"x={x}", 4, 8000, 1500))
        cells.append((1000, 0.01, 0.0005, 1.2, 0.35, "hard", "map36", None, "lam=5e-4", 4, 8000, 1500))
        for R in (1.5, 2.0, 3.0):
            for x in (0.5, 1.0):
                lam = x * (math.log(R) - 0.35) / Dpred(1000)
                cells.append((1000, 0.01, lam, R, 0.35, "hard", "map36", None, f"xh={x}", 4, 8000, 1500))
        for R in (3.0, 10.0, 20.0):
            cells.append((1000, 0.01, 0.0005, R, 2.2, "hard", "map36", None, "lam=5e-4", 4, 8000, 1500))
        for x in (0.5, 1.0):
            lam = x * (math.log(20) - 2.2) / Dpred(1000)
            cells.append((1000, 0.01, lam, 20.0, 2.2, "hard", "map36", None, f"xh={x}", 4, 8000, 1500))
    if stage == "C":
        for R in (1.1, 1.5):
            for M in (1.0, 0.1):
                for x in (0.5, 1.0):
                    lam = x * math.log(R) / (Dpred(1000) + 1 / M)
                    cells.append((1000, 0.01, lam, R, 0.0, "none", "free", M, f"xM={x}", 6, 10000, 2000))
    if stage == "S":
        for R in (1.1, 2.0):
            for x in (0.5, 1.0):
                lam = x * math.log(R) / Dpred(1000)
                cells.append((1000, 0.03, lam, R, 0.0, "none", "free", None, f"x={x}", 6, 10000, 2000))
    if stage == "smoke":
        cells.append((1000, 0.01, 0.003, 1.1, 0.0, "none", "map36", None, "smoke", 1, 300, 50))
        cells.append((1000, 0.01, 0.01, 1.5, 2.2, "soft", "map36", None, "smoke", 1, 150, 50))
        cells.append((1000, 0.01, 0.01, 1.5, 0.35, "hard", "map36", None, "smoke", 1, 150, 50))
        cells.append((1000, 0.01, 0.01, 1.5, 0.0, "none", "free", 0.1, "smoke", 1, 300, 50))
    jobs = []
    code = {"V": 1, "A": 2, "B": 3, "C": 4, "S": 5, "smoke": 0}[stage]
    for ci, c in enumerate(cells):
        for rep in range(c[9]):
            jobs.append((stage, code, ci) + c + (rep,))
    return jobs


def job(a):
    stage, code, ci, K, s, lam, R, U, load, link, M, lab, reps, gens, burn, rep = a
    rng = np.random.default_rng(np.random.SeedSequence([SEED, code, ci, rep]))
    t0 = time.time()
    r = run(K, s, lam, R, U, load, link, gens, burn, rng, M_sup=M)
    r.update(dict(stage=stage, cell=ci, K=K, s=s, lam=lam, R=R, U=U, load=load, linkage=link, M_sup=M, x=lab,
                  rep=rep, gens=gens, burn=burn, sec=time.time() - t0, D_pred=Dpred(K),
                  lam_star=(math.log(R) - (U if load == "hard" else 0.0)) / Dpred(K)))
    return r


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def summarize(rows):
    import collections
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["stage"], r["cell"])].append(r)
    out = []
    for key in sorted(g):
        rs = g[key]
        r0 = rs[0]
        n = len(rs)
        nper = sum(not r["ext"] for r in rs)
        lo, hi = wilson(nper, n)

        def m(k, only_alive=False):
            v = [r[k] for r in rs if (not only_alive or not r["ext"]) and r[k] is not None
                 and not (isinstance(r[k], float) and math.isnan(r[k]))]
            return float(np.mean(v)) if v else float("nan")
        out.append(dict(stage=r0["stage"], cell=r0["cell"], K=r0["K"], s=r0["s"], R=r0["R"], U=r0["U"],
                        load=r0["load"], linkage=r0["linkage"], M_sup=r0["M_sup"], x=r0["x"], lam=r0["lam"],
                        lam_star=r0["lam_star"], lam_over_star=r0["lam"] / r0["lam_star"] if r0["lam_star"] > 0 else float("inf"),
                        reps=n, persist=nper / n, ci_lo=lo, ci_hi=hi,
                        k_over_lam=(m("k", True) / r0["lam"]) if nper else float("nan"),
                        D=m("D", True), D_all=m("D"), nfrac=m("nfrac", True), nopen=m("nopen"), La=m("La", True),
                        Ld=m("Ld"), pfix=m("pfix"), ttf=m("ttf"),
                        t_ext=float(np.mean([r["t_ext"] for r in rs if r["ext"]])) if nper < n else float("nan"),
                        sec=m("sec")))
    return out


def run_stage(stage, workers=8):
    jobs = build(stage)
    jobs.sort(key=lambda a: -(a[5] * a[13]))      # rough cost order (lam x gens) for load balance
    t0 = time.time()
    rows = []
    path = os.path.join(RAW, f"h3_{stage}.jsonl")
    with Pool(workers) as pool, open(path, "w") as f:
        for r in pool.imap_unordered(job, jobs, chunksize=1):
            rows.append(r)
            f.write(json.dumps(r) + "\n")
            f.flush()
    print(f"stage {stage}: {len(jobs)} runs, {time.time()-t0:.0f} s wall", flush=True)
    sm = summarize(rows)
    with open(os.path.join(RAW, f"h3_{stage}_summary.json"), "w") as f:
        json.dump(sm, f, indent=1)
    for x in sm:
        print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in x.items() if k not in ("stage",)},
              flush=True)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "analytic"
    os.makedirs(RAW, exist_ok=True)
    if which == "analytic":
        analytic()
    elif which == "wfD":
        wfD_stage()
    else:
        run_stage(which, workers=int(sys.argv[2]) if len(sys.argv) > 2 else 8)
