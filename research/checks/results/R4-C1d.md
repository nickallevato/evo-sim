# R4 C1d: Day's aDNA "21" statistic on the real AADR genotypes, and a replication of keruru's measured temporal N_e (B2e)

Scripts: `research/checks/c1d_aadr_real.py` (pre-registered in commit c0a4071, predictions P1-P16 in its docstring, before the main run). Post hoc, separate commits and labelled: `c1d_posthoc.py` (814f5da, fix in the next commit), `c1d_verify.py`, `c1d_figure.py`. Raw outputs: `results/raw/c1d_*` (v62 and v66 `_day`, `_ne`, `_groups`, `_posthoc`, `_verify`, `c1d_sim.json`, `c1d.host`). Figure: `results/R4-C1d-real-vs-day.png`.
Everything ran on na-workhorse (host and md5s in `raw/c1d.host`). The genotypes were downloaded there only and are not on the workstation or in git. Extraction used 6 processes (about 2 minutes per release), all other steps one process.

## Result in brief
1. **Day's scripts: not found.** The Z23046531 sentence "Analysis scripts are available from the authors at Zenodo" has no target. All records the Zenodo API returns for the creator filters (37 by ORCID, 38 by "Athos, Claude"; the repo's 2026-10-09 listing has 39 under "Day, Vox") hold only pdf/docx/odt/xlsx files; the `software` resource-type search returns 0 records; `related_identifiers` link no code; the AADR-paper record 23046531 holds a single pdf. So his method was re-implemented from his verbatim text, with every ambiguity run as a labelled reading.
2. **Day's table is not reproduced on the real genotypes, under any reading in the grid.** Literal reading (E1 eligibility, T2 dating, his European sample, v62.0.p1, 1,233,013 SNPs): **62,757 eligible alleles (Day 22,428), 4,957 events in the 5000-6000 BP and younger bins (Day 21)**, pre-7000 share 0.909 (Day 0.9986), tracked fraction 1.000 (Day 0.727). v66: 48,888 / 3,649. No configuration of the 120 tried on V1 (eligibility E1/E2/E1p x dating T2/T1 x min-calls 1, 5, 10, 20, 50 x two tracked rules x all/autosomal SNPs; 12 more on the PASS-only sample V2) came within 10% of his eligible count together with S21 within 50% of 21.
3. **What the thousands are.** 97.7% of the 4,957 are transitions (A/G, C/T; the panel is 77.6% transitions), 98.1% have a minor-allele frequency below 5% in the older bins (median 68 minor copies), and 4,177 of them sit in the 0-500 BP bin. Restricting to transversions (immune to deamination damage) gives **S21 = 113 (all chromosomes) or 36 (autosomes) on v62, 66 or 44 on v66**, with eligible 6,306-10,034 and pre-7000 share 0.98-0.99. So the number is highly sensitive to the substitution class (about 100-fold), and a transversion-only count is the same order as Day's 21 while his eligible total and his bin profile are still not matched.
4. **keruru's N_e replicates.** On v66 with his recipe (his formula, same bins and filters): **BA to Medieval 7,812 (his 8,139, -4.0%); Early Neolithic to Modern 9,672 (his 9,835, -1.7%)**; the other five windows are within 1-8%. SNP counts agree to 0.3%, mean sample sizes to 2-7%. The number is real. Its interpretation is the open part (section 4).
5. **keruru's sampling correction is half the standard one for pseudo-haploid data.** His formula `1/(2 S0) + 1/(2 St)` is right when S counts diploid individuals; his code feeds it a pseudo-haploid allele count. The correct correction is `1/n0 + 1/nt` (confirmed by simulation: pure binomial sampling gives F = 0.001921 against 1/n0 + 1/nt = 0.001917). Corrected, BA to Medieval is **9,665** (+24%) and Early Neolithic to Modern **10,508** (+8.6%). The error runs against his own conclusion's direction (corrected values are larger), so it does not rescue Day.
6. **Whether temporal N_e contradicts Wright's N_e = 4N/(V_k+2) is not decided by this data.** The temporal F contains every non-drift contribution (structure, composition change, relatedness, batch), so the estimate is a lower bound on a drift N_e. The same-time F between two European regions inside one bin is 0.006-0.055, i.e. 1-10 times the whole BA-to-Medieval temporal F (0.0053 on v66). Ancestry informativeness along the WHG / Anatolian-farmer / Yamnaya axes explains little of it (BA-Med top/bottom quintile ratio 0.96; EN-Modern 1.3).

