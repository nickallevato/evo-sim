"""HF: H follow-ups (QUEUE item 8).  Four parts, one script, one pre-registration:
  HF-a  soft-selection rate LIMIT across R (including Wallace-type partly-hard selection, hardness h);
  HF-b  truncation selection and synergistic epistasis: does either lower the cost below H8's hard cap and
        Day's Term 3 at the same R?
  HF-c  binomial (Beta-posterior) intervals on the H-C2 T50 values and on the H8 lam50 values;
  HF-d  GAP-05: slightly deleterious fixations on the human lineage (Kimura flux over a sourced DFE).
THROWAWAY research code (no simulator product code).  Engine = H8's run() (h8_haldane_regime.py) generalised:
same treadmill (locus opens with one beneficial copy, re-seeded when lost, closes at fixation; s = 0.01 per
ancestral copy, log-additive, free recombination, diploid), plus modes "mix" (hardness h), "trunc" (truncation)
and a synergistic term b (w = exp(-s A - b A^2), A = ancestral copies over open loci).
Run:    research/.venv/bin/python -I research/checks/hf_followups.py smoke|main|ci|gap05|analyse [workers]
Seeds:  numpy SeedSequence([SEED, stage_code, cell_index, rep]); H-C2 reruns reuse the original seeds.
Output: research/checks/results/raw/hf_<stage>.jsonl / .out; `analyse` prints the tables for R4-HF.md.

Written 2026-10-10 BEFORE any run of this file (smoke included).  Predictions are fixed here; anything changed
after a run goes in a separate commit labelled "post hoc".

=====================================================================================================
TARGETS (verbatim; locators as in the claim files / quotes files)
  H  (Day, Z18168236 Abstract): "Haldane calculated that mammals could fix no more than approximately one
      beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes
      on a population."
  H8 (Day, Z19984826 s3.3.1): "None of them raises smax above order unity, and the reason is the same in all
      three cases."   (the three: truncation, soft selection, composite fitness)
  H8 (Day, Z19984826 s4.3): "ksel = smax . d / [2L . ln(2Ne)] = 1 . 0.45 / [2 . 3.1 x 10^9 . ln(6,600)] ...
      ~ 8.3 x 10^-12"   (Term 3; at simulation scale with d = 1: lam_T3(R) = s_max / (2 ln 2K), audit mapping
      s_max = ln R; literal s_max = 1 gives 1/(2 ln 2000) = 0.0658 at K = 1000)
  H7 (Keightley 2012, Abstract): "could be tolerated if selection acts on relative fitness differences between
      individuals or if there is synergistic epistasis."  (critic-side mechanism list, here applied to adaptive cost)
  GAP-05 Day (blog 2026-01-11 "The Drift Deathmarch", body): "At observed mutation rates and population sizes, the
      drift model fixes roughly 7.6 harmful mutations per actual generation. Using standard estimates for the
      damage caused by each mutation, collapse occurs in 9 generations—about 225 years."  and "Since 75% of all
      mutations are harmful, the genome accumulates damaging mutations three times faster than it accumulates
      neutral ones."
  GAP-05 ally (Hossjer, HO-11, PDF p6): "so that the overall fitness of the population declines over time and the
      population eventually (and quite rapidly) dies."
  DFE source (Boyko 2008, PLoS Genet, PMC2377339, Discussion): "the mean selection coefficient for newly arising
      mutations under the best-fit distributions is −0.058 for the lognormal and −0.029 for the gamma"; Methods:
      "We assume s and 2s are the selective disadvantage of heterozygotes and homozygous mutants"; Results:
      "proportion of nearly neutral mutations (|s|<0.0001) is tightly clustered around 28% in African Americans".
      Shape: Kim, Huber & Lohmueller 2017 (PMC5419480, Results): "(Boyko: α = 0.184, β = 2488; Fit∂a∂i: α = 0.179,
      β = 3161)".  Boyko Introduction: "gamma distributed with a shape parameter between 0.1 and 1".
  No sourced human BENEFICIAL DFE exists (refresh-2026-10-10b item 3).  Uricchio 2019 (abstract only): "estimate
      α = 0.135 in human protein-coding sequences, 72% of which is contributed by weakly adaptive variants".  HF
      therefore keeps H8's single s = 0.01 per copy (2Ns = 20 at K = 1000: "strong" in Uricchio's split) and adds a
      weak bracket s = 0.002 (2Ns = 4) in HF-a/HF-b at R = 1.111 and 2 only.  This is a BRACKET, not a DFE.

"HUMAN-REALISTIC R"
  No sourced net reproductive excess exists (R5-draft V17).  The grid brackets it: 1.111 (Haldane's 10%), 1.5,
  2 (Day's "twice as many descendants"), 3 (Day's TFR 6-8 upper end, H8), plus 1.05.  Every result is a curve in R.

MODEL / MODES (K adults at the ceiling; all modes share the treadmill)
  hard   : H8 hard, w = exp(-s A - b A^2) (b = 0 is H8).  J = f N, f = min(R, K/N); survive with prob w.
  mix(h) : J = R N juveniles (stochastic rounding); hard survival with prob w^h; if survivors > K, keep K by
           weighted sampling without replacement on w^(1-h) (Efraimidis-Spirakis), else keep all.  h = 0 is
           softJ (H8); h = 1 is hard selection followed by random culling to K (validation against H8 hard).
           Extinct if N < 20.  Wallace's soft/hard continuum; h is not sourced for humans (bracket).
  trunc  : J = R K juveniles; keep the K with the fewest ancestral copies (ties random).  N = K always; the
           selective death fraction is exactly 1 - 1/R (Maynard Smith 1968 / Kimura-Crow 1969 truncation).
  softWF : H8 softWF (R-free relative-fitness Wright-Fisher).
  Gather is chunked over loci (memory bound ~ nl x 2J bytes).
  Per run: alive at 10k/20k; k_obs; D_obs (sum -ln wbar / fixations, wbar of w = exp(-sA-bA^2) over juveniles);
  nopen (q1, q4); Crow's I; maxrel; failure type (extinct / backlog, nopen > max_open).
  SUCCESS rule (fixed now): hard and mix h = 1: alive to T (T = 10k primary, 20k secondary).  softJ (mix h = 0),
  mix 0 < h < 1, trunc and softWF additionally need k_obs/lam >= 0.9 and nopen_q4/nopen_q1 <= 1.15 over the recorded window (a run that is
  alive but backlogging is a failure).  lam50 = H8's estimator (first 0.5 crossing, log-linear) on the success
  fraction; "> top" if never crossed (censored by the grid or by max_open, reported as such).

STAGE main (K = 1000 unless stated; 20,000 generations, burn 5,000 (hard/syn burn 3,000))
  A soft limit : softJ (= mix h=0), trunc: R in {1.05, 1.111, 1.5, 2, 3}, lam in {0.0351, 0.1, 0.2, 0.4, 0.8, 1.6},
                 4 reps, max_open 5000.   softWF: same lam, 4 reps.
  A mix        : h in {0.1, 0.3}, R in {1.111, 2, 3}, lam in {0.0037, 0.0111, 0.0351, 0.1, 0.2, 0.4}, 4 reps.
  A valid      : mix h = 1, R in {1.111, 2}, lam = x ln R / Dref(1000), x in {0.45, 0.6, 0.8, 1.0, 1.25}, 6 reps.
  A K4000      : softJ and trunc, K = 4000, R in {1.111, 2}, lam in {0.1, 0.4, 1.6}, 3 reps, max_open 5000.
  A weak       : s = 0.002: softJ and trunc at R in {1.111, 2}, lam in {0.0351, 0.1, 0.2, 0.4}, 4 reps;
                 hard at R in {1.111, 2}, x in {0.3, 0.45, 0.6, 0.8, 1.0, 1.25}, 6 reps (40k gens: sweeps ~5x longer).
  B syn        : hard, R in {1.111, 2, 3}, b in {0, 2.5e-4, 1e-3, 4e-3}, x in {0.3, 0.45, 0.6, 0.8, 1.0, 1.25, 1.6, 2.0,
                 2.5} (lam = x ln R / Dref), 10 reps.  b = 0 is a fresh-seed H8 replicate.
STAGE ci (HF-c): rerun every H-C2 condition with its ORIGINAL seed (h_cost_of_selection.build(), h_nunney_gauss and
  _lowR seeds), record the per-T success counts, and check T50 reproduces the published value exactly.  Interval:
  per grid T draw p_T ~ Beta(k + 0.5, n - k + 0.5) (Jeffreys), recompute T50 with the original first-crossing rule,
  10,000 draws, 2.5/97.5 percentiles; draws with no crossing in the observed grid are right-censored and counted.
  The same interval on H8 lam50 (survival fraction per lam cell, raw/h8_main.jsonl, kscale16, kscale64) and on the
  D = 30 interval 30/(lam50 D_obs) with D_obs bootstrapped over persisting reps.
STAGE gap05 (HF-d), analytic with numerical integration over the DFE plus a per-site WF validation:
  DFE: gamma on |s| (heterozygote effect; homozygote 2s), shape a in {0.184 (primary), 0.1, 0.3}, mean 0.029.
  U_d (new deleterious mutations per haploid genome per generation): {0.3, 1, 3}; 3 = gaps.md GAP-05 upper end
  (8% constrained x 3.1e9 x 1.2e-8) with Boyko's nonsynonymous DFE applied to all constrained sites (extrapolation).
  Ne in {1e4 (parameters.yaml Ne_modern_human), 2e4}; T = 252,000 generations (Day).  Kimura u(s) =
  (1 - e^{-2s})/(1 - e^{-4 Ne s}) (B0.3), for a new mutation in N = Ne.  Back mutation rate mu/3 per site.
  Scenarios: S1 start at the optimum (all sites good; no back flux): substitutions and log-fitness decline sum 2|s|.
  S2 start at the mutation-selection-drift equilibrium at the same Ne: net decline (expected 0).
  S3 equilibrium at Ne_anc = 2.06e5 (Yoo 2025 HCB Ne 1.98e5 x 1.25/1.2, refresh-2026-10-10b s2), then Ne = 1e4 for T
     (linear flux; per-site relaxation time 1/mu >> T): net decline.
  S0 Day's hypothesis (selection off): harmful substitutions per generation = 0.75 x U_total x (1/2N) x 2N = 0.75 U
     per haploid genome (neutral substitution rate = mutation rate); reported next to Day's 7.6.
  Validation: per-site WF (N = 1000, 2N s in {-8, -4, -2, -1, -0.5, 0, 1}, 400,000 new-mutation replicates each,
  vectorised): fixation fraction within the binomial 99% band of Kimura's u.

PRE-REGISTERED PREDICTIONS
  HF-a soft limit
    Day side (s3.3.1 read as a rate claim, steelmanned: soft success needs purely relative fitness):
      DA1 any hard component collapses the soft advantage: mix h = 0.1 and 0.3 give lam50(10k) within 2x of H8's hard
          cap at the same R (R = 1.111: <= 0.0074; R = 2: <= 0.073).
      DA2 the soft limit does not grow with K (K = 4000 lam_max <= K = 1000 lam_max).
    Critic side (Wallace, Nunney, Maynard Smith):
      CA1 softJ and trunc sustain lam >= 0.1 at every R >= 1.111 (>= 15x Haldane's 1/300) and >= 0.4 at R >= 2.
      CA2 partial softness keeps most of it: mix h = 0.1 lam50 >= 3x the hard cap at R <= 2.
    Audit (numeric):
      PA1 softJ lam_max (last lam sustained, K = 1000): R = 1.05: 0.1-0.4; R = 1.111: 0.2-0.8; R >= 2: >= 0.4.
          trunc lam_max >= softJ lam_max at every R.  softWF sustains lam <= 0.4; maxrel at its limit < 2.
      PA2 mix: h = 0.3 lam50(10k) at R = 1.111 in [0.004, 0.012]; h = 0.1 in [0.008, 0.035]; at R = 2, h = 0.3
          in [0.04, 0.12], h = 0.1 in [0.07, 0.3].  (Mean field: extinction when h lam D_soft > phi ln R.)
      PA3 validation: mix h = 1 lam50(10k) at R = 1.111 and 2 within 25% of H8 (0.00368, 0.0363).
      PA4 K = 4000: softJ and trunc lam_max within one lam step of K = 1000 (no step either way).
      PA5 weak s = 0.002: hard lam50 x D_obs within 25% of the s = 0.01 value at the same R (Haldane: cost is
          independent of s); soft limits lower (sweeps 5x slower, nopen 5x larger): softJ lam_max at R = 2 0.1-0.2.
  HF-b truncation / synergistic epistasis vs Term 3
    Day side: DB1 truncation and synergy do not raise the sustainable rate above Term 3 at the same s_max:
          lam_max(trunc, R) and lam50(syn, R) <= 1.25 x lam_T3(R) = 1.25 ln R / (2 ln 2000) (0.0087 / 0.057 / 0.090
          at R = 1.111 / 2 / 3).  Day's s3.3.1 verbatim (s_max order unity) is scored on trunc maxrel, = R by
          construction (holds trivially for R <= 3).
    Critic side: CB1 truncation sustains >= 5x Term 3(R) at every R; CB2 synergy raises lam50 by >= 1.5x at b = 4e-3.
    Audit: PB1 trunc lam_max >= 10x lam_T3(R) at R = 1.111 (>= 0.1); PB2 quadratic synergy: lam50(b)/lam50(0) in
          [1.0, 1.3] at b = 2.5e-4, [1.1, 1.6] at 1e-3, [1.2, 2.0] at 4e-3 (mean field: load per unit selection is
          (s + b m)/(s + 2 b m), so the gain is < 2 for a quadratic); never > 2.2 at any R.  D_obs (in w units)
          falls with b by the same factor.
  HF-c intervals
    PC1 rerun T50 values reproduce the published H-C2 values exactly (same seeds; any mismatch is reported, not fixed).
    PC2 95% intervals on H-C2 T50 span about +-20-40% (8 reps per T, grid ratio ~1.33); "soft T50 > hard T50" holds
        with non-overlapping intervals in at least half of the matched pairs, overlapping elsewhere.
    PC3 H8 R = 1.111 D = 30 interval (10k): 95% interval contains 300 or lies above it; lower end in [300, 420].
        Day side: interval lies wholly >= 300 (1/300 conservative).  Critic side: interval reaches <= 300.
  HF-d GAP-05 (primary: shape 0.184, Ne = 1e4, U_d = 3)
    Day / ally (HO-11): slightly deleterious fixation is a real, ongoing log-fitness decline large enough to matter
        (S1 total decline over 252,000 generations > ln 3 = 1.1, i.e. more than Day's upper R can absorb).
    Critic (Charlesworth 2013, Kondrashov 1995): at equilibrium the net decline is ~0 (S2); Day's 9-generation figure
        needs selection switched off for strongly deleterious mutations (S0 vs S1 differ by > 10x in substitutions).
    Audit: PD1 S1 substitutions per lineage 3e4-3e5; S1 log decline (sum 2|s|) 0.3-5.  PD2 S2 |net| < 0.01.
        PD3 S3 net decline 0.1-2.  PD4 S0 harmful substitutions per generation = 0.75 U_total; S1 rate per
        generation <= 1/10 of S0's at U_d = 3.  PD5 validation passes at every 2Ns.  Results scale linearly in U_d.
  What would change a verdict: DA1 holding (any hardness kills the soft advantage) restores Day's s3.3.1 as a rate
  claim for partly-hard selection; CA2 holding means the rate is not capped near Haldane's unless selection is
  nearly fully hard.  DB1 holding would support Day's Term 3 as a bound across mechanisms; PB1/CB1 holding means
  truncation is a real cost reduction (Day's "order unity" is then true of s_max but not of the rate).  HF-d S1
  above ln 3 with S2 ~ 0 means GAP-05 turns on the initial condition (equilibrium or not), not on the arithmetic.
=====================================================================================================
"""
import json
import math
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
RAW = os.path.join(HERE, "results", "raw")
SEED = 20261011
EXT_N = 20
HOSSJER = 15800 / 450000
CHECKS = (10000, 20000, 40000)
RH = 1.0 / 0.9
LAMS_SOFT = (0.0351, 0.1, 0.2, 0.4, 0.8, 1.6)
LAMS_MIX = (0.0037, 0.0111, 0.0351, 0.1, 0.2, 0.4)
XS_SYN = (0.3, 0.45, 0.6, 0.8, 1.0, 1.25, 1.6, 2.0, 2.5)
BS = (0.0, 2.5e-4, 1e-3, 4e-3)


