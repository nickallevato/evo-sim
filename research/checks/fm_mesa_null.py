"""FMnull: neutral-null calibration of Day's substitution-density overdispersion ("more than 80 times more
variable than a uniform-rate process predicts"), as a function of window size W and divergence d.

PRE-REGISTERED: this docstring, the parameter brackets (COMPONENTS, UNITS, TREE) and the scoring rule are
committed BEFORE the analytic table, the simulation or the real-data arm is run.  Only `selftest` (tiny
synthetic input, local, 1.6 s, 120 MB RSS) was run before the commit.  Any later change to a bracket, a
threshold or the scoring rule goes in a separate commit labelled "post hoc".

TIER. LOAD-BEARING (three reviews: correctness, steelman-day, steelman-critic).  The check informs FM3 (statistic
and magnitude) and the FM10 premise "neutral diffusive drift" is not viable (FM10 and ROOT-FM are
`load_bearing: true`).

TARGET QUOTES (verbatim; voxday.net "The Fourth Mechanism", 2026-10-10; local copy hash in quotes-day.md)
  Q164 (FM3, ¶4) "The substitution density across the genome is massively overdispersed, more than 80 times more
       variable than a uniform-rate process predicts."
  Q165 (FM4, ¶4) "Dense regions cluster next to other dense regions, forming contiguous blocks of elevated
       substitution with sharp boundaries in a pattern we call mesas."
  Q171 (FM10, ¶8) "What we do know is that neither natural selection nor neutral diffusive drift can still be
       considered viable candidates. ..."
  Q162 (FM1, ¶3) "... to analyze all six complete ape genomes provided by the T2T Primate Consortium."
  No window size, statistic, lineage unit, masking or code released (refreshes 2026-10-10, -11, -12-day).

WHAT THIS CHECK ADDS TO R4-FM.  R4-FM measured phi on the real alignment (1 kb - 1 Mb) and a shared-rate null that
borrows rate variation from the other lineages.  It did not say what a NEUTRAL MECHANISTIC model predicts for the
index at each W.  This check gives that: a lookup table W x d -> neutral band, scoreable the moment Day publishes
W and the statistic, plus a consistency test against the R4-FM numbers already committed (raw/fm_analyse.json).

STATISTIC: READINGS (rule RD; every plausible reading carried, none chosen)
  R1  dispersion index D = Var(n_w) / mean(n_w) over equal windows (Poisson null: D = 1); "80 times more
      variable" = variance ratio; threshold T = 80.  R1b = R4-FM's exposure-weighted binomial phi (same as R1 up
      to (1 - p) and exposure; carried by the same numbers).  R1x = "80 times MORE" read as D - 1 > 80 (T = 81;
      reported, numerically indistinguishable).
  R2  SD ratio: SD(n_w) / Poisson SD > 80, i.e. D > 6400 ("variable" read as standard deviation / CV ratio).
  Unit sub-readings (what is counted; "across the genome", "all six complete ape genomes"):
    U-H    human-lineage substitutions (parsimony, outgroups)          d = 0.0051 (R4-FM F0 density, in-house)
    U-C    chimp lineage                                               d = 0.0057 (in-house)
    U-G    gorilla terminal                                            d = 0.0077 (in-house)
    U-DHC  human-chimp pairwise differences, unpolarised               d in [0.0123, 0.0146] (CSAC2005 1.23%;
           Yoo2025 SI III.14 1.46%; in-house 0.0137)
    U-TREE substitutions summed over every branch of the seven-ape tree (one count per event) d in [0.03, 0.15]
           (UNSOURCED bracket)
    U-PAIRS differences summed over all 21 pairs (each event counted once per pair it separates): a uniform-rate
           process already gives D_struct = sum a_b^2 t_b / sum a_b t_b > 1 (a_b = s(n - s)); sub-readings
           U-PAIRS-naive (null = Poisson, D_struct counted as overdispersion) and U-PAIRS-struct (null includes
           D_struct; index = 1 + excess / D_struct).  Branch lengths in TREE are UNSOURCED except H, C, G terminal
           (in-house); the band scales the pairwise length by 0.7 (N_lo) and 1.3 (N_hi); the rate field is taken
           as fully shared by all branches (upper-side simplification).
  Exposure c = aligned (core) bp per window / W in {0.5, 1.0} (R4-FM: 86% of 1-kb bins pass at F0).

NEUTRAL MODEL (no selection).  Window count n_w ~ Poisson(c W d Rbar_w); Rbar_w = window mean of a relative-rate
field R(x) = prod_i F_i(x), independent stationary log-normal factors with mean 1, Var sigma_i^2 and log-scale
exponential autocorrelation (length ell_i).  Exact: D = 1 + c W d V(W), V(W) = Var(Rbar_w) from the discrete
covariance sum at BIN_BP resolution.  First-order check: D ~ 1 + mean * CV^2, CV^2 = sum sigma_i^2 g(W/ell_i),
g(x) = 2(x - 1 + e^-x)/x^2 (both printed).  Consequence fixed in advance: a component with ell << W adds a
W-INDEPENDENT 2 d sigma^2 ell to D; only components with ell >~ W make D grow linearly in W.
Components (sigma = SD of the relative rate at the component's own scale; ALL brackets UNSOURCED unless noted;
fetch items below):
  M0   chromosome-scale (subtelomeric etc.)            sigma [0.02, 0.10]   ell [5, 20] Mb
  M1   replication timing / large-scale mu             sigma [0.05, 0.20]   ell [0.5, 2] Mb
  M2   meso-scale (isochore, chromatin)                sigma [0.05, 0.20]   ell [20, 100] kb
  M3   fine-scale context clusters                     sigma [0.10, 0.40]   ell [0.2, 2] kb
  CPG  regional CpG-content variation                  sigma [0.03, 0.15]   ell [5, 50] kb
  GBGC recombination-associated gBGC                   sigma [0.02, 0.10]   ell [50 kb, 1 Mb]; lineage-specific
       fraction lambda [0.3, 1.0] (PRDM9 turnover)
  ILS  ancestral coalescence depth (incl. ancestral polymorphism): sigma = T2/(t1 + T2) with t1 6-7 My, T2 1-2 My
       (SOURCED: CSAC2005 quote, quotes-literature.md "Genome-wide rates") -> [0.125, 0.25]; tract length
       ell [0.1, 2] kb UNSOURCED (derivation: 1/(r 2 T2) ~ 126 bp at r = 1e-8, Ne 198,000 from Yoo2025)
  ALN  alignment / paralog / mappability error (UNMASKED arm only): sigma^2 = pi(1-pi)e^2, pi [0.001, 0.02],
       e [0.5, 3] -> sigma [0.016, 0.42]   ell [10, 100] kb
  Bands: N_lo = neutral components at (sigma_lo, ell_lo), c = 0.5; N_hi(masked) = at (sigma_hi, ell_hi), c = 1.0;
  N_hi(unmasked) = N_hi + ALN_hi.  Because V is monotone in every sigma and ell, the band is the bracket image.

SELECTION ARM (known non-neutral mechanisms; band K = N plus these)
  BGS  linked selection on ancestral Ne -> T2 (Scally2012: "most likely due to natural selection reducing Ne and
       making ILS less likely", held): sigma = [T2/(t1+T2)] sd(B), sd(B) [0.05, 0.25] UNSOURCED -> [0.006, 0.0625],
       ell [0.2, 2] Mb; SHARED by H and C, NEGATIVELY correlated with gene density / conservation (troughs, not
       mesas).  K_hi = N_hi(unmasked) + BGS_hi.
  Sweeps on a terminal lineage change expected neutral divergence by 0 (fixation probability = frequency); the
  variance they add per window is ~ (pi_anc / 2) W (~50 per 100 kb, Poisson variance ~500): negligible; recorded,
  not modelled.  Positive selection on coding/regulatory sites: each excess substitution is one adaptive
  fixation; a 100-kb mesa with hundreds of excess substitutions needs hundreds of adaptive fixations in that window
  (the Haldane/MITTENS comparison of FM5 applies only on this reading).
  SIGILLATION model (Day-side alternative; simulation only): H-only blocks of length Lb in {20, 100} kb with excess
  e in {0.5, 1.0} over genome fraction f in {0.005, 0.02}; "dominant source of divergence" (FM8b) needs
  f e / (1 + f e) > 0.5, i.e. f e > 1.

WHAT DISTINGUISHES "A FOURTH MECHANISM" FROM KNOWN MECHANISMS (criteria fixed now; for any future data)
  Day-supporting observables (each scored DAY if met by > 3x the relevant neutral upper bound):
   S1  index far above N_hi at EVERY plausible W (and after covariate regression);
   S2  lineage specificity: phi_HC (dispersion of the H/(H+C) split) > 3x its neutral upper bound (below);
   S3  edges sharper than the shortest-ell component allows AND |Spearman| < 0.1 with GC, CpG, repeat, recombination
       and replication-timing covariates;
   S4  tree-incongruent sharing: mesas shared by H and G but not C (or C and G, not H) above the ILS rate
       (Scally2012: "In 30% of the genome, gorilla is closer to human or chimpanzee than the latter are to each
       other", held) at matched density.
  Critic-supporting: index inside the band at Day's W; mesas shared across lineages (k = mu predicts the SAME
  windows high in every lineage: expected corr(H, C) density at W is CV2_shared / sqrt((CV2_H + 1/m_H)(CV2_C +
  1/m_C))); covariate correlations; phi_HC inside its neutral band.
  Neutral phi_HC band: 1 + N p(1-p) (V_lsH + V_lsC), N = mean H+C count, V_ls = lineage-specific variance
  (lambda x GBGC, plus ALN for unmasked).

PREDICTIONS (fixed now; hand estimates from the formulas, central exposure c = 1, the script's table governs)
  P1 (R1, U-DHC d 0.012, masked)  80 lies INSIDE [N_lo, N_hi] at W = 100 kb (hand: ~[5.7, ~133]) and 1 Mb
     (~[24, ~740]); ABOVE N_hi at W <= 10 kb (hand N_hi ~24).  Critic expects inside at >= 100 kb; Day expects
     above at every W <= 1 Mb.
  P2 (R1, U-H d 0.0051)  inside at 1 Mb (~[10, ~310]); above masked N_hi at <= 100 kb (~55) but inside unmasked
     N_hi at 100 kb (~120).
  P3 (R2, T = 6400)  above N_hi(unmasked) at every W <= 1 Mb for U-H, U-C, U-G, U-DHC (Day-side under R2); inside
     only for U-TREE/U-PAIRS at W >= ~3-10 Mb, if at all.  Recorded as a Day-side point if it holds.
  P4 (consistency, the key cell)  using the committed R4-FM phi (raw/fm_analyse.json), the window W80 at which the
     real data reach T = 80 (log-log interpolation; F0 and F2; H, C, B, G, DHC) lies where 80 is INSIDE the band
     (F0 vs unmasked, F2 vs masked).  CRITIC: inside for every lineage.  DAY: above N_hi by > 3x for some
     lineage.  For R2 (6400) the data reach T only beyond 1 Mb (extrapolated, flagged): reported as "R2 implies W >
     1 Mb on these data", then scored at the extrapolated W.
  P5 (bracket adequacy, not a Day/critic test)  >= 80% of the R4-FM autosomal grid cells (F0 vs unmasked band,
     F2 and F3 vs masked band; 1 kb - 1 Mb; H, C, B, G, DHC; exposure c in [0.5, 1]) fall inside their band.
     Cells ABOVE the band are reported as unexplained heterogeneity (a Day-side point) or bracket failure, not
     hidden.  Audit guess: DHC F0 1 kb may lie above (fine-scale indel/misalignment clustering).
  P6 (simulation reproduces analytic)  mean simulated D within 15% of the exact expectation (D - 1) at W <= 1 Mb,
     every band cell; Poisson baseline 1.00 +/- 0.05.
  P7 (selection arm)  BGS_hi adds <= 25% to N_hi(unmasked) at every W <= 1 Mb; corr(H density, gene-density
     covariate) < 0 under BGS; neutral phi_HC at 100 kb in [1, 6] (masked); corr(H, C) >= 0.6 at W >= 100 kb under
     the central neutral model.
  P8 (sigillation detectability)  f = 0.02, e = 1, Lb = 100 kb gives phi_HC > 10 at 100 kb (> 3x the neutral
     upper bound), so a block mechanism large enough to matter is visible to S2; f e > 1 (FM8b) gives phi_HC >
     100.  Day side: the block model at f = 0.005, e = 0.5 is NOT detectable by phi alone (phi_H inside N band):
     credited as a limit of the critic's main test.

SCORING DAY'S NUMBER (frozen; `score` mode).  Inputs: his W, statistic reading, unit (or d), masking, exposure.
  value / N_hi > 3 -> DAY ("far outside"; the 3x band convention of the RH closeness test)
  1 < value / N_hi <= 3 -> MARGINAL (undecidable)
  N_lo <= value <= N_hi -> CRITIC (index unremarkable for neutral heterogeneity at that W)
  value < N_lo -> BELOW (bracket error or a different statistic; reported, no verdict move)
  Unknown W: report, per reading and unit, the W ranges giving each outcome (the lookup table); FM3 fidelity stays
  `unverifiable` (rule F).
  Verdict moves (proposed; the integration decides): CRITIC on every plausible reading -> FM3 external stays
  `supported` as a description with the annotation "unremarkable against neutral heterogeneity at W"; FM10's
  premise "drift implies a uniform rate" gets a quantitative defeater.  DAY on the most charitable plausible
  reading -> FM3 annotated "anomalous against the neutral band at W"; FM10 external moves toward `contested` (not
  `supported`: an index alone does not identify a mechanism or a lineage; S2-S4 decide that).  Reading-dependent
  outcomes are recorded per rule RD (verdict field = reading most charitable to the speaker).

REAL-DATA ARM (`realdata`; DESIGNED, NOT RUN; na-workhorse, where fm_bins.npz (74 MB) lives)
  Reuses fm_mesa_replication.load/windows on raw/fm_bins.npz (1-kb bins, classes rep/CpG/dup).  For F0 and F2,
  W in {1, 3, 10, 30, 100, 300, 1000, 3000, 10000} kb, lineages H, C, B, G, DHC: phi, mean exposure, density,
  empirical CV2_excess = (phi - 1)/(m p); NNLS fit of CV2(W) = sum_j a_j g(W / ell_j), ell_j in {1, 10, 100, 1000,
  10000} kb (empirical sigma, ell vs the brackets); covariate-adjusted phi (OLS of log((n + 0.5)/m) on GC, CpG
  fraction, repeat fraction, dup fraction, hs1 != hg38 rate); corr(H, C), corr(H, G) by W; W80 and W6400 per
  lineage; phi_HC.  Estimate: 1 process, peak ~1.5 GB (largest chromosome as int64 x 8 classes x 11 fields),
  < 15 min CPU.  Recombination and replication-timing maps are NOT held (fetch items; need a CHM13 liftover).

FETCH ITEMS (none held; brackets above are UNSOURCED until fetched and quoted)
  Hodgkinson & Eyre-Walker 2011 Nat Rev Genet 12:756 (regional mutation-rate variation, CV by scale);
  Smith, Arndt & Eyre-Walker 2018 PLoS Genet 14:e1007254 (Mb-scale DNM, divergence, diversity variation; OA);
  Phung, Huber & Lohmueller 2016 PLoS Genet 12:e1006199 (linked selection and divergence across species; OA);
  Duret & Arndt 2008 PLoS Genet 4:e1000071 (gBGC in the human genome; OA); McVicker et al. 2009 PLoS Genet
  5:e1000471 (B map, sd(B)); Hobolth et al. 2007 PLoS Genet 3:e7 (ILS tract lengths); Hwang & Green 2004 PNAS
  101:13994 (CpG rate multiple); a replication-timing map (Koren et al. 2012) and a recombination map lifted to
  CHM13.  Citation details from memory: verify before use.

RESOURCES.  analytic: < 1 s; simulate (default 300 Mb x 10 reps x 12 scenarios): 1 process, < 600 MB, ~5-15 min;
realdata: as above.  Host: na-workhorse or builder (NOT run in this commit).
  analytic : python -I research/checks/fm_mesa_null.py analytic research/checks/results/raw/fmnull_analytic.json
  simulate : python -I research/checks/fm_mesa_null.py simulate research/checks/results/raw/fmnull_sim.json
  realdata : python -I research/checks/fm_mesa_null.py realdata research/checks/results/raw/fm_bins.npz \
             research/checks/results/raw/fmnull_real.json
  score    : python -I research/checks/fm_mesa_null.py score --W 100000 --value 80 --reading R1 --unit DHC
  selftest : python -I research/checks/fm_mesa_null.py selftest

POST HOC AMENDMENT 2026-10-12 (pre-run, no data seen)
  Status when written: only `selftest` had ever been run; `analytic`, `simulate`, `realdata`, `score` had NOT, and
  raw/fm_analyse.json was not opened for this amendment.  Everything above this section is the registration of
  commit 48241c7 and is unchanged: brackets, bands, P1-P8 and their hand estimates, scoring rule.
  WHAT CHANGED.  The registered brackets are kept verbatim as parameter set `PREREG`.  A second set `SOURCED` is
  added (PARAM_SETS).  Every table, crossing, score, P4/P5 cell, BGS share, simulation arm and `score` output is
  computed under BOTH sets and reported side by side; the write-up must state both, and every prediction is scored
  as registered (PREREG) and re-scored under SOURCED.  `realdata` is empirical and uses neither set.  New output
  only: `mutation_cv` (model CV of the window-mean mutation rate, M0-M3 + CPG, for comparison with Smith 2018).
  WHY.  Literature pass c1712c9 (docs/research/sources/refresh-2026-10-12c-lit.md; quote ids FML-* in
  quotes-literature.md) found sourced numbers for three components.  Each was re-derived here from the quotes;
  the derivations below are arithmetic on quoted numbers, not quotes.
  (a) M1, 1-Mb mutation-rate CV.  FML-S2: gamma CV of DNM density at 1 Mb = 0.18 (Francioli), 0.27 (Wong), 0.15
      (Jonsson).  The comparable model quantity is NOT sigma_M1 and NOT sqrt(sigma_M0^2 + sigma_M1^2) (0.224, the
      refresh file's comparison): it is the CV of the 1-Mb window mean, sqrt(sum_i sigma_i^2 g(1 Mb / ell_i)) over
      the mutational components M0-M3 + CPG.  First order, PREREG: lo edge 0.044, hi edge 0.232.  So PREREG's hi
      edge is below Wong (0.27) but ABOVE Francioli and Jonsson, and its lo edge is 3.4x BELOW the lowest dataset.
      SOURCED M1 sigma [0.20, 0.25] is calibrated so the 1-Mb CV is 0.152 at the lo edge (ell 0.5 Mb: 0.04 x
      g(2) = 0.0227, + others 0.0005) and 0.270 at the hi edge (ell 2 Mb: 0.0625 x g(0.5) = 0.0533, + others
      0.0197).  Caveats, both ways: Smith's Abstract says the datasets differ "at the 1MB and 100KB scales probably
      as a consequence of differences in sequencing technology and processing", so Wong 0.27 may be technical (hi
      edge then too high: calibrating to Francioli 0.18 instead gives sigma_M1 0.12, BELOW the registered 0.20, i.e.
      on that reading PREREG's hi edge was already too wide); and FML-S8 (divergence tracks DNM density only "about
      half as strong as it could") means the long-term CV relevant to divergence may be below the DNM CV (lo edge
      then too high).  Mutation only; gBGC, ILS, BGS are separate components.
  (b) M2, 100-kb CV: UNCHANGED [0.05, 0.20].  No 100-kb CV is quoted.  Power-law interpolation of FML-S2 with the
      FML-S5 slopes, CV(100 kb) = CV(1 Mb) x 10^(-b): 0.18 x 10^0.25 = 0.320, 0.27 x 10^0.10 = 0.340, 0.15 x
      10^0.16 = 0.217 (assumes the 10 kb - 10 Mb slope holds between 1 Mb and 100 kb).  Comparable model quantity:
      100-kb window-mean CV (not sqrt(0.01 + 0.04 + 0.04) = 0.30): PREREG [0.061, 0.313]; SOURCED, with M1 changed
      and M2 as registered, [0.197, 0.346], which brackets 0.217-0.340 to within 10%.  So the registered M2 bracket
      is supported once M1 is sourced.  Not applied, flagged: the same extrapolation to 10 kb gives 0.31-0.57
      against a SOURCED hi edge of ~0.43 (M3 and CPG remain unsourced).
  (c) ILS sigma.  Definition checked: sigma = SD across loci of relative divergence (t1 + T2)/(t1 + E[T2]) =
      sd(T2)/(t1 + E[T2]); it is a PER-LOCUS (tract-scale, ell 0.1-2 kb) quantity, independent of W; its effect on
      D at W >> ell is the W-independent 2 d sigma^2 ell.  The registered "T2/(t1 + T2)" equals this only for a
      single exponential epoch (sd = mean).  FML-H1 (Hobolth 2007): speciation 4.1 +/- 0.4 My, N_HC 65,000 +/-
      30,000, N_HCG 45,000 +/- 10,000; 25-y generations.  Single epoch: E[T2] = 2 N g = 3.25 My, sigma = 3.25/7.35
      = 0.44; N 35k-95k: 1.75/5.85 = 0.30 to 4.75/8.85 = 0.54 (the refresh file's numbers: arithmetic confirmed).
      But Hobolth's own model has a second epoch: FML-H2 ("around 50% ... coalesces with chimpanzee after speciation
      with gorilla") implies exp(-Delta/3.25) = 0.5, Delta = 2.25 My, after which coalescence is at the HCG rate
      (mean 2 x 45,000 x 25 y = 2.25 My).  Two-epoch: E[T2] = 2.75, sd = 2.41 My, sigma = 2.41/6.85 = 0.35; over
      N_HC 35k-95k and N_HCG 35k-55k: 0.30-0.40 (insensitive to N_HC because the HCG epoch takes over).  The ratio
      is calibration-independent.  SOURCED ILS sigma = [0.125 (CSAC2005, as registered), 0.40 (Hobolth two-epoch
      upper)].  NOT comparable / not applied: CSAC2005 "polymorphism accounts for 14-22% of the observed divergence
      rate" is present-day polymorphism, not the ancestral term.  Unverified, pointing higher: Yoo2025 Ne 198,000
      with split 5.5-6.3 Ma gives single-epoch 0.56-0.64 at an (unquoted) 20-25-y generation; the registered ell
      derivation already used that Ne while the sigma used T2 1-2 My (N 20-40k): an inconsistency inside PREREG,
      recorded.  Simplification kept from PREREG: the same ILS sigma is applied to every unit (it is derived for
      H, C and DHC; G, TREE and PAIRS have other depths).  Sensitivity, hand: sigma 0.54 instead of 0.40 adds a
      further ~7 to N_hi (DHC, any W >= 10 kb).
  (d) BGS sigma.  Definition checked: local ancestral coalescence scales with B, so SD of relative divergence =
      [E[T2]/(t1 + E[T2])] x sd(B)/mean(B).  The registered form omitted 1/mean(B) and used the CSAC ratio.  The
      ratio here is the MEAN fraction, not sd: Hobolth two-epoch 2.75/6.85 = 0.40, range 0.30-0.46 (single-epoch
      0.30-0.54).  mean(B) = 0.74-0.81 (FML-M2).  sd(B) [0.05, 0.25] stays UNSOURCED (B distribution is in a figure
      only).  SOURCED = [0.125 x 0.05/0.81, 0.44 x 0.25/0.74] = [0.0077, 0.15].  (The refresh file's 0.015-0.135 =
      0.30 x 0.05 to 0.54 x 0.25: arithmetic confirmed; superseded by the two-epoch ratio and the 1/mean(B) factor.)
  (e) No number found; SOURCED = registered bracket: M0, M2, M3, CPG, GBGC, LAMBDA, ALN, all ell, UNITS, TREE.
  DIRECTION OF THE EFFECT (hand, first order, U-DHC, c = 1, d = 0.012 as in P1; the script's table governs)
      N_hi masked   100 kb: PREREG ~133 -> SOURCED ~163 (+23%)    1 Mb: ~740 -> ~970 (+32%)    10 kb: ~24 -> ~30
      N_hi unmasked 100 kb: ~288 -> ~319
      N_lo          100 kb: ~5.7 -> ~48 (c = 0.5: ~3.4 -> ~24)    1 Mb: ~24 -> ~280 (c = 0.5: ~13 -> ~140)
      BGS_hi share of N_hi(unmasked) excess: 1 Mb ~3.6% -> ~17%; 100 kb ~1.6% -> ~8%
    Critic side: N_hi rises, so the W range where a given index is "far outside" (DAY) shrinks; 80 at 10 kb moves
    from about 3.3x to about 2.7x N_hi.  Day side: N_lo rises 8-12x, so the band is NARROWER at the bottom, and
    at 1 Mb an index of 80 would lie BELOW the SOURCED band (outcome BELOW, no verdict move) where P1 registered
    "inside"; if Wong is technical the SOURCED hi edge overstates neutral variance.  These SOURCED figures are hand
    expectations written before any run; they are NOT predictions of record and add no new prediction bands.
  P7 stands as registered ("BGS_hi adds <= 25% to N_hi(unmasked) at every W <= 1 Mb") and will be scored as
  registered under PREREG, then re-scored under SOURCED.  Noted for the reviews: P7 measures BGS against the UPPER
  bound of all other components (including ALN), which is not the quantity in FML-M3 / FML-P1 (share of the actual
  variance in H/C divergence explained by BGS); those model-based claims, and FML-M5, belong in both steelmen.
  Resource: analytic still < 1 min; simulate runs both sets with the same seed, ~2x the registered estimate.

POST HOC AMENDMENT 2 2026-10-12 (pre-run, no data seen)
  Answers research/checks/results/REVIEW-R4-FMnull-prerun.md (0 BLOCKER, 10 MAJOR, 11 MINOR; resolution table
  appended there).  Status when written: only `selftest` had ever been run; `analytic`, `simulate`, `realdata`,
  `score`, `post` had NOT; raw/fm_analyse.json and every real-data output were not opened.  Everything above is
  unchanged: PREREG, SOURCED, P1-P8, the frozen scoring rule and the registered outputs are still computed and
  scored as registered.  Amendments are computed BESIDE them (output key `amend2`, third parameter set `AMENDED`,
  function names ending in 2).  Numbers marked "hand" are first-order arithmetic; the script's table governs.
  Informed-by note: P4, P5 (below) and the U-BP inputs use in-house results committed before this registration.

  A1  M1/M0 AS A CONSTRAINT ENVELOPE (MAJOR-1, MAJOR-3, MINOR-10).  Smith's numbers fix the CV of the window MEAN,
      not sigma.  AMENDED drops the (sigma, ell) corners for M0 and M1: for every (ell_M1, ell_M0) on a grid over
      the registered ell brackets it solves sigma_M1, sigma_M0 (first order, the other mutational components at the
      edge) so that the model's mutation CV equals a Smith target at 1 Mb (FML-S2, quoted) AND at 10 Mb (derived:
      CV(1 Mb) x 10^b with the FML-S5 slope; 10 Mb is inside Smith's fitted range, FML-S4; derived, not quoted:
      Francioli 0.101, Wong 0.214, Jonsson 0.104).  Infeasible pairs (negative sigma^2) are dropped; the band edge
      at each W is the min (lo) / max (hi) of V(W) over the feasible set.  The slopes are NOT imposed below 1 Mb
      (M2, M3, CPG unsourced): the derived 100-kb and 10-kb CVs are printed beside the envelope (`mutation_cv_env`),
      and every cell at W <= 30 kb or W > 10 Mb is flagged `under_sourced`.  Hand: the 10-Mb constraint needs
      sigma_M0 ~0.10 (Jonsson) to ~0.22 (Wong), above the registered M0 hi of 0.10.
      Helps: critics at the top (N_hi rises at W < 1 Mb by ~1.2-1.4x and at W >= 3 Mb; DAY harder under R2); Day at
      the bottom at W >= 3 Mb (N_lo rises); removes spurious BELOW at W < 1 Mb (N_lo falls), which helps neither
      side's score but makes the band honest.
  A2  CALIBRATION VARIANTS, REPORTED SIDE BY SIDE (MAJOR-2; rule RD: none chosen).  Which datasets set the edges:
        ALL3    lo = Jonsson (0.15), hi = Wong (0.27)       all three datasets
        NOWONG  lo = Jonsson (0.15), hi = Francioli (0.18)  Wong treated as technical (Smith Abstract)
        FRANC   lo = hi = Francioli (0.18)                  one dataset; only ell varies
      and, for the lo edge only, how much of the present-day DNM landscape persists over the divergence time:
        persist 1.0  the DNM CV is a floor for divergence      persist 0.5  half of the SD persists (one reading
        of FML-S8 "only about half as strong as it could"; the other reading, extra variance sources, is persist 1).
      PREREG (sigma_M1 lo 0.05) is the third low-edge value and is always printed.  So N_lo is reported under
      PREREG, SOURCED and six AMENDED variants; N_hi under PREREG, SOURCED and three.  An AMENDED outcome counts
      only if it is the same under all six variants; otherwise it is CAL-DEPENDENT (table of variants reported, no
      verdict move).  Helps: both; it removes a choice the sources do not settle.  Day: NOWONG/FRANC lower N_hi
      (hand ~0.5x at 1 Mb).  Critics: persist 0.5 lowers N_lo, so fewer BELOW cells.
  A3  SCORE TAKES THE REGISTERED INPUTS (MAJOR-4).  `score --exposure c --d d [--cvc v]`: both band edges use the
      stated exposure and divergence; without them the registered brackets (c 0.5 / 1.0, unit d) are used and
      labelled so.  P4/P5 are re-scored with each cell's own exposure (m_mean / W) from the realdata output, in the
      new mode `post`; the registered bracket version stays in `analytic`.  Helps: Day (N_hi for masked data falls
      in proportion to c, up to 2x); tightens P5 (neutral).
  A4  SYMMETRIC MARGIN (MAJOR-6, MINOR-6, MINOR-9).  Amended classes (`classify2`; registered `classify` kept):
        DAY           value > 3 N_hi
        MARGINAL-OUT  N_hi < value <= 3 N_hi
        MARGINAL-IN   max(N_hi / 3, N_c) < value <= N_hi   inside, but only near the simultaneous upper corner
        CRITIC        N_lo <= value <= max(N_hi / 3, N_c)
        BELOW-NEAR    N_lo / 3 <= value < N_lo             BELOW-FAR  value < N_lo / 3
      N_c = 1 + sqrt((N_lo - 1)(N_hi - 1)), the geometric centre of the excess.  The critic now needs the same 3x
      clearance inside N_hi that Day needs outside it; N_c is the floor of that rule so that a band narrower than
      9x still has a CRITIC zone (a value at or below the centre of the band is unremarkable whatever its width).
      BELOW carries two labels, one per question: for "is the index anomalously high?" it is NOT-HIGH (critic-side,
      a fortiori); for "is the null calibrated?" it is a bracket failure (Day-side: the model over-predicts there
      and a CRITIC score from the same parameter set at a neighbouring W is weakened).  BELOW-FAR gives no
      defeater credit against FM10.  Helps: Day (MARGINAL-IN was CRITIC); critics (BELOW-NEAR was unscored).
  A5  ALN AS A SEPARATE, LABELLED COMPONENT (MAJOR-7).  Every table row prints ALN_part = N_hi(unmasked) -
      N_hi(masked) and its share.  For unmasked data the value is classified against both bands; if the classes
      differ the outcome is ALN-DEPENDENT ("rests on an unsourced artefact term, not a neutral evolutionary
      process") and moves no verdict for either side.  Helps: Day (a value inside only because of ALN_hi is no
      longer "unremarkable"); costs critics nothing that is sourced.
  A6  KNOWN-MECHANISMS BAND (MINOR-7).  Every score is also given against K_hi (neutral + BGS; `class_K`).  Q171
      says "neither natural selection nor neutral diffusive drift": FM10 moves toward `contested` only on DAY
      against K_hi; DAY against N_hi but not K_hi is recorded as "outside neutral, inside known mechanisms" (a
      Day-side point against "drift alone suffices", FML-M3 / FML-P1, and a critic-side point against a fourth
      mechanism).
  A7  REPRODUCTION GATE (MAJOR-8, MINOR-11).  A DAY or CRITIC class moves a verdict only if the real-data arm
      reproduces Day's number: the measured index at his W, reading, unit and masking lies within [1/3, 3] x his
      value (`repro_gate`; with W unknown, at any measured W, and only the classes at those W count).  Otherwise
      NOT-REPRODUCED (his number is not a property of the held alignment under that reading; FM3 fidelity stays
      `unverifiable`, rule F; recorded with the caveat, Day-side, that his pipeline is unreleased) or UNTESTED
      (unit not measured: TREE, PAIRS, BP; or W outside 1 kb - 10 Mb).  Same gate for both sides.  The registered
      asymmetry "CRITIC on every plausible reading, DAY on the most charitable one" is kept and is rule RD (Day is
      the speaker); with the gate, "most charitable" means the reading under which his statement is true OF THE
      DATA.  Helps: critics (removes the near-automatic R2 DAY of P3); Day keeps R2 wherever the data reach 6,400.
      P3 stays registered and is scored as registered, with the gate result beside it.
  A8  TWO MISSING READINGS (MAJOR-9; both are readings of Day's own words or practice, rule RD).
      R1u  counts per fixed genomic window, NOT normalised for alignable bases.  With exposure c_w independent of
           the rate field: D - 1 = m [V (1 + CV_c^2) + CV_c^2], m = mean count, so a UNIFORM rate already gives
           m CV_c^2.  CV_c bracket [0.2, 0.5] is UNSOURCED (reviewer's hand range); `realdata` now measures CV_c
           and the unnormalised index (over used windows and over all windows), and `score --cvc` takes it.
      U-BP gap-inclusive base pairs (how Day counts divergence elsewhere: the 410 M figure, R4-L7 / A3x).  The count
           is compound: D = D_struct + m_bp V, D_struct = E[L^2] / E[L] over event sizes.  Inputs, in-house
           (R4-GAP07t summary, known before this amendment): 42.87 M SNV, 5.40 M indel events, 2 x 205 M bp, 1-bp
           share 39.7%.  Derived floors (Cauchy-Schwarz; the length distribution itself is not used): D_struct >=
           61 (equal lengths) and >= 100 (given the 1-bp share).  The true value is higher (heavy tail); the upper
           edge uses an UNSOURCED tail factor 10 and is flagged.  d_bp [0.13, 0.14] (410 M / ~3.1 Gb, approximate;
           Yoo2025 SI III.14 1.46% + 12.47%).  Sub-readings BP-naive (null = Poisson) and BP-struct (null includes
           D_struct), as for PAIRS.  Hand: under BP-naive a uniform-rate process gives D >= ~60-100 at EVERY W.
           Not measurable on fm_bins.npz (no indel lengths): the gate returns UNTESTED.
      Helps: critics.  Limits, Day-side: both make "80" trivially reachable only if Day did not normalise; nothing
      in Q164 says he did not, so neither reading can score CRITIC alone (the registered rule needs CRITIC on
      EVERY plausible reading).
  A9  LINEAGE-SPECIFIC MUTATIONAL SHARE (MAJOR-10).  The neutral phi_HC bound (S2) is now computed (`phi_hc_bound`;
      the registered text gave the formula but no code): 1 + N p(1 - p)(V_lsH + V_lsC), with V_ls from lambda x
      GBGC, PLUS a share lambda_M of the mutational components M0-M3 + CPG, PLUS ALN for unmasked data (assembly
      error is lineage-specific).  lambda_M in {0 (registered), 0.25, 0.5}: 0.5 is one reading of FML-S8 (half of
      the landscape not shared; "gets worse as more divergent species are considered"); the paper itself proposes
      gBGC, which is already a separate term, so 0.5 is an upper reading, not an estimate.  Reported side by side
      (rule RD).  S2 scores DAY only above 3x the bound at EVERY lambda_M, and "phi_HC inside its neutral band"
      scores for the critic only inside at lambda_M = 0; between the two it is LAMBDA-DEPENDENT.  The H-C
      correlation that `realdata` measures is NOT used to set lambda_M (it would calibrate the null for lineage
      specificity on the lineage data).  Helps: critics on S2.  Cost, stated: at lambda_M = 0.5 the bound at
      100 kb is of order 30 (hand), so P8's block model (phi_HC > 10) is no longer > 3x the bound; P8 is scored as
      registered and again per lambda_M.
  A10 P4 AND P5 ARE INFORMED, NOT PREDICTIVE (MAJOR-5).  R4-FM's phi values and RESULTS.md's "3x to 800x" were
      committed before 48241c7.  P4 and P5 stay as written and are scored, but as consistency checks against
      known numbers; they earn neither side a prediction credit (L7 MAJOR-2 precedent).  P1-P3, P6-P8 are unaffected.
  A11 ILS (MINOR-1, MINOR-2).  (i) Quoted in place of the inferred Delta = 2.25 My: Hobolth 2007, Discussion (held
      text, PMC1802818): "The HCG speciation time is estimated to have occurred approximately 2 Myr earlier than the
      HC speciation time (i.e., 6 Myr ago)."  `two_epoch` computes E[T2], sd and the mean fraction from t1 4.1 My,
      Delta 2.0 My, N_HC 35-95k, N_HCG 35-55k, 25 y; hand at the centre: E[T2] 2.71, sd 2.38, sigma 0.35 (was
      0.352).  AMENDED takes the maximum over that grid.  (ii) Kernel.  The per-locus sigma DOES average down with
      window size (through V(W)); the registered exponential kernel makes its contribution to D exactly
      W-independent at W >> ell.  For two lineages in one constant population the correlation of coalescence times
      at rho = 4 N r x is (rho + 18)/(rho^2 + 13 rho + 18).  VERIFIED here by an independent first-step derivation
      (three-state Markov chain, linear system in `hudson_cov_check`, in the selftest); NOT verified against a held
      source text (attribution Griffiths 1981 / Hudson 1983 is from memory).  Its 1/rho tail gives window variance
      ~ log(W)/W, so the ILS term in D grows slowly with log W: the registered "W-independent" wording is corrected
      for ILS.  AMENDED uses this kernel with 4 N r per bp in [4 x 35,000 x 1e-8, 4 x 95,000 x 1.5e-8] (N: FML-H1;
      r = 1e-8 UNSOURCED convention, 1.5 cM/Mb is Hobolth's simulation setting, not an estimate).  Not covered: the
      formula is for one constant-size population; the two-epoch ancestor and the three-lineage HCG epoch are not
      modelled (unverified approximation).  Size: a few percent of N_hi at W >= 100 kb (hand ~13 at 1 Mb, U-DHC).
      Helps: critics, slightly.
  A12 BGS AND DOUBLE COUNTING (MINOR-3, MINOR-4).  AMENDED BGS hi = (largest two-epoch mean fraction from
      `two_epoch`) x 0.25 / 0.74, replacing the single-epoch 0.44; elasticity kept at 1 (upper side; 0.87 if BGS
      acts on the HC epoch only).  sd(B) stays UNSOURCED and dominates.  Double counting, checked: in SOURCED and
      AMENDED the mutational terms are calibrated on pedigree DNMs (1 Mb quoted, 10 Mb derived), which carry no
      BGS, ILS or gBGC signal, and M2, M3, CPG sit inside the sum matched to Smith, so nothing is added twice.
      Three places where it CAN enter, and the rule for each: (i) PREREG's mutational brackets are unsourced; if
      they echo divergence-based estimates they already contain BGS, ILS and gBGC, so K_hi under PREREG may count
      BGS twice (upper side; stated wherever PREREG K_hi is used); (ii) the `realdata` NNLS fit of CV^2(W) is
      estimated from divergence and is the TOTAL of all components: it is compared with the band, never added to
      BGS, ILS or GBGC, and never used to reset a mutational bracket; (iii) residual overlaps M0 "subtelomeric"
      vs GBGC (FML-D1) and technical variance inside the DNM CV (both upper side).
  A13 SMALL (MINOR-5, MINOR-8).  P7's "corr(H density, gene-density covariate) < 0 under BGS" is true by
      construction of the simulation: reported, not scored as a test; the rest of P7 stands.  The BGS simulation
      arm uses ell 1 Mb, not the bracket edge (disclosed).  TREE branch lengths stay UNSOURCED: only the pairwise
      SNV means of Yoo SI III.14 are held, not branch lengths; every TREE/PAIRS cell is flagged.  `window_var` at
      100-bp bins overstates components with ell 100-200 bp by ~8% (upper side, kept).  S3 is NOT TESTABLE on the
      held 1-kb bins (the shortest ell is below the bin) and, after FML-S6 (covariates explain < 40% of the
      explainable DNM variance), weak covariate correlation is the neutral norm: S3 scores for neither side on
      these data, and "covariate correlations" is dropped as a critic-side criterion on the same ground.
  RESOURCES (re-estimated; nothing run).  analytic: 1 process, < 300 MB, < 1 min (envelope: <= 15 (ell, ell) pairs
  x 9 variants x ~100 window sizes, cached).  simulate: 1 process, < 1 GB at 300 Mb (int64/float64 arrays of 3e6
  bins), both sets plus the amendment arms (R1u, BP, lambda_M): ~20-45 min.  realdata: unchanged (~1.5 GB peak,
  < 15 min).  post: seconds.  Order on na-workhorse: analytic, simulate, realdata, then post.
    post  : python -I research/checks/fm_mesa_null.py post research/checks/results/raw/fmnull_real.json \
            research/checks/results/raw/fmnull_post.json
    score : ... --exposure 0.86 --d 0.0137 [--cvc 0.3] [--real research/checks/results/raw/fmnull_real.json]
"""
import functools
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BIN_BP = 100

