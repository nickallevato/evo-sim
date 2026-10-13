"""FMnull-S4: criterion S4 of FMnull (tree-incongruent sharing above the ILS rate), run post hoc.

POST HOC RELATIVE TO FMnull.  S4 was registered in `fm_mesa_null.py` (48241c7, 2026-10-12) and never run
(R4-FMnull.md section 7: "Not tested by this script ... To be queued, or dropped with a stated reason").  This
script operationalises it on 2026-10-13, AFTER FMnull's results (index, phi_HC, corr(H, C), corr(H, G)) were
seen.  Every number and threshold below is fixed in this docstring BEFORE any run of the simulation null or of the
real-data arm.  Only `selftest` (assertions on micro inputs; it prints no statistic of the null or of the data)
had run before this commit.  Later changes go in separate commits labelled "post hoc".
Brief: research/checks/briefs/FMnull-S4-analyst.md.  Task EVO-14 (parent EVO-13).

DECISION ON THE TWO OPEN PIECES (brief, Goal)
  1. S4 is RUN, not dropped.  The held bins already count the site patterns S4 needs (fm_mesa_replication.py
     FIELDS: HCs, iHG, iCG; R4-FM used iHG + iCG only as a covariate), the run is cheap, and an unrun registered
     criterion is a pre-registration defect either way.  What S4 can and cannot detect is stated before the run
     (POWER below): in particular it has, by construction, almost no power against the one-lineage block
     mechanism Q168 describes, and the verdict table is written with that in view.
  2. The Poisson GLM re-estimate of the covariate-adjusted index is OUT OF SCOPE, explicitly.  Reason: S1 is a
     conjunction ("index far above N_hi at EVERY plausible W (and after covariate regression)"); its first clause
     is already not met on raw phi (no measured cell above 3 N_hi under any parameter set, R4-FMnull section 7),
     so no value of the covariate-adjusted index can make S1 met; and amendment A13 dropped "covariate
     correlations" as a critic-side criterion.  The re-estimate could change no registered class for either
     side.  It is not run; fm_bins.npz is not re-read for it.

TIER.  LOAD-BEARING (three reviews: correctness, steelman-day, steelman-critic).  FMnull feeds FM3 and FM10, both
`load_bearing: true` in hierarchy.yaml.

TARGET QUOTES (verbatim; voxday.net "The Fourth Mechanism", 2026-10-10; local copy and hash in quotes-day.md)
  Q168 (FM7, ¶6) "I propose the term sigillation for the hypothesis that some of these mesa regions represent
       deliberate genomic modification: discrete engineering events that wrote contiguous blocks of change into
       one dominate lineage."
  Q169 (FM8, ¶7) "what the data establish beyond any dispute is that a) the mesa signature exists, b) that it is
       the dominant source of genomic divergence between humans and the great apes, and, c) no account of
       speciation is complete without it."
  Q171 (FM10, ¶8) "What we do know is that neither natural selection nor neutral diffusive drift can still be
       considered viable candidates."
  Day has said nothing about tree incongruence, gorilla, ILS or site patterns (quotes-day.md, refreshes to
  2026-10-13).  S4 is the AUDIT's criterion, written into FMnull as one of four "Day-supporting observables".

THE REGISTERED CRITERION (fm_mesa_null.py, 48241c7, verbatim)
  "S4  tree-incongruent sharing: mesas shared by H and G but not C (or C and G, not H) above the ILS rate
       (Scally2012: "In 30% of the genome, gorilla is closer to human or chimpanzee than the latter are to each
       other", held) at matched density."  Scored DAY "if met by > 3x the relevant neutral upper bound".

DATA.  raw/fm_bins.npz (na-workhorse only; md5 716db19e2ed5a43015a49f0b7a5ff98c in raw/fmnull.host): 1-kb hs1
  bins, classes rep + 2 cpg + 4 dup, fields (fm_mesa_replication.py, verbatim definitions, all require hs1 ==
  hg38 and the six core genomes present):
    HCs  h == c != g == o            human-chimp stem (tree-congruent)
    iHG  h == g != c == b == o       human and gorilla share a derived state
    iCG  c == g != h == o            chimp and gorilla share a derived state (bonobo unconstrained)
    H, C, G                          lineage fields, used for density matching only
  The two incongruent fields are defined asymmetrically (b constrained in iHG only).  Every statistic below is
  centred on the measured genome share, never on 1/2, so a constant definitional offset cannot score.
  Labels read from the npz are ASSERTED (meta fields, bin size, class encoding): the FMnull label bug dropped
  cells silently.  Filters as in R4-FM: F2 (dup = 0, non-repeat) GOVERNS; F3 (F2 and non-CpG) reported beside
  it; F0 (all classes) reported and labelled ALN-dependent, never scored (the S4 null has no alignment term).
  Autosomes only.  A window is used if its core columns m >= 0.5 W (fm.windows).

STATISTICS (readings of S4; rule RD: every reading reported; how the readings combine is fixed below)
  S4-A  ASYMMETRY ("H and G but not C, or C and G but not H").  x = iHG, n = iHG + iCG per window; a = genome
        share sum x / sum n.  phi_A = sum (x - n a)^2 / (n a (1 - a)) / (k - 1) over used windows with n > 0
        (= fm_mesa_null.split_phi).  Under ILS in a panmictic ancestor the two incongruent topologies are equally
        likely at EVERY locus, whatever the local ancestral Ne or recombination rate, so regional ILS-rate
        variation cannot create asymmetry; what remains is clustering of sites within shared genealogical
        tracts, which the coalescent null below models.  W in {10, 30, 100, 300, 1000} kb scored; 3000 kb
        reported only (too few simulated windows).
  S4-M  HG / CG MESAS (the literal "mesas").  At W in {30, 100} kb, a window is eligible if used and n >= 10; it
        is HG-excess if x / n - a >= 0.30, CG-excess if x / n - a <= -0.30.  A mesa is a maximal run of >= 3
        consecutive eligible same-direction windows on one chromosome (an ineligible window breaks the run, as
        in R4-FM's mesa rule).  Statistic: M = number of HG mesas + CG mesas (each direction also reported).
  S4-R  RATE AT MATCHED DENSITY ("above the ILS rate ... at matched density").  I = iHG + iCG, N = I + HCs per
        window.  Windows (used, N > 0) are split into deciles of total lineage density (H + C + G) / m; q_s =
        sum I / sum N within decile s.  phi_R = sum (I - N q_s)^2 / (N q_s (1 - q_s)) / (k - 10).  Matching on
        density absorbs the homoplasy trend (parallel mutation rises with local rate).  Unstratified phi_R0 is
        reported, not scored.
  Descriptive only: a, q-bar, mean n and N per window, mean exposure, Spearman(q_w, H density), counts by
  direction.

NULL MODEL (msprime 1.4.4 coalescent with recombination, pinned in requirements; JC69 mutations on a discrete
genome, so homoplasy is present).  One haploid genome each of H, C, G and orangutan O.
  Species tree ((H, C), G), O.  H-C split t1 = 4.1 My (FML-H1); HCG split t1 + 2.0 My (A11 quote of Hobolth
  2007: "approximately 2 Myr earlier"); O split 18 My (the assumption Hobolth states, FML-H1 note); generation 25
  y (Hobolth's assumption).  Ancestral sizes N_HC in {35,000, 95,000} and N_HCG in {35,000, 55,000} (FML-H1:
  65,000 +/- 30,000 and 45,000 +/- 10,000; SOURCED).  N_HCGO = N_HCG (UNSOURCED convention).  This replaces the
  ILS sigma bracket the brief names (0.30-0.54 single-epoch): the null uses the same N range directly and never
  uses sigma.  Terminal sizes are irrelevant (one genome per species).
  Recombination r in {1.0e-8, 1.5e-8} per bp per generation (UNSOURCED convention; 1.5 cM/Mb is Hobolth's
  simulation setting, not an estimate).  Heterogeneity RHET in {0, 1.0}: none, or piecewise-constant r over 50-kb
  segments, log-normal with sigma_ln 1.0 and mean r (UNSOURCED; a stand-in for coldspots, which lengthen tracts).
  Linked selection on ancestral Ne (Scally2012: ILS "rarer around coding genes"; the "ILS rate" S4 cites is the
  observed one, which contains it): BGS in {none, (sd 0.32, ell 0.2 Mb), (sd 0.32, ell 2 Mb)}: independent
  segments of length ell, each with every ancestral N multiplied by a log-normal factor of mean 1 and SD 0.32
  (= sd(B) 0.25 / mean(B) 0.78; sd(B) UNSOURCED as in FMnull, mean(B) FML-M2).  Segment blocks stand in for an
  exponential autocorrelation (simplification).
  Mutation rate: calibrated per configuration so that the H-lineage field density is D_H_SIM = 0.006 at full
  exposure (expected H-private branch length from tskit branch statistics on a 2-Mb pilot, seed fixed per
  configuration).  Each data cell is matched by binomial thinning of the simulated window counts with factor
  c_w x rho: c_w = a per-window exposure m / W drawn from the data cell's own exposure distribution (101
  quantiles), rho = (H density of the data cell) / (realised H density of the configuration; CENTRAL's for the
  planted runs, whose extra H sites must not re-calibrate them; planted runs also share CENTRAL's thinning draws).  Binomial thinning
  of window sums is exactly independent per-site thinning, so the clustering term scales as it should; masking
  in the data is in blocks (repeats), not per site, and adjacent windows' exposures are drawn independently
  (both simplifications, disclosed).  rho > 1 is capped at 1 and flagged.
  Simplifications kept: bonobo not simulated (b = c, so iHG's b constraint is vacuous in the null); hs1 = hg38;
  no alignment error (hence F0 not scored); no gene conversion; one constant population per epoch.
  Grid: 2 (N_HC) x 2 (N_HCG) x 2 (r) x 2 (RHET) x 3 (BGS) = 48 CORNERS, plus CENTRAL (N_HC 65,000, N_HCG 45,000,
  r 1.25e-8, RHET 0, no BGS) used only as the base of the planted scenarios.  Genome per configuration: 1000 Mb
  as 100 chunks of 10 Mb (windows never span chunks).  POST HOC, PRE-RUN (after the local smoke, no data and no
  full-size null seen): was 200 Mb with a 100-Mb fallback.  Reason: the smoke measured ~0.05 CPU-s per 0.2 Mb
  per configuration (~1 CPU-h for the whole 200-Mb grid), and at 200 Mb (~2,000 simulated 100-kb windows against
  ~9,500 F2 data windows) the Poisson upper limit of a null mesa count of 0 already scales to E_hi ~ 17, so S4-M
  could miss DAY for simulation size alone; 1000 Mb brings that floor to ~3.5.  Fallback fixed now: if the
  compute-host smoke projects a wall time above 8 h at the allowed number of processes, 500 Mb, then 200 Mb; the
  .host file records which.

BANDS (per statistic, filter, W; computed from the 48 corners after thinning to the data cell)
  phi statistics: for corner c, value v_c and a leave-one-chunk-out jackknife SE_c (one group per chunk).
    N_lo = min_c (v_c - 2 SE_c), N_hi = max_c (v_c + 2 SE_c).  FULL band (all 48) GOVERNS.  Reported beside it:
    band N (no BGS, 16 corners) and band U (no BGS, RHET 0: 8 corners, the narrowest).
  S4-M counts: corner count M_c on k_c eligible windows, scaled to the data's eligible windows k_d:
    E_lo = min_c LCL_2.5%(M_c) k_d / k_c, E_hi = max_c UCL_97.5%(M_c) k_d / k_c (exact Poisson limits; for M_c = 0
    the UCL is 3.69, so E_hi is never 0).
  The +/- 2 SE and the Poisson limits widen every band in BOTH directions: DAY and BELOW are both harder.

CLASSES (exhaustive; every value lands in exactly one)
  phi statistics (FMnull amendment A4, classify2, unchanged):
    DAY            v > 3 N_hi
    MARGINAL-OUT   N_hi < v <= 3 N_hi
    MARGINAL-IN    max(N_hi / 3, N_c) < v <= N_hi,   N_c = 1 + sqrt(max(N_lo - 1, 0) max(N_hi - 1, 0))
    CRITIC         N_lo <= v <= max(N_hi / 3, N_c)
    BELOW-NEAR     N_lo / 3 <= v < N_lo;  BELOW-FAR v < N_lo / 3
  S4-M counts:
    DAY            M > 3 E_hi AND P(Poisson(E_hi) >= M) < 1e-3
    MARGINAL-OUT   M > E_hi and not DAY
    MARGINAL-IN    max(E_hi / 3, sqrt(E_lo E_hi)) < M <= E_hi
    CRITIC         E_lo <= M <= max(E_hi / 3, sqrt(E_lo E_hi))
    BELOW          M < E_lo
  UNSCORED         fewer than 20 used windows in the data cell, or a statistic undefined (n or N all zero).
  NON-DISCRIMINATING (label on CRITIC and MARGINAL-IN, fixed now; the FMnull fix-pass convention made a rule
  here): band width (N_hi - 1) / (N_lo - 1) > 9 (phi; infinite if N_lo <= 1) or E_hi / E_lo > 9 (counts;
  infinite if E_lo = 0).
  AGGREGATE S4 (F2 governs): S4-DAY if any of S4-A (any scored W), S4-M (30 or 100 kb), S4-R (any scored W) is
  DAY on F2; else S4-MARGINAL if any is MARGINAL-OUT; else S4-NOT-MET (all CRITIC, MARGINAL-IN, BELOW or
  UNSCORED, at least one scored).  F3 and F0 never change the aggregate; disagreements are reported
  (F3 lower = CpG-dependent; F0 higher = ALN-dependent).

PLANTED SCENARIOS (power, both ways; CENTRAL demography, same chunk seeds as CENTRAL, thinned to the F2 cell)
  Q168 one-lineage blocks (H-only extra substitutions, rate e x D_H_SIM per bp, over blocks of length Lb covering
  fraction f; an extra H mutation at an existing variant site moves h to one of the three other bases at random,
  so it can create or destroy iHG, iCG and HCs sites exactly as in the data):
    Q1  f 0.02, e 1, Lb 100 kb        (FMnull's registered block model)
    Q2  f 0.5,  e 2, Lb 100 kb        (FMnull's "dominant" model, audit gloss of Q169 (b): f e > 1)
  Non-tree two-lineage blocks (the alternative S4 was written for: inside a block, a fraction s of the 1-kb bins
  is taken from a simulation under the swapped species tree ((H, G), C), same split times and sizes):
    T1  f 0.02,  Lb 100 kb, s 1        T2  f 0.02, Lb 300 kb, s 1        T3  f 0.005, Lb 300 kb, s 1
    T4  f 0.5,   Lb 100 kb, s 1        T5  f 0.5,  Lb 1 Mb,   s 1        T6  f 0.1,   Lb 300 kb, s 0.5
  Blocks are placed on a grid of Lb slots with a random phase per chunk (FMnull's grid-phase lesson).  T3 has
  about 17 blocks per 1000 Mb; its yield is also reported per block, and as projected from T2's yield per block.

PREDICTIONS (fixed now; hand values from the formulas in HAND below; the scoring code in `post` implements each)
  P1 S4-A on F2.  Critic side: CRITIC or MARGINAL-IN at every scored W.  Day side (S4 read as a test of a
     fourth mechanism, the audit's steelman; Day has not predicted it): DAY at some W >= 100 kb.  Audit: F2 phi_A
     in [1.5, 8] at every scored W, and phi_A(1 Mb) / phi_A(10 kb) <= 3.
  P2 S4-M on F2.  Critic side: neither DAY nor MARGINAL-OUT at 30 or 100 kb.  Day side: DAY at 100 kb.
  P3 S4-R on F2.  Critic side: CRITIC or MARGINAL-IN at every scored W.  Day side: DAY at some W.  Audit: the
     FULL band is NON-DISCRIMINATING (width > 9) at W >= 300 kb (BGS with sd 0.32 makes the upper edge large).
  P4 Power against Q168 (no side has predicted it; it decides what a non-DAY S4 can mean).  Q1 and Q2 move
     phi_A and phi_R by less than 10% of the CENTRAL value at every scored W and leave every class unchanged; M
     moves by at most max(20%, 3).  If P4 fails for Q2, the verdict table's "no power against Q168" clause is
     replaced by the measured power (no value moves either way; see VERDICT MOVES).
  P5 Reachability of DAY (the lines the severe-testing pass asks for): T5 is DAY on S4-A at 1000 kb; T2 is DAY
     on S4-M at 100 kb; T1 is not DAY on S4-A at any W (a dispersion index averages rare short blocks away); T4
     is MARGINAL-OUT or DAY on S4-A at 100 kb.
  P6 Simulator set-up, every corner without BGS and CENTRAL: span-weighted incongruent-topology fraction among
     H, C, G (pilot) in [0.20, 0.45]; full-exposure a in [0.40, 0.60]; q-bar in [0.15, 0.40].
  P7 Data, F2 at 100 kb (descriptive; not seen before this commit): mean n = iHG + iCG per used window in
     [20, 60]; q-bar in [0.15, 0.40]; a in [0.40, 0.55].
  Only S4-relevant number seen before this commit: R4-FM's Spearman of H density with (iHG + iCG) density, 0.76
  (100 kb, F2).  No share, asymmetry, dispersion or mesa count of iHG, iCG or HCs has been computed by anyone.

REACHABILITY, ONE LINE PER SIDE
  Day's band (DAY on S4-A or S4-M): produced by a non-tree process writing the same changes into two non-sister
  lineages over blocks of >= 300 kb (T2, S4-M) or over half the genome in blocks of 1 Mb (T5, S4-A); NOT produced
  by Q168's one-lineage blocks at any size simulated (P4 predicts this), and probably not by short rare blocks
  (T1).  If P5 fails for both T2 and T5 in the run, S4 is reported as UNREACHABLE for Day and scores for
  neither side (the S2 lesson).
  Critics' band (CRITIC on S4-A, S4-M): produced by ILS in a panmictic ancestor at any corner; it fails
  (MARGINAL-OUT or DAY) under T-type blocks above the sizes in P5, under ancestral structure or introgression,
  or under alignment artefact (F0).

SEVERITY, STATED FIRST (ST-10)
  A DAY on S4-A or S4-M is severe: ILS alone cannot create asymmetric blocks, and the band already carries every
  corner.  A CRITIC on S4-A or S4-M is discriminating only against non-tree processes at least as large as the
  planted ones the run shows it detects, and NEVER against Q168's mechanism (P4).  A CRITIC on S4-R is expected
  to be non-discriminating (P3).  None of the three tests the mechanism Day describes.

VERDICT MOVES (proposals; the integration decides; FM10 internal is `pending` by owner decision D-09 until Day
releases his method and NO outcome here touches it; D-25's fairer FM10 criterion, proposal (l), is a separate
registration not yet made, and this one does not pre-empt it)
  S4-DAY      FM3: no change (S4 is not about the index).  FM10 external: no change; it is `contested`, and the
              FMnull rule's move for a Day-side criterion ("toward `contested`") is already the state; not
              `supported`, because non-tree sharing is also produced by known processes (introgression,
              ancestral structure) and S4 cannot tell them from a fourth mechanism, and because Q168's own
              mechanism does not produce it (P4).  Licensed: a Day-side argument-map item "tree-incongruent
              sharing in blocks above the coalescent ILS band (F2)", as a defeater of the critic-side items that
              rest on tree-plus-ILS site patterns (FMnull's "mesas shared across lineages" reading; R4-FM's
              shared-rate null), with the alternatives named in the same sentence.  No defeater against FM10.
  S4-MARGINAL No value moves; reported for both sides as undecided; no defeater.
  S4-NOT-MET  No value moves.  Licensed: a critic-side descriptive item "incongruent sharing behaves as
              coalescent ILS at window scale (F2), no HG / CG mesas above the band", ALWAYS with the power line
              (detects T-type blocks of the sizes P5 shows; does not detect Q168 blocks of any size).  NOT a
              defeater against FM10 or against any statement of Day's (he made none about incongruence).  If the
              CRITIC classes are NON-DISCRIMINATING, the item says so.
  BELOW / UNSCORED  Calibration or data flag; no item.
  "S4 unreachable" (P5 fails for T2 and T5)  Recorded as a defect of the audit's criterion, on Day's side, as S2
              was; "S4 not met" is then not counted against him.
  Whatever the outcome, R4-FMnull's "S4 not run" becomes "S4 run post hoc (registered 48241c7, operationalised
  in this script)", and the pre-registration-status record says so.

HAND (central demography; 25-y generations; times in generations)
  HC epoch 80,000 gens; P(no H-C coalescence in it) = exp(-80,000 / (2 N_HC)) = 0.319, 0.540, 0.656 at N_HC 35k,
  65k, 95k; incongruent-topology fraction (2/3) of that = 0.213, 0.360, 0.438 (FML-H2's 50% gives 0.33; Scally's
  30% of the genome).  H-private branch ~256,000 gens (API check of msprime/tskit on 200 kb printed 252,289;
  no statistic of the null was computed).  Mutation rate ~ 0.00493 / 256,000 = 1.9e-8 per gen at the F2
  density.  Incongruent internal branch 2 N_HCG = 90,000 gens; congruent branch mass ~78,000 gens and
  incongruent ~32,000 gens per site, so q-bar ~ 0.29; incongruent sites ~6.2e-4 per bp, n ~ 36 per F2 100-kb
  window (m ~ 57,700).  Sites per incongruent tract ~ 1.74e-3 x tract length (400-900 bp from r x the
  branch length above the HCG split) ~ 0.7-1.6, so phi_A ~ 1 + 0.58 x 2 x (0.7-1.6) = 1.8-2.8 at F2 exposure,
  rising slowly with W through the 1/rho tail of the two-locus correlation, and up to ~e^1 = 2.7 times the
  excess where RHET = 1.  S4-R adds regional ILS-rate variance under BGS: at 1 Mb, n ~ 1,150, sd(ln q) up to
  ~0.33, excess up to ~50.
  Q168 blocks add iHG sites only where an extra H change hits a gorilla-derived site and copies its base:
  ~e d_H d_G / 3 ~ 1.2e-5 e per bp against ~3.1e-4 iHG per bp, i.e. +4% e inside blocks; Q2 shifts the share in
  block windows by ~0.02, adding ~0.01 to phi_A at 100 kb and ~0.1 at 1 Mb.

RESOURCES.  Not guessed: the compute-host smoke measures them.  Local smoke (after this commit; one parent plus
  one pool worker; real entry points, every configuration): `smoke --procs 1 --mb 0.2 --out /tmp/s4_smoke.npz`,
  `synth /tmp/s4_synth.npz`, `realdata /tmp/s4_synth.npz /tmp/s4_synth.json`, `post /tmp/s4_smoke.npz
  /tmp/s4_synth.json /tmp/s4_smoke_post.json` (synthetic uniform-Poisson bins: its classes mean nothing).
  Real-data arm: like FMnull realdata (~1.5 GB peak, minutes).
RUN (na-workhorse, only after the `ph2` collect task is done; check `uptime` first; at most 11 busy processes
across all agents, RAM under ~12 GB; launch with < /dev/null; record hostname and md5s in raw/fmnull_s4.host):
  P=research/.venv/bin/python; S=research/checks/fmnull_s4.py; R=research/checks/results/raw
  $P -I $S selftest
  $P -I $S smoke --procs 10 --mb 2 --out /tmp/fmnull_s4_smoke.npz > $R/fmnull_s4_smoke.out 2>&1
  $P -I $S realdata $R/fm_bins.npz $R/fmnull_s4_real.json > $R/fmnull_s4_real.out 2>&1
  $P -I $S sim --procs 10 --mb 1000 --out $R/fmnull_s4_sim.npz > $R/fmnull_s4_sim.out 2>&1   (or 500 / 200, rule)
  $P -I $S post $R/fmnull_s4_sim.npz $R/fmnull_s4_real.json $R/fmnull_s4_post.json > $R/fmnull_s4_post.out 2>&1
  Collect: rsync $R/fmnull_s4_* back (the sim npz is kept on the host, md5 in .host; json and .out committed).
"""
import json
import math
import os
import sys
import time
import zlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = 25.0
T_HC = 4.1e6 / GEN
T_HCG = 6.1e6 / GEN
T_O = 18e6 / GEN
D_H_SIM = 0.006
BIN = 1000
CHUNK_BP = 10_000_000
PILOT_BP = 2_000_000
RHET_SEG = 50_000
SF = ("H", "C", "G", "HCs", "iHG", "iCG")          # simulated per-bin fields, in this order
WS = (10, 30, 100, 300, 1000)                       # scored window sizes, kb
WS_DATA = WS + (3000,)
MESA_W, MESA_DEV, MESA_RUN, MESA_NMIN = (30, 100), 0.30, 3, 10
NSTRATA = 10
FM_FIELDS = ("m", "H", "C", "B", "G", "HCs", "iHG", "iCG", "DHC", "hh", "gc")   # asserted against the npz

