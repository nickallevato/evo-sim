# R4-FMnull: neutral-null calibration of Day's "more than 80 times more variable" (FM3, Q164)

Status: **run, scored, three reviews done, fix pass done (2026-10-13); not yet integrated** (load-bearing tier). Reviews: `REVIEW-R4-FMnull-correctness.md` (af8a960), `REVIEW-R4-FMnull-steelman-day.md` (5a36667), `REVIEW-R4-FMnull-steelman-critic.md` (64c2dba). Every MAJOR and MINOR is answered by id in the last section, "Review resolution". **Severity limit (ST-10), which qualifies every result below:** a DAY class would have been a severe result; the outcome observed (no DAY) is the weakly tested one. The check could return DAY for a one-lineage block mechanism of the size Q169 (b) asserts and has little power against smaller ones (section 6a). No verdict value moves. Script `research/checks/fm_mesa_null.py` (md5 0b25eaf7…8cab68c, equal to the md5 in `raw/fmnull.host`). Registered 48241c7 (2026-10-12); post hoc amendment 1, pre-run, no data seen, cc5e6dd (parameter set SOURCED beside PREREG); post hoc amendment 2, pre-run, no data seen, 408ba53 (answers `REVIEW-R4-FMnull-prerun.md`: set AMENDED, calibration variants, symmetric classes, reproduction gate, readings R1u and U-BP). Only `selftest` had run before each of the three commits. Run 2026-10-13 on na-workhorse, one process, in the order selftest, analytic, simulate, realdata, post (17:06:42 to 17:28:37 UTC). Raw outputs committed 29245a8: `raw/fmnull_selftest.out`, `fmnull_analytic.{out,json}`, `fmnull_sim.{out,json}`, `fmnull_real.{out,json}`, `fmnull_post.{out,json}`, `fmnull.host`. The json files are the source of every number below. No registered or amended code, output or score was changed after the run. Anything computed here beyond the printed outputs is marked **post hoc, descriptive**. The fix pass added three modes beside the registered ones, each committed and pushed before its run, each writing new files: `simphase` (script 57f2834, outputs fee27c3: `raw/fmnull_simphase.{json,out,host}`, na-workhorse, one process, 5 min 08 s, 390 MB; phase 0 reproduces `fmnull_sim.json` with maximum relative difference 0), `p45fix` (script 3d508ef, outputs 70eb15b: `raw/fmnull_p45fix.{json,out}`, local, 1.1 s; the truncated grid reproduces the committed json exactly) and `fixpass` (script 5463c7c, outputs 319e127: `raw/fmnull_fixpass.{json,out}`, local, 12 s, from committed json). `git diff 408ba53` on the script shows additions only.

Target (verbatim, Q164, voxday.net "The Fourth Mechanism", 2026-10-10, ¶4): "The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts." It is claim FM3 and a premise of FM10 (Q171, ¶8: "What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable candidates.") and ROOT-FM. Day has released no window size W, no definition of the statistic, no lineage unit, no masking rule and no code (refreshes to 2026-10-12).

**What can and cannot be scored today.** The index of a count process over windows grows with W under every model with regional rate variation, so "80" fixes no class without W. The deliverable is therefore a lookup table (W x divergence -> neutral band) under three parameter sets, plus a statement of where the held alignment itself shows an index near 80. Day's number cannot be given one class. Q164 is a comparison with a uniform rate and, read as a variance-to-mean ratio, is true as such of the held alignment at W >= 1 Mb (section 0); this check asks a further question that Day has not posed in writing, namely whether such an index exceeds what known neutral heterogeneity gives. No verdict value moves (section 7). The table can score his number the day he publishes W, statistic and unit: `fm_mesa_null.py score --W … --value 80 --reading … --unit … --exposure … --d … --real raw/fmnull_real.json`.

**Label for every result.** REGISTERED = computed and scored exactly as in 48241c7 with the brackets of set PREREG. SOURCED = the same code with the brackets of amendment 1. AMENDED = the amendment-2 outputs (json key `amend2`, mode `post`). All three were fixed before any run. Set PREREG's brackets are unsourced except the ILS sigma; SOURCED sources M1 sigma (Smith 2018, FML-S2), ILS sigma (Hobolth 2007, FML-H1, FML-H2) and the BGS ratio; AMENDED replaces the M0 and M1 corners by an envelope fitted to the three de novo mutation datasets in Smith 2018. Every length scale ell, and M2, M3, CPG, GBGC, ALN and the TREE branch lengths, are unsourced in all three sets.

## 0. Readings and lineages (added in the fix pass; post hoc, descriptive, from `raw/fmnull_fixpass.json`)

**Readings (rule RD; one paragraph for both sides).** The most defensible reading of Q164 is R1, the variance-to-mean ratio that the word "overdispersed" names; R1u and R2 are readings the audit added. Under R1 the statement "more than 80" is **true of the held alignment at W >= 1 Mb in all ten lineage-by-masking cells**: F2 at 1 Mb 89.4 (H), 89.5 (C), 88.3 (B), 85.1 (G), 253 (DHC); F0 136, 125, 123, 92.9, 826; larger at 3 and 10 Mb in every cell; DHC already from 30 kb (F0) and 300 kb (F2). **In none of the cells where it is true is the measured index anomalous**: in the 14 lineage-by-masking-by-W cells at W <= 1 Mb with an index of 80 or more, the class of the measured index over the eight parameter sets (112 set-cells) is CRITIC 37, MARGINAL-IN 61, BELOW-NEAR 14, none above its upper bound; index / N_hi runs from 0.11 to 0.91 (single lineages 0.11 to 0.77). At 3 and 10 Mb (20 further cells) the index is at or below its upper bound under PREREG, SOURCED and both ALL3 variants (index / N_hi 0.13 to 0.86); under the four Francioli-edge variants six cells are above N_hi (1.07 to 1.47, MARGINAL-OUT; section 4), none DAY. Proposed annotation for FM3 external, wording as R4-FM uses for FM5: **`supported` as a description, non-discriminating**. The window range where the number 80 would exceed every band by more than 3x (W <= 10 kb for single lineages) is an **extended reading**: Day released no window, and on alignable sequence the measured single-lineage index there is 1.4 to 10.4, nowhere near 80. It is recorded as UNTESTED as his claim (`unverifiable`, rule F). It is neither a credit to Day nor a failure of his statement.

| reading | whose | where "more than 80" is true of the held data | class where true / status | sets the field? |
|---|---|---|---|---|
| R1: D = Var / mean, normalised for aligned bases | the reading "overdispersed" selects | W >= 1 Mb, all ten lineage-by-masking cells (DHC from 30 kb F0, 300 kb F2) | measured index inside or below the band at W <= 1 Mb under all eight sets (index / N_hi 0.11 to 0.91); six cells MARGINAL-OUT at 3 to 10 Mb under the Francioli-edge variants; none DAY | **yes**: FM3 external `supported` as a description, non-discriminating |
| R1x: D - 1 > 80 | numerically R1 | same cells (smallest 85.1) | same | same as R1 |
| R1u: D on counts not normalised for aligned bases | audit's addition (A8) | from 300 kb for single lineages (H F0: 72 at 100 kb, 168 at 300 kb), from 30 kb to 100 kb for DHC | classes at the reproduced W: MARGINAL-IN, CRITIC or ALN-dependent; none DAY. At F2 the index largely measures the mask (section 9 item 7) | no; A8 bars it from scoring CRITIC alone |
| R2: SD ratio > 80, i.e. D > 6,400 | audit's addition | nowhere: the largest normalised SD ratio is 53.5 (DHC, F0, 10 Mb), 25.5 for a single lineage; unnormalised 75.4 (DHC, F2, 10 Mb) | as a number, 6,400 is DAY against every band at W <= 1 Mb (P3). Within 3x of it: one of ten cells in variance units, DHC only in SD units, where the class is MARGINAL-OUT (section 4) | no; neither side's credit (section 8, "Both") |
| R1 at W <= 10 kb (DHC at W <= 3 kb) | **extended reading** (a window Day did not state) | not true on alignable sequence: single lineages 1.4 to 10.4, DHC 2.2 to 20.6 | 80 as a number would be DAY in all six variants there; **UNTESTED** as his claim, `unverifiable` (rule F) | no (rule RD: extended readings cannot set the field) |
| TREE, PAIRS, BP units | audit's sub-readings of "substitution density across the genome" | not measurable on `fm_bins.npz` | UNTESTED; unsourced inputs | no |

**Lineage sharing (as prominent as the small-window point; no bracket enters it).** Q164 is as true of chimpanzee, bonobo and gorilla as of human. Repeat-masked single-copy sequence (F2):

| W | φ H | φ C | φ B | φ G | φ_H / φ_C | excess CV² H / C | corr(H, C) | corr(H, G) |
|---|---|---|---|---|---|---|---|---|
| 10 kb | 3.46 | 3.33 | 3.31 | 2.80 | 1.04 | 1.13 | 0.57 | 0.38 |
| 100 kb | 14.3 | 14.7 | 14.5 | 12.5 | 0.97 | 1.04 | 0.87 | 0.74 |
| 300 kb | 32.1 | 32.7 | 32.3 | 29.4 | 0.98 | 1.06 | 0.92 | 0.84 |
| 1 Mb | 89.4 | 89.5 | 88.3 | 85.1 | 1.00 | 1.07 | 0.96 | 0.92 |
| 3 Mb (144 windows) | 258 | 247 | 244 | 240 | 1.04 | 1.12 | 0.98 | 0.96 |

φ_H / φ_C is 0.97 to 1.04 at every W from 1 kb to 3 Mb (0.88 at 10 Mb, 22 windows); φ_H / φ_B 0.99 to 1.06. At the windows where the sentence is true, r² between the human and chimp window densities is 0.92 (1 Mb) to 0.96 (3 Mb), Poisson noise included. Q168 defines the proposed mechanism as writing "contiguous blocks of change into one dominate lineage"; an index equal to within 4% on three other lineages in the same windows is not evidence for a mechanism acting on one. Limits, stated: the scale-free excess CV² of H is above C's by 4% to 13% at every W up to 3 Mb, so "identical" would overstate; R4-FM notes that the hs1 = hg38 filter lowers H density; gorilla's excess CV² is 1.4 to 2.1 times lower than H's and 1.4 to 2.0 times lower than C's, so the odd lineage is gorilla. At F0 the lineages differ (100 kb: φ_H / φ_C 1.43, corr 0.52); R4-FM's mirror test identifies that F0 excess as a reference-projection effect (section 4).

## 1. Severity limit (ST-10), stated first

Finding ST-10 (`docs/research/criticality/severe-testing-2026-10-12.md`): "FMnull is a severe test of one outcome and a weak test of the other." A DAY class (80 above three times the neutral upper bound) is hard to reach by accident. A CRITIC class is cheap where the band is wide. The run confirms the asymmetry and adds two points.

| band width, (N_hi masked - 1) / (N_lo - 1) | 10 kb | 100 kb | 300 kb | 1 Mb |
|---|---|---|---|---|
| H, PREREG | 62 | 58 | 59 | 64 |
| H, SOURCED | 12 | 7.3 | 6.6 | 7.2 |
| H, AMENDED (six variants, min to max) | 9.7 to 46 | 5.1 to 39 | 3.7 to 35 | 2.6 to 29 |
| DHC, PREREG | 73 | 69 | 70 | 77 |
| DHC, SOURCED | 15 | 8.7 | 7.8 | 8.5 |
| DHC, AMENDED (six variants, min to max) | 12 to 55 | 6.1 to 46 | 4.4 to 41 | 3.1 to 35 |

(Post hoc, descriptive, from `amend2.table`.) Under PREREG the band spans a factor of about 60 to 75 at every W, so "inside" is the expected outcome in most worlds: a registered CRITIC under PREREG is **not discriminating**. Under SOURCED and the persistence-1.0 variants of AMENDED the band is 3 to 21 wide; the persistence-0.5 variants are 10 to 55 wide.

**Ratio used for "not discriminating" (fix pass, post hoc; a reporting convention of this write-up, not a rule change).** A CRITIC class is called not discriminating where the band width (N_hi - 1) / (N_lo - 1) exceeds 9, the width of the rule's own undecided zone (N_hi / 3 to 3 N_hi). Over the 20 masked cells H, C, G, DHC at 10 kb to 1 Mb the width exceeds 9 in 20 of 20 under PREREG (57 to 77) and under each persistence-0.5 variant (10 to 55), in 16 of 20 under ALL3 persistence 1.0 (7.4 to 21), 9 of 20 under NOWONG persistence 1.0 (3.7 to 17), 5 of 20 under SOURCED (6.6 to 15) and 4 of 20 under FRANC persistence 1.0 (2.6 to 12). **Which variants survive the data** (section 4): the narrow ones are the ones the measured cells contradict at the low edge (SOURCED 10 of 70 below N_lo; persistence 1.0: 5, 5 and 19 of 70); the variants with no low-edge failure are PREREG and the persistence-0.5 ones, i.e. exactly the sets whose every CRITIC is not discriminating by this ratio. "Inside under every set" is therefore carried by sets that are either contradicted at the bottom or too wide to exclude much. In the other direction, under SOURCED the central neutral simulation at 100 kb (φ_H 32.0) is itself MARGINAL-IN against the registered band (N_lo 11.0 at exposure 0.5, N_hi 73.8; CRITIC ceiling 27.9) and CRITIC only against the band at the simulation's own exposure (ceiling 39.1), where the BGS arm (43.4) is MARGINAL-IN; so the amended rule is not uniformly easy on the critic side either.