## 1. Day's scripts (step 1)
- Searched (2026-10-09): Zenodo API record 23046531 (files, relations, versions), record 18525185, the creator-name and ORCID queries ("Day, Vox", "Athos, Claude", ORCID 0009-0003-4191-8985; 37-38 hits, all publications except one dataset, the LTEE xlsx), a `resource_type.type:software` query combined with the creator name (0 hits), and Day's own text for "github" (only an unrelated LTEE repository in Z23003785).
- Saved in `sources/raw/day-scripts-search-2026-10-09/` (gitignored): `rec23046531.json` (sha256 f8439d01...), `rec18525185.json` (3f936957...), `athos_p1.json` (14b2a91d...), `athos_p2.json` (ddafec29...), `versions23046530.json` (404).
- Consequence: the Z23046531 data-availability sentence is unfulfilled as of 2026-10-09. Nothing was executed.
- Method text used: Z18525185 s3.1-s3.4, s4.1, s4.3 (quotes in the script docstring). The two-period statistic of Z23046531 is a different quantity and is not computed here.

## 2. Data (steps 2-3)
- AADR v62.0.p1 (Dataverse 11.0, 7 June 2026; file ids 13994086 geno, 13987485 snp, 13987487 ind, 13994492 anno). md5 equal the Dataverse API values: geno 24419bba..., snp 50f66178..., ind 3f23dd87..., anno 6468eb19.... The v62 files have no published md5sum file; the only one is `v66.p1__files.md5sum`. Day cites "v62.0", the original of 16 Sept 2024 (Dataverse 9.0), which the API no longer serves; the p1 patch is what is used here (as in C1c).
- AADR v66.p1 1240K (file ids 13994829, 13994513, 13994514, 13994515, same as keruru's release). md5 equal the published md5sum file: geno 5ea1d267..., ind 19a434ac..., snp 50f66178..., anno a2db1ac1....
- Both genotype files are TGENO (transposed, one record per individual, 48-byte header, 2-bit codes, high bits first), not the PACKEDANCESTRYMAP that Z23046531 says. The script reads TGENO and GENO; the reader is checked on synthetic files of both kinds.
- Streaming: SNP blocks of 1,024 over 9.8k (v62) or 14.2k (v66) selected individuals, per-group sums by matrix product, 6 processes; peak RAM well under 14 GB. Per-SNP group counts stay on workhorse (`sources/raw/aadr-geno-2026-10-09/derived/`, about 0.7 GB per release).
- QC (P1): decoded autosomal call count per individual equals the anno "SNPs hit on autosomal targets" column exactly (correlation 0.9999997 on v62, 1.0 on v66; ratio median 1.000, IQR 1.000-1.000). Pseudo-haploid-labelled individuals have median heterozygote rate 0 (1-2 individuals each at 1.2-1.6%); `.DG` individuals median 0.27. Independent explicit bit-by-bit decode of three SNPs for three groups matches the matrix extraction (9 of 9 per release); a brute-force Python day_events on 20,000 random SNPs matches the vectorised code (1,032 and 785 eligible, identical profile); rs4988235 (LCT) counted-allele frequency by bin is 0.999 / 1.000 / 0.966 / 0.902 / 0.739 / 0.743 (v62) and ends at 0.733 on v66 (keruru's draft: 0.732).

## 3. Day's statistic, cell by cell (step 4)
Sample V1 = C1c's lat/long rule (v62: 8,808 individuals, per bin 167 / 133 / 669 / 579 / 726 / 1,155 / 1,015 / 1,000 / 2,125 / 715 / 524 against Day's 168 / 129 / 668 / 573 / 721 / 1,141 / 980 / 952 / 2,093 / 688 / 625; the 0-500 BP bin is 16% short, the other ten are within 5.1%). v66 has more individuals (12,335 in V1). Bins oldest to youngest: 10000+, 8000-10000, 7000-8000, 6000-7000, 5000-6000, 4000-5000, 3000-4000, 2000-3000, 1000-2000, 500-1000, 0-500.

Headline reading (E1, T2, any single call counts, tracked = observed in all 11 bins, all 1,233,013 SNPs, chromosome counting: pseudo-haploid = 1, diploid = 2):

| Quantity | Day (Z18525185) | Real v62.0.p1 | Real v66.p1 |
|---|---|---|---|
| eligible alleles | 22,428 | 62,757 (2.8x) | 48,888 (2.2x) |
| tracked | 16,299 (72.7%) | 62,747 (100.0%) | 48,886 (100.0%) |
| 10000+ | 3,038 | 45,815 | 35,753 |
| 8000-10000 | 8,741 | 10,444 | 8,342 |
| 7000-8000 | 4,497 | 771 | 627 |
| 6000-7000 | 2 | 760 | 515 |
| 5000-6000 | 9 | 268 | 213 |
| 4000-5000 | 7 | 111 | 66 |
| 3000-4000 | 2 | 144 | 109 |
| 2000-3000 | 1 | 88 | 33 |
| 1000-2000 | 0 | 4 | 1 |
| 500-1000 | 0 | 165 | 21 |
| 0-500 | 2 | 4,177 | 3,206 |
| pre-7000 share | 0.9986 | 0.9089 | 0.9148 |
| S21 (5000-6000 and younger) | 21 | **4,957** | **3,649** |
| S23 (6000-7000 and younger) | 23 | 5,717 | 4,164 |
| start frequency, fixed allele in the Neolithic: [99,100) / [95,99) / [90,95) / <90 | 79.2 / 20.2 / 0.5 / 0.2 % | 79.0 / 19.8 / 0.7 / 0.5 % | 87.3 / 12.4 / 0.2 / 0.0 % |

- **Start table (v62):** the only quantity that comes close to Day's, within 0.4 percentage points per cell. It is not sensitive to the dating or to the post-7000 counts, and v66 does not match it, so this is weak evidence that his sample was v62-like, not evidence that his procedure was reproduced. 50.3% of the 62,757 eligible alleles (31,541) have exactly one copy of the other allele in the pooled 6000-8000 BP sample (P7: singletons >= 40%, held).
- **Reading sensitivity (v62, S21 in parentheses):** autosomes only 54,243 (4,595); E2 eligibility 137,200 (4,957); a bin counts as observed only with >= 5 / 10 / 20 / 50 chromosomes: eligible 62,722 / 62,503 / 59,789 / 58,196, tracked 0.996 / 0.986 / 0.959 / 0.572, S21 4,953 / 4,935 / 4,794 / 3,301; "intermediate bins only" tracking: tracked >= 0.99 throughout; QC-restricted sample V2 (ASSESSMENT contains PASS): 60,409 (3,980). No setting gives tracked 0.65-0.80 (it jumps from 0.96 to 0.57 between m = 20 and m = 50). The T1 reading puts 53,863 of 62,747 events in the 0-1000 BP bins (Day: 2), so T1 is excluded by his own table, as C1c's correctness review argued; T2 is the only dating that can produce his profile shape, and it does not produce his profile.
- **A coincidence worth recording, not a result:** the post hoc rule "pooled Neolithic minor-allele count >= 2" gives 22,410 eligible on v66, against Day's 22,428; on v62 it gives 31,216, and in both its S21 (3,649 / 4,957) and profile are still far from his. Found among 8 rules after seeing the data; no weight.

### Anatomy of the post-6000 BP events (post hoc, v62 / v66)
| Subset | n | transition share | minor allele < 5% in older bins | median minor copies in older bins |
|---|---|---|---|---|
| S23 (6000-7000 BP and younger) | 5,717 / 4,164 | 97.1% / 97.3% | 5,607 / 4,152 | 61 / 77 |
| S21 | 4,957 / 3,649 | 97.7% / 98.2% | 4,861 / 3,640 | 68 / 84 |
| in the 0-500 BP bin | 4,177 / 3,206 | 98.5% / 99.2% | | 74 / 91 |
| dated 6000-7000 .. 500-1000 BP | 1,540 / 958 | 93.2% / 90.9% | | 6 / 6 |

- Typical event: rs11260588 (chr1), counted allele at 88% / 97.5% / 97% / 98% / 96% / 98% / 98% / 97% / 98% / 98% in the ten older bins and 901 of 901 chromosomes in the 0-500 BP bin. A near-fixed allele that the largest, mostly diploid shotgun bin happens to call as 100%. This is the mirror image of the 3,038-8,741-4,497 pre-7000 cluster (alleles near-fixed that the small old bins call as 100%).
- Substitution class (E1/T2, any call, 11-bin tracking): transitions S21 4,844 (v62) / 3,583 (v66); **transversions 113 / 66; transversions on autosomes 36 / 44**, eligible 6,306 / 7,614, pre-7000 share 0.989 / 0.990, start table [99,100) 99.0 / 99.5%. With the extra requirement of >= 5 minor copies in the pooled Neolithic sample, transversions give eligible 364 / 163 and S21 78 / 32.
- That transitions are over-represented ten-fold in the excess is what deamination-type error or the high mutability of transition sites would produce; this check cannot tell damage from real mutation-class-dependent differences between the ancient and modern bins. Not isolated further (a UDG-treated versus untreated comparison on the AADR library-type column is the natural next test).

## 4. keruru's temporal N_e (step 5; B2e, C5b)
Recipe as in his draft (v66.p1; Political Entity country regex with no UK/England in it; ASSESSMENT contains PASS; >= 10,000 autosomal SNPs hit, moderns exempt; 7 bins; 27 y per generation; F = sum (x-y)^2 / sum m(1-m); >= 20 individuals called). Forms: (K) his formula, (B) the same F with correction `1/n0 + 1/nt` in called chromosomes, (C) Nei-Tajima Fc (denominator m - xy). Groups: Meso 322, EN 1,665, LN 1,557, BA 1,846, Iron 1,828, Med 2,974, Modern 559 individuals.

| window (v66) | t (gen) | his reported | (K) here | (B) here [95% jackknife CI] | (C) here |
|---|---|---|---|---|---|
| BA to Medieval | 102 | 8,139 | 7,812 | 9,665 [9,267-10,098] | 9,691 |
| Early Neolithic to Modern | 250 | 9,835 | 9,672 | 10,508 [9,926-11,162] | 10,555 |
| Early Neolithic vs Mesolithic | 111 | 938 | 866 | 872 | 887 |
| EN to Late Neolithic | 65 | 4,922 | 4,706 | 5,954 | 5,973 |
| EN to Bronze Age | 120 | 6,933 | 6,761 | 8,273 | 8,303 |
| EN to Iron/Roman | 176 | 9,792 | 9,691 | 11,520 | 11,561 |
| EN to Medieval | 222 | 8,530 | 8,410 | 9,302 | 9,341 |

- (K) reproduces all seven of his numbers within 1-8%. His BA-Med F is 0.007183 against 0.007505 here; S = 842/1,548 against 782/1,444; SNPs 1,117,492 against 1,114,724. My v62 values (different release): BA-Med (K) 6,368, (B) 8,228; EN-Modern (K) 7,269, (B) 8,086.
- Generation-time sensitivity (B, 25-31 y): BA-Med 10,438-8,418; EN-Modern 11,348-9,152. Cumulative trajectory (B, anchored on Early Neolithic) rises 872 -> 5,954 -> 8,273 -> 11,520 -> 9,302 -> 10,508 as he reports.
- **Against Wright's frame.** With V_k = 5, 4N/(V_k+2) = 0.571 N. For N = 1e7 (keruru's own unsourced census, flagged in his ledger) that is 5.7e6, so the drift-only F in the BA-Med window would be 102/(2 x 5.7e6) = 9e-6, about 600 times below the measured corrected F of 0.0053 (v66; (B) Ne 9,665 gives N_e/N = 9.7e-4, 590 times below 0.571). Arithmetic, not a test: the data fix F, not N.
- **What F contains.** (i) Ancestry informativeness (per-SNP variance across WHG / Neolithic-Turkey / Yamnaya source samples, 1.0 M SNPs, quintiles): F_adj by quintile for BA-Med is flat (0.00536 -> 0.00516; top/bottom 0.96; intercept N_e 9,530); for EN-Modern 0.0104 -> 0.0136 (1.31x; intercept N_e 11,996); for EN-BA 0.0047 -> 0.0102 (2.14x; intercept 12,150); EN-Medieval 1.63x. So the three-way admixture axis matters only for windows that cross the steppe arrival, and even there removing it changes N_e by about 15-45%. (ii) Same-time spatial F: F_adj between two regional samples inside one bin (v66, BA bin) is 0.008-0.055 (Iberia-Central 0.019, Central-Italy/Balkans 0.016, Central-Scandinavia 0.008, Central-Eastern Europe 0.023, Italy/Balkans-Eastern Europe 0.049) and 0.006-0.044 in the Medieval bin, against 0.0053 for the whole BA-to-Medieval change. A shift in where the sampled people came from (of the individuals falling in the five regions, v66: Central Europe 37% of the BA sample but 65% of the Medieval one, Iberia 13% to 5%, Italy/Balkans 22% to 7%, Scandinavia 7% to 16%, Eastern Europe 22% to 7%) can therefore contribute F of the measured order without drift. Not quantified as a share. (iii) Not tested: relatedness and cemetery clustering (his draft states they are unfiltered), library and damage batch effects.
- **Reading.** Because every non-drift term adds to F, 9-10 thousand is a lower bound on a drift N_e, and the window-by-window rise (872 to 10,508) is what a growing population produces, but also what sampling progressively less regionally concentrated groups produces. The data neither confirm that Wright's N_e is wrong by three orders of magnitude (that needs F_nondrift to be a small fraction of 0.005) nor rescue it (that needs F_nondrift to be nearly all of it). Day's N_e near 2 (C5a) is excluded: the observed F_adj of 0.005-0.014 is nowhere near the saturation that N_e = 2 implies.

