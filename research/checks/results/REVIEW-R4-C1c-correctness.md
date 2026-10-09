# Correctness review: R4 C1c (call-depth + ancestry-replacement model of Day's binned "21")

Reviewer: correctness pass, 2026-10-09. Files read: `results/R4-C1c.md`, `c1c_call_depth_replacement.py` (unchanged since pre-registration b128110; `git diff b128110 HEAD` is empty for the script and the depth table), `c1c_posthoc_mindepth.py`, `c1c_posthoc_variant_gate.py`, `results/c1c_depth_table.json`, `results/raw/c1c_*`, context (`c1b_day_binned_statistic.py`, `c1_ascertainment_sim.py`, REVIEW.md/RESULTS.md C1b entries, claims C6 and C1a), and Day's text (`sources/raw/day/zenodo-18525185.txt`, s3.2-s4.4). The AADR anno was read as text only, through `research/.venv/bin/python -I`, with scratch scripts in the session scratchpad (`depth_check.py`, `dens.py`, `analytic.py`, `srcne.py`, `f0.py`, `repro.py`, `kmod.py`, `old.py`).

**Verdict: no BLOCKER.** I found no code bug in the Wright-Fisher, pulse, sampling or statistic code. The headline base-grid numbers (S21 against Ne, the 0/44 gate) reproduce. Two MAJOR findings concern conclusions drawn from the sampling-heterogeneity variants and the profile mismatch. Both need correction in the fix pass. The rest are MINOR.

## What I verified (all reproduce)
- `selftest` passes. `analyse` on the committed raw files regenerates `raw/c1c_analysis.txt` byte-identically.
- **Depth table.** An independent re-parse of the anno gives the same 8,808 European individuals and the same per-bin counts, and zero rows dropped for missing hits. In the anno, `.DG` rows are the "Shotgun.diploid" data type and everything else in this file is pseudo-haploid. There are no `.HO` rows in the 1240k file, so the `.HO` branch in `build_depth` is dead code. This is harmless.
- **WF drift and pulse math.** Drift is exact binomial on 2Ne chromosomes (the selftest also checks variance). The pulse step `x=(1-m)x+m*y` is the correct frequency-level admixture, and `pulse_fractions` / `ancestry_shares` give the stated R1-R3 end shares (R2: W .124, A .496, S .38). Control run: with pre-window Fst ~0.004 and no post-window source drift, R2 and R3 at Ne 1e6 give S21 = 2-4 and 7-10 (R0: 3.6). The replacement effect therefore vanishes when the sources are identical, so the pulse code is not creating events by itself.
- **Fst calibration.** The panel gives realised Hudson Fst of 0.0858 / 0.0667 / 0.0488, as stated. Branch lengths of 2200 / 1400 / 600 generations at Ne 1e4 give those values by the usual F/2 sums.
- **Panel density.** Drifted W/A/S sources keep a flat folded density of 1.79-1.95 per unit q down to q = 1e-3, as claimed. 10.5% / 6.8% / 3.0% of sites are absorbed in W / A / S.
- **Independent replicate** (rep 77, new seeds, scratch):

  | Cell | S21 (2 draws) |
  |---|---|
  | R0 Ne 1e5 | 22 and 33 (R4 mean 31.8) |
  | R0 Ne 1e6 | 2 and 6 (R4 3.6) |
  | R2 Ne 1e6 | 28 and 19 (R4 25.8) |

  The k2, k0.5 and eps variants also reproduce (R0 Ne 1e5: k2 416/434, k0.5 16.1k, eps 66/60).
- **Analytic limit.** At Ne -> infinity with no replacement, a site with minor-allele frequency q gives an eligible event with probability (1-q)^1039 x [1-(1-q)^522], and an S21 event if additionally bins 0-3 are all polymorphic. Integrating with 2 x 1,063,614 sites per unit q and the table's mean chromosome counts gives eligible = 683, S21 = 2.1, and bin 0-3 profile 632 / 44 / 3.1 / 1.7. The simulation at Ne 1e6 gives 702, 3.6 and 640 / 52 / 2.6 / 2.8. The statistic code agrees with the closed form.
- **Scorecard.** The P1-P8 text in R4 matches the b128110 docstring, and the outcome labels (held / partly / failed / refuted) agree with the raw numbers. Details in finding 8.

## Findings

