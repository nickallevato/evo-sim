# R4 C1c: Day's "21" with real AADR call depth and an ancestry-replacement model (revised after reviews)

Scripts: `research/checks/c1c_call_depth_replacement.py` (pre-registered, commit b128110, predictions P1-P8 in its docstring), `c1c_posthoc_mindepth.py`, `c1c_posthoc_variant_gate.py`, `c1c_posthoc2_fixpass.py` (post hoc, each committed before its run). Inputs: `results/c1c_depth_table.json`, `results/c1c_old_bin_dates.json`. Raw: `results/raw/c1c_rep0..3.json` (main), `c1c2_rep0..3.json` (post hoc 2); tables `results/raw/c1c_analysis.txt`, `c1c2_analysis.txt`. Figure: `results/R4-C1c-S21-vs-Ne.png`.

## Result in brief
1. **Day's statistic cannot be reproduced from his published method, in this model family or (so far) at all.** His 22,428 eligible alleles, his 11-bin profile (3,038 / 8,741 / 4,497 / ...), his tracked fraction (0.727) and his start-frequency table are not reproduced together by any of the 44 base scenarios or any variant (0 cells pass eligible + pre-7000 share + S21 + start table). His "tracked" threshold, error handling and code are unpublished. A direct run on the real AADR genotypes (follow-up C1d, running on workhorse) is the decisive test; this note does not do it.
2. **Scope.** Everything below is conditional on one model family: a single pooled European population per bin, independent sites, a flat low-frequency panel density assumed from the c1 chain, assumed source divergence and pulse schedules, strict neutrality. Numbers are sensitivities of the statistic, not measurements of the real S21.
3. **What the model does show.** At real AADR depth the "handful of calls" hypothesis (mean depth) is refuted: 49 / 62 / 282 chromosomes per site in the three oldest bins. Under homogeneous capture and no assay error, the model count of post-5000 BP events (S21, tracked E1-T2) is **1.5k-3.9k at a constant Ne of 1e4 (70-190x Day's 21)**, falls steeply with Ne, and reaches 21 at a closed-population Ne of about 1e5-2e5 (4-5e5 if the 10000+ bin is modelled at its real, mostly pre-10,500 BP dates). Ancestry replacement does not close the gap; at high Ne it raises S21 3-7x (R2) or up to ~40x (R3).
4. **The ratio S21 / eligible is the density-robust number.** Day: 21 / 16,299 = 0.129% (21 / 22,428 = 0.094%). Every error-free cell is 0.5% to 27%. Only error cells approach it (R0 Ne 1e5 with eps 1e-3: 0.13%).
5. **Capture matched to Day's tracked fraction** (ancient-bin heterogeneity only, minimum depth m = 40 chromosomes; corrected after review) changes S21 by at most ~1.6x: R0 Ne 1e5 gives 50.5 (tracked 0.72), R2 Ne 1e6 gives 25.8. The earlier "thousands" came from a design flaw (modern bin given Gamma capture) and is withdrawn.
6. **Verdict conditional on Holocene Ne, which is not sourced in this repo.** The Day-side reading (21 is a deficit) holds at Ne <= ~5e4 and under strong replacement at any Ne <= 1e6; the critic-side reading (21 is neutral-compatible) needs closed-population Ne >= ~1e5 or growth/step schedules reaching 1e5-1e6 within the window. The only Holocene Ne measurements either side cites (keruru 8,139 / 9,835) point to the first.

## 1. What was built
1. **Real call depth.** Public AADR **v62.0.p1** `.anno` (Harvard Dataverse file 13994492, the June 2026 patch; Day cites v62.0, the original is a different file; sha256 1935ecee..., parsed as text only). "SNPs hit on autosomal targets (1240k)" and the diploid/pseudo-haploid suffix give per-bin calls per site: Binomial(n, p x w_site). The European filter (lat/long box minus Turkey/Armenia/Syria/Georgia/Iraq/N. Africa/Russia/Crimea) was **chosen so the per-bin counts match Day's**: 8,808 individuals vs his 8,738, within about 1-5% per bin except the 0-500 BP bin (524 vs his 625). The script **rescales n to Day's n**, which invents 101 modern individuals with the observed diploid/pseudo-haploid mix; the unscaled alternative is in section 4 (S21 about 1.5x higher).
2. **Replacement.** Frequency-level exact Wright-Fisher; pooled European population EU starts as Mesolithic (W) at 10,500 BP, receives 10 Anatolian pulses (9,500-7,250 BP) and 6 steppe pulses (5,000-4,500 BP); sources W, A, S drifted from a common ancestor (Hudson Fst 0.086 / 0.067 / 0.049, assumed). R0 none; R1 modern shares W .32 / A .48 / S .20; R2 .12 / .50 / .38; R3 .05 / .41 / .55.
3. **Statistic** as c1b: E1 eligibility, T2 dating, tracked = at least one call in every bin. S21 = tracked events dated 5000-6000 BP or younger (Day: "0-6000 BP: 21"). **T1 is ruled out deductively, not only empirically:** under T1 an event dated to bin 0 would be 100% in every bin, hence not "polymorphic in an earlier bin" under any eligibility rule, yet Day reports 3,038 events in bin 0 (and under E1 also 8,741 + 4,497 in bins 1-2). Only a gaps-allowed "oldest 100% bin" reading such as T2 can produce his table; "working backward from the present", taken literally, is T1 and is impossible.
4. **The 10000+ bin is not 10,500 BP.** In the anno its pseudo-haploid individuals (n = 166) have median date 15,516 BP, quartiles 10,835 / 29,060, maximum 50,000. The main run placed the whole bin at 10,500 BP as the ancestral W population. Section 4 reruns with real dates (a bound, not a model of Upper Palaeolithic populations).

## 2. What the 21 maps to: the Ne axis
S21 = tracked E1-T2 events dated 5000-6000 BP or younger; homogeneous capture, no assay error; mean over 4 replicates. Day: S21 = 21, eligible 22,428 (tracked 16,299), S21 / eligible = 1.29e-3.

| Ne scenario | R0 closed S21 (x21) | R2 central replacement S21 (x21) | R0 eligible | R0 S21/eligible |
|---|---|---|---|---|
| **Ne = 2** (Day C5a "near 2") | 0 | degenerate (see note) | 0 | n/a |
| d = 0.45 at Ne 1e4 (drift clock x0.45, i.e. Ne/0.45) | 739 (35x) | 737 (35x) | 6,609 | 0.11 |
| d = 0.45 at Ne 2e4 | 157 (7.5x) | 286 (14x) | 3,292 | 0.048 |
| keruru's measured 8,139 (constant) | 5,825 (277x) | 3,026 (144x) | 18,839 | 0.31 |
| textbook 1e4 | 3,925 (187x) | 2,259 (108x) | 15,220 | 0.26 |
| keruru's 8,139 rising to 2e4 ("roughly doubles") | 2,055 (98x) | 1,254 (60x) | 10,508 | 0.20 |
| 8,139-9,835 raised ~5x for the bias keruru states (about 5e4) | 120 (5.7x) | 238 (11x) | 2,940 | 0.041 |
| Ne where S21 = 21 (main run, order of magnitude) | ~1.4e5 | above 1e6 (26 at 1e6) | ~1.4k | ~0.015 |
| step 1e4 until 8,000 BP, 1e5 until 4,000 BP, 1e6 after | 32 (1.5x) | 51 (2.4x) | 1,103 | 0.029 |
| growth 1e4 to 1e6 (exponential) | 35 (1.7x); R1 15 (0.7x) | 67 (3.2x); R3 220 (10x) | 1,359 | 0.026 |
| growth 1e4 to 1e5 | 262 (12x) | 276 (13x) | 3,635 | 0.072 |
| Ne = 1e6 (the "stasis" edge, Ne -> infinity) | 3.6 (0.17x) | 26 (1.2x) | 702 | 0.0052 |

Notes.
- **Ne = 2.** With 4 chromosomes every site is fixed within a few generations: R0 has no polymorphism in any later bin, so eligible = 0 and S21 = 0. Day's own paper reports polymorphic bins (22,428 eligible, 4,497 in the 7000-8000 bin), so Ne near 2 is inconsistent with his own table. The R2 cell is a numerical artefact (pulses re-inject frequencies that drift collapses at once; 943k "eligible") and is not interpretable.
- **Stasis.** Day's stated model ("genetic drift isn't happening at all", Q96, Z18525185 s5.1, s4.4) is the Ne -> infinity edge. Ne = 1e6 is within a few percent of it over 525 generations; an analytic limit (correctness review) gives eligible 683, S21 2.1. So non-drifting sampling alone yields a few events, and Day's observed 21 is about 6x above the stasis edge in the closed model. Day's own two Ne positions (stasis, and Ne near 2 in C5a) are mutually incompatible.
- **Keruru's range.** His 8,139 and 9,835 are for windows that include replacement and no relatedness filter, and his draft says all three biases are downward (up to fivefold under heavy replacement; "the true value is therefore plausibly higher", `adna-draft-1.md` lines 212-218). The model alone does not say how much to correct. The reviewer's scratch Nei-Tajima estimator on this model's own bins (not reproduced here) suggests that a temporal Ne over the Neolithic-to-present window comes out near 7-14k whatever the true drift Ne is under R2. The deficit at keruru's Ne is therefore a range, about 6x (R0 at 5e4) to ~280x (R0 at 8,139), not a point.
- **Every route to S21 near 21 needs a Ne at least 5-10x larger than keruru's stated figures** (at least 10x at the high end of his correction), or growth/step schedules that reach 1e5-1e6 within the window. Neither side's cited measurement supports that; see the retrieval gap in section 8.
- **Steepness.** S21 falls about as Ne^-2 near 1e4-1e5 (3,925 / 908 / 120 / 32 at Ne 1e4 / 2e4 / 5e4 / 1e5), so "Ne about 1e5" is a statement about a steep function.

**Matched-capture row (recomputed after the modern-bin fix).** Ancient-only Gamma heterogeneity plus a minimum of m called chromosomes per bin, chosen so tracked is closest to Day's 0.727:

| Cell | variant | tracked | eligible | pre-7000 | S21 | 0-500 BP events | S21/eligible |
|---|---|---|---|---|---|---|---|
| R0 Ne 1e4 | kappa 0.25, m 20 | 0.77 | 7,832 | 0.57 | 2,203 | 211 | 0.36 |
| R0 Ne 1e5 | kappa 0.5, m 40 | 0.72 | 1,074 | 0.92 | 50.5 | 19 | 0.065 |
| R0 Ne 3e5 | kappa 0.5, m 40 | 0.74 | 634 | 0.96 | 11.8 | 4 | 0.025 |
| R0 Ne 1e6 | kappa 1, m 40 | 0.71 | 566 | 0.98 | 8.2 | 4 | 0.020 |
| R0 growth 1e4-1e6 | kappa 0.5, m 40 | 0.73 | 882 | 0.88 | 48.5 | 11 | 0.075 |
| R2 Ne 1e5 | kappa 0.25, m 40 | 0.73 | 546 | 0.74 | 83 | 16 | 0.21 |
| R2 Ne 1e6 | kappa 0.25, m 40 | 0.72 | 257 | 0.82 | 25.8 | 10 | 0.14 |

Matched capture raises S21 by at most ~1.6x at high Ne (and lowers eligible); it does not rescue Day's ratio. Day's tracked fraction needs m = 40 here, i.e. a depth threshold plus heterogeneity; the threshold is a fitted device (one parameter, one number).

## 3. Does the model reproduce Day's table? (validity gate)
Pre-registered gate (P3): eligible within 3x of 22,428, pre-7000 share >= 0.90, S21 in [7, 63]. **Post hoc additions, labelled:** start-frequency table (share of eligible alleles with Neolithic frequency in [99,100) between 70 and 90%, Day 79.2%), the S21 / eligible ratio, and the total-variation (TV) distance of the 11-bin profile from Day's (no pre-registered threshold). **0 of 44 base cells pass the pre-registered gate; no base cell or variant passes all four criteria (three numbers + start table).**
- **Error cells (eps = flat false-minor-call rate on pseudo-haploid calls; assumed, not measured).** Post hoc sweep, homogeneous capture, tracked E1-T2:

| Cell | eps | eligible | pre-7000 | S21 | S21/eligible | start [99,100) % | 0-500 BP events |
|---|---|---|---|---|---|---|---|
| R2 Ne 1e4 | 1e-4 / 3e-4 / 1e-3 / 3e-3 | 9.8k / 12.7k / **20.2k** / 29.1k | 0.71 / 0.77 / 0.85 / 0.88 | 2,274 / 2,326 / 2,429 / 2,831 | 0.23 / 0.18 / 0.12 / 0.097 | (main run, 1e-3) **81.7** | 160 / 208 / 342 / 999 |
| R0 Ne 1e4 | 1e-3 | 61.2k | 0.917 | 4,216 | 0.069 | 89.8 | 572 |
| R0 Ne 1e5 | 1e-4 / 3e-4 / 1e-3 / 3e-3 | 7.4k / 17.7k / 45.3k / 78.8k | 0.993 / 0.997 / 0.997 / 0.984 | 31 / 34 / 78 / 704 | 0.004 / 0.002 / 0.0017 / 0.009 | 99.7-99.8 | 4 / 3 / 12 / 105 |
| R2 Ne 1e6 | 1e-4 / 3e-4 / 1e-3 / 3e-3 | 1.8k / 4.0k / 10.2k / 17.5k | 0.974 / 0.987 / 0.992 / 0.981 | 27 / 30 / 41 / 193 | 0.015 / 0.007 / 0.004 / 0.011 | 99.7 | 4 / 5 / 6 / 36 |

- **The textbook-Ne error cell** (R2, Ne 1e4, eps 1e-3) matches Day's **eligible count (20.2k vs 22.4k)** and his **start-frequency table (81.7 / 17.8 / 0.5 / 0.0 vs 79.2 / 20.2 / 0.5 / 0.2)** but not the tail: S21 2,429 (115x), pre-7000 share 0.853 vs 0.9986, S21 / eligible 0.12 vs 0.0013. The high-Ne error cells (R0 Ne 1e5, R2 Ne 1e6 at eps 1e-3) match the tail and the ratio (R0 Ne 1e5: 0.0017 in the post hoc run, 0.0013 in the main run) but miss the start table (99.8% in [99,100)) and the eligible count by 2x. **The summaries disagree about Ne** (eligible and start table prefer ~1e4; the tail prefers ~1e5), which is a sign of misspecification, not a fit; the pre-7000 share and S21 are the same tail measured twice.
- **What eps explains and what it does not.** It explains most of the **eligible count and the pre-7000 share** (eligible x4 to x27; pre-7000 0.98-0.997 at Ne >= 1e5) because errors on near-fixed sites make them look polymorphic in a deep old bin. It does **not** reduce the tail: S21 rises 1.5x (R2 Ne 1e6) to 2.5x (R0 Ne 1e5) with eps = 1e-3, about 4.6x for R0 at Ne >= 3e5, and 5-12x at eps = 3e-3 (704 at R0 Ne 1e5). So an error rate large enough to explain the 22,428 adds events to the post-5000 BP bins rather than removing them, and leaves the 21 where the Ne map puts it; the eps value was not measured (no sweep value is anchored to anno damage/library columns, which are available and unused).
- **Profile.** TV 0.57-0.80 in every main-run cell. The old-bin variant below shows this is partly the oldest-bin composition.
- **Post-7000 timing.** Day has 2 / 16 / 5 events in 6000-7000 / 4000-6000 / younger. R2 at Ne 1e6 gives 42% / 30% / 28%; no steppe cluster like his.
- **S21 events by start band** (post hoc, tracked, base; % in [99,100) / [95,99) / [90,95) / <90): R0 Ne 1e4 27 / 70 / 2.3 / 0; R0 Ne 1e5 76 / 24 / 0 / 0; R2 Ne 1e6 86 / 14 / 0 / 0; step schedule 93 / 7 / 0 / 0. In every non-degenerate cell at least 95.7% of S21 events start at >= 95% in the Neolithic and at most 0.1% start below 90%. These are near-fixed completions, the class Day's own s4.3 says his events belong to. **Day's separate intermediate-start claim (0 events from <50%, 1 and 3 from 50-90%; claim C, Z23046531) is not addressed or contradicted by this statistic.**

## 4. Sampling variants and the 10000+ bin (post hoc 2)
**Capture heterogeneity (kappa), corrected.** The main run drew an independent Gamma multiplier for the modern bin too, although 82% of that bin is high-coverage shotgun diploid; sites with a low draw had a handful of modern calls and were trivially "100% modern", so 95-99% of the apparent inflation sat in the 0-500 BP bin (Day: 2 events). With heterogeneity on the ancient bins only (modern uniform), kappa in {2, 1, 0.5, 0.25} x m in {1, 10, 20, 40}:

| Cell | variant | eligible | tracked | S21 | 0-500 BP events |
|---|---|---|---|---|---|
| R0 Ne 1e5 | homogeneous | 1,678 | 1.00 | 31 | 6 |
| R0 Ne 1e5 | modern also heterogeneous (main-run design), kappa 1, m 1 | 8,986 | 0.99 | 3,989 | 3,856 |
| R0 Ne 1e5 | same, kappa 0.5, m 1 | 27,407 | 0.95 | 16,216 | 15,996 |
| R0 Ne 1e5 | ancient only, kappa 1, m 1 | 1,368 | 1.00 | 49 | 16 |
| R0 Ne 1e5 | ancient only, kappa 0.5, m 1 | 1,122 | 1.00 | 52 | 19 |
| R0 Ne 1e5 | ancient only, kappa 0.25, m 40 | 820 | 0.75 | 42 | 15 |
| R2 Ne 1e6 | modern also heterogeneous, kappa 1, m 1 | 7,284 | 0.99 | 3,580 | 3,410 |
| R2 Ne 1e6 | ancient only, kappa 1, m 1 | 428 | 1.00 | 31 | 8 |
| R0 Ne 1e4 | ancient only, kappa 0.5, m 1 | 10,754 | 0.99 | 2,794 | 248 |

**Withdrawn:** "capture heterogeneity is the strongest upward lever on S21", "S21 of 15-20k at every Ne", "Day's tracked fraction can be reproduced, but only with S21 in the thousands", and the P7 reading of a 40-600x change. With ancient-only heterogeneity S21 changes by x0.5 (R0 Ne 1e4) to x1.7 (R0 Ne 1e5), eligible falls, and tracked 0.72-0.75 needs a depth threshold of m = 40. **P7 re-scored:** as pre-registered (modern bin included) it failed for a design reason; rerun post hoc, the S21 half (<2x) holds and the tracked-fraction half (55-90%) holds only with m >= 20-40.

**10000+ bin at real dates (bound).** Individuals of the bin are placed on the W lineage at their real dates (7 date groups), i.e. nearer the ancestor than W at 10,500 BP:

| Cell | variant | eligible | pre-7000 | S21 | TV, all bins | TV, bins 1-10 only |
|---|---|---|---|---|---|---|
| R0 Ne 1e5 | 10,500 BP (main) | 1,678 | 0.968 | 31 | 0.69 | 0.29 |
| R0 Ne 1e5 | real dates | 1,669 | 0.910 | 79 | **0.25** | 0.30 |
| R0 Ne 1e6 | real dates | 700 | 0.950 | 13.8 | 0.26 | 0.31 |
| R0 Ne 1e4 | real dates | 15,195 | 0.579 | 5,062 | 0.43 | 0.52 |
| R2 Ne 1e6 | real dates | 561 | 0.877 | 35 | 0.49 | 0.28 |
| R2 Ne 1e6 | real dates + eps 1e-3 | 10,064 | 0.988 | 62 | 0.70 | 0.30 |
| R0 Ne 1e5 | real dates + eps 1e-3 | 45,314 | 0.986 | 212 | 0.55 | 0.31 |

The over-dominance of the oldest bin in the profile mismatch is largely attributable to its age composition (all-bin TV 0.69 to 0.25 in R0 high-Ne cells). The shape of bins 1-10 (8000-10000 and 7000-8000 dominating in Day's table) is unchanged (TV 0.28-0.33 at high Ne), so that part of the mismatch is still unexplained. Real dates raise S21 by 1.3x (Ne 1e4) to 2.6-4.5x (R0 Ne >= 1e5), moving the R0 crossing to Ne of about 4-5e5. This is a bound; the model of older individuals is crude.
**Unscaled modern bin (524 individuals):** S21 1.5x higher (R0 Ne 1e5: 46; R2 Ne 1e6: 43), eligible 1.15-1.26x.
**Other sensitivities (main run), 25 y/generation and Fst x0.5 / x2:** S21 0.6-0.7x for 25 y; Fst changes S21 by <1.5x, but see the caveat on the saturated replacement lever below.

## 5. Pre-registered predictions: what held
| P | Prediction | Result |
|---|---|---|
| P1 | Real depth alone does not give 21; R0 Ne 1e4 S21 in [300, 10,000] | **Held** (3,925). "Refuted" applies to the mean depth only (49 / 62 / 282 chromosomes); per-site structure in real AADR data (probe subsets, damage filtering) is untested. |
| P2 | S21 monotone in Ne; R0 Ne* in [3e4, 1e6]; R2 Ne* within 3x of R0 | **Partly held:** monotone; R0 Ne* ~1.4e5 (order of magnitude, 4 replicates); R1 ~1e5. **Failed for R2/R3** (26 and 140 at Ne 1e6). |
| P3 | No (R, Ne) cell passes eligible + pre-7000 + S21 | **Held for the base grid (0/44); refuted when an error rate is added** (R0 Ne 1e5 and R2 Ne 1e6 at eps 1e-3 pass the three numbers; they fail the profile and the post hoc start-table criterion). |
| P4 | Replacement second order for S21 (<2x); eligible >= 1.3x; pre-7000 +10 pp; steppe bump >= 1.5x | **Refuted.** R2/R0 S21 = 0.58 at Ne 1e4, 3.2x at 1e5, 7.2x at 1e6 (R3 up to ~39x). Eligible lower for R1/R2 at all Ne (not for R3 at Ne >= 1e5: 1,983 vs 1,659). Pre-7000 share lower. 4000-6000 BP share R2/R0 0.96 (Ne 1e5) to 1.65 (R3/R0 at 1e6; R0 has 6 events): noisy, not >= 1.5x consistently. |
| P5 | d = 0.45 acts as neutral at Ne/0.45 | **Tautological** (implemented as Ne/d): not a test of any model. The substantive part (S21 >= 5x the 21 at Ne 1e4) holds: 739. |
| P6 | eps 1e-3 raises S21 >= 3x at R2 Ne 1e6 | **Failed:** 1.4-1.5x (37-41 vs 26-27); 1.9-2.5x at R0 Ne 1e5 (4.6x at R0 Ne >= 3e5); its large effect is on eligible and pre-7000. |
| P7 | kappa 0.5: tracked 55-90%, S21 <2x | **Failed as run** (design flaw, section 4); post hoc rerun: S21 half holds, tracked half only with m >= 20-40. |
| P8 | 21 reached only if Holocene Ne >= ~5e4; at Ne <= 2e4 hundreds to thousands | **Held for closed populations** (Ne* ~1-1.4e5; 908 at 2e4); **not for strong replacement** (floor 26-140 at Ne 1e6); and the Ne >= 1e5 escape is also reached by growth/step schedules (section 2). |
Two priors were wrong: replacement is a large lever at high Ne (a first-order effect, mechanism untested; the lever depends on the source Ne and rare-allele differentiation, see caveats), and the 10000+ bin's age composition matters for the profile and S21.

## 6. Which assumptions flip the conclusion
"Conclusion" = whether the observed 21 is far below the model expectation (deficit), within about 3x, or above. All cells fail the full gate (section 3); "within about 3x" cells fail eligible, profile and tracked fraction, so this is a sensitivity table, not a consistency test.
- **Deficit (S21 model >= ~60):** constant Ne <= ~5e4 in any model; R2-R3 at any Ne up to 1e6; reading T1 (impossible reading); Day's d = 0.45 at Ne <= 2e4; the 10000+ bin at real dates at Ne 1e5 (79); unscaled modern bin (x1.5).
- **Within ~3x:** closed or mild replacement (R0, R1) at Ne ~1e5-3e5; R2 at Ne >= 3e5; growth 1e4 to 1e6 (R0 35, R1 15) and the 1e4 / 1e5 / 1e6 step schedule (32; R2 51); homogeneous or matched capture (ancient-only), no assay error.
- **Below 21 (the observation is above the model):** R0/R1 at Ne >= 3e5 (3-8), eligible 0.3-0.9k.
- **Largest single input:** the Holocene Ne trajectory. Next: replacement strength at high Ne; then, for the tail, any error term.
- **Eligible vs S21 sensitivity:** both scale with the unmeasured low-q panel density; the S21 map against Ne is much less sensitive than eligible (analytic check: tilting the density by (q/0.01)^+-0.5 multiplies eligible by 3.1 / 0.38 but S21 by 1.7 / 0.62), and the S21 / eligible ratio is density-robust. The "eligible 13-40x short" part of the gate is therefore assumption-dependent; the S21 map and the ratio are the robust parts.

## 7. Verdict and suggested edits (not applied; claim files untouched)
Vocabulary as in the repo (internal / fidelity / external; `untestable`, `contested`, `supported`, `holds`, `non-sequitur`, `pending`):
- **C6** (Day, Z18525185): external stays `untestable`. Comment: the 21 and 22,428 are not reproducible from the published method; in a model with real AADR depth, the 21 is 70-190x below the neutral expectation at Ne 1e4 (S21 / eligible 0.26 vs Day 0.0013), within ~3x only at closed-population Ne ~1e5-3e5 or with growth/step schedules to 1e5-1e6; strong replacement keeps it above 21 at Ne 1e6. Replace the review #4 phrase "per-site call depth (a handful of calls)" with "mean depth 49 / 62 / 282 chromosomes in the three oldest bins; the modern-bin heterogeneity result was a design flaw". Internal verdict unchanged (`arithmetic-error`, the 630-vs-21 denominator).
- **C** (Day, 0-3 from intermediate starts): external `contested` unchanged. Add: C1c does not address the intermediate-start statistic; the 21-class events start at >= 95%.
- **C1** (ascertainment): external `supported` unchanged; add that the panel-density input (flat folded 1.86/q to q = 0, 7% fixed) is unmeasured and controls the eligible leg (S21 less so).
- **C1a** (Day's ascertainment reply): `holds` for the 10-90% bands unchanged; comment that this check does not test it.
- **C5** (keruru, neutral zero): internal `holds` for the statistic it addresses (intermediate starts); comment that the three figures do not agree (keruru's 10^-29 over a million loci and 4 x 10^-35 per locus from p = 0.5, vs the repo's derived 1.2e-46 for the per-locus case, 11 orders spread in the C5 file) and that C1c does not test the intermediate-start claim.
- **C5b** (keruru, temporal Ne): keep `pending`. Comment: his 8,139 / 9,835 are for windows spanning replacement, carry no relatedness filter, and the draft states all biases are downward (up to fivefold); the repo's model puts S21 at 6-280x the 21 across that range; the author's code and a temporal-Ne observable on these simulations are not yet in the repo.
- **C7** ("genetic drift isn't happening at all"): external `pending` -> keep `pending`, add: the stasis edge (Ne -> infinity) gives S21 about 2-5 against 21 observed, but C1c does not isolate drift from replacement; Day's other position (C5a, Ne near 2) predicts no polymorphism, inconsistent with his own table; internal `non-sequitur` stands.

## 8. Who this helps
**Favours Day / allies.**
- The 21 is not an artefact of sparse calls (mean depth 49-282 chromosomes in the oldest bins) or of replacement (which widens the gap at high Ne) or of capture heterogeneity (matched capture changes S21 by <= 1.6x).
- At every Ne <= ~5e4 and under strong replacement at any Ne <= 1e6 the model expectation exceeds the 21.
- The two cited Holocene measurements (keruru 8,139 / 9,835) sit in that range.
- The textbook-Ne cell with a small error rate reproduces his eligible count and start table (section 3).
- "Neutral also predicts ~0" is false for this statistic at Ne <= 1e5 closed and at any Ne under strong replacement (that phrase is the repo's own audit wording in claim C, not a quoted critic; C1b attributed it to the Day side, C1c to the critic side).

**Favours the critics.**
- Day's own d = 0.45 gives 739 (35x), so his parameter does not produce the 21; his two Ne positions (stasis; Ne near 2) are mutually incompatible and Ne near 2 contradicts his own table.
- Closed-population drift, a growth or step schedule to 1e5-1e6, or Ne about 1e5 gives 15-35 events with no clock failure; R0 Ne* is 1e5-5e5 depending on the 10000+ bin's dates.
- A false-minor-call rate of 1e-3 explains most of the 22,428 and the pre-7000 share. It does not explain the tail.
- The 630-vs-21 comparison remains invalid (C6 denominator).

**Against both / neutral.**
- No cell passes the full gate (three numbers plus start table; profile TV >= 0.25 in every cell, 0.5-0.8 in most); the matched-capture, error and Ne routes each fit some summaries and miss others. Neither side may quote these numbers as a replication.
- The same gate caveat applies to the Day-side and critic-side bullets above: all are model-conditional.
- The Holocene Ne is the load-bearing, unsourced input for both. The repo's only Ne parameter is the textbook 1e4 ("unverified"); keruru's 8-10k is the only measurement either side cites and it is self-described as biased downward.

**Where each side was wrong or unsupported (attributed).**
- **Day:** Ne near 2 (C5a) contradicts his own polymorphic table; the abstract's "99.8% in 8000-10000 BP" is the 3-bin pre-7000 share (C6 file); five different fold figures; "stasis" asserted without a model; no thresholds for "tracked"; the 630 expectation is a genome-wide count compared with a panel count.
- **keruru (critic):** "somewhere near 10^-29" (KR-03) and "around 4 x 10^-35" vs the repo's 1.2e-46 for the same start (C5 file; I did not re-derive); the draft states the ratio three ways (abstract 10^-4, s6 4 x 10^-4, s6.2 8 x 10^-4; B2e claim file) with `[CHECK]` marks and no review pass; his own draft says his Ne is biased downward while critics quote it as "Ne about 1e4", and at Ne 1e4 neutral predicts 1.5-3.9k, not ~0; his "structure inflates the estimate, does not deflate it" (draft line 637) cuts against any critic who invokes structure to dismiss a low Ne.
- **McCarthy:** I found no aDNA, Ne or C-branch quote from him in `quotes-critics.md`; his recorded slips concern other branches.
- **"Literature Holocene Ne plausibly well above 1e4"** (my earlier sentence): removed; unsourced.

## 9. Caveats
- **Model family.** One pooled population per bin (real bins mix regions of different ancestry and date); independent sites (linkage would widen run-to-run variance, not move means); strict neutrality; no new mutations.
- **Panel density.** Flat folded density (1.86 per unit q) to q = 0 from the c1 chain, 7% of sites fixed in the ancestor excluded. No out-of-Africa bottleneck, no European-discovery arrays. Controls the eligible leg far more than S21 (section 6).
- **Replacement lever.** Fst x0.5 / x2 changes S21 only 22-32 at R2 Ne 1e6, but this is not evidence of robustness: the effect is saturated and set by the assumed source Ne (1e4) and rare-allele differentiation. A control with pre-window Fst ~0.004 and no post-window source drift gave S21 2-4 (R2) and 7-10 (R3) at Ne 1e6, against 20-26 and 49-54 with source Ne 1e4 (correctness review scratch). The mechanism is open; P4's "refuted" stands.
- **Depth.** Binomial(n, mean p) per bin (slightly over-dispersed against the Poisson-binomial); heterogeneity is Gamma, not the real structured missingness (array subsets, probe sets); kin clusters and damage are not modelled; the 1e-3 error rate is flat and symmetric and not anchored to the anno's damage, library-type or contamination columns (available, unused).
- **Replicates.** 4 independent panel trajectories (2 sampling draws each share one trajectory) for the main run and 4 x 1 for post hoc 2. Enough for factor-of-2 to factor-of-10 statements (Ne* of order 1e5, 70-190x at Ne 1e4); not enough for a point value of Ne* (S21 standard error ~8-10% gives ~10-15% on Ne* before the model uncertainties) or for borderline calls at 1.2-1.9x. The Poisson `pL(21)` column in `c1c_analysis.txt` is not meaningful (independence understates variance).
- **Tracked definition.** Calls in all 11 bins (Day: "insufficient coverage in intermediate time bins", threshold unstated); S21 events additionally need calls in older bins than the dating bin.
- **Day's reading.** E1/T2 is a reconstruction; T1 is impossible (section 1).
- **Unexplained.** The 8000-10000 and 7000-8000 BP dominance of Day's profile (bins 1-10 TV 0.28-0.58) and why replacement raises S21.

## 10. Review resolution
Correctness review (`REVIEW-R4-C1c-correctness.md`):
| # | Finding | Status |
|---|---|---|
| 1 MAJOR | kappa variants gave the modern bin Gamma capture; "strongest lever" an artefact | **Applied.** Rerun post hoc with ancient-only heterogeneity; bin-10 counts reported for every variant (`c1c2_analysis.txt` A); "strongest lever", P7 outcome, "tracked reproducible only with S21 in thousands" and the priors paragraph withdrawn or rewritten (sections 2, 4, 5). Post hoc script `c1c_posthoc2_fixpass.py` committed before the run (d2fe788). |
| 2 MAJOR | 10000+ bin is mostly older than 10,500 BP (median 15.6 kBP) | **Applied.** Date composition stated; real-date bound run; profile mismatch re-assessed (all-bin TV 0.69 to 0.25 in R0 high-Ne cells; bins 1-10 shape unchanged); "unexplained" rephrased as "partly attributable ... remainder unexplained"; S21 rises 1.3x to 4.5x (section 4). |
| 3 MINOR | Eligible leg depends on low-q density; S21 and ratio robust | **Applied** (sections 2, 3, 6, 9; ratio is headline item 4). |
| 4 MINOR | Fst x0.5/x2 does not bound the replacement lever | **Applied** (section 9: saturation, source-Ne control). |
| 5 MINOR | T1 deductively impossible; tracked stricter than Day's wording | **Applied** (sections 1, 9). |
| 6 MINOR | file is v62.0.p1; tuned filter; 101 rescaled individuals; dead `.HO` branch; within-bin date spread | **Applied** (section 1; unscaled sensitivity in section 4). `.HO` is dead code, harmless; within-bin date spread still not modelled (listed in caveats via "pooled population per bin"). |
| 7 MINOR | replicates | **Applied** (section 9: 4 trajectories; no point Ne*). Seed keyed on scenario index noted; irrelevant to committed runs. |
| 8 MINOR | unlabelled post hoc criteria; numeric slips; P5 tautological; s6 too broad; "refuted" scope | **Applied.** Post hoc criteria labelled (section 3); kappa-2 multiplier is 14x (R0 Ne 1e5) to 5x (R2 Ne 1e5) to 16x (R2 Ne 1e6); TV minimum 0.57; steppe range 0.96-1.65; replacement lowered eligible for R1/R2 but not R3; P5 flagged tautological; the "Ne >= 1e5" statement now says R0/R1 only; "refuted" scoped to mean depth. |
| 9 NIT | pulse update not clipped; float32; 0-500 BP at 250 BP | **Declined as unneeded** (ran without error; immaterial); the post hoc 2 drift function clips p. |

Day-side steelman (`REVIEW-R4-C1c-steelman-day.md`):
| # | Finding | Status |
|---|---|---|
| F1 MAJOR | "Consistent" cells assume homogeneous capture; matched capture gives 40-80x | **Applied and revised:** the 40-80x result came from the design flaw (correctness M1); matched-capture rows recomputed ancient-only (S21 <= 1.6x change), table in section 2; "Ne* = 1.4e5" labelled conditional (4 replicates; real dates shift it to 4-5e5). Matched cells at Ne 3e5, 1e6 and growth run. |
| F2 MAJOR | Textbook-Ne error cell matches eligible and start table | **Applied** (section 3; start table added to gate; "which Ne each summary prefers"). |
| F3 MAJOR | Assay-error cluster claim drawn from cells worst on the profile | **Applied.** Clause removed; eps explains eligible and pre-7000 share, not the tail, "hypothesis, profile TV 0.55-0.80". |
| F4 MAJOR | Eligible and S21 not independent; report S21/eligible; measure panel density | **Partly applied:** ratio reported throughout; density-sensitivity analytic check added; measuring the real low-q density from 1000G / modern AADR bin deferred (C1d / follow-up; not done here). |
| F5 MAJOR | Ne >= 1e5 unsourced and contradicted by cited measurement; growth under-reported | **Applied.** "Plausibly well above 1e4" removed; Holocene-Ne retrieval gap recorded (below); growth and step cells in section 2; keruru's schedule run (8,139 constant; 8,139 to 2e4). The implied growth schedules need Ne ~1e5 by the Bronze Age, >10x keruru's 8,139 (stated). |
| F6 MAJOR | Stasis not simulated | **Applied:** stasis = Ne -> infinity edge (3.6 at 1e6; analytic 2.1); Ne axis in section 2 includes Ne near 2 (C5a). |
| F7 MAJOR | eps flat, single point, unmeasured | **Partly applied:** sweep 1e-4 to 3e-3 at 7 cells (section 3). Anno-derived eps (damage-rate, library-type columns) and a transversions-only variant **deferred** (needs a new pre-registered design; reviewer's suggestion is sound). |
| F8 MAJOR | T2 chosen to resemble Day's; replicate on real genotypes | **Applied:** T1 ruled out deductively; scope narrowed to "this model family"; direct replication on real genotypes referred to follow-up C1d (running on workhorse; not started here). Zenodo scripts check deferred to C1d. |
| F9 MINOR | Day-valid points not prominent | **Applied** ("Result in brief"; section 8). |
| F10 MINOR | "Consistent" label too strong | **Applied** ("within ~3x"; "sensitivity, not consistency"). |
| F11 MINOR | 190x range; capture raises; "no model" wording | **Applied** (ranges 70-190x; "none of 44 base cells and no variant passes the full gate"). |
| F12 MINOR | modern 524 vs 625; generation time | **Applied** (section 4: x1.5). |
| F13 MINOR | typo "Calls depth"; C6 correction | **Applied** (typo gone; C6 edit in section 7). |

Critic-side steelman (`REVIEW-R4-C1c-steelman-critic.md`):
| # | Finding | Status |
|---|---|---|
| 1 MAJOR | Headline constant-Ne; growth/step families | **Applied:** Ne-axis table includes growth, step and measured trajectories; sign flips inside the census-explosion family; Ne^-2 steepness stated. The step cell is the reviewer's suggestion (1e4 / 1e5 / 1e6). |
| 2 MAJOR | keruru's Ne and his stated downward bias; estimator insensitive to drift Ne under replacement | **Partly applied:** deficit stated as a range (6x to ~280x); his bias caveat quoted; reviewer's scratch temporal-Ne estimate cited as reviewer scratch, not reproduced. Building and pre-registering an in-model temporal-Ne observable **deferred** (separate check). |
| 3 MAJOR | "Neutral predicts ~0" is about a different statistic; S21 start bands | **Applied.** S21 start-band table added (section 3); wording split into intermediate starts (not addressed) and near-fixed starts; attribution corrected (repo's phrase). |
| 4 MAJOR | Report S21/eligible; run Z23046531 two-period statistic at Ne 1e5; panel-density variants | **Partly applied:** ratio is headline; out-of-Africa bottleneck / European-discovery array variants and the two-period check at Ne 1e5 **deferred** (separate pre-registered checks). |
| 5 MAJOR | eps result missing from verdict and headline; anchor eps | **Applied** (headline item, section 3; `k0.5e1e-3` variant dropped with the flawed design; eps sweep). Anno-anchored eps deferred (see F7). |
| 6 MINOR | Reproducibility should lead; same gate caveat on Day-side bullets | **Applied** (Result in brief item 1; section 8 "Against both"). |
| 7 MAJOR | Critics' errors not attributed | **Applied** (section 8 attributed list; verdict edits for C5, C5b in section 7; B2e inconsistency cited from its claim file; no McCarthy aDNA claim found by search of `quotes-critics.md`). |
| 8 MINOR | "strongest lever" rests on modern-bin heterogeneity | **Applied** (withdrawn; attribution run: modern vs ancient-only, section 4). |
| 9 MINOR | kin-cluster design effect | **Declined for now:** hypothesis only; needs a new design; listed in caveats. |
| 10 MINOR | Bullets filed under the wrong side | **Applied** (section 8 regrouped; d = 0.45 under critics, "no model reproduces" under both). |
| 11 MINOR | Unsourced Holocene Ne | **Applied** (removed; gap recorded). |
| 12 MINOR | Claim files beyond C6 | **Applied** (section 7 covers C, C1, C1a, C5, C5b, C6, C7; C4 and B2e comments: the 3.3-fold and "roughly doubles" measurements bound the variation far below 100x growth). |

## Follow-ups and retrieval gap
- **Holocene-Ne retrieval gap (for `ledgers/gaps.md`, not edited here):** retrieve IBD-based and ancient-DNA demographic estimates of European Ne over the last ~10,000 years with locators; neither the 1e4 textbook value nor any "well above 1e4" statement is currently sourced in the repo.
- **C1d (running on workhorse):** direct run of E1/T2 and T1 on real AADR v62 genotypes; check Day's Zenodo scripts. This is the decisive test of whether the statistic as published reproduces 22,428 / 21.
- Deferred, each needing its own pre-registration: anno-anchored eps and transversions-only variant; in-model temporal-Ne estimator (keruru-style); Z23046531 two-period statistic at Ne 1e5; measured low-q panel density and European-discovery sites; kin-cluster design effect; real structured missingness (HO array subset).