N_HC, N_HCG, R_BP, RHET = (35e3, 95e3), (35e3, 55e3), (1.0e-8, 1.5e-8), (0.0, 1.0)
BGS = (None, (0.32, 200_000), (0.32, 2_000_000))
CENTRAL = dict(N_HC=65e3, N_HCG=45e3, r=1.25e-8, rhet=0.0, bgs=None)
PLANTED = {
    "Q1": dict(kind="Q168", f=0.02, e=1.0, Lb=100_000),
    "Q2": dict(kind="Q168", f=0.5, e=2.0, Lb=100_000),
    "T1": dict(kind="swap", f=0.02, Lb=100_000, s=1.0),
    "T2": dict(kind="swap", f=0.02, Lb=300_000, s=1.0),
    "T3": dict(kind="swap", f=0.005, Lb=300_000, s=1.0),
    "T4": dict(kind="swap", f=0.5, Lb=100_000, s=1.0),
    "T5": dict(kind="swap", f=0.5, Lb=1_000_000, s=1.0),
    "T6": dict(kind="swap", f=0.1, Lb=300_000, s=0.5),
}


def configs():
    out = []
    for a in N_HC:
        for b in N_HCG:
            for r in R_BP:
                for h in RHET:
                    for g in BGS:
                        name = f"c_{int(a/1e3)}k_{int(b/1e3)}k_r{r:.1e}_h{h:g}_" + ("bgs0" if g is None else f"bgs{g[1]//1000}k")
                        out.append((name, dict(N_HC=a, N_HCG=b, r=r, rhet=h, bgs=g)))
    out.append(("central", dict(CENTRAL)))
    for k, p in PLANTED.items():
        out.append((k, dict(CENTRAL, planted=p)))
    return out


