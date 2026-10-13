"""L5 -- aDNA zero-fixation POWER analysis: how many of Day's 'fixations' would a selection-driven model show on the
1240k panel, at his sample sizes, in his window?  (claims C, C1, C1a; also C6's '15,500' comparator)

THROWAWAY research check.  PRE-REGISTRATION: this docstring was committed with the script before the main run.
Run (isolated venv; main run on na-workhorse only, after the HF `ph` run has finished):
    research/.venv/bin/python -I research/checks/l5_adna_power.py selftest            # validations V2, V3 (also part of main)
    research/.venv/bin/python -I research/checks/l5_adna_power.py smoke <outdir>      # tiny sizes; timing/structure only
    research/.venv/bin/python -I research/checks/l5_adna_power.py main <workers> <outdir>
    research/.venv/bin/python -I research/checks/l5_adna_power.py analyse <outdir>
Reuses: c1c_call_depth_replacement.py (AADR per-bin call depth, results/c1c_depth_table.json) and
c1e_holocene_trajectories.py (the four published Holocene N_e trajectories, holocene-ne.md s3-4), imported unchanged.
The neutral chain logic follows c1_ascertainment_sim.py (equilibrium SFS theta/i, African-male discovery design D2,
African MAF design D3, split 2000 generations), here as a scaled Monte Carlo so that selection and linkage can be added.

------------------------------------------------------------------------------------------------------------------------
1. WHAT DAY OBSERVED (his definitions; quotes in docs/research/sources/quotes-day.md)
  - Panel: AADR 1240k autosomal SNPs, 1,143,671 analysed (v62.0), 1,143,230 (v66.p1) (Q52; C claim table); blog version
    1,211,499 loci (Q55 note).
  - Periods: "a Neolithic period (6000-8000 BP) and a modern period (date = 0, i.e., present-day)" (Q113); 1,372 / 680
    individuals (v62), 395 / 441 (v66); blog 1,112 / 645 (Q55 note).  Filter: "minimum of 100 genotyped samples in each
    period" (Q114).  Frequency = "proportion of the minor allele among genotyped individuals" (Q115); as in C1d, a
    pseudo-haploid individual contributes one chromosome, a diploid two.
  - Statistics (all four are scored; 'either allele' = fixation or loss, as Day counts both, Q52/Q54):
      Z50  modern sample monomorphic for allele A, Neolithic sample frequency of A < 50%.   Observed 0 and 0 (Q53).
      Z10  same with < 10%.                                                                   Observed 0 and 0 (Q53).
      B10  blog: Neolithic < 10% and modern > 90% (blog sample sizes, 1,211,499 loci).        Observed 0 (Q55).
      M10  Neolithic minor-allele frequency >= 10%, modern monomorphic.                       Observed 1 (v62), 3 (v66) (Q52).
      N100 'newly 100%' (modern monomorphic, Neolithic polymorphic); validation only.          Observed 17,814 / 3,470 (Q54).
  - Rule C (most charitable reading of the inference "zero refutes the selection-driven rate"): the PRIMARY statistic
    S* in each model cell is whichever of {Z50 v62, Z50 v66, B10 blog} has the LARGEST expected count (the most powerful
    of his zero-reported statistics); P(0) is reported for that statistic.  All are reported.
  - The comparator Day sets against zero: "approximately 15,500" fixations in 7,000 y under the modern synthesis
    (blog 2026-01-14, para 4; derived 20,000,000 / 9,000,000 y x 7,000 y = 15,556; claim C).  Day gives no panel scaling.

2. MODEL (forward Wright-Fisher, unlinked focal sites plus linked panel SNPs by the hitchhiking escape approximation)
  Populations: ancestral (N_e 1e4) splits 2,000 generations ago (ASSUMED, as C1) into Africa (N_e 1e4, discovery
  population) and Europe.  Europe N_e = 1e4 before 10,500 BP, then one of the Holocene trajectories (c1e): const 1e4
  (textbook/keruru; Day-side reading), Gravel 2011, Gazave 2014, Nelson 2012 central (1.7%).  Generation time 25 y
  (the trajectories' own clock, C1e post hoc); sensitivity at Day's 20 y for const 1e4 and Gravel (more generations in
  the window = more power = Day-favourable).  No admixture/replacement (Day: admixture makes his count conservative,
  Z23046531 s1); no migration between Africa and Europe; no genotype error.
  Neolithic sample = two dates, 7,500 BP and 6,500 BP, weighted by the AADR bin counts 7000-8000 (668) / 6000-7000 (573)
  and their per-site call rates (c1c depth table), scaled to Day's n; modern = date 0, diploid, call rate of the
  0-500 BP diploids (0.967).  Each simulated SNP gets its own call counts (binomial), then 32 Monte Carlo draws of the
  Neolithic allele count; the modern 'monomorphic' probability is exact (f^(2m)).
  Panel ascertainment (quantified, not assumed away): D2 (primary) = site heterozygous in one African individual
  (Haak 2015 design; C1 shows it reproduces v62's 17,806 within 1.3x): inclusion probability c2 * 2a(1-a), a = present
  African frequency, c2 normalised so that the neutral genome gives 1,143,671 panel sites over L = 3.1e9 bp (C1's
  genome size).  D3 (sensitivity) = African MAF >= 5% in 100 diploids, normalised the same way.  A swept allele that
  arose in Europe after the split has a = 0 and is therefore NOT on the panel (the mechanical exclusion); linked panel
  SNPs that hitchhike are old variants still polymorphic in Africa and ARE on the panel (local sweeps), or are dropped
  in proportion to their loss of African polymorphism (species-wide sweeps).  Reported: share of window completions
  whose focal site is on the panel (D2, D3) against the uniform share 1,143,671 / 3.1e9 = 3.7e-4.
  Hitchhiking: panel SNPs at genetic distance r from a sweep, density 1,143,671 / 36.8 M (parameters.yaml
  genetic_map_morgans.human_w_b_regime) per Morgan, out to r_max = 8 / I (I = sum over the sweep of (1 - x));
  founder background carries the SNP allele with probability p (its European frequency); allele frequency at time t =
  x(t)[(1-E(t)) beta + E(t) p] + (1 - x(t)) p, E(t) = 1 - exp(-r I(t)).  For standing-variation sweeps I starts at the
  variant's own neutral pre-history integral, sampled by diffusion reversibility (a neutral path from its onset
  frequency conditioned on loss has the law of its reversed past; scaled N_s = 1000), so association with the founder
  haplotype decays with the variant's age.  The focal-only count is reported too (lower bound on hitchhiking).
  Validated against an explicit two-locus WF in selftest (V3; hard-sweep case).
  Selection: additive (h = 0.5), s = homozygote advantage, fixation probability ~ s.  Grid s in {1e-3, 3e-3, 1e-2,
  2e-2, 3e-2, 5e-2, 1e-1}.  Two modes:
     hard     = species-wide new-mutation sweeps (MITTENS picture: human-lineage substitutions by new beneficial
                mutations); s acts in every population; origins in the ancestral population or in Europe.
     standing = European sweeps of standing variants (mainstream Holocene picture); onset in the last 2,000
                generations, start frequency from the neutral European spectrum, s in Europe only.
  Calibration: each task simulates origins/onsets uniformly in time and counts European population fixations dated in
  the 7,000-y window (n_wc).  rho = expected observed events per window completion; q = probability per window
  completion that a sweep shows >= 1 event.  A model with F window completions then expects E = F rho events
  (+ neutral background) and P(0) = exp(-F q - E_neutral).
  Models:
     (i)   neutral: panel sites only (D2 / D3), no sweeps.
     (ii)  mainstream: F_ii = alpha x D_n x 7,000 / T_div = 0.135 x 29,925 x 7,000 / 6.3e6 = 4.49 completions per
           window (Uricchio 2019 alpha 0.135, HPD 0.096-0.17, and its 29,925 nonsynonymous counts read as human-lineage
           substitutions, a Day-favourable reading; refresh-2026-10-11b-lit.md s3; T_div 6.3 My parameters.yaml
           divergence.day_2026_mittens3).  s mixture 72% weak / 28% strong (Uricchio) mapped to s = 1e-3 / 1e-2
           (ASSUMED mapping; the paper's class boundaries are not in the repo).  Brackets: alpha HPD; x10 and x100
           (generous: noncoding adaptation, Holocene acceleration; UNSOURCED, labelled as such).
     (iii) Day's required rate: F_iii = 15,556 completions in the window (his own comparator), per s and mode.
           Day's own beneficial s input elsewhere is 1e-3 (parameters.yaml selection.s_zeng_2021, 'Day uses as
           beneficial'); that cell is reported separately.

3. PRE-REGISTERED PREDICTIONS (written before any run; smoke inspected timing and structure only, see section 6)
  Validation
   V1  neutral, const 1e4, gy 25, v62, D2: N100 in [7,000, 28,000] (C1 chain 13,807); M10 in [0.01, 0.15] (C1: 0.038);
       Z50 < 0.01.  Failure of V1 = the panel model is off; results are then reported as 'model not validated'.
   V2  selftest: simulated fixation probability (N 1e3, s 0.02) within 10% of Kimura's; event-probability sanity cases.
   V3  selftest: hitchhiking formula vs explicit two-locus WF (N 1e3, s 0.1, r in {1e-4, 1e-3, 5e-3}): mean final
       non-founder share within 30% (relative) or 0.01 (absolute) of the formula at each r.
  Results (E = expected count of S*; 'cell' = demography x mode; valid cells need n_wc >= 100)
   P1  neutral (i): Z50, Z10 (v62, v66) and B10 < 0.01 in every demography; M10 <= 0.15.
   P2  mainstream (ii) central: E < 0.01 in every cell; at x100: E < 0.5; P(0) >= 0.6 everywhere.
   P3  Day (iii): s <= 1e-2: E < 1 in every cell (a sweep with s <= 1e-2 cannot carry an allele from < 50% to
       sample-monomorphic within ~280 generations: logistic time ~ ln(odds ratio) / (s/2) ~ 1,000+ generations).
       s = 3e-2: median over demographies in [0.3, 300].  s >= 5e-2: median >= 10 in both modes.
   P4  where median E >= 1, hitchhiking panel SNPs supply >= 90% of S* events (the swept site itself is rarely on the
       panel).
   P5  focal-site ascertainment: hard mode, s >= 1e-2: mean D2 inclusion per window completion < 1e-4 (below the
       uniform 3.7e-4: post-split European origins are absent in Africa); standing mode: in [3.7e-4, 0.2].
   P6  gy 20 gives E >= gy 25 (same demography, mode) for every s >= 3e-2.
   P7  band (section 4): MIDDLE, with the crossover s* (smallest grid s with median E >= 3) equal to 2e-2 or 3e-2 in
       both modes.
   P8  M10 (Day's observed 1 and 3) under (iii) at s >= 5e-2: median E >= 30, i.e. his own non-zero count is also far
       below the strong-selection required-rate expectation.

  WHAT EACH SIDE PREDICTS (numeric, before the run)
   Day (Q53/Q55, C1a "such bias would favor detecting recent fixations, not obscure them"): a selection-driven model at
     the rate the modern synthesis requires predicts many observed fixations, so zero refutes it.  Day band: E >= 3
     (P(0) <= 0.05) for every s >= 3e-3 in both modes (median demography).
   Critics (C1 ascertainment; C5 keruru 'zero is the expectation'): the test has near-zero power: ascertainment drops
     the swept sites and 7,000 y is too short for completions from < 50%.  Critic band: E <= 1 (P(0) >= 0.37) for every
     s <= 1e-2 in every cell, AND mainstream (ii) central E <= 0.1.

4. BANDS AND THE VERDICTS EACH MOVES (claims C, C1, C1a; C6 noted)
   DAY band:    C1 external supported -> contested (ascertainment does not hide selection-driven completions);
                C1a external contested -> supported (scoped: selection-driven completions); C external contested ->
                supported (scoped: zero excludes the 15,556 required rate at s >= 3e-3).  C internal stays non-sequitur
                for the neutral comparison (neutral also predicts ~0), with a note that the MS-rate inference holds.
   CRITIC band: C1 external stays supported, with the power result added; C1a stays contested (wrong for
                selection-driven completions); C external contested -> contradicted (scoped: the zero carries no
                information on selection with s <= 1e-2, which includes Day's own s = 1e-3).
   MIDDLE:      no verdict flip.  Claim files record s*: "zero excludes the required rate only if its sweeps had
                s >= s*"; C external stays contested with that comment; owner decision whether Day's model implies
                s >= s* (his own beneficial s input is 1e-3).
   Gy-20 and D3 cells are sensitivities; if they alone change the band, the band is reported as 'sensitive' and does
   not move a verdict.

5. SEEDS, OUTPUTS, RESOURCES
   ROOT_SEED 20261011; neutral sample SeedSequence([ROOT_SEED, 5, 0, gy]) (shared by all tasks with that gy); task k:
   SeedSequence([ROOT_SEED, 5, 1, k, pass]); selftest SeedSequence([ROOT_SEED, 5, 9, ...]).
   Output: <outdir>/l5_<task>.json (one per task), l5_selftest.json; analyse prints the tables and the band.
   Tasks: 6 neutral + 7 s x 2 modes x 6 demography cells = 90.  Largest: hard s = 1e-3 (~1.9e8 origins over ~28,000
   generations, pool ~2.5e5 alleles): ~10-20 min.  Estimated total ~6-8 CPU-hours; peak RAM ~1 GB per worker
   (smoke at tiny sizes: 0.41 GB).  na-workhorse: 8 workers (~8 GB), wall ~1 h, ONLY when total busy processes across agents stay <= 11.
   builder alternative: 4 workers (<= 3.5 GB of its 5 GB).
   Launch (after `ph` is collected; check `uptime` first):
     rsync -a research/checks/l5_adna_power.py research/checks/c1c_call_depth_replacement.py \
           research/checks/c1e_holocene_trajectories.py na-workhorse:projects/evo-sim/research/checks/
     rsync -a research/checks/results/c1c_depth_table.json na-workhorse:projects/evo-sim/research/checks/results/
     ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && mkdir -p research/checks/results/raw/l5 && \
         (hostname; date -u; md5sum research/checks/l5_adna_power.py research/checks/c1c_call_depth_replacement.py \
          research/checks/c1e_holocene_trajectories.py research/checks/results/c1c_depth_table.json) \
          > research/checks/results/raw/l5.host && \
         nohup research/.venv/bin/python -I research/checks/l5_adna_power.py main 8 research/checks/results/raw/l5 \
          > research/checks/results/raw/l5.out 2>&1 < /dev/null &'
   Collect (once, ~1.5 h later):
     rsync -a na-workhorse:projects/evo-sim/research/checks/results/raw/l5 \
           na-workhorse:projects/evo-sim/research/checks/results/raw/l5.out \
           na-workhorse:projects/evo-sim/research/checks/results/raw/l5.host research/checks/results/raw/
     research/.venv/bin/python -I research/checks/l5_adna_power.py analyse research/checks/results/raw/l5 \
           > research/checks/results/raw/l5_analysis.txt
   Never commit from workhorse.  Review tier: three reviews (precedent C1c/C1d; C is in the R5-draft s1.3 promotion
   list although hierarchy.yaml marks C/C1/C1a load_bearing: false) -- owner may downgrade to one combined review.

6. DISCLOSED BEFORE THE MAIN RUN
   Local smoke on the workstation (one process, < 500 MB, < 1 min; 19 s, 0.41 GB): `smoke` with tiny sizes printed
   timings, task counts, n_wc and kept-sweep counts only; expected counts were not printed or inspected.  The first
   smoke stalled in the standing-mode task: standing variants entered with I = 0, i.e. single-founder hitchhiking over
   whole chromosomes (a large Day-favourable artefact); fixed before any result was seen by sampling each variant's
   pre-history integral (section 2) and initialising I7/I6 at entry.  `analyse` was run on the smoke output with
   stdout discarded (exit status only).  `selftest` (reduced) was run
   locally to check the code paths; its pass/fail lines were seen (they are validations, not results).
   Known limits: no admixture, migration, background selection, genotype error, or capture heterogeneity; panel
   ascertainment = single-African-individual model (non-African discovery panels of Human Origins not modelled; they
   matter only for alleles present outside Europe); founder-background drift during long sweeps ignored; hitchhiker
   density scaled (not regenerated) for the v66/blog panel sizes.
"""
import os
import sys
import json
import time
import math

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
from scipy.stats import binom
import c1c_call_depth_replacement as c1c
import c1e_holocene_trajectories as c1e