# name: (sigma_lo, sigma_hi), (ell_lo_bp, ell_hi_bp), arm, source note
PREREG = {
    "M0":   ((0.02, 0.10), (5e6, 2e7), "neutral", "unsourced"),
    "M1":   ((0.05, 0.20), (5e5, 2e6), "neutral", "unsourced"),
    "M2":   ((0.05, 0.20), (2e4, 1e5), "neutral", "unsourced"),
    "M3":   ((0.10, 0.40), (2e2, 2e3), "neutral", "unsourced"),
    "CPG":  ((0.03, 0.15), (5e3, 5e4), "neutral", "unsourced"),
    "GBGC": ((0.02, 0.10), (5e4, 1e6), "neutral", "unsourced; lineage-specific fraction LAMBDA"),
    "ILS":  ((0.125, 0.25), (1e2, 2e3), "neutral", "sigma from CSAC2005 t1/t2; ell unsourced"),
    "ALN":  ((0.016, 0.42), (1e4, 1e5), "unmasked", "unsourced; sigma^2 = pi(1-pi)e^2"),
    "BGS":  ((0.006, 0.0625), (2e5, 2e6), "selection", "unsourced sd(B) x CSAC2005 T2/(t1+T2)"),
}
# Post hoc amendment 2026-10-12 (pre-run, no data seen): literature-backed where verified (docstring (a)-(e)),
# registered bracket where nothing was found.  PREREG above is unchanged from commit 48241c7.
SOURCED = {
    "M0":   ((0.02, 0.10), (5e6, 2e7), "neutral", "unsourced (FML-S4 qualitative only); = PREREG"),
    "M1":   ((0.20, 0.25), (5e5, 2e6), "neutral", "sigma FML-S2 (1-Mb CV 0.15 Jonsson lo, 0.27 Wong hi; Wong may be "
                                                  "technical, Smith Abstract; FML-S8); ell unsourced"),
    "M2":   ((0.05, 0.20), (2e4, 1e5), "neutral", "unsourced; = PREREG; consistent with FML-S2 x FML-S5 derived "
                                                  "100-kb CV 0.22-0.34"),
    "M3":   ((0.10, 0.40), (2e2, 2e3), "neutral", "unsourced (FML-S7 qualitative only); = PREREG"),
    "CPG":  ((0.03, 0.15), (5e3, 5e4), "neutral", "unsourced (FML-HG1 abstract only); = PREREG"),
    "GBGC": ((0.02, 0.10), (5e4, 1e6), "neutral", "unsourced (FML-D4/D5 give no sigma); = PREREG; LAMBDA unsourced"),
    "ILS":  ((0.125, 0.40), (1e2, 2e3), "neutral", "sigma lo CSAC2005 t1/t2 (= PREREG), hi FML-H1 + FML-H2 two-epoch "
                                                   "derivation; ell unsourced"),
    "ALN":  ((0.016, 0.42), (1e4, 1e5), "unmasked", "unsourced; = PREREG"),
    "BGS":  ((0.0077, 0.15), (2e5, 2e6), "selection", "ratio CSAC2005 (lo) / FML-H1 + FML-H2 (hi) x sd(B) unsourced "
                                                      "/ mean B FML-M2; ell unsourced"),
}
PARAM_SETS = {"PREREG": PREREG, "SOURCED": SOURCED}
COMPONENTS = PREREG          # active set; switch only through use_set()
ACTIVE = "PREREG"
MUTATIONAL = ("M0", "M1", "M2", "M3", "CPG")
LAMBDA = (0.3, 1.0)
EXPOSURE = (0.5, 1.0)
UNITS = {"H": (0.0051, 0.0051), "C": (0.0057, 0.0057), "G": (0.0077, 0.0077), "DHC": (0.0123, 0.0146),
         "TREE": (0.03, 0.15)}
