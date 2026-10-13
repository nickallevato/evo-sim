# R4-FMnull: neutral-null calibration of Day's "more than 80 times more variable" (FM3, Q164)

Status: **run and scored; NOT yet reviewed** (load-bearing tier: correctness, steelman-day and steelman-critic reviews to follow; nothing here is integrated). Script `research/checks/fm_mesa_null.py` (md5 0b25eaf7…8cab68c, equal to the md5 in `raw/fmnull.host`). Registered 48241c7 (2026-10-12); post hoc amendment 1, pre-run, no data seen, cc5e6dd (parameter set SOURCED beside PREREG); post hoc amendment 2, pre-run, no data seen, 408ba53 (answers `REVIEW-R4-FMnull-prerun.md`: set AMENDED, calibration variants, symmetric classes, reproduction gate, readings R1u and U-BP). Only `selftest` had run before each of the three commits. Run 2026-10-13 on na-workhorse, one process, in the order selftest, analytic, simulate, realdata, post (17:06:42 to 17:28:37 UTC). Raw outputs committed 29245a8: `raw/fmnull_selftest.out`, `fmnull_analytic.{out,json}`, `fmnull_sim.{out,json}`, `fmnull_real.{out,json}`, `fmnull_post.{out,json}`, `fmnull.host`. The json files are the source of every number below. No code or score was changed after the run. Anything computed here beyond the printed outputs is marked **post hoc, descriptive**.

Target (verbatim, Q164, voxday.net "The Fourth Mechanism", 2026-10-10, ¶4): "The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts." It is claim FM3 and a premise of FM10 (Q171, ¶8: "What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable candidates.") and ROOT-FM. Day has released no window size W, no definition of the statistic, no lineage unit, no masking rule and no code (refreshes to 2026-10-12).

**What can and cannot be scored today.** The index of a count process over windows grows with W under every model with regional rate variation, so "80" has no meaning without W. The deliverable is therefore a lookup table (W x divergence -> neutral band) under three parameter sets, plus a statement of where the held alignment itself shows an index near 80. Day's number cannot be given one class. No verdict moves (section 7). The table can score his number the day he publishes W, statistic and unit: `fm_mesa_null.py score --W … --value 80 --reading … --unit … --exposure … --d … --real raw/fmnull_real.json`.

**Label for every result.** REGISTERED = computed and scored exactly as in 48241c7 with the brackets of set PREREG. SOURCED = the same code with the brackets of amendment 1. AMENDED = the amendment-2 outputs (json key `amend2`, mode `post`). All three were fixed before any run. Set PREREG's brackets are unsourced except the ILS sigma; SOURCED sources M1 sigma (Smith 2018, FML-S2), ILS sigma (Hobolth 2007, FML-H1, FML-H2) and the BGS ratio; AMENDED replaces the M0 and M1 corners by an envelope fitted to the three de novo mutation datasets in Smith 2018. Every length scale ell, and M2, M3, CPG, GBGC, ALN and the TREE branch lengths, are unsourced in all three sets.

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

Share of the upper edge that is sourced (post hoc, descriptive; first-order CV² of each component at its upper corner, set SOURCED): the two components with a sourced sigma (M1, ILS) carry 46%, 50%, 57% and 66% of the masked upper edge at 10 kb, 100 kb, 300 kb and 1 Mb, and 27%, 25%, 33% and 48% of the unmasked one. The alignment term ALN (unsourced; an artefact term, not an evolutionary process) alone is 41%, 49%, 43% and 28% of the unmasked upper edge. Under PREREG the sourced share of the masked edge is 31% to 56%, and ALN is 34% to 54% of the unmasked edge.

The two added points. (a) The reproduction gate, meant to restore severity, is near-automatic for reading R1 when W is unknown: the measured index rises monotonically from about 2 to several hundred between 1 kb and 10 Mb in every lineage, so it passes within 3x of 80 at some W by construction. The gate discriminates only for R2. (b) The lineage-specificity criterion S2, which ST-10 says the write-up should lead with, cannot be met at 100 kb by the planted block model the check registered, and at the upper lineage-specific share (lambda_M = 0.5) not even by the "dominant" block model (section 5, P8). So the Day-side empirical criterion is also weak, in the opposite direction: failing S2 says little.

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

## 3. Where "80" falls, by reading, unit and W (rule RD: every reading, none chosen)

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