ROOT_SEED = 20261011
TAG = 5
MU = 1.2e-8                 # parameters.yaml mutation.mu_per_site_per_gen.pedigree_human
NE_ANC = 1.0e4              # parameters.yaml population.Ne_modern_human (textbook, unverified)
NE_AFR = 1.0e4              # as C1 (equal N_e assumed)
THETA = 4 * NE_ANC * MU
T_SPLIT_G = 2000            # ASSUMED African-European split (C1)
L_GENOME = 3.1e9            # C1 / claim C order of magnitude
MAP_M = 36.8                # parameters.yaml genetic_map_morgans.human_w_b_regime
NPANEL = 1_143_671
START_BP = c1c.START_BP     # 10,500
F_DAY = 20_000_000 / 9_000_000 * 7000          # 15,555.6
ALPHA, ALPHA_LO, ALPHA_HI = 0.135, 0.096, 0.17
DN_URICCHIO = 29_925
T_DIV_Y = 6.3e6
F_MS = ALPHA * DN_URICCHIO * 7000 / T_DIV_Y      # 4.49
WEAK = 0.72
S_GRID = [1e-3, 3e-3, 1e-2, 2e-2, 3e-2, 5e-2, 1e-1]
MODES = ["hard", "standing"]
DEMOGS = [("const1e4", c1e.const(1e4), 25), ("Gravel", c1e.gravel, 25), ("Gazave", c1e.gazave, 25),
          ("Nelson", c1e.nelson_g(0.017), 25), ("const1e4_gy20", c1e.const(1e4), 20), ("Gravel_gy20", c1e.gravel, 20)]