# seven-ape tree, UNSOURCED branch lengths except H, C (C term + Pan stem), G terminal (R4-FM in-house):
# ((((H,(C,B)),G),(So,Bo)),Sia); entries: (leaves below, length per site)
TREE = [(("H",), 0.0051), (("C",), 0.0020), (("B",), 0.0020), (("C", "B"), 0.0037), (("H", "C", "B"), 0.0020),
        (("G",), 0.0077), (("H", "C", "B", "G"), 0.0040), (("So",), 0.0030), (("Bo",), 0.0030),
        (("So", "Bo"), 0.0100), (("Sia",), 0.0300)]
NTAXA = 7
READINGS = {"R1": 80.0, "R1x": 81.0, "R2": 6400.0}
WGRID = (1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7)


# ------------------------------------------------------------------------------------------------ analytic core
def use_set(name):
    """Make PARAM_SETS[name] the active COMPONENTS (post hoc amendment 2026-10-12)."""
    global COMPONENTS, ACTIVE
    COMPONENTS, ACTIVE = PARAM_SETS[name], name
    unit_bands.cache_clear()


def mutation_cv(W, which, first_order=False):
    """Model CV of the window-mean mutation rate (M0-M3 + CPG) at edge 'lo' / 'hi'; comparable to Smith 2018."""
    comps = comp_params(which, MUTATIONAL)
    return math.sqrt(cv2_first_order(W, comps) if first_order else window_var(W, comps))