### Simulation of the estimator (c1d_sim.json; WF, N_e = 1e4, t = 100, 200k loci, pseudo-haploid n 800 / 1500, source drifted 700 generations, pulse at generation 50)
| pulse m | F | (K)/true | (B)/true | intercept/true |
|---|---|---|---|---|
| 0 | 0.00692 | 0.84 | 1.00 | 1.00 |
| 0.05 | 0.00674 | 0.86 | 1.04 | 1.06 |
| 0.10 | 0.00676 | 0.86 | 1.03 | 1.11 |
| 0.20 | 0.00736 | 0.78 | 0.92 | 1.23 |
| 0.40 | 0.01077 | 0.51 | 0.56 | 1.48 |
Closed N_e 3e4 and 1e5: (B)/true 1.00 and 0.99. Admixture invalidates the estimator only for large pulses from a well-differentiated source (here m >= 0.2 with source Fst of about 0.04; a 40% pulse halves the estimate). The informativeness-intercept correction over-corrects (1.23, 1.48), so it is not an estimator of the drift N_e, only a diagnostic. Real EN-to-Modern turnover (steppe about 40%, sources Fst 0.05-0.09 as assumed in C1c) is in the range where bias is substantial; the real-data gradient (1.3x top/bottom) is much weaker than a 40% pulse would give in the simulation, which is itself unexplained here.