DESIGNS = {"v62": (1372, 680, 1_143_671), "v66": (395, 441, 1_143_230), "blog": (1112, 645, 1_211_499)}
STATS = ["Z50", "Z10", "M10", "N100", "B10"]
R_MC = 32
X0_KEEP = 0.8
SIZES = dict(K_anc=400_000, K_new=1_000, K_panel=400_000, K_cand=40_000, N_TARGET=1500, N_MIN=300, B_CAP=4.0e8, MAXPASS=4)
SMOKE_SIZES = dict(K_anc=20_000, K_new=100, K_panel=20_000, K_cand=2_000, N_TARGET=30, N_MIN=10, B_CAP=2.0e5, MAXPASS=1)
COLS = ["xE", "xA", "IE", "IA", "x7", "x6", "I7", "I6", "fixT", "a0"]
CI = {k: i for i, k in enumerate(COLS)}


# ------------------------------------------------------------------------------------------------ basics
def sel(x, s):
    """additive diploid selection, fitnesses 1, 1+s/2, 1+s"""
    return x * (1.0 + 0.5 * s + 0.5 * s * x) / (1.0 + s * x)


def kimura(p, s, ne):
    a = 2.0 * ne * s
    return -np.expm1(-a * p) / -np.expm1(-a)


def times(gy):
    return dict(t7=int(round(7500 / gy)), t6=int(round(6500 / gy)), win=int(round(7000 / gy)),
                start=int(round(START_BP / gy)))


