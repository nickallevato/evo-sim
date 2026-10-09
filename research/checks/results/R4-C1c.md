# R4 C1c: Day's "21" with real AADR call depth and an ancestry-replacement model

Script: `research/checks/c1c_call_depth_replacement.py` (pre-registered in commit b128110, docstring P1-P8, before the main run). Depth table: `results/c1c_depth_table.json`. Raw: `results/raw/c1c_rep0..3.json`, formatted tables `results/raw/c1c_analysis.txt`. Post hoc scripts (separate commits, labelled): `c1c_posthoc_mindepth.py`, `c1c_posthoc_variant_gate.py`. Figure: `results/R4-C1c-S21-vs-Ne.png`.
Run: 4 replicates x 2 sampling draws x 44 scenarios on 1,063,614 panel sites, all on this workstation (`nice -n 19`, 4 processes). I started 4 more replicates on na-workhorse, but its load was ~16 on 12 cores and none had finished its first scenario after 31 min, so I stopped them (my own PIDs only). Four replicates are enough: the spread between runs is small next to the effects (see "min,max" in `c1c_analysis.txt`).

## 1. What was built
1. **Real call depth.** The public AADR v62.0 `.anno` (Harvard Dataverse file 13994492, sha256 1935ecee...; downloaded to `sources/raw/aadr-anno-2026-10-09/`, parsed as text only) gives each individual's "SNPs hit on autosomal targets (1240k)". Per bin I derived n pseudo-haploid, n diploid (`.DG`/`.HO`) and mean hit probability, and drew called individuals per site as Binomial(n, p x w_site). Day's sample is almost reproduced from the file: with a European lat/long box minus Turkey/Armenia/Syria/Georgia/Iraq/N. Africa/Russia, the anno has 167/133/669/579/726/1155/1015/1000/2125/715/524 individuals per bin against Day's 168/129/668/573/721/1141/980/952/2093/688/625 (8,808 vs 8,738).
2. **Ancestry replacement.** Frequency-level exact Wright-Fisher: a pooled European population EU starts as Mesolithic (W) at 10,500 BP and receives 10 Anatolian-farmer pulses (9,500-7,250 BP) and 6 steppe pulses (5,000-4,500 BP). Sources W, A, S are drifted from a common ancestor (pairwise Hudson Fst 0.086/0.067/0.049, assumed). Replacement levels: R0 none, R1 modern shares W .32/A .48/S .20, R2 .12/.50/.38 (literature-central), R3 .05/.41/.55.
3. Day's statistic as in C1b (E1 or E2 eligibility, T1 or T2 dating, tracked = data in all 11 bins). Headline model number S21 = tracked E1-T2 events dated 5000-6000 BP or younger.

**The "handful of calls" hypothesis from review #4 is refuted at the real depth.** Chromosomes called per site in the three oldest bins are about 49 / 62 / 282 (not a handful), and 240-1,100 in the younger bins and ~1,040 in the modern bin. The reviewer's 1-replicate test used coverage 0.01-0.03 (2-6 calls), which is 10-25 times below the anno.

## 2. What the 21 maps to (E1-T2, tracked; mean of runs)
S21 by constant window Ne (Day: 21; eligible Day: 22,428):

| Model | 1e4 | 2e4 | 5e4 | 1e5 | 3e5 | 1e6 | Ne where S21 = 21 |
|---|---|---|---|---|---|---|---|
| R0 closed | 3,925 | 908 | 120 | 32 | 8 | 3.6 | **~1.4e5** |
| R1 mild replacement | 1,488 | 396 | 66 | 20 | 7 | 3 | ~1.0e5 |
| R2 literature-central | 2,259 | 853 | 238 | 102 | 39 | 26 | >1e6 (still 26 at 1e6) |
| R3 strong replacement | 3,020 | 1,524 | 634 | 369 | 199 | 140 | >1e6 (still 140 at 1e6) |
| Eligible, R0 | 15.2k | 7.3k | 2.9k | 1.7k | 0.94k | 0.70k | |
| Eligible, R2 | 8.2k | 4.1k | 1.8k | 1.1k | 0.68k | 0.54k | |