def comp_params(which, names):
    """which: 'lo' or 'hi' -> list of (sigma, ell)."""
    k = 0 if which == "lo" else 1
    return [(COMPONENTS[n][0][k], COMPONENTS[n][1][k]) for n in names]


def g_cont(x):
    x = np.asarray(x, float)
    return np.where(x < 1e-6, 1.0 - x / 3.0, 2.0 * (x - 1.0 + np.exp(-x)) / np.maximum(x, 1e-300) ** 2)


def cov_R(lags_bp, comps):
    """Autocovariance of R = prod of independent log-normal mean-1 factors (log-scale exp. correlation)."""
    out = np.ones_like(lags_bp, dtype=float)
    for s, ell in comps:
        s2 = math.log1p(s * s)
        corr = hudson_corr(ell[1] * lags_bp) if isinstance(ell, tuple) else np.exp(-lags_bp / ell)   # amendment 2
        out *= np.exp(s2 * corr)
    return out - 1.0


def window_var(W, comps, bin_bp=BIN_BP):
    """Var of the window mean of R over n = W/bin_bp bins (exact discrete covariance sum)."""
    n = max(1, int(round(W / bin_bp)))
    k = np.arange(n, dtype=float)
    c = cov_R(k * bin_bp, comps)
    return float((n * c[0] + 2.0 * ((n - k[1:]) * c[1:]).sum()) / n ** 2)


def cv2_first_order(W, comps):
    return float(sum(s * s * (g_hudson(W * ell[1]) if isinstance(ell, tuple) else g_cont(W / ell)) for s, ell in comps))


def tree_struct():
    """D_struct and pairwise multiplicity-weighted length for U-PAIRS."""
    num = den = 0.0
    for leaves, t in TREE:
        s = len(leaves)
        a = s * (NTAXA - s)
        num += a * a * t
        den += a * t
    return num / den, den


NEUTRAL = ("M0", "M1", "M2", "M3", "CPG", "GBGC", "ILS")


def band(W, d, which):
    """Return D for band edge which in {'N_lo', 'N_hi_masked', 'N_hi_unmasked', 'K_hi'} at exposure edge."""
    if which == "N_lo":
        comps, c = comp_params("lo", NEUTRAL), EXPOSURE[0]
    elif which == "N_hi_masked":
        comps, c = comp_params("hi", NEUTRAL), EXPOSURE[1]
    elif which == "N_hi_unmasked":
        comps, c = comp_params("hi", NEUTRAL + ("ALN",)), EXPOSURE[1]
    elif which == "K_hi":
        comps, c = comp_params("hi", NEUTRAL + ("ALN", "BGS")), EXPOSURE[1]
    else:
        raise ValueError(which)
    return 1.0 + c * W * d * window_var(W, comps), 1.0 + c * W * d * cv2_first_order(W, comps)


@functools.lru_cache(maxsize=None)
def unit_bands(unit, W):
    """Bands for a unit; d bracket edges go with the band edge (lo d for N_lo, hi d for N_hi)."""
    out = {}
    if unit.startswith("PAIRS"):
        dstruct, dp = tree_struct()
        for edge, scale in (("N_lo", 0.7), ("N_hi_masked", 1.3), ("N_hi_unmasked", 1.3), ("K_hi", 1.3)):
            D, _ = band(W, dp * scale, edge)          # 1 + c W d_pairs V(W), rate field fully shared by branches
            ex = D - 1.0
            # naive: Poisson null, structural excess counted as overdispersion; struct: Var / Var_uniform
            out[edge] = dstruct + ex if unit == "PAIRS-naive" else 1.0 + ex / dstruct
        out["D_struct"] = dstruct
        return out
    dlo, dhi = UNITS[unit]
    for edge in ("N_lo", "N_hi_masked", "N_hi_unmasked", "K_hi"):
        D, D1 = band(W, dlo if edge == "N_lo" else dhi, edge)
        out[edge] = D
        out[edge + "_firstorder"] = D1
    return out


def classify(value, lo, hi):
    if value > 3.0 * hi:
        return "DAY"
    if value > hi:
        return "MARGINAL"
    if value >= lo:
        return "CRITIC"
    return "BELOW"


def crossing_windows(unit, T, hi_key):
    """Smallest W where N_hi >= T (below it T is anomalous) and smallest W where N_lo >= T (beyond it T is low)."""
    Ws = np.logspace(3, 7.5, 91)
    w_hi = w_lo = None
    for W in Ws:
        b = unit_bands(unit, W)
        if w_hi is None and b[hi_key] >= T:
            w_hi = float(W)
        if w_lo is None and b["N_lo"] >= T:
            w_lo = float(W)
    return w_hi, w_lo


def analytic(outjson, fm_json=None):
    """Both parameter sets, side by side (post hoc amendment 2026-10-12)."""
    res = {"sets": {}}
    for name in PARAM_SETS:
        use_set(name)
        print(f"===== parameter set {name}")
        res["sets"][name] = analytic_one(fm_json)
        print_table(res["sets"][name])
    use_set("PREREG")
    a, b = res["sets"]["PREREG"], res["sets"]["SOURCED"]
    print("===== side by side: unit|W  edge  PREREG  SOURCED")
    for k in a["table"]:
        for e in ("N_lo", "N_hi_masked", "N_hi_unmasked", "K_hi"):
            print(k, e, f"{a['table'][k][e]:.3g}", f"{b['table'][k][e]:.3g}")
    for k in a["scores"]:
        if a["scores"][k] != b["scores"][k]:
            print("score differs", k, a["scores"][k], b["scores"][k])
    for k in a["bgs_share"]:
        print("bgs_share", k, f"{a['bgs_share'][k]:.3g}", f"{b['bgs_share'][k]:.3g}")
    res["amend2"] = analytic_amend()          # post hoc amendment 2; registered outputs above are unchanged
    json.dump(res, open(outjson, "w"), indent=1)
    return res


def analytic_one(fm_json=None):
    fm_json = fm_json or os.path.join(HERE, "results", "raw", "fm_analyse.json")
    units = list(UNITS) + ["PAIRS-naive", "PAIRS-struct"]
    res = {"param_set": ACTIVE,
           "mutation_cv": {f"{int(W)}|{e}": mutation_cv(W, e) for W in (1e4, 1e5, 1e6, 1e7) for e in ("lo", "hi")},
           "brackets": {k: list(map(list, v[:2])) + list(v[2:]) for k, v in COMPONENTS.items()},
           "units": UNITS, "tree_struct": tree_struct(), "table": {}, "crossings": {}, "scores": {}}
    for u in units:
        for W in WGRID:
            res["table"][f"{u}|{int(W)}"] = unit_bands(u, W)
    for u in units:
        for r, T in READINGS.items():
            for hk in ("N_hi_masked", "N_hi_unmasked"):
                res["crossings"][f"{u}|{r}|{hk}"] = crossing_windows(u, T, hk)
            for W in WGRID:
                b = res["table"][f"{u}|{int(W)}"]
                res["scores"][f"{u}|{r}|{int(W)}"] = {
                    "masked": classify(T, b["N_lo"], b["N_hi_masked"]),
                    "unmasked": classify(T, b["N_lo"], b["N_hi_unmasked"])}
    # selection arm share
    res["bgs_share"] = {}
    for u in ("H", "DHC"):
        for W in WGRID:
            b = res["table"][f"{u}|{int(W)}"]
            res["bgs_share"][f"{u}|{int(W)}"] = (b["K_hi"] - b["N_hi_unmasked"]) / (b["N_hi_unmasked"] - 1.0)
    res["inhouse"] = inhouse(fm_json) if os.path.exists(fm_json) else "fm_analyse.json not found"
    return res


def inhouse(fm_json):
    """P4 and P5 against the committed R4-FM grid (raw/fm_analyse.json)."""
    g = json.load(open(fm_json))["grid"]
    Wmap = {"1kb": 1e3, "10kb": 1e4, "100kb": 1e5, "1Mb": 1e6}
    cells, curves = [], {}
    for key, v in g.items():
        st, filt, wl = key.split("|")
        if st != "auto" or wl not in Wmap:
            continue
        W = Wmap[wl]
        hk = "N_hi_unmasked" if filt in ("F0", "F1") else "N_hi_masked"
        for L in ("H", "C", "B", "G", "DHC"):
            if L not in v or "phi" not in v[L]:
                continue
            p, phi = v[L]["density"], v[L]["phi"]
            lo, _ = band(W, p, "N_lo")
            hi, _ = band(W, p, hk)
            cells.append(dict(cell=key, L=L, phi=phi, d=p, lo=lo, hi=hi, out=classify(phi, lo, hi)))
            curves.setdefault((filt, L), []).append((W, phi, p))
    inside = sum(c["out"] == "CRITIC" for c in cells)
    p4 = {}
    for (filt, L), pts in curves.items():
        pts.sort()
        if len(pts) < 2:
            continue
        lw = np.log([q[0] for q in pts])
        lp = np.log([max(q[1], 1.0001) for q in pts])
        dmean = float(np.mean([q[2] for q in pts]))
        hk = "N_hi_unmasked" if filt in ("F0", "F1") else "N_hi_masked"
        for r, T in READINGS.items():
            if lp[-1] >= math.log(T):
                W80 = float(np.exp(np.interp(math.log(T), lp, lw)))
                extrap = False
            else:   # log-log extrapolation from the last two points (flagged)
                slope = (lp[-1] - lp[-2]) / (lw[-1] - lw[-2])
                W80 = float(np.exp(lw[-1] + (math.log(T) - lp[-1]) / max(slope, 1e-6)))
                extrap = True
            lo, _ = band(W80, dmean, "N_lo")
            hi, _ = band(W80, dmean, hk)
            p4[f"{filt}|{L}|{r}"] = dict(W_T=W80, extrapolated=extrap, lo=lo, hi=hi, out=classify(T, lo, hi))
    return {"P5_cells": cells, "P5_inside": inside, "P5_n": len(cells), "P4": p4,
            "status": "P4, P5: informed, not predictive (amendment 2, A10); own-exposure version in mode `post`"}