def two_n_europe(fn, gy, T):
    t = np.arange(T + 1)
    bp = (t * gy).astype(float)
    ne = np.where(bp <= START_BP, fn(np.minimum(bp, START_BP)), NE_ANC)
    return np.maximum(2, np.rint(2 * ne)).astype(np.int64)


def p3(a):
    """P(African sample of 200 chromosomes has MAF >= 5%)"""
    a = np.clip(a, 0.0, 1.0)
    return binom.cdf(190, 200, a) - binom.cdf(9, 200, a)


# ------------------------------------------------------------------------------------------------ neutral sample
def neutral_sample(gy, sz, rng):
    """Scaled two-population neutral MC (N_s = 1000, f = 10).  Europe state at START_BP, Africa at present.
    w = expected number of such sites per genome bp."""
    Ns = 1000
    f = NE_ANC / Ns
    M = 2 * Ns
    split_steps = int(round(T_SPLIT_G / f))
    eu_steps = int(round((T_SPLIT_G - START_BP / gy) / f))
    i = np.arange(1, M)
    H = float(np.sum(1.0 / i))
    e = rng.choice(i, size=sz["K_anc"], p=(1.0 / i) / H) / M
    a = e.copy()
    new = np.empty(0)
    for st in range(split_steps):
        a = rng.binomial(M, a) / M
        if st < eu_steps:
            e = rng.binomial(M, e) / M
            if new.size:
                new = rng.binomial(M, new) / M
            new = np.concatenate([new, np.full(sz["K_new"], 1.0 / M)])
    E = np.concatenate([e, new])
    A = np.concatenate([a, np.zeros(new.size)])
    W = np.concatenate([np.full(e.size, THETA * H / sz["K_anc"]), np.full(new.size, THETA / 2 / sz["K_new"])])
    keep = (E > 0) | (A > 0)
    E, A, W = E[keep], A[keep], W[keep]
    h2 = W * 2 * A * (1 - A)
    q3 = W * p3(A)
    c2 = NPANEL / (L_GENOME * h2.sum())
    c3 = NPANEL / (L_GENOME * q3.sum())
    i2 = rng.choice(E.size, size=sz["K_panel"], p=h2 / h2.sum())
    i3 = rng.choice(E.size, size=sz["K_panel"], p=q3 / q3.sum())
    seg = (E > 0) & (E < 1)
    ws = W * seg
    return dict(c2=float(c2), c3=float(c3), pe=E[i2], pa=A[i2], pe3=E[i3], pa3=A[i3],
                ce=E[seg], ca=A[seg], cw=ws[seg] / ws.sum(), **standing_candidates(E[seg], A[seg], ws[seg] / ws.sum(),
                                                                                   sz["K_cand"], rng))


def standing_candidates(ce, ca, cw, K, rng, Ns=1000):
    """Draw K standing variants (European freq e, African freq a) by weight; give each its pre-onset integral
    I_pre = sum over its past of (1 - x), sampled as a neutral path from e conditioned on loss (reversibility),
    scaled N_s = 1000, f = NE_ANC / N_s generations per step."""
    f = NE_ANC / Ns
    M = 2 * Ns
    ix = rng.choice(ce.size, size=K, p=cw)
    e, a = ce[ix], ca[ix]
    I = np.zeros(K)
    x = e.copy()
    act = np.arange(K)
    for _ in range(200_000):
        if act.size == 0:
            break
        xa = rng.binomial(M, x[act]) / M
        I[act] += f * (1.0 - xa)
        x[act] = xa
        fixd = xa >= 1.0
        if fixd.any():                     # rejected path (fixed): restart from e
            r_ = act[fixd]
            x[r_] = e[r_]
            I[r_] = 0.0
        act = act[xa > 0.0]
    return dict(ke=e, ka=a, kI=I)


# ------------------------------------------------------------------------------------------------ sampling / events
def design_params(name):
    nneo, nmod, npan = DESIGNS[name]
    d = {b["bin"]: b for b in c1c.load_depth()}
    b7, b6, bm = d["7000-8000"], d["6000-7000"], d["0-500"]
    tot = b7["n_day"] + b6["n_day"]
    sc = nneo / tot
    return dict(ph7=int(round(b7["n_ph"] * sc)), dip7=int(round(b7["n_dip"] * sc)), ph6=int(round(b6["n_ph"] * sc)),
                p_ph7=b7["p_ph"], p_dip7=b7["p_dip"], p_ph6=b6["p_ph"], nmod=nmod, p_mod=bm["p_dip"], npanel=npan)


def event_probs(f7, f6, f0, dp, rng, chunk=50_000):
    """per-SNP probabilities of each statistic under Day's sampling (exact modern, MC Neolithic)."""
    f7, f6, f0 = (np.clip(np.asarray(v, float), 0.0, 1.0) for v in (f7, f6, f0))
    S = f0.size
    out = {k: np.zeros(S) for k in STATS}
    m = rng.binomial(dp["nmod"], dp["p_mod"], S)
    mchr = 2 * m
    with np.errstate(divide="ignore", invalid="ignore"):
        mono_b = np.where(f0 > 0, np.exp(mchr * np.log(np.where(f0 > 0, f0, 1.0))), 0.0)
        mono_o = np.where(f0 < 1, np.exp(mchr * np.log(np.where(f0 < 1, 1 - f0, 1.0))), 0.0)
    gt90 = binom.sf(np.floor(0.9 * mchr), mchr, f0)
    lt10 = binom.cdf(np.ceil(0.1 * mchr) - 1, mchr, f0)
    live = np.flatnonzero(np.maximum.reduce([mono_b, mono_o, gt90, lt10]) > 1e-7)
    for s0 in range(0, live.size, chunk):
        ix = live[s0:s0 + chunk]
        n = ix.size
        c7 = rng.binomial(dp["ph7"], dp["p_ph7"], n)
        d7 = rng.binomial(dp["dip7"], dp["p_dip7"], n) if dp["dip7"] else np.zeros(n, np.int64)
        c6 = rng.binomial(dp["ph6"], dp["p_ph6"], n)
        nind = c7 + d7 + c6
        n7 = c7 + 2 * d7
        nn = np.maximum(n7 + c6, 1)
        k = rng.binomial(n7[:, None], f7[ix, None], (n, R_MC)) + rng.binomial(c6[:, None], f6[ix, None], (n, R_MC))
        q = k / nn[:, None]
        lt50, gt50 = (q < 0.5).mean(1), (q > 0.5).mean(1)
        l10, g90 = (q < 0.1).mean(1), (q > 0.9).mean(1)
        mid = ((q >= 0.1) & (q <= 0.9)).mean(1)
        pb, po = (q < 1).mean(1), (q > 0).mean(1)
        ok = (nind >= 100) & (m[ix] >= 100)
        mb, mo = mono_b[ix], mono_o[ix]
        out["Z50"][ix] = ok * (mb * lt50 + mo * gt50)
        out["Z10"][ix] = ok * (mb * l10 + mo * g90)
        out["M10"][ix] = ok * ((mb + mo) * mid)
        out["N100"][ix] = ok * (mb * pb + mo * po)
        out["B10"][ix] = ok * (gt90[ix] * l10 + lt10[ix] * g90)
    return out