def Dref(K):
    return 2 * math.log(2 * K) + 2


def lam_T3(R, K=1000):
    return math.log(R) / (2 * math.log(2 * K))


def es_keep(w, k, rng):
    """Weighted sampling of k indices without replacement (Efraimidis-Spirakis), weights w > 0."""
    keys = rng.exponential(size=len(w)) / np.maximum(w, 1e-300)
    keep = np.zeros(len(w), bool)
    keep[np.argpartition(keys, k - 1)[:k]] = True
    return keep


def run(K, s, b, lam, R, mode, h, gens, burn, rng, max_open=5000, chunk=256):
    N = K
    G = np.zeros((0, 2 * N), dtype=np.uint8)
    t_open = []
    fixes_rec = 0
    acc = dict(rec=0, La=0.0, I=0.0, maxrel=0.0, nfrac=0.0, nopen=0.0)
    rec_len = gens - burn
    q1, q4 = [0.0, 0], [0.0, 0]
    alive_at = {T: False for T in CHECKS}
    fail, t_fail = None, None
    for t in range(gens):
        for T in CHECKS:
            if t == T - 1:
                alive_at[T] = True
        nnew = rng.poisson(lam)
        if nnew:
            cols = np.zeros((nnew, 2 * N), dtype=np.uint8)
            cols[np.arange(nnew), rng.integers(0, 2 * N, nnew)] = 1
            G = np.vstack([G, cols])
            t_open.extend([t] * nnew)
        nl = G.shape[0]
        if nl > max_open:
            fail, t_fail = "backlog", t
            break
        wA = None
        if mode == "hard":
            f = min(R, K / N)
            J = int(f * N)
            J += int(rng.random() < f * N - J)
        elif mode == "mix":
            J = int(R * N)
            J += int(rng.random() < R * N - J)
        elif mode == "trunc":
            J = int(round(R * K))
        else:                                             # softWF
            J = K
            ancA = (2 * nl - G.reshape(nl, N, 2).sum(axis=(0, 2), dtype=np.int64)) if nl else np.zeros(N, np.int64)
            wA = np.exp(-s * ancA - b * ancA.astype(float) ** 2)
        if J < 2:
            fail, t_fail = "extinct", t
            break
        if mode == "softWF":
            pw = wA / wA.sum()
            pa = rng.choice(N, size=J, p=pw)
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
        C = np.empty((nl, 2 * J), dtype=np.uint8)
        anc = np.zeros(J, dtype=np.int64)
        for i0 in range(0, nl, chunk):
            i1 = min(nl, i0 + chunk)
            o = rng.integers(0, 2, size=(i1 - i0, 2 * J), dtype=np.uint8)
            C[i0:i1] = np.take_along_axis(G[i0:i1], 2 * par[None, :] + o, axis=1)
            anc += C[i0:i1].reshape(i1 - i0, J, 2).sum(axis=(0, 2), dtype=np.int64)
        anc = 2 * nl - anc
        w = np.exp(-s * anc - b * anc.astype(float) ** 2) if mode != "softWF" else wA
        wbar = float(w.mean())
        if mode == "hard":
            keep = rng.random(J) < w
        elif mode == "mix":
            keep = rng.random(J) < w ** h if h > 0 else np.ones(J, bool)
            ns = int(keep.sum())
            if ns > K:
                idx = np.flatnonzero(keep)
                k2 = es_keep(w[idx] ** (1 - h), K, rng) if h < 1 else es_keep(np.ones(ns), K, rng)
                keep = np.zeros(J, bool)
                keep[idx[k2]] = True
        elif mode == "trunc":
            key = anc + rng.random(J) * 0.5
            keep = np.zeros(J, bool)
            keep[np.argpartition(key, K - 1)[:K]] = True
        else:
            keep = np.ones(J, bool)
        surv = np.flatnonzero(keep)
        Nn = len(surv)
        if t >= burn:
            rel = w / wbar
            acc["rec"] += 1
            acc["La"] += -math.log(max(wbar, 1e-300))
            acc["I"] += float(rel.var())
            acc["maxrel"] += float(rel.max())
            acc["nfrac"] += Nn / K
            acc["nopen"] += nl
            if t < burn + rec_len // 4:
                q1[0] += nl; q1[1] += 1
            elif t >= gens - rec_len // 4:
                q4[0] += nl; q4[1] += 1
        if Nn < EXT_N:
            fail, t_fail = "extinct", t
            break
        N = Nn
        hidx = (2 * surv[:, None] + np.arange(2)[None, :]).ravel()
        G = np.ascontiguousarray(C[:, hidx]) if nl else np.zeros((0, 2 * N), dtype=np.uint8)
        if nl:
            cnt = G.sum(axis=1, dtype=np.int64)
            fixed = cnt == 2 * N
            lost = np.flatnonzero(cnt == 0)
            if fixed.any():
                fixes_rec += int(t >= burn) * int(fixed.sum())
            if len(lost):
                G[lost, rng.integers(0, 2 * N, len(lost))] = 1
            if fixed.any():
                kr = np.flatnonzero(~fixed)
                G = G[kr]
                t_open = [t_open[j] for j in kr]
    if fail is None:
        for T in CHECKS:
            if gens >= T:
                alive_at[T] = True
    n = max(acc["rec"], 1)
    return dict(fail=fail, t_fail=t_fail, alive={str(T): alive_at[T] for T in CHECKS if T <= gens},
                k=fixes_rec / n, fixes_rec=fixes_rec, gens_rec=acc["rec"],
                D=acc["La"] / fixes_rec if fixes_rec else float("nan"), La=acc["La"] / n,
                I=acc["I"] / n, maxrel=acc["maxrel"] / n, nfrac=acc["nfrac"] / n,
                nopen=acc["nopen"] / n, nopen_q1=q1[0] / max(q1[1], 1), nopen_q4=q4[0] / max(q4[1], 1))