def print_table(res):
    print("mutation_cv (Smith 2018 FML-S2 at 1 Mb: 0.15, 0.18, 0.27)", {k: round(v, 3) for k, v in res["mutation_cv"].items()})
    print("unit | W | N_lo | N_hi masked | N_hi unmasked | K_hi")
    for k, b in res["table"].items():
        print(k, *(f"{b[e]:.3g}" for e in ("N_lo", "N_hi_masked", "N_hi_unmasked", "K_hi")))
    for k, v in res["crossings"].items():
        print("cross", k, v)
    if isinstance(res.get("inhouse"), dict):
        ih = res["inhouse"]
        print(f"P5 inside {ih['P5_inside']}/{ih['P5_n']}")
        for k, v in ih["P4"].items():
            print("P4", k, {a: (round(b, 3) if isinstance(b, float) else b) for a, b in v.items()})


# ------------------------------------------------------------------------------------------------ simulation
def ar1_lognormal(n, sigma, ell, rng, bin_bp=BIN_BP):
    from scipy.signal import lfilter
    s2 = math.log1p(sigma * sigma)
    s = math.sqrt(s2)
    rho = math.exp(-bin_bp / ell)
    eps = rng.standard_normal(n)
    x = lfilter([s * math.sqrt(1.0 - rho * rho)], [1.0, -rho], eps, zi=[rho * s * rng.standard_normal()])[0]
    return np.exp(x - s2 / 2.0)


def rate_field(n, comps, rng, bin_bp=BIN_BP):
    R = np.ones(n)
    for s, ell in comps:
        if s > 0:
            R *= ar1_lognormal(n, s, ell, rng, bin_bp)
    return R


def disp(counts, W_bins):
    k = len(counts) // W_bins
    w = counts[: k * W_bins].reshape(k, W_bins).sum(axis=1)
    return float(w.var(ddof=1) / w.mean()), w


def expected_sample_D(W, d, comps, n_total, bin_bp=BIN_BP):
    """E[s^2]/mean over K windows of one stationary chromosome of n_total bins (finite-genome correction)."""
    nW = int(round(W / bin_bp))
    K = n_total // nW
    Vw = window_var(W, comps, bin_bp)
    VG = window_var(K * nW * bin_bp, comps, bin_bp)
    m = W * d
    return 1.0 + m * K / (K - 1.0) * (Vw - VG)


def split_phi(h, c):
    N = h + c
    ok = N > 0
    p = h[ok].sum() / N[ok].sum()
    e = N[ok] * p
    return float((((h[ok] - e) ** 2) / (e * (1 - p))).sum() / (ok.sum() - 1))