Share of the upper edge that is sourced (post hoc, descriptive; first-order CV² of each component at its upper corner, set SOURCED): the two components with a sourced sigma (M1, ILS) carry 46%, 50%, 57% and 66% of the masked upper edge at 10 kb, 100 kb, 300 kb and 1 Mb, and 27%, 25%, 33% and 48% of the unmasked one. The alignment term ALN (an artefact term, not an evolutionary process; no paper quantifies it, and R4-FM's mirror test measured an artefact of this class in-house, section 4) alone is 41%, 49%, 43% and 28% of the unmasked upper edge. Under PREREG the sourced share of the masked edge is 31% to 56%, and ALN is 34% to 54% of the unmasked edge.

The two added points. (a) The reproduction gate, meant to restore severity, has two parts and only one does any work. Its flag (REPRODUCED) is automatic for reading R1 when W is unknown: the measured index rises monotonically from about 2 to several hundred between 1 kb and 10 Mb in every lineage, so it passes within 3x of 80 at some W by construction. Its restriction ("only the classes at those W count") is decisive: it removes every small-W DAY class of R1. With W free, a gated DAY needs 80 > 3 N_hi at a W where the measured index is at least 26.7, i.e. the measured index itself above about N_hi; so "no reproduced cell is DAY" is implied by "no measured cell is above 3 N_hi" and is **not a second observation**. **Scope of the gate (accepted from the Day-side review):** the gate puts the audit's alignable subset in the place of Day's unreleased window. "The data" in every gate sentence means hs1-referenced core columns that also align to hg38 and orangutan: about 86% of autosomal 1-kb bins at F0 (R4-FM, Scope), with centromeric satellites, rDNA and CHM13-only sequence in no cell; F2 keeps under half of those windows. If Day's windows include that sequence, his index is not comparable with any number here. Small-W R1 cells therefore read **UNTESTED** (`unverifiable` until W is released, rule F), not "not reproduced". (b) The lineage-specificity criterion S2, which ST-10 says the write-up should lead with, cannot be met at 100 kb by the 2%-of-genome block model the check registered. For the "dominant" block model the ratio of φ_HC to the bound at lambda_M = 0, 0.25, 0.5 is 16.6, 5.3, 3.1 under PREREG and 16.6, 4.5, 2.6 under SOURCED / AMENDED when blocks sit on the window grid, and 11.7, 3.7, 2.2 and 11.7, 3.2, 1.8 at random phase (post hoc `simphase`, section 6). Since A9 lets S2 score DAY only above 3x the bound at every lambda_M, S2 as amended cannot fire at 100 kb even for a mechanism that triples the rate over half the genome on one lineage. That is a **defect of the audit's criteria**, recorded on Day's side (section 7): failing S2 says little, and "S2 unmet" is not counted against him.

Tree-incongruent sharing (S4), the other bracket-free statistic, was not measured by this script.

## 2. The lookup table

Bands are for the dispersion index D = Var(n_w) / mean(n_w) over equal windows (Poisson: D = 1). N_lo: all neutral components at the low corner, exposure c = 0.5, low end of the unit's divergence. N_hi masked: high corner, c = 1, high divergence. N_hi unmasked: N_hi masked plus the alignment term. K_hi: N_hi unmasked plus background selection (BGS). Divergence per unit: H 0.0051, C 0.0057, G 0.0077, DHC 0.0123 to 0.0146, TREE 0.03 to 0.15 (unsourced), PAIRS from the unsourced seven-ape tree (D_struct = 7.86), BP 0.13 to 0.14 gap-inclusive bp. Cells at W <= 30 kb are flagged `under_sourced_fine_scale`; every TREE and PAIRS cell is flagged `unsourced_tree`; every BP cell `unsourced_indel_tail`. "k" = thousands.

### 2a. REGISTERED (set PREREG)

| unit | edge | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | N_lo | 1.03 | 1.07 | 1.17 | 1.41 | 2 | 3.25 | 5.96 | 9.24 | 13.2 |
| H | N_hi masked | 2.78 | 5.45 | 11.5 | 24 | 59.4 | 134 | 321 | 672 | 1,244 |
| H | N_hi unmasked | 3.99 | 8.89 | 21.9 | 52 | 132 | 266 | 491 | 855 | 1,431 |
| H | K_hi | 4.02 | 8.98 | 22.2 | 52.8 | 135 | 272 | 510 | 896 | 1,498 |
| C | N_lo | 1.04 | 1.08 | 1.19 | 1.45 | 2.12 | 3.51 | 6.55 | 10.2 | 14.7 |
| C | N_hi masked | 2.99 | 5.97 | 12.7 | 26.7 | 66.3 | 150 | 358 | 751 | 1,391 |
| C | N_hi unmasked | 4.34 | 9.82 | 24.4 | 58 | 148 | 297 | 549 | 956 | 1,600 |
| C | K_hi | 4.37 | 9.92 | 24.7 | 58.9 | 150 | 304 | 570 | 1,001 | 1,674 |
| G | N_lo | 1.05 | 1.1 | 1.26 | 1.61 | 2.51 | 4.39 | 8.49 | 13.4 | 19.5 |
| G | N_hi masked | 3.68 | 7.71 | 16.8 | 35.7 | 89.2 | 202 | 484 | 1,015 | 1,878 |
| G | N_hi unmasked | 5.51 | 12.9 | 32.6 | 78.1 | 199 | 400 | 741 | 1,291 | 2,160 |
| G | K_hi | 5.56 | 13.1 | 33 | 79.3 | 203 | 411 | 770 | 1,352 | 2,262 |
| DHC | N_lo | 1.08 | 1.16 | 1.41 | 1.98 | 3.42 | 6.42 | 13 | 20.9 | 30.5 |
| DHC | N_hi masked | 6.09 | 13.7 | 31 | 66.9 | 168 | 382 | 916 | 1,923 | 3,561 |
| DHC | N_hi unmasked | 9.55 | 23.6 | 61 | 147 | 377 | 758 | 1,405 | 2,446 | 4,096 |
| DHC | K_hi | 9.64 | 23.9 | 61.8 | 149 | 384 | 778 | 1,458 | 2,563 | 4,287 |
| TREE | N_lo | 1.2 | 1.4 | 2 | 3.38 | 6.9 | 14.2 | 30.2 | 49.5 | 73 |
| TREE | N_hi masked | 53.3 | 132 | 309 | 678 | 1,720 | 3,920 | 9,406 | 20k | 37k |
| TREE | N_hi unmasked | 88.8 | 233 | 617 | 1,502 | 3,862 | 7,783 | 14k | 25k | 42k |
| TREE | K_hi | 89.8 | 236 | 625 | 1,526 | 3,934 | 7,979 | 15k | 26k | 44k |
| PAIRS-naive | N_lo | 10.3 | 12.7 | 20.1 | 37.1 | 80.2 | 170 | 366 | 603 | 891 |
| PAIRS-naive | N_hi masked | 246 | 604 | 1,411 | 3,092 | 7,840 | 18k | 43k | 90k | 167k |
| PAIRS-naive | N_hi unmasked | 408 | 1,066 | 2,815 | 6,849 | 18k | 35k | 66k | 114k | 192k |
| PAIRS-naive | K_hi | 412 | 1,078 | 2,852 | 6,955 | 18k | 36k | 68k | 120k | 201k |
| PAIRS-struct | N_lo | 1.31 | 1.62 | 2.56 | 4.72 | 10.2 | 21.6 | 46.6 | 76.6 | 113 |
| PAIRS-struct | N_hi masked | 31.3 | 76.8 | 179 | 393 | 997 | 2,272 | 5,451 | 11k | 21k |
| PAIRS-struct | N_hi unmasked | 51.9 | 136 | 358 | 871 | 2,238 | 4,510 | 8,359 | 15k | 24k |
| PAIRS-struct | K_hi | 52.4 | 137 | 363 | 884 | 2,280 | 4,624 | 8,678 | 15k | 26k |

### 2b. SOURCED

| unit | edge | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | N_lo | 1.13 | 1.36 | 2.12 | 4.22 | 11 | 26.9 | 59.9 | 88.3 | 103 |
| H | N_hi masked | 3.47 | 7.07 | 14.7 | 30 | 73.8 | 171 | 423 | 897 | 1,613 |
| H | N_hi unmasked | 4.81 | 10.8 | 25.7 | 59 | 149 | 305 | 598 | 1,084 | 1,804 |
| H | K_hi | 5.01 | 11.4 | 27.4 | 63.7 | 163 | 345 | 707 | 1,323 | 2,193 |
| C | N_lo | 1.15 | 1.4 | 2.26 | 4.6 | 12.1 | 30 | 66.8 | 98.5 | 115 |
| C | N_hi masked | 3.77 | 7.78 | 16.3 | 33.4 | 82.4 | 191 | 473 | 1,003 | 1,802 |
| C | N_hi unmasked | 5.25 | 11.9 | 28.6 | 65.8 | 166 | 341 | 668 | 1,212 | 2,016 |
| C | K_hi | 5.48 | 12.6 | 30.5 | 71.1 | 182 | 385 | 791 | 1,479 | 2,451 |
| G | N_lo | 1.2 | 1.54 | 2.7 | 5.87 | 16 | 40.1 | 89.9 | 133 | 155 |
| G | N_hi masked | 4.74 | 10.2 | 21.7 | 44.8 | 111 | 257 | 638 | 1,354 | 2,434 |
| G | N_hi unmasked | 6.75 | 15.8 | 38.3 | 88.6 | 224 | 460 | 902 | 1,636 | 2,723 |
| G | K_hi | 7.05 | 16.6 | 40.9 | 95.7 | 246 | 520 | 1,068 | 1,998 | 3,311 |
| DHC | N_lo | 1.31 | 1.86 | 3.71 | 8.78 | 25 | 63.5 | 143 | 211 | 248 |
| DHC | N_hi masked | 8.08 | 18.4 | 40.2 | 84 | 210 | 487 | 1,209 | 2,567 | 4,615 |
| DHC | N_hi unmasked | 11.9 | 29 | 71.8 | 167 | 424 | 872 | 1,709 | 3,102 | 5,162 |
| DHC | K_hi | 12.5 | 30.7 | 76.7 | 181 | 465 | 985 | 2,023 | 3,787 | 6,276 |
| TREE | N_lo | 1.76 | 3.09 | 7.61 | 20 | 59.6 | 153 | 347 | 514 | 602 |
| TREE | N_hi masked | 73.8 | 179 | 404 | 854 | 2,143 | 4,996 | 12k | 26k | 47k |
| TREE | N_hi unmasked | 113 | 289 | 729 | 1,707 | 4,343 | 8,952 | 18k | 32k | 53k |
| TREE | K_hi | 119 | 306 | 779 | 1,846 | 4,771 | 10k | 21k | 39k | 64k |
| PAIRS-naive | N_lo | 17.2 | 33.5 | 88.9 | 241 | 727 | 1,878 | 4,259 | 6,306 | 7,385 |
| PAIRS-naive | N_hi masked | 340 | 821 | 1,844 | 3,895 | 9,770 | 23k | 57k | 120k | 216k |
| PAIRS-naive | N_hi unmasked | 518 | 1,321 | 3,323 | 7,784 | 20k | 41k | 80k | 145k | 242k |
| PAIRS-naive | K_hi | 545 | 1,397 | 3,551 | 8,417 | 22k | 46k | 95k | 177k | 294k |
| PAIRS-struct | N_lo | 2.19 | 4.26 | 11.3 | 30.6 | 92.4 | 239 | 542 | 802 | 939 |
| PAIRS-struct | N_hi masked | 43.2 | 104 | 235 | 495 | 1,242 | 2,896 | 7,195 | 15k | 27k |
| PAIRS-struct | N_hi unmasked | 65.9 | 168 | 423 | 990 | 2,517 | 5,188 | 10k | 18k | 31k |
| PAIRS-struct | K_hi | 69.3 | 178 | 452 | 1,070 | 2,765 | 5,859 | 12k | 23k | 37k |

Model CV of the 1-Mb window-mean mutation rate (M0-M3 + CPG): PREREG 0.044 to 0.234, SOURCED 0.152 to 0.272, against Smith 2018's 0.15, 0.18, 0.27 (FML-S2). The amendment-1 hand figures (0.044, 0.232; 0.152, 0.270) are reproduced.

### 2c. AMENDED (envelope; calibration variants side by side)

N_lo takes four distinct values (dataset Jonsson or Francioli at the low edge, persistence 1.0 or 0.5); the range over the six variants is shown. N_hi takes two (Francioli for NOWONG and FRANC, Wong for ALL3). Full rows per variant are in `fmnull_analytic.json`, key `amend2.table`, label `AMENDED|<cal>|persist<p>|<unit>|<W>`.

| unit | edge | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | N_lo, min to max of six | 1.05 to 1.14 | 1.12 to 1.38 | 1.3 to 2.17 | 1.72 to 4.3 | 2.95 to 11.4 | 6.04 to 30.1 | 15.6 to 83.6 | 31.4 to 147 | 66.5 to 276 |
| H | N_hi masked, Francioli / Wong | 3.11 / 3.4 | 6.05 / 6.87 | 12.3 / 14.8 | 24.2 / 31.3 | 54.4 / 77.1 | 110 / 176 | 216 / 430 | 402 / 1,027 | 630 / 2,467 |
| H | N_hi unmasked, Francioli / Wong | 4.38 / 4.72 | 9.6 / 10.6 | 22.9 / 25.9 | 52.3 / 60.5 | 127 / 152 | 240 / 311 | 384 / 604 | 582 / 1,213 | 814 / 2,658 |
| H | K_hi, Francioli / Wong | 4.58 / 4.93 | 10.2 / 11.2 | 24.7 / 27.7 | 57.1 / 65.5 | 142 / 168 | 280 / 352 | 495 / 720 | 826 / 1,467 | 1,213 / 3,073 |
| C | N_lo, min to max of six | 1.06 to 1.16 | 1.13 to 1.43 | 1.33 to 2.3 | 1.81 to 4.69 | 3.17 to 12.6 | 6.63 to 33.6 | 17.3 to 93.4 | 35 to 165 | 74.2 to 308 |
| C | N_hi masked, Francioli / Wong | 3.36 / 3.69 | 6.64 / 7.56 | 13.6 / 16.4 | 26.9 / 34.8 | 60.7 / 86 | 123 / 196 | 241 / 480 | 450 / 1,147 | 704 / 2,757 |
| C | N_hi unmasked, Francioli / Wong | 4.78 / 5.16 | 10.6 / 11.7 | 25.5 / 28.8 | 58.3 / 67.5 | 142 / 170 | 268 / 347 | 429 / 675 | 650 / 1,356 | 910 / 2,971 |
| C | K_hi, Francioli / Wong | 5 / 5.39 | 11.2 / 12.3 | 27.4 / 30.8 | 63.7 / 73.1 | 158 / 187 | 313 / 394 | 554 / 805 | 923 / 1,639 | 1,355 / 3,434 |
| G | N_lo, min to max of six | 1.08 to 1.21 | 1.18 to 1.58 | 1.45 to 2.76 | 2.09 to 5.99 | 3.94 to 16.7 | 8.6 to 45 | 23 to 126 | 46.9 to 222 | 99.8 to 415 |
| G | N_hi masked, Francioli / Wong | 4.19 / 4.63 | 8.63 / 9.86 | 18.1 / 21.8 | 36 / 46.7 | 81.7 / 116 | 165 / 265 | 325 / 648 | 607 / 1,550 | 951 / 3,724 |
| G | N_hi unmasked, Francioli / Wong | 6.11 / 6.62 | 14 / 15.4 | 34.1 / 38.5 | 78.4 / 90.8 | 191 / 229 | 361 / 469 | 579 / 912 | 878 / 1,831 | 1,229 / 4,013 |
| G | K_hi, Francioli / Wong | 6.41 / 6.94 | 14.8 / 16.3 | 36.7 / 41.2 | 85.7 / 98.4 | 213 / 253 | 422 / 532 | 747 / 1,087 | 1,246 / 2,214 | 1,831 / 4,639 |
| DHC | N_lo, min to max of six | 1.13 to 1.34 | 1.29 to 1.92 | 1.72 to 3.81 | 2.74 to 8.97 | 5.69 to 26.1 | 13.1 to 71.3 | 36.1 to 200 | 74.3 to 354 | 159 to 663 |
| DHC | N_hi masked, Francioli / Wong | 7.05 / 7.88 | 15.5 / 17.8 | 33.4 / 40.5 | 67.4 / 87.7 | 154 / 219 | 313 / 501 | 615 / 1,228 | 1,150 / 2,937 | 1,802 / 7,061 |
| DHC | N_hi unmasked, Francioli / Wong | 10.7 / 11.7 | 25.6 / 28.4 | 63.8 / 72.1 | 148 / 171 | 361 / 434 | 684 / 888 | 1,097 / 1,727 | 1,664 / 3,471 | 2,329 / 7,608 |
| DHC | K_hi, Francioli / Wong | 11.3 / 12.3 | 27.3 / 30.1 | 68.7 / 77.3 | 162 / 186 | 404 / 478 | 799 / 1,007 | 1,416 / 2,059 | 2,362 / 4,197 | 3,470 / 8,795 |
| TREE | N_lo, min to max of six | 1.32 to 1.84 | 1.7 to 3.24 | 2.76 to 7.86 | 5.24 to 20.4 | 12.4 to 62.1 | 30.6 to 172 | 86.7 to 487 | 180 to 863 | 386 to 1,616 |
| TREE | N_hi masked, Francioli / Wong | 63.2 / 71.7 | 150 / 174 | 333 / 407 | 684 / 892 | 1,573 / 2,238 | 3,203 / 5,140 | 6,312 / 13k | 12k / 30k | 19k / 73k |
| TREE | N_hi unmasked, Francioli / Wong | 100 / 110 | 254 / 282 | 646 / 732 | 1,510 / 1,751 | 3,700 / 4,451 | 7,022 / 9,113 | 11k / 18k | 17k / 36k | 24k / 78k |
| TREE | K_hi, Francioli / Wong | 106 / 117 | 271 / 300 | 697 / 785 | 1,652 / 1,899 | 4,137 / 4,905 | 8,200 / 10k | 15k / 21k | 24k / 43k | 36k / 90k |
| PAIRS-naive | N_lo, min to max of six | 11.8 to 18.1 | 16.5 to 35.4 | 29.4 to 92 | 59.9 to 246 | 148 to 758 | 371 to 2,110 | 1,060 to 5,972 | 2,201 to 11k | 4,732 to 20k |
| PAIRS-naive | N_hi masked, Francioli / Wong | 291 / 330 | 685 / 794 | 1,523 / 1,858 | 3,119 / 4,066 | 7,171 / 10k | 15k / 23k | 29k / 57k | 54k / 137k | 84k / 331k |
| PAIRS-naive | N_hi unmasked, Francioli / Wong | 461 / 507 | 1,161 / 1,289 | 2,947 / 3,339 | 6,883 / 7,982 | 17k / 20k | 32k / 42k | 51k / 81k | 78k / 162k | 109k / 356k |
| PAIRS-naive | K_hi, Francioli / Wong | 488 / 535 | 1,237 / 1,369 | 3,178 / 3,580 | 7,530 / 8,655 | 19k / 22k | 37k / 47k | 66k / 96k | 111k / 196k | 162k / 412k |
| PAIRS-struct | N_lo, min to max of six | 1.5 to 2.31 | 2.1 to 4.5 | 3.74 to 11.7 | 7.62 to 31.3 | 18.9 to 96.4 | 47.2 to 268 | 135 to 759 | 280 to 1,345 | 602 to 2,520 |
| PAIRS-struct | N_hi masked, Francioli / Wong | 37 / 42 | 87.1 / 101 | 194 / 236 | 397 / 517 | 912 / 1,298 | 1,856 / 2,979 | 3,658 / 7,305 | 6,843 / 17k | 11k / 42k |
| PAIRS-struct | N_hi unmasked, Francioli / Wong | 58.6 / 64.4 | 148 / 164 | 375 / 425 | 875 / 1,015 | 2,144 / 2,580 | 4,070 / 5,281 | 6,527 / 10k | 9,901 / 21k | 14k / 45k |
| PAIRS-struct | K_hi, Francioli / Wong | 62.1 / 68 | 157 / 174 | 404 / 455 | 958 / 1,101 | 2,398 / 2,843 | 4,752 / 5,991 | 8,427 / 12k | 14k / 25k | 21k / 52k |
| BP-naive | N_lo, min to max of six | 62.4 to 64.6 | 64 to 70.7 | 68.6 to 90.7 | 79.4 to 145 | 111 to 326 | 189 to 804 | 432 to 2,167 | 836 to 3,794 | 1,729 to 7,059 |
| BP-naive | N_hi masked, Francioli / Wong | 1,057 / 1,065 | 1,138 / 1,160 | 1,309 / 1,378 | 1,636 / 1,830 | 2,466 / 3,087 | 3,987 / 5,796 | 6,889 / 13k | 12k / 29k | 18k / 69k |
| BP-naive | N_hi unmasked, Francioli / Wong | 1,092 / 1,101 | 1,235 / 1,261 | 1,601 / 1,681 | 2,407 / 2,632 | 4,451 / 5,152 | 7,552 / 9,504 | 12k / 18k | 17k / 34k | 23k / 74k |
| BP-naive | K_hi, Francioli / Wong | 1,097 / 1,107 | 1,251 / 1,278 | 1,648 / 1,731 | 2,540 / 2,770 | 4,859 / 5,576 | 8,651 / 11k | 15k / 21k | 24k / 41k | 34k / 85k |
| BP-struct | N_lo, min to max of six | 1 to 1 | 1 to 1.01 | 1.01 to 1.03 | 1.02 to 1.08 | 1.05 to 1.27 | 1.13 to 1.74 | 1.37 to 3.11 | 1.78 to 4.74 | 2.67 to 8.01 |
| BP-struct | N_hi masked, Francioli / Wong | 1.95 / 2.08 | 3.27 / 3.64 | 6.09 / 7.21 | 11.4 / 14.6 | 25.1 / 35.2 | 50 / 79.7 | 97.6 / 194 | 182 / 463 | 284 / 1,111 |
| BP-struct | N_hi unmasked, Francioli / Wong | 2.52 / 2.68 | 4.87 / 5.3 | 10.9 / 12.2 | 24.1 / 27.8 | 57.6 / 69.1 | 108 / 140 | 173 / 272 | 262 / 547 | 367 / 1,197 |
| BP-struct | K_hi, Francioli / Wong | 2.61 / 2.77 | 5.13 / 5.57 | 11.6 / 13 | 26.3 / 30 | 64.3 / 76.1 | 126 / 159 | 224 / 325 | 372 / 661 | 546 / 1,384 |

Other amendment-2 constants as run: Hobolth two-epoch centre E[T2] 2.71 My, sd 2.38 My, sigma 0.350, mean fraction 0.398 (hand: 2.71, 2.38, 0.35); ILS sigma upper 0.398; BGS sigma upper 0.154. U-BP structural floors D_struct >= 61.0 and >= 99.9, flagged upper edge 999. The two-locus ILS kernel gives a window-variance factor of 0.022 to 0.067 at 100 kb and 0.003 to 0.010 at 1 Mb. ALN is 35% to 50% of the unmasked upper excess at W <= 300 kb, 29% at 1 Mb and 7% at 10 Mb (ALL3).

## 3. Where the number 80 falls, by reading, unit and W (rule RD: every reading is tabulated; R1 sets the field, section 0)

These tables class the point value 80 (or 6,400) against the bands. Q164 is one-sided ("more than 80"), so where a table says BELOW at W >= 1 Mb his statement is true of the data there (the measured index is above 80) and the label says only that the null predicts as much or more.

Readings: **R1** D > 80. **R1x** D - 1 > 80 (differs from R1 in 10 of 648 table cells, all at class boundaries; not shown separately). **R1u** D > 80 on counts not normalised for alignable bases (amendment 2; exposure CV bracket 0.2 to 0.5, unsourced). **R2** SD ratio > 80, i.e. D > 6,400.

### 3a. REGISTERED classes for R1 (frozen rule: DAY > 3 N_hi; MARG = MARGINAL, N_hi to 3 N_hi; CRITIC inside; BELOW < N_lo). Cells: masked / unmasked

| unit | set | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| H | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | MARG / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW |
| C | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | MARG / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| C | SOURCED | DAY / DAY | DAY / DAY | DAY / MARG | MARG / MARG | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW |
| G | PREREG | DAY / DAY | DAY / DAY | DAY / MARG | MARG / MARG | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| G | SOURCED | DAY / DAY | DAY / DAY | DAY / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW |
| DHC | PREREG | DAY / DAY | DAY / DAY | MARG / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| DHC | SOURCED | DAY / DAY | DAY / MARG | MARG / MARG | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW |
| TREE | PREREG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| TREE | SOURCED | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW |
| PAIRS-naive | PREREG | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW |
| PAIRS-naive | SOURCED | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW |
| PAIRS-struct | PREREG | MARG / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW |
| PAIRS-struct | SOURCED | MARG / MARG | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW | BELOW / BELOW |

First W at which N_hi reaches 80 (below it 80 is above the band), masked / unmasked: PREREG H 158 kb / 56 kb, C 141 kb / 50 kb, G 89 kb / 32 kb, DHC 40 kb / 14 kb; SOURCED H 112 kb / 45 kb, C 100 kb / 40 kb, G 71 kb / 28 kb, DHC 28 kb / 12.6 kb (91-point log grid, steps of 12%). First W at which N_lo reaches 80 (beyond it 80 is below the band): never up to 31.6 Mb under PREREG for H, C, G, DHC; under SOURCED H 2.2 Mb, C 1.6 Mb, G 0.89 Mb, DHC 0.45 Mb.

### 3b. REGISTERED classes for R2 (D > 6,400). Cells: masked / unmasked

| unit | set | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY |
| H | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY |
| C | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY |
| C | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY |
| G | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / MARG |
| G | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | MARG / MARG |
| DHC | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / MARG | MARG / MARG |
| DHC | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | MARG / MARG | MARG / MARG |
| TREE | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| TREE | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | MARG / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| PAIRS-naive | PREREG | DAY / DAY | DAY / DAY | DAY / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| PAIRS-naive | SOURCED | DAY / DAY | DAY / DAY | DAY / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC | BELOW / BELOW |
| PAIRS-struct | PREREG | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / MARG | MARG / MARG | MARG / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |
| PAIRS-struct | SOURCED | DAY / DAY | DAY / DAY | DAY / DAY | DAY / DAY | DAY / MARG | MARG / MARG | CRITIC / CRITIC | CRITIC / CRITIC | CRITIC / CRITIC |

### 3c. AMENDED classes for R1 (consensus of the six calibration variants)

Classes: DAY > 3 N_hi; M-OUT = MARGINAL-OUT (N_hi to 3 N_hi); M-IN = MARGINAL-IN (inside, above max(N_hi / 3, N_c)); CRITIC; B-NEAR, B-FAR = BELOW-NEAR / BELOW-FAR. "CAL (…)" = CAL-DEPENDENT: the six variants disagree, the classes they give are listed, no verdict move. "ALN:" = ALN-DEPENDENT: in at least one variant the class against the unmasked band differs from the class against the masked band, so the outcome rests on the artefact term (not sourced from the literature; of the size R4-FM's mirror test measured) and moves no verdict. The consensus and the ALN flag are aggregated here from the per-variant classes in `amend2.classes` by the rule of amendment A2 / A5 (the script prints the per-variant classes; `score2` applies the same rule to one cell).

| unit | band | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | N masked | DAY | DAY | DAY | CAL (DAY, M-OUT) | M-OUT | M-IN | CAL (M-IN, CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-FAR) |
| H | N unmasked | DAY | DAY | DAY | ALN: M-OUT | ALN: M-IN | ALN: CAL (M-IN, CRITIC) | ALN: CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-FAR) |
| H | K_hi | DAY | DAY | CAL (DAY, M-OUT) | M-OUT | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-FAR) |
| C | N masked | DAY | DAY | DAY | M-OUT | CAL (M-OUT, M-IN) | M-IN | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-FAR) |
| C | N unmasked | DAY | DAY | ALN: CAL (DAY, M-OUT) | M-OUT | ALN: M-IN | ALN: CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-FAR) |
| C | K_hi | DAY | DAY | M-OUT | M-OUT | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-FAR) |
| G | N masked | DAY | DAY | DAY | M-OUT | M-IN | CAL (M-IN, CRITIC) | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) |
| G | N unmasked | DAY | DAY | ALN: M-OUT | ALN: CAL (M-OUT, M-IN) | M-IN | ALN: CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) |
| G | K_hi | DAY | DAY | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) |
| DHC | N masked | DAY | DAY | M-OUT | CAL (M-OUT, M-IN) | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) |
| DHC | N unmasked | DAY | ALN: CAL (DAY, M-OUT) | M-OUT | ALN: M-IN | ALN: CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) |
| DHC | K_hi | DAY | M-OUT | M-OUT | M-IN | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) |
| TREE | N masked | M-OUT | M-IN | CRITIC | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR |
| TREE | N unmasked | ALN: M-IN | ALN: CRITIC | CRITIC | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR |
| TREE | K_hi | M-IN | CRITIC | CRITIC | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR |
| PAIRS-naive | N masked | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-naive | N unmasked | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-naive | K_hi | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-struct | N masked | M-OUT | M-IN | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR |
| PAIRS-struct | N unmasked | M-OUT | M-IN | ALN: CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR |
| PAIRS-struct | K_hi | M-OUT | M-IN | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR |
| BP-naive | N masked | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR |
| BP-naive | N unmasked | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR |
| BP-naive | K_hi | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR |
| BP-struct | N masked | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC |
| BP-struct | N unmasked | DAY | DAY | DAY | ALN: CAL (DAY, M-OUT) | ALN: M-OUT | ALN: M-IN | ALN: CAL (M-IN, CRITIC) | ALN: CRITIC | CRITIC |
| BP-struct | K_hi | DAY | DAY | DAY | CAL (DAY, M-OUT) | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CRITIC |