### 1. MAJOR: the capture-heterogeneity (kappa) variants apply an independent Gamma multiplier to the modern bin, which is 82% high-coverage shotgun diploid; this alone produces the "strongest upward lever" result
- **Code.** `sample_bins` draws `w_mod = rng.gamma(kappa, 1/kappa, size=S)` for bin 10 (0-500 BP) and applies `min(1, p_dip*w_mod)` to 513 diploid `.DG` individuals (`n_dip` = 513 of 625, p_dip = 0.967 in the depth table). Site-level "capture efficiency" is a property of enrichment captures. Shotgun diploid genomes (1000G/SGDP-type) cover the 1240k sites nearly uniformly.
- **Effect.** A site with a low `w_mod` has only a handful of modern calls, so the allele is trivially "100% modern". Because T2 dates an event at the oldest 100% bin, these sites are dated 0-500 BP.
- **Test (scratch `kmod.py`, same panel and same simulated allele frequencies, heterogeneity switched on only for the ancient bins).** "mod het" below means Gamma heterogeneity also applied to the modern bin, as in the main run.

| Cell | variant | eligible | tracked | S21 | events dated 0-500 BP |
|---|---|---|---|---|---|
| R0 Ne 1e5 | homogeneous | 1,714 | 1.00 | 34 | 7 |
| R0 Ne 1e5 | kappa 1, mod het (as in R4) | 9,072 | 0.99 | 4,047 | 3,902 |
| R0 Ne 1e5 | kappa 1, ancient only | 1,377 | 1.00 | 52 | 12 |
| R0 Ne 1e5 | kappa 0.5, mod het | 27,315 | 0.95 | 16,151 | 15,938 |
| R0 Ne 1e5 | kappa 0.5, ancient only | 1,112 | 0.99 | 48 | 19 |
| R2 Ne 1e6 | kappa 1, mod het | 7,328 | 0.99 | 3,581 | 3,418 |
| R2 Ne 1e6 | kappa 1, ancient only | 441 | 1.00 | 25 | 6 |

  So 95-99% of the "inflation" sits in the 0-500 BP bin, where Day has 2 events.
- **Post hoc min-depth analysis.** The same signature is in `raw/c1c_posthoc_mindepth.json`, which R4 did not examine. For kappa 1.0 at m = 20, `profile_trk` puts 981 of 1,064 S21 events (R0 Ne 1e5) and 749 of 843 (R2 Ne 1e6) in the 0-500 BP bin. With heterogeneity on the ancient bins only, kappa 0.5 and m = 20 gives tracked 0.87, S21 47 and eligible 1,095. That is nowhere near Day's tracked 0.727, but S21 is not in the thousands either.
- **What this overturns in R4.**
  - s3: "Capture heterogeneity is the strongest upward lever on S21 ... kappa 0.5 gives 15,000-20,000 at every Ne".
  - s3: "Day's tracked fraction can therefore be reproduced, but only with S21 in the thousands".
  - s4 P7 ("S21 changes ~500x").
  - The "Two systematic errors in my priors" paragraph ("depth heterogeneity ... is the largest lever of all").
  - s5 "Deficit" bullet ("capture heterogeneity kappa <= 2").
- **What survives.** Ancient-bin heterogeneity does raise S21 modestly (x1.4-1.5 here, one rep) and lowers the tracked fraction. These are the physically motivated effects.
- **Fix.**
  - Set `w_mod = 1` for the diploid share, or at most use a separate small kappa.
  - Rerun the variants and the post hoc min-depth script, report the bin-10 count for every variant, and drop or rewrite the statements above.
  - The design flaw is in the pre-registered script (P7 included the modern bin), so label the rerun as post hoc and say so.