# ------------------------------------------------------------------------------------------------ neutral baseline
def neutral_task(demog, ns, rng):
    name, fn, gy = demog
    tm = times(gy)
    twoN = two_n_europe(fn, gy, tm["start"])
    res = {}
    for lab, pe in (("D2", ns["pe"]), ("D3", ns["pe3"])):
        x = pe.copy()
        rec = {}
        for t in range(tm["start"], -1, -1):
            if t == tm["t7"]:
                rec[7] = x.copy()
            if t == tm["t6"]:
                rec[6] = x.copy()
            if t == 0:
                break
            x = rng.binomial(twoN[t - 1], x) / twoN[t - 1]
        res[lab] = {}
        for dn in DESIGNS:
            dp = design_params(dn)
            ev = event_probs(rec[7], rec[6], x, dp, rng)
            sc = dp["npanel"] / pe.size
            res[lab][dn] = {k: float(ev[k].sum() * sc) for k in STATS}
    return res


# ------------------------------------------------------------------------------------------------ sweep engine
class Pool:
    def __init__(self, cap=1 << 15):
        self.A = np.zeros((len(COLS), cap))
        self.n = 0

    def add(self, block):
        k = block.shape[1]
        if self.n + k > self.A.shape[1]:
            B = np.zeros((len(COLS), max(2 * self.A.shape[1], self.n + k)))
            B[:, :self.n] = self.A[:, :self.n]
            self.A = B
        self.A[:, self.n:self.n + k] = block
        self.n += k

    def v(self):
        return self.A[:, :self.n]

    def compact(self, keep):
        w = self.A[:, :self.n][:, keep]
        self.A[:, :w.shape[1]] = w
        self.n = w.shape[1]


def run_pass(s, mode, twoN, T_hi, n_per_gen, gy, ns, rng):
    tm = times(gy)
    P = Pool()
    entries = 0
    for t in range(T_hi, -1, -1):
        if n_per_gen > 0:
            blk = np.zeros((len(COLS), n_per_gen))
            if mode == "hard":
                if t > T_SPLIT_G:
                    blk[CI["xE"]] = 1.0 / (2 * NE_ANC)
                    blk[CI["xA"]] = np.nan
                else:
                    blk[CI["xE"]] = 1.0 / twoN[t]
                    blk[CI["xA"]] = 0.0
                blk[CI["a0"]] = np.nan
            else:
                ix = rng.integers(0, ns["ke"].size, n_per_gen)
                blk[CI["xE"]] = ns["ke"][ix]
                blk[CI["xA"]] = ns["ka"][ix]
                blk[CI["a0"]] = ns["ka"][ix]
                blk[CI["IE"]] = ns["kI"][ix]
            blk[CI["x7"]] = blk[CI["xE"]]
            blk[CI["x6"]] = blk[CI["xE"]]
            blk[CI["I7"]] = blk[CI["IE"]]
            blk[CI["I6"]] = blk[CI["IE"]]
            blk[CI["fixT"]] = -1.0
            P.add(blk)
            entries += n_per_gen
        V = P.v()
        if t == tm["t7"]:
            V[CI["x7"]] = V[CI["xE"]]
            V[CI["I7"]] = V[CI["IE"]]
        if t == tm["t6"]:
            V[CI["x6"]] = V[CI["xE"]]
            V[CI["I6"]] = V[CI["IE"]]
        if t == 0:
            break
        N2 = twoN[t - 1]
        V[CI["xE"]] = rng.binomial(N2, sel(V[CI["xE"]], s)) / N2
        V[CI["IE"]] += 1.0 - V[CI["xE"]]
        if mode == "hard" and t - 1 < T_SPLIT_G:
            if t - 1 == T_SPLIT_G - 1:
                pre = np.isnan(V[CI["xA"]])
                V[CI["xA"], pre] = V[CI["xE"], pre]     # split happened at T_SPLIT_G: copy (one generation lag ok)
                V[CI["IA"], pre] = V[CI["IE"], pre]
            nA = int(2 * NE_AFR)
            V[CI["xA"]] = rng.binomial(nA, sel(V[CI["xA"]], s)) / nA
            V[CI["IA"]] += 1.0 - V[CI["xA"]]
        nf = (V[CI["xE"]] >= 1.0) & (V[CI["fixT"]] < 0)
        V[CI["fixT"], nf] = t - 1
        if (t % 16 == 0) or t - 1 in (tm["t7"], tm["t6"], 0):
            keep = (V[CI["xE"]] > 0) & ~(V[CI["fixT"]] > tm["t7"])
            P.compact(keep)
    V = P.v()
    keep = (V[CI["xE"]] > 0) & ~(V[CI["fixT"]] > tm["t7"])
    V = V[:, keep]
    wc = (V[CI["fixT"]] >= 0) & (V[CI["fixT"]] <= tm["win"])
    kept = V[:, V[CI["xE"]] >= X0_KEEP]
    return dict(V=kept, n_wc=int(wc.sum()), entries=entries,
                wc_x7_lt50=int(((V[CI["x7"]] < 0.5) & wc).sum()),
                wc_a=(V[CI["xA"]][wc] if mode == "hard" else V[CI["a0"]][wc]))