## 5. Pre-registered predictions: what held
| P | Prediction (credence) | Result |
|---|---|---|
| P1 | layout/QC (95%) | **Held.** Correlation 0.9999997, ratio 1.000; pseudo-haploid het 0; `.DG` het median 0.27. |
| P2 | V1 within 5% in 9 of 11 bins, 8,808 total (90%) | **Held** (9 of 11; the 2000-3000 BP bin is +5.04%; 0-500 BP is -16%). |
| P3 | eligible within 2x of 22,428 (50%) | **Failed.** 62,757 (2.8x; v66 2.2x). |
| P4 | S21 >= 105 (60%) | **Held.** 4,957 / 3,649; 7-63 (25%) and <7 (15%) did not occur. |
| P5 | some grid configuration reproduces eligible, S21 and tracked fraction (25%) | **No such configuration** (the closest eligible count in the grid is 2.4x Day's). Reading: not reproducible from the published method. |
| P6 | pre-7000 share >= 0.99; 10000+ below 50%; 8000-10000 the plurality bin | **Failed on all three.** 0.909; 10000+ is 73%; 8000-10000 is second (17%). |
| P7 | [99,100) share 60-95%; <90% share <= 1%; singletons >= 40% | **Held on all three.** 79.0%; 0.5%; 50.3%. |
| P8 | T1 puts >= 500 events in 0-1000 BP (90%) | **Held** (53,863). |
| P9 | tracked >= 0.90 at m = 1; falls to 0.65-0.80 at m >= 10 or the intermediate rule | **Half held.** 1.000 at m = 1; never in 0.65-0.80 (0.986 at m = 10, 0.959 at 20, 0.572 at 50). |
| P10 | >= 80% of post-5000 events have older-bin minor frequency < 5% (65%) | **Held** (98.1%). |
| P11 | his recipe reproduces BA-Med and EN-Modern within 10%; SNP count and S within 10% | **Held** (-4.0%, -1.7%; SNPs 0.2-0.3%; S -7% and -3%). |
| P12 | (B) 10-25% above (K) for BA-Med; 3-8% for EN-Modern; (C) within 5% of (B) | **Held / borderline:** +23.7%; +8.6% (just outside); (C) within 0.3%. Analytic, as stated in the docstring. |
| P13 | trajectory shape as reported; Meso < 3,000; others within 1.3x of his | **Held** (872; 1.07-1.21x). |
| P14 | top/bottom informativeness quintile >= 2x in EN-Modern and >= 1.3x in BA-Med; intercept N_e >= 2x / 1.2x genome-wide | **Failed.** 1.31x and 0.96x; intercept 1.14x and 0.99x. Gradient present only in windows that cross the steppe arrival (EN-BA 2.14x). |
| P15 | drift-only (intercept) N_e < 1e5 (85%) | **Held** (9,530-14,089). |
| P16 | closed (B) within 10%, (K) 10-20% low; 10% pulse drives (B) below 0.7x; intercept within 25% | **Mixed.** (B) 1.00, (K) 0.84; **10% pulse: (B) 1.03, so refuted** (needs m >= 0.4); intercept within 25% up to m = 0.2, 1.48 at 0.4. |

Systematic errors in my priors: I expected the real data to look like the C1c model with eligibility within 2x and the 10000+ bin not dominant; instead eligibility was 2.2-2.8x higher and the 10000+ bin dominates exactly as C1c's simulations did, so on the profile the real data resemble the model, not Day's table. I expected strong admixture structure in the temporal F and found little along the three source axes.

## 6. Link back to C1c
C1c's model with R0, N_e = 1e4 and a 0.1% false-minor-call rate gave eligible 61,353 and S21 4,217. The real v62 literal reading gives 62,757 and 4,957 (v66 48,888 and 3,649). The model's central prediction for the literal statistic (thousands at textbook N_e, the 10000+ bin dominating, the 8000-7000 clusters absent) matches the real data to within about 20%, which was not expected from a model with an assumed flat SFS and assumed error rate; it may be partly coincidence (the model's profile, tracked fraction and start table were not fitted, and the transition-class concentration in the real events is something the model does not represent). It does not make the model a valid null for Day's table, because his table is still not reproduced.

## 7. Verdict and suggested edits (not applied; claim files untouched)
- **C6 external:** keep `untestable`, but replace the reason. Not "cannot decide pending a call-depth model" but "his table does not reproduce on the real genotypes under the literal method: 62,757 / 4,957 (v62), 48,888 / 3,649 (v66) against 22,428 / 21; the post-6000 BP events are 97-98% transitions at 1-5% minor frequency; transversions-only gives 36-113". Day's scripts, named in Z23046531, are not on Zenodo.
- **C6 / C1 Check paragraph:** the T2 reading is the only one compatible with his profile shape, T1 is excluded by his table. The C1c sentence "likely cause: call depth" stays refuted.
- **B2e external:** `pending` -> `contested`: the measured number replicates (7.8k-9.7k) but reading it as a measurement of the drift N_e that contradicts Wright's formula by 3 orders of magnitude needs F_nondrift to be a small fraction of F, which this data does not support or rule out (same-time spatial F is comparable to the temporal F). keruru's correction factor is half the standard one for pseudo-haploid bins (his numbers rise 8-24% when fixed).
- **C5b:** unchanged in direction; add that the corrected values are 9.7k-10.5k and that C5a's N_e near 2 is excluded by the real F.
- Not for me to edit: argmap, README, RESULTS.md, REVIEW.md.

## 8. Who this helps
**Day / allies.**
- The sampling-artefact reading that critics offered for the pre-7000 cluster is not what the real data say about the post-6000 count: the thousands are in the literal statistic, and 97-98% are in the transition class, so the "21" is not what neutral drift plus sparse sampling gives; it is closer to the damage-immune residual (36-113). Taken at face value that residual is small compared with the thousands the neutral expectation gives at textbook N_e under C1c's assumptions (rough, panel share of transversions about 22%: roughly 900 expected against 36-113 seen; not run as a calibrated comparison).
- His §4.3 description is accurate in kind: essentially all eligible alleles are at 95-100% in the Neolithic (98.8% in v62; 99.7% in v66), and the start table reproduces to 0.4 points on v62. The 97-99% pre-7000 share in the transversion class matches his "99.8% before 7000 BP" better than the all-site 91%.
- keruru's "three orders of magnitude" is not established (section 4, point 6); his own estimator is a lower bound, and his correction error means his published numbers are slightly off.
- The estimate N_e = 8-10k does not by itself support the claim that N is small either; Day's C4 caution that drift-variance N_e should not be read as census survives.

**Critics.**
- Day's table does not reproduce under the stated method (2.2-2.8x eligible, 170-240x on the 21, wrong profile, wrong tracked fraction), and the scripts he cites are not on Zenodo. His own statement "essentially zero fixations in the subsequent 7,000 years" is false under his own rule on real data: the literal statistic gives 4-5 thousand post-6000 BP events.
- The thousands are overwhelmingly near-fixed alleles that the largest bin samples as 100%, and 97-98% are transitions; the "21" is therefore a statement about assay and error class as much as about the clock. C1c's model, with an error term, predicted the literal numbers within 20%.
- keruru's N_e 8-10k replicates to 4% with his own recipe, in two releases, and the three-way ancestry stratification does not wipe it out; the corrected sampling term pushes it up, not down.
- Cuts against critics: the same data show a transversion-only count of 36-113 that is near Day's number, so "neutral predicts thousands" is not the full picture once error is controlled; the "neutral also predicts ~0" reading is false for the literal rule but the opposite claim "21 is a deficit against neutral thousands" is not supported either, because the thousands are mostly an error-class artefact. keruru's formula under-corrects by half for pseudo-haploid data, his "N_e/N of 1e-4 to 8e-4" rests on an unsourced census and a lower-bound estimator, his region regex excludes Britain, relatives are unfiltered, and his own measurement shows regional composition alone can produce F of the observed size.

## 9. Caveats
- Day's procedure is a reconstruction from prose; the unpublished choices (quality filters, calibrated-date field, what "tracked" requires, treatment of sex chromosomes, how moderns were chosen: his 0-500 BP bin has 625 individuals against 524 in the public anno rule) may differ from mine. Nothing here shows that Day's numbers came from a different pipeline, only that mine does not reproduce them. The v62.0.p1 patch (June 2026) is not the v62.0 original he used (September 2024), which is no longer retrievable.
- The 120-configuration grid (V1) plus 12 (V2) and the post hoc rules (T3, minor-count >= k, transversions) are exploratory: no rule was fitted to hit his numbers, and the grid does not exhaust possible implementations. The post hoc rules were chosen after seeing the main result (labelled post hoc, separate commits).
- Event anatomy shows transitions are 97% of the excess, not that the cause is deamination damage; library-type (UDG) stratification, per-individual damage rates and reference bias were not tested.
- Temporal N_e: the same sample hygiene as keruru's (no relatedness filter, region regex with no UK). Jackknife CIs by chromosome (22 blocks) understate the uncertainty from linkage within chromosomes and from the sample itself. The informativeness-quintile method assumes admixture F is proportional to the source differentiation; the simulation shows it over-corrects (1.23, 1.48), so the intercept N_e values are diagnostics, not estimates. Regional strata for N_e mostly fail the power rule (regional Modern bins of 6-228 individuals) and are listed in `c1d_*_ne.txt`, not interpreted.
- Wright's formula and the census N = 1e7 are used as keruru frames them; neither was retrieved or tested here.
- All counts are on 1,233,013 sites with the 1240K panel's own ascertainment; no mutation or selection model; V1 is a lat/long box, not Day's sample.