### 2. MAJOR: the "unexplained" profile mismatch has a checkable contributor in the anno that R4 does not mention: the 10000+ bin is mostly Upper Palaeolithic, not 10,500 BP Mesolithic
- **Placement.** The model places the whole bin at 10,500 BP as the ancestral W population (`BINS`, `START_BP`; "assumed" in the docstring and caveats).
- **Dates in the anno.** The 167 European individuals in that bin have median date 15,572 BP and quartiles 10,835 / 29,458 BP. 97 are older than 14,000 BP, 72 older than 20,000 BP, and the maximum is 50,000 BP. Only 44 are younger than 11,000 BP.
- **Consequence.** The bin has the lowest depth (49 chromosomes per site) and is by construction the bin T2 prefers. In every simulated cell it is the dominant bin (94% of events in R0 Ne 1e5, R2 Ne 1e6 with eps 1e-3). Day's bin has 18.6% of events and 8000-10000 BP has 53.6%. A bin that is mostly 15-50 kBP individuals, structurally distinct from the later European populations, would be polymorphic at many sites where the model's W-like bin is 100%, and this cuts directly into the 10000+ count.
- **No bug.** The analytic profile above (632 / 44 / 3.1) matches the code, so the dominance of bin 0 is a depth effect plus this misspecification, not a dating error. For a stationary rare allele, T2 shares are P0 : (1-P0)P1 : ... with P_b = (1-q)^c_b and c = 49, 62, 282. Day's shares need P0 ~ 0.19, which the model's own depths cannot give.
- **Why it matters.** R4 uses the profile (TV 0.56-0.76) as a validity criterion that all cells, including the eps passers, fail. If the 10000+ bin is misplaced, TV is not a clean test of the demographic or error model.
- **Fix.** State the median date and spread of the 10000+ bin in R4. Either rerun with the 10000+ bin treated as a separate, deeper-diverged source, or drop it and compare profiles on bins 1-10 only (renormalised). Rephrase "unexplained" as "partly attributable to the 10000+ bin's age composition, not tested".

### 3. MINOR: the flat-to-q->0 density drives the eligible leg of the gate and the pre-7000 share much more than it drives S21; R4 does not say which leg is robust
- **Analytic check.** Scale the panel density by (q/0.01)^t at Ne -> infinity. t = -0.5 gives eligible x3.1 and S21 x1.7; t = +0.5 gives eligible x0.38 and S21 x0.62. Half of the eligible events come from q < 0.0013 and half of S21 from q < 0.0038.
- **Consequence.** The "eligible 13-40x short" gate failure for S21 ~ 21 cells is therefore assumption-dependent (mild tilts move it 3x), whereas the S21 map against Ne is comparatively robust.
- **Density-independent diagnostic.** A uniform change in density cancels in the eligible/S21 ratio. Day's ratio is 22,428 / 21 ~ 1,070. The model's is 50-200 (R0 Ne 1e5: 52; Ne 1e6: 195). The eps cells give 770 only because most eligible events become error events.
- **Fix.** Add a sentence to the s8 caveat on the low-q density and the ratio argument. The R4 comment that "a panel richer in rare variants would raise [eligible]" is right but omits that S21 is much less sensitive.

### 4. MINOR: Fst x0.5 / x2 does not bound the replacement lever
- **What R4 says.** "Fst x0.5 or x2: S21 changes <1.5x".
- **What the numbers show.** The replacement effect at high Ne is saturated and non-monotonic in Fst: R2 Ne 1e6 gives S21 32 / 26 / 22 and eligible 683 / 540 / 436 for Fst x0.5 / x1 / x2.
- **Control run** (scratch `f0.py`; pre-window Fst ~0.004, so essentially zero):

| Source Ne after 10,500 BP | R2 Ne 1e6 S21 | eligible | R3 Ne 1e6 S21 |
|---|---|---|---|
| none (1e8) | 2-4 | ~585 | 7-10 |
| 1e4 | 20-26 | 1,166-1,222 | 49-54 |

  Source Ne 1e5 or none at Fst x1 gave 13-21 (`srcne.py`).
- **Interpretation.** Roughly 0.01 of post-window divergence is enough. Rare alleles (q ~ 1e-3) in a 1e4 source diverge by far more, in relative terms, than common-allele Fst suggests. The replacement lever is therefore set by the assumed source Ne / rare-allele differentiation (a star tree with no mutation), not by the Fst that was calibrated. The Fst sensitivity test is not evidence of robustness.
- **Fix.** Report the saturation and state that the lever depends on source Ne and rare-allele differentiation, which are unconstrained. P4's "refuted" stands, but the explanation is open.
- **Calibration caveat.** Fst was calibrated at 10,500 BP, whereas A and S drift further to their pulse dates (+50 to +275 generations at Ne 1e4, F ~ +0.003 to +0.014). The "assumed, recollection" label is present.