def sweep_events(V, mode, ns, rng, max_snps=1_000_000):
    """expected events (hitchhikers + focal) per statistic/design for kept sweeps; returns sums incl. per-sweep Q.
    Hitchhiker SNPs are generated and evaluated in chunks of sweeps (memory bound ~1e6 SNPs per chunk)."""
    nsw = V.shape[1]
    x7, x6, x0 = V[CI["x7"]], V[CI["x6"]], V[CI["xE"]]
    I7, I6, I0 = V[CI["I7"]], V[CI["I6"]], V[CI["IE"]]
    aN = np.nan_to_num(V[CI["xA"]] if mode == "hard" else V[CI["a0"]])
    IA = V[CI["IA"]]
    lam = NPANEL / MAP_M
    rmax = np.minimum(0.5, 8.0 / np.maximum(I0, 1.0))
    nh = rng.poisson(lam * 2 * rmax)
    dps = {dn: design_params(dn) for dn in DESIGNS}
    keys = [(dn, lab, k) for dn in DESIGNS for lab in ("D2", "D3") for k in STATS]
    Eh = {kk: np.zeros(nsw) for kk in keys}
    lq = {kk: np.zeros(nsw) for kk in keys}
    # chunks of sweeps
    bounds, cur, acc = [], 0, 0
    for jsw in range(nsw):
        acc += int(nh[jsw])
        if acc >= max_snps:
            bounds.append((cur, jsw + 1))
            cur, acc = jsw + 1, 0
    if cur < nsw:
        bounds.append((cur, nsw))
    nsnp = 0
    for lo, hi in bounds:
        sid = np.repeat(np.arange(lo, hi), nh[lo:hi])
        if sid.size == 0:
            continue
        nsnp += sid.size
        r = rng.random(sid.size) * rmax[sid]
        j = rng.integers(0, ns["pe"].size, sid.size)
        p, ap = ns["pe"][j], ns["pa"][j]
        beta = (rng.random(sid.size) < p).astype(float)

        def hh(xk, Ik):
            Ek = -np.expm1(-r * Ik[sid])
            return xk[sid] * ((1 - Ek) * beta + Ek * p) + (1 - xk[sid]) * p
        f7, f6, f0 = hh(x7, I7), hh(x6, I6), hh(x0, I0)
        if mode == "hard":
            EA = -np.expm1(-r * IA[sid])
            ah = aN[sid] * ((1 - EA) * beta + EA * ap) + (1 - aN[sid]) * ap
            wts = {"D2": (2 * ah * (1 - ah)) / np.maximum(2 * ap * (1 - ap), 1e-300),
                   "D3": p3(ah) / np.maximum(p3(ap), 1e-300)}
        else:
            wts = {"D2": np.ones(sid.size), "D3": np.ones(sid.size)}
        for dn in DESIGNS:
            sc = dps[dn]["npanel"] / NPANEL
            evh = event_probs(f7, f6, f0, dps[dn], rng)
            for lab in ("D2", "D3"):
                for k in STATS:
                    ph = np.minimum(wts[lab] * evh[k] * sc, 1.0)
                    Eh[(dn, lab, k)] += np.bincount(sid, ph, minlength=nsw)
                    lq[(dn, lab, k)] += np.bincount(sid, np.log1p(-np.minimum(ph, 1 - 1e-12)), minlength=nsw)
    wf = {"D2": ns["c2"] * 2 * aN * (1 - aN), "D3": ns["c3"] * p3(aN)}
    out = {}
    for dn in DESIGNS:
        evf = event_probs(x7, x6, x0, dps[dn], rng)
        out[dn] = {}
        for lab in ("D2", "D3"):
            out[dn][lab] = {}
            for k in STATS:
                pf = np.minimum(wf[lab] * evf[k], 1.0)
                L = lq[(dn, lab, k)] + np.log1p(-np.minimum(pf, 1 - 1e-12))
                out[dn][lab][k] = dict(E_hh=float(Eh[(dn, lab, k)].sum()), E_f=float(pf.sum()),
                                       Q=float((-np.expm1(L)).sum()))
    return out, int(nsnp)


def add_into(acc, new):
    for dn in new:
        for lab in new[dn]:
            for k in new[dn][lab]:
                for f in new[dn][lab][k]:
                    acc.setdefault(dn, {}).setdefault(lab, {}).setdefault(k, {}).setdefault(f, 0.0)
                    acc[dn][lab][k][f] += new[dn][lab][k][f]


def sweep_task(s, mode, demog, ns, seed_key, sz):
    name, fn, gy = demog
    tm = times(gy)
    tfix = 4.0 * math.log(max(NE_ANC * s, 2.0)) / s
    T_hi = int(tm["win"] + 3 * tfix)
    if mode == "standing":
        T_hi = min(T_SPLIT_G, T_hi)
        pf = float(np.sum(ns["cw"] * kimura(ns["ce"], s, NE_ANC)))
    else:
        pf = s
    twoN = two_n_europe(fn, gy, max(T_hi, T_SPLIT_G) + 1)
    B = float(np.clip(sz["N_TARGET"] * T_hi / (pf * tm["win"] * 0.8), 1e4, sz["B_CAP"]))
    acc, n_wc, entries, x7lt, nsnp, nkept, passes = {}, 0, 0, 0, 0, 0, 0
    wa = []
    t0 = time.time()
    while passes < sz["MAXPASS"]:
        rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 1, seed_key, passes]))
        npg = max(1, int(math.ceil(B / (T_hi + 1))))
        r = run_pass(s, mode, twoN, T_hi, npg, gy, ns, rng)
        ev, ns_snp = sweep_events(r["V"], mode, ns, rng)
        add_into(acc, ev)
        n_wc += r["n_wc"]
        entries += r["entries"]
        x7lt += r["wc_x7_lt50"]
        nsnp += ns_snp
        nkept += r["V"].shape[1]
        wa.append(r["wc_a"])
        passes += 1
        if n_wc >= sz["N_MIN"] or entries >= sz["B_CAP"]:
            break
        B = min(sz["B_CAP"] - entries, B * min(10.0, sz["N_TARGET"] / max(n_wc, 1)))
        if B < 1:
            break
    wa = np.concatenate(wa) if wa else np.empty(0)
    wa = np.nan_to_num(wa)
    return dict(meta=dict(s=s, mode=mode, demog=name, gy=gy, T_hi=T_hi, entries=entries, passes=passes, n_wc=n_wc,
                          wc_x7_lt50=x7lt, n_kept=nkept, n_hh_snps=nsnp, secs=round(time.time() - t0, 1),
                          c2=ns["c2"], c3=ns["c3"], uniform_share=NPANEL / L_GENOME,
                          focal_incl_D2=float(np.sum(ns["c2"] * 2 * wa * (1 - wa))),
                          focal_incl_D3=float(np.sum(ns["c3"] * p3(wa)))),
                sums=acc)


# ------------------------------------------------------------------------------------------------ tasks / main
def task_list():
    L = [("neutral", None, None, d) for d in DEMOGS]
    for d in DEMOGS:
        for mode in MODES:
            for s in S_GRID:
                L.append(("sweep", s, mode, d))
    return L


def task_name(tk):
    kind, s, mode, d = tk
    return "neutral_%s" % d[0] if kind == "neutral" else "sweep_%s_%s_s%g" % (d[0], mode, s)


_NS = {}


def get_ns(gy, sz):
    if gy not in _NS:
        _NS[gy] = neutral_sample(gy, sz, np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 0, gy])))
    return _NS[gy]


def run_task_k(a):
    k, outdir, sz = a
    return run_task((k, task_list()[k], outdir, sz))