Classes: DAY > 3 N_hi; M-OUT = MARGINAL-OUT (N_hi to 3 N_hi); M-IN = MARGINAL-IN (inside, above max(N_hi / 3, N_c)); CRITIC; B-NEAR, B-FAR = BELOW-NEAR / BELOW-FAR. "CAL (…)" = CAL-DEPENDENT: the six variants disagree, the classes they give are listed, no verdict move. "ALN:" = ALN-DEPENDENT: in at least one variant the class against the unmasked band differs from the class against the masked band, so the outcome rests on the unsourced artefact term and moves no verdict. The consensus and the ALN flag are aggregated here from the per-variant classes in `amend2.classes` by the rule of amendment A2 / A5 (the script prints the per-variant classes; `score2` applies the same rule to one cell).

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
- **CRITIC** as a clean consensus (not CAL- or ALN-dependent): R1 with DHC at 300 kb (masked and unmasked); R1 with TREE at 10 kb to 100 kb; PAIRS-naive and BP-naive at 1 to 3 kb; PAIRS-struct at 30 kb; BP-struct at 10 Mb. For the single-lineage units H, C and G **no W gives a clean CRITIC consensus against the masked band under R1**: the cells are M-IN, CAL-DEPENDENT or, unmasked, ALN-DEPENDENT.
- **BELOW** (80 under the neutral lower bound; "not high" for the critic, a bracket failure at the low edge for Day): R1 at W >= 1 Mb in at least one variant for every unit (CAL-DEPENDENT), and for PAIRS-naive and BP-naive at much smaller W: on those two unit readings the neutral lower bound itself is above 80 (in every variant from 300 kb for PAIRS-naive and from 1 Mb for BP-naive; in some variants from 10 kb).
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

| set / variant | CRITIC | MARGINAL-IN | MARGINAL-OUT | DAY | BELOW-NEAR | inside (CRITIC + M-IN) |
|---|---|---|---|---|---|---|
| PREREG | 23 | 46 | 1 | 0 | 0 | 69 / 70 |
| SOURCED | 45 | 15 | 0 | 0 | 10 | 60 / 70 |
| AMENDED ALL3, persist 1.0 | 48 | 17 | 0 | 0 | 5 | 65 / 70 |
| AMENDED ALL3, persist 0.5 | 38 | 32 | 0 | 0 | 0 | 70 / 70 |
| AMENDED NOWONG, persist 1.0 | 41 | 24 | 0 | 0 | 5 | 65 / 70 |
| AMENDED NOWONG, persist 0.5 | 23 | 47 | 0 | 0 | 0 | 70 / 70 |
| AMENDED FRANC, persist 1.0 | 34 | 17 | 0 | 0 | 19 | 51 / 70 |
| AMENDED FRANC, persist 0.5 | 24 | 46 | 0 | 0 | 0 | 70 / 70 |

- **No measured cell is DAY under any set.** One cell is above its upper bound: DHC, F0, 1 kb under PREREG (φ 9.5 against 8.8, ratio 1.09). The largest ratio φ / N_hi under any AMENDED variant is 0.97 (the same cell, NOWONG).
- **Failures at the low edge.** Under SOURCED, 10 cells fall below N_lo, 8 of them gorilla (F2 at 10 kb to 1 Mb; F0 at 100 kb to 1 Mb). Under FRANC with persistence 1.0, 19 cells do (all four single lineages at 300 kb and 1 Mb in F2, among others). The lower bound calibrated on pedigree mutation data over-predicts the dispersion of divergence at W >= 100 kb. The measured excess CV of the 1-Mb window mean, all processes together, is 0.17 to 0.18 for H and 0.11 to 0.15 for G, against 0.15, 0.18 and 0.27 for de novo mutations alone in Smith's three datasets. All BELOW cells disappear at persistence 0.5.
- **DHC at F0 is inside only through the alignment term** (post hoc, descriptive, from `post.cells`): at every W from 3 kb to 300 kb, and at 1 kb and 1 Mb in some variants, the measured DHC φ exceeds N_hi minus ALN_part (e.g. 100 kb: φ 210, masked-equivalent bound 132 to 187, unmasked bound 309 to 372). For H the same holds only at 1 to 3 kb. So "unmasked DHC is unremarkable" rests on an unsourced artefact bracket; with repeats and paralogs removed (F2) DHC is inside without it (100 kb: φ 38).