### 5. MINOR: the T1-versus-T2 choice can be argued deductively, and "tracked" is defined more strictly than Day's wording
- **T1 cannot be Day's rule.** Under any eligibility rule (E1: pooled 6000-8000 BP polymorphic; E2: some older bin polymorphic), the start of the unbroken terminal 100% run cannot be in bins 0-2 (E1) or in bin 0 (E2). Day reports 3,038 events in bin 0 (impossible under T1 for any eligibility rule), and under E1 also 8,741 + 4,497 in bins 1-2. Only a "gaps allowed / oldest 100% bin" reading such as T2 can produce his table.
- **Why this matters.** The R4 phrase "T2 is the only reading with a profile resembling Day's" is correct, and a stronger statement than the empirical one. "Working backward from the present" taken literally is T1, which is impossible. Say so.
- **Tracked definition.** Day: "insufficient coverage in intermediate time bins". The script requires calls in all 11 bins, including bins older than the event date. For S21 events (T2 >= 4) this adds a requirement on the sparse old bins that Day's wording does not obviously impose. It is a reading, flagged as such ("threshold unstated"), but the min-depth analysis inherits it.

### 6. MINOR: AADR parsing and sample match
- **Release.** The file is `v62.0.p1_1240k_public.anno`. `p1` is the June 2026 patch (the Dataverse JSON in the same directory lists V62.0.p1 as the June 2026 patch and V62.0 as the Sept 2024 original); Day cites v62.0. R4 says "v62.0 anno".
- **Filter.** The lat/lon box and the exclusion list (including all of Russia, all of Turkey) were chosen to reproduce Day's per-bin counts, so the close match (8,808 vs 8,738) is partly tuned. The oldest bin matches (167 / 168). The 0-500 BP bin does not: 524 anno individuals against Day's 625 (-16%). `build_depth` rescales n_ph and n_dip by 625/524, which silently invents 101 individuals with the observed ph/dip mix. The effect on chromosomes per site is small but nonzero (pseudo-haploid 94 to 112; chromosomes 1,039 vs ~870 unscaled).
- **Date handling.** Dates are the anno's "Date mean in BP", with a mean-date bin assignment. The within-bin date spread (e.g. 7000-8000 BP) is not modelled; every individual sits at the bin midpoint.
- **Hit-per-site assumption.** p = hits / 1,150,639 per individual, correct for the autosomal 1240k count. The model panel is 1,143,671 x 0.93 sites (Day's Z23046531 autosomal SNP count, a 0.6% mismatch of no consequence). The per-site call count is Binomial(n, mean p), whereas the true count is Poisson-binomial with very heterogeneous p_i. In the 10000+ bin the per-individual hit rate has median 186k against a mean of 332k, and the 10th percentile is 10.8k. This makes the per-site variance somewhat too large, as R4 notes. It does not change the mean.

### 7. MINOR: replicates and seeds
- **Seeds.** `SeedSequence([ROOT, rep, stream, ...])` gives distinct, reproducible streams. Scenarios in one rep share a panel and source trajectories (common random numbers), which is good for comparisons. One fragility: the scenario RNG is keyed on the scenario's index in the (optionally filtered) list, so `run ... only` produces different draws from the full run. That is not a problem for the committed runs.
- **Replicate spread.** Per-rep means of S21 (2 draws averaged):

| Cell | per-rep means | mean | SD across reps | Poisson SD |
|---|---|---|---|---|
| R0 Ne 1e5 | 24.5 / 33.5 / 35.5 / 33.5 | 31.8 | 4.9 | 5.6 |
| R2 Ne 1e6 | 25.5 / 27.5 / 28.0 / 22.0 | 25.8 | 2.7 | 5.1 |
| R0 Ne 3e5 | | 7.9 | 1.8 | |

- **Verdict on 4 replicates.**
  - Enough for the factor-of-2 to factor-of-10 statements in R4 (R0/R2 ratio, Ne* of order 1e5, the 70-190x gap at Ne 1e4).
  - Not enough for tight point statements such as "Ne* = 1.4e5" (SE ~ 8-10% on S21, so ~10-15% on Ne*) or the borderline "consistent / deficit" calls at 1.2x-1.9x.
  - The two sampling draws per rep share one allele-frequency realisation, so the effective replicate count is 4 independent trajectories (the `[min,max]` column has 8 samples).
  - The Poisson `pL(21)` column in `c1c_analysis.txt` is not meaningful, because per-site independence understates real variance (linkage), as the caveat says.
  - The post hoc min-depth results are 1 rep x 1 draw. The counts are large (>800), so they are stable, but see finding 1 for their content.

### 8. MINOR: scorecard and wording
- **Pre-registration state.** The script and depth table are unchanged since b128110, and the docstring predictions P1-P8 match what R4 quotes. The post hoc scripts are separate, labelled commits (ee0b725, 9045329), and R4 says "Post hoc:" for the min-depth results.
- **Unlabelled post hoc criteria.** In s3, the variant gate table (eligible / pre-7000 / S21 / PASS) and the "fail the profile and start table" language are post hoc: `c1c_analysis.txt` Table 3 gated only the base variant, and the profile/start-table failure criteria have no pre-registered thresholds. Label them. Under a literal reading of P3's falsifier ("any cell passes all three"), the eps passers falsify P3. R4's "held for the base grid, refuted when an error rate is added" is the honest framing and should be kept.
- **Numerical slips in R4.**
  - "kappa 2 multiplies S21 by 14-16x at Ne 1e5-1e6": R0 Ne 1e5 is 14x and R2 Ne 1e6 is 16x, but R2 Ne 1e5 is 5.1x (516 / 102).
  - "profile TV 0.56-0.76": the table minimum is 0.57.
  - "Steppe bump 1.0-1.5x": from Table 8 the 4000-6000 BP share of R3 over R0 at Ne 1e6 is 0.33/0.20 = 1.65 (R0 has only 6 events), and R2/R0 at Ne 1e5 is 0.96. A fairer range is 0.96-1.65, noisy.
  - "Replacement lowered eligible": true for R1/R2 at all Ne, false for R3 at Ne >= 1e5 (1,983 vs 1,659; 1,132 vs 702).
- **P5 is tautological.** The d = 0.45 scenario is implemented as Ne/d, so "behaves like neutral at Ne/0.45" is true by construction. It is not a test of any model; say so rather than "held".
- **s6 conclusion is too broad.** "At Holocene Ne >= ~1e5 it is [what neutral predicts]" holds for R0/R1 only. Under R2 (the "literature-central" level) the neutral expectation is 102 at Ne 1e5 (4.9x) and needs ~3e5-1e6 to reach 39-26. Both the statement and the matching "Critics" bullet should carry the replacement qualifier.
- **"Refuted" overstates one result.** The header says the "handful of calls" hypothesis is refuted. What is refuted is the mean depth (49 / 62 / 282 chromosomes per site). Per-site structure in real AADR data (probe subsets, damage filtering, transversion-only sets) is untested, and finding 1 shows it can matter.

### 9. NIT
- The pulse update `(1-m)*x + m*y` is not clipped to [0, 1]. It ran without error, but `numpy.binomial` rejects p > 1, so this is fragile for other parameters.
- `xb` is stored as float32. This is fine to ~6e-8.
- The 0-500 BP bin is recorded at step 512 (250 BP, round-half-even of 512.5), so "modern" is 250 BP, not 0. Immaterial.

## Answers to the specific questions
- **Frequency-level drift, pulse admixture, Fst calibration.** Correct as implemented. The calibration is an assumption (labelled). It is not a lever for the replacement effect (finding 4).
- **q->0 density.** Reproduced as stated and flat; the dependence of the eligible count on it is real (finding 3).
- **AADR parsing.** Correct and reproducible. Minor issues in finding 6. Pseudo-haploid and diploid counts are sound, with `.HO` dead.
- **E1/T2 faithful?** It is a defensible reconstruction and the only one logically able to produce Day's table (finding 5). S21 is computed as Day's "0-6000 BP: 21" (bins 5000-6000 BP and younger; the table sums to 21 for those seven bins).
- **Gate and profile.** The gate is implemented as pre-registered. Profile TV and the start-frequency table are descriptive and have no pre-registered thresholds (finding 8). The profile is compromised by the 10000+ bin (finding 2).
- **Scorecard.** Faithful to the docstring, with the labelling and numerical slips in finding 8.
- **Replicates.** Adequate for order-of-magnitude claims, not point estimates (finding 7).
- **Missing 8000-10000 BP dominance.** Not a bug. Analytic and simulation agree (finding 2). It reflects depth structure plus the misplaced 10000+ bin, and probably real structure; neither is tested.

## Items to carry into the fix pass
1. Rerun the kappa variants and the post hoc min-depth analysis with a uniform modern bin (finding 1) and report bin-10 counts. This is the only item that can change a headline statement.
2. Describe the 10000+ bin's age composition and re-assess the profile criterion (finding 2).
3. Add the S21-versus-eligible density-robustness remark and the eligible/S21 ratio (finding 3).
4. Reword the Fst-robustness sentence (finding 4).
5. Fix the numerical and wording slips and label the post hoc gate/profile criteria (finding 8).