def run_task(args):
    k, tk, outdir, sz = args
    kind, s, mode, d = tk
    fn = os.path.join(outdir, "l5_%s.json" % task_name(tk))
    if os.path.exists(fn):
        return fn
    t0 = time.time()
    ns = get_ns(d[2], sz)
    if kind == "neutral":
        rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 1, k, 0]))
        res = dict(meta=dict(demog=d[0], gy=d[2], c2=ns["c2"], c3=ns["c3"]), neutral=neutral_task(d, ns, rng))
    else:
        res = sweep_task(s, mode, d, ns, k, sz)
    res["meta"]["task"] = task_name(tk)
    res["meta"]["wall"] = round(time.time() - t0, 1)
    with open(fn + ".tmp", "w") as f:
        json.dump(res, f)
    os.replace(fn + ".tmp", fn)
    print("done %s %.0fs" % (task_name(tk), time.time() - t0), flush=True)
    return fn


def cost(tk):
    kind, s, mode, d = tk
    if kind == "neutral":
        return 1.0
    return (10.0 if mode == "hard" else 2.0) / s


# ------------------------------------------------------------------------------------------------ selftest
def selftest(small=False, outdir=None):
    rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 9, 1]))
    res = {}
    # V2a fixation probability
    N, s, n0 = 1000, 0.02, (40_000 if small else 200_000)
    x = np.full(n0, 1.0 / (2 * N))
    fixed = 0
    while x.size:
        x = rng.binomial(2 * N, sel(x, s)) / (2 * N)
        fixed += int((x >= 1).sum())
        x = x[(x > 0) & (x < 1)]
    pk = float(kimura(1.0 / (2 * N), s, N))
    res["V2_pfix"] = dict(sim=fixed / n0, kimura=pk, ok=abs(fixed / n0 / pk - 1) < 0.10)
    # V2b event sanity
    dp = design_params("v62")
    ev = event_probs(np.array([0.3, 0.97, 0.5]), np.array([0.3, 0.97, 0.5]), np.array([1.0, 1.0, 0.5]), dp, rng)
    res["V2_events"] = dict(Z50=[float(v) for v in ev["Z50"]], N100=[float(v) for v in ev["N100"]],
                            ok=bool(ev["Z50"][0] > 0.99 and ev["Z50"][1] < 1e-9 and ev["N100"][1] > 0.99
                                    and max(ev[k][2] for k in STATS) < 1e-9))
    # V3 hitchhiking: explicit two-locus haploid-gamete WF, founder carries B; compare final b share to formula
    N, s, pB = 1000, 0.1, 0.3
    v3 = {}
    for r in (1e-4, 1e-3, 5e-3):
        sims, preds = [], []
        target = 60 if small else 300
        tries = 0
        while len(sims) < target and tries < 100_000:
            tries += 1
            g = np.array([1.0, 0.0, pB - 1.0 / (2 * N), 1 - pB]) / 1.0     # AB, Ab, aB, ab
            g[0] = 1.0 / (2 * N)
            g = g / g.sum()
            I = 0.0
            while True:
                xa = g[0] + g[1]
                xs = sel(xa, s)
                fac_A = xs / xa if xa > 0 else 0.0
                fac_a = (1 - xs) / (1 - xa) if xa < 1 else 0.0
                g2 = g * np.array([fac_A, fac_A, fac_a, fac_a])
                D = g2[0] * g2[3] - g2[1] * g2[2]
                g2 = g2 + np.array([-r * D, r * D, r * D, -r * D])
                g2 = np.clip(g2, 0, None)
                g = rng.multinomial(2 * N, g2 / g2.sum()) / (2 * N)
                xa = g[0] + g[1]
                I += 1 - xa
                if xa <= 0 or xa >= 1:
                    break
            if xa >= 1:
                sims.append(g[1])                       # share of A chromosomes carrying b
                preds.append(-math.expm1(-r * I) * (1 - pB))
        ms, mp = float(np.mean(sims)), float(np.mean(preds))
        v3[str(r)] = dict(sim=ms, pred=mp, n=len(sims), ok=bool(abs(ms - mp) <= max(0.01, 0.30 * mp)))
    res["V3_hitchhike"] = v3
    res["ok"] = bool(res["V2_pfix"]["ok"] and res["V2_events"]["ok"] and all(v["ok"] for v in v3.values()))
    for k in ("V2_pfix", "V2_events"):
        print(k, "ok" if res[k]["ok"] else "FAIL", flush=True)
    for r, v in v3.items():
        print("V3 r=%s" % r, "ok" if v["ok"] else "FAIL", flush=True)
    if outdir:
        with open(os.path.join(outdir, "l5_selftest.json"), "w") as f:
            json.dump(res, f, indent=1)
    return res