**Reproduction gate** (amendment A7; W unknown, so "REPRODUCED" means the measured index is within [1/3, 3] x Day's value at some measured W, and only classes at those W count). Bonobo has no registered unit; the chimp band is shown for it. R1x gives the same gate as R1 except that G masked also passes at 3 Mb.

| reading | unit | masking | gate | W where the measured index is within 3x | AMENDED consensus at those W | registered class, PREREG / SOURCED |
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
- **R1u: REPRODUCED for every lineage**, at 10 kb to 300 kb. The unnormalised index over all windows is 1.1 to 11 times the normalised φ and reaches 80 at smaller W (H, F0: 72 at 100 kb and 168 at 300 kb, against φ 37 and 70).
- **R2: NOT-REPRODUCED in 9 of 10 cells.** The held alignment gives no index within 3x of 6,400 for any single lineage at any W up to 10 Mb. The exception is DHC unmasked at 10 Mb (2,861, ratio 2.2), where the class is CAL- and ALN-dependent. On these data the SD-ratio reading is not a description of any measured quantity; the caveat, Day-side, is that his pipeline is unreleased.
- **UNTESTED**: TREE, PAIRS and BP units (not measurable on `fm_bins.npz`).

Classes at the reproduced windows: under AMENDED, **no reproduced cell is DAY**, and exactly one R1 cell is a clean CRITIC (DHC, masked, 300 kb: 80 against N_lo 13 to 71 and N_hi 313 to 501; measured φ there 89). Every other reproduced R1 cell is MARGINAL-IN, MARGINAL-OUT (DHC unmasked 10 kb), CAL-DEPENDENT or ALN-DEPENDENT. Under the REGISTERED rule every reproduced R1 cell is CRITIC under PREREG except DHC unmasked at 10 kb (MARGINAL); under SOURCED gorilla at 1 Mb and 3 Mb is BELOW.

**Post hoc, descriptive: the class of 80 exactly at the W where each lineage measures 80** (bands at the lineage's mean measured density, registered exposure bracket). PREREG: CRITIC in all ten (F0 and F2; H, C, B, G, DHC). SOURCED: CRITIC in eight, BELOW for gorilla in both filters. AMENDED consensus: ALN-DEPENDENT for F0 H, C, B and DHC; CAL-DEPENDENT for the other six (CRITIC or M-IN for F2 H, C, B, DHC; CRITIC or B-NEAR for G). None is DAY; none is a clean CRITIC.

R1u limit: the registered R1u classes use the unsourced exposure-CV bracket 0.2 to 0.5. `realdata` measured CV_c at 0.03 to 0.20 over used windows and 0.25 to 0.88 over all windows (F2 at W <= 30 kb is above the bracket). The classes were not re-scored with the measured CV_c in this chain (`score --cvc` exists). Amendment A8 already bars R1u from scoring CRITIC alone.

## 5. Predictions P1-P8, scored as registered

| # | Registered prediction (PREREG) | Result | Score |
|---|---|---|---|
| P1 | R1, DHC, masked: 80 inside the band at 100 kb (hand ~[5.7, 133]) and 1 Mb (~[24, 740]); above N_hi at W <= 10 kb (hand N_hi ~24) | 100 kb [3.4, 168] inside; 1 Mb [13, 916] inside; N_hi 31 at 10 kb, 13.7 at 3 kb, 6.1 at 1 kb, 80 above each (MARGINAL at 10 kb, DAY below) | **HIT** (3 of 3 parts). Critic's expectation (inside at >= 100 kb) met; Day's (above at every W <= 1 Mb) not met |
| P2 | R1, H: inside at 1 Mb (~[10, 310]); above masked N_hi at <= 100 kb (~55); inside unmasked N_hi at 100 kb (~120) | 1 Mb [6.0, 321] inside; masked N_hi 59.4 at 100 kb, 80 above (MARGINAL); unmasked N_hi 132, inside | **HIT** (3 of 3) |
| P3 | R2 (6,400) above N_hi unmasked at every W <= 1 Mb for H, C, G, DHC; inside only for TREE / PAIRS at W >= ~3-10 Mb, if at all. A Day-side point if it holds | Largest N_hi unmasked at 1 Mb is 1,405 (DHC): 6,400 is above for all four units at every W <= 1 Mb, and DAY (> 3x) throughout. Against the unmasked band TREE is inside from 300 kb, PAIRS-naive from 30 kb, PAIRS-struct from 1 Mb | **HIT** on the main clause: recorded as a Day-side point. **MISS** on the window estimate for TREE / PAIRS (inside 10 to 100 times earlier than ~3-10 Mb). Gate beside it (A7): R2 NOT-REPRODUCED in 9 of 10 cells |
| P4 *(informed, not predictive)* | Window at which the R4-FM φ reaches 80 lies where 80 is inside the band; CRITIC: every lineage; DAY: above by > 3x for some lineage; R2 only beyond 1 Mb | R1 and R1x: CRITIC in 40 of 40 cells (F0-F3; H, C, B, G, DHC). R2: reached only by extrapolation to 1.6e7 to 1.3e10 bp, MARGINAL in 19 of 20 | **CRITIC outcome observed**; no prediction credit (A10). Computed on a truncated grid, see "Defects" |
| P5 *(informed, not predictive)* | >= 80% of the R4-FM grid cells inside their band; audit guess: DHC F0 1 kb may lie above | 59 of 60 inside (98%); the one cell outside is DHC F0 1 kb (φ 9.51 against N_hi 9.01), as guessed | **Met**; no prediction credit. 60 cells, not the registered 80, see "Defects" |
| P6 | Simulated D within 15% of the exact expectation (D - 1) at W <= 1 Mb, every band cell; Poisson 1.00 +/- 0.05 | 24 of 24 band cells within 15%: ratio of excesses 0.973 to 1.073. Poisson means 0.967 to 1.034 | **HIT** |
| P7 | (i) BGS_hi adds <= 25% to N_hi unmasked at every W <= 1 Mb; (ii) corr(H density, gene-density covariate) < 0 under BGS; (iii) neutral φ_HC at 100 kb in [1, 6] masked; (iv) corr(H, C) >= 0.6 at W >= 100 kb, central neutral model | (i) 1.1% to 3.8%. (ii) -0.26, -0.37, -0.45 at 10 kb, 100 kb, 1 Mb: true by construction, reported and not scored (A13). (iii) 1.51 (central); the high lineage-specific arm gives 6.05 and the analytic bound 6.21, 1% and 3% over the stated top. (iv) 0.875 at 100 kb, 0.946 at 1 Mb | **HIT** on (i), (iii) central, (iv). (iii) is a near-miss if "[1, 6]" is read as the band rather than the central value |
| P8 | (i) Block model f = 0.02, e = 1, Lb = 100 kb gives φ_HC > 10 at 100 kb (> 3x the neutral upper bound); (ii) f e > 1 gives φ_HC > 100; (iii) Day side: f = 0.005, e = 0.5 is not detectable by φ alone | (i) φ_HC = 5.06: below 10 and below the neutral upper bound itself (6.05 simulated, 6.21 analytic). (ii) 103 at 100 kb (11.2 at 10 kb, 102 at 1 Mb). (iii) φ_H 11.9 (Lb 20 kb) and 12.6 (Lb 100 kb) against 11.6 neutral: inside the band | (i) **MISS**, and the miss counts for Day: a lineage-specific block mechanism doubling the rate over 2% of the genome is **not** visible to S2 at 100 kb. (ii) **HIT**, narrowly. (iii) **HIT**: credited as a limit of the critic's main test |

**P7 re-scored under SOURCED** (as amendment 1 requires): (i) BGS_hi adds 5.3% at 1 kb, 9.9% at 100 kb, 12.9% at 300 kb and 18.4% at 1 Mb: **HIT** at every W <= 1 Mb (22% at 3 Mb and 10 Mb, outside the registered range). The amendment's hand figures were ~8% and ~17%. (ii) -0.41, -0.48, -0.50, by construction. (iii) 1.50 central; 5.98 in the high lineage-specific arm. (iv) 0.955 and 0.986. P7 measures BGS against the upper bound of all other components, not the share of real variance BGS explains (FML-M3, FML-P1); that question is not answered here.

**The other predictions re-scored under SOURCED** (amendment 1: every prediction re-scored). P1: 100 kb [25, 210] inside; **1 Mb [143, 1,209]: 80 is BELOW the band, a miss at 1 Mb**, as amendment 1's hand figures anticipated; above N_hi at 10 kb (40.2), 3 kb and 1 kb. P2: 1 Mb [60, 423] inside; masked N_hi 73.8 at 100 kb, 80 above; unmasked 149, inside: hit. P3: main clause holds (largest N_hi unmasked at 1 Mb is 1,709). P4: R1 CRITIC in 32 of 40, **BELOW in 8 (gorilla, all four filters)**. P5: 57 of 60 (95%); the three outside are gorilla at 100 kb, F1 to F3, below N_lo. P6: 24 of 24, ratios 0.950 to 1.087; Poisson 0.972 to 1.032. P8: (i) 5.00, miss; (ii) 103 at 100 kb, 97.7 at 1 Mb; (iii) 30.8 and 32.5 against 32.0 neutral.

**Defects in the registered P4 / P5 computation (found at write-up; no code changed).** `inhouse()` maps window labels `1kb, 10kb, 100kb, 1Mb`, but `fm_analyse.json` names the last cell `1000kb`. The 1-Mb cells were silently skipped: P5 covers 60 cells (1 kb to 100 kb), not the registered 80 (1 kb to 1 Mb), and every P4 window except DHC F0 was extrapolated from the 10-kb and 100-kb points instead of interpolated to 1 Mb (H F0: 410 kb extrapolated against 382 kb measured; G F0: 1.93 Mb against 817 kb). The R2 windows are extrapolated to 16 Mb (DHC F0) and otherwise 0.1 to 13 Gb, beyond any chromosome and mostly beyond the genome; `realdata` shows the index never reaches 6,400. The corrected versions are the `post` own-exposure table and the W_T paragraph of section 4, which do not change the direction of P4 or P5 under PREREG and sharpen the gorilla failure under SOURCED.

## 6. Amendment-2 outputs, and the simulate arm

**Classes for Day's 80**: sections 3c to 3e. **CAL-DEPENDENT cells**: under R1 and the masked band, 20 of the 36 single-lineage and DHC cells are clean; the CAL-DEPENDENT ones are H 30 kb, C 100 kb, G 300 kb, DHC 30 kb, and every unit at W >= 1 Mb. The disagreement at W >= 1 Mb is persistence: with the pedigree CV taken as a floor (1.0), 80 is BELOW; with half of it persisting (0.5), 80 is CRITIC. **ALN part**: section 2c and the ALN flags in 3c; under R1 the unmasked class differs from the masked class for H at 30 kb to 1 Mb, C at 10 kb, 100 kb and 300 kb, G at 10 kb, 30 kb and 300 kb, DHC at 3 kb, 30 kb and 100 kb. **K_hi comparison** (Q171 names selection as well as drift): no cell is DAY against N_hi and CRITIC against K_hi; adding BGS to the unmasked band moves boundary cells by at most one class (H 10 kb: DAY -> CAL (DAY, M-OUT); DHC 3 kb: CAL (DAY, M-OUT) -> M-OUT; H 300 kb: CAL (M-IN, CRITIC) -> CRITIC). **Reproduction gate**: section 4. **R1u and U-BP**: sections 3d, 4; U-BP is UNTESTED on the held bins. Under BP-naive a uniform-rate process alone gives D >= 61 at every W (structural floor; N_lo 62 to 65 at 1 kb), as the amendment's hand figure said; under BP-struct the bands are the lowest in the table and 80 is DAY to 30 kb.

**φ_HC neutral upper bound (S2, amendment A9)**, c = 1, against the measured split dispersion:

| W | bound masked, lambda_M = 0 / 0.25 / 0.5 | measured F2 (exposure) | bound unmasked, lambda_M = 0 / 0.25 / 0.5 | measured F0 (exposure) |
|---|---|---|---|---|
| 10 kb | 1.5 / 4.1 / 6.7 | 1.33 (0.64) | 10.8 / 13.8 / 16.8 | 2.72 (0.94) |
| 100 kb | 6.2 / 22.7 / 39.4 | 1.81 (0.58) | 75 / 94 / 113 | 8.54 (0.92) |
| 1 Mb | 41 / 140 / 240 | 3.49 (0.54) | 207 / 310 / 415 | 24.1 (0.91) |

(SOURCED and AMENDED rows, which are equal; PREREG differs only at lambda_M > 0: 3.8 / 6.0, 19.6 / 33.2, 114 / 188 masked.) The measured masked φ_HC is inside the bound at lambda_M = 0 at all three W, which under A9 is the critic-side outcome for "φ_HC inside its neutral band". The measured unmasked φ_HC is inside the unmasked bound but above the masked lambda_M = 0 bound at 10 kb and 100 kb (2.72 against 1.5; 8.54 against 6.2), so at F0 it is inside only through ALN or a lineage-specific mutational share.

**Simulate arm: does the simulation reproduce the analytic bands?** Yes, per scenario:

| arm | set | simulated against expected | 
|---|---|---|
| P6 band cells (N_lo, N_hi masked, N_hi unmasked; d 0.0051 and 0.012; 1 kb to 1 Mb; 300 Mb x 10 replicates; expectation with the finite-genome correction) | PREREG | excess ratio 0.973 to 1.073 (24 cells) |
| same | SOURCED | 0.950 to 1.087 (24 cells) |
| Poisson baseline | both | 0.967 to 1.034 (largest replicate SD 0.11 at 1 Mb) |
| R1u formula (amendment 2; fixed test components, not a parameter set) | n/a | 13.8 / 13.7, 81.8 / 80.5, 205 / 194 at 10 kb, 100 kb, 1 Mb (within 6%) |
| U-BP compound formula | n/a | 38.3 / 38.3, 133 / 133, 429 / 418 (within 3%) |
| φ_HC with lambda_M = 0.25 and 0.5 | n/a | 2.31 / 2.35, 11.9 / 12.1, 39.8 / 39.1; 3.11 / 3.18, 18.0 / 18.3, 57.0 / 54.2 (within 5%) |

The largest deviations are at 1 Mb (300 windows per replicate), at the upper corner.

Two-lineage scenarios at 100 kb (H 0.0051, C 0.0057, c = 1; central neutral model plus the stated change):

| scenario | set | φ_H | φ_C | φ_HC | corr(H, C) | φ_res H (R4-FM shared-rate null) |
|---|---|---|---|---|---|---|
| S0 neutral, central | PREREG / SOURCED | 11.6 / 32.0 | 12.8 / 35.5 | 1.51 / 1.50 | 0.88 / 0.95 | 2.86 / 2.84 |
| S0 with lineage-specific gBGC at the upper edge | PREREG / SOURCED | 16.2 / 36.5 | 18.5 / 40.7 | 6.05 / 5.98 | 0.64 / 0.83 | 11.6 / 11.5 |
| S1 BGS at the upper edge (ell 1 Mb) | PREREG / SOURCED | 13.5 / 43.4 | 14.9 / 48.1 | 1.53 / 1.51 | 0.89 / 0.97 | 2.89 / 2.87 |
| S2 blocks, Lb 20 kb, e 0.5, f 0.005 | PREREG / SOURCED | 11.9 / 30.8 | 13.1 / 34.2 | 1.60 / 1.56 | 0.87 / 0.95 | 3.04 / 2.97 |
| S2 blocks, Lb 100 kb, e 0.5, f 0.005 | PREREG / SOURCED | 12.6 / 32.5 | 13.1 / 35.1 | 1.76 / 1.78 | 0.86 / 0.94 | 3.46 / 3.52 |
| S2 blocks, Lb 100 kb, e 1.0, f 0.02 | PREREG / SOURCED | 21.7 / 41.8 | 12.7 / 34.7 | 5.06 / 5.00 | 0.64 / 0.83 | 12.7 / 12.6 |
| S2 dominant, Lb 100 kb, e 2, f 0.5 | PREREG / SOURCED | 283 / 328 | 12.6 / 35.4 | 103 / 103 | 0.25 / 0.40 | 260 / 260 |

Measured at 100 kb for comparison: F2 φ_H 14.3, φ_C 14.7, φ_HC 1.81, corr(H, C) 0.87 at exposure 0.58; F0 36.9, 25.7, 8.54, 0.52 at exposure 0.92. R4-FM's φ_res at F2, 100 kb is 2.7 (H) and 2.4 (C). Post hoc, descriptive: the F2 values sit at the central neutral scenario (φ_HC 1.5, φ_res 2.9, corr 0.88) and equally at the small-block scenarios (φ_HC 1.6 to 1.8, φ_res 3.0 to 3.5, corr 0.86 to 0.87); the two are not separable by these statistics. The large-block and dominant scenarios (φ_HC 5 and 103, φ_res 13 and 260) are far from the F2 measurement. The F0 φ_HC of 8.5 is above both the central neutral value and the 2%-of-genome block model, and inside the unmasked bound only through ALN.

**P8 re-scored per lambda_M (A9).** At 100 kb the neutral upper bound for φ_HC (masked) is 6.2, 22.7 and 39.4 at lambda_M = 0, 0.25, 0.5. The registered block model (5.06) is below all three. The dominant model (103) is 16.6, 4.5 and 2.6 times the three bounds: it clears the 3x rule at lambda_M = 0 and 0.25 and **fails it at lambda_M = 0.5**. Since A9 lets S2 score DAY only above 3x the bound at every lambda_M, S2 as amended cannot be met at 100 kb even by a mechanism that triples the rate over half the genome on one lineage. At 10 kb the ratios are 7.3, 2.7, 1.7; at 1 Mb 2.4, 0.7, 0.4.

## 7. Criteria S1-S4, and proposed effect on verdicts (proposals only)

| criterion (registered; DAY if met by > 3x the neutral upper bound) | status on the held alignment |
|---|---|
| S1: index far above N_hi at every plausible W, and after covariate regression | **Unmet.** No measured cell is above 3 N_hi under any set; one of 70 is above N_hi at all (DHC F0 1 kb, PREREG, 1.09x). Covariate regression lowers φ at W >= 300 kb (H F2 1 Mb: 89 to 36) and does not raise any cell toward the bound that matters. Limits: under SOURCED 34% to 54% of the masked upper edge is unsourced, and the unmasked edge leans on ALN |
| S2: φ_HC > 3x its neutral upper bound | **Unmet.** Masked φ_HC 1.33, 1.81, 3.49 against bounds 1.5, 6.2, 41 at lambda_M = 0. Under A9 this is the critic-side outcome (inside at lambda_M = 0) for F2. **Weak test**: P8 (i) missed, and at lambda_M = 0.5 the criterion is unreachable by the registered block models |
| S3: edges sharper than the shortest-ell component allows, and \|Spearman\| < 0.1 with covariates | **Untestable** on 1-kb bins (A13); scores for neither side |
| S4: tree-incongruent sharing above the ILS rate | **Not tested** by this script. corr(H, G) is below corr(H, C) at every W (F2 100 kb: 0.74 against 0.87), which is not an S4 test |
| Critic-side: index inside the band at Day's W | **Not scoreable** (W unknown). At the W where the data measure 80: CAL- or ALN-dependent, never DAY, never a clean CRITIC except DHC masked at 300 kb |
| Critic-side: mesas shared across lineages | corr(H, C) at F2: 0.57, 0.87, 0.96 at 10 kb, 100 kb, 1 Mb, against 0.63, 0.88, 0.95 in the central PREREG simulation and 0.80, 0.95, 0.99 under SOURCED. At F0: 0.33, 0.52, 0.77, below both. The registered expected-correlation formula was not evaluated per cell by the script |
| Critic-side: φ_HC inside its neutral band | Met at F2 at lambda_M = 0; at F0 LAMBDA- or ALN-dependent |

**What the docstring licenses.** Registered rule: "CRITIC on every plausible reading" keeps FM3 external `supported` with the annotation "unremarkable against neutral heterogeneity at W" and gives FM10's premise a quantitative defeater; "DAY on the most charitable plausible reading" annotates FM3 "anomalous against the neutral band at W" and moves FM10 external toward `contested`. Amendment A7: a DAY or CRITIC class moves a verdict only if the real-data arm reproduces Day's number at that reading, unit and masking.

- **As registered, without the gate**, the Day-side clause is formally met: R2 is DAY at every W <= 1 Mb for every single-lineage unit (P3, a hit), and R1 is DAY at W <= 10 kb. The critic-side clause is not met (R2 and small-W R1 are not CRITIC).
- **With the gate (pre-run amendment 2, the rule in force)**: R2 is NOT-REPRODUCED, so its DAY classes do not count; R1 at W <= 10 kb is not reproduced for single lineages (measured 2 to 10) and DHC at 10 kb is M-OUT. No reproduced cell is DAY. The critic-side clause needs CRITIC on every plausible reading and has one clean reproduced CRITIC cell under R1 (DHC, masked, 300 kb). **Neither clause is met. No verdict move is proposed.**

Proposals for integration, after the three reviews:
1. **FM3** (`internal: holds`, `fidelity: unverifiable`, `external: supported`): no change. Proposed comment text only: the measured index reaches 80 at 382 kb (H, F0) to 933 kb (G, F2) and at 25 kb to 261 kb for DHC, on a nine-point grid; against a mechanistic neutral band 80 is DAY below about 10 kb, MARGINAL from about 30 kb to 300 kb and calibration-dependent from 1 Mb, so the claim's weight is set by an unreleased W; the SD-ratio reading (D > 6,400) is not reproduced by the held alignment. Fidelity stays `unverifiable` (rule F). A Readings table per rule RD should carry R1, R1x, R1u, R2 and the unit sub-readings with the classes of section 3.
2. **FM10** (`internal: pending`, `external: contested`): no change. Internal stays `pending` by owner decision until Day releases his method. External is already `contested`; nothing here moves it in either direction. The quantitative defeater against "drift implies a uniform rate" is **not licensed** by the registered rule (CRITIC on every reading is not met). What may be recorded, as description and with its limits, is that no measured cell exceeds three times the neutral upper bound at any W from 1 kb to 1 Mb.
3. Day-side items for the argument map, if the reviews agree: S2 is not a severe test (P8 miss; unreachable at lambda_M = 0.5); the pedigree-calibrated lower edge fails for gorilla; unmasked DHC is inside only through an unsourced artefact term.
4. Critic-side items: R2 is not a property of the data; under gap-inclusive bp a uniform-rate process alone gives an index of at least 61, and under all-pairs sums 7.9 (structure of the unsourced tree); the measured indices are inside the band in 51 to 70 of 70 cells.

## 8. Who this helps

**Day.**
- There is a reading and a window range where 80 exceeds every neutral band by more than 3x under all six calibration variants: R1 with a single lineage at W <= 10 kb (DHC at <= 3 kb), and R2 at every W <= 1 Mb. If Day's windows are 10 kb or smaller and his statistic is a normalised variance-to-mean ratio, his number is far outside the neutral band as modelled here. The check cannot exclude that, because W is unreleased, and the real data do not show 80 at those windows (H: 3 to 10).
- For single lineages no window gives a clean CRITIC consensus under the amended, symmetric rule. The registered CRITIC classes under PREREG come from a band about 60-fold wide.
- The null over-predicts at the low edge. SOURCED and the persistence-1.0 variants put gorilla, and under FRANC every lineage, below the lower bound at W >= 100 kb to 300 kb. A model that is wrong at the bottom is weaker evidence when it says "inside" at a neighbouring W.
- Most brackets are unsourced, and several could be too generous to the null: ALN supplies 28% to 54% of the unmasked upper edge and is the only reason unmasked DHC is inside; the Wong dataset's 0.27, which Smith's abstract attributes to possible technical differences, sets the ALL3 upper edge and doubles N_hi at 1 Mb relative to Francioli; every ell is a guess.
- P8 (i) missed in Day's favour: a block mechanism doubling the human rate over 2% of the genome is invisible to S2 at 100 kb, and a small one (0.5% of the genome, +50%) is invisible to φ. The measured F2 statistics do not separate the central neutral model from small-block models.
- The audit's own engineering estimate was wrong: `analytic` was registered at under a minute and 300 MB and took about 11.5 minutes and, as reported by the launching agent, about 3.8 GB (section 9). Its registered P4 / P5 computation dropped the 1-Mb cells through a label mismatch.

**Critics.**
- On the held alignment no measured index is above three times the neutral upper bound at any W, lineage or masking, under any parameter set; 69 of 70 cells are at or below the upper bound under PREREG and 70 of 70 under SOURCED and AMENDED.
- At every W where the data themselves show an index near 80 (100 kb to 1 Mb for single lineages), 80 is inside the band or below it under every set. The DAY region (W <= 10 kb) is one where the data show 2 to 10, not 80.
- The R2 reading, the only one that is DAY at every window, is not reproduced: no single lineage reaches 6,400 at any W up to 10 Mb.
- Two readings of "substitution density across the genome" that follow Day's own practice elsewhere (sums over all pairs; gap-inclusive base pairs) put the neutral lower bound at 10 to 65 at 1 kb and above 80 from 10 to 100 kb; for gap-inclusive bp a uniform rate alone gives at least 61, so under that reading "80 times a uniform-rate process" needs almost no rate variation. Both are UNTESTED on the held bins and rest on unsourced inputs (tree, indel tail).
- H and C densities are correlated at 0.87 (100 kb) to 0.96 (1 Mb) on repeat-masked sequence, as the central neutral simulation gives (0.88, 0.95), and the masked φ_HC (1.8 at 100 kb) is inside the neutral bound at lambda_M = 0. The large-block and dominant block models are far from the measurement.
- P1, P2, P6 and P7 (i), (iv) hit as registered; BGS adds at most 18% to the upper edge under SOURCED.

## 9. Limits, and what looked wrong

1. **Severity (ST-10).** Section 1. A CRITIC class here is weak to partial evidence; the gate is near-automatic for R1 with W free; S2 is weak in the Day direction. The check is a severe test only of the outcome it did not find (DAY at a reproduced window).
2. **Unsourced brackets.** M0 (derived in AMENDED from a slope, not quoted), M2, M3, CPG, GBGC and its lineage-specific share, ALN, sd(B), every ell, the recombination rate in the ILS kernel, the TREE branch lengths, the indel tail factor and the exposure-CV bracket. Cells at W <= 30 kb, where the DAY classes sit, are flagged under-sourced.
3. **P4 / P5 label mismatch** (section 5, "Defects"). Registered code, not changed. The reviews should decide whether P4 and P5 stand as scored on the truncated grid or are scored from `post`.
4. **`analytic` cost.** Registered estimate: under 1 s, re-estimated in amendment 2 at under 1 minute and 300 MB. Observed: 11 min 26 s between the mtimes of `fmnull_selftest.out` and `fmnull_analytic.out`. `fmnull_analytic.out` carries no timing block (only `simulate` and `realdata` were wrapped in `/usr/bin/time`: 472 s CPU and 460 MB; 159 s CPU and 1.20 GB, both under their estimates), so the peak of about 3.8 GB is the launching agent's report and is not in the committed files. Likely cause, from the code and not profiled: P4's R2 rows. `inhouse()` evaluates `band()` at the extrapolated window, 0.1 to 13 Gb, and `window_var` builds arrays of W / 100 elements: 1.3e8 float64 values (about 1 GB each) with three or four alive at once in `cov_R`, for two band edges, twenty curves and two parameter sets. These rows are also the meaningless ones (windows longer than the genome). The envelope, which amendment 2 expected to dominate, works on windows of at most 10 Mb (1e5 elements).
5. **φ_cov.** At F0 the covariate-adjusted index for H is above the raw φ at W <= 100 kb (3.84 against 3.25 at 1 kb; 40.1 against 36.9 at 100 kb), and for DHC at F2, 1 kb (3.75 against 2.25). A regression that raises the dispersion is suspect (log-linear fit with a 0.5 pseudo-count against a Pearson statistic). φ_cov enters no score; the correctness review should look at it before S1's "after covariate regression" is relied on.
6. **NNLS fit of CV²(W)** (five fixed length scales): relative residual 0.01 to 0.10 at F0 and 0.28 to 0.33 at F2, so the F2 decomposition is poor. Fitted SD at 1 kb, 10 kb, 100 kb, 1 Mb, 10 Mb for H: F0 0.66, 0.27, 0.22, 0.08, 0.12; F2 0.36, 0.13, 0, 0.19, 0.08. These are totals over all processes and, by A12, are compared with brackets and never used to reset them: the F0 1-kb value (0.66) is above the M3 bracket (0.10 to 0.40), the F2 value inside it; the 1-Mb values (0.08 to 0.19) are at or below the SOURCED M1 bracket (0.20 to 0.25).
7. **R1u** is gated on the index over all windows, including windows that are mostly masked; at F2 that index (up to 5,692) largely measures the mask. The R1u classes use the unsourced CV_c bracket, not the measured values.
8. **Units.** Bonobo has no registered unit. TREE, PAIRS and BP are UNTESTED. The same ILS sigma is applied to every unit. Simulation arms use c = 1 and one 300-Mb chromosome.
9. **NOWONG at 10 Mb**: the derived Francioli CV at the upper edge (0.101) is below the Jonsson CV at the lower edge (0.104). The bands stay ordered through exposure and the other components; the mutational term is inverted there.
10. **Scope** as R4-FM: alignable sequence only; centromeric satellites, rDNA and CHM13-only sequence are in no cell. If Day's windows include them, his index is not comparable with any number here.
11. Hand estimates in the registration used d = 0.012 for DHC; the table uses the bracket's upper end 0.0146 for N_hi (168 at 100 kb against the hand 133; the simulation at d = 0.012 gives 136 expected, 142 simulated).