- **Textbook Ne = 1e4:** neutral expectation 1.5k-3.9k, i.e. the 21 is 70-190 times below it (R1-R3 and R0). Calls depth and replacement do not close this gap.
- **Growth** 1e4 to 1e5 across the window: S21 262 (R0), 276 (R2). Growth 1e4 to 1e6: 35 (R0, 1.7x the 21), 15 (R1), 67 (R2), 220 (R3).
- **Day's d = 0.45:** R0 Ne 1e4 gives 739 (35x the 21); Ne 2e4 gives 157 (7.5x). It matches neutral at Ne/0.45 (neutral 2.2e4 would give ~720). Day's d maps to the 21 only for a closed population at Ne ~6e4. The "stasis" reading (zero frequency movement) is not a simulable model.
- **Reading T1** (start of the terminal 100% run) puts 500-13,000 events in the post-5000 BP bins in every scenario, plus 150-850 in 0-500 BP (Day: 2). T2 is the only reading with a profile resembling Day's.
- Gen time 25 y instead of 20 y: S21 2.5k (R0, Ne 1e4) and 73 (R2, Ne 1e5), about 0.6-0.7x. Fst x0.5 or x2: S21 changes by <1.5x (R2, Ne 1e6: 32 and 22).

## 3. Does the model reproduce Day's own table? (the validity gate)
No cell does. Gate (pre-registered P3): eligible within 3x of 22,428, pre-7000 share >= 0.90, S21 in [7, 63]. **0 of 44 base cells pass.**
- Closed populations at Ne 1e4 give eligible 15k (within 3x) but S21 3.9k and a pre-7000 share of 0.69. High-Ne cells with S21 near 21 give eligible only 0.5k-1.7k (13-40x short).
- **Profile:** total-variation distance from Day's 11-bin profile is 0.56-0.76 in every cell. The model puts old-bin events in the 10000+ bin (e.g. R0 Ne 1e5: 1,398 / 199 / 13 for 10000+ / 8000-10000 / 7000-8000) while Day has 3,038 / 8,741 / 4,497. Nothing in this model produces Day's dominance of the 8000-10000 and 7000-8000 bins.
- **Start frequencies of the fixed allele in the Neolithic** (Day: 79.2/20.2/0.5/0.2%): Ne 1e4 gives 61/38/0.7/0; Ne >= 1e5 gives 94-99.8% in [99,100). Day's split lies between them.
- **Tracked fraction** is 1.00 with homogeneous capture; Day's is 0.727.
- Post-7000 distribution: Day has 2 / 16 / 5 events in 6000-7000 / 4000-6000 / younger. R2 at Ne 1e6 gives 42% / 30% / 28%; no steppe bump comparable to Day's 4000-6000 cluster.

### Sampling variants (kappa = capture heterogeneity, eps = false minor-call rate)
| Cell | variant | eligible | tracked | pre-7000 | S21 | gate |
|---|---|---|---|---|---|---|
| R0 Ne 1e5 | base | 1,659 | 1.00 | 0.970 | 32 | e- p+ s+ |
| R0 Ne 1e5 | kappa 2 | 3,127 | 1.00 | 0.843 | 452 | fails |
| R0 Ne 1e5 | kappa 0.5 | 27,286 | 0.95 | 0.373 | 16,213 | e+ p- s- |
| R0 Ne 1e5 | eps 1e-3 | 45,340 | 1.00 | 0.997 | 59 | **PASS** |
| R2 Ne 1e6 | base | 540 | 1.00 | 0.917 | 26 | e- p+ s+ |
| R2 Ne 1e6 | eps 1e-3 | 10,233 | 1.00 | 0.993 | 37 | **PASS** |
| R2 Ne 1e5 | eps 1e-3 | 11,066 | 1.00 | 0.981 | 139 | e+ p+ s- |
| R0 Ne 1e4 | eps 1e-3 | 61,353 | 1.00 | 0.917 | 4,217 | e+ p+ s- |