# ------------------------------------------------------------------------------------------------ cells
# cell = (part, K, s, b, lam, R, mode, h, label, reps, gens, burn, max_open)
def build(stage):
    c = []
    if stage == "smoke":
        c.append(("smoke", 1000, 0.01, 0.0, 0.1, RH, "mix", 0.0, "softJ", 1, 600, 200, 5000))
        c.append(("smoke", 1000, 0.01, 0.0, 0.4, 2.0, "trunc", 0.0, "trunc", 1, 600, 200, 5000))
        c.append(("smoke", 1000, 0.01, 1e-3, 0.03, 2.0, "hard", 1.0, "syn", 1, 600, 200, 5000))
        c.append(("smoke", 1000, 0.01, 0.0, 0.03, 2.0, "mix", 0.3, "mix", 1, 600, 200, 5000))
        c.append(("smoke", 4000, 0.01, 0.0, 0.4, 2.0, "trunc", 0.0, "trunc", 1, 200, 50, 5000))
        c.append(("smoke", 1000, 0.01, 0.0, 0.4, float("nan"), "softWF", 0.0, "softWF", 1, 600, 200, 5000))
        return c
    if stage != "main":
        raise SystemExit("unknown stage " + stage)
    for R in (1.05, RH, 1.5, 2.0, 3.0):
        for lam in LAMS_SOFT:
            c.append(("A-soft", 1000, 0.01, 0.0, lam, R, "mix", 0.0, "softJ", 4, 20000, 5000, 5000))
            c.append(("A-soft", 1000, 0.01, 0.0, lam, R, "trunc", 0.0, "trunc", 4, 20000, 5000, 5000))
    for lam in LAMS_SOFT:
        c.append(("A-soft", 1000, 0.01, 0.0, lam, float("nan"), "softWF", 0.0, "softWF", 4, 20000, 5000, 5000))
    for h in (0.1, 0.3):
        for R in (RH, 2.0, 3.0):
            for lam in LAMS_MIX:
                c.append(("A-mix", 1000, 0.01, 0.0, lam, R, "mix", h, f"h={h}", 4, 20000, 5000, 5000))
    for R in (RH, 2.0):
        for x in (0.45, 0.6, 0.8, 1.0, 1.25):
            c.append(("A-valid", 1000, 0.01, 0.0, x * math.log(R) / Dref(1000), R, "mix", 1.0, f"x={x}", 6, 20000, 3000, 5000))
    for R in (RH, 2.0):
        for lam in (0.1, 0.4, 1.6):
            for mode, lab in (("mix", "softJ"), ("trunc", "trunc")):
                c.append(("A-K4000", 4000, 0.01, 0.0, lam, R, mode, 0.0, lab, 3, 20000, 5000, 5000))
    for R in (RH, 2.0):
        for lam in (0.0351, 0.1, 0.2, 0.4):
            for mode, lab in (("mix", "softJ"), ("trunc", "trunc")):
                c.append(("A-weak", 1000, 0.002, 0.0, lam, R, mode, 0.0, lab, 4, 20000, 5000, 5000))
        for x in (0.3, 0.45, 0.6, 0.8, 1.0, 1.25):
            c.append(("A-weak", 1000, 0.002, 0.0, x * math.log(R) / Dref(1000), R, "hard", 1.0, f"x={x}", 6, 40000, 5000, 5000))
    for R in (RH, 2.0, 3.0):
        for b in BS:
            for x in XS_SYN:
                c.append(("B-syn", 1000, 0.01, b, x * math.log(R) / Dref(1000), R, "hard", 1.0, f"x={x}", 10, 20000, 3000, 5000))
    return c