### 3d. AMENDED classes for R1u

| unit | band | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | N masked | DAY | DAY | M-OUT | M-OUT | M-IN | CRITIC | B-NEAR | B-FAR | B-FAR |
| H | N unmasked | DAY | DAY | M-OUT | ALN: M-IN | ALN: CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR |
| H | K_hi | DAY | DAY | M-OUT | M-IN | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR |
| C | N masked | DAY | DAY | M-OUT | CAL (M-OUT, M-IN) | CAL (M-IN, CRITIC) | CRITIC | B-NEAR | B-FAR | B-FAR |
| C | N unmasked | DAY | DAY | M-OUT | ALN: M-IN | ALN: CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR |
| C | K_hi | DAY | DAY | M-OUT | M-IN | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR |
| G | N masked | DAY | DAY | M-OUT | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR |
| G | N unmasked | DAY | DAY | M-OUT | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR |
| G | K_hi | DAY | DAY | M-OUT | M-IN | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR |
| DHC | N masked | DAY | M-OUT | CAL (M-OUT, M-IN) | M-IN | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR |
| DHC | N unmasked | DAY | M-OUT | ALN: M-IN | ALN: CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR |
| DHC | K_hi | DAY | M-OUT | M-IN | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR |
| TREE | N masked | M-IN | CRITIC | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR |
| TREE | N unmasked | M-IN | CRITIC | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR |
| TREE | K_hi | M-IN | CRITIC | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (B-NEAR, B-FAR) | B-FAR | B-FAR | B-FAR |
| PAIRS-naive | N masked | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-naive | N unmasked | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-naive | K_hi | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-struct | N masked | M-OUT | M-IN | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-struct | N unmasked | ALN: M-IN | ALN: CRITIC | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR |
| PAIRS-struct | K_hi | M-IN | CRITIC | CRITIC | CRITIC | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR |
| BP-naive | N masked | CRITIC | CRITIC | B-NEAR | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR |
| BP-naive | N unmasked | CRITIC | CRITIC | B-NEAR | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR |
| BP-naive | K_hi | CRITIC | CRITIC | B-NEAR | B-NEAR | B-FAR | B-FAR | B-FAR | B-FAR | B-FAR |
| BP-struct | N masked | DAY | DAY | DAY | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CRITIC | CRITIC |
| BP-struct | N unmasked | DAY | DAY | DAY | M-OUT | M-IN | ALN: CRITIC | CRITIC | CRITIC | CRITIC |
| BP-struct | K_hi | DAY | DAY | DAY | M-OUT | M-IN | CRITIC | CRITIC | CRITIC | CRITIC |

### 3e. AMENDED classes for R2

| unit | band | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| H | N masked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| H | N unmasked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| H | K_hi | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| C | N masked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| C | N unmasked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| C | K_hi | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| G | N masked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| G | N unmasked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) |
| G | K_hi | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) | CAL (DAY, M-OUT) |
| DHC | N masked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) | CAL (DAY, M-IN) |
| DHC | N unmasked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) | ALN: CAL (M-OUT, M-IN) |
| DHC | K_hi | DAY | DAY | DAY | DAY | DAY | DAY | DAY | M-OUT | CAL (M-OUT, M-IN) |
| TREE | N masked | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) | M-OUT | CAL (M-OUT, M-IN) | CAL (M-IN, CRITIC) | CAL (M-IN, CRITIC) |
| TREE | N unmasked | DAY | DAY | DAY | DAY | ALN: M-OUT | ALN: M-IN | ALN: M-IN | CAL (M-IN, CRITIC) | ALN: CRITIC |
| TREE | K_hi | DAY | DAY | DAY | DAY | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CRITIC |
| PAIRS-naive | N masked | DAY | DAY | DAY | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) |
| PAIRS-naive | N unmasked | DAY | DAY | ALN: M-OUT | ALN: M-IN | ALN: CAL (M-IN, CRITIC) | ALN: CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) |
| PAIRS-naive | K_hi | DAY | DAY | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CRITIC | CAL (CRITIC, B-NEAR) | CAL (CRITIC, B-NEAR, B-FAR) |
| PAIRS-struct | N masked | DAY | DAY | DAY | DAY | DAY | CAL (DAY, M-OUT) | CAL (M-OUT, M-IN) | M-IN | CAL (M-IN, CRITIC) |
| PAIRS-struct | N unmasked | DAY | DAY | DAY | DAY | ALN: M-OUT | ALN: M-OUT | ALN: M-IN | ALN: CAL (M-IN, CRITIC) | CAL (M-IN, CRITIC) |
| PAIRS-struct | K_hi | DAY | DAY | DAY | DAY | M-OUT | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC |
| BP-naive | N masked | DAY | DAY | DAY | DAY | M-OUT | M-OUT | M-IN | CAL (M-IN, CRITIC) | CAL (M-IN, CRITIC, B-NEAR) |
| BP-naive | N unmasked | DAY | DAY | DAY | ALN: M-OUT | M-OUT | ALN: M-IN | M-IN | ALN: CAL (M-IN, CRITIC) | ALN: CAL (CRITIC, B-NEAR) |
| BP-naive | K_hi | DAY | DAY | DAY | M-OUT | M-OUT | M-IN | CAL (M-IN, CRITIC) | CRITIC | CAL (CRITIC, B-NEAR) |
| BP-struct | N masked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY |
| BP-struct | N unmasked | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY |
| BP-struct | K_hi | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY | DAY |

### 3f. In words

- **DAY** (80 is more than three times every neutral upper bound, all six variants, masked band): R1 with a single-lineage unit (H, C, G) at W <= 10 kb; R1 with DHC at W <= 3 kb; R1 with BP-struct at W <= 30 kb; R2 with H, C or G at every W <= 3 Mb and with DHC at W <= 1 Mb. Against the known-mechanisms band K_hi the R1 region loses one grid step (H: DAY at <= 3 kb, CAL-DEPENDENT at 10 kb). All W <= 30 kb cells are flagged under-sourced at the fine scale.
- **MARGINAL** (undecidable): R1, single lineage, about 30 kb to 300 kb (M-OUT at 30 to 100 kb, M-IN at 100 to 300 kb, with CAL-DEPENDENT cells between); DHC 10 kb to 100 kb.
- **CRITIC** as a clean consensus (not CAL- or ALN-dependent): R1 with DHC at 300 kb (masked and unmasked); R1 with TREE at 10 kb to 100 kb; PAIRS-naive and BP-naive at 1 to 3 kb; PAIRS-struct at 30 kb; BP-struct at 10 Mb. For the single-lineage units H, C and G **no W gives a clean CRITIC consensus against the masked band under R1**: the cells are M-IN, CAL-DEPENDENT or, unmasked, ALN-DEPENDENT. **On A4's separate anomaly question ("is 80 high?") the six variants agree at W >= 1 Mb** (fix pass, post hoc): in 11 of the 12 masked cells H, C, G, DHC at 1, 3 and 10 Mb every variant gives CRITIC, B-NEAR or B-FAR, i.e. NOT-HIGH in all six; the exception is H at 1 Mb (M-IN in one variant). The variants disagree there only on whether the null predicts about 80 or more than 80. At 30 to 300 kb the class is MARGINAL. A4 also says BELOW-FAR gives no defeater credit against FM10, and a null that over-predicts is weakened at neighbouring W; no CRITIC is scored from this.
- **BELOW** (80 under the neutral lower bound; "not high" for the critic, a bracket failure at the low edge for Day): R1 at W >= 1 Mb in at least one variant for every unit (CAL-DEPENDENT), and for PAIRS-naive and BP-naive at much smaller W: on those two unit readings the neutral lower bound itself is above 80 (in every variant from 100 kb for both: the smallest N_lo over the six variants at 100 kb is 148 for PAIRS-naive and 111 for BP-naive; BELOW-FAR in every variant from 300 kb and 1 Mb; in some variants from 10 kb). For H, C, G and DHC the one-sided statement "more than 80" is true of the data at these W (section 0).
- Under the REGISTERED rule the same picture is coarser: under PREREG, R1 is DAY at small W (to 3 kb for DHC, 10 to 30 kb for single lineages), MARGINAL for one or two grid steps and CRITIC above that (from 30 kb for DHC unmasked to 300 kb for H and C masked); under SOURCED the CRITIC range is closed at the top (BELOW from 3 Mb for H and C, 1 Mb for G and DHC). R2 is DAY at every W <= 1 Mb for H, C, G and DHC under both sets.

## 4. The real-data arm, and the reproduction gate

Same per-1-kb bin file as R4-FM (`fm_bins.npz`, md5 716db19e…7a5ff98c, hs1-referenced; scope as in R4-FM: only hg38- and orangutan-alignable CHM13 sequence). F0 = all core columns; F2 = no paralogous rows, no soft-masked repeats. Autosomes. φ is the exposure-weighted index of R4-FM; φ_cov is φ after a log-linear regression on GC, hs1 != hg38 rate and the repeat / CpG / dup class fractions.

| filter | quantity | 1 kb | 3 kb | 10 kb | 30 kb | 100 kb | 300 kb | 1 Mb | 3 Mb | 10 Mb |
|---|---|---|---|---|---|---|---|---|---|---|
| F0 | windows k | 2,501,091 | 847,452 | 258,327 | 87,492 | 26,386 | 8,821 | 2,648 | 875 | 258 |
| F0 | exposure c | 0.97 | 0.95 | 0.94 | 0.92 | 0.92 | 0.92 | 0.91 | 0.91 | 0.90 |
| F0 | φ H | 3.25 | 5.84 | 10.4 | 18.7 | 36.9 | 70 | 136 | 272 | 576 |
| F0 | φ C | 2.59 | 4.14 | 7.32 | 12.9 | 25.7 | 53.4 | 125 | 282 | 649 |
| F0 | φ B | 2.49 | 3.98 | 7.16 | 12.4 | 25.7 | 52.7 | 123 | 277 | 642 |
| F0 | φ G | 2.07 | 3.23 | 5.86 | 11 | 18.4 | 38.1 | 92.9 | 218 | 497 |
| F0 | φ DHC | 9.51 | 20.6 | 44.7 | 90.7 | 210 | 454 | 826 | 1,405 | 2,861 |
| F0 | φ_cov H | 3.84 | 8.27 | 13.9 | 22.2 | 40.1 | 68.3 | 113 | 182 | 323 |
| F0 | φ_cov DHC | 4.09 | 7.68 | 15.2 | 29.4 | 62.2 | 129 | 256 | 424 | 710 |
| F0 | D unnormalised, all windows, H | 3.69 | 7.04 | 14.7 | 30.5 | 72.2 | 168 | 443 | 1,123 | 2,873 |
| F0 | D unnormalised, all windows, C | 3.13 | 5.61 | 11.6 | 24.3 | 61.1 | 153 | 435 | 1,138 | 2,937 |
| F0 | D unnormalised, all windows, G | 2.86 | 5.29 | 11.6 | 26.3 | 69.8 | 181 | 534 | 1,438 | 3,748 |
| F0 | D unnormalised, all windows, DHC | 9.83 | 21.2 | 47.9 | 101 | 241 | 534 | 1,215 | 2,551 | 5,305 |
| F0 | CV_c (used / all windows) | 0.08 / 0.38 | 0.10 / 0.36 | 0.10 / 0.33 | 0.09 / 0.31 | 0.08 / 0.30 | 0.07 / 0.29 | 0.07 / 0.28 | 0.06 / 0.27 | 0.08 / 0.25 |
| F0 | excess CV, H (sqrt of cv2_excess) | 0.673 | 0.575 | 0.443 | 0.353 | 0.276 | 0.221 | 0.170 | 0.139 | 0.112 |
| F0 | excess CV, G | 0.379 | 0.319 | 0.260 | 0.216 | 0.157 | 0.132 | 0.114 | 0.102 | 0.085 |
| F0 | corr(H, C) / corr(H, G) | 0.17 / 0.09 | 0.24 / 0.13 | 0.33 / 0.20 | 0.42 / 0.29 | 0.52 / 0.39 | 0.62 / 0.52 | 0.77 / 0.69 | 0.85 / 0.79 | 0.93 / 0.87 |
| F0 | φ_HC | 1.31 | 1.74 | 2.72 | 4.5 | 8.54 | 14.8 | 24.1 | 34 | 37.6 |
| F2 | windows k | 1,214,608 | 409,456 | 116,826 | 35,635 | 9,520 | 2,761 | 626 | 144 | 22 |
| F2 | exposure c | 0.77 | 0.70 | 0.64 | 0.61 | 0.58 | 0.56 | 0.54 | 0.52 | 0.51 |
| F2 | φ H | 1.6 | 2.14 | 3.46 | 6.34 | 14.3 | 32.1 | 89.4 | 258 | 269 |
| F2 | φ C | 1.61 | 2.11 | 3.33 | 6.26 | 14.7 | 32.7 | 89.5 | 247 | 306 |
| F2 | φ B | 1.6 | 2.1 | 3.31 | 6.19 | 14.5 | 32.3 | 88.3 | 244 | 293 |
| F2 | φ G | 1.42 | 1.8 | 2.8 | 5.3 | 12.5 | 29.4 | 85.1 | 240 | 272 |
| F2 | φ DHC | 2.25 | 3.57 | 7.01 | 15 | 38 | 89.1 | 253 | 730 | 875 |
| F2 | φ_cov H | 1.56 | 2.09 | 3.33 | 5.83 | 11.5 | 21.2 | 36 | 56.2 | 123 |
| F2 | φ_cov DHC | 3.75 | 3.33 | 6.28 | 12.3 | 25.7 | 47.6 | 81.1 | 123 | 269 |
| F2 | D unnormalised, all windows, H | 2.98 | 5.13 | 10.3 | 21.5 | 55.1 | 136 | 368 | 910 | 2,289 |
| F2 | D unnormalised, all windows, C | 3.13 | 5.38 | 10.7 | 22.6 | 58.4 | 146 | 396 | 984 | 2,488 |
| F2 | D unnormalised, all windows, G | 3.49 | 6.26 | 12.9 | 27.8 | 72.6 | 182 | 491 | 1,219 | 3,097 |
| F2 | D unnormalised, all windows, DHC | 5.59 | 10.7 | 23.2 | 50.8 | 134 | 337 | 916 | 2,272 | 5,692 |
| F2 | CV_c (used / all windows) | 0.20 / 0.88 | 0.18 / 0.75 | 0.15 / 0.62 | 0.13 / 0.53 | 0.10 / 0.47 | 0.08 / 0.43 | 0.06 / 0.38 | 0.04 / 0.35 | 0.03 / 0.32 |
| F2 | excess CV, H (sqrt of cv2_excess) | 0.399 | 0.335 | 0.280 | 0.246 | 0.216 | 0.193 | 0.180 | 0.179 | 0.102 |
| F2 | excess CV, G | 0.277 | 0.232 | 0.200 | 0.183 | 0.168 | 0.154 | 0.146 | 0.144 | 0.085 |
| F2 | corr(H, C) / corr(H, G) | 0.20 / 0.11 | 0.35 / 0.20 | 0.57 / 0.38 | 0.74 / 0.57 | 0.87 / 0.74 | 0.92 / 0.84 | 0.96 / 0.92 | 0.98 / 0.96 | 0.98 / 0.93 |
| F2 | φ_HC | 1.11 | 1.2 | 1.33 | 1.51 | 1.81 | 2.3 | 3.49 | 5.43 | 6.16 |

Notes. F2 at 3 Mb and 10 Mb has 144 and 22 windows: those two columns are noisy. The four W shared with R4-FM (1 kb, 10 kb, 100 kb, 1 Mb) reproduce its φ to the printed digits (H at F0: 3.25, 10.4, 36.9, 136).

**W at which the measured index reaches 80** (log-log interpolation on the nine-point grid, `W_T`): F0 H 382 kb, C 531 kb, B 543 kb, G 817 kb, DHC 24.7 kb; F2 H 877 kb, C 875 kb, B 889 kb, G 933 kb, DHC 261 kb. No lineage reaches 6,400 at any W up to 10 Mb (largest measured: DHC F0 2,861 at 10 Mb; H F0 576).

**Measured index against the bands, each cell with its own exposure and density** (mode `post`, 70 cells: F0 and F2, seven W from 1 kb to 1 Mb, five lineages; informed, not predictive):