def sim_two_lineage(n, comps_shared, comps_ls, dH, dC, rng, blocks=None, bgs=None, bin_bp=BIN_BP):
    """H and C counts with a shared field, independent lineage-specific fields, optional BGS (shared, with an
    observed covariate) and optional H-only sigillation blocks (Lb_bp, e, f)."""
    Rs = rate_field(n, comps_shared, rng, bin_bp)
    cov = None
    if bgs is not None:
        s, ell = bgs
        gfield = ar1_lognormal(n, 0.5, ell, rng, bin_bp)        # gene-density covariate (log-normal)
        z = (np.log(gfield) - np.log(gfield).mean()) / np.log(gfield).std()
        Rs = Rs * np.clip(1.0 - s * z, 0.05, None)
        cov = z + 0.5 * rng.standard_normal(n)
    RH = Rs * rate_field(n, comps_ls, rng, bin_bp)
    RC = Rs * rate_field(n, comps_ls, rng, bin_bp)
    if blocks is not None:
        Lb, e, f = blocks
        nb = max(1, int(round(Lb / bin_bp)))
        nblk = int(round(f * n / nb))
        starts = rng.choice(n // nb, size=nblk, replace=False) * nb
        mult = np.ones(n)
        for s0 in starts:
            mult[s0:s0 + nb] += e
        RH = RH * mult
    H = rng.poisson(bin_bp * dH * RH)
    C = rng.poisson(bin_bp * dC * RC)
    return H, C, cov


def central(names):
    return [(math.sqrt(COMPONENTS[k][0][0] * COMPONENTS[k][0][1]), math.sqrt(COMPONENTS[k][1][0] * COMPONENTS[k][1][1]))
            for k in names]


def simulate(outjson, genome_mb=300, reps=10, seed=20261012):
    """Both parameter sets, same seed (post hoc amendment 2026-10-12)."""
    res = {"sets": {}}
    for name in PARAM_SETS:
        use_set(name)
        print(f"===== parameter set {name}", flush=True)
        res["sets"][name] = simulate_one(genome_mb, reps, seed)
    use_set("PREREG")
    res["amend2"] = simulate_amend(int(genome_mb * 1e6 / BIN_BP), reps, np.random.default_rng(seed + 2))
    print("amend2", json.dumps(res["amend2"]), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)
    return res


def simulate_one(genome_mb, reps, seed):
    rng = np.random.default_rng(seed)
    n = int(genome_mb * 1e6 / BIN_BP)
    res = {"param_set": ACTIVE, "genome_mb": genome_mb, "reps": reps, "seed": seed, "P6": {}, "arms": {}}
    # P6: neutral bands reproduced (single lineage, d = 0.012 and 0.0051)
    for edge, comps in (("N_lo", comp_params("lo", NEUTRAL)), ("N_hi_masked", comp_params("hi", NEUTRAL)),
                        ("N_hi_unmasked", comp_params("hi", NEUTRAL + ("ALN",))), ("poisson", [])):
        for d in (0.0051, 0.012):
            Ds = {W: [] for W in (1e3, 1e4, 1e5, 1e6)}
            for _ in range(reps):
                cnt = rng.poisson(BIN_BP * d * rate_field(n, comps, rng))
                for W in Ds:
                    Ds[W].append(disp(cnt, int(W / BIN_BP))[0])
            for W, v in Ds.items():
                exp = expected_sample_D(W, d, comps, n) if comps else 1.0
                res["P6"][f"{edge}|{d}|{int(W)}"] = dict(sim=float(np.mean(v)), sd=float(np.std(v)), exp=exp,
                                                         rel=float((np.mean(v) - 1) / (exp - 1)) if comps else None)
    # selection and sigillation arms (two lineages; central neutral; lineage-specific GBGC fraction LAMBDA)
    lam = math.sqrt(LAMBDA[0] * LAMBDA[1])
    sh = [c for k, c in zip(NEUTRAL, central(NEUTRAL)) if k != "GBGC"]
    sg, lg = central(("GBGC",))[0]
    shared = sh + [(sg * math.sqrt(1 - lam), lg)]
    ls = [(sg * math.sqrt(lam), lg)]
    scen = {"S0_neutral": {}, "S0_hi_ls": {"ls": [(COMPONENTS["GBGC"][0][1], COMPONENTS["GBGC"][1][1])]},
            "S1_bgs": {"bgs": (COMPONENTS["BGS"][0][1], 1e6)}}
    for Lb in (2e4, 1e5):
        for e in (0.5, 1.0):
            for f in (0.005, 0.02):
                scen[f"S2_sig_L{int(Lb/1e3)}k_e{e}_f{f}"] = {"blocks": (Lb, e, f)}
    scen["S2_sig_dominant_L100k_e2_f0.5"] = {"blocks": (1e5, 2.0, 0.5)}
    for name, sp in scen.items():
        acc = {}
        for _ in range(reps):
            H, C, cov = sim_two_lineage(n, shared, sp.get("ls", ls), 0.0051, 0.0057, rng,
                                        blocks=sp.get("blocks"), bgs=sp.get("bgs"))
            for W in (1e4, 1e5, 1e6):
                nb = int(W / BIN_BP)
                k = n // nb
                h = H[: k * nb].reshape(k, nb).sum(1).astype(float)
                c = C[: k * nb].reshape(k, nb).sum(1).astype(float)
                r = acc.setdefault(int(W), {"phi_H": [], "phi_C": [], "phi_HC": [], "corr_HC": [], "corr_cov": [],
                                            "phi_res_H": []})
                r["phi_H"].append(h.var(ddof=1) / h.mean())
                r["phi_C"].append(c.var(ddof=1) / c.mean())
                r["phi_HC"].append(split_phi(h, c))
                r["corr_HC"].append(float(np.corrcoef(h, c)[0, 1]))
                E = h.sum() / c.sum() * (c + 1.0)          # shared-rate null as in R4-FM (one pseudo-count)
                r["phi_res_H"].append(float(((h - E) ** 2 / E).sum() / (k - 1)))
                if cov is not None:
                    cw = cov[: k * nb].reshape(k, nb).mean(1)
                    r["corr_cov"].append(float(np.corrcoef(h, cw)[0, 1]))
        res["arms"][name] = {W: {s: (float(np.mean(v)) if v else None) for s, v in r.items()} for W, r in acc.items()}
        print(name, json.dumps(res["arms"][name]), flush=True)
    return res


# ------------------------------------------------------------------------------------------------ real data
def realdata(npz, outjson):
    sys.path.insert(0, HERE)
    import fm_mesa_replication as fm
    from scipy.optimize import nnls
    z, meta, chroms_all = fm.load(npz)
    auto = [c for c in chroms_all if c not in ("chrX", "chrY", "chrM")]
    WK = (1, 3, 10, 30, 100, 300, 1000, 3000, 10000)
    ells = np.array([1e3, 1e4, 1e5, 1e6, 1e7])
    res = {"grid": {}, "fit": {}, "W_T": {}}
    for filt in ("F0", "F2"):
        curves = {}
        for Wk in WK:
            try:
                w, cid, ok = fm.windows(z, auto, filt, Wk)
            except ValueError:          # no chromosome long enough for this window
                continue
            if ok.sum() < 20:
                continue
            m = w["m"][ok].astype(float)
            cell = {"k": int(ok.sum()), "m_mean": float(m.mean())}
            m_all = w["m"].astype(float)       # amendment 2 (A8, R1u): exposure CV, used windows and all windows
            cell["cv_c_ok"] = float(m.std(ddof=1) / m.mean())
            cell["cv_c_all"] = float(m_all.std(ddof=1) / m_all.mean())
            cls = {}
            for name, idx in (("rep", (1, 3, 5, 7)), ("cpg", (2, 3, 6, 7)), ("dup", (4, 5, 6, 7))):
                idx = tuple(i for i in idx if i in fm.FILTERS[filt])
                if not idx:
                    continue
                a, _, _ = fm.windows_cls(z, auto, idx, Wk)
                cls[name] = a[ok] / np.maximum(m, 1)   # same window order as fm.windows (per chromosome, nb windows)
            X = [np.ones_like(m), w["gc"][ok] / m, w["hh"][ok] / m] + list(cls.values())
            X = np.column_stack(X)
            for L in ("H", "C", "B", "G", "DHC"):
                n = w[L][ok].astype(float)
                phi, _ = fm.phi_uniform(n, m)
                p = n.sum() / m.sum()
                y = np.log((n + 0.5) / m)
                beta, *_ = np.linalg.lstsq(X, y, rcond=None)
                E = m * np.exp(X @ beta)
                E *= n.sum() / E.sum()
                phi_cov = float(((n - E) ** 2 / E).sum() / (len(n) - X.shape[1]))
                cv2 = (phi - 1.0) / (m.mean() * p)
                cell[L] = {"phi": phi, "density": float(p), "cv2_excess": float(cv2), "phi_cov": phi_cov}
                n_all = w[L].astype(float)
                cell[L]["D_unnorm_ok"] = float(n.var(ddof=1) / n.mean())
                cell[L]["D_unnorm_all"] = float(n_all.var(ddof=1) / n_all.mean())
                curves.setdefault(L, []).append((Wk * 1000.0, phi, cv2))
            h, c, g = (w[k][ok].astype(float) for k in ("H", "C", "G"))
            cell["corr_HC"] = float(np.corrcoef(h / m, c / m)[0, 1])
            cell["corr_HG"] = float(np.corrcoef(h / m, g / m)[0, 1])
            cell["phi_HC"] = fm_split(h, c)
            res["grid"][f"{filt}|{Wk}kb"] = cell
            print(filt, Wk, json.dumps({k: v for k, v in cell.items() if not isinstance(v, dict)}), flush=True)
        for L, pts in curves.items():
            lw = np.log([q[0] for q in pts])
            lp = np.log(np.maximum([q[1] for q in pts], 1.0001))
            for r, T in READINGS.items():
                res["W_T"][f"{filt}|{L}|{r}"] = (float(np.exp(np.interp(math.log(T), lp, lw)))
                                                 if lp.max() >= math.log(T) else None)
            pos = [q for q in pts if q[2] > 0]
            Ws = np.array([q[0] for q in pos])
            cv2 = np.array([q[2] for q in pos])
            if len(pos) < 2:
                res["fit"][f"{filt}|{L}"] = "fewer than 2 windows sizes with positive excess"
                continue
            A = np.column_stack([g_cont(Ws / l) for l in ells]) / cv2[:, None]
            coef, rnorm = nnls(A, np.ones_like(cv2))
            res["fit"][f"{filt}|{L}"] = {"ell_bp": ells.tolist(), "sigma2": coef.tolist(), "rel_resid": float(rnorm)}
    json.dump(res, open(outjson, "w"), indent=1)
    return res


def fm_split(h, c):
    return split_phi(h, c)


# ------------------------------------------------------------------------------- amendment 2 (2026-10-12, pre-run)
# Everything in this section is post hoc amendment 2 (docstring A1-A13).  It adds outputs beside the registered ones
# and does not change PREREG, SOURCED, band(), unit_bands(), classify() or the registered predictions.
SMITH = {"Francioli": (0.18, -0.25), "Wong": (0.27, -0.10), "Jonsson": (0.15, -0.16)}   # FML-S2 CV(1 Mb), FML-S5 slope
CAL = {"ALL3": ("Jonsson", "Wong"), "NOWONG": ("Jonsson", "Francioli"), "FRANC": ("Francioli", "Francioli")}
PERSIST = (1.0, 0.5)                    # share of the DNM-landscape SD that persists over the divergence time (lo edge)
ELL_M1 = tuple(np.geomspace(5e5, 2e6, 5))
ELL_M0 = tuple(np.geomspace(5e6, 2e7, 3))
CVC = (0.2, 0.5)                        # CV of exposure across windows, reading R1u; UNSOURCED until realdata
LAMBDA_M = (0.0, 0.25, 0.5)             # lineage-specific share of the mutational variance (A9)
HOB = dict(t1=4.1, delta=2.0, N_HC=(35e3, 65e3, 95e3), N_HCG=(35e3, 45e3, 55e3), gen=25e-6)   # FML-H1; Delta quoted (A11)
RHO_BP = (4 * 95e3 * 1.5e-8, 4 * 35e3 * 1e-8)     # 4 N r per bp: (low-variance edge, high-variance edge)
BP = dict(n_snv=42.87e6, n_indel=5.40e6, bp_total=410e6, one_bp=0.397, tail_hi=10.0, d=(0.13, 0.14))  # R4-GAP07t
_HA, _HB = (13 - math.sqrt(97)) / 2, (13 + math.sqrt(97)) / 2


def hudson_corr(y):
    """Correlation of two-lineage coalescence times at two loci, y = 4 N r x (constant N); checked in selftest."""
    y = np.asarray(y, float)
    return (y + 18.0) / (y * y + 13.0 * y + 18.0)


def g_hudson(Y):
    """(2 / Y^2) int_0^Y (Y - y) hudson_corr(y) dy: variance of the window mean relative to the per-locus variance."""
    Y = float(Y)
    if Y < 1e-6:
        return 1.0
    A, B = (18 - _HA) / (_HB - _HA), (_HB - 18) / (_HB - _HA)
    la, lb = math.log1p(Y / _HA), math.log1p(Y / _HB)
    i0 = A * la + B * lb
    i1 = A * (Y - _HA * la) + B * (Y - _HB * lb)
    return 2.0 * (Y * i0 - i1) / (Y * Y)


def hudson_cov_check(rho):
    """Independent first-step derivation of Cov(Ta, Tb) (time in 2N generations, rho = 4 N r).  States: A two
    lineages carrying both loci; B three lineages (ab, a, b); C four lineages (a, a, b, b).  f = E[Ta Tb]."""
    lA, lB, lC = 1 + rho, 3 + rho / 2, 6.0
    # f_s = 2/l^2 + (1/l) sum_j p_j (E[Ta'] + E[Tb'])_j + sum_j p_j f_j ; after one locus coalesces: sum = 1, f = 0
    M = np.array([[1.0, -rho / lA, 0.0], [-1 / lB, 1.0, -(rho / 2) / lB], [0.0, -4 / lC, 1.0]])
    rhs = np.array([2 / lA ** 2 + (rho / lA) * 2 / lA,
                    2 / lB ** 2 + ((1 + 1 + 2 + (rho / 2) * 2) / lB) / lB,
                    2 / lC ** 2 + ((1 + 1 + 4 * 2) / lC) / lC])
    return float(np.linalg.solve(M, rhs)[0] - 1.0)


def two_epoch(t1, N1, N2, delta, gen=25e-6):
    """Coalescence beyond the HC split: rate 1/(2 N1 g) for delta My, then 1/(2 N2 g).  Returns E[T2], sd,
    sigma = sd / (t1 + E), mean fraction E / (t1 + E).  Times in My."""
    m1, m2 = 2 * N1 * gen, 2 * N2 * gen
    q = math.exp(-delta / m1)
    e1 = m1 * (1 - q) + q * m2
    e2 = 2 * m1 * m1 * (1 - q) - 2 * q * m1 * delta + q * (2 * delta * m2 + 2 * m2 * m2)
    sd = math.sqrt(e2 - e1 * e1)
    return e1, sd, sd / (t1 + e1), e1 / (t1 + e1)


def _hob_grid():
    return [two_epoch(HOB["t1"], a, b, HOB["delta"], HOB["gen"]) for a in HOB["N_HC"] for b in HOB["N_HCG"]]


ILS_HI2 = max(x[2] for x in _hob_grid())
BGS_HI2 = max(x[3] for x in _hob_grid()) * 0.25 / 0.74
AMENDED = dict(SOURCED)
AMENDED["M0"] = (None, (5e6, 2e7), "neutral", "envelope: FML-S2 x FML-S5 at 10 Mb (derived); see m_envelope")
AMENDED["M1"] = (None, (5e5, 2e6), "neutral", "envelope: FML-S2 at 1 Mb; see m_envelope")
AMENDED["ILS"] = ((0.125, ILS_HI2), (("H", RHO_BP[0]), ("H", RHO_BP[1])), "neutral",
                  "sigma lo CSAC2005, hi two_epoch(FML-H1, Delta quoted); two-locus kernel, r unsourced")
AMENDED["BGS"] = ((0.0077, BGS_HI2), (2e5, 2e6), "selection", "two-epoch mean fraction x sd(B) unsourced / mean B FML-M2")
SETS2 = {"PREREG": PREREG, "SOURCED": SOURCED, "AMENDED": AMENDED}
EDGES2 = {"N_lo": ("lo", NEUTRAL), "N_hi_masked": ("hi", NEUTRAL), "N_hi_unmasked": ("hi", NEUTRAL + ("ALN",)),
          "K_hi": ("hi", NEUTRAL + ("ALN", "BGS")), "K_hi_masked": ("hi", NEUTRAL + ("BGS",))}


def cp(setd, which, names):
    k = 0 if which == "lo" else 1
    return [(setd[n][0][k], setd[n][1][k]) for n in names]


def smith_targets(ds, persist=1.0):
    cv1, b = SMITH[ds]
    return (persist * cv1) ** 2, (persist * cv1 * 10 ** b) ** 2


@functools.lru_cache(maxsize=None)
def m_envelope(which, ds, persist):
    """Feasible (sigma_M0, ell_M0, sigma_M1, ell_M1) reproducing the Smith targets at 1 Mb and 10 Mb (first order)."""
    others = cp(AMENDED, which, ("M2", "M3", "CPG"))
    t1, t10 = smith_targets(ds, persist)
    r = np.array([t1 - cv2_first_order(1e6, others), t10 - cv2_first_order(1e7, others)])
    out = []
    for l1 in ELL_M1:
        for l0 in ELL_M0:
            A = np.array([[float(g_cont(1e6 / l1)), float(g_cont(1e6 / l0))],
                          [float(g_cont(1e7 / l1)), float(g_cont(1e7 / l0))]])
            a, b = np.linalg.solve(A, r)
            if a >= 0 and b >= 0:
                out.append((math.sqrt(b), l0, math.sqrt(a), l1))
    return tuple(out)


@functools.lru_cache(maxsize=None)
def V_edge(setname, edge, W, cal="ALL3", persist=1.0):
    """Var of the window-mean rate at a band edge.  AMENDED: min / max over the M0-M1 constraint envelope."""
    which, names = EDGES2[edge]
    if setname != "AMENDED":
        return window_var(W, cp(SETS2[setname], which, names))
    ds = CAL[cal][0 if which == "lo" else 1]
    rest = cp(AMENDED, which, [n for n in names if n not in ("M0", "M1")])
    vals = [window_var(W, [(s0, l0), (s1, l1)] + rest)
            for s0, l0, s1, l1 in m_envelope(which, ds, persist if which == "lo" else 1.0)]
    return min(vals) if which == "lo" else max(vals)


def mutation_cv_env(W, cal, persist):
    """First-order mutation CV (M0-M3 + CPG) over the envelope: (min at lo edge, max at hi edge)."""
    out = []
    for which, pick in (("lo", min), ("hi", max)):
        ds = CAL[cal][0 if which == "lo" else 1]
        others = cp(AMENDED, which, ("M2", "M3", "CPG"))
        out.append(math.sqrt(pick(cv2_first_order(W, [(s0, l0), (s1, l1)] + others)
                                  for s0, l0, s1, l1 in m_envelope(which, ds, persist if which == "lo" else 1.0))))
    return out


def bp_struct():
    """D_struct = E[L^2] / E[L] for gap-inclusive bp: (floor with equal indel lengths, floor given the 1-bp share,
    flagged upper edge = tail factor x the second floor).  Derived from the GAP-07t summary counts."""
    ns, ni, q = BP["n_snv"], BP["n_indel"], BP["one_bp"]
    lbar = (BP["bp_total"] - ns) / ni
    f1 = (ns + ni * lbar ** 2) / BP["bp_total"]
    f2 = (ns + ni * (q + (1 - q) * ((lbar - q) / (1 - q)) ** 2)) / BP["bp_total"]
    return f1, f2, BP["tail_hi"] * f2


def unit_info(unit):
    """(d_lo, d_hi, D_struct_lo, D_struct_hi, mode); mode in plain / naive / struct."""
    if unit.startswith("PAIRS"):
        ds, dp = tree_struct()
        return 0.7 * dp, 1.3 * dp, ds, ds, unit.split("-")[1]
    if unit.startswith("BP"):
        f1, _, f3 = bp_struct()
        return BP["d"][0], BP["d"][1], f1, f3, unit.split("-")[1]
    return UNITS[unit] + (1.0, 1.0, "plain")


def bands2(setname, W, unit="DHC", d=None, c=None, cal="ALL3", persist=1.0, cvc=(0.0, 0.0)):
    """Amended bands.  d, c: (lo, hi) pairs overriding the unit bracket / EXPOSURE; cvc: exposure CV for R1u."""
    dlo, dhi, slo, shi, mode = unit_info(unit)
    if d is not None:
        dlo, dhi = d
    clo, chi = EXPOSURE if c is None else c
    out = {}
    for edge in EDGES2:
        lo = edge == "N_lo"
        V = V_edge(setname, edge, float(W), cal, persist)
        cv2 = (cvc[0] if lo else cvc[1]) ** 2
        ex = (clo if lo else chi) * W * (dlo if lo else dhi) * (V * (1 + cv2) + cv2)
        if mode == "naive":
            out[edge] = (slo if lo else shi) + ex
        elif mode == "struct":
            out[edge] = 1.0 + ex / (shi if lo else slo)
        else:
            out[edge] = 1.0 + ex
    for m in ("masked", "unmasked"):
        out["N_c_" + m] = centre(out["N_lo"], out["N_hi_" + m])
    out["ALN_part"] = out["N_hi_unmasked"] - out["N_hi_masked"]
    out["ALN_share"] = out["ALN_part"] / max(out["N_hi_unmasked"] - 1.0, 1e-12)
    out["BGS_part"] = out["K_hi"] - out["N_hi_unmasked"]
    out["flags"] = [f for f, on in (("under_sourced_fine_scale", W <= 3e4), ("beyond_smith_range", W > 1e7),
                                    ("unsourced_tree", unit in ("TREE", "PAIRS-naive", "PAIRS-struct")),
                                    ("unsourced_indel_tail", unit.startswith("BP")),
                                    ("unsourced_cvc", cvc != (0.0, 0.0))) if on]
    return out


def centre(lo, hi):
    return 1.0 + math.sqrt(max(lo - 1.0, 0.0) * max(hi - 1.0, 0.0))


def classify2(value, lo, hi):
    """Amended, symmetric classes (A4)."""
    if value > 3.0 * hi:
        return "DAY"
    if value > hi:
        return "MARGINAL-OUT"
    if value > max(hi / 3.0, centre(lo, hi)):
        return "MARGINAL-IN"
    if value >= lo:
        return "CRITIC"
    return "BELOW-NEAR" if value >= lo / 3.0 else "BELOW-FAR"


def variants2():
    """(label, set, cal, persist): PREREG, SOURCED and the six AMENDED calibration variants."""
    return [("PREREG", "PREREG", "ALL3", 1.0), ("SOURCED", "SOURCED", "ALL3", 1.0)] + \
           [(f"AMENDED|{cal}|persist{p}", "AMENDED", cal, p) for cal in CAL for p in PERSIST]


def to_D(value, reading):
    return value ** 2 if reading == "R2" else (value + 1.0 if reading == "R1x" else value)


def score2(W, value, reading, unit, masked, exposure=None, d=None, cvc=None, real=None):
    """Amended scoring (A2-A8).  Returns per-variant classes, the AMENDED consensus and the reproduction gate."""
    D = to_D(value, reading)
    cv = ((cvc, cvc) if cvc is not None else CVC) if reading == "R1u" else (0.0, 0.0)
    rows = {}
    for label, sname, cal, p in variants2():
        b = bands2(sname, W, unit, d=None if d is None else (d, d), c=None if exposure is None else (exposure, exposure),
                   cal=cal, persist=p, cvc=cv)
        hk = "N_hi_masked" if masked else "N_hi_unmasked"
        cls = classify2(D, b["N_lo"], b[hk])
        cls_m = classify2(D, b["N_lo"], b["N_hi_masked"])
        rows[label] = dict(N_lo=b["N_lo"], N_hi=b[hk], N_c=centre(b["N_lo"], b[hk]), K_hi=b["K_hi" if not masked else "K_hi_masked"],
                           ALN_part=0.0 if masked else b["ALN_part"], flags=b["flags"], cls=cls,
                           cls_K=classify2(D, b["N_lo"], b["K_hi" if not masked else "K_hi_masked"]),
                           aln_dependent=(not masked) and cls != cls_m,
                           registered_cls=classify(D, b["N_lo"], b[hk]))
    am = [r for k, r in rows.items() if k.startswith("AMENDED")]
    kinds = sorted({r["cls"] for r in am})
    consensus = kinds[0] if len(kinds) == 1 else "CAL-DEPENDENT"
    if any(r["aln_dependent"] for r in am):
        consensus = "ALN-DEPENDENT"
    gate = repro_gate(real, unit, masked, D, W, reading) if real is not None else {"gate": "UNGATED (no realdata output given)"}
    moves = consensus in ("DAY", "CRITIC") and gate["gate"] == "REPRODUCED"
    return dict(W=W, D=D, reading=reading, unit=unit, masked=masked, exposure=exposure, d=d, inputs="stated" if exposure
                is not None and d is not None else "registered brackets for missing inputs", variants=rows,
                amended_consensus=consensus, amended_K=sorted({r["cls_K"] for r in am}), gate=gate,
                verdict_move_allowed=bool(moves),
                below_labels=("NOT-HIGH (critic-side, a fortiori); bracket failure at the low edge (Day-side)"
                              if consensus.startswith("BELOW") else None))


def repro_gate(real, unit, masked, D, W=None, reading="R1"):
    """A7: is the stated index D reproduced (within 3x) by the realdata grid at W (or at any measured W)?"""
    if isinstance(real, str):
        real = json.load(open(real))
    filt = "F2" if masked else "F0"
    key = "D_unnorm_all" if reading == "R1u" else "phi"
    pts = sorted((float(k.split("|")[1][:-2]) * 1e3, c[unit][key]) for k, c in real["grid"].items()
                 if k.startswith(filt + "|") and unit in c and key in c[unit])
    if len(pts) < 2:
        return {"gate": "UNTESTED", "why": f"unit {unit} / {key} not measured on the held alignment"}
    ws, ph = np.array([p[0] for p in pts]), np.maximum(np.array([p[1] for p in pts]), 1e-9)
    if W is None:
        ok = [float(w) for w, p in zip(ws, ph) if D / 3.0 <= p <= 3.0 * D]
        return {"gate": "REPRODUCED" if ok else "NOT-REPRODUCED", "W_within_3x": ok, "max_measured": float(ph.max())}
    if not ws[0] <= W <= ws[-1]:
        return {"gate": "UNTESTED", "why": "W outside the measured range"}
    m = float(np.exp(np.interp(math.log(W), np.log(ws), np.log(ph))))
    return {"gate": "REPRODUCED" if D / 3.0 <= m <= 3.0 * D else "NOT-REPRODUCED", "measured": m, "ratio": D / m}


def phi_hc_from(W, dH, dC, comps_ls, c=1.0):
    p = dH / (dH + dC)
    return 1.0 + c * W * (dH + dC) * p * (1 - p) * 2.0 * window_var(W, comps_ls)


def phi_hc_bound(setname, W, lam_m, masked, c=1.0):
    """Neutral upper bound for the H/(H+C) split dispersion (S2), A9.  AMENDED uses SOURCED's mutational hi corner."""
    setd = SOURCED if setname == "AMENDED" else SETS2[setname]
    ls = [(s * math.sqrt(LAMBDA[1]), ell) for s, ell in cp(setd, "hi", ("GBGC",))]
    if lam_m > 0:
        ls += [(s * math.sqrt(lam_m), ell) for s, ell in cp(setd, "hi", MUTATIONAL)]
    if not masked:
        ls += cp(setd, "hi", ("ALN",))
    return phi_hc_from(W, UNITS["H"][0], UNITS["C"][0], ls, c)


def analytic_amend():
    """Amendment-2 tables: bands per variant (incl. units BP-*), amended classes per reading, phi_HC bounds."""
    units = list(UNITS) + ["PAIRS-naive", "PAIRS-struct", "BP-naive", "BP-struct"]
    res = {"status": "post hoc amendment 2 (pre-run); registered outputs are under `sets`",
           "hobolth_two_epoch": dict(ILS_sigma_hi=ILS_HI2, BGS_sigma_hi=BGS_HI2, centre=two_epoch(4.1, 65e3, 45e3, 2.0)),
           "bp_struct": bp_struct(), "smith_derived": {ds: {str(int(W)): cv * (W / 1e6) ** b for W in (1e4, 1e5, 1e6, 1e7)}
                                                       for ds, (cv, b) in SMITH.items()},
           "envelope": {f"{w}|{ds}|{p}": m_envelope(w, ds, p) for w in ("lo", "hi") for ds in SMITH
                        for p in (PERSIST if w == "lo" else (1.0,))},
           "mutation_cv_env": {f"{cal}|persist{p}|{int(W)}": mutation_cv_env(W, cal, p)
                               for cal in CAL for p in PERSIST for W in (1e4, 1e5, 1e6, 1e7)},
           "table": {}, "classes": {}, "phi_hc_bound": {}, "ils_hudson_g": {str(int(W)): [g_hudson(W * r) for r in RHO_BP]
                                                                             for W in WGRID}}
    for label, sname, cal, p in variants2():
        for u in units:
            for W in WGRID:
                b = bands2(sname, W, u, cal=cal, persist=p)
                bu = bands2(sname, W, u, cal=cal, persist=p, cvc=CVC)
                res["table"][f"{label}|{u}|{int(W)}"] = b
                row = {}
                for r, T in list(READINGS.items()) + [("R1u", 80.0)]:
                    bb = bu if r == "R1u" else b
                    row[r] = {"masked": classify2(T, bb["N_lo"], bb["N_hi_masked"]),
                              "unmasked": classify2(T, bb["N_lo"], bb["N_hi_unmasked"]),
                              "K": classify2(T, bb["N_lo"], bb["K_hi"])}
                res["classes"][f"{label}|{u}|{int(W)}"] = row
        for W in (1e4, 1e5, 1e6):
            for lam in LAMBDA_M:
                for m in (True, False):
                    res["phi_hc_bound"][f"{sname}|{int(W)}|lam{lam}|{'masked' if m else 'unmasked'}"] = \
                        phi_hc_bound(sname, W, lam, m)
    print("===== amendment 2: label|unit|W  N_lo  N_c  N_hi masked  ALN_part  K_hi  flags | classes R1 R1u R2 (masked)")
    for k, b in res["table"].items():
        c = res["classes"][k]
        print(k, *(f"{b[e]:.3g}" for e in ("N_lo", "N_c_masked", "N_hi_masked", "ALN_part", "K_hi")), ",".join(b["flags"]),
              "|", c["R1"]["masked"], c["R1u"]["masked"], c["R2"]["masked"])
    for k, v in res["phi_hc_bound"].items():
        print("phi_HC bound", k, f"{v:.3g}")
    for k, v in res["mutation_cv_env"].items():
        print("mutation_cv_env", k, [round(x, 3) for x in v])
    print("smith_derived", res["smith_derived"])
    return res


def sim_r1u(n, comps, comps_c, cbar, d, rng):
    """Unnormalised counts with a varying exposure field (A8, R1u)."""
    return rng.poisson(BIN_BP * d * rate_field(n, comps, rng) * cbar * rate_field(n, comps_c, rng))


def expected_r1u(W, d, comps, comps_c, cbar):
    V, vc = window_var(W, comps), window_var(W, comps_c)
    return 1.0 + cbar * W * d * (V * (1 + vc) + vc)


def draw_len(k, rng, q=0.4, mean_rest=20.0):
    """Indel lengths for the BP check: share q of 1 bp, the rest 1 + geometric (mean mean_rest)."""
    L = np.ones(k)
    rest = rng.random(k) >= q
    L[rest] = 1 + rng.geometric(1.0 / (mean_rest - 1.0), int(rest.sum()))
    return L


def sim_bp(n, comps, d_s, d_i, rng):
    """Gap-inclusive bp per bin: substitutions plus summed indel lengths (A8, U-BP).  Returns bp and (EL, EL2)."""
    R = rate_field(n, comps, rng)
    ns, ni = rng.poisson(BIN_BP * d_s * R), rng.poisson(BIN_BP * d_i * R)
    L = draw_len(int(ni.sum()), rng)
    bp = ns + np.bincount(np.repeat(np.arange(n), ni), weights=L, minlength=n)
    f = d_i / (d_s + d_i)
    return bp, ((1 - f) + f * L.mean(), (1 - f) + f * (L ** 2).mean())


def simulate_amend(n, reps, rng):
    """Amendment-2 simulation arms: the R1u, U-BP and lambda_M formulas against simulation (set-independent inputs)."""
    out = {"R1u": {}, "BP": {}, "phi_HC": {}}
    comps, comps_c = [(0.2, 2e5), (0.15, 5e3)], [(0.3, 5e4)]
    acc = {W: [] for W in (1e4, 1e5, 1e6)}
    accb = {W: [] for W in acc}
    for _ in range(reps):
        cnt = sim_r1u(n, comps, comps_c, 0.75, 0.012, rng)
        bp, (el, el2) = sim_bp(n, comps, 0.012, 0.0015, rng)
        for W in acc:
            acc[W].append(disp(cnt, int(W / BIN_BP))[0])
            accb[W].append(disp(bp, int(W / BIN_BP))[0])
    for W in acc:
        out["R1u"][int(W)] = dict(sim=float(np.mean(acc[W])), exp=expected_r1u(W, 0.012, comps, comps_c, 0.75))
        out["BP"][int(W)] = dict(sim=float(np.mean(accb[W])), D_struct=el2 / el,
                                 exp=el2 / el + W * 0.0135 * el * window_var(W, comps))
    shared = [(0.2, 2e5)]
    for lam in LAMBDA_M[1:]:
        ls = [(0.25 * math.sqrt(lam), 1e5), (0.1, 3e5)]
        acc = {W: [] for W in (1e4, 1e5, 1e6)}
        for _ in range(reps):
            H, C, _ = sim_two_lineage(n, shared, ls, 0.0051, 0.0057, rng)
            for W in acc:
                nb = int(W / BIN_BP)
                k = n // nb
                acc[W].append(split_phi(H[: k * nb].reshape(k, nb).sum(1).astype(float),
                                        C[: k * nb].reshape(k, nb).sum(1).astype(float)))
        for W in acc:
            out["phi_HC"][f"lam{lam}|{int(W)}"] = dict(sim=float(np.mean(acc[W])),
                                                       exp=phi_hc_from(W, 0.0051, 0.0057, ls))
    return out


def post(real_json, outjson):
    """After `realdata`: P4/P5 with each cell's own exposure (informed, not predictive), the reproduction gate per
    reading / lineage / masking, and the measured R1u inputs.  Reads only the realdata output of THIS check."""
    real = json.load(open(real_json))
    res = {"status": "post hoc amendment 2; P4/P5 informed, not predictive", "P5": {}, "cells": [], "gate": {}}
    counts = {}
    for key, cell in real["grid"].items():
        filt, wl = key.split("|")
        W = float(wl[:-2]) * 1e3
        if not 1e3 <= W <= 1e6:
            continue
        c = cell["m_mean"] / W
        for L in ("H", "C", "B", "G", "DHC"):
            if L not in cell:
                continue
            for label, sname, cal, p in variants2():
                b = bands2(sname, W, "H", d=(cell[L]["density"],) * 2, c=(c, c), cal=cal, persist=p)   # plain unit
                hi = b["N_hi_masked" if filt == "F2" else "N_hi_unmasked"]
                cls = classify2(cell[L]["phi"], b["N_lo"], hi)
                res["cells"].append(dict(cell=key, L=L, set=label, phi=cell[L]["phi"], c=c, lo=b["N_lo"], hi=hi,
                                         cls=cls, registered_cls=classify(cell[L]["phi"], b["N_lo"], hi),
                                         ALN_part=b["ALN_part"] if filt != "F2" else 0.0))
                t = counts.setdefault(label, [0, 0])
                t[0] += cls in ("CRITIC", "MARGINAL-IN")
                t[1] += 1
    res["P5"] = {k: dict(inside=v[0], n=v[1]) for k, v in counts.items()}
    for r, T in list(READINGS.items()) + [("R1u", 80.0)]:
        for L in ("H", "C", "B", "G", "DHC"):
            for masked in (False, True):
                res["gate"][f"{r}|{L}|{'masked' if masked else 'unmasked'}"] = repro_gate(real, L, masked, T, None, r)
    for k, v in res["P5"].items():
        print("P5 own exposure", k, v)
    for k, v in res["gate"].items():
        print("gate", k, v)
    json.dump(res, open(outjson, "w"), indent=1)
    return res


# ------------------------------------------------------------------------------------------------ score / selftest
def score(W, value, reading, unit, masked, exposure=None, d=None, cvc=None, real=None):
    """Scored under PREREG (as registered) and SOURCED; both are printed and returned.  Amendment 2 adds key
    `amend2` (score2: stated exposure and d, symmetric classes, calibration variants, ALN / K labels, gate).  The
    registered rows need a registered reading and unit; for R1u or BP-* only `amend2` is returned."""
    amend = score2(W, value, reading, unit, masked, exposure, d, cvc, real)
    if reading == "R1u" or unit.startswith("BP"):
        print(json.dumps(amend))
        return {"amend2": amend}
    hk = "N_hi_masked" if masked else "N_hi_unmasked"
    D = value if reading in ("R1", "R1b") else (value + 1.0 if reading == "R1x" else value ** 2)
    outs = {"amend2": amend}
    for name in PARAM_SETS:
        use_set(name)
        b = unit_bands(unit, W)
        outs[name] = dict(param_set=name, W=W, reading=reading, unit=unit, D=D, lo=b["N_lo"], hi=b[hk],
                          outcome=classify(D, b["N_lo"], b[hk]))
        print(json.dumps(outs[name]))
    use_set("PREREG")
    print(json.dumps(amend))
    return outs


def selftest():
    import tempfile
    rng = np.random.default_rng(1)
    # 1. exact log-normal vs first-order formula at small sigma
    comps = [(0.1, 1e4)]
    for W in (1e3, 1e5):
        a, b = window_var(W, comps, 10), cv2_first_order(W, comps)
        assert abs(a / b - 1) < 0.05, (W, a, b)
    # 2. Poisson baseline
    n = 200000
    Ds = [disp(rng.poisson(BIN_BP * 0.012 * np.ones(n)), 100)[0] for _ in range(4)]
    assert abs(np.mean(Ds) - 1.0) < 0.05, Ds
    # 3. simulation reproduces the exact expectation (20 Mb, 2 components)
    comps = [(0.2, 5e3), (0.15, 2e5)]
    for W in (1e3, 1e4, 1e5):
        Ds = []
        for _ in range(8):
            R = rate_field(n, comps, rng)
            Ds.append(disp(rng.poisson(BIN_BP * 0.012 * R), int(W / BIN_BP))[0])
        e = expected_sample_D(W, 0.012, comps, n)
        assert abs((np.mean(Ds) - 1) / (e - 1) - 1) < 0.15, (W, np.mean(Ds), e)
    # 4. short-ell component gives a W-independent excess 2 d sigma^2 ell (W >> ell)
    c1 = [(0.2, 200.0)]
    e1, e2 = (band_one(W, 0.012, c1) for W in (1e5, 1e6))
    assert abs(e1 - e2) / e1 < 0.02 and abs(e1 - 2 * 0.012 * math.log1p(0.04) * 200) / e1 < 0.15, (e1, e2)
    # 5. scoring rule and readings
    assert classify(400, 5, 100) == "DAY" and classify(200, 5, 100) == "MARGINAL"
    assert classify(80, 5, 100) == "CRITIC" and classify(2, 5, 100) == "BELOW"
    ds, dp = tree_struct()
    assert 6.0 <= ds <= 12.0, ds
    # 6. split dispersion is ~1 under a shared field, large under H-only blocks
    H, C, _ = sim_two_lineage(n, [(0.2, 1e5)], [], 0.0051, 0.0057, rng)
    k = n // 1000
    h, c = H[: k * 1000].reshape(k, 1000).sum(1), C[: k * 1000].reshape(k, 1000).sum(1)
    assert split_phi(h, c) < 1.3, split_phi(h, c)
    H, C, _ = sim_two_lineage(n, [(0.2, 1e5)], [], 0.0051, 0.0057, rng, blocks=(1e5, 1.0, 0.05))
    h, c = H[: k * 1000].reshape(k, 1000).sum(1), C[: k * 1000].reshape(k, 1000).sum(1)
    assert split_phi(h, c) > 3.0, split_phi(h, c)
    # 7. real-data arm on a tiny synthetic npz in the fm_mesa_replication layout (uniform Poisson -> phi ~ 1)
    sys.path.insert(0, HERE)
    import fm_mesa_replication as fm
    d = tempfile.mkdtemp()
    data = {}
    for ch in ("chr1", "chr2"):
        a = np.zeros((4000, 8, fm.NF), np.uint16)
        a[:, 0, 0] = 1000
        for j, L in enumerate(fm.FIELDS):
            if L in ("H", "C", "B", "G", "DHC", "hh", "gc"):
                lam = {"H": 5.1, "C": 5.7, "B": 5.7, "G": 7.7, "DHC": 13.7, "hh": 1.0, "gc": 400.0}[L]
                a[:, 0, j] = rng.poisson(lam, 4000)
        data["chr_" + ch] = a
    p = os.path.join(d, "t.npz")
    np.savez_compressed(p, **data, meta=json.dumps(dict(fields=fm.FIELDS, bin=1000, sizes={}, blocks=0,
                                                        classes="rep + 2*cpg + 4*dup")))
    r = realdata(p, os.path.join(d, "r.json"))
    for key in ("F0|1kb", "F0|10kb", "F0|100kb"):
        assert 0.7 < r["grid"][key]["H"]["phi"] < 1.4, (key, r["grid"][key]["H"]["phi"])
    # 8. post hoc amendment 2026-10-12: PREREG is the registered set, unchanged; SOURCED differs only in M1, ILS, BGS;
    #    the SOURCED M1 calibration reproduces the Smith 2018 1-Mb CVs (FML-S2); set switching works.
    reg = {"M0": ((0.02, 0.10), (5e6, 2e7)), "M1": ((0.05, 0.20), (5e5, 2e6)), "M2": ((0.05, 0.20), (2e4, 1e5)),
           "M3": ((0.10, 0.40), (2e2, 2e3)), "CPG": ((0.03, 0.15), (5e3, 5e4)), "GBGC": ((0.02, 0.10), (5e4, 1e6)),
           "ILS": ((0.125, 0.25), (1e2, 2e3)), "ALN": ((0.016, 0.42), (1e4, 1e5)),
           "BGS": ((0.006, 0.0625), (2e5, 2e6))}
    assert {k: v[:2] for k, v in PREREG.items()} == reg and COMPONENTS is PREREG and ACTIVE == "PREREG"
    assert sorted(k for k in reg if SOURCED[k][:2] != PREREG[k][:2]) == ["BGS", "ILS", "M1"]
    assert all(SOURCED[k][1] == PREREG[k][1] and SOURCED[k][2] == PREREG[k][2] for k in reg)
    use_set("SOURCED")
    assert COMPONENTS is SOURCED
    lo, hi = mutation_cv(1e6, "lo", True), mutation_cv(1e6, "hi", True)
    assert abs(lo / 0.15 - 1) < 0.05 and abs(hi / 0.27 - 1) < 0.05, (lo, hi)
    assert abs(mutation_cv(1e6, "hi") / hi - 1) < 0.10
    use_set("PREREG")
    assert COMPONENTS is PREREG and abs(mutation_cv(1e6, "hi", True) - 0.232) < 0.005
    selftest2(rng, r)
    print("selftest ok")


def selftest2(rng, real):
    """Amendment 2 pieces (A1-A12).  `real` is the synthetic realdata result of step 7 (uniform Poisson)."""
    # 9. two-locus kernel: closed form == independent first-step derivation; closed-form window average == discrete sum
    for rho in (0.0, 0.5, 5.0, 50.0, 500.0):
        assert abs(hudson_cov_check(rho) - float(hudson_corr(rho))) < 1e-9, rho
    for W in (1e4, 1e6):
        a, b = window_var(W, [(0.05, ("H", 2.6e-3))]), cv2_first_order(W, [(0.05, ("H", 2.6e-3))])
        assert abs(a / b - 1) < 0.08, (W, a, b)
    assert g_hudson(2600.0) * 1e6 / 2 > 2500            # equivalent ell at 1 Mb, N 65k, r 1e-8: ~3.4 kb, above 2 kb
    # 10. two-epoch coalescence: single-epoch limit and the quoted-Delta centre
    e, sd, sig, frac = two_epoch(4.1, 65e3, 45e3, 1e6)
    assert abs(e - 3.25) < 1e-6 and abs(sd - 3.25) < 1e-6 and abs(sig - 3.25 / 7.35) < 1e-9
    e, sd, sig, frac = two_epoch(4.1, 65e3, 45e3, 2.0)
    assert abs(e - 2.71) < 0.01 and abs(sd - 2.38) < 0.01 and abs(sig - 0.35) < 0.005, (e, sd, sig)
    assert 0.35 <= ILS_HI2 <= 0.45 and 0.10 <= BGS_HI2 <= 0.17, (ILS_HI2, BGS_HI2)
    # 11. M0-M1 envelope: feasible for every variant, reproduces both Smith targets, wider than a corner below 1 Mb
    for which in ("lo", "hi"):
        for ds in SMITH:
            for p in (PERSIST if which == "lo" else (1.0,)):       # persistence applies to the lo edge only
                env = m_envelope(which, ds, p)
                assert len(env) >= 2, (which, ds, p)
                oth = cp(AMENDED, which, ("M2", "M3", "CPG"))
                for s0, l0, s1, l1 in env:
                    for W, t in zip((1e6, 1e7), smith_targets(ds, p)):
                        assert abs(cv2_first_order(W, [(s0, l0), (s1, l1)] + oth) / t - 1) < 1e-9
    lo5, hi5 = mutation_cv_env(1e5, "ALL3", 1.0)
    lo6, hi6 = mutation_cv_env(1e6, "ALL3", 1.0)
    assert abs(lo6 - 0.15) < 1e-6 and abs(hi6 - 0.27) < 1e-6 and lo5 < hi5
    assert V_edge("AMENDED", "N_lo", 1e5, "ALL3", 0.5) < V_edge("AMENDED", "N_lo", 1e5, "ALL3", 1.0)
    assert V_edge("AMENDED", "N_hi_masked", 1e6, "NOWONG") < V_edge("AMENDED", "N_hi_masked", 1e6, "ALL3")
    assert V_edge("AMENDED", "N_hi_masked", 1e5, "FRANC") == V_edge("AMENDED", "N_hi_masked", 1e5, "NOWONG")
    # 12. bands2 reproduces the registered bands; stated exposure and d are used; ALN is a separate part
    for name in PARAM_SETS:
        use_set(name)
        for u in ("H", "DHC", "PAIRS-naive", "PAIRS-struct"):
            reg, new = unit_bands(u, 1e5), bands2(name, 1e5, u)
            for e in ("N_lo", "N_hi_masked", "N_hi_unmasked", "K_hi"):
                assert abs(reg[e] / new[e] - 1) < 1e-12, (name, u, e)
    use_set("PREREG")
    full, part = bands2("SOURCED", 1e5, "DHC"), bands2("SOURCED", 1e5, "DHC", d=(0.0137, 0.0137), c=(0.6, 0.6))
    assert abs((part["N_hi_masked"] - 1) / (full["N_hi_masked"] - 1) - 0.6 * 0.0137 / 0.0146) < 1e-9
    assert full["ALN_part"] > 0 and abs(full["N_hi_masked"] + full["ALN_part"] - full["N_hi_unmasked"]) < 1e-9
    # 13. symmetric classes
    assert [classify2(v, 5, 100) for v in (400, 200, 60, 30, 5, 2, 1.2)] == \
        ["DAY", "MARGINAL-OUT", "MARGINAL-IN", "CRITIC", "CRITIC", "BELOW-NEAR", "BELOW-FAR"]
    assert classify2(60, 30, 100) == "MARGINAL-IN" and classify2(40, 30, 100) == "CRITIC"     # narrow band: N_c rules
    # 14. R1u, U-BP and lambda_M formulas against simulation; BP floors
    n = 200000
    sim = simulate_amend(n, 6, rng)
    for W in (10000, 100000):
        for arm in ("R1u", "BP"):
            s = sim[arm][W]
            assert abs((s["sim"] - 1) / (s["exp"] - 1) - 1) < 0.25, (arm, W, s)
        s = sim["phi_HC"][f"lam0.5|{W}"]
        assert abs((s["sim"] - 1) / (s["exp"] - 1) - 1) < 0.25, (W, s)
    assert sim["BP"][10000]["D_struct"] > 15
    f1, f2, f3 = bp_struct()
    assert 55 < f1 < 65 and 95 < f2 < 105 and f3 == 10 * f2, (f1, f2)
    u0, u1 = bands2("SOURCED", 1e5, "DHC"), bands2("SOURCED", 1e5, "DHC", cvc=CVC)
    assert u1["N_lo"] - u0["N_lo"] > 0.5 * 1e5 * 0.0123 * 0.04 * 0.99            # uniform-rate part m CV_c^2
    assert bands2("SOURCED", 1e3, "BP-naive")["N_lo"] > 60
    # 15. phi_HC bound: registered form at lambda_M = 0, rises with lambda_M and with ALN
    b0, b5 = phi_hc_bound("PREREG", 1e5, 0.0, True), phi_hc_bound("PREREG", 1e5, 0.5, True)
    assert 1.0 < b0 < 8.0 and b5 > 2 * b0 and phi_hc_bound("PREREG", 1e5, 0.0, False) > b0, (b0, b5)
    # 16. reproduction gate and score with the stated inputs (synthetic uniform-Poisson realdata: phi ~ 1)
    assert repro_gate(real, "H", False, 80.0, 1e4)["gate"] == "NOT-REPRODUCED"
    assert repro_gate(real, "H", False, 1.0, 1e4)["gate"] == "REPRODUCED"
    assert repro_gate(real, "H", False, 6400.0)["gate"] == "NOT-REPRODUCED"
    assert repro_gate(real, "TREE", False, 80.0, 1e4)["gate"] == "UNTESTED"
    assert repro_gate(real, "H", False, 80.0, 1e9)["gate"] == "UNTESTED"
    assert "D_unnorm_all" in real["grid"]["F0|10kb"]["H"] and real["grid"]["F0|10kb"]["cv_c_ok"] < 0.01
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        o = score(1e5, 80, "R1", "DHC", True, exposure=0.86, d=0.0137, real=real)
        o2 = score(1e5, 80, "R1u", "BP-naive", False, cvc=0.3)
        o3 = score(1e5, 80, "R2", "H", False)
    a2 = o["amend2"]
    assert set(o) == {"amend2", "PREREG", "SOURCED"} and len(a2["variants"]) == 8
    assert a2["gate"]["gate"] == "NOT-REPRODUCED" and a2["verdict_move_allowed"] is False
    assert o["PREREG"]["outcome"] in ("DAY", "MARGINAL", "CRITIC", "BELOW") and COMPONENTS is PREREG
    assert o2["amend2"]["gate"]["gate"].startswith("UNGATED") and o3["amend2"]["verdict_move_allowed"] is False
    assert o3["amend2"]["D"] == 6400.0
    # 17. code paths of the amendment tables and of `post` (one window size, output discarded: no table is read here)
    import tempfile
    global WGRID
    keep, WGRID = WGRID, (1e4,)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            am = analytic_amend()
            td = tempfile.mkdtemp()
            json.dump(real, open(os.path.join(td, "real.json"), "w"))
            po = post(os.path.join(td, "real.json"), os.path.join(td, "post.json"))
    finally:
        WGRID = keep
    json.dumps(am)
    assert len(am["table"]) == 8 * 9 and "AMENDED|FRANC|persist0.5|BP-struct|10000" in am["classes"]
    assert set(po["P5"]) == {v[0] for v in variants2()} and po["gate"]["R2|DHC|masked"]["gate"] == "NOT-REPRODUCED"


def band_one(W, d, comps):
    return W * d * window_var(W, comps)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "selftest":
        selftest()
    elif a[0] == "analytic":
        analytic(a[1], a[2] if len(a) > 2 else None)
    elif a[0] == "simulate":
        simulate(a[1], *(float(x) if i == 0 else int(x) for i, x in enumerate(a[2:])))
    elif a[0] == "realdata":
        realdata(a[1], a[2])
    elif a[0] == "score":
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("--W", type=float, required=True)
        ap.add_argument("--value", type=float, required=True)
        ap.add_argument("--reading", default="R1", choices=("R1", "R1b", "R1x", "R2", "R1u"))
        ap.add_argument("--unit", default="DHC")
        ap.add_argument("--masked", action="store_true")
        ap.add_argument("--exposure", type=float)      # amendment 2 (A3): aligned bp per window / W
        ap.add_argument("--d", type=float)             # amendment 2 (A3): divergence per aligned site
        ap.add_argument("--cvc", type=float)           # amendment 2 (A8): CV of exposure across windows (R1u)
        ap.add_argument("--real")                      # amendment 2 (A7): realdata output for the reproduction gate
        o = ap.parse_args(a[1:])
        score(o.W, o.value, o.reading, o.unit, o.masked, o.exposure, o.d, o.cvc, o.real)
    elif a[0] == "post":
        post(a[1], a[2])
    else:
        sys.exit(__doc__)