def job(a):
    code, ci, cell, rep = a
    part, K, s, b, lam, R, mode, h, lab, reps, gens, burn, mo = cell
    rng = np.random.default_rng(np.random.SeedSequence([SEED, code, ci, rep]))
    t0 = time.time()
    r = run(K, s, b, lam, R, mode, h, gens, burn, rng, max_open=mo)
    r.update(dict(part=part, cell=ci, K=K, s=s, b=b, lam=lam, R=R, mode=mode, h=h, label=lab, rep=rep,
                  gens=gens, burn=burn, sec=time.time() - t0))
    return r


def cost_key(j):
    cell = j[2]
    K, lam, R, mode, gens = cell[1], cell[4], cell[5], cell[6], cell[10]
    Rr = 1.0 if R != R else R
    return -(gens * K * (Rr if mode != "hard" else 1.0) * (1 + min(lam, 1.6) * 20))


def run_stage(stage, workers):
    cells = build(stage)
    code = {"smoke": 0, "main": 1}[stage]
    jobs = [(code, ci, cell, rep) for ci, cell in enumerate(cells) for rep in range(cell[9])]
    jobs.sort(key=cost_key)
    os.makedirs(RAW, exist_ok=True)
    path = os.path.join(RAW, f"hf_{stage}.jsonl")
    done = set()
    if os.path.exists(path):
        for line in open(path):
            d = json.loads(line)
            done.add((d["cell"], d["rep"]))
    jobs = [j for j in jobs if (j[1], j[3]) not in done]
    if os.environ.get("HF_REVERSE") == "1":  # post hoc, orchestration only: a second host works from the cheap end
        jobs.reverse()
    if os.environ.get("HF_ROTATE"):  # post hoc, orchestration only: a third host starts mid-list
        k = int(len(jobs) * float(os.environ["HF_ROTATE"]))
        jobs = jobs[k:] + jobs[:k]
    print(f"stage {stage}: {len(cells)} cells, {len(jobs)} jobs to run ({len(done)} done), workers {workers}", flush=True)
    t0 = time.time()
    with Pool(workers) as pool, open(path, "a") as fh:
        for i, r in enumerate(pool.imap_unordered(job, jobs, chunksize=1)):
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            if stage == "smoke" or i % 25 == 0:
                print(f"[{time.time() - t0:7.0f}s] {i + 1}/{len(jobs)} {r['part']} {r['mode']} h={r['h']} K={r['K']} "
                      f"s={r['s']} b={r['b']} R={r['R']:.3f} lam={r['lam']:.4g} rep{r['rep']} fail={r['fail']} "
                      f"k/lam={r['k'] / r['lam']:.3f} D={r['D']:.3g} nopen={r['nopen']:.0f} sec={r['sec']:.0f}", flush=True)
    print(f"stage {stage} done in {time.time() - t0:.0f} s", flush=True)