| set / variant | CRITIC | MARGINAL-IN | MARGINAL-OUT | DAY | BELOW-NEAR | inside (CRITIC + M-IN) | **clean inside** (post hoc) | **ALN-dependent** F0 cells, of 35 (post hoc) | F0 cells above the masked-equivalent bound (post hoc) | **F2 against the masked band**: at or below N_hi; inside; largest φ / N_hi (post hoc) |
|---|---|---|---|---|---|---|---|---|---|---|
| PREREG | 23 | 46 | 1 | 0 | 0 | 69 / 70 | 46 / 70 | 23 | 9 | 35 / 35; 35; 0.69 |
| SOURCED | 45 | 15 | 0 | 0 | 10 | 60 / 70 | 50 / 70 | 10 | 6 | 35 / 35; 30; 0.57 |
| AMENDED ALL3, persist 1.0 | 48 | 17 | 0 | 0 | 5 | 65 / 70 | 54 / 70 | 11 | 6 | 35 / 35; 33; 0.58 |
| AMENDED ALL3, persist 0.5 | 38 | 32 | 0 | 0 | 0 | 70 / 70 | 54 / 70 | 16 | 6 | 35 / 35; 35; 0.58 |
| AMENDED NOWONG, persist 1.0 | 41 | 24 | 0 | 0 | 5 | 65 / 70 | 49 / 70 | 16 | 9 | 35 / 35; 33; 0.91 |
| AMENDED NOWONG, persist 0.5 | 23 | 47 | 0 | 0 | 0 | 70 / 70 | 47 / 70 | 23 | 9 | 35 / 35; 35; 0.91 |
| AMENDED FRANC, persist 1.0 | 34 | 17 | 0 | 0 | 19 | 51 / 70 | 39 / 70 | 12 | 9 | 35 / 35; 24; 0.91 |
| AMENDED FRANC, persist 0.5 | 24 | 46 | 0 | 0 | 0 | 70 / 70 | 47 / 70 | 23 | 9 | 35 / 35; 35; 0.91 |

The four right-hand columns apply rule A5 to the measured cells (fix pass, `fixpass` section C). An F0 cell is ALN-dependent if its class against the unmasked band differs from its class against N_hi minus ALN_part (the masked-equivalent bound); "clean inside" counts F2 cells that are inside and F0 cells that are inside under both. **Headline comparison: F2 against the masked band**, where the alignment term does not enter: 35 of 35 cells are at or below N_hi in every set (largest φ / N_hi 0.57 to 0.91; single lineages 0.57 to 0.77), and 24 to 35 are inside, the rest below N_lo. **F0 counts are ALN-dependent for both sides**: 10 to 23 of the 35 F0 cells per set change class with the alignment term, and 6 to 9 are above the masked-equivalent bound (none above three times it). R4-FM's mirror test measured what that F0 excess is. With chimp as the reference in place of hs1, at 100 kb φ_C goes from 25.7 to 127.6 and φ_HC from 8.54 to 18.0 while φ_H stays at 36.9 / 34.9; F1 (paralogous rows removed) and F2 do not move (φ_HC 2.71 / 2.90 and 1.81 / 1.85). R4-FM, M1: "the F0 excess follows the reference". So the unmasked F0 excess is a reference-projection effect; it is evidence for neither side (A5), neither generosity to the null nor a residual Day can claim.