- **Capture heterogeneity is the strongest upward lever on S21.** Sites with few calls in one bin are trivially "100%". kappa = 2 multiplies S21 by 14-16x at Ne 1e5-1e6; kappa = 0.5 gives 15,000-20,000 at every Ne. Post hoc: requiring >= m called chromosomes per bin to count as observed, kappa 0.5 with m = 20 gives tracked 0.73-0.75 (Day 0.727), eligible 14.5k (Ne 1e4) or 5.8k (Ne 1e5) and S21 5.0k or 1.7k. kappa 1 with m = 20 gives tracked 0.78-0.80 and S21 4.8k / 1.06k / 0.84k (R0 Ne 1e4 / R0 Ne 1e5 / R2 Ne 1e6). Day's tracked fraction can therefore be reproduced, but only with S21 in the thousands.
- **A 0.1% false-minor-call rate** inflates eligible 4-27x and pushes the pre-7000 share to 0.98-0.997, as in Day's table (0.9986), while S21 stays within about 2x of the 21 at Ne >= 1e5 (R0 59, R2 Ne 1e6 37). Those two cells pass the three-number gate but still fail the profile (TV 0.75; 94% of events in the 10000+ bin) and the start-frequency table (99.8% vs 79.2% in [99,100)). The 1e-3 value is an assumption, not a measured AADR error rate.

## 4. Pre-registered predictions: what held
| P | Prediction | Result |
|---|---|---|
| P1 | Real depth alone does not give 21; R0 Ne 1e4 S21 in [300, 10,000] | **Held.** 3,925. The depth "handful" cause is refuted. |
| P2 | S21 falls monotonically with Ne; R0 Ne* in [3e4, 1e6]; R2 Ne* within 3x of R0 | **Partly held.** Monotone; R0 Ne* = 1.4e5; R1 1.0e5. **Failed for R2/R3:** their S21 never reaches 21 by Ne 1e6. |
| P3 | No (R, Ne) cell passes eligible + pre-7000 + S21 | **Held for the base grid (0/44), refuted when an error rate is added:** R0 Ne 1e5 and R2 Ne 1e6 at eps 1e-3 pass the three numbers (but not the profile or start table). |
| P4 | Replacement is second order for S21 (<2x), raises eligible >= 1.3x and pre-7000 share +10 pp, steppe bump >= 1.5x | **Refuted.** R2/R0 S21 = 0.6 at Ne 1e4, 3.2x at 1e5, 7x at 1e6; R3 up to 40x. Replacement lowered eligible (8.2k vs 15.2k at Ne 1e4) and the pre-7000 share. Steppe bump 1.0-1.5x, not reproduced. |
| P5 | Day's d = 0.45 acts as neutral at Ne/0.45; S21 >= 5x the 21 at Ne 1e4 | **Held** (739; neutral at 2.2e4 ~720). |
| P6 | eps 1e-3 raises S21 >= 3x at R2 Ne 1e6 | **Failed.** 1.4x (37 vs 26); 1.85x for R0 Ne 1e5. Its big effect is on eligible and the pre-7000 share. |
| P7 | kappa 0.5 gives tracked 55-90%, S21 changes <2x | **Failed.** Tracked 0.95; S21 up 5x at Ne 1e4 and ~500x at Ne >= 1e5. |
| P8 | 21 is reached only if Holocene Ne >= ~5e4; at Ne <= 2e4 neutral predicts hundreds to thousands | **Held for closed populations** (Ne* 1.0-1.4e5; 908 at Ne 2e4); **wrong for strong replacement**, where the floor stays 26-140 even at Ne 1e6. |

Two systematic errors in my priors: I expected replacement to be a minor lever and it is a large one at high Ne (it adds frequency movement that lets alleles visible in the old bins vanish); I expected depth heterogeneity to be minor and it is the largest lever of all. Mechanisms are hypotheses; I did not run an attribution test.

## 5. Which assumptions flip the conclusion
"Conclusion" = whether the observed 21 is far below the model expectation (deficit), consistent with it (within about 3x), or above it.
- **Deficit (S21 model >= ~60 = 3x):** textbook Holocene Ne <= ~5e4 in any model; any replacement level R2-R3 at Ne up to 1e6; reading T1; Day's d = 0.45 at Ne <= 2e4; capture heterogeneity kappa <= 2; sampling error eps = 1e-3 at R2 Ne <= 1e5.
- **Consistent:** closed or mildly replaced population (R0, R1) with Ne ~1e5-3e5 (S21 8-32), or R2 at Ne >= 3e5 (39 at 3e5, 26 at 1e6), homogeneous capture and no assay error.
- **Excess (model below 21):** R0/R1 at Ne >= 3e5 (S21 3-8). In these cells the observed 21 is above the neutral expectation, but those cells also have eligible 0.3-0.9k, 25-70x below Day's 22,428, so they do not describe his data.
- The most consequential single input is the Holocene Ne. It is the C4/C5 dispute: keruru's temporal Ne 8,139-9,835 (C5b) puts the 21 in the deficit class, 190x below the neutral expectation. A Holocene Ne of ~1e5 or more is needed for it to be consistent, and the same data then fail Day's eligible count and profile.