# ------------------------------------------------------------------------------------------------ HF-c intervals
def first_cross(xs, fr, increasing):
    """H-C2 rule (increasing=True: T grid, success rises with T) or H8 rule (survival falls with lam)."""
    if increasing:
        for i, f in enumerate(fr):
            if f >= 0.5:
                if i == 0:
                    return xs[0]
                f0 = fr[i - 1]
                return float(np.exp(np.log(xs[i - 1]) + (0.5 - f0) / (f - f0) * (np.log(xs[i]) - np.log(xs[i - 1]))))
        return float("nan")
    if fr[0] < 0.5:
        return float("nan")
    for i in range(len(fr) - 1):
        if fr[i] >= 0.5 > fr[i + 1]:
            u = (fr[i] - 0.5) / (fr[i] - fr[i + 1])
            return float(math.exp(math.log(xs[i]) + u * (math.log(xs[i + 1]) - math.log(xs[i]))))
    return float("nan")


def beta_interval(xs, ks, ns, increasing, rng, draws=10000):
    ks, ns = np.asarray(ks, float), np.asarray(ns, float)
    P = rng.beta(ks[None, :] + 0.5, ns[None, :] - ks[None, :] + 0.5, size=(draws, len(xs)))
    v = np.array([first_cross(xs, p, increasing) for p in P])
    ok = v[v == v]
    cens = 1 - len(ok) / draws
    if len(ok) < draws * 0.5:
        return (float("nan"), float("nan"), cens)
    lo, hi = np.percentile(ok, [2.5, 97.5])
    return (float(lo), float(hi), cens)