- **No measured cell is DAY under any set, on a test with little power against block mechanisms below the dominant one** (section 6a: every planted non-dominant block scenario also scores CRITIC or MARGINAL-IN, while the dominant one scores DAY at 100 kb against the masked band). One cell is above its upper bound: DHC, F0, 1 kb under PREREG (φ 9.5 against 8.8, ratio 1.09). The largest ratio φ / N_hi under any AMENDED variant is 0.97 (the same cell, NOWONG).
- **3 Mb and 10 Mb** (not in `post`; fix pass, same construction, `fixpass` section D; 20 cells: F0 and F2, two W, five lineages). Under PREREG, SOURCED and both ALL3 variants all 20 are at or below N_hi (φ / N_hi 0.13 to 0.86). Under the four Francioli-edge variants (NOWONG, FRANC) **six cells are above N_hi, none DAY**: F2 at 3 Mb H 1.22, C 1.09, B 1.07, DHC 1.43; F2 DHC at 10 Mb 1.14; F0 DHC at 10 Mb 1.47 (F0 DHC at 3 Mb is at 1.00). This is a finding of the critic-side review against the critics' side: "at any W" does not hold for the Francioli edge at 3 to 10 Mb. Riders: the excess is shared (chimp 1.09 beside human 1.22; corr(H, C) 0.98 at 3 Mb), F2 has 144 and 22 windows there, and the Francioli M0 term at these scales is derived from a slope and inverted at 10 Mb (section 9 items 2 and 9), so it reads as a band too narrow there, not as a lineage-specific anomaly.
- **Low edge: the pedigree-calibrated bound exceeds the data** (both A4 labels below). Under SOURCED, 10 cells fall below N_lo, 8 of them gorilla (F2 at 10 kb to 1 Mb; F0 at 100 kb to 1 Mb). Under FRANC with persistence 1.0, 19 cells do (all four single lineages at 300 kb and 1 Mb in F2, among others). The lower bound calibrated on pedigree mutation data over-predicts the dispersion of divergence at W >= 100 kb. The measured excess CV of the 1-Mb window mean, all processes together, is 0.17 to 0.18 for H and 0.11 to 0.15 for G, against 0.15, 0.18 and 0.27 for de novo mutations alone in Smith's three datasets. All BELOW cells disappear at persistence 0.5. A4 gives this two labels and both are reported. *Calibration question (Day-side): bracket failure.* A present-day human pedigree CV is used as a floor for every lineage's divergence CV, and the data fall under it; the clear cells are the own-exposure ones (G, F0: 38.1 against N_lo 72.7 at 300 kb; 92.9 against 163.5 at 1 Mb); a model that is wrong at the bottom is weaker evidence when it says "inside" at a neighbouring W. *Anomaly question (critic-side): NOT-HIGH, a fortiori.* **The sourced pedigree CV alone matches the measured megabase dispersion**: FML-S2 gives a CV of 0.15, 0.18 and 0.27 for de novo mutations at 1 Mb in three human datasets, and the measured excess CV of divergence at 1 Mb, all processes together, is 0.170 / 0.180 (H, F0 / F2), 0.154 / 0.174 (C), 0.152 / 0.172 (B) and 0.114 / 0.146 (G). So the regional variation of the mutation rate observed directly in human families is as large as, or larger than, all the regional variation in single-lineage divergence at the window where Q164 is true, before gBGC, ILS, BGS or any artefact is added; a uniform rate is not the neutral expectation. Limits: one species' pedigrees; Wong's 0.27 may be technical (Smith's abstract); the CV is of mutation, and its persistence over about 6 My is not sourced (that divergence is somewhat less dispersed than pedigree mutation is what FML-S8 reports qualitatively); below 1 Mb the low edge rests on the unsourced ell of M1, not on Smith.
- **DHC at F0 is inside only through the alignment term** (post hoc, descriptive, from `post.cells`): at every W from 1 kb to 300 kb in all eight sets, and at 1 Mb in five of eight (four of six AMENDED), the measured DHC φ exceeds N_hi minus ALN_part (φ over that bound 1.06 to 1.70 at 1 kb to 300 kb; e.g. 100 kb: φ 210, masked-equivalent bound 132 to 187, unmasked bound 309 to 372). For H the same holds only at 1 to 3 kb, in five of eight sets. So "unmasked DHC is unremarkable" rests on an artefact term that no paper quantifies (sigma bracket 0.016 to 0.42) and that R4-FM measured in-house by changing the reference (M1, numbers above the bullets): removing paralogous rows alone (F1) takes DHC from 210 to 49.3 at 100 kb, 44.7 to 11.3 at 10 kb and 826 to 291 at 1 Mb, and with repeats removed as well (F2) DHC is inside without the term (100 kb: φ 38). These cells are ALN-DEPENDENT (A5) and count for neither side.

**Reproduction gate** (amendment A7; W unknown, so "REPRODUCED" means the measured index is within [1/3, 3] x Day's value at some measured W, and only classes at those W count; "measured" means on the audit's alignable subset, section 1 (a); the table is as coded, in variance units). Bonobo has no registered unit; the chimp band is shown for it. R1x gives the same gate as R1 except that G masked also passes at 3 Mb.

| reading | unit | masking | gate | W where the measured index is within 3x | AMENDED consensus at those W | registered class at the gated W, PREREG / SOURCED (hybrid: the gate is amendment 2) |
|---|---|---|---|---|---|---|
| R1 | H | unmasked | REPRODUCED (max measured 576) | 100 kb, 300 kb, 1 Mb | 100 kb: ALN: M-IN; 300 kb: ALN: CAL (M-IN, CRITIC); 1 Mb: ALN: CAL (CRITIC, B-NEAR) | 100 kb: CRITIC / CRITIC; 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / CRITIC |
| R1 | H | masked | REPRODUCED (max measured 269) | 300 kb, 1 Mb | 300 kb: M-IN; 1 Mb: CAL (M-IN, CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / CRITIC |
| R1 | C | unmasked | REPRODUCED (max measured 649) | 300 kb, 1 Mb | 300 kb: ALN: CRITIC; 1 Mb: CAL (CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / CRITIC |
| R1 | C | masked | REPRODUCED (max measured 306) | 300 kb, 1 Mb | 300 kb: M-IN; 1 Mb: CAL (CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / CRITIC |
| R1 | B (C band) | unmasked | REPRODUCED (max measured 642) | 300 kb, 1 Mb | 300 kb: ALN: CRITIC; 1 Mb: CAL (CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / CRITIC |
| R1 | B (C band) | masked | REPRODUCED (max measured 293) | 300 kb, 1 Mb | 300 kb: M-IN; 1 Mb: CAL (CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / CRITIC |
| R1 | G | unmasked | REPRODUCED (max measured 497) | 300 kb, 1 Mb, 3 Mb | 300 kb: ALN: CRITIC; 1 Mb: CAL (CRITIC, B-NEAR); 3 Mb: CAL (CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / BELOW; 3 Mb: CRITIC / BELOW |
| R1 | G | masked | REPRODUCED (max measured 272) | 300 kb, 1 Mb | 300 kb: CAL (M-IN, CRITIC); 1 Mb: CAL (CRITIC, B-NEAR) | 300 kb: CRITIC / CRITIC; 1 Mb: CRITIC / BELOW |
| R1 | DHC | unmasked | REPRODUCED (max measured 2,861) | 10 kb, 30 kb, 100 kb | 10 kb: M-OUT; 30 kb: ALN: M-IN; 100 kb: ALN: CRITIC | 10 kb: MARGINAL / MARGINAL; 30 kb: CRITIC / CRITIC; 100 kb: CRITIC / CRITIC |
| R1 | DHC | masked | REPRODUCED (max measured 875) | 100 kb, 300 kb | 100 kb: M-IN; 300 kb: CRITIC | 100 kb: CRITIC / CRITIC; 300 kb: CRITIC / CRITIC |
| R1u | H | unmasked | REPRODUCED (max measured 2,873) | 30 kb, 100 kb, 300 kb | 30 kb: ALN: M-IN; 100 kb: ALN: CRITIC; 300 kb: CRITIC | not a registered reading |
| R1u | H | masked | REPRODUCED (max measured 2,289) | 100 kb, 300 kb | 100 kb: M-IN; 300 kb: CRITIC | not a registered reading |
| R1u | C | unmasked | REPRODUCED (max measured 2,937) | 100 kb, 300 kb | 100 kb: ALN: CRITIC; 300 kb: CRITIC | not a registered reading |
| R1u | C | masked | REPRODUCED (max measured 2,488) | 100 kb, 300 kb | 100 kb: CAL (M-IN, CRITIC); 300 kb: CRITIC | not a registered reading |
| R1u | B (C band) | unmasked | REPRODUCED (max measured 2,942) | 100 kb, 300 kb | 100 kb: ALN: CRITIC; 300 kb: CRITIC | not a registered reading |
| R1u | B (C band) | masked | REPRODUCED (max measured 2,485) | 100 kb, 300 kb | 100 kb: CAL (M-IN, CRITIC); 300 kb: CRITIC | not a registered reading |
| R1u | G | unmasked | REPRODUCED (max measured 3,748) | 100 kb, 300 kb | 100 kb: CRITIC; 300 kb: CAL (CRITIC, B-NEAR) | not a registered reading |
| R1u | G | masked | REPRODUCED (max measured 3,097) | 30 kb, 100 kb, 300 kb | 30 kb: M-IN; 100 kb: CRITIC; 300 kb: CAL (CRITIC, B-NEAR) | not a registered reading |
| R1u | DHC | unmasked | REPRODUCED (max measured 5,305) | 10 kb, 30 kb | 10 kb: ALN: M-IN; 30 kb: ALN: CRITIC | not a registered reading |
| R1u | DHC | masked | REPRODUCED (max measured 5,692) | 30 kb, 100 kb | 30 kb: M-IN; 100 kb: CRITIC | not a registered reading |
| R2 | H | unmasked | NOT-REPRODUCED (max measured 576) | none | none | none |
| R2 | H | masked | NOT-REPRODUCED (max measured 269) | none | none | none |
| R2 | C | unmasked | NOT-REPRODUCED (max measured 649) | none | none | none |
| R2 | C | masked | NOT-REPRODUCED (max measured 306) | none | none | none |
| R2 | B (C band) | unmasked | NOT-REPRODUCED (max measured 642) | none | none | none |
| R2 | B (C band) | masked | NOT-REPRODUCED (max measured 293) | none | none | none |
| R2 | G | unmasked | NOT-REPRODUCED (max measured 497) | none | none | none |
| R2 | G | masked | NOT-REPRODUCED (max measured 272) | none | none | none |
| R2 | DHC | unmasked | REPRODUCED (max measured 2,861) | 10 Mb | 10 Mb: ALN: CAL (M-OUT, M-IN) | 10 Mb: MARGINAL / MARGINAL |
| R2 | DHC | masked | NOT-REPRODUCED (max measured 875) | none | none | none |

- **R1: REPRODUCED for every lineage and both maskings**, at 100 kb to 1 Mb for single lineages (to 3 Mb for G unmasked) and at 10 kb to 300 kb for DHC. As section 1 notes, with W free this is close to automatic.
- **R1u: REPRODUCED for every lineage**, at 10 kb to 300 kb. The unnormalised index over all windows is 1.03 (DHC, F0, 3 kb) to 11.4 (G, F2, 10 Mb) times the normalised φ and reaches 80 at smaller W (H, F0: 72 at 100 kb and 168 at 300 kb, against φ 37 and 70).
- **R2, in both unit conventions** (A7's text does not fix the unit; the code compares the index with 6,400; the second and third rows are fix-pass additions, post hoc, `fixpass` section F):

| convention | normalised φ | unnormalised index (R2 with R1u's normalisation; not a registered combination) |
|---|---|---|
| variance units, as coded: index within [2,133, 19,200] | 1 of 10 lineage-by-masking cells: DHC F0 at 10 Mb (2,861). No single lineage at any W up to 10 Mb (largest 576 to 649 at F0) | every lineage and both maskings at 10 Mb (2,289 to 5,692); DHC also at 3 Mb (2,551; 2,272) |
| SD units: sqrt(index) within [26.7, 240] | 2 of 10: DHC F0 at 1, 3, 10 Mb (SD ratio 28.7, 37.5, 53.5) and DHC F2 at 3, 10 Mb (27.0, 29.6). No single lineage: largest SD ratio 24.0 (H), 25.5 (C), 25.3 (B), 22.3 (G), all F0 at 10 Mb | every lineage and both maskings at 3 and 10 Mb (30.2 to 61.2); DHC also at 1 Mb, up to 72.8 (F0) and 75.4 (F2) at 10 Mb |
| class at those cells, margin in the same units as the gate | SD units, 80 / sqrt(N_hi), six variants: DHC F0 1.92 to 2.42 (1 Mb), 1.36 to 1.96 (3 Mb), 0.92 to 1.66 (10 Mb); DHC F2 1.48 to 2.36 (3 Mb), 0.95 to 1.88 (10 Mb). **MARGINAL-OUT at 1 and 3 Mb, calibration-dependent at 10 Mb; none DAY** (DAY needs more than 3) | variance units, 6,400 against the R1u bands (unsourced exposure-CV bracket): H, C, B at 10 Mb MARGINAL-IN; G and DHC at 10 Mb CRITIC; DHC at 3 Mb MARGINAL-IN. **None DAY**; largely a measure of the mask (section 9 item 7) |

  Under R2 no single lineage reaches an SD ratio within 3x of 80 at any W up to 10 Mb in the normalised index (largest 24 to 25.5); DHC does from 1 Mb (F0) or 3 Mb (F2). The one-sided statement "more than 80" is true under R2 in no measured cell, normalised or not (largest 53.5 and 75.4). A DAY class at a reproduced R2 cell appears only by mixing units (gate in SD units, class in variance units), which neither review claims. **Symmetry:** R2 is a reading the audit added. Its non-reproduction for single lineages is convention-dependent in the same way as P3's hit is a class of a number under that reading; neither is a point for either side, and both are listed under "Both" in section 8. The caveat that Day's pipeline is unreleased applies to both.
- **UNTESTED**: TREE, PAIRS and BP units (not measurable on `fm_bins.npz`).

Classes at the reproduced windows: under AMENDED, **no reproduced cell is DAY** (implied by the own-exposure result, section 1 (a); the small-W R1 cells are UNTESTED, not failed; power as in section 6a), and exactly one R1 cell is a clean CRITIC (DHC, masked, 300 kb: 80 against N_lo 13 to 71 and N_hi 313 to 501; measured φ there 89; band width 4.4 to 41 over the six variants, at or under the ratio 9 of section 1 in two of them, FRANC and NOWONG at persistence 1.0). Every other reproduced R1 cell is MARGINAL-IN, MARGINAL-OUT (DHC unmasked 10 kb), CAL-DEPENDENT or ALN-DEPENDENT. Under the REGISTERED rule at the gated W (a hybrid of two labels: the gate is amendment 2) every reproduced R1 cell is CRITIC under PREREG except DHC unmasked at 10 kb (MARGINAL); under SOURCED gorilla at 1 Mb and 3 Mb is BELOW.

**Post hoc, descriptive: the class of 80 exactly at the W where each lineage measures 80** (bands at the lineage's mean measured density, registered exposure bracket). PREREG: CRITIC in all ten (F0 and F2; H, C, B, G, DHC). SOURCED: CRITIC in eight, BELOW for gorilla in both filters, which is a boundary case (N_lo 80.4 at F0 and 80.6 at F2 against 80; with the label fixed the registered P4 gives 79.97, CRITIC, and 80.03, BELOW; the clear form of the gorilla failure is the own-exposure cells above). AMENDED consensus: ALN-DEPENDENT for F0 H, C, B and DHC; CAL-DEPENDENT for the other six (CRITIC or M-IN for F2 H, C, B, DHC; CRITIC or B-NEAR for G, which on A4's anomaly question is NOT-HIGH in all six variants). None is DAY; none is a clean CRITIC.

R1u limit: the registered R1u classes use the unsourced exposure-CV bracket 0.2 to 0.5. `realdata` measured CV_c at 0.03 to 0.20 over used windows and 0.25 to 0.88 over all windows (F2 at W <= 30 kb is above the bracket). The classes were not re-scored with the measured CV_c in this chain (`score --cvc` exists). Amendment A8 already bars R1u from scoring CRITIC alone.

## 5. Predictions P1-P8, scored as registered

The "Day side" and "critic side" expectations inside the registered predictions were written by the audit. They are audit gloss, not statements of Day or of any critic (rule S: only verbatim statements are scored); Day has stated no window and no expectation about a heterogeneous neutral band.

| # | Registered prediction (PREREG) | Result | Score |
|---|---|---|---|
| P1 | R1, DHC, masked: 80 inside the band at 100 kb (hand ~[5.7, 133]) and 1 Mb (~[24, 740]); above N_hi at W <= 10 kb (hand N_hi ~24) | 100 kb [3.4, 168] inside; 1 Mb [13, 916] inside; N_hi 31 at 10 kb, 13.7 at 3 kb, 6.1 at 1 kb, 80 above each (MARGINAL at 10 kb, DAY below) | **HIT** (3 of 3 parts). The critic-side expectation as written by the audit (inside at >= 100 kb) is met; the Day-side expectation as written by the audit (above at every W <= 1 Mb; he has stated none) is not |
| P2 | R1, H: inside at 1 Mb (~[10, 310]); above masked N_hi at <= 100 kb (~55); inside unmasked N_hi at 100 kb (~120) | 1 Mb [6.0, 321] inside; masked N_hi 59.4 at 100 kb, 80 above (MARGINAL); unmasked N_hi 132, inside | **HIT** (3 of 3) |
| P3 | R2 (6,400) above N_hi unmasked at every W <= 1 Mb for H, C, G, DHC; inside only for TREE / PAIRS at W >= ~3-10 Mb, if at all. A Day-side point if it holds | Largest N_hi unmasked at 1 Mb is 1,405 (DHC): 6,400 is above for all four units at every W <= 1 Mb, and DAY (> 3x) throughout. Against the unmasked band TREE is inside from 300 kb, PAIRS-naive from 30 kb, PAIRS-struct from 1 Mb | **HIT as registered** on the main clause. It is a class of the number 6,400, not of anything measured: no measured SD ratio exceeds 80 at any W up to 10 Mb (largest 53.5 for DHC, 25.5 for a single lineage). The registration said "A Day-side point if it holds"; because R2 is a reading the audit added, the fix pass lists the hit and R2's non-reproduction together under "Both" in section 8, on neither side's credit list. **MISS** on the window estimate for TREE / PAIRS: against the unmasked band inside 3 to 100 times earlier than ~3-10 Mb (PAIRS-struct from 1 Mb, TREE from 300 kb, PAIRS-naive from 30 kb); PAIRS-struct against the masked band from 3 Mb, as predicted. Gate beside it (A7), both unit conventions: section 4 |
| P4 *(informed, not predictive)* | Window at which the R4-FM φ reaches 80 lies where 80 is inside the band; CRITIC: every lineage; DAY: above by > 3x for some lineage; R2 only beyond 1 Mb | **REGISTERED code, truncated grid** (1-Mb cells skipped, see "Defects"): R1 and R1x CRITIC in 40 of 40 curve-readings (the code scores 20 curves, F0-F3 x H, C, B, G, DHC, under two readings; the registered curves are F0 and F2 only: 20 of 20). R2: reached only by extrapolation to 1.6e7 to 1.3e10 bp, MARGINAL in 19 of 20, CRITIC in one. **Post hoc, label fixed** (`p45fix`): R1 and R1x CRITIC in 40 of 40 (registered curves 20 of 20); the window moves down (H F0 410 -> 392 kb, C F0 800 -> 521 kb, G F0 1,934 -> 808 kb, DHC F2 275 -> 247 kb, H F2 1,632 -> 870 kb); 15 of 20 curves interpolated, 5 still extrapolated past 1 Mb (G F1; H, C, B, G F3). R2 windows 31 Mb (DHC F0, MARGINAL) to 886 Mb (H F0), still extrapolated; bands not evaluated beyond 31.6 Mb | **CRITIC outcome observed** in both versions; no prediction credit (A10) |
| P5 *(informed, not predictive)* | >= 80% of the R4-FM grid cells inside their band; audit guess: DHC F0 1 kb may lie above | **REGISTERED code, truncated grid**: 59 of 60 scored cells inside (98%); on the registered cell set (F0, F2, F3) 44 of 45. **Post hoc, label fixed**: 79 of 80 (99%); registered cell set 59 of 60. The one cell outside in every version is DHC F0 1 kb (φ 9.51 against N_hi 9.01), as guessed | **Met** in every version; no prediction credit (A10). See "Defects" for the cell sets |
| P6 | Simulated D within 15% of the exact expectation (D - 1) at W <= 1 Mb, every band cell; Poisson 1.00 +/- 0.05 | 24 of 24 band cells within 15%: ratio of excesses 0.973 to 1.073. Poisson means 0.967 to 1.034 | **HIT** |
| P7 | (i) BGS_hi adds <= 25% to N_hi unmasked at every W <= 1 Mb; (ii) corr(H density, gene-density covariate) < 0 under BGS; (iii) neutral φ_HC at 100 kb in [1, 6] masked; (iv) corr(H, C) >= 0.6 at W >= 100 kb, central neutral model | (i) 1.1% to 3.8%. (ii) -0.26, -0.37, -0.45 at 10 kb, 100 kb, 1 Mb: true by construction, reported and not scored (A13). (iii) 1.51 (central); the high lineage-specific arm gives 6.05 and the analytic bound 6.21, 1% and 3% over the stated top. (iv) 0.875 at 100 kb, 0.946 at 1 Mb | **HIT** on (i) and (iv). (iii) is **reading-dependent**: hit if "[1, 6]" is the central value (1.51); miss by 0.8% (simulated upper arm, 6.05) to 3.5% (analytic bound, 6.21) if it is the band, a reading the registration's own wording ("Neutral phi_HC band") supports at least as well |
| P8 | (i) Block model f = 0.02, e = 1, Lb = 100 kb gives φ_HC > 10 at 100 kb (> 3x the neutral upper bound); (ii) f e > 1 gives φ_HC > 100; (iii) Day side: f = 0.005, e = 0.5 is not detectable by φ alone | (i) φ_HC = 5.06 with blocks on the window grid; 3.97, 3.61, 3.95 at phases 1/4, 1/2, 3/4 and 4.27 at random phase (post hoc `simphase`): below 10, below three times the bound (18.6 at lambda_M = 0, which is what the registered parenthesis implies; the "10" and the "3x" were already inconsistent at registration) and below the neutral upper bound itself (6.05 simulated, 6.21 analytic). (ii) The scenario run is f e = 1 (e 2, f 0.5), the boundary of "f e > 1": 103 at 100 kb on the grid (11.2 at 10 kb, 102 at 1 Mb); off the grid 64.1, 52.5, 64.2 at phases 1/4, 1/2, 3/4 and 72.5 at random phase (10.9 at 10 kb, 101 at 1 Mb). (iii) φ_H 11.9 (Lb 20 kb) and 12.6 (Lb 100 kb; 12.3 at random phase) against 11.6 neutral: inside the band | (i) **MISS**, by more off the grid. The miss is an error of the audit's hand estimate (section 8, "Both"), not evidence for Day's claim; what it shows about the test is a limit on Day's side: a one-lineage block mechanism doubling the rate over 2% of the genome is **not** flagged by S2's 3x rule at 100 kb. (ii) **HIT on the registered code, by 3%; MISS at any other phase** (52 to 73 against > 100). The registration did not specify block placement; the hit is a property of blocks and windows sharing a grid, not of the block model. (iii) **HIT**: credited as a limit of the critic's main test (and it holds equally for the 2%-doubling model, section 6a) |

**P7 re-scored under SOURCED** (as amendment 1 requires): (i) BGS_hi adds 5.3% at 1 kb, 9.9% at 100 kb, 12.9% at 300 kb and 18.4% at 1 Mb: **HIT** at every W <= 1 Mb (22% at 3 Mb and 10 Mb, outside the registered range). The amendment's hand figures were ~8% and ~17%. (ii) -0.41, -0.48, -0.50, by construction. (iii) 1.50 central; 5.98 in the high lineage-specific arm. (iv) 0.955 and 0.986. P7 measures BGS against the upper bound of all other components, not the share of real variance BGS explains (FML-M3, FML-P1); that question is not answered here.

**The other predictions re-scored under SOURCED** (amendment 1: every prediction re-scored). P1: 100 kb [25, 210] inside; **1 Mb [143, 1,209]: 80 is BELOW the band, a miss at 1 Mb**, as amendment 1's hand figures anticipated; above N_hi at 10 kb (40.2), 3 kb and 1 kb. P2: 1 Mb [60, 423] inside; masked N_hi 73.8 at 100 kb, 80 above; unmasked 149, inside: hit. P3: main clause holds (largest N_hi unmasked at 1 Mb is 1,709). P4, truncated grid: R1 and R1x CRITIC in 32 of 40, **BELOW in 8 (gorilla, all four filters)**; R2 rows MARGINAL in 18 of 20 (DHC F1 and F2 CRITIC). P4, label fixed (post hoc): CRITIC 37, **BELOW 3** (gorilla F1 under R1 and R1x; gorilla F2 under R1 only, N_lo 80.03 against 80; gorilla F0 N_lo 79.97, CRITIC): boundary cases, and on the registered curves (F0, F2) 19 of 20 CRITIC. P5, truncated grid: 57 of 60 (95%; registered cell set 43 of 45); the three outside are gorilla at 100 kb, F1 to F3, below N_lo. P5, label fixed: 75 of 80 (94%; registered cell set 57 of 60); two more gorilla cells below N_lo at 1 Mb (F1 78.7 against 89.2; F3 56.5 against 65.1). So the label-fixed registered computation is slightly better for the SOURCED null on P4 and slightly worse on P5; P5 stays far above 80% in every version. P6: 24 of 24, ratios 0.950 to 1.087; Poisson 0.972 to 1.032. P8: (i) 5.00 on the grid, 4.21 at random phase, miss; (ii) 103 at 100 kb on the grid (97.7 at 1 Mb), 72.6 at random phase (64.6, 53.0, 64.6 at the fixed phases); (iii) 30.8 and 32.5 against 32.0 neutral.

**Defects in the registered P4 / P5 computation (found at write-up; confirmed by the correctness review; registered code and outputs unchanged).** `inhouse()` maps window labels `1kb, 10kb, 100kb, 1Mb`, but `fm_analyse.json` names the last cell `1000kb`. The bug was in the registration commit; `selftest` never called `inhouse` and nothing asserted the cell count. The twenty 1-Mb cells were silently skipped. Cell sets, corrected: the registered P5 text names three filters (F0, F2, F3), four W and five lineages, i.e. **60 registered cells**, not 80; the code scored F0-F3 at three W, i.e. 45 of the registered cells plus 15 unregistered F1 cells (the two "60" are equal by coincidence). The registered P4 names F0 and F2 (10 curves); the code scored 20. Every P4 window except DHC F0 was extrapolated from the 10-kb and 100-kb points instead of interpolated to 1 Mb. Three things are now reported and kept apart:
1. **REGISTERED code, truncated grid** (committed `fmnull_analytic.json`): the numbers in the table above.
2. **Post hoc, label fixed** (`inhouse_fix`, mode `p45fix`, `raw/fmnull_p45fix.{json,out}`; both spellings accepted, every `auto|...` key asserted mapped, 80 cells asserted; `selftest_fix` adds the missing synthetic four-label case; with the registered label map the mode reproduces the committed P5 cells and P4 windows exactly). Numbers beside the registered ones above. No hit, miss or direction changes. Under SOURCED the gorilla BELOW count on P4 falls from 8 to 3 of 40, so the label-fixed registered computation does not sharpen the gorilla failure on P4; on P5 it adds two gorilla BELOW cells.
3. **The `post` own-exposure table** (section 4): a different computation (each cell's own exposure, F0 and F2, seven W, amended classes). It is not "the corrected P4 / P5"; it is where the gorilla low-edge failure is clear (G F0: 38.1 against 72.7 at 300 kb).

The R2 windows are extrapolated in both versions (truncated: 16 Mb for DHC F0, otherwise 0.1 to 13 Gb; label fixed: 31 Mb to 886 Mb, all beyond 10 Mb); `realdata` shows the index never reaches 6,400. P4 and P5 stand as scored on the truncated grid under the label REGISTERED; neither earns prediction credit (A10).

## 6. Amendment-2 outputs, and the simulate arm

**Classes for Day's 80**: sections 3c to 3e. **CAL-DEPENDENT cells**: under R1 and the masked band, 20 of the 36 single-lineage and DHC cells are clean; the CAL-DEPENDENT ones are H 30 kb, C 100 kb, G 300 kb, DHC 30 kb, and every unit at W >= 1 Mb. The disagreement at W >= 1 Mb is persistence: with the pedigree CV taken as a floor (1.0), 80 is BELOW; with half of it persisting (0.5), 80 is CRITIC. **ALN part**: section 2c and the ALN flags in 3c; under R1 the unmasked class differs from the masked class for H at 30 kb to 1 Mb, C at 10 kb, 100 kb and 300 kb, G at 10 kb, 30 kb and 300 kb, DHC at 3 kb, 30 kb and 100 kb. **K_hi comparison** (Q171 names selection as well as drift): no cell is DAY against N_hi and CRITIC against K_hi; adding BGS to the unmasked band moves boundary cells by at most one class (H 10 kb: DAY -> CAL (DAY, M-OUT); DHC 3 kb: CAL (DAY, M-OUT) -> M-OUT; H 300 kb: CAL (M-IN, CRITIC) -> CRITIC). **Reproduction gate**: section 4. **R1u and U-BP**: sections 3d, 4; U-BP is UNTESTED on the held bins. Under BP-naive a uniform-rate process alone gives D >= 61 at every W (structural floor; N_lo 62 to 65 at 1 kb), as the amendment's hand figure said; under BP-struct the bands are the lowest in the table and 80 is DAY to 30 kb.

**φ_HC neutral upper bound (S2, amendment A9), as registered: c = 1, unit densities**, beside the measured split dispersion (which is at exposure 0.54 to 0.94, so the two columns of each pair are **not like for like**; kept as the registered output):

| W | bound masked, lambda_M = 0 / 0.25 / 0.5 | measured F2 (exposure) | bound unmasked, lambda_M = 0 / 0.25 / 0.5 | measured F0 (exposure) |
|---|---|---|---|---|
| 10 kb | 1.5 / 4.1 / 6.7 | 1.33 (0.64) | 10.8 / 13.8 / 16.8 | 2.72 (0.94) |
| 100 kb | 6.2 / 22.7 / 39.4 | 1.81 (0.58) | 75 / 94 / 113 | 8.54 (0.92) |
| 1 Mb | 41 / 140 / 240 | 3.49 (0.54) | 207 / 310 / 415 | 24.1 (0.91) |

(SOURCED and AMENDED rows, which are equal; PREREG differs only at lambda_M > 0: 3.8 / 6.0, 19.6 / 33.2, 114 / 188 masked.)

**The same bound at each cell's own exposure and densities** (fix pass, post hoc, `fixpass` section E; `phi_hc_from` with the cell's c, d_H, d_C; SOURCED = AMENDED; the excess φ_HC - 1 is proportional to the mean H + C count, so this is the like-for-like comparison):

| W | F2 measured (c) | F2 bound masked, lambda_M = 0 / 0.25 / 0.5 | (measured - 1) / (bound - 1) at lambda_M = 0 | lambda_M at which bound = measured | A9 status, F2 | F0 measured against the masked lambda_M = 0 bound (ratio of values; lambda_M needed) | F0 unmasked bound, lambda_M = 0 |
|---|---|---|---|---|---|---|---|
| 1 kb | 1.109 (0.77) | 1.039 / 1.31 / 1.59 | 2.82 | 0.07 | **LAMBDA-DEPENDENT** | 1.31 against 1.05 (1.24; 0.18) | 1.99 |
| 3 kb | 1.200 (0.70) | 1.106 / 1.75 / 2.42 | 1.89 | 0.04 | **LAMBDA-DEPENDENT** | 1.74 against 1.16 (1.50; 0.16) | 3.88 |
| 10 kb | 1.333 (0.64) | 1.323 / 2.85 / 4.41 | 1.03 | 0.002 | **LAMBDA-DEPENDENT** (above by 3% of the excess) | 2.72 against 1.51 (1.81; 0.13) | 10.2 |
| 30 kb | 1.51 (0.61) | 1.91 / 5.36 / 8.88 | 0.56 | 0 | inside at lambda_M = 0 | 4.50 against 2.49 (1.81; 0.09) | 26.6 |
| 100 kb | 1.81 (0.58) | 3.85 / 12.8 / 22.0 | 0.29 | 0 | inside | 8.54 against 5.82 (1.47; 0.05) | 70.0 |
| 300 kb | 2.30 (0.56) | 8.84 / 29.9 / 51.2 | 0.17 | 0 | inside | 14.8 against 14.5 (1.02; 0.002) | 132 |
| 1 Mb | 3.49 (0.54) | 21.8 / 74.0 / 127 | 0.12 | 0 | inside | 24.1 against 37.4 (0.64; 0) | 190 |
| 3 Mb | 5.43 (0.52) | 38.8 / 150 / 262 | 0.12 | 0 | inside | 34.0 against 68.3 (0.50; 0) | 231 |
| 10 Mb | 6.16 (0.51) | 49.0 / 248 / 447 | 0.11 | 0 | inside | 37.6 against 88.5 (0.43; 0) | 253 |

Both statements, as the two steelman reviews ask. **Day-side:** on single-copy sequence the measured human / chimp split dispersion **exceeds the registered gBGC-only bound (lambda_M = 0) at the three finest scales**, 1, 3 and 10 kb, by 2.8, 1.9 and 1.03 times the bound's excess; the earlier sentence "inside the bound at lambda_M = 0 at all three W" was wrong at 10 kb (1.333 against 1.323), and these are the scales at which the number 80 would be DAY. **Critic-side:** that excess needs a lineage-specific share of the mutational variance of only **0.04 to 0.07** (PREREG and SOURCED alike; 0.002 at 10 kb), about a tenth of A9's upper reading of 0.5; lambda_M = 0 is the corner at which no part of the mutation landscape differs between human and chimp, against FML-S8; nothing is near 3x on the value (at 10 kb DAY would need 3.97, an excess 9.2 times the bound's); the cells are flagged under-sourced at the fine scale; and at 1 kb parsimony misassignment, clustered multi-nucleotide mutation or the private polymorphism of the sequenced ape (none in the null) would do the same. It is an unexplained residual at the registered lambda, not a mechanism. The F0 values are above the masked lambda_M = 0 bound from 1 kb to 300 kb and inside the unmasked bound at every W; that F0 excess is the reference-projection effect (φ_HC 8.54 becomes 18.0 on the chimp reference and 2.7 without paralogous rows; section 4) and counts for neither side.

**Simulate arm: does the simulation reproduce the analytic bands?** Yes for the PREREG and SOURCED corners (24 cells each) and for the three amendment formulas listed; the AMENDED bands and K_hi have no simulation arm (section 9 item 12):

| arm | set | simulated against expected | 
|---|---|---|
| P6 band cells (N_lo, N_hi masked, N_hi unmasked; d 0.0051 and 0.012; 1 kb to 1 Mb; 300 Mb x 10 replicates; expectation with the finite-genome correction) | PREREG | excess ratio 0.973 to 1.073 (24 cells) |
| same | SOURCED | 0.950 to 1.087 (24 cells) |
| Poisson baseline | both | 0.967 to 1.034 (largest replicate SD 0.11 at 1 Mb) |
| R1u formula (amendment 2; fixed test components, not a parameter set) | n/a | 13.8 / 13.7, 81.8 / 80.5, 205 / 194 at 10 kb, 100 kb, 1 Mb (within 6%) |
| U-BP compound formula | n/a | 38.3 / 38.3, 133 / 133, 429 / 418 (within 3%) |
| φ_HC with lambda_M = 0.25 and 0.5 | n/a | 2.31 / 2.35, 11.9 / 12.1, 39.8 / 39.1; 3.11 / 3.18, 18.0 / 18.3, 57.0 / 54.2 (within 5.2%) |

The largest deviations are at 1 Mb (300 windows per replicate), at the upper corner.

Two-lineage scenarios at 100 kb (H 0.0051, C 0.0057, c = 1; central neutral model plus the stated change). The first five numeric columns are the registered run, in which every block starts on a multiple of Lb, so with Lb = W = 100 kb each block fills exactly one window (the best case for φ_HC). The last two columns are the post hoc `simphase` run: the same seed and random stream (phase 0 reproduces the registered run exactly), windows taken off the block grid; "rand" is one offset per replicate, uniform on [0, Lb); the three fixed phases are 1/4, 1/2, 3/4 of Lb.

| scenario | set | φ_H | φ_C | φ_HC | corr(H, C) | φ_res H (R4-FM shared-rate null) | off grid: φ_HC rand (1/4, 1/2, 3/4), PREREG; SOURCED | off grid: φ_H rand |
|---|---|---|---|---|---|---|---|---|
| S0 neutral, central | PREREG / SOURCED | 11.6 / 32.0 | 12.8 / 35.5 | 1.51 / 1.50 | 0.88 / 0.95 | 2.86 / 2.84 | 1.52 (1.50, 1.50, 1.50); 1.50 (1.49, 1.50, 1.51) | 11.6 / 32.0 |
| S0 with lineage-specific gBGC at the upper edge | PREREG / SOURCED | 16.2 / 36.5 | 18.5 / 40.7 | 6.05 / 5.98 | 0.64 / 0.83 | 11.6 / 11.5 | 6.04 (6.04, 6.04, 6.05); 5.98 (5.98, 5.97, 5.97) | 16.2 / 36.5 |
| S1 BGS at the upper edge (ell 1 Mb) | PREREG / SOURCED | 13.5 / 43.4 | 14.9 / 48.1 | 1.53 / 1.51 | 0.89 / 0.97 | 2.89 / 2.87 | 1.52 (1.51, 1.51, 1.52); 1.52 (1.53, 1.52, 1.52) | 13.5 / 43.4 |
| S2 blocks, Lb 20 kb, e 0.5, f 0.005 | PREREG / SOURCED | 11.9 / 30.8 | 13.1 / 34.2 | 1.60 / 1.56 | 0.87 / 0.95 | 3.04 / 2.97 | 1.58 (1.58, 1.59, 1.58); 1.56 (1.56, 1.56, 1.56) | 11.9 / 30.8 |
| S2 blocks, Lb 100 kb, e 0.5, f 0.005 | PREREG / SOURCED | 12.6 / 32.5 | 13.1 / 35.1 | 1.76 / 1.78 | 0.86 / 0.94 | 3.46 / 3.52 | 1.68 (1.67, 1.66, 1.67); 1.71 (1.69, 1.67, 1.70) | 12.3 / 32.3 |
| S2 blocks, Lb 100 kb, e 1.0, f 0.02 | PREREG / SOURCED | 21.7 / 41.8 | 12.7 / 34.7 | 5.06 / 5.00 | 0.64 / 0.83 | 12.7 / 12.6 | **4.27 (3.97, 3.61, 3.95); 4.21 (3.93, 3.57, 3.91)** | 18.9 / 39.0 |
| S2 dominant, Lb 100 kb, e 2, f 0.5 | PREREG / SOURCED | 283 / 328 | 12.6 / 35.4 | 103 / 103 | 0.25 / 0.40 | 260 / 260 | **72.5 (64.1, 52.5, 64.2); 72.6 (64.6, 53.0, 64.6)** | 204 / 248 |

**`simphase` against its predictions (fixed in the docstring before the run, commit 57f2834).** Audit expectation: dominant φ_HC about 64 at phases 1/4 and 3/4, about 52 at 1/2, 55 to 85 at random phase, so P8 (ii) misses off the grid: **held** (64.1 / 64.6, 52.5 / 53.0, 72.5 / 72.6). Registered block model 3.5 to 4.1 at every non-zero phase: **held at the three fixed phases** (3.57 to 3.97); the random-phase mean is 4.21 to 4.27, just above that range (three of its ten offsets fall within 2.6 kb of the grid). Neutral scenarios change by under 3%: **held** (largest 1.3%). Lb = 20 kb scenarios change by under 10% at 100 kb: **held** (largest 3.9%). Dominant φ_H keeps its DAY class against the masked band at phase 0 and loses it at phase 1/2: **held** (152 / 195 against 3 N_hi = 178 / 221); at random phase it is DAY (204 / 248), on which no call was made. Day-side expectation (audit gloss): off the grid the dominant model no longer clears 3x the bound at lambda_M = 0.25: **held in part** (at phase 1/2 under both sets, 2.7 and 2.3; at 1/4 and 3/4 under SOURCED, 2.9; **not** at random phase, 3.7 and 3.2, nor at 1/4 and 3/4 under PREREG, 3.3). Critic-side expectation (audit gloss): the dominant model stays above 3x the lambda_M = 0 bound at every phase and more than 20 times the measured F2 excess at matched exposure, and block models with f e² <= 0.02 stay inside the bound at every phase: **held** (8.4 to 16.6 times the bound; 34 to 69 times the measured excess; largest small-block φ_HC 5.06).

**P8 re-scored per lambda_M (A9), per set.** At 100 kb the neutral upper bound for φ_HC (masked, c = 1) is 6.2, 19.6, 33.2 under PREREG and 6.2, 22.7, 39.4 under SOURCED / AMENDED at lambda_M = 0, 0.25, 0.5. The registered block model (5.06 on the grid, 4.27 at random phase) is below all three in both sets. The dominant model, ratio of values to the three bounds:

| | PREREG | SOURCED / AMENDED |
|---|---|---|
| on the grid (103) | 16.6, 5.3, 3.1: clears 3x at all three | 16.6, 4.5, 2.6: **fails at lambda_M = 0.5** |
| random phase (72.5 / 72.6) | 11.7, 3.7, 2.2: fails at 0.5 | 11.7, 3.2, 1.8: fails at 0.5 |
| phase 1/2 (52.5 / 53.0) | 8.5, 2.7, 1.6: fails at 0.25 and 0.5 | 8.5, 2.3, 1.3: fails at 0.25 and 0.5 |

Since A9 lets S2 score DAY only above 3x the bound at every lambda_M, S2 as amended cannot be met at 100 kb, off the window grid in either set, even by a mechanism that triples the rate over half the genome on one lineage. On the grid: 10 kb 7.3, 3.0, 1.9 (PREREG) and 7.3, 2.8, 1.7 (SOURCED); 1 Mb 2.5, 0.9, 0.5 and 2.4, 0.7, 0.4. A9 stated this cost for the registered block model only. This is a defect of the criterion (an unsourced upper reading, lambda_M = 0.5, applied to the upper mutational corner), recorded on Day's side in section 7.

### 6a. Power, both ways (fix pass; post hoc, descriptive; `fixpass` sections G and H)

Two statements are both true and belong together: **the null is falsifiable, by the mechanism Day asserts**, and **the check has little power against anything smaller**.

*Class of the simulated φ_H of each planted scenario, against the band at the simulation's own exposure (c = 1, d 0.0051; PREREG sims against PREREG bands, SOURCED against SOURCED; amended classes):*

| planted scenario | f e² | 10 kb, masked / unmasked | 100 kb, masked / unmasked | 1 Mb, masked / unmasked |
|---|---|---|---|---|
| eight non-dominant block scenarios (Lb 20 or 100 kb; e 0.5 or 1; f 0.005 or 0.02) | 0.00125 to 0.02 | CRITIC / CRITIC, all | CRITIC / CRITIC, except f 0.02, e 1, Lb 100 kb on the grid: MARGINAL-IN / CRITIC (0.36 and 0.57 of N_hi) | CRITIC / CRITIC, all |
| the same eight, totals | | on the grid: CRITIC 94, MARGINAL-IN 2 of 96 set-band-W cells; random phase: CRITIC 96 of 96 | largest φ_H excess 1.95 times the central neutral excess (1.69 at random phase) | |
| dominant (f 0.5, e 2, Lb 100 kb; f e = 1) | 2 | MARGINAL-OUT / MARGINAL-OUT (2.70, 2.44 x N_hi; 1.41, 1.40) | **DAY** / MARGINAL-OUT on the grid (4.76, 4.45; 2.14, 2.21) and at random phase (3.44, 3.36; 1.55, 1.67); MARGINAL-OUT / MARGINAL-OUT at phase 1/2 (2.56, 2.64; 1.15, 1.31) | MARGINAL-OUT / MARGINAL-IN (PREREG 1.19; 0.78), MARGINAL-OUT / MARGINAL-OUT (SOURCED 1.54; 1.09) |

So: (i) **the dominant planted scenario scores DAY**, at 100 kb against the masked band, in both sets, on the grid and at random phase; it never scores DAY against the unmasked band (at most 2.2 x N_hi) and is MARGINAL-OUT at 10 kb and 1 Mb. (ii) **Every non-dominant planted scenario scores CRITIC or MARGINAL-IN**, including the one that doubles the human rate over 2% of the genome (about 3e5 extra substitutions on a 3-Gb genome: 0.02 x 0.0051 x 3e9, arithmetic). The reason is the rule, not the data: DAY needs three times the simultaneous upper corner, which is 15 and 6.9 times the central neutral index at 100 kb against the masked band (PREREG, SOURCED) and 34 and 14 times it against the unmasked band. **Every "no DAY" sentence in this write-up carries this qualifier: by the 3x class of φ alone, a one-lineage mechanism up to a doubling over 2% of the genome would give the same result.**

*How far the data are from the dominant scenario, and what the data bound (F2, 100 kb; simulated excesses rescaled to the cell's own exposure, N = 589 H + C substitutions per window against 1,080 in the simulation; φ - 1 is proportional to the mean count; PREREG shown, SOURCED within 2% for φ_HC and φ_res):*

| | φ_HC, blocks on grid / random phase | φ_res H | φ_H, PREREG / SOURCED |
|---|---|---|---|
| **measured, F2** | **1.81** | **2.68** | **14.3** |
| central neutral | 1.28 / 1.28 | 2.0 | 6.9 / 18.3 |
| neutral, lineage-specific gBGC at the upper edge | 3.75 / 3.75 | 6.9 | 9.5 / 20.8 |
| blocks Lb 20 kb, e 0.5, f 0.005 (f e² 0.00125) | 1.33 / 1.32 | 2.1 | 7.1 / 17.6 |
| blocks Lb 100 kb, e 0.5, f 0.005 (0.00125) | 1.42 / 1.37 | 2.4 / 2.3 | 7.4 / 18.6 |
| blocks Lb 20 kb, e 1, f 0.02 (0.02) | 1.79 / 1.75 | 3.2 / 3.1 | 7.8 / 18.8 |
| blocks Lb 100 kb, e 1, f 0.02 (0.02) | 3.22 / 2.78 | 7.5 / 6.1 | 12.5 / 23.7 |
| dominant (f e² = 2) | 56.8 / 40.0 | 145 / 103 | 158 / 183 on grid; 114 / 139 random phase |

- **The data are far below the dominant scenario at matched exposure**: φ_HC 31 times (on grid) or 22 times (random phase) below it by value, 69 or 48 times by excess; φ_H 11 to 13 times below it on the grid and 8 to 10 times at random phase. Q169 (b) says the mesa signature "is the dominant source of genomic divergence between humans and the great apes"; the registration translated that as f e > 1 (audit gloss), and the outcome that would have supported it was reachable and was not observed.
- **Where the data sit among the scenarios.** Rescaled to c = 1 the measured F2 φ_HC is 2.49, not 1.81. At matched exposure it is **above** the central neutral scenario (1.28) and the two small-block scenarios (1.32 to 1.42), at the level of the Lb 20 kb, 2% doubling (1.75 to 1.79), **below** the Lb 100 kb, 2% doubling (2.78 to 3.22) and below the upper lineage-specific neutral arm (3.75). The earlier sentence "the F2 values sit at the central neutral scenario" is withdrawn for φ_HC; it holds for corr(H, C) (0.87 measured, 0.86 to 0.88 simulated under PREREG) and roughly for φ_res (2.68 against 2.0 to 2.4). The statistic cannot say which lineage carries the excess, and the null's lineage-specific arm covers it.
- **What φ_HC bounds, without the 3x rule.** φ_HC - 1 is an upper bound on the sum of all lineage-specific variance in the H / C split, neutral or not, with no bracket in it. In the simulations the block excess is close to linear in f e² (175 to 230 per unit at c = 1 for Lb 100 kb on the grid, 130 to 165 at random phase; 47 to 70 and 43 to 53 for Lb 20 kb). Giving the **whole** measured excess (0.81) to human-only blocks, with no gBGC turnover, no private polymorphism and no error: f e² <= 0.0065 to 0.0085 (Lb 100 kb, on grid), 0.009 to 0.011 (random phase), 0.02 to 0.03 (Lb 20 kb), 0.03 to 0.035 (Lb 20 kb, random phase). Dominance needs f e > 1, hence e > 1 and f e² > 1: **at least about 29 times short** on single-copy sequence. This agrees with R4-FM's direct count (human mesas hold 1.25% to 2.5% of human-chimp differences). Assumptions: the linear scaling is read off eight scenarios; block lengths other than 20 and 100 kb were not simulated (shorter blocks give looser bounds); the bound is for alignable F2 sequence.
- **What is not excluded.** One-lineage block models with f e² up to about 0.01 (blocks of 100 kb) or 0.03 (20 kb) are **not** excluded by anything here, and the F2 φ_HC is above the central neutral scenario. Neither the DAY class nor S2 could have flagged them.

## 7. Criteria S1-S4, and proposed effect on verdicts (proposals only)

| criterion (registered; DAY if met by > 3x the neutral upper bound) | status on the held alignment | could it have been met (Day-side) / could it have failed (critic-side)? (fix pass, from sections 6 and 6a) |
|---|---|---|
| S1: index far above N_hi at every plausible W, and after covariate regression | **Not met.** No measured cell is above 3 N_hi under any set; at W <= 1 Mb one of 70 is above N_hi at all (DHC F0 1 kb, PREREG, 1.09x, an ALN-dependent cell); at 3 to 10 Mb six of 20 are above N_hi under the Francioli-edge variants (up to 1.47x). Covariate clause: **not evaluated** (the φ_cov estimator is invalid, section 9 item 5); S1 is unmet on raw φ alone. Limits: under SOURCED 34% to 54% of the masked upper edge is unsourced, and the unmasked edge leans on ALN | By the dominant planted model: yes at 100 kb against the masked band (DAY: 4.5 to 4.8 x N_hi on the grid, 3.4 at random phase), no at 10 kb or 1 Mb, and no against the unmasked band at any W. By any planted model below the dominant one: no (CRITIC or MARGINAL-IN). "At every plausible W": by no planted model |
| S2: φ_HC > 3x its neutral upper bound | **Not met**: no measured φ_HC is near 3x a bound (largest ratio of values at F2: 1.09, at 3 kb). At own exposure the F2 value is above the lambda_M = 0 bound at 1, 3 and 10 kb (LAMBDA-DEPENDENT; lambda_M 0.04 to 0.07 absorbs it) and inside from 30 kb (bounds 1.32, 3.85, 21.8 at 10 kb, 100 kb, 1 Mb) | **No**, at 100 kb, by any planted model, once blocks are off the window grid or the SOURCED bound is used (dominant model 1.3 to 2.6 x the lambda_M = 0.5 bound); only on the grid under PREREG does the dominant model clear all three lambda_M (3.1). Never by a smaller model. **This is a defect of the audit's criterion** (A9's "at every lambda_M" with an unsourced upper reading of 0.5), **recorded on Day's side. "S2 unmet" is not counted against him.** It is not a severe test in either direction: the critic-side "inside" is also what the registered 2%-doubling block model gives |
| S3: edges sharper than the shortest-ell component allows, and \|Spearman\| < 0.1 with covariates | **Untestable** on 1-kb bins (A13); scores for neither side | No (not testable on these bins) |
| S4: tree-incongruent sharing above the ILS rate | **Not tested** by this script. corr(H, G) is below corr(H, C) at every W (F2 100 kb: 0.74 against 0.87), which is not an S4 test | Not known: not run. To be queued, or dropped with a stated reason, at integration |
| Critic-side: index inside the band at Day's W | **Not scoreable** (W unknown). At the W where the data measure 80 (post hoc): CAL- or ALN-dependent, never DAY, never a clean CRITIC except DHC masked at 300 kb; on A4's anomaly question NOT-HIGH in all six variants for gorilla and for 11 of 12 masked cells at W >= 1 Mb | It could have failed for a dominant mechanism at 100 kb (masked band). It could not have failed for the smaller planted models |
| Critic-side: mesas shared across lineages (no bracket) | Section 0 table. corr(H, C) at F2: 0.57, 0.87, 0.96 at 10 kb, 100 kb, 1 Mb, against 0.63, 0.88, 0.95 in the central PREREG simulation and 0.80, 0.95, 0.99 under SOURCED; φ_H / φ_C 0.97 to 1.04 from 1 kb to 3 Mb. At F0: 0.33, 0.52, 0.77, below both (reference-projection effect, section 4). The registered expected-correlation formula was not evaluated per cell by the script | Yes: the dominant planted model gives corr(H, C) 0.25 / 0.40 at 100 kb (0.30 / 0.47 at random phase) and the 2%-doubling model 0.64 / 0.83 (0.69 / 0.86), against 0.87 measured (simulations at c = 1; the measured value is at exposure 0.58, which lowers a correlation, so the comparison is conservative for the critic side) |
| Critic-side: φ_HC inside its neutral band | **F2: inside at lambda_M = 0 from 30 kb; LAMBDA-DEPENDENT at 1, 3 and 10 kb** (inside from lambda_M about 0.05). F0: ALN-dependent (projection effect) | It would have failed for the dominant model (40 to 57 at the F2 cell's exposure against a bound of 3.85). It carries **no weight against a block mechanism up to f = 0.02, e = 1**: that model predicts 2.8 to 3.2 at matched exposure, also inside |

Summary of the last column, both ways: **no Day-side criterion could have been met by a mechanism smaller than the one Q169 (b) asserts** (audit gloss: f e > 1), S2 could not have been met even by that one off the window grid, and S4 was not run; S1 could have been met by the dominant model at 100 kb on masked sequence, and was not.

**What the docstring licenses.** Registered rule: "CRITIC on every plausible reading" keeps FM3 external `supported` with the annotation "unremarkable against neutral heterogeneity at W" and gives FM10's premise a quantitative defeater; "DAY on the most charitable plausible reading" annotates FM3 "anomalous against the neutral band at W" and moves FM10 external toward `contested`. Amendment A7: a DAY or CRITIC class moves a verdict only if the real-data arm reproduces Day's number at that reading, unit and masking.

- **As registered, without the gate**, the Day-side clause is formally met, by classes of a number at windows, and under a reading, where the measured data do not show it: R2 is DAY at every W <= 1 Mb for every single-lineage unit (P3, a hit), and R1 is DAY at W <= 10 kb. The critic-side clause is not met (R2 and small-W R1 are not CRITIC).
- **With the gate (pre-run amendment 2, the rule in force)**: R2's DAY classes do not count (not reproduced for single lineages in either unit convention; reproduced for DHC in SD units, where the class is MARGINAL-OUT); R1 at W <= 10 kb is not reproduced on alignable sequence for single lineages (measured 1.4 to 10.4), UNTESTED outside it and `unverifiable` until W is released (rule F); DHC at 10 kb is M-OUT. No reproduced cell is DAY. The critic-side clause needs CRITIC on every plausible reading and has one clean reproduced CRITIC cell under R1 (DHC, masked, 300 kb). **Neither clause is met. No verdict move is proposed.**
- **No verdict value changes under either branch.** Even un-gated, the registered move is an FM3 annotation and FM10 external "toward `contested`", which FM10 already is. All three reviews agree.

Proposals for integration (nothing below is applied by this fix pass):
1. **FM3** (`internal: holds`, `fidelity: unverifiable`, `external: supported`): no value changes. Proposed comment for the external field only, extending the present one ("as a description; the magnitude is set by the window ..."): `reading-dependent:` R1 (variance over mean) sets the field: **`supported` as a description, non-discriminating**: "more than 80" is true of the held alignment at W >= 1 Mb in every lineage and both maskings (F2 at 1 Mb: H 89.4, C 89.5, B 88.3, G 85.1), and wherever it is true at W <= 1 Mb the measured index is inside or below a mechanistic neutral band (index / N_hi 0.11 to 0.91 under eight parameter sets; post hoc); R2 (SD ratio, the audit's reading): true in no measured cell; R1 at W <= 10 kb: extended reading, UNTESTED, `unverifiable` until W is released. Fidelity stays `unverifiable` (rule F). The Readings table of section 0 goes into the claim file's R4 paragraph, and the verdict is counted as reading-dependent (rule RD).
2. **FM10** (`internal: pending`, `external: contested`): no change. Internal stays `pending` by owner decision until Day releases his method. External is already `contested`; nothing here moves it in either direction. The quantitative defeater against the audit's reconstructed premise (drift implies a uniform rate; not Day's words: the FM10 claim file records that no text of his states or defends it) is **not licensed** by the registered rule (CRITIC on every reading is not met). Recorded as description, with its power statement attached and not without it: no measured cell exceeds three times the neutral upper bound at any W from 1 kb to 10 Mb; the F2 cells do not exceed the bound at all at W <= 1 Mb; the check had power against a dominant one-lineage block mechanism (which scores DAY at 100 kb and from which the data are 22 to 31 times away in φ_HC at matched exposure) and little against one below f e² of about 0.02. This answers the sentence R4-FM left open (its shared-rate null was descriptive); a defeater, if integration wants one, would attach to that R4-FM sentence, reading-dependent, and not to FM10's verdict.
3. **Day-side items for the argument map**, if integration agrees: the check has little power against one-lineage block mechanisms up to a doubling over 2% of the genome, and against the dominant model on unmasked data; none of S1-S4 could have been met by a mechanism smaller than "dominant", and S2 as amended not even by that (criterion defect); F2 φ_HC exceeds the gBGC-only bound (lambda_M = 0) at W <= 10 kb, **always with the number that a lineage-specific mutational share of 0.04 to 0.07 absorbs it**; the pedigree-calibrated lower edge fails for gorilla on the calibration question; most length scales are unsourced.
4. **Critic-side items**: no cell at W <= 1 Mb is both true of the data and outside the band; pedigree mutation-rate variation alone reaches the measured megabase dispersion; the index is lineage-shared (section 0); φ_HC bounds one-lineage block variance at least about 29 times below "dominant" on single-copy sequence; under gap-inclusive bp a uniform-rate process alone gives an index of at least 61, and under all-pairs sums 7.9 (both UNTESTED on the held bins, unsourced inputs).
5. **Items for neither side** (section 8, "Both"): the F0 excess is a reference-projection effect (R4-FM M1), so F0 classes are ALN-dependent for both sides; R2 (P3's hit and its non-reproduction); six cells at 3 to 10 Mb above the Francioli-edge bound, none DAY (this cuts against "at any W" on the critic side); the audit's own errors.

## 8. Who this helps

**Readings (neutral; this paragraph replaces the former first bullet of each list).** Under R1, the most defensible reading of Q164, the statement is true of the held alignment at W >= 1 Mb in all ten lineage-by-masking cells (F2 at 1 Mb: 89.4, 89.5, 88.3, 85.1, 253), and in none of the cells where it is true at W <= 1 Mb is the measured index above its neutral upper bound under any of the eight parameter sets (index / N_hi 0.11 to 0.91). Day's descriptive sentence is granted in full; it does not discriminate between a heterogeneous neutral process and a further mechanism. The window range where the number 80 would exceed every band (W <= 10 kb) is an extended reading: the index measured there on alignable sequence is 1.4 to 10.4, Day released no window, and the cell is UNTESTED as his claim. If his W were that small and his statistic R1 on a single lineage, an index of 80 would not be explained by this null, and the audit cannot find such an index in alignable sequence; both halves are conditional, and neither is a credit or a failure. Section 0 has the Readings table.

**Day.**
- **The check has little power against anything smaller than a dominant mechanism.** Every planted non-dominant block scenario, including a doubling of the human rate over 2% of the genome, scores CRITIC or MARGINAL-IN on φ_H (96 of 96 set-band-W cells at random phase), is invisible to S2, and the dominant one never scores DAY against the unmasked band. So "no DAY" is the weakly tested outcome (ST-10). One-lineage block models with f e² up to about 0.01 (100-kb blocks) or 0.03 (20-kb blocks) are not excluded, and at matched exposure the measured F2 φ_HC (1.81) is above the central neutral scenario (1.28).
- **No Day-side criterion could have been met by a mechanism smaller than "dominant"**, and S2 as amended could not have been met at 100 kb even by the dominant one off the window grid. That is a defect of the audit's criteria. "S2 unmet" carries no weight against him; S4, the other bracket-free statistic, was not run.
- **On single-copy sequence φ_HC exceeds the registered gBGC-only bound (lambda_M = 0) at 1, 3 and 10 kb**, by 2.8, 1.9 and 1.03 times the bound's excess. Rider, in the same sentence as the review asks: a lineage-specific mutational share of 0.04 to 0.07 absorbs it, nothing is near 3x, and the cells are flagged under-sourced.
- For single lineages no window gives a clean CRITIC consensus under the amended, symmetric rule (rider: at W >= 1 Mb the variants agree that 80 is not high and disagree only on whether it is inside or below the band). The registered CRITIC classes under PREREG come from a band about 60-fold wide, and the variants that survive the low edge are the wide ones (section 1).
- **The null over-predicts at the low edge** (calibration question, A4). SOURCED and the persistence-1.0 variants put gorilla, and under FRANC every lineage, below the lower bound at W >= 100 kb to 300 kb. A model that is wrong at the bottom is weaker evidence when it says "inside" at a neighbouring W. (On A4's anomaly question the same cells are NOT-HIGH; see the critic list.)
- Most brackets are unsourced, and several could be too generous to the null: the ALN bracket is 26-fold wide (sigma 0.016 to 0.42) and no paper quantifies it; the Wong dataset's 0.27, which Smith's abstract attributes to possible technical differences, sets the ALL3 upper edge and doubles N_hi at 1 Mb relative to Francioli; every ell is a guess. The margin is taken about the stacked upper corner and on the value, not the excess (section 9 item 15).
- Under BP-struct, where the structural term is put into the null, 80 is DAY to 30 kb under R1 and 6,400 is DAY at every W under R2. UNTESTED on the held bins; unsourced inputs. It is the mirror of the critic-side unit readings below.
- Scope: every "measured" in this file means hg38- and orangutan-alignable sequence, about 86% of autosomal 1-kb bins; the sequence that makes the T2T assemblies complete (Q162: "all six complete ape genomes") is in no cell.

**Critics.**
- **Where the sentence is true it is not anomalous** (Readings paragraph). Headline count: F2 against the masked band, 35 of 35 cells at or below the neutral upper bound in every one of the eight sets (largest φ / N_hi 0.57 to 0.91). No measured cell is above three times any upper bound at any W from 1 kb to 10 Mb. Riders: little power below a dominant mechanism (section 6a); the surviving bands are wide (section 1); alignable sequence only; counting F0 as well, 39 to 54 of 70 cells are inside without help from the alignment term.
- **Lineage sharing.** Q164 is as true of chimpanzee, bonobo and gorilla as of human: F2 indices at 1 Mb 89.4, 89.5, 88.3, 85.1; φ_H / φ_C 0.97 to 1.04 from 1 kb to 3 Mb; corr(H, C) 0.96 at 1 Mb. No bracket enters this. Rider: H's excess CV² is 4% to 13% above C's.
- **Pedigree de novo mutation data alone** (FML-S2: CV 0.15 to 0.27 at 1 Mb) imply at least the measured dispersion of divergence at 1 Mb (measured excess CV 0.17 to 0.18 for H, 0.11 to 0.15 for G). A uniform rate is not the neutral expectation, and the directly observed non-uniformity is enough to give an index above 80 at 1 Mb. Riders: one species; persistence over the divergence time unsourced; the same fact is a bracket failure on the calibration question.
- **The null is falsifiable by the mechanism Day asserts, and the data are far from it.** The dominant planted scenario scores DAY at 100 kb; at matched exposure the measured φ_HC is 22 to 31 times below it and φ_H 8 to 13 times below it; read without the 3x rule, φ_HC bounds f e² of one-lineage blocks at 0.007 to 0.035, at least about 29 times short of dominance. Rider: smaller block models are not excluded.
- Two unit readings of "substitution density across the genome" (sums over all pairs; gap-inclusive base pairs) put the neutral lower bound at 10 to 65 at 1 kb and above 80 in every variant from 100 kb; for gap-inclusive bp a uniform rate alone gives at least 61. **Both are UNTESTED** on the held bins, rest on unsourced inputs (tree, indel tail), and under A8 cannot score CRITIC alone.
- P1, P2, P6 and P7 (i), (iv) hit as registered; BGS adds at most 18% to the upper edge under SOURCED.
- **Against the critics' side, from their own steelman review:** at 3 and 10 Mb six cells are above the Francioli-edge upper bound (1.07 to 1.47 x N_hi; none DAY), so "inside at any W" does not hold for those four variants; the F2 φ_HC is above the lambda_M = 0 bound at W <= 10 kb and above the central neutral scenario at matched exposure; the registered FM10 defeater is not licensed; small block mechanisms are not excluded; nothing is said about sequence outside the alignable set.

**Both (neither side's credit list).**
- **R2, treated symmetrically.** R2 (SD ratio) is a reading the audit added. P3's hit (6,400 is DAY against every band at W <= 1 Mb) is a class of a number, not of the data; R2's non-reproduction for single lineages holds in both unit conventions, and for DHC depends on the convention (not reproduced in variance units except at 10 Mb unmasked; reproduced in SD units, class MARGINAL-OUT). Neither is a point for either side.
- **F0 (unmasked) classes.** The unmasked F0 excess, in φ and in φ_HC, is the reference-projection effect R4-FM measured (mirror test M1: at 100 kb φ_C 25.7 becomes 127.6 and φ_HC 8.54 becomes 18.0 when chimp is the reference; φ_H 36.9 / 34.9; F1 and F2 unchanged). The 10 to 23 ALN-dependent F0 cells per set, and the 6 to 9 above the masked-equivalent bound, are evidence for neither side (A5).
- **The audit's own errors**, which lower confidence in its engineering for both sides alike and are credited to no one: (a) P8 (i): the hand estimate (φ_HC > 10) was wrong (5.06 on the grid, 4.27 at random phase). (b) P8 (ii) held only because blocks and windows shared a grid. (c) The P4 / P5 label bug dropped twenty cells, and the first write-up miscounted the registered cell set (80 for 60). (d) The registered cost estimate for `analytic` was wrong: under a minute and 300 MB against about 11.5 minutes and, as reported by the launching agent, about 3.8 GB (section 9 item 4). (e) The first write-up compared φ_HC bounds and scenarios at c = 1 with measurements at exposure 0.54 to 0.64 and so called 10 kb "inside". (f) φ_cov is not a valid covariate-adjusted index (section 9 item 5). (g) A9's S2 rule cannot fire for the planted models. (h) P3's window estimate for TREE / PAIRS missed by 3 to 100 times; P7 (iii) is hit or missed depending on how its own wording is read.

## 9. Limits, and what looked wrong

1. **Severity (ST-10).** Sections 1 and 6a. A CRITIC class here is weak to partial evidence; the gate's flag is automatic for R1 with W free and its W restriction is equivalent to the own-data test; S2 as amended cannot fire. **The outcome observed (no DAY) is the weakly tested one.** DAY was reachable for the mechanism size Q169 (b) asserts (audit gloss: f e > 1) at 100 kb on masked sequence, and the data are 8 to 13 times (φ_H) and 22 to 31 times (φ_HC) below that scenario at matched exposure; the check has little power to return DAY for any planted mechanism below it, or for the dominant one on unmasked sequence.
2. **Unsourced brackets.** M0 (derived in AMENDED from a slope, not quoted), M2, M3, CPG, GBGC and its lineage-specific share, ALN, sd(B), every ell, the recombination rate in the ILS kernel, the TREE branch lengths, the indel tail factor and the exposure-CV bracket. Cells at W <= 30 kb, where the DAY classes sit, are flagged under-sourced. **Known sources the null leaves out, on the narrow side** (critic-side review): (i) the ILS sigma derived from Hobolth's N runs 0.30 to 0.54 in the sourcing refresh (`refresh-2026-10-12c-lit.md`) against an AMENDED upper edge of 0.398; (ii) FML-M3 attributes the large intragenomic variation in human / chimp divergence to long-term selection, against a BGS term that adds at most 18% here; (iii) R4-FM notes that every lineage field requires hs1 = hg38, which removes CHM13 minor alleles and errors from H while ape heterozygous sites and errors stay in C, B and G: private polymorphism of the sequenced ape is lineage-specific and absent from the φ_HC bound at lambda_M = 0; (iv) not held: replication-timing and recombination maps (fetch items), clustered multi-nucleotide mutation and parsimony misassignment at 1 kb. None of these changes a class at W <= 1 Mb, where no measured cell is outside the present band; they bear on the 3 to 10 Mb Francioli-edge cells and on the fine-scale φ_HC residual.
3. **P4 / P5 label mismatch** (section 5, "Defects"). Registered code, not changed. Resolved by the correctness review: P4 and P5 stand as scored on the truncated grid under the label REGISTERED, with the label-fixed `p45fix` numbers beside them; `post` is a separate computation.
4. **`analytic` cost.** Registered estimate: under 1 s, re-estimated in amendment 2 at under 1 minute and 300 MB. Observed: 11 min 26 s between the mtimes of `fmnull_selftest.out` and `fmnull_analytic.out`. `fmnull_analytic.out` carries no timing block (only `simulate` and `realdata` were wrapped in `/usr/bin/time`: 472 s CPU and 460 MB; 159 s CPU and 1.20 GB, both under their estimates), so the peak of about 3.8 GB is the launching agent's report and is not in the committed files. Likely cause, from the code and not profiled: P4's R2 rows. `inhouse()` evaluates `band()` at the extrapolated window, 0.1 to 13 Gb, and `window_var` builds arrays of W / 100 elements: 1.3e8 float64 values (about 1 GB each) with three or four alive at once in `cov_R`, for two band edges, twenty curves and two parameter sets. These rows are also the meaningless ones (windows longer than the genome). The envelope, which amendment 2 expected to dominate, works on windows of at most 10 Mb (1e5 elements).
5. **φ_cov.** At F0 the covariate-adjusted index for H is above the raw φ at W <= 100 kb (3.84 against 3.25 at 1 kb; 40.1 against 36.9 at 100 kb), and for DHC at F2, 1 kb (3.75 against 2.25). The correctness review explains it from the code: β comes from OLS on log((n + 0.5) / m) and the Pearson sum is then taken on E = m exp(Xβ); OLS on logs does not minimise the Pearson sum and weights low windows (and at 1 kb the pseudo-count) heavily, so adding covariates can raise it; a second symptom is that DHC F2 φ_cov falls from 3.75 at 1 kb to 3.33 at 3 kb. **φ_cov is not a valid covariate-adjusted index in either direction**, enters no score, and has been removed from the S1 row. That it lowers the F2 index at 1 Mb by 60% for H (89.4 to 36.0) and 68% for DHC (253 to 81.1) is therefore not listed as a result for the critic side either. Not re-estimated in this pass (a Poisson GLM with offset would need `fm_bins.npz` on na-workhorse; it is wanted only if S1's covariate clause is to be used, and the two maps of item 2 (iv) should be fetched first). The hs1 != hg38 covariate is itself a proxy for the local mutation rate, so removing it removes neutral heterogeneity, not artefact.
6. **NNLS fit of CV²(W)** (five fixed length scales): relative residual 0.01 to 0.10 at F0 and 0.28 to 0.33 at F2, so the F2 decomposition is poor. Fitted SD at 1 kb, 10 kb, 100 kb, 1 Mb, 10 Mb for H: F0 0.66, 0.27, 0.22, 0.08, 0.12; F2 0.36, 0.13, 0, 0.19, 0.08. These are totals over all processes and, by A12, are compared with brackets and never used to reset them: the F0 1-kb value (0.66) is above the M3 bracket (0.10 to 0.40), the F2 value inside it; the 1-Mb values (0.08 to 0.19) are at or below the SOURCED M1 bracket (0.20 to 0.25).
7. **R1u** is gated on the index over all windows, including windows that are mostly masked; at F2 that index (up to 5,692) largely measures the mask. The R1u classes use the unsourced CV_c bracket, not the measured values.
8. **Units.** Bonobo has no registered unit. TREE, PAIRS and BP are UNTESTED. The same ILS sigma is applied to every unit. Simulation arms use c = 1 and one 300-Mb chromosome; section 6a rescales their excesses to the F2 cell's exposure.
9. **NOWONG at 10 Mb**: the derived Francioli CV at the upper edge (0.101) is below the Jonsson CV at the lower edge (0.104). The bands stay ordered through exposure and the other components; the mutational term is inverted there.
10. **Scope** (also stated beside the gate, section 1 (a)) as R4-FM: alignable sequence only; centromeric satellites, rDNA and CHM13-only sequence are in no cell. If Day's windows include them, his index is not comparable with any number here.
11. Hand estimates in the registration used d = 0.012 for DHC; the table uses the bracket's upper end 0.0146 for N_hi (168 at 100 kb against the hand 133; the simulation at d = 0.012 gives 136 expected, 142 simulated).
12. **What the simulate arm validates** (correctness review). Validated: the PREREG and SOURCED corners N_lo, N_hi masked and N_hi unmasked for a single lineage at d 0.0051 and 0.012, four W (24 cells per set), against the finite-genome expectation. Not validated: (a) no AMENDED band is simulated; the two-locus ILS kernel is checked only algebraically (`hudson_cov_check`), and no simulated process has it; (b) K_hi: the BGS arm uses a different construction (clipped multiplicative field, ell 1 Mb) and is not compared with K_hi; (c) the two-lineage scenarios have an analytic counterpart only for the upper lineage-specific arm (6.05 against 6.21) and the fixed-component lambda_M arms; (d) TREE, PAIRS and BP bands: formula check for BP only.
13. **Units and masking of the real-data arm against the bands** are consistent in `post` (own exposure, own density, F0 against the unmasked band, F2 against the masked band). Three small mismatches, none moving a class: φ is exposure-weighted over windows with at least half their bases aligned, so its expectation is the band value times about (1 + CV_c²), at most 4%; one genome-wide p pools between-chromosome differences into φ at every W; F3 excludes CpG sites while the masked band keeps the CPG component (registered `inhouse` only). The registered `inhouse` uses c = 0.5 for N_lo and c = 1 for N_hi whatever the cell's exposure.
14. **Unit ambiguity of A7.** The amendment says "within [1/3, 3] x his value" and does not say whether, under R2, that is taken on the SD ratio or on the index; the code takes it on the index (within 1.73x in SD units). Both conventions are reported in section 4. No rule change here.
15. **The margin is symmetric about the stacked upper corner and is taken on the value, not the excess.** The undecided zone runs from N_hi / 3 to 3 N_hi, centred on N_hi: every component at its upper end at once, exposure 1, upper divergence. A value at the null's own centre scores CRITIC, and one at three times the centre is usually still CRITIC or MARGINAL-IN. For φ_HC, whose Poisson floor is 1, 3x on the value asks for far more than 3x the signal (at 10 kb, own exposure: 3.97, an excess 9.2 times the bound's). In the other direction, under SOURCED the central neutral simulation is itself MARGINAL-IN at 100 kb against the registered band (section 1). No rule change here (freeze procedure); a record beside ST-10 in the criticality layer is proposed for integration, together with the S2 criterion defect and the critic-side review's proposal for a fair Day-side criterion (a stated alternative at the size Day asserts and at a tenth of it; an interval for the one-lineage excess variance computed on both references; DAY if the interval excludes the whole neutral lineage-specific range, CRITIC if its upper end is 3x below the stated alternative), which belongs in `DECISIONS.md` under the freeze procedure and is not applied here.
16. **Block placement.** The registered block scenarios start every block on a multiple of Lb; `simphase` shows what that did (section 6). The "dominant" scenario is f e = 1, the boundary of the registered "f e > 1". Block lengths other than 20 and 100 kb were not simulated.

## Review resolution (fix pass, 2026-10-13)

Reviews: correctness (C, af8a960: 4 MAJOR, 8 MINOR, 6 NOTE), steelman-day (D, 5a36667: 6 MAJOR, 6 MINOR, 3 NOTE), steelman-critic (K, 64c2dba: 7 MAJOR, 6 MINOR, 3 NOTE). **No verdict value moves; all three reviews agree.** FM10 internal stays `pending` (owner decision). Every reviewer figure used above was recomputed from the committed json (`fixpass`, `p45fix`) or from the new simulation (`simphase`) before it was written in; differences from the reviewers' figures are noted in the rows. All new computations are **post hoc**, each script change committed and pushed before its run (57f2834, 3d508ef, 5463c7c), original outputs untouched. Where the two steelman reviews conflict, the lead's rulings apply (equal scrutiny; rule RD): one neutral Readings paragraph; power stated both ways; clean-inside and ALN-dependent counted separately; R2 and P3 treated symmetrically; the audit's own misses under "Both". Not done here, by the scope of this pass (only this file, the script and new raw outputs may change): entries in `QUEUE.md`, claim files, argmap, `REVIEW.md`, `DECISIONS.md` and the criticality layer; they are listed as proposals for integration.

### Post hoc results

| computation | registered / on grid | post hoc |
|---|---|---|
| P5, PREREG (cells the code scores; registered cell set) | 59 / 60; 44 / 45 | label fixed: 79 / 80; 59 / 60 |
| P5, SOURCED | 57 / 60; 43 / 45 | 75 / 80; 57 / 60 |
| P4 R1 + R1x, PREREG | CRITIC 40 / 40 | CRITIC 40 / 40 |
| P4 R1 + R1x, SOURCED | CRITIC 32, BELOW 8 | CRITIC 37, BELOW 3 |
| P8 (ii): dominant model φ_HC at 100 kb, PREREG / SOURCED (registered: > 100) | 103 / 103 (hit) | random phase 72.5 / 72.6; phases 1/4, 1/2, 3/4: 64.1, 52.5, 64.2 / 64.6, 53.0, 64.6 (miss) |
| P8 (i): 2%-doubling model φ_HC at 100 kb (registered: > 10) | 5.06 / 5.00 (miss) | random phase 4.27 / 4.21; fixed phases 3.57 to 3.97 (miss) |
| dominant model φ_H at 100 kb; class against the masked band | 283 / 328; DAY (4.76, 4.45 x N_hi) | random phase 204 / 248; DAY (3.44, 3.36); phase 1/2: 152 / 195, MARGINAL-OUT |
| dominant model against the measured F2 cell at matched exposure | φ_HC 56.8 against 1.81 (31x); φ_H 158 / 183 against 14.3 | φ_HC 40.0 (22x); φ_H 114 / 139 |
| φ_HC bound at lambda_M = 0, F2, 10 kb / 100 kb / 1 Mb | c = 1: 1.5 / 6.2 / 41 | own exposure: 1.323 / 3.85 / 21.8 (measured 1.333 / 1.81 / 3.49) |

### Correctness review

| id | sev. | decision | what changed |
|---|---|---|---|
| C1 | MAJOR | **Accepted.** | `inhouse_fix`, `selftest_fix` and mode `p45fix` added beside the unchanged `inhouse()`; run locally (1.1 s; the truncated grid reproduces the committed json exactly, cells and windows). Reviewer's numbers confirmed in full: P5 79 / 80 and 75 / 80 (registered cell set 59 / 60 and 57 / 60), P4 CRITIC 40 / 40 PREREG and 37 + 3 BELOW SOURCED, W80 shifts, 5 curves still extrapolated. One addition: with the label fixed the single R2 row whose band is evaluated (DHC F0, 31 Mb) is MARGINAL under PREREG and CRITIC under SOURCED. Section 5: P4 and P5 rows, SOURCED re-score and "Defects" rewritten as the three-way statement; "registered 80" corrected to 60 registered cells (45 scored plus 15 unregistered F1 cells); "sharpen the gorilla failure" withdrawn for P4. Departure from the suggested fix: the mode does not evaluate bands for R2 windows beyond 31.6 Mb (so it runs locally); those rows are reported as windows only |
| C2 | MAJOR | **Accepted.** | Own-exposure bounds computed for all nine W (`fixpass` E): 10 kb 1.323 against 1.333 measured, 100 kb 3.85, 1 Mb 21.8, as the reviewer found. Section 6: registered c = 1 table kept and labelled not like for like; own-exposure table added; "inside at lambda_M = 0 at all three W" withdrawn; status LAMBDA-DEPENDENT at 1, 3, 10 kb. Scenario comparison redone at matched exposure by rescaling the excess (section 6a) instead of rerunning at c = 0.58: measured φ_HC is 2.49 at c = 1; "the F2 values sit at the central neutral scenario" withdrawn for φ_HC. S2 stays unmet |
| C3 | MAJOR | **Accepted.** | Mode `simphase` (predictions in the docstring, 57f2834, before the run; na-workhorse, one process). Design note: instead of new block positions with a new seed, the registered seed and stream are replayed and the windows are shifted against the block grid, which is equivalent for a stationary field and lets phase 0 reproduce `fmnull_sim.json` exactly (maximum relative difference 0); "rand" uses a separate generator. Reviewer's reduced-run figures confirmed (dominant 53 to 64 at fixed phases; 2% model 3.6 to 4.0). P8 (ii) now reads "hit on the registered code, miss at any other phase"; per-lambda ratios recomputed per set and per phase; Critics bullet reduced to the numbers; scenario table carries off-grid columns |
| C4 | MAJOR | **Accepted.** | Section 4: R2 bullet replaced by a table in both unit conventions, with the unregistered combination (6,400 against the unnormalised index) as a labelled post hoc column: within 3x at 10 Mb for every lineage, DHC also at 3 Mb, classes MARGINAL-IN or CRITIC, none DAY, as the reviewer found. "Not a description of any measured quantity" and "R2 is not a property of the data" removed; every remaining sentence says "normalised" or gives both |
| C5 | MINOR | **Accepted**, in part. | φ_cov sentence removed from the S1 row; "covariate clause: not evaluated (estimator invalid)". Section 9 item 5 gives the reviewer's explanation and the proxy caveat. Not done: the Poisson GLM re-estimate (needs `fm_bins.npz` on na-workhorse; wanted only if the clause is to be used) |
| C6 | MINOR | **Accepted.** | Section 1 (a) rewritten: the flag is automatic, the W restriction is decisive, gated DAY is equivalent to the own-data test and is not a second observation. The former Critics bullets 1 and 2 are merged into the Readings paragraph and one Critics bullet |
| C7 | MINOR | **Accepted.** | Low-edge bullet leads with the own-exposure cells (G F0 38.1 against 72.7; 92.9 against 163.5); N_lo 80.4 and 80.6 given wherever "BELOW for gorilla" at W_T is stated, called boundary cases; both A4 labels kept; "below 1 Mb the low edge rests on the unsourced ell of M1" added |
| C8 | MINOR | **Accepted**, in part. | Ratios stated per set (PREREG 16.6, 5.3, 3.1; SOURCED / AMENDED 16.6, 4.5, 2.6) and after `simphase` (11.7, 3.7, 2.2; 11.7, 3.2, 1.8). S2 row: "not a severe test in either direction". φ_HC row: "no weight against a block mechanism up to f = 0.02, e = 1". The criterion defect is recorded in sections 1, 6 and 7 as a defect of the audit's criteria on Day's side. Not done here: the entry beside ST-10 in the criticality layer (proposed for integration; section 9 item 15) |
| C9 | MINOR | **Accepted.** | P7 (iii) scored reading-dependent (hit as central value; miss by 0.8% to 3.5% as band). The 18.6 added to the P8 (i) cell with the note that "10" and "3x" were inconsistent at registration |
| C10 | MINOR | **Accepted.** | P3: "3 to 100 times earlier (unmasked band); PAIRS-struct against the masked band from 3 Mb, as predicted". SOURCED: R2 rows MARGINAL 18 of 20, two DHC cells CRITIC (recounted from the committed json: F1 and F2) |
| C11 | MINOR | **Accepted.** | Heading reworded ("Yes for the PREREG and SOURCED corners (24 cells each) ...; the AMENDED bands and K_hi have no simulation arm"); (a) to (d) listed as section 9 item 12 |
| C12 | MINOR | **Accepted.** | (a) DHC F0 above the masked-equivalent bound: all eight sets at 1 kb, five of eight at 1 Mb (recounted). (b) 1.03 to 11.4. (c) BELOW in every variant from 100 kb for PAIRS-naive and BP-naive. (d) "within 5.2%" |
| C13-C18 | NOTE | Taken up. | C13: "no verdict value changes under either branch" stated in section 7. C14: gate column headed as a hybrid. C15: section 9 item 13. C16: no change beyond C12 (a). C17: "f e = 1 (boundary)" in P8 and section 9 item 16. C18: covered by C1 |

### Steelman review, Day's side

| id | sev. | decision | what changed |
|---|---|---|---|
| D1 | MAJOR | **Accepted** as fact; placement by the lead's ruling 1. | Verified: under R1 "more than 80" holds in all ten lineage-by-masking cells at 1 Mb and above (F2 85.1 to 89.5 for single lineages). It leads the results as the neutral Readings paragraph (sections 0 and 8), not as a first Day bullet, because the same paragraph must carry the critic-side half (not anomalous where true; K1). R1 named as the reading that sets the FM3 field, comment beginning `reading-dependent:`. "Has no meaning without W" replaced by "fixes no class without W". Section 3 says that where BELOW is listed at W >= 1 Mb his one-sided statement is true there |
| D2 | MAJOR | **Accepted**, with the lead's ruling 2 on wording. | Power table added (section 6a, `fixpass` G). Verified: all eight non-dominant block scenarios are CRITIC or MARGINAL-IN (on the grid 94 + 2 of 96; random phase 96 of 96); largest excess 1.95 times central neutral; dominant DAY only at 100 kb against the masked band and never against the unmasked band; DAY needs 15 / 6.9 (masked) and 34 / 14 (unmasked) times the central neutral index. Every "no DAY" sentence now carries the power qualifier (section 4, section 7 proposal 2, Critics bullet 1, section 9 item 1). Two limits on the review's own wording: its rider is restricted to "by the 3x class of φ alone" and stands beside what φ_HC says at matched exposure (K6); and "or not at all" is not adopted: the description is recorded with its power statement (K13) |
| D3 | MAJOR | **Accepted**, in part (lead's ruling 3). | Columns "clean inside", "ALN-dependent" and "above the masked-equivalent bound" added to the own-exposure table; reviewer's counts confirmed (clean inside 46, 50, 39 to 54; ALN-dependent 10 to 23; 6 to 9 above; DHC F0 1.06 to 1.70 at 1 kb to 300 kb in every set). "At or below the upper bound" dropped from the critic list; the F2 masked comparison is the headline. (b) stated in section 1 (which variants fail at the low edge; how wide the survivors are). Not accepted: listing "unmasked human-chimp φ above the masked-equivalent bound" as a Day-side item; those are the cells R4-FM's mirror test showed to follow the reference (verified: φ_C 25.7 to 127.6, φ_HC 8.54 to 18.0 at 100 kb), so they are under "Both" as evidence for neither side |
| D4 | MAJOR | **Accepted** (lead's ruling 4). | Gate reported in variance units (as coded: 1 of 10) and in SD units (DHC F0 at 1 to 10 Mb, DHC F2 at 3 to 10 Mb), with the class in the same units: 80 / sqrt(N_hi) 1.92 to 2.42 and 1.36 to 1.96 at 1 and 3 Mb (MARGINAL-OUT), 0.92 to 1.66 at 10 Mb (calibration-dependent); DHC F2 1.48 to 2.36 and 0.95 to 1.88; none DAY. Reviewer's figures confirmed. R2's non-reproduction moved out of "Critics" and P3's hit out of "Day"; both under "Both". A7's unit ambiguity recorded (section 9 item 14) |
| D5 | MAJOR | **Accepted** (lead's ruling 5); one part placed differently. | Gate scoped to the audit's alignable subset in section 1 (a) (limit 10 moved up); small-W R1 cells read UNTESTED / `unverifiable`, not "not reproduced", in sections 0, 4, 7. The two-sided conditional is stated once, in the neutral Readings paragraph of section 8, instead of as a sentence under each side (K7 objects to it as a Day point; ruling 1: neither credit nor failure) |
| D6 | MAJOR | **Accepted**, in part (lead's ruling 6). | φ_HC table extended to all nine W at own exposure; F2 above the lambda_M = 0 bound at 1, 3, 10 kb (2.82, 1.89, 1.03 times the bound's excess; reviewer's figures confirmed), marked LAMBDA-DEPENDENT; both statements given together (Day: exceeds the bound; critic: lambda_M of 0.04 to 0.07 absorbs it, verified by bisection under both sets). Criteria table has a "could it have been met?" column; bold "Unmet" replaced by "Not met" with that column; S2 at lambda_M = 0.5 recorded as a defect of the audit's criteria on Day's side and "S2 unmet" not counted against him. Reworded: not "no Day-side criterion was capable of being met" but "none could be met by a mechanism smaller than the one Q169 (b) asserts, and S2 not even by that off the grid" (S1 is met by the dominant planted model at 100 kb; K6). The F0 part is the projection effect (K5). S4: not queued here (this pass may not edit the queue); flagged for integration |
| D7 | MINOR | **Accepted.** | The reconstructed premise is written without quotation marks, as the audit's reconstruction (not Day's words; FM10 claim file); summary sentence added ("Q164 is a comparison with a uniform rate and ... is true as such") |
| D8 | MINOR | **Accepted.** | Section 5 opens by labelling the registered "Day side" / "critic side" expectations as audit gloss (rule S); P1 reworded; "(audit gloss)" wherever f e > 1 is used for Q169 (b) |
| D9 | MINOR | **Accepted.** | Riders added to the critic bullets (power, band width, scope, clean-inside count); the former Day bullet 6 (audit engineering) moved to "Both"; "follow Day's own practice" dropped and both unit readings labelled UNTESTED; the BP-struct mirror added to "Day" |
| D10 | MINOR | **Accepted**, in part. | Section 9 item 15 states both directions; ratio of excesses reported beside ratio of values for φ_HC (own-exposure table; 9.2 at 10 kb). Reviewer's "27.9" confirmed against the registered band. Not done here: the record beside ST-10 (proposed for integration) |
| D11 | MINOR | **Accepted.** | One ratio stated (band width above 9, the width of the rule's own undecided zone; a post hoc reporting convention, not a rule change) and applied per set in section 1; the clean CRITIC cell is given with its width 4.4 to 41 (two of six variants at or under 9) |
| D12 | MINOR | **Accepted.** | "(post hoc)" added to the criteria-table row and to the proposed FM3 comment text |
| D13-D15 | NOTE | No change asked. | D13: "Neither clause is met. No verdict move is proposed." kept as written |

### Steelman review, critics' side

| id | sev. | decision | what changed |
|---|---|---|---|
| K1 | MAJOR | **Accepted**; placement by the lead's ruling 1. | Cross-tabulation verified exactly (14 cells; 112 set-cells: CRITIC 37, MARGINAL-IN 61, BELOW-NEAR 14; none above N_hi; φ / N_hi 0.11 to 0.91; single lineages 32 / 18 / 14, largest 0.77). It leads the results in the neutral Readings paragraph (with D1's half) rather than at the head of "Critics". FM3 external comment proposed: `supported` as a description, non-discriminating |
| K2 | MAJOR | **Accepted.** | Verified: NOT-HIGH in all six variants in 11 of 12 masked cells at W >= 1 Mb (exception H at 1 Mb). Added to section 3f, the W_T paragraph and the criteria table; Day bullet reworded. No CRITIC is scored from it (A4) |
| K3 | MAJOR | **Accepted** (lead's ruling 9). | Heading changed to "Low edge: the pedigree-calibrated bound exceeds the data"; both A4 labels given; new Critics bullet. Verified: measured excess CV at 1 Mb 0.170 / 0.180 (H), 0.114 / 0.146 (G) against FML-S2's 0.15, 0.18, 0.27. The Day bullet keeps the calibration point and points to the anomaly label |
| K4 | MAJOR | **Accepted** (lead's ruling 8). | Lineage table in section 0, before the severity section; second Critics bullet. Verified: φ_H / φ_C 0.97 to 1.04 (1 kb to 3 Mb), 0.88 at 10 Mb; φ_H / φ_B 0.99 to 1.06; CV² H / C 1.04 to 1.13; corr(H, C) 0.87, 0.92, 0.96, 0.98 |
| K5 | MAJOR | **Accepted** (lead's ruling 3). | Mirror test cited wherever ALN or F0 is discussed (sections 0, 1, 3, 4, 6, 7, 8), with the two-reference numbers verified from `fm_analyse.json` and `fm_mirror_analyse.json`. "Unsourced" for ALN now reads "no paper quantifies it; measured in-house by R4-FM (M1)". F2 against the masked band (35 of 35 at or below N_hi; 0.57 to 0.91) is the headline count |
| K6 | MAJOR | **Accepted**, in part. | "What the data bound" table added (section 6a). Verified with small differences: at matched exposure the data are 11 to 13 times below the dominant scenario in φ_H (reviewer: 12 to 14) and 31 times in φ_HC; off the grid 8 to 10 and 22 times. f e² bound 0.0065 to 0.0085 (Lb 100 kb) and 0.02 to 0.03 (Lb 20 kb) on the grid, looser off it (to 0.035): "at least about 29 times short" in place of 30. P8 (i) moved from Day's credit to "Both" as an audit error (lead's ruling 7); its content as a limit of S2 stays on Day's side. Not adopted as worded: "low power only against mechanisms too small to be 'dominant'": the dominant model is also not DAY against the unmasked band or at 10 kb and 1 Mb, and S2 cannot fire for it; both are stated |
| K7 | MAJOR | **Accepted** (lead's ruling 1). | The W <= 10 kb class of the number 80 is an extended reading (rule RD) in the Readings table: UNTESTED, `unverifiable`; removed from the Day list. Section 7: "formally met, by classes of a number at windows, and under a reading, where the measured data do not show it". The conditional is kept, once, in the neutral paragraph (D5) |
| K8 | MINOR | **Accepted.** | P3 row: "a class of the number, not of the data; no measured SD ratio exceeds 80"; R2 treated symmetrically under "Both" |
| K9 | MINOR | **Accepted.** | 3 and 10 Mb own-exposure classes computed (`fixpass` D) and reported in section 4 and under "Critics" as a finding against the critics' side. With bonobo included the cells above N_hi under the Francioli-edge variants are six: F2 3 Mb H 1.22, C 1.09, B 1.07, DHC 1.43; F2 DHC 10 Mb 1.14; F0 DHC 10 Mb 1.47 (the reviewer's sixth, F0 DHC at 3 Mb, is at 1.00, just under). "At any W" removed |
| K10 | MINOR | **Accepted**, in part. | Section 9 item 2 lists (i) to (iv) with ids; the φ_HC row reads "inside at lambda_M = 0 from 30 kb; at 1 to 10 kb inside from lambda_M about 0.05 (F2)"; the argmap proposal carries the number. Not done here: queueing the two maps |
| K11 | MINOR | **Not accepted** as a critic bullet. | The figures are right arithmetically (60% for H, 68% for DHC at F2, 1 Mb), but the correctness review (C5) found the φ_cov estimator invalid in either direction; a result that rests on it is listed for neither side (section 9 item 5) until it is re-estimated |
| K12 | MINOR | **Accepted** as a proposal only. | Recorded in section 9 item 15 for `DECISIONS.md` under the freeze procedure; no rule change in this write-up; not written to `DECISIONS.md` by this pass |
| K13 | MINOR | **Accepted.** | Proposal 2 records the description together with its power statement; the argmap suggestion (a defeater on the R4-FM sentence, reading-dependent, not on FM10's verdict) is passed to integration |
| K14-K16 | NOTE | Taken up. | K14 ("where the critics' case stops") is the last Critics bullet |

Conflicts between the two steelman reviews, as listed by the critic-side review, and how each was settled: D3 (a) against K5: F0 cells count for neither side (K5), counted separately as D3 asks. D6 (a) F0 part against K5: projection effect. D6 (a) F2 part against K10: both statements, always together. D2 against K6 and K13: power both ways in one section; the rider is restricted and the description kept. D5 against K7: scoping accepted, conditional stated once and neutrally. D4 against K8: symmetric, under "Both". D6 (b) against K6: reworded to what the simulations show.
