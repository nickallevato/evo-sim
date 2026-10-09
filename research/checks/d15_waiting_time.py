"""D15 -- Hossjer's prediction: the waiting time for coordinated regulatory changes "far exceeds" 9 My.

PRE-REGISTRATION.  Committed BEFORE any main run.  Stages: analytic | ds_moran | valid | sweep | all.
Run:  research/.venv/bin/python -I research/checks/d15_waiting_time.py <stage> [workers]
Heavy stages (valid, sweep) go to na-workhorse (<= 6 workers); analytic and ds_moran are light.

CLAIM (verbatim, Hossjer, MITTENS review PDF p.8, 2026-09-14, HO-12 in quotes-critics.md):
  "Although this mathematical model has not yet been applied to humans and chimps, my prediction is that the
   waiting time for several genes to change expression (so that their expressions match that of humans rather
   than chimps) far exceeds 9 million years."
MODEL he cites: Hossjer, Bechly & Gauger 2021, J Theor Biol 524:110657 (CC BY; local copy
  sources/raw/d15-hossjer2021/, untrusted, read-only).  Haploid Moran population of N, m genes, each with a
  regulatory sequence of L nt; a gene is "done" when a binding site of length W (K target words, <= dmax
  mismatches) is present; mutation prob mu per nt per generation; fitness s_h depends on the number h of genes
  done; backward mutations allowed with prob c; fixed-state approximation; T_m = time until all m are fixed.
  His default (Table 3): N=1e4, L=1000, m=1, mu=1e-8, c=1, W=6, K=1, dmax=0, neutral.  His Table 16 uses
  W=10, K=3, m=5, "valley" intermediates s_h = 0.9999.
9 My = 450,000 generations at 20 y, 360,000 at 25 y.  We report 25 y/generation (D&S 2008's human value) and 20 y.

DISCLOSURE.  Before this commit the analytic reproductions in stage `analytic` (Hossjer Tables 4, 5, 9 via the
  fixed-state chain; Durrett-Schmidt Theorem 1; Behe-Snoke rate model) were prototyped in scratch and their
  outputs seen.  They are baseline reproductions, not predictions.  The simulation engine was timed in smoke
  runs (outputs discarded).  Nothing in `ds_moran`, `valid` or `sweep` had been run for results.

BASELINES THAT MUST PASS FIRST (stage `analytic`, `ds_moran`):
  B1  Hossjer 2021 Table 4 (no-ST columns), 5 (W=6,8,10; dmax 0,1; m=1,2), 9 (K=2,3 dispersed, W=6,7)
      reproduced by the fixed-state phase-type chain to <= 1% (<= 2% for m=2 W=8,10 where the paper's C=2
      decomposition differs).
  B2  Durrett & Schmidt 2008 (preprint text, sources/raw/d15-durrett2008/): Theorem 1 E = 1/(2N u1 sqrt(u2));
      human case 8.66e6 generations (216 My at 25 y); with the 0.747 simulation ratio, 162 My; Drosophila
      34,600 generations; neutral-B factor 1/sqrt(beta) ~ 2236; Thm 4 factor ~2 at 1-r = 1e-4.
  B3  D&S Table 2 Sim/Pred ratios reproduced by an independent Moran implementation of their algorithm at
      n = 1000, 2000 replicates: case1 1.565, case2 1.15, case3 1.05, case4 1.00, case5 0.78, Drosophila 1.27;
      tolerance +-0.12 (SE ~ 0.03 plus their own Monte Carlo error).
  B4  Behe & Snoke 2004 (PMC2286568): required N for fixation of a lambda-site feature in 1e8 / 1e6 generations
      with v=1e-8, rho=1000, s=0.01: text values ~1e11 / 1e17 (lambda=3), ~1e22 / ~1e30 (lambda=6), >1e25
      (lambda=7).  Pass = within one order of magnitude of each text-read value.  Their abstract's
      "no less than 1e9" for 1e8 generations is a bound, not a value.
  B5  Lynch 2005 (PMC2253472): the large-N asymptote theta -> 2 N mu n/(20+n); n=50 gives 1.43e-6 N (text).
      His 10^6-yr headline rests on simulation figures that are not in the text; it is NOT numerically
      reproduced (stated as such), only compared qualitatively through the m=2 "final-only benefit" cells.
  Failure of B1-B3 stops the study (the engine or the transcription is wrong).

SIMULATION (numpy; fwdpy11 not used).  Haploid Wright-Fisher, M = 2*N_e gene copies (N_e = diploid effective
  size; neutral rates do not depend on N_e).  m genes; haplotype = bit mask of which genes are done; each gene
  has forward rate uf = kmult * 1.458e-8 per genome per generation (= mu * L0 * W * 4^-W for W=6, L=1000, K=1
  = Hossjer's k10 for his default) and back rate ub = 5.30e-8 (his k01; "c=1"; 0 for "c=0").  kmult is the
  redundancy axis: how many equivalent target words / precursor sites there are:
    1/12 (W=8 specific), 1 (Hossjer default, W=6 specific), 3 and 10 (any of K=3,10 dispersed sites),
    15 (one mismatch tolerated, W=6: uf = 2.19e-7), 30, 100 (region 1e5 nt, or many weak sites).
  Fitness depends on the number j of genes done (order of appearance arbitrary):
    N    neutral;  V4/V3/V2: intermediates 0<j<m have 1-1e-4 / 1e-3 / 1e-2 ("valley"), w_m = 1;
    Fin2/Fin3: only w_m = 1.01 / 1.001 ("target-selected", Hossjer eq. 96);
    S2/S3: stepping stones w_j = (1.01)^j / (1.001)^j.
  Recombination: rho = 0 (no recombination; asexual or tightly linked) or rho = 1 (offspring haplotype drawn
  from the product of allele frequencies = free recombination between genes).
  Start: all genes absent (a NEW feature, no standing variation; the D15 claim file's implicit assumption).
  Validation runs start from Hossjer's stationary distribution instead (P(done) = 1-exp(-E H0)).
  Event-driven: a monomorphic population jumps (geometric waiting time) to the next mutation arrival, then runs
  per-generation WF (selection, recombination, mutation, multinomial sampling) until monomorphic again.
  Statistics per cell (R replicates): p9 = P(T <= 9 My), p90 = P(T <= 90 My), p900, median, mean over finished;
  censored at 900 My (3.6e7 generations at 25 y); an exponential censored-MLE mean is reported only as a rough
  guide.  "Hossjer holds" = p9 <= 0.05; "far exceeds" (my convention, 10x) = p90 <= 0.05; "fails" = p9 >= 0.5.
  Scaling: N_e = 1e4 is run unscaled (M = 2e4); N_e = 1e5 is run with scale factor f = 10 (M = 2e4, mu*10,
  s*10, T/10 reported back x10).  Scale validity is TESTED in stage `valid`, not assumed.
  [Post hoc amendment 2026-10-09, see end of docstring: N_e = 1e5 S2/S3/Fin2/Fin3 cells run at f = 3.]

PREDICTIONS (written before the runs; "Hossjer-side model" = the 2021 fixed-state theory; "critic-side model" =
  Durrett-Schmidt / Lynch):
  P1  Hossjer-side: for his default spec (kmult=1) E[T_1] = 5.38e7 generations (1,345 My at 25 y), E[T_4] >= 2.2e8
      (c=0) to 2.4e9 (c=1); N_e-independent when neutral; valley s=0.9999 changes little.  Critic-side agrees
      on the arithmetic (D&S's own human number for a specific inactivate-then-create pair is 162-216 My) and
      differs only on whether the target is specific, whether intermediates are neutral, and whether N_e is
      large enough for stepping stones to be selected.
  P2  Neutral cells: p9 <= 0.05 for all m, N_e, rho whenever kmult <= 30.  At kmult = 100 and m = 1,
      E[T] = 6.9e5 generations (17 My): p9 ~ 0.4 (borderline; "far exceeds" fails).  Neutral p9 >= 0.5 needs
      kmult >~ 130 at m = 1 (so never reached in the grid), and is worse at m = 4.
  P3  Valley cells (V4, V3, V2) with kmult = 1: p9 = 0 (Hossjer's Table 16 shows valley ~ neutral).  Valley with
      N_e*d >> 1 (V3, V2 at N_e = 1e5; V2 at 1e4) is LONGER than neutral; stochastic tunneling makes it shorter
      than the single-mutation chain by a factor that grows with kmult.
  P4  Final-only benefit (Fin2, Fin3), kmult = 1, m >= 2: still p9 <= 0.05 at both N_e (neutral first steps
      plus tunneling, ~2e7 generations); at m = 1 Fin2 with N_e = 1e5, E[T] ~ 1.7e4 generations: FAILS.
  P5  Stepping stones S2 (1%/step), kmult = 1, independent genes, per-step mean 1/(M*uf*2s): N_e = 1e5, 1.7e4
      generations: p9 >= 0.99 for m <= 4 (FAILS); N_e = 1e4, 1.7e5 generations: p9 ~ 0.88 (m = 1) falling to
      ~ 0.6 (m = 4).  S3 (0.1%): N_e = 1e4, 1.7e6 per step: p9 ~ 0.19 (m = 1), <= 0.05 for m >= 2 (HOLDS);
      N_e = 1e5, 1.7e5 per step: same as S2 at N_e = 1e4 (p9 ~ 0.88 at m = 1, ~ 0.6 at m = 4).
  P6  kmult >= 10 with S2 (N_e = 1e5): p9 >= 0.99 for every m.  Fin2/Fin3 with m >= 3 and kmult <= 10: p9 <= 0.1
      (two or more neutral steps, ~1e7 generations).  Neutral steps at kmult = 30: m = 1 has mean 2.3e6
      generations (57 My).  So the flip from "holds" to "fails" is set by (kmult, selection on intermediates, N_e).
  P7  Recombination (rho = 1 vs 0): neutral cells differ by < 10%; valley and S cells at kmult >= 30 are shorter or
      equal with rho = 1 (assembly of singles); no cell is longer by > 25%.
  P8  Engine vs theory: neutral-cell sim means within +-15% of the chain (R=300, stationary start); scaling:
      neutral invariant within 10% across f = 1..100; valley cells with N_e*d >= 3 are LONGER at f = 10 than at
      f = 1 by > 30% (the tunneling parameter 2N*sqrt(u2) scales as 1/sqrt(f)); Fin/S cells within 25% for f <= 10.
  P9  Three-type tunneling check (A neutral, B selected, 1/sqrt(u2) << M << 1/u1): sim mean / Theorem 1 with
      2N = M within [0.5, 2]; deleterious A matches the Theorem 4 factor 1/R within the same band.
  What would change the verdict on D15 (external): a computed E[T_m] at kmult = 1 below 90 My for m >= 2 in a
  neutral or mildly deleterious valley (contradicts "far exceeds" even for the specific target); or p9 >= 0.5
  at kmult <= 3 with neutral/valley intermediates.  What would NOT: results for beneficial intermediates or
  kmult >= 30 -- those test the assumptions the prediction rests on (specific target, low-fitness intermediates),
  not its arithmetic.

Seeds: SeedSequence([20261090, stage, cell, rep]).  Outputs: results/raw/d15_<stage>.jsonl / .json / .out

POST HOC AMENDMENT (2026-10-09; made AFTER stage `valid` was run and seen, BEFORE any `sweep` run; own commit).
  Why: `valid` showed that scaling at f = 10 inflates strong selection.  At N_e = 1e4, S2 (m=2, kmult=1) gave
  mean 2.45e5 / 3.0e5 / 3.1e5 / 5.9e5 generations and p9 0.82 / 0.65 / 0.65 / 0.35 at f = 1 / 3 / 10 / 100
  (f = 10: +27%, outside P8's 25% band); Fin2 (m=2, kmult=3) was within ~25% to f = 10.  At f = 10 the
  selected cells' s = 0.01 becomes 0.1 in simulation units, which biases them long (conservative for Hossjer).
  Change: the N_e = 1e5 cells of the selected fitness classes S2, S3, Fin2, Fin3 run at f = 3 (M = 66,667,
  mu*3, s*3, cap 100*T9/3 generations, T reported x3); every other N_e = 1e5 cell stays at f = 10; N_e = 1e4
  stays unscaled.  M, the generation cap and the chain prediction all follow from f exactly as before
  (sweep_job reads f from scale_for()); each cell records its f.  Caveat stated in advance: f = 3 reduces but
  does not remove the bias (valid, N_e = 1e4: S2 at f = 3 was +23% in mean, p9 0.82 -> 0.65), so the
  N_e = 1e5 S/Fin cells remain biased long, i.e. conservative for Hossjer; the write-up must flag this.
  Wall guard: unchanged at 1500 s per cell.  Reason: `valid` timings put f = 3 cells at 3-4x their f = 10
  counterparts (Fin2 30 s vs 7 s; N 60 s vs 25 s; worst unscaled V3 m=3 cell 1543 s), so the f = 3 S/Fin cells
  (simulated span 1.2e7 generations, a third of an unscaled cell) are expected well inside 1500 s; any cell that
  hits the guard is censored at its clock and flagged by complete_at_900My as before.
  Scheduling only: the heaviest-first sort key now divides by f (no effect on results; seeds are per cell index).
  Predictions P1-P9 are NOT changed.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys
import json
import math
import time
from itertools import product
from math import comb, exp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
SEED = 20261090
MU = 1e-8
L_REG = 1000
GEN_Y = 25.0
T9 = 9e6 / GEN_Y            # 360,000 generations
T9_20 = 9e6 / 20.0          # 450,000 generations
UF0 = MU * (L_REG - 6 + 1) * 6 / 4 ** 6      # 1.458e-8 (Hossjer k10, W=6, K=1)
UB0 = UF0 * math.exp(-(L_REG - 5) / 4 ** 6) / (1 - math.exp(-(L_REG - 5) / 4 ** 6))   # k01 = 5.30e-8


# ----------------------------------------------------------------------------------------------------------
# Analytic parts
# ----------------------------------------------------------------------------------------------------------
def words(W, dmax, K=1, L=L_REG):
    """E(H0) (words already hitting), E(H1) (words one step further), forward rate k10 (Hossjer 2021, App. A)."""
    L0 = L - W + 1
    E0 = K * L0 * sum(comb(W, d) * 3 ** d for d in range(dmax + 1)) / 4 ** W
    E1 = K * L0 * comb(W, dmax + 1) * 3 ** (dmax + 1) / 4 ** W
    return E0, E1, MU * E1 * (dmax + 1) / 3


def hossjer_ET(m, W=6, dmax=0, K=1, c=1, order="arb"):
    """Expected T_m from the fixed-state (single-mutation, no-ST) neutral chain on j = genes done."""
    from scipy.stats import binom
    E0, E1, k10 = words(W, dmax, K)
    kap = exp(-E0)
    k01 = c * k10 * kap / (1 - kap)
    A = np.zeros((m, m))
    for j in range(m):
        fw, bw = (m - j) * k10, j * k01
        if j + 1 < m:
            A[j, j + 1] += fw
        if j > 0:
            A[j, j - 1] += bw
        A[j, j] -= fw + bw
    init = np.array([binom.pmf(j, m, 1 - kap) for j in range(m)])
    et = float(init @ np.linalg.solve(-A, np.ones(m)))
    if order == "fixed" and c == 0:
        et = m * kap / k10
    return et


def fixprob_safe(sig, M):
    if abs(sig) < 1e-14:
        return 1.0 / M
    a, b = -2 * sig, -2 * M * sig
    # P = (1 - e^a)/(1 - e^b), use logs
    if sig > 0:
        return -math.expm1(a) / (-math.expm1(b))
    # sig < 0: a, b > 0 ; P = (e^a - 1)/(e^b - 1)
    if b > 600:
        return math.expm1(a) * math.exp(-b)
    return math.expm1(a) / math.expm1(b)


def chain_ET(m, uf, ub, w, M, start=0):
    """Fixed-state single-mutation chain with fitness w[j]; M copies.  Returns E[T] to j = m from j = start."""
    A = np.zeros((m, m))
    for j in range(m):
        fw = max((m - j) * M * uf * fixprob_safe(math.log(w[j + 1] / w[j]), M), 1e-300)
        bw = (j * M * ub * fixprob_safe(math.log(w[j - 1] / w[j]), M)) if j > 0 else 0.0
        if j + 1 < m:
            A[j, j + 1] += fw
        if j > 0:
            A[j, j - 1] += bw
        A[j, j] -= fw + bw
    try:
        x = np.linalg.solve(-A, np.ones(m))
    except np.linalg.LinAlgError:
        return float("inf")
    return float(x[start]) if np.all(np.isfinite(x)) and x[start] > 0 else float("inf")


FIT = {
    "N": lambda m: [1.0] * (m + 1),
    "V4": lambda m: [1.0] + [1 - 1e-4] * (m - 1) + [1.0] if m > 1 else None,
    "V3": lambda m: [1.0] + [1 - 1e-3] * (m - 1) + [1.0] if m > 1 else None,
    "V2": lambda m: [1.0] + [1 - 1e-2] * (m - 1) + [1.0] if m > 1 else None,
    "Fin2": lambda m: [1.0] * m + [1.01],
    "Fin3": lambda m: [1.0] * m + [1.001],
    "S2": lambda m: [1.01 ** j for j in range(m + 1)],
    "S3": lambda m: [1.001 ** j for j in range(m + 1)],
}


def stage_analytic():
    out = {}
    print("== B1  Hossjer 2021 fixed-state chain vs printed tables ==")
    t4 = {  # (m): (c0 fixed, c0 arb, c1)  printed Table 4 'No ST'
        1: (5.3813e7, 5.3813e7, 5.3813e7), 2: (1.0763e8, 8.6522e7, 2.0548e8), 3: (1.6144e8, 1.0916e8, 6.9225e8),
        4: (2.1523e8, 1.2628e8, 2.3985e9), 5: (2.6906e8, 1.3999e8, 8.7385e9), 6: (3.2288e8, 1.5143e8, 3.3245e10)}
    rows = []
    for m, pr in t4.items():
        mine = (hossjer_ET(m, c=0, order="fixed"), hossjer_ET(m, c=0), hossjer_ET(m, c=1))
        for lab, a, b in zip(("c0 fixed", "c0 arb", "c1"), mine, pr):
            rows.append(dict(table="4", m=m, col=lab, mine=a, printed=b, ratio=a / b))
    t5 = [(6, 0, 1, 5.3813e7), (6, 0, 2, 2.0518e8), (6, 1, 1, 4.5271e4), (6, 1, 2, 9.0758e4), (8, 0, 1, 8.1257e8),
          (8, 0, 2, 2.8186e10), (8, 1, 1, 2.6897e7), (8, 1, 2, 8.2858e7), (10, 0, 1, 1.0571e10),
          (10, 0, 2, 5.5986e12), (10, 1, 1, 3.8057e8), (10, 1, 2, 7.1473e9)]
    for W, d, m, pr in t5:
        mine = hossjer_ET(m, W=W, dmax=d, c=1)
        rows.append(dict(table="5", W=W, dmax=d, m=m, mine=mine, printed=pr, ratio=mine / pr))
    t9 = [(6, 0, 2, 2.11e7), (6, 0, 3, 1.10e7), (6, 1, 2, 2.24e2), (6, 1, 3, 1.48e0), (7, 0, 2, 1.04e8),
          (7, 0, 3, 6.54e7), (7, 1, 3, 7.95e4)]       # K = 2,3 maximally dispersed
    for W, d, K, pr in t9:
        mine = hossjer_ET(1, W=W, dmax=d, K=K, c=1)
        rows.append(dict(table="9", W=W, dmax=d, K=K, mine=mine, printed=pr, ratio=mine / pr))
    for r in rows:
        print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items()})
    worst = max(abs(r["ratio"] - 1) for r in rows)
    print(f"B1 worst |ratio-1| = {worst:.4f}")
    out["B1"] = dict(rows=rows, worst=worst)

    print("\n== B2  Durrett & Schmidt 2008 (preprint) headline numbers ==")
    def thm1(n, u1, u2, beta=1.0):
        return 1.0 / (n * u1 * math.sqrt(beta * u2))
    h = thm1(2e4, 1e-7, 3.3e-9)
    dro = thm1(5e6, 1e-7, 3.3e-9)
    b2 = dict(human_gens=h, human_My_25y=h * 25 / 1e6, human_My_25y_x0p747=h * 0.747 * 25 / 1e6,
              dros_gens=dro, dros_years_10gy=dro / 10, dros_neutralB_factor=1 / math.sqrt(2e-7),
              dros_neutralB_My=dro * 1.25 / math.sqrt(2e-7) / 10 / 1e6, dros_beta1e4_years=dro * 1.25 / math.sqrt(1e-4) / 10,
              thm4_factor_1mr_1e4=1 / (0.5 * (math.sqrt((1e-4 / math.sqrt(3.3e-9)) ** 2 + 4) - 1e-4 / math.sqrt(3.3e-9))),
              behe_CCC_gens=thm1(1e6, 1e-9, 1e-9), behe_sqrt_u2_factor=1 / math.sqrt(1e-9))
    for k, v in b2.items():
        print(f"  {k:28s} {v:.6g}")
    out["B2"] = b2

    print("\n== B4  Behe & Snoke 2004 rate model (CTMC reading of their text; see docstring) ==")
    import mpmath as mp
    mp.mp.dps = 60

    def Hcum(lam, rho, v, T):
        n = lam
        rho, v, T = mp.mpf(rho), mp.mpf(v), mp.mpf(T)
        A = mp.zeros(n + 1, n + 1)
        hit = v / (1 + rho)
        for k in range(n):
            up = v * (lam - k) / (1 + rho); dn = v * k / (1 + rho); rs = v * lam * rho / (1 + rho)
            out_ = up
            A[k, k + 1 if k + 1 < n else 0] += up
            if k > 0:
                A[k, k - 1] += dn; out_ += dn; A[k, 0] += rs; out_ += rs
            A[k, k] -= out_
        A[n - 1, n] = hit
        return mp.expm(A.T * T)[n, 0]
    text = {(3, 1e8): 1e11, (3, 1e6): 1e17, (6, 1e8): 1e22, (6, 1e6): 1e30, (7, 1e8): 1e25}
    bs = []
    for lam in (2, 3, 4, 5, 6, 7):
        for T in (1e8, 1e6):
            N = float(1 / (2 * mp.mpf("0.01")) / Hcum(lam, 1000, 1e-8, T))
            ref = text.get((lam, T))
            bs.append(dict(lam=lam, T=T, N_req=N, text=ref, ratio=(N / ref if ref else None)))
            print(f"  lambda={lam} T={T:.0e}: N_req = {N:.3g}" + (f"  (text ~{ref:.0e}; ratio {N/ref:.2f})" if ref else ""))
    out["B4"] = bs

    print("\n== B5  Lynch 2005 asymptote ==")
    th = 2 * 1e-6 * 50 / 70
    print(f"  theta/N at large N, n=50, mu=1e-6: {th:.4g}  (text: 1.43e-6)")
    out["B5"] = dict(theta_over_N=th)

    print("\n== Chain predictions for the sweep cells (single-mutation fixed-state; no ST, no recombination) ==")
    pred = {}
    for Ne, kmult, F, m in product((1e4, 1e5), (1 / 12, 1, 3, 10, 15, 30, 100), FIT.keys(), (1, 2, 3, 4)):
        w = FIT[F](m)
        if w is None:
            continue
        et = chain_ET(m, kmult * UF0, UB0, w, 2 * Ne)
        pred[f"{Ne:g}|{kmult:g}|{F}|{m}"] = et
    out["chain_pred"] = pred
    for Ne in (1e4, 1e5):
        for F in ("N", "V3", "Fin2", "S2"):
            print(f"  Ne={Ne:g} {F:5s} kmult=1: " + "  ".join(
                f"m={m}: {pred[f'{Ne:g}|1|{F}|{m}']:.3g}" for m in (1, 2, 3, 4) if f'{Ne:g}|1|{F}|{m}' in pred))
    print(f"  9 My = {T9:.3g} generations (25 y), {T9_20:.3g} (20 y)")
    json.dump(out, open(os.path.join(RAW, "d15_analytic.json"), "w"), indent=1, default=float)
    return out


# ----------------------------------------------------------------------------------------------------------
# Durrett & Schmidt 2008 algorithm, Moran, n = 2N haploids (their Section "Simulation results")
# ----------------------------------------------------------------------------------------------------------
def ds_moran(rng, n, u1, u2, R):
    k = np.zeros(R, dtype=np.int64)
    t = np.zeros(R)
    T = np.full(R, np.nan)
    act = np.arange(R)
    while act.size:
        kk = k[act]
        z = kk == 0
        if z.any():
            iz = act[z]
            t[iz] += rng.exponential(1.0 / (n * u1), iz.size)
            k[iz] = 1
            kk = k[act]
        fx = kk >= n
        if fx.any():
            ifx = act[fx]
            T[ifx] = t[ifx] + rng.exponential(1.0 / (n * u2), ifx.size)
        act = act[~fx]
        kk = kk[~fx]
        if act.size == 0:
            break
        kf = kk.astype(float)
        base = kf * (n - kf) / n
        pk, qk, rk = base + (n - kf) * u1, base, kf * kf / n
        tot = pk + qk + rk
        t[act] += rng.exponential(1.0, act.size) / tot
        u = rng.random(act.size) * tot
        up = u < pk
        down = (~up) & (u < pk + qk)
        selfr = ~(up | down)
        bq = (up | selfr) & (rng.random(act.size) < u2)
        if bq.any():
            T[act[bq]] = t[act[bq]]
        k[act[up]] += 1
        k[act[down]] -= 1
        act = act[~bq]
    return T


DS_CASES = {   # name: (u1, u2) as functions of n; published Sim/Pred at n = 1000 (Table 2)
    "case1": (lambda n: 1 / n, lambda n: (10 / n) ** 2, 1.565),
    "case2": (lambda n: 1 / (4 * n), lambda n: (10 / n) ** 2, 1.150),
    "case3": (lambda n: 1 / (10 * n), lambda n: (10 / n) ** 2, 1.048),
    "case4": (lambda n: 1 / (10 * n), lambda n: (4 / n) ** 2, 0.997),
    "case5": (lambda n: 1 / (10 * n), lambda n: (1 / n) ** 2, 0.781),
    "drosophila": (lambda n: 1 / (2 * n), lambda n: (10 / math.sqrt(3) / n) ** 2, 1.273),
}


def ds_job(a):
    name, n, R, ci = a
    u1f, u2f, pub = DS_CASES[name]
    u1, u2 = u1f(n), u2f(n)
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 2, ci, 0]))
    t0 = time.time()
    T = ds_moran(rng, n, u1, u2, R)
    pred = 1.0 / (n * u1 * math.sqrt(u2))
    return dict(stage="ds_moran", case=name, n=n, R=R, pred=pred, sim_mean=float(T.mean()),
                se=float(T.std(ddof=1) / math.sqrt(R)), ratio=float(T.mean() / pred), published_ratio=pub,
                sec=time.time() - t0)


def stage_ds_moran(workers):
    from multiprocessing import Pool
    jobs = [(nm, 1000, 2000, i) for i, nm in enumerate(DS_CASES)]
    with Pool(min(workers, 4)) as pool, open(os.path.join(RAW, "d15_ds_moran.jsonl"), "w") as f:
        rows = []
        for r in pool.imap_unordered(ds_job, jobs):
            rows.append(r)
            f.write(json.dumps(r) + "\n")
            f.flush()
            print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
    return rows


# ----------------------------------------------------------------------------------------------------------
# Wright-Fisher engine: event-driven, vectorised across replicates
# ----------------------------------------------------------------------------------------------------------
def feature_Q(m, uf, ub):
    H = 1 << m
    Q = np.zeros((H, H))
    for h in range(H):
        for i in range(m):
            Q[h, h ^ (1 << i)] = ub if (h >> i) & 1 else uf
    return Q


def wf_batch(rng, M, Q, w, rho, m, start, target, tmax, deadline=None):
    """Replicates run in lockstep.  Returns (T, clock): T=inf for unfinished; clock = final generation count."""
    R = len(start)
    H = Q.shape[0]
    qtot = Q.sum(1)
    Mut = Q.copy()
    Mut[np.arange(H), np.arange(H)] = 1 - qtot
    B = ((np.arange(H)[:, None] >> np.arange(m)[None, :]) & 1).astype(float) if (rho > 0 and m > 1) else None
    ev_cdf = np.cumsum(Q, axis=1) / np.where(qtot > 0, qtot, 1)[:, None]
    counts = np.zeros((R, H), dtype=np.int64)
    counts[np.arange(R), start] = M
    t = np.zeros(R)
    T = np.full(R, np.inf)
    active = np.arange(R)
    it = 0
    while active.size:
        it += 1
        if deadline is not None and (it & 1023) == 0 and time.time() > deadline:
            break
        c = counts[active]
        mono = c.max(1) == M
        hm = c.argmax(1)
        fin = mono & (hm == target)
        if fin.any():
            T[active[fin]] = t[active[fin]]
        keep = ~fin & (t[active] <= tmax)
        if not keep.all():
            active, c, mono, hm = active[keep], c[keep], mono[keep], hm[keep]
            if active.size == 0:
                break
        if mono.any():
            ia, hh = active[mono], hm[mono]
            lam = M * qtot[hh]
            dt = rng.geometric(-np.expm1(-lam))
            t[ia] += dt
            K = np.ones(ia.size, dtype=np.int64)
            big = rng.random(ia.size) < lam / 2.0
            if big.any():
                K[big] = 2 + rng.poisson(lam[big])
            u = rng.random(ia.size)
            h2 = np.minimum((ev_cdf[hh] < u[:, None]).sum(1), H - 1)
            counts[ia, hh] -= 1
            counts[ia, h2] += 1
            for j in np.flatnonzero(K > 1):
                for _ in range(K[j] - 1):
                    h3 = min(int(np.searchsorted(ev_cdf[hh[j]], rng.random(), side="right")), H - 1)
                    counts[ia[j], hh[j]] -= 1
                    counts[ia[j], h3] += 1
        poly = ~mono
        if poly.any():
            ip = active[poly]
            fw = counts[ip] * w[None, :]
            sp = fw / fw.sum(1, keepdims=True)
            if B is not None:
                marg = sp @ B
                pr = np.prod(np.where(B[None] == 1, marg[:, None, :], 1 - marg[:, None, :]), axis=2)
                sp = (1 - rho) * sp + rho * pr
            pp = np.clip(sp @ Mut, 0, None)
            pp /= pp.sum(1, keepdims=True)
            counts[ip] = rng.multinomial(M, pp)
            t[ip] += 1
    return T, t


def fit_vec(F, m, f=1.0):
    """Fitness by haplotype (popcount), selection coefficients multiplied by scale f."""
    wj = np.array(FIT[F](m), dtype=float)
    wj = np.exp(f * np.log(wj))
    pc = np.array([bin(h).count("1") for h in range(1 << m)])
    return wj[pc]


def summarize(T, clock, f, R):
    Tg = T * f
    fin = np.isfinite(Tg)
    cens = clock[~fin] * f
    s = dict(R=R, n_fin=int(fin.sum()),
             p9=float((Tg <= T9).sum() / R), p9_20=float((Tg <= T9_20).sum() / R),
             p90=float((Tg <= 10 * T9).sum() / R), p900=float((Tg <= 100 * T9).sum() / R),
             median=float(np.median(Tg)) if np.isfinite(np.median(Tg)) else None,
             mean_fin=float(Tg[fin].mean()) if fin.any() else None,
             min_censor_clock=float(cens.min()) if cens.size else None,
             total_time=float(np.where(fin, Tg, clock * f).sum()))
    s["complete_at_900My"] = bool(cens.size == 0 or cens.min() >= 100 * T9 * 0.999)
    return s


# ----------------------------------------------------------------------------------------------------------
# valid: engine validation (neutral vs chain; scaling; three-type tunneling check)
# ----------------------------------------------------------------------------------------------------------
def stationary_start(rng, m, R, W=6, K=1):
    E0 = K * (L_REG - W + 1) / 4 ** W
    pdone = 1 - math.exp(-E0)
    bits = rng.random((R, m)) < pdone
    return (bits * (1 << np.arange(m))[None, :]).sum(1).astype(int)


def valid_job(a):
    kind, ci, params = a
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 3, ci, 0]))
    t0 = time.time()
    if kind == "neutral":
        m, c, f, R = params["m"], params["c"], params["f"], params["R"]
        M = int(round(2e4 / f))
        uf, ub = UF0 * f, (UB0 * f if c else 0.0)
        Q = feature_Q(m, uf, ub)
        start = stationary_start(rng, m, R)
        T, clk = wf_batch(rng, M, Q, np.ones(1 << m), 0, m, start, (1 << m) - 1, 1e13)
        pred = hossjer_ET(m, c=c, order="arb")
        s = summarize(T, clk, f, R)
        s.update(kind=kind, m=m, c=c, f=f, pred_chain=pred, ratio=s["mean_fin"] / pred, sec=time.time() - t0)
        return s
    if kind == "scaling":
        F, m, kmult, f, R, Ne = params["F"], params["m"], params["kmult"], params["f"], params["R"], params["Ne"]
        M = int(round(2 * Ne / f))
        Q = feature_Q(m, kmult * UF0 * f, UB0 * f)
        w = fit_vec(F, m, f)
        start = np.zeros(R, dtype=int)
        T, clk = wf_batch(rng, M, Q, w, params.get("rho", 0), m, start, (1 << m) - 1, 100 * T9 / f,
                          deadline=time.time() + params.get("wall", 3000))
        s = summarize(T, clk, f, R)
        s.update(kind=kind, F=F, m=m, kmult=kmult, f=f, Ne=Ne, rho=params.get("rho", 0),
                 pred_chain=chain_ET(m, kmult * UF0, UB0, FIT[F](m), 2 * Ne), sec=time.time() - t0)
        return s
    if kind == "tunnel":     # three-type chain 0 -(u1)-> A -(u2)-> B ; B (log-fitness sig) fixes ; A fitness r
        u1, u2, sig, r, M, R = params["u1"], params["u2"], params["sig"], params["r"], params["M"], params["R"]
        Q = np.zeros((3, 3))
        Q[0, 1] = u1
        Q[1, 2] = u2
        w = np.array([1.0, r, math.exp(sig)])
        T, clk = wf_batch(rng, M, Q, w, 0, 1, np.zeros(R, dtype=int), 2, 1e12,
                          deadline=time.time() + params.get("wall", 3000))
        beta = fixprob_safe(sig, M)
        thm1 = 1.0 / (M * u1 * math.sqrt(beta * u2))
        rho_ = (1 - r) / math.sqrt(beta * u2) if r < 1 else 0.0
        Rf = 0.5 * (math.sqrt(rho_ ** 2 + 4) - rho_)
        fin = np.isfinite(T)
        return dict(kind=kind, params=params, n_fin=int(fin.sum()), mean=float(T[fin].mean()) if fin.any() else None,
                    thm1_2N_eq_M=thm1, thm4_factor=1 / Rf, thm_pred=thm1 / Rf, ratio=float(T[fin].mean() / (thm1 / Rf)),
                    sec=time.time() - t0)


def valid_cells():
    cells = []
    for m in (1, 2, 3, 4):
        for c in (0, 1):
            cells.append(("neutral", len(cells), dict(m=m, c=c, f=100.0, R=300)))
    # scaling: Ne = 1e4 ; f in 1,3,10,100 ; neutral / valley / final / steps
    for F, m, kmult in (("N", 2, 30), ("V4", 2, 30), ("V3", 2, 30), ("V2", 2, 30), ("Fin2", 2, 3), ("S2", 2, 1),
                        ("V3", 3, 30)):
        for f in (1.0, 3.0, 10.0, 100.0):
            cells.append(("scaling", len(cells), dict(F=F, m=m, kmult=kmult, f=f, R=60, Ne=1e4, rho=0)))
    # three-type tunnelling: 1/sqrt(u2) << M << 1/u1 ; M=2000, u1=1e-6, u2=1e-4, B fitness e^0.05
    for r in (1.0, 0.98):
        cells.append(("tunnel", len(cells), dict(u1=1e-6, u2=1e-4, sig=0.05, r=r, M=2000, R=60)))
    return cells


def run_pool(cells_or_jobs, fn, workers, path, order_key=None):
    from multiprocessing import Pool
    rows = []
    t0 = time.time()
    with Pool(workers) as pool, open(path, "w") as f:
        for r in pool.imap_unordered(fn, cells_or_jobs, chunksize=1):
            rows.append(r)
            f.write(json.dumps(r, default=float) + "\n")
            f.flush()
            print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k != "params"}, flush=True)
    print(f"{len(cells_or_jobs)} jobs, {time.time()-t0:.0f} s wall", flush=True)
    return rows


def stage_valid(workers):
    cells = valid_cells()
    # slow ones first
    cells.sort(key=lambda c: (c[0] != "scaling" or c[2]["f"] != 1.0))
    return run_pool(cells, valid_job, workers, os.path.join(RAW, "d15_valid.jsonl"))


# ----------------------------------------------------------------------------------------------------------
# sweep
# ----------------------------------------------------------------------------------------------------------
KMULTS = (1 / 12, 1.0, 3.0, 10.0, 15.0, 30.0, 100.0)
SCALE = {1e4: 1.0, 1e5: 10.0}
SELECTED_F3 = ("S2", "S3", "Fin2", "Fin3")     # post hoc amendment 2026-10-09 (see docstring)


def scale_for(Ne, F):
    """Scale factor f for a sweep cell: N_e = 1e5 selected classes at f = 3, else SCALE[Ne]."""
    if Ne == 1e5 and F in SELECTED_F3:
        return 3.0
    return SCALE[Ne]


def sweep_cells():
    cells = []
    for Ne, kmult, F, m, rho in product((1e4, 1e5), KMULTS, FIT.keys(), (1, 2, 3, 4), (0, 1)):
        if FIT[F](m) is None:
            continue
        if m == 1 and (F in ("S2", "S3")):      # identical to Fin2 / Fin3 at m = 1
            continue
        if m == 1 and rho == 1:
            continue
        cells.append(dict(Ne=Ne, kmult=kmult, F=F, m=m, rho=rho, R=60))
    return cells


def sweep_job(a):
    ci, cell = a
    Ne, kmult, F, m, rho, R = cell["Ne"], cell["kmult"], cell["F"], cell["m"], cell["rho"], cell["R"]
    f = scale_for(Ne, F)
    M = int(round(2 * Ne / f))
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 4, ci, 0]))
    t0 = time.time()
    Q = feature_Q(m, kmult * UF0 * f, UB0 * f)
    w = fit_vec(F, m, f)
    T, clk = wf_batch(rng, M, Q, w, rho, m, np.zeros(R, dtype=int), (1 << m) - 1, 100 * T9 / f,
                      deadline=time.time() + 1500)
    s = summarize(T, clk, f, R)
    s.update(cell, f=f, cell=ci, pred_chain=chain_ET(m, kmult * UF0, UB0, FIT[F](m), 2 * Ne), sec=time.time() - t0)
    return s


def stage_sweep(workers):
    cells = sweep_cells()
    jobs = list(enumerate(cells))
    # heaviest first: many mutation arrivals and long caps
    jobs.sort(key=lambda a: -(a[1]["kmult"] * a[1]["m"] / scale_for(a[1]["Ne"], a[1]["F"])))
    return run_pool(jobs, sweep_job, workers, os.path.join(RAW, "d15_sweep.jsonl"))


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "analytic"
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    os.makedirs(RAW, exist_ok=True)
    if stage in ("analytic", "all"):
        stage_analytic()
    if stage in ("ds_moran", "all"):
        stage_ds_moran(workers)
    if stage in ("valid", "all"):
        stage_valid(workers)
    if stage in ("sweep", "all"):
        stage_sweep(workers)