def gauss_cond(a):
    """Mirror of h_nunney_gauss.cond, returning the per-T success counts (same seeds, same code path)."""
    import h_nunney_gauss as g
    import wf_hc as hh
    K, n, R, M, reg, seed = a
    rng = np.random.default_rng(np.random.SeedSequence(seed))
    u = M / (2 * K)
    ks, streak = [], 0
    for T in g.GRID:
        ok = 0
        for _ in range(10):
            o = hh.gauss_run(K, n, T, R, u, reg, 5 if T < 300 else 4, rng)
            ok += (not o["extinct"]) and (o["dev2"] < 0.5)
        ks.append(ok)
        streak = streak + 1 if ok >= 9 else 0
        if streak >= 2:
            break
    grid = list(g.GRID[:len(ks)])
    return dict(model="gauss", K=K, n=n, R=R, M=M, regime=reg, seed=seed, grid=grid, k=ks, reps=10,
                T50=first_cross(grid, [k / 10 for k in ks], True))


def cost_cond(a):
    import h_cost_of_selection as hc
    r = hc.cond(a)
    reps = a[9]
    grid = list(hc.GRID[:len(r["fr"])])
    return dict(model="treadmill", label=r["label"], K=r["K"], n=r["n"], s=r["s"], R=r["R"], M=r["M"],
                regime=r["regime"], stagger=r["stagger"], grid=grid, k=[int(round(f * reps)) for f in r["fr"]],
                reps=reps, T50=r["T50"])


def ci_wrap(a):
    kind, arg = a
    return cost_cond(arg) if kind == "cost" else gauss_cond(arg)


def stage_ci(workers):
    import h_cost_of_selection as hc
    jobs = [("cost", c) for c in hc.build()]
    i = 0
    gj = []
    for reg in ("hard", "soft"):
        for n in (1, 7):
            for M in (0.1, 0.25, 0.5, 1.0, 10.0):
                i += 1
                gj.append((500, n, 10, M, reg, 20261010 + i))
    for reg in ("hard", "soft"):
        for R in (2.2, 3, 5, 40):
            i += 1
            gj.append((500, 1, R, 1.0, reg, 20261010 + i))
    i = 0
    for reg in ("hard", "soft"):
        for M in (0.1, 0.25, 1.0, 10.0):
            i += 1
            gj.append((500, 1, 2.2, M, reg, 20261020 + i))
    jobs += [("gauss", c) for c in gj]
    path = os.path.join(RAW, "hf_ci.jsonl")
    t0 = time.time()
    with Pool(workers) as pool, open(path, "w") as fh:
        for r in pool.imap_unordered(ci_wrap, jobs, chunksize=1):
            fh.write(json.dumps(r) + "\n")
            fh.flush()
    print(f"ci reruns done: {len(jobs)} conditions in {time.time() - t0:.0f} s", flush=True)