def seed_of(*parts):
    return zlib.crc32("|".join(str(p) for p in parts).encode()) % (2**31 - 1) + 1


# ------------------------------------------------------------------------------------------------ simulation
def demography(n_hc, n_hcg, swap=False):
    import msprime
    d = msprime.Demography()
    for p in ("H", "C", "G", "O"):
        d.add_population(name=p, initial_size=1e4)
    d.add_population(name="X1", initial_size=n_hc)
    d.add_population(name="X2", initial_size=n_hcg)
    d.add_population(name="X3", initial_size=n_hcg)
    pair, third = (["H", "G"], "C") if swap else (["H", "C"], "G")
    d.add_population_split(time=T_HC, derived=pair, ancestral="X1")
    d.add_population_split(time=T_HCG, derived=["X1", third], ancestral="X2")
    d.add_population_split(time=T_O, derived=["X2", "O"], ancestral="X3")
    return d


def rate_map(L, r, rhet, rng):
    import msprime
    if rhet <= 0:
        return msprime.RateMap.uniform(L, r)
    n = int(math.ceil(L / RHET_SEG))
    pos = np.minimum(np.arange(n + 1) * RHET_SEG, L).astype(float)
    rates = r * np.exp(rng.normal(-rhet * rhet / 2.0, rhet, n))
    return msprime.RateMap(position=pos, rate=rates)