## 6. Verdict and suggested edits (not applied; claim files untouched)
- C6 external: keep "untestable / not reproducible", but sharpen. The model is still not a valid null for Day's table (0/44 gate; profile TV >= 0.56; tracked fraction; eps variants pass only the three summary numbers). Conditional readings: at Ne = 1e4 and real depth, neutral expectation is 1.5k-3.9k, so the 21 is not "what neutral predicts"; at Holocene Ne >= ~1e5 it is. Neither "neutral predicts ~0" nor "deficit vs neutral" is supported without fixing Ne.
- The review #4 sentence "likely cause: per-site call depth (a handful of calls)" should be corrected: real depth is 49-282 chromosomes in the oldest three bins.
- C1/C unchanged for the two-period statistic.

## 7. Who this helps
**Day / allies.**
- The 21 is not an artefact of sparse calls: at real AADR depth and with the Neolithic and Bronze Age replacement included, the neutral expectation at the textbook Ne = 1e4 is thousands, and replacement does not remove the gap (it widens it at high Ne). The earlier critic-side hope that call depth explains it fails.
- "Neutral also predicts ~0" (the critic-side reading of this statistic) is false unless Ne >= ~1e5 (closed) and is false at any Ne <= 1e6 under strong replacement.
- The model also cannot reproduce his 22,428 / profile without an error term, so a different implementation of his statistic (unpublished tracked threshold, error handling) is not excluded.
- His own d = 0.45 does not rescue the number: it gives 739 at Ne 1e4.

**Critics.**
- The 21 is only a deficit if Holocene Ne is ~1e4. Closed-population neutral drift gives ~20-30 post-5000 BP events at Ne ~1e5 with no clock failure; literature Holocene European Ne (growth, structure) is plausibly well above 1e4. A "stopped clock" is not needed.
- A 0.1% false-minor-call rate reproduces Day's pre-7000 share (0.98-0.997) and large eligible count, so the pre-7000 cluster is plausibly dominated by old-bin sampling and assay error, not by a burst of fixation.
- The 630-vs-21 comparison remains invalid (C6 denominator point is unchanged).
- Cuts against critics: the temporal-method Ne they cite (8-10k, C5b) makes the neutral expectation 190x above 21; the neutral expectation is not "~0" at their own Ne. Replacement does not explain the 21 either way; it raises S21. The eps = 1e-3 value is assumed, and the passing cells fail the profile and start-frequency table.
- No model, either side, reproduces Day's bin profile (8000-10000 and 7000-8000 dominate in his table; the 10000+ bin dominates in every simulation), so none of these numbers should be quoted as a replication of his result.

## 8. Caveats
- Single pooled European population per bin; real bins mix regions with different ancestry and dates. Sites are independent (no linkage; real effective numbers of independent loci are smaller, so run-to-run variance is understated, not the means).
- Panel density flat in folded frequency (1.86 per unit q, from the c1 D2 chain) down to 0, 7% of sites fixed in the ancestor and excluded, no mutations. Eligible counts at high Ne depend directly on this low-frequency end; a panel richer in rare variants would raise them.
- W, A, S branch lengths (Fst 0.09/0.07/0.05), pulse schedules, source Ne (1e4) and replacement shares are assumptions, not retrieved; Fst x0.5 and x2 changed S21 by <1.5x.
- Call depth: Binomial(n, mean p) per bin (slightly over-dispersed against the true Poisson-binomial). Per-site capture efficiency is a Gamma multiplier, not the real structured missingness (array subsets, probe sets). Day's "tracked" threshold is unstated; my tracked = at least one call per bin (0.95-1.00 vs his 0.727). The min-depth analysis is post hoc and single-replicate.
- Day's E1/T2 reading is my reconstruction; E2 gives the same post-7000 counts but larger eligible; T1 gives 2-3 orders more events.
- No selection, no genotype error in base cells, no contamination model; eps is flat per pseudo-haploid call. Bin dates are midpoints, 10000+ bin at 10,500 BP (assumed).
- I did not test the "why" of replacement raising S21 or of the missing 8000-10000 / 7000-8000 dominance. The profile mismatch is unexplained.
- Workhorse jobs were stopped for load; reps 0-3 ran locally.