def analyse_ci():
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 99]))
    rows = [json.loads(l) for l in open(os.path.join(RAW, "hf_ci.jsonl"))]
    print("## HF-c H-C2 T50 with 95% Jeffreys-Beta intervals (cens = share of draws with no crossing)")
    print("| model | label | regime | n | s | R | M | T50 | 95% interval | cens |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    rows.sort(key=lambda r: (r["model"], r.get("label", ""), r["n"], r.get("s", 0), r["R"], r["M"], r["regime"]))
    for r in rows:
        lo, hi, cens = beta_interval(r["grid"], r["k"], [r["reps"]] * len(r["k"]), True, rng)
        print(f"| {r['model']} | {r.get('label', '-')}{' stag' if r.get('stagger') else ''} | {r['regime']} | {r['n']} | "
              f"{r.get('s', '-')} | {r['R']} | {r['M']} | {r['T50']:.1f} | {lo:.1f}-{hi:.1f} | {cens:.2f} |")
    # H8 lam50 intervals
    print("\n## HF-c H8 lam50 (10k / 20k) with 95% Jeffreys-Beta intervals; D = 30 interval with D_obs rep-bootstrap")
    print("| stage | K | R | T | lam50 | 95% interval | D_obs | D=30 interval (gens) | 95% interval |")
    print("|---|---|---|---|---|---|---|---|---|")
    import collections
    for stage, arms in (("main", (("hard", 1000), ("Kscale", 500), ("Kscale", 4000))), ("kscale16", (("Kscale", 16000),)),
                        ("kscale64", (("Kscale", 64000),))):
        p = os.path.join(RAW, f"h8_{stage}.jsonl")
        if not os.path.exists(p):
            print(f"(missing {p})")
            continue
        rows8 = [json.loads(l) for l in open(p)]
        for arm, K in arms:
            g = collections.defaultdict(list)
            for r in rows8:
                if r["arm"] == arm and r["K"] == K:
                    g[(round(r["R"], 6), r["lam"])].append(r)
            for R in sorted({k[0] for k in g}):
                cells = sorted((lam, v) for (RR, lam), v in g.items() if RR == R)
                lnR = math.log(R)
                Ds = np.array([r["D"] for lam, v in cells for r in v
                               if lam <= 0.8 * lnR / Dref(K) * 1.0001 and r["fail"] is None and r["D"] == r["D"]])
                if len(Ds) == 0:
                    continue
                Dm = float(np.median(Ds))
                for T in (10000, 20000):
                    xs, ks, ns = [], [], []
                    for lam, v in cells:
                        vv = [r for r in v if str(T) in r["alive"]]
                        if vv:
                            xs.append(lam); ks.append(sum(r["alive"][str(T)] for r in vv)); ns.append(len(vv))
                    if len(xs) < 2:
                        continue
                    l50 = first_cross(xs, [k / n for k, n in zip(ks, ns)], False)
                    lo, hi, cens = beta_interval(xs, ks, ns, False, rng)
                    # joint: lam draws x D draws
                    P = rng.beta(np.array(ks)[None, :] + 0.5, np.array(ns)[None, :] - np.array(ks)[None, :] + 0.5,
                                 size=(4000, len(xs)))
                    lv = np.array([first_cross(xs, pp, False) for pp in P])
                    dv = np.array([np.median(rng.choice(Ds, len(Ds))) for _ in range(4000)])
                    iv = 30 / (lv * dv)
                    iv = iv[iv == iv]
                    ilo, ihi = (np.percentile(iv, [2.5, 97.5]) if len(iv) > 2000 else (float("nan"), float("nan")))
                    print(f"| {stage} | {K} | {R:.3f} | {T} | {l50:.4g} | {lo:.4g}-{hi:.4g} (cens {cens:.2f}) | {Dm:.2f} | "
                          f"{30 / (l50 * Dm):.0f} | {ilo:.0f}-{ihi:.0f} |")


# ------------------------------------------------------------------------------------------------ HF-d GAP-05
def kimura_u(s, N):
    """Fixation probability of a new mutation, genic selection, heterozygote effect s (B0.3); vectorised; s may be 0."""
    s = np.asarray(s, float)
    x = 4 * N * s
    out = np.empty_like(s)
    small = np.abs(x) < 1e-8
    out[small] = 1 / (2 * N)
    xs, ss = x[~small], s[~small]
    out[~small] = -np.expm1(-2 * ss) / -np.expm1(-xs)
    return out


def gamma_grid(shape, mean, n=400000):
    """Quadrature over |s| ~ Gamma(shape, mean/shape) by quantiles (equal-mass points), |s| capped at 1."""
    from scipy.stats import gamma
    q = (np.arange(n) + 0.5) / n
    sv = gamma.ppf(q, shape, scale=mean / shape)
    return np.minimum(sv, 1.0)


def stage_gap05():
    np.seterr(over="ignore", invalid="ignore", divide="ignore")
    out = {}
    T = 252000
    print("## HF-d GAP-05: deleterious fixation flux (heterozygote effect s; fixed homozygote log-fitness 2s)")
    print("| shape | Ne | U_d | S1 subs/lineage | S1 decline (sum 2s) | S1 subs/gen | S0 0.75 U/gen at U_tot | S2 net | S3 net (Ne 2.06e5 -> Ne) | share |s|<1e-4 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for shape in (0.184, 0.1, 0.3):
        sv = gamma_grid(shape, 0.029)
        for Ne in (1e4, 2e4):
            ud = kimura_u(-sv, Ne) * 2 * Ne                     # relative to neutral (= 1)
            ub = kimura_u(sv, Ne) * 2 * Ne
            # S1: rate per generation per unit U_d: U_d * E[ud]; decline: U_d * E[ud * 2 s]
            r1, d1 = float(ud.mean()), float((ud * 2 * sv).mean())
            # S2/S3: per-site two-state; good->bad rate mu*ud/... relative units, bad->good rate (mu/3)*ub
            def eq_bad(N):
                a = kimura_u(-sv, N) * 2 * N
                bb = kimura_u(sv, N) * 2 * N / 3
                return a / (a + bb)
            pi_now = eq_bad(Ne)
            pi_anc = eq_bad(2.06e5)
            flux_now = lambda pi: ((1 - pi) * ud - pi * ub / 3)
            s2 = float((flux_now(pi_now) * 2 * sv).mean())          # per unit U_d per generation (sites = U_d/mu)
            s3 = float((flux_now(pi_anc) * 2 * sv).mean())
            for Ud in (0.3, 1.0, 3.0):
                row = dict(shape=shape, Ne=Ne, Ud=Ud, S1_subs=Ud * r1 * T, S1_decline=Ud * d1 * T, S1_rate=Ud * r1,
                           S2_net=Ud * s2 * T, S3_net=Ud * s3 * T, nn_share=float((sv < 1e-4).mean()))
                out[f"{shape}_{Ne:g}_{Ud}"] = row
                print(f"| {shape} | {Ne:g} | {Ud} | {row['S1_subs']:.3g} | {row['S1_decline']:.3g} | {row['S1_rate']:.3g} | "
                      f"(see S0 line) | {row['S2_net']:.2e} | {row['S3_net']:.3g} | {row['nn_share']:.3f} |")
    print("\nS0 (Day's hypothesis, selection off): harmful substitutions per generation = 0.75 x U_total (neutral "
          "substitution rate = mutation rate per haploid genome).  U_total = 38.4 (parameters.yaml, 3.2e9 x 1.2e-8) "
          f"-> {0.75 * 38.4:.1f}; Day's stated 7.6 -> implied U_total {7.6 / 0.75:.1f}.")
    # validation: per-site WF, N = 1000
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 5]))
    N = 1000
    print("\nvalidation (per-site WF, N = 1000, genic selection, heterozygote effect s; 400,000 new mutations each):")
    val = []
    for S2 in (-8, -4, -2, -1, -0.5, 0, 1):
        s = S2 / (2 * N)
        reps = 400000
        p = np.full(reps, 1 / (2 * N))
        fixed = 0
        while len(p):
            w_mean = 1 + 2 * s * p          # additive: genotype fitness 1, 1+s, 1+2s (s<0 deleterious)
            pp = p * (1 + s + s * p) / w_mean
            p = rng.binomial(2 * N, np.clip(pp, 0, 1)) / (2 * N)
            fixed += int((p == 1).sum())
            p = p[(p > 0) & (p < 1)]
        u = float(kimura_u(np.array([s]), N)[0])
        se = math.sqrt(u * (1 - u) / reps)
        ok = abs(fixed / reps - u) <= 2.576 * se
        val.append(ok)
        print(f"  2Ns = {S2:5}: sim {fixed / reps:.3e}  Kimura {u:.3e}  z = {(fixed / reps - u) / se:+.2f}  {'PASS' if ok else 'FAIL'}")
        out[f"val_{S2}"] = dict(sim=fixed / reps, kimura=u, ok=ok)
    print(f"validation: {sum(val)}/{len(val)} pass")
    json.dump(out, open(os.path.join(RAW, "hf_gap05.json"), "w"), indent=1)