def ancestry(cfg, L, seed, rmap, scale=1.0, swap=False):
    import msprime
    dem = demography(cfg["N_HC"] * scale, cfg["N_HCG"] * scale, swap=swap)
    ts = msprime.sim_ancestry(samples=[msprime.SampleSet(1, population=p, ploidy=1) for p in ("H", "C", "G", "O")],
                              demography=dem, sequence_length=L, recombination_rate=rmap, ploidy=2,
                              random_seed=seed)
    names = [ts.population(ts.node(u).population).metadata["name"] for u in ts.samples()]
    assert names == ["H", "C", "G", "O"], names
    return ts


def h_branch(ts):
    """Expected H-private branch length per bp (generations): the H-field density divided by mu."""
    s = ts.samples()

    def f(x):
        x = np.asarray(x)
        v = (x[..., 0] == 1) & (x[..., 1] == 0) & (x[..., 2] == 0) & (x[..., 3] == 0)
        return v.astype(float).reshape(x.shape[:-1] + (1,))
    return float(np.ravel(ts.sample_count_stat([[s[0]], [s[1]], [s[2]], [s[3]]], f, 1, mode="branch",
                                               polarised=True, strict=False, span_normalise=True))[0])


def topo_fraction(ts):
    """Span-weighted fraction of trees in which H-G or C-G coalesce first among H, C, G."""
    h, c, g = ts.samples()[:3]
    inc = 0.0
    for t in ts.trees():
        hc, hg, cg = t.tmrca(h, c), t.tmrca(h, g), t.tmrca(c, g)
        if min(hg, cg) < hc:
            inc += t.span
    return inc / ts.sequence_length


def classify_sites(h, c, g, o):
    """Field logic of fm_mesa_replication.classify with hs1 == hg38 and b == c (bonobo not simulated)."""
    return {"H": (h != g) & (c == g) & (g == o), "C": (c != g) & (h == g) & (g == o),
            "G": (g != h) & (h == c) & (c == o), "HCs": (h == c) & (c != g) & (g == o),
            "iHG": (h == g) & (h != c) & (c == o), "iCG": (c == g) & (c != h) & (h == o)}


def site_states(ts, mu, seed):
    import msprime
    mts = msprime.sim_mutations(ts, rate=mu, model=msprime.JC69(), discrete_genome=True, random_seed=seed)
    G = mts.genotype_matrix().astype(np.int16)       # allele indices; alleles are distinct per site (selftest)
    pos = mts.tables.sites.position.astype(np.int64)
    return pos, G[:, 0].copy(), G[:, 1].copy(), G[:, 2].copy(), G[:, 3].copy()


def bin_counts(pos, h, c, g, o, nb, extra_H=None):
    f = classify_sites(h, c, g, o)
    b = pos // BIN
    out = np.zeros((nb, len(SF)), np.int64)
    for j, k in enumerate(SF):
        out[:, j] = np.bincount(b[f[k]], minlength=nb)[:nb]
    if extra_H is not None:
        out[:, 0] += extra_H
    return out