# ------------------------------------------------------------------------------------------------ analyse
def analyse(outdir):
    import glob
    R = {}
    for fn in glob.glob(os.path.join(outdir, "l5_*.json")):
        if fn.endswith("selftest.json"):
            continue
        R[json.load(open(fn))["meta"]["task"]] = json.load(open(fn))
    st = os.path.join(outdir, "l5_selftest.json")
    if os.path.exists(st):
        print("selftest:", json.dumps(json.load(open(st))))
    print("tasks loaded: %d of %d" % (len(R), len(task_list())))
    PRIM = [("v62", "Z50"), ("v66", "Z50"), ("blog", "B10")]

    def neutral_E(dname, lab="D2"):
        r = R.get("neutral_%s" % dname)
        return r["neutral"][lab] if r else None

    def rho(dname, mode, s, lab="D2"):
        r = R.get("sweep_%s_%s_s%g" % (dname, mode, s))
        if not r or r["meta"]["n_wc"] < 100:
            return None
        n = r["meta"]["n_wc"]
        out = {}
        for dn in DESIGNS:
            for k in STATS:
                c = r["sums"][dn][lab][k]
                out[(dn, k)] = dict(rho=(c["E_hh"] + c["E_f"]) / n, q=c["Q"] / n,
                                    hh_share=(c["E_hh"] / (c["E_hh"] + c["E_f"]) if c["E_hh"] + c["E_f"] > 0 else None))
        out["meta"] = r["meta"]
        return out

    def model(dname, lab, F_of_s):
        """F_of_s: list of (s, weight F); returns E, P0 for primary stat (max-E of PRIM), plus all."""
        ne = neutral_E(dname, lab)
        res = {}
        for mode in MODES:
            parts = [(rho(dname, mode, s, lab), F) for s, F in F_of_s]
            if any(p is None for p, _ in parts) or ne is None:
                res[mode] = None
                continue
            tab = {}
            for dn in DESIGNS:
                for k in STATS:
                    E = sum(F * p[(dn, k)]["rho"] for p, F in parts) + ne[dn][k]
                    lq = sum(F * p[(dn, k)]["q"] for p, F in parts) + ne[dn][k]
                    tab[(dn, k)] = (E, math.exp(-lq))
            best = max(PRIM, key=lambda dk: tab[dk][0])
            res[mode] = dict(E=tab[best][0], P0=tab[best][1], stat=best, M10_v62=tab[("v62", "M10")][0],
                             M10_v66=tab[("v66", "M10")][0], all=tab)
        return res

    print("\n== (i) neutral: expected counts (D2; D3 in brackets)")
    for d in DEMOGS:
        a, b = neutral_E(d[0], "D2"), neutral_E(d[0], "D3")
        if a:
            print("%-14s " % d[0] + "  ".join("%s/%s %.3g [%.3g]" % (dn, k, a[dn][k], b[dn][k])
                                              for dn in DESIGNS for k in STATS if not (dn == "blog") or k == "B10"))
    print("\n== (ii) mainstream (F = %.2f per window; 72%% s=1e-3, 28%% s=1e-2), D2" % F_MS)
    for mult in (1, ALPHA_HI / ALPHA, 10, 100):
        for d in DEMOGS:
            m = model(d[0], "D2", [(1e-3, WEAK * F_MS * mult), (1e-2, (1 - WEAK) * F_MS * mult)])
            print("x%-5.3g %-14s " % (mult, d[0]) + "  ".join(
                "%s E=%.3g P0=%.3g (%s)" % (mo, m[mo]["E"], m[mo]["P0"], "/".join(m[mo]["stat"])) if m[mo] else "%s n/a" % mo
                for mo in MODES))
    print("\n== (iii) Day's required rate (F = %.0f completions per window), D2 [D3]" % F_DAY)
    med = {}
    for mode in MODES:
        for s in S_GRID:
            row, Es = [], []
            for d in DEMOGS:
                m2 = model(d[0], "D2", [(s, F_DAY)])[mode]
                m3 = model(d[0], "D3", [(s, F_DAY)])[mode]
                rr = rho(d[0], mode, s)
                if m2 is None:
                    row.append("%s n/a" % d[0])
                    continue
                if d[2] == 25:
                    Es.append(m2["E"])
                hs = rr[m2["stat"]]["hh_share"] if rr else None
                row.append("%s E=%.3g [%.3g] P0=%.2g M10=%.3g/%.3g hh=%s wc=%d x7<.5=%d fD2=%.2g" % (
                    d[0], m2["E"], m3["E"] if m3 else float("nan"), m2["P0"], m2["M10_v62"], m2["M10_v66"],
                    "%.2f" % hs if hs is not None else "-", rr["meta"]["n_wc"], rr["meta"]["wc_x7_lt50"],
                    rr["meta"]["focal_incl_D2"] / max(rr["meta"]["n_wc"], 1)))
            med[(mode, s)] = float(np.median(Es)) if len(Es) == 4 else None
            print("%-8s s=%-6g median(gy25)=%s\n    %s" % (mode, s, med[(mode, s)], "\n    ".join(row)))
    # band
    day = all(med.get((mo, s)) is not None and med[(mo, s)] >= 3 for mo in MODES for s in S_GRID if s >= 3e-3)
    crit_iii = True
    for mo in MODES:
        for s in S_GRID:
            if s <= 1e-2:
                for d in DEMOGS[:4]:
                    m = model(d[0], "D2", [(s, F_DAY)])[mo]
                    if m is None or m["E"] > 1:
                        crit_iii = False
    crit_ii = True
    for d in DEMOGS[:4]:
        m = model(d[0], "D2", [(1e-3, WEAK * F_MS), (1e-2, (1 - WEAK) * F_MS)])
        for mo in MODES:
            if m[mo] is None or m[mo]["E"] > 0.1:
                crit_ii = False
    sstar = {mo: next((s for s in S_GRID if med.get((mo, s)) is not None and med[(mo, s)] >= 3), None) for mo in MODES}
    band = "DAY" if day else ("CRITIC" if (crit_iii and crit_ii) else "MIDDLE")
    print("\n== BAND: %s   (Day condition %s; critic (iii) %s, (ii) %s); s* by mode: %s" % (band, day, crit_iii, crit_ii, sstar))
    print("Day's own beneficial s (1e-3, Zeng 2021 as used by Day): " + ", ".join(
        "%s median E=%s" % (mo, med.get((mo, 1e-3))) for mo in MODES))


# ------------------------------------------------------------------------------------------------ entry
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if cmd == "selftest":
        selftest(small=False, outdir=sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd == "smoke":
        outdir = sys.argv[2]
        os.makedirs(outdir, exist_ok=True)
        t0 = time.time()
        selftest(small=True)
        print("selftest(small) %.1fs" % (time.time() - t0), flush=True)
        tl = task_list()
        pick = [tl[0], next(t for t in tl if t[0] == "sweep" and t[1] == 5e-2 and t[2] == "hard"),
                next(t for t in tl if t[0] == "sweep" and t[1] == 5e-2 and t[2] == "standing" and t[3][0] == "Gravel")]
        for k, tk in enumerate(pick):
            t1 = time.time()
            fn = run_task((tl.index(tk), tk, outdir, SMOKE_SIZES))
            meta = json.load(open(fn))["meta"]
            print("smoke %s: %.1fs keys=%s" % (task_name(tk), time.time() - t1,
                  {k2: meta[k2] for k2 in ("n_wc", "n_kept", "n_hh_snps", "entries", "passes") if k2 in meta}), flush=True)
        print("smoke total %.1fs" % (time.time() - t0))
    elif cmd == "main":
        import multiprocessing as mp
        workers = int(sys.argv[2])
        outdir = sys.argv[3]
        os.makedirs(outdir, exist_ok=True)
        st = selftest(small=False, outdir=outdir)
        tl = task_list()
        # post hoc 2026-10-13 (pre-run, launch fix): a task tuple holds a demography lambda (c1e.const), which the
        # forkserver pool cannot pickle; send the task index and rebuild the tuple in the worker.  Order, seeds
        # (keyed on k) and outputs are unchanged.
        jobs = [(k, outdir, SIZES) for k, tk in sorted(enumerate(tl), key=lambda a: -cost(a[1]))]
        with mp.get_context("forkserver").Pool(workers, maxtasksperchild=4) as pool:
            for _ in pool.imap_unordered(run_task_k, jobs):
                pass
        print("all done", flush=True)
    elif cmd == "analyse":
        analyse(sys.argv[2])
    else:
        sys.exit("unknown command")