# ------------------------------------------------------------------------------------------------ analysis (main)
def analyse_main():
    import collections
    rows = [json.loads(l) for l in open(os.path.join(RAW, "hf_main.jsonl"))]
    print(f"rows {len(rows)}")
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["part"], r["mode"], r["h"], r["K"], r["s"], r["b"], None if r["R"] != r["R"] else round(r["R"], 6),
           round(r["lam"], 8))].append(r)

    def success(r, T, steady):
        if str(T) not in r["alive"] or not r["alive"][str(T)]:
            return False
        if r["fail"] is not None and (r["t_fail"] is None or r["t_fail"] < T):
            return False
        if steady:
            if r["fail"] is not None:
                return False
            if r["k"] / r["lam"] < 0.9 or r["nopen_q4"] / max(r["nopen_q1"], 1e-9) > 1.15:
                return False
        return True

    groups = collections.defaultdict(list)
    for k, v in g.items():
        groups[k[:7]].append((k[7], v))
    print("\n## per group: lam50 (10k / 20k) on the success rule; lam_max = largest lam with >= 50% success")
    print("| part | mode | h | K | s | b | R | lam50 10k | lam50 20k | lam_max | x hard cap(H8) | x Term3(R) | x 1/300 | cells: lam succ/n k/lam nopen maxrel D |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    H8CAP = {round(RH, 6): 0.00368, 2.0: 0.03627, 3.0: 0.06059, 1.05: 0.00187, 1.5: 0.01886}
    res = {}
    for key in sorted(groups, key=lambda k: (k[0], k[1], k[2], k[3], k[4], k[5], str(k[6]))):
        part, mode, h, K, s, b, R = key
        cells = sorted(groups[key])
        steady = not (mode == "hard" or (mode == "mix" and h >= 1.0))
        out = []
        for T in (10000, 20000):
            pts = [(lam, sum(success(r, T, steady) for r in v) / len(v)) for lam, v in cells]
            out.append(first_cross([p[0] for p in pts], [p[1] for p in pts], False))
        pts20 = [(lam, sum(success(r, 20000, steady) for r in v) / len(v)) for lam, v in cells]
        lmax = max([lam for lam, f in pts20 if f >= 0.5], default=float("nan"))
        ref = out[0] if out[0] == out[0] else lmax
        cap = H8CAP.get(R) if R is not None else None
        t3 = lam_T3(R, K) if R is not None else float("nan")
        desc = "; ".join(
            f"{lam:.4g}:{sum(success(r, 20000, steady) for r in v)}/{len(v)} "
            f"{np.mean([r['k'] for r in v]) / lam:.2f} {np.mean([r['nopen'] for r in v]):.0f} "
            f"{np.mean([r['maxrel'] for r in v]):.2f} {np.nanmean([r['D'] for r in v]):.1f}" for lam, v in cells)
        res[key] = dict(l10=out[0], l20=out[1], lmax=lmax)
        print(f"| {part} | {mode} | {h} | {K} | {s} | {b} | {R if R is None else round(R, 3)} | {out[0]:.4g} | {out[1]:.4g} | "
              f"{lmax:.4g} | {(ref / cap) if cap else float('nan'):.1f} | {ref / t3:.1f} | {ref * 300:.1f} | {desc} |")
    print("\n## synergy gain lam50(b)/lam50(0), 10k and 20k")
    for R in (round(RH, 6), 2.0, 3.0):
        base = res.get(("B-syn", "hard", 1.0, 1000, 0.01, 0.0, R))
        for b in BS[1:]:
            d = res.get(("B-syn", "hard", 1.0, 1000, 0.01, b, R))
            if base and d:
                print(f"R={R:.3f} b={b}: 10k {d['l10'] / base['l10']:.2f}  20k {d['l20'] / base['l20']:.2f}  "
                      f"(lam50 {d['l10']:.4g} vs {base['l10']:.4g}; Term3(R) {lam_T3(R):.4g})")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    if which == "analyse":
        part = sys.argv[2] if len(sys.argv) > 2 else "main"
        {"main": analyse_main, "ci": analyse_ci}[part]()
    elif which == "ci":
        stage_ci(int(sys.argv[2]) if len(sys.argv) > 2 else 2)
        analyse_ci()
    elif which == "gap05":
        stage_gap05()
    else:
        run_stage(which, int(sys.argv[2]) if len(sys.argv) > 2 else 3)