def blocks_mask(L, Lb, f, rng):
    """Bins (bool, length L / BIN) covered by blocks: Lb slots with a random phase, a fraction f of them chosen."""
    nb = L // BIN
    m = np.zeros(nb, bool)
    if f <= 0 or Lb > L:
        return m
    phase = int(rng.integers(0, Lb // BIN))
    starts = np.arange(phase, nb, Lb // BIN)
    x = f * L / Lb                                  # stochastic rounding keeps the expected fraction f per chunk
    k = int(math.floor(x)) + int(rng.random() < x - math.floor(x))
    for s in rng.choice(starts, size=min(k, len(starts)), replace=False):
        m[s: s + Lb // BIN] = True
    return m


def plant_q168(pos, h, c, g, o, L, p, rng):
    """Extra H substitutions at rate e * D_H_SIM per bp inside blocks.  Returns modified h and the per-bin count of
    extra H-private sites at previously invariant positions."""
    nb = L // BIN
    bm = blocks_mask(L, p["Lb"], p["f"], rng)
    nnew = rng.poisson(p["e"] * D_H_SIM * BIN, size=nb) * bm
    newpos = np.repeat(np.arange(nb) * BIN, nnew) + rng.integers(0, BIN, int(nnew.sum()))
    hit = np.isin(newpos, pos)
    extra = np.bincount(newpos[~hit] // BIN, minlength=nb)[:nb]
    idx = np.searchsorted(pos, newpos[hit])
    h = h.copy()
    for i in idx:                                   # move h to one of the three other bases (JC)
        cand = sorted({int(c[i]), int(g[i]), int(o[i])} - {int(h[i])})
        u = int(rng.integers(0, 3))
        h[i] = cand[u] if u < len(cand) else 100 + int(rng.integers(0, 1 << 14))
    return h, extra


def sim_chunk(task):
    """One chunk of one configuration.  task = (name, cfg, chunk_index, L, mu)."""
    import resource
    name, cfg, ci, L, mu = task
    t0 = time.time()
    base = "central" if "planted" in cfg else name
    rng = np.random.default_rng(seed_of(base, "rng", ci))
    rmap_all = rate_map(L, cfg["r"], cfg["rhet"], rng)
    seglen = L if cfg["bgs"] is None else min(cfg["bgs"][1], L)
    nb = L // BIN
    parts, parts_swap = [], []
    p = cfg.get("planted")
    for si, s0 in enumerate(range(0, L, seglen)):
        s1 = min(s0 + seglen, L)
        scale = 1.0
        if cfg["bgs"] is not None:
            sd = cfg["bgs"][0]
            s2 = math.log1p(sd * sd)
            scale = math.exp(rng.normal(-s2 / 2.0, math.sqrt(s2)))
        rmap = rmap_all.slice(left=s0, right=s1, trim=True)
        ts = ancestry(cfg, s1 - s0, seed_of(base, "anc", ci, si), rmap, scale)
        pos, h, c, g, o = site_states(ts, mu, seed_of(base, "mut", ci, si))
        extra = None
        if p is not None and p["kind"] == "Q168":
            prng = np.random.default_rng(seed_of(name, "plant", ci, si))
            h, extra = plant_q168(pos, h, c, g, o, s1 - s0, p, prng)
        parts.append(bin_counts(pos, h, c, g, o, (s1 - s0) // BIN, extra))
        if p is not None and p["kind"] == "swap":
            tsw = ancestry(cfg, s1 - s0, seed_of(name, "swap", ci, si), rmap, scale, swap=True)
            parts_swap.append(bin_counts(*site_states(tsw, mu, seed_of(name, "swapmut", ci, si)), (s1 - s0) // BIN))
    out = np.concatenate(parts)
    if parts_swap:
        prng = np.random.default_rng(seed_of(name, "plant", ci))
        bm = blocks_mask(L, p["Lb"], p["f"], prng) & (prng.random(nb) < p["s"])
        out[bm] = np.concatenate(parts_swap)[bm]
    assert out.shape == (nb, len(SF)) and out.max() < 65535
    return name, ci, out.astype(np.uint16), time.time() - t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def pilot(task):
    """Mutation-rate calibration and topology fraction for one configuration (uniform r at the config's mean)."""
    import msprime
    name, cfg, L = task
    if "planted" in cfg:
        name, cfg = "central", {k: v for k, v in cfg.items() if k != "planted"}
    ts = ancestry(cfg, L, seed_of(name, "pilot"), msprime.RateMap.uniform(L, cfg["r"]))
    lh = h_branch(ts)
    return task[0], D_H_SIM / lh, lh, topo_fraction(ts)


def run_sims(procs, mb, out, only=None):
    import multiprocessing as mp
    L = int(round(mb * 1e6))
    chunk = min(CHUNK_BP, L)
    assert L % chunk == 0 and chunk % BIN == 0
    cfgs = [(n, c) for n, c in configs() if only is None or n in only]
    t0 = time.time()
    with mp.Pool(procs) as pool:
        pil = {n: (mu, lh, tf) for n, mu, lh, tf in pool.map(pilot, [(n, c, min(PILOT_BP, L)) for n, c in cfgs])}
        tasks = [(n, c, ci, chunk, pil[n][0]) for n, c in cfgs for ci in range(L // chunk)]
        res, cost, rss = {}, {}, 0.0
        for n, ci, arr, dt, mem in pool.imap_unordered(sim_chunk, tasks):
            res[(n, ci)] = arr
            cost[n] = cost.get(n, 0.0) + dt
            rss = max(rss, mem)
    arrays = {n: np.stack([res[(n, ci)] for ci in range(L // chunk)]) for n, _ in cfgs}
    meta = dict(mb=mb, chunk_bp=chunk, fields=SF, pilot={n: dict(mu=v[0], h_branch=v[1], topo=v[2]) for n, v in pil.items()},
                cfg={n: {k: v for k, v in c.items()} for n, c in cfgs}, cpu_s=cost, wall_s=time.time() - t0,
                peak_rss_mb_worker=rss, procs=procs)
    np.savez_compressed(out, meta=json.dumps(meta, default=str), **{"cfg_" + n: a for n, a in arrays.items()})
    return meta


# ------------------------------------------------------------------------------------------------ statistics
def jk(groups, fn):
    ug = np.unique(groups)
    if len(ug) < 2:
        return float("nan")
    th = np.array([fn(groups != u) for u in ug])
    th = th[np.isfinite(th)]
    G = len(th)
    return float(math.sqrt((G - 1) / G * ((th - th.mean()) ** 2).sum())) if G > 1 else float("nan")


def phi_A(x, n, sel):
    s = sel & (n > 0)
    if s.sum() < 2:
        return float("nan")
    a = x[s].sum() / n[s].sum()
    if not 0 < a < 1:
        return float("nan")
    e = n[s] * a
    return float(((x[s] - e) ** 2 / (e * (1 - a))).sum() / (s.sum() - 1))


def phi_R(I, N, dens, sel, edges):
    s = sel & (N > 0)
    if s.sum() <= NSTRATA:
        return float("nan")
    st = np.searchsorted(edges, dens[s], side="right")
    num = 0.0
    for k in range(NSTRATA):
        q = st == k
        if q.sum() == 0:
            continue
        qs = I[s][q].sum() / N[s][q].sum()
        if not 0 < qs < 1:
            continue
        e = N[s][q] * qs
        num += ((I[s][q] - e) ** 2 / (e * (1 - qs))).sum()
    return float(num / (s.sum() - NSTRATA))


def mesa_count(x, n, used, grp, a):
    """HG and CG mesas: runs of >= MESA_RUN consecutive eligible same-direction windows within one group."""
    elig = used & (n >= MESA_NMIN)
    dev = np.where(elig, x / np.maximum(n, 1) - a, 0.0)
    out = {}
    for lab, flag in (("HG", elig & (dev >= MESA_DEV)), ("CG", elig & (dev <= -MESA_DEV))):
        cnt, run = 0, 0
        for i in range(len(flag)):
            if i > 0 and grp[i] != grp[i - 1]:
                cnt += run >= MESA_RUN
                run = 0
            if flag[i]:
                run += 1
            else:
                cnt += run >= MESA_RUN
                run = 0
        cnt += run >= MESA_RUN
        out[lab] = int(cnt)
    out["M"] = out["HG"] + out["CG"]
    out["k_elig"] = int(elig.sum())
    return out


def cell_stats(w, used, grp, W):
    """w: dict of window arrays (H, C, G, HCs, iHG, iCG, m); used: bool; grp: chromosome / chunk id per window."""
    x, n = w["iHG"].astype(float), (w["iHG"] + w["iCG"]).astype(float)
    I, N = n, n + w["HCs"].astype(float)
    m = np.maximum(w["m"].astype(float), 1.0)
    dens = (w["H"] + w["C"] + w["G"]) / m
    s = used & (N > 0)
    res = {"k_used": int(used.sum())}
    if used.sum() < 20 or n[used].sum() == 0:
        res["unscored"] = True
        return res
    edges = np.quantile(dens[s], np.linspace(0, 1, NSTRATA + 1)[1:-1])
    a = float(x[used].sum() / n[used].sum())
    res.update(a=a, qbar=float(I[s].sum() / N[s].sum()), n_mean=float(n[used].mean()), N_mean=float(N[used].mean()),
               c_mean=float(m[used].mean() / (W * BIN)), dH=float(w["H"][used].sum() / m[used].sum()))
    res["phi_A"] = phi_A(x, n, used)
    res["phi_A_se"] = jk(grp, lambda keep: phi_A(x, n, used & keep))
    res["phi_R"] = phi_R(I, N, dens, used, edges)
    res["phi_R_se"] = jk(grp, lambda keep: phi_R(I, N, dens, used & keep, edges))
    qq = np.where(N > 0, I / np.maximum(N, 1), np.nan)
    p0 = I[s].sum() / N[s].sum()
    res["phi_R0"] = float(((I[s] - N[s] * p0) ** 2 / (N[s] * p0 * (1 - p0))).sum() / (s.sum() - 1))
    from scipy.stats import spearmanr
    res["spearman_q_dH"] = float(spearmanr(qq[s], (w["H"] / m)[s]).correlation)
    if W in MESA_W:
        res["mesa"] = mesa_count(x, n, used, grp, a)
    return res


def sim_windows(arr, W):
    """arr: chunks x bins x SF (uint16) -> window sums (chunks*nw, SF) and chunk id per window."""
    nc, nb, _ = arr.shape
    nw = nb // W
    a = arr[:, : nw * W].astype(np.int64).reshape(nc, nw, W, len(SF)).sum(axis=2)
    return a.reshape(nc * nw, len(SF)), np.repeat(np.arange(nc), nw)


def thin(win, W, cq, rho, rng):
    """Binomial thinning of simulated window sums to a data cell: exposure c_w from the cell's quantiles, times rho."""
    k = win.shape[0]
    c = np.interp(rng.random(k), np.linspace(0, 1, len(cq)), cq)
    pthin = np.clip(c * rho, 0.0, 1.0)
    out = {f: rng.binomial(win[:, j], pthin) for j, f in enumerate(SF)}
    out["m"] = c * W * BIN
    return out


# ------------------------------------------------------------------------------------------------ classes
def centre(lo, hi):
    return 1.0 + math.sqrt(max(lo - 1.0, 0.0) * max(hi - 1.0, 0.0))


def classify_phi(v, lo, hi):
    if not all(np.isfinite([v, lo, hi])):
        return "UNSCORED"
    if v > 3.0 * hi:
        return "DAY"
    if v > hi:
        return "MARGINAL-OUT"
    if v > max(hi / 3.0, centre(lo, hi)):
        return "MARGINAL-IN"
    if v >= lo:
        return "CRITIC"
    return "BELOW-NEAR" if v >= lo / 3.0 else "BELOW-FAR"


def classify_count(M, lo, hi):
    from scipy.stats import poisson
    if M is None or not np.isfinite(hi):
        return "UNSCORED"
    if M > 3.0 * hi and poisson.sf(M - 1, hi) < 1e-3:
        return "DAY"
    if M > hi:
        return "MARGINAL-OUT"
    if M > max(hi / 3.0, math.sqrt(max(lo, 0.0) * hi)):
        return "MARGINAL-IN"
    if M >= lo:
        return "CRITIC"
    return "BELOW"


def poisson_limits(k):
    from scipy.stats import chi2
    lo = 0.0 if k == 0 else chi2.ppf(0.025, 2 * k) / 2.0
    return lo, chi2.ppf(0.975, 2 * (k + 1)) / 2.0


def width_phi(lo, hi):
    return float("inf") if lo <= 1.0 else (hi - 1.0) / (lo - 1.0)


def width_count(lo, hi):
    return float("inf") if lo <= 0 else hi / lo


# ------------------------------------------------------------------------------------------------ real data
def realdata(npz, outjson):
    sys.path.insert(0, HERE)
    import fm_mesa_replication as fm
    z, meta, chroms_all = fm.load(npz)
    assert tuple(meta["fields"]) == FM_FIELDS, meta["fields"]          # labels asserted, not assumed
    assert tuple(fm.FIELDS) == FM_FIELDS and int(meta["bin"]) == BIN == fm.BIN, (fm.FIELDS, meta["bin"])
    assert meta["classes"] == "rep + 2*cpg + 4*dup", meta["classes"]
    assert fm.FILTERS["F2"] == (0, 2) and fm.FILTERS["F3"] == (0,), fm.FILTERS
    auto = [c for c in chroms_all if c not in ("chrX", "chrY", "chrM")]
    assert len(auto) >= 1 and all(c.startswith("chr") for c in auto), auto
    res = {"chroms": auto, "cells": {}}
    for filt in ("F0", "F2", "F3"):
        for W in WS_DATA:
            try:
                w, cid, ok = fm.windows(z, auto, filt, W)
            except ValueError:
                continue
            cell = cell_stats(w, ok, cid, W)
            c = w["m"][ok] / (W * BIN)
            cell["c_quantiles"] = np.quantile(c, np.linspace(0, 1, 101)).tolist() if ok.sum() else []
            res["cells"][f"{filt}|{W}"] = cell
            print(filt, W, json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in cell.items()
                                       if k != "c_quantiles"}), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)
    return res


# ------------------------------------------------------------------------------------------------ post
def post(simnpz, realjson, outjson, seed=20261013):
    zs = np.load(simnpz)
    meta = json.loads(str(zs["meta"]))
    assert tuple(meta["fields"]) == SF, meta["fields"]
    real = json.load(open(realjson))
    names = [n for n, _ in configs() if "cfg_" + n in zs.files]
    corners = [n for n in names if n.startswith("c_")]
    assert len(corners) == 48 or meta.get("smoke_subset"), len(corners)
    bandsets = {"FULL": corners, "N": [n for n in corners if n.endswith("bgs0")],
                "U": [n for n in corners if n.endswith("_h0_bgs0")]}
    dH_sim = {}
    for n in names:
        arr = zs["cfg_" + n]
        dH_sim[n] = float(arr[..., 0].sum()) / (arr.shape[0] * arr.shape[1] * BIN)
    out = {"meta": {k: meta[k] for k in ("mb", "chunk_bp", "pilot", "cpu_s", "wall_s", "peak_rss_mb_worker", "procs")},
           "dH_sim": dH_sim, "cells": {}, "planted": {}, "aggregate": {}, "predictions": {}}
    full_exp = {}
    for n in names:                                                   # full-exposure descriptive values (P6)
        win, grp = sim_windows(zs["cfg_" + n], 100)
        w = {f: win[:, j] for j, f in enumerate(SF)}
        w["m"] = np.full(win.shape[0], 100.0 * BIN)
        st = cell_stats(w, np.ones(win.shape[0], bool), grp, 100)
        full_exp[n] = {k: st.get(k) for k in ("a", "qbar", "phi_A", "phi_R")}
    out["full_exposure_100kb"] = full_exp
    for filt in ("F2", "F3", "F0"):
        for W in WS + (3000,):
            key = f"{filt}|{W}"
            d = real["cells"].get(key)
            if d is None or d.get("unscored"):
                out["cells"][key] = {"data": d, "class": "UNSCORED"}
                continue
            sims, capped = {}, []
            for n in names:
                arr = zs["cfg_" + n]
                if arr.shape[1] // W < 1:
                    continue
                base = "central" if (n in PLANTED or n == "central") else n
                rho = d["dH"] / dH_sim[base]        # planted runs keep CENTRAL's calibration (Q168 adds H sites)
                if rho > 1.0:
                    capped.append(n)
                win, grp = sim_windows(arr, W)
                rng = np.random.default_rng(seed_of(seed, base, key))      # common random numbers with CENTRAL
                w = thin(win, W, np.array(d["c_quantiles"]), min(rho, 1.0), rng)
                sims[n] = cell_stats(w, np.ones(win.shape[0], bool), grp, W)
            cell = {"data": d, "rho_capped": capped, "sims": sims, "bands": {}, "classes": {},
                    "reported_only": W not in WS or filt != "F2"}
            for bs, members in bandsets.items():
                mem = [n for n in members if n in sims and not sims[n].get("unscored")]
                if not mem:
                    continue
                b = {}
                for stat in ("phi_A", "phi_R"):
                    lo = min(sims[n][stat] - 2 * (sims[n][stat + "_se"] if np.isfinite(sims[n][stat + "_se"]) else 0) for n in mem)
                    hi = max(sims[n][stat] + 2 * (sims[n][stat + "_se"] if np.isfinite(sims[n][stat + "_se"]) else 0) for n in mem)
                    b[stat] = dict(lo=lo, hi=hi, width=width_phi(lo, hi))
                    cell["classes"][f"{bs}|{stat}"] = classify_phi(d.get(stat, float("nan")), lo, hi)
                if W in MESA_W and "mesa" in d:
                    los, his = [], []
                    for n in mem:
                        ms = sims[n]["mesa"]
                        pl, pu = poisson_limits(ms["M"])
                        sc = d["mesa"]["k_elig"] / max(ms["k_elig"], 1)
                        los.append(pl * sc)
                        his.append(pu * sc)
                    b["M"] = dict(lo=min(los), hi=max(his), width=width_count(min(los), max(his)))
                    cell["classes"][f"{bs}|M"] = classify_count(d["mesa"]["M"], min(los), max(his))
                cell["bands"][bs] = b
            cell["nondiscriminating"] = {s: bool(cell["classes"].get(f"FULL|{s}") in ("CRITIC", "MARGINAL-IN")
                                                 and cell["bands"].get("FULL", {}).get(s, {}).get("width", 0) > 9)
                                         for s in ("phi_A", "phi_R", "M") if s in cell["bands"].get("FULL", {})}
            out["cells"][key] = cell
            print(key, {k: v for k, v in cell["classes"].items() if k.startswith("FULL")},
                  {s: (round(d.get(s, float("nan")), 3), round(cell["bands"].get("FULL", {}).get(s, {}).get("lo", float("nan")), 3),
                       round(cell["bands"].get("FULL", {}).get(s, {}).get("hi", float("nan")), 3)) for s in ("phi_A", "phi_R")},
                  ("M", d.get("mesa", {}).get("M"), cell["bands"].get("FULL", {}).get("M")), flush=True)
    # planted scenarios against the FULL band of the F2 cell
    for pn in PLANTED:
        if pn not in names:
            continue
        rows = {}
        for W in WS:
            cell = out["cells"].get(f"F2|{W}", {})
            if "sims" not in cell or pn not in cell["sims"] or "FULL" not in cell["bands"]:
                continue
            sp, sc = cell["sims"][pn], cell["sims"].get("central", {})
            r = {}
            for stat in ("phi_A", "phi_R"):
                b = cell["bands"]["FULL"][stat]
                r[stat] = dict(value=sp[stat], central=sc.get(stat), cls=classify_phi(sp[stat], b["lo"], b["hi"]),
                               central_cls=classify_phi(sc.get(stat, float("nan")), b["lo"], b["hi"]))
            if W in MESA_W and "M" in cell["bands"]["FULL"]:
                b = cell["bands"]["FULL"]["M"]
                scale = cell["data"]["mesa"]["k_elig"] / max(sp["mesa"]["k_elig"], 1)
                Mp, Mc = sp["mesa"]["M"] * scale, sc["mesa"]["M"] * scale
                r["M"] = dict(value_scaled=Mp, central_scaled=Mc, raw=sp["mesa"], cls=classify_count(Mp, b["lo"], b["hi"]),
                              central_cls=classify_count(Mc, b["lo"], b["hi"]))
                p = PLANTED[pn]
                if p["kind"] == "swap":                     # expected blocks placed in the simulated genome
                    nblk = p["f"] * meta["mb"] * 1e6 / p["Lb"]
                    r["M"]["yield_per_block"] = (sp["mesa"]["M"] - sc["mesa"]["M"]) / nblk
                    r["M"]["data_blocks_at_f"] = p["f"] * cell["data"]["mesa"]["k_elig"] * W * BIN / p["Lb"]
            rows[W] = r
        out["planted"][pn] = rows
    t2 = out["planted"].get("T2", {}).get(100, {}).get("M")
    if t2 and "T3" in out["planted"]:                # T3 projected from T2's yield per block (docstring)
        out["planted"]["T3_from_T2_yield_100kb"] = t2["yield_per_block"] * PLANTED["T3"]["f"] / PLANTED["T2"]["f"] * \
            t2["data_blocks_at_f"] + t2["central_scaled"]
    out["aggregate"] = aggregate(out)
    out["predictions"] = score_predictions(out, real, meta)
    json.dump(out, open(outjson, "w"), indent=1, default=float)
    print("AGGREGATE", json.dumps(out["aggregate"]))
    print("PREDICTIONS", json.dumps(out["predictions"], default=float))
    return out


def aggregate(out):
    agg = {}
    for filt in ("F2", "F3", "F0"):
        cls = []
        for W in WS:
            c = out["cells"].get(f"{filt}|{W}", {}).get("classes", {})
            cls += [c.get("FULL|phi_A"), c.get("FULL|phi_R")]
            if W in MESA_W:
                cls.append(c.get("FULL|M"))
        cls = [x for x in cls if x]
        if "DAY" in cls:
            agg[filt] = "S4-DAY"
        elif "MARGINAL-OUT" in cls:
            agg[filt] = "S4-MARGINAL"
        elif any(x != "UNSCORED" for x in cls):
            agg[filt] = "S4-NOT-MET"
        else:
            agg[filt] = "UNSCORED"
    agg["governing"] = agg.get("F2", "UNSCORED")
    return agg


def _all(flags):
    """None (unscorable) if any required class or value is missing; else all()."""
    flags = list(flags)
    return None if (not flags or any(f is None for f in flags)) else all(flags)


def _ok(c):
    return c is not None and c != "UNSCORED"


def score_predictions(out, real, meta):
    """Post hoc, pre-run (after the local smoke): a missing or UNSCORED class makes a prediction unscorable (None),
    never a vacuous hit."""
    P = {}
    C = lambda W, s: out["cells"].get(f"F2|{W}", {}).get("classes", {}).get(f"FULL|{s}")
    V = lambda W, s: (real["cells"].get(f"F2|{W}") or {}).get(s)
    inside = ("CRITIC", "MARGINAL-IN")
    a_cls = [C(W, "phi_A") for W in WS]
    a_val = [V(W, "phi_A") for W in WS]
    a_ge100 = [C(W, "phi_A") for W in WS if W >= 100]
    P["P1"] = dict(critic=_all((c in inside) if _ok(c) else None for c in a_cls),
                   day=(any(c == "DAY" for c in a_ge100) if all(_ok(c) for c in a_ge100) else None),
                   audit=(None if any(v is None for v in a_val) else
                          bool(all(1.5 <= v <= 8 for v in a_val) and a_val[-1] / a_val[0] <= 3)),
                   classes=a_cls, values=a_val)
    m_cls = [C(W, "M") for W in MESA_W]
    P["P2"] = dict(critic=_all((c not in ("DAY", "MARGINAL-OUT")) if _ok(c) else None for c in m_cls),
                   day=(C(100, "M") == "DAY") if _ok(C(100, "M")) else None, classes=m_cls)
    r_cls = [C(W, "phi_R") for W in WS]
    wid = [out["cells"].get(f"F2|{W}", {}).get("bands", {}).get("FULL", {}).get("phi_R", {}).get("width") for W in WS if W >= 300]
    P["P3"] = dict(critic=_all((c in inside) if _ok(c) else None for c in r_cls),
                   day=(any(c == "DAY" for c in r_cls) if all(_ok(c) for c in r_cls) else None),
                   audit=_all((x > 9) if x is not None else None for x in wid), classes=r_cls, widths_ge300=wid)
    ok4, det4 = True, {}
    for pn in ("Q1", "Q2"):
        if sorted(out["planted"].get(pn, {})) != sorted(WS):
            ok4 = None
            continue
        for W, r in out["planted"].get(pn, {}).items():
            for stat in ("phi_A", "phi_R"):
                v, c0 = r[stat]["value"], r[stat]["central"]
                good = c0 and abs(v / c0 - 1) < 0.10 and r[stat]["cls"] == r[stat]["central_cls"]
                ok4 = ok4 and bool(good) if ok4 is not None else None
                det4[f"{pn}|{W}|{stat}"] = (v, c0, r[stat]["cls"], r[stat]["central_cls"])
            if "M" in r:
                v, c0 = r["M"]["value_scaled"], r["M"]["central_scaled"]
                good = abs(v - c0) <= max(0.2 * c0, 3) and r["M"]["cls"] == r["M"]["central_cls"]
                ok4 = ok4 and bool(good) if ok4 is not None else None
                det4[f"{pn}|{W}|M"] = (v, c0, r["M"]["cls"], r["M"]["central_cls"])
    P["P4"] = dict(hit=ok4, detail=det4)
    pl = out["planted"]
    g = lambda pn, W, s: pl.get(pn, {}).get(W, {}).get(s, {}).get("cls")
    eq = lambda c, vals: (c in vals) if _ok(c) else None
    t1 = [g("T1", W, "phi_A") for W in WS]
    P["P5"] = dict(T5_A_1000_DAY=eq(g("T5", 1000, "phi_A"), ("DAY",)), T2_M_100_DAY=eq(g("T2", 100, "M"), ("DAY",)),
                   T1_A_never_DAY=_all((c != "DAY") if _ok(c) else None for c in t1),
                   T4_A_100=eq(g("T4", 100, "phi_A"), ("MARGINAL-OUT", "DAY")))
    P["P5"]["hit"] = _all(P["P5"].values())
    t5, t2 = P["P5"]["T5_A_1000_DAY"], P["P5"]["T2_M_100_DAY"]
    P["P5"]["S4_unreachable_for_Day"] = None if (t5 is None or t2 is None) else not (t5 or t2)
    ok6, det6 = True, {}
    for n, v in meta["pilot"].items():
        if n == "central" or (n.startswith("c_") and n.endswith("bgs0")):
            fe = out["full_exposure_100kb"].get(n, {})
            good = 0.20 <= v["topo"] <= 0.45 and fe.get("a") is not None and 0.40 <= fe["a"] <= 0.60 and 0.15 <= fe["qbar"] <= 0.40
            ok6 = ok6 and bool(good)
            det6[n] = (v["topo"], fe.get("a"), fe.get("qbar"))
    P["P6"] = dict(hit=ok6, detail=det6)
    d = real["cells"].get("F2|100") or {}
    P["P7"] = dict(hit=bool(d.get("n_mean") is not None and 20 <= d["n_mean"] <= 60 and 0.15 <= d["qbar"] <= 0.40
                            and 0.40 <= d["a"] <= 0.55),
                   n_mean=d.get("n_mean"), qbar=d.get("qbar"), a=d.get("a"))
    return P


# ------------------------------------------------------------------------------------------------ selftest / smoke
def synthetic_npz(path, rng, nbins=3000, nchrom=3):
    """A tiny npz in the fm_mesa_replication layout (bins x 8 classes x 11 fields), uniform Poisson counts."""
    arrs = {}
    for ci in range(nchrom):
        a = np.zeros((nbins, 8, len(FM_FIELDS)), np.uint16)
        cls = rng.choice(8, size=nbins, p=[0.75, 0.025, 0.1, 0.025, 0.025, 0.025, 0.025, 0.025])
        m = rng.integers(800, 1001, nbins)
        a[np.arange(nbins), cls, 0] = m
        for j, f in enumerate(FM_FIELDS[1:], start=1):
            lam = {"H": 0.005, "C": 0.0055, "B": 0.0055, "G": 0.007, "HCs": 0.0015, "iHG": 0.0003,
                   "iCG": 0.0003, "DHC": 0.012, "hh": 0.001, "gc": 0.4}[f]
            a[np.arange(nbins), cls, j] = rng.poisson(lam * m)
        arrs[f"chr_chr{ci + 1}"] = a
    np.savez_compressed(path, meta=json.dumps(dict(fields=FM_FIELDS, bin=BIN, sizes={}, blocks=0,
                                                   classes="rep + 2*cpg + 4*dup")), **arrs)


def selftest():
    import tempfile
    import msprime
    rng = np.random.default_rng(1)
    t0 = time.time()
    # 1. field logic on hand-made states (0 = ancestral)
    h, c, g, o = (np.array(v) for v in ([1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0]))
    f = classify_sites(h, c, g, o)
    assert [int(f[k].sum()) for k in SF] == [1, 1, 1, 1, 0, 1] and f["iHG"].sum() == 0 and bool(f["iCG"][4])
    assert f["H"][0] and f["C"][1] and f["HCs"][2] and f["G"][3]
    # 2. alleles distinct per site, so index equality is state equality
    ts = ancestry(CENTRAL, 100_000, 7, msprime.RateMap.uniform(100_000, CENTRAL["r"]))
    mts = msprime.sim_mutations(ts, rate=2.4e-8, model=msprime.JC69(), discrete_genome=True, random_seed=8)
    assert all(len(set(v.alleles)) == len(v.alleles) for v in mts.variants())
    # 3. split dispersion of a binomial is ~1; classes are exhaustive and ordered
    n = rng.poisson(40, 20000)
    x = rng.binomial(n, 0.5)
    assert abs(phi_A(x.astype(float), n.astype(float), np.ones(len(n), bool)) - 1) < 0.05
    lo, hi = 1.8, 6.0
    seen = {classify_phi(v, lo, hi) for v in np.linspace(0.1, 25, 2000)}
    assert seen == {"DAY", "MARGINAL-OUT", "MARGINAL-IN", "CRITIC", "BELOW-NEAR", "BELOW-FAR"}, seen
    assert classify_phi(float("nan"), lo, hi) == "UNSCORED"
    seen = {classify_count(M, 2.0, 12.0) for M in range(0, 200)}
    assert seen == {"DAY", "MARGINAL-OUT", "MARGINAL-IN", "CRITIC", "BELOW"}, seen
    assert classify_count(10, 0.0, 3.69) == "MARGINAL-OUT"            # > 3 E_hi but Poisson tail not < 1e-3
    assert abs(poisson_limits(0)[1] - 3.689) < 0.01
    # 4. mesa runs break on group change and on ineligible windows
    xx = np.array([9, 9, 9, 0, 9, 9, 9, 9, 9, 2], float)
    nn = np.full(10, 10.0)
    gg = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
    mc = mesa_count(xx, nn, np.ones(10, bool), gg, 0.5)
    assert mc["HG"] == 2 and mc["CG"] == 0, mc
    # 5. stratified phi_R of homogeneous binomial data ~1
    N = rng.poisson(120, 20000).astype(float)
    I = rng.binomial(N.astype(int), 0.3).astype(float)
    dens = rng.random(20000)
    edges = np.quantile(dens, np.linspace(0, 1, NSTRATA + 1)[1:-1])
    assert abs(phi_R(I, N, dens, np.ones(len(N), bool), edges) - 1) < 0.05
    # 6. thinning is binomial and keeps the window count
    win = rng.poisson(50, (500, len(SF)))
    tw = thin(win, 100, np.linspace(0.5, 1.0, 101), 0.9, rng)
    assert tw["iHG"].mean() < win[:, 4].mean() and len(tw["m"]) == 500
    # 7. planting: Q168 adds H-private sites inside blocks only; swap changes iHG inside blocks
    bm = blocks_mask(1_000_000, 100_000, 0.5, np.random.default_rng(3))
    assert bm.sum() == 500 and len(bm) == 1000
    with tempfile.TemporaryDirectory() as td:
        # 8. the whole pipeline on micro input: sims for a corner subset and two planted, synthetic npz, post
        cf = dict(configs())
        sub = [n for n in cf if n.startswith("c_") and n.endswith("_h0_bgs0")][:2] + \
              [n for n in cf if n.endswith("_h1_bgs200k")][:1] + ["central", "Q2", "T4"]
        meta = run_sims(1, 0.3, os.path.join(td, "s.npz"), only=sub)
        assert set(meta["pilot"]) == set(sub)
        assert meta["pilot"]["Q2"]["mu"] == meta["pilot"]["central"]["mu"]
        z = np.load(os.path.join(td, "s.npz"))
        assert z["cfg_central"].shape == (1, 300, len(SF))
        assert not np.array_equal(z["cfg_T4"], z["cfg_central"]) and not np.array_equal(z["cfg_Q2"], z["cfg_central"])
        assert z["cfg_Q2"][..., 0].sum() > z["cfg_central"][..., 0].sum()          # extra H-private sites
        synthetic_npz(os.path.join(td, "b.npz"), rng)
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):                  # no statistic is printed by the selftest
            realdata(os.path.join(td, "b.npz"), os.path.join(td, "r.json"))
            zz = dict(np.load(os.path.join(td, "s.npz")))
            mm = json.loads(str(zz.pop("meta")))
            mm["smoke_subset"] = True
            np.savez_compressed(os.path.join(td, "s2.npz"), meta=json.dumps(mm), **zz)
            o = post(os.path.join(td, "s2.npz"), os.path.join(td, "r.json"), os.path.join(td, "p.json"))
        assert set(o["aggregate"]) == {"F2", "F3", "F0", "governing"}
        assert set(o["predictions"]) == {"P1", "P2", "P3", "P4", "P5", "P6", "P7"}
        # 9. label assertion fires on a wrong layout
        bad = os.path.join(td, "bad.npz")
        np.savez_compressed(bad, meta=json.dumps(dict(fields=FM_FIELDS[::-1], bin=BIN, classes="x")),
                            chr_chr1=np.zeros((10, 8, 11), np.uint16))
        try:
            realdata(bad, os.path.join(td, "x.json"))
            raise SystemExit("label assertion did not fire")
        except AssertionError:
            pass
    import resource
    print(f"selftest ok ({time.time() - t0:.1f} s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024:.0f} MB)")


def main(argv):
    if not argv or argv[0] == "selftest":
        return selftest()
    mode = argv[0]
    opt = {argv[i][2:]: argv[i + 1] for i in range(1, len(argv) - 1) if argv[i].startswith("--")}
    pos = [a for i, a in enumerate(argv[1:], start=1) if not a.startswith("--") and not argv[i - 1].startswith("--")]
    if mode in ("sim", "smoke"):
        meta = run_sims(int(opt.get("procs", 1)), float(opt.get("mb", 1000 if mode == "sim" else 0.2)), opt["out"])
        cpu = meta["cpu_s"]
        print(json.dumps({k: meta[k] for k in ("mb", "wall_s", "peak_rss_mb_worker", "procs")}))
        print("cpu_s per configuration:", json.dumps({k: round(v, 2) for k, v in cpu.items()}))
        if mode == "smoke":
            tot = sum(cpu.values())
            for mb in (1000, 500, 200):
                proj = tot * mb / meta["mb"] / max(int(opt.get("procs", 1)), 1) / 3600.0
                print(f"projected wall at {mb} Mb per configuration and {opt.get('procs', 1)} processes: {proj:.2f} h "
                      f"(rule: the largest of 1000 / 500 / 200 Mb with a projection <= 8 h)")
        return
    if mode == "synth":                     # synthetic npz in the fm_bins layout, for the local smoke of realdata/post
        return synthetic_npz(pos[0], np.random.default_rng(20261013), nbins=int(opt.get("nbins", 20000)))
    if mode == "realdata":
        return realdata(pos[0], pos[1])
    if mode == "post":
        return post(pos[0], pos[1], pos[2])
    raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    main(sys.argv[1:])
