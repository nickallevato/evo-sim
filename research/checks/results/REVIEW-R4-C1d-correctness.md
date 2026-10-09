# Correctness review: R4 C1d (Day's "21" statistic and keruru's temporal N_e on the real AADR genotypes)

Reviewer: correctness pass, 2026-10-09. Read: `results/R4-C1d.md`, `c1d_aadr_real.py` (identical to the pre-registered c0a4071: same md5 ce613f52..., and the md5 in `raw/c1d.host`), `c1d_posthoc.py`, `c1d_verify.py`, `c1d_figure.py`, `raw/c1d_*`, `R4-C1c.md`, the C6 and B2e claim files, keruru's deposited code (`sources/raw/refresh-2026-10-09/.../adna-temporal-ne/code/`), Day's Z23046531 and Z18525185 texts, and `sources/raw/day-scripts-search-2026-10-09/` (read as data only).

Independent work on na-workhorse: scratch scripts in `/tmp/c1d_review/` (outside the repo, nothing committed, one or two niced processes). Nothing in the repo was edited except this file.

**Verdict: no BLOCKER.** The decoding, sample, statistic code and keruru replication all check out, and the headline "Day's table is not reproduced" is robust to every variation I tried. Three MAJOR findings concern (1) a fully specified Day comparator that was skipped, (2) an inference in the B2e section that the numbers do not support, and (3) a false negative statement about the "tracked" fraction caused by a hole in the min-calls grid. The rest are MINOR.

## What I verified (all reproduce)

1. **TGENO layout.** Header "TGENO 17468 1233013 ..." is 48 bytes; file size 5,384,580,920 = 48 + 17,468 x 308,254 exactly (v62). The reader's `header = size - nind*rec` inference therefore equals 48. High-bits-first 2-bit codes, 3 = missing, and the allele counted is the first allele column of the .snp (the copies of column 5). Every analysis that matters is symmetric in the two alleles, so the counted-allele choice cannot affect any count.
2. **Bit order (independent check, see finding 7).** Named SNPs decoded with my own explicit-shift code, on my own parse of the anno and .ind, V1 rule, chromosome counting (pseudo-haploid = 1, `.DG` = 2), v62:

   | SNP | counted allele frequency by Day bin (10000+ ... 0-500) |
   |---|---|
   | rs1426654 (SLC24A5) | 0.18, 0.38, 0.87, 0.94, 0.95, 0.98, 0.99, 1.00, 0.92, 0.98, 1.00 |
   | rs16891982 (SLC45A2) | 0.85, 0.88, 0.69, 0.57, 0.64, 0.46, 0.39, 0.20, 0.24, 0.07, 0.09 |
   | rs4988235 (LCT) | 0.96, 0.99, 1.00, 1.00, 1.00, 0.98, 0.95, 0.77, 0.72, 0.55, 0.60 |

   These are the textbook trajectories (WHG low, farmer/steppe high for SLC24A5; LCT flat until the Bronze Age). The seven SNPs around LCT (index +-3) are all about 1.00 in the modern bins, so the test discriminates a wrong in-byte order.
3. **Sample and binning identical to C1c.** My own anno parse (columns 9, 15, 16, 17 = date mean, Political Entity, Lat., Long.; the same exclusion list; `d >= lo and d < hi`) gives per-bin n = 167 / 133 / 669 / 579 / 726 / 1,155 / 1,015 / 1,000 / 2,125 / 715 / 524 = 8,808, equal to `c1d_v62_groups.json` and to C1c's depth table. No duplicate Genetic IDs; 17,468 .ind rows = 17,468 anno rows. In the 0-500 bin 432 of 524 are date 0 / "present"; the other 92 are historical (1450-1800 CE).
4. **Ploidy handling.** Het rate on SNPs 0-200,000 for the 8,808 V1 individuals by ID suffix: `.DG` n = 440, median 0.263, all > 1%; `.AG` 4,805, `.SG` 2,690, `.TW` 86, `.AA` 14, `.BY` 1: every one has het exactly 0. No non-DG individual has het > 0.5% and the only DG below 5% is `Vindija_snpAD.DG` (a Neanderthal, 1.1%). So `dip = endswith(".DG")` is the right label for this file. C1c's rule (`".DG" in id or endswith(".HO")`) gives the same split here (no `.HO` rows).
5. **Statistic code, hand computation.** For `rs11260588` (idx 16, chr1) my decode gives n = 57/80/378/319/385/567/531/595/1209/307/901, k = 50/78/367/314/370/554/521/577/1180/302/901, identical to the stored event (`c1d_v62_day.json`). Hand check: modern 901/901 (100%), pooled 7000-8000 + 6000-7000 = 681/697 < 100%, so E1-eligible; no older bin is 100%, so T2 date = 0-500; all 11 bins observed, so tracked. For `rs183919107` (n 74/86/417/371/425, k 73/85/416/371/425, ..., 908/908): pooled Neolithic 787/788 (eligible); oldest 100% bin is 6000-7000 (371/371), so T2 dates it 6000-7000 although the allele is below 100% again in 4000-5000 (690/691); the stored event says 6000-7000. `rs145004114` also matches n and k exactly. The brute-force check in `c1d_verify.py` (1,032 and 785 eligible, identical profile) is sound.
6. **keruru replication, independent reimplementation** (my own group definition from his regex/bins/PASS/hits rule and my own decode; v66; groups BA 1,846, Med 2,974, EN 1,665, Mod 559, as R4):

   | | R4 | mine |
   |---|---|---|
   | BA-Med (K): SNPs, S, F, N_e | 1,114,724; 782/1,444; 0.007505; 7,812 | 1,114,724; 782.3/1,444.3; 0.007505; 7,815 |
   | BA-Med (B): N_e [CI] | 9,665 [9,267-10,098] | 9,669 [9,272-10,103] |
   | EN-Mod (K): S, F, N_e | 836/474; 0.014575; 9,672 | 835.7/474.5; 0.014575; 9,672 |
   | EN-Mod (B): N_e [CI] | 10,508 [9,926-11,162] | 10,508 [9,926-11,162] |

   Differences are the single half-allele convention for rare heterozygote calls in pseudo-haploid individuals. His formula, the bins (his `findInterval(-ybp, -hi)` gives hi[i+1] < age <= hi[i], as in `build_groups`) and the 20-call rule are as in his code. R4's claim "all seven windows within 1-8% of his" is right (-4.0, -1.7, -7.7, -4.4, -2.5, -1.0, -1.4%).
7. **Derivation of the factor of 2.** Pure binomial sampling of n_0 and n_t alleles from a common p gives E[(x-y)^2] = p(1-p)(1/n_0 + 1/n_t); with n = 2S for S diploids this is the Nei-Tajima 1/(2S_0)+1/(2S_t); for pseudo-haploid bins n = S, so keruru's `1/(2S)` under-corrects by exactly 2 on those bins. His own header comment (adna_temporal_ne.r lines 14-17) says S is the individual count for pseudo-haploid data, then applies 1/(2S). The selftest identity (0.001921 vs 0.001917) confirms it. R4 is right.
8. **Jackknife.** Delete-one-chromosome on F_adj, normal CI, delta-method back to N_e: reproduced to 4 digits (above). A Busing-style weighted jackknife gives se(F_adj) = 0.000101 against 0.000115 unweighted (BA-Med). Immaterial.
9. **Day-statistic numbers in the table.** Panel is 77.6% transitions (956,696 of 1,233,013; 12 allele pairs, no non-ACGT alleles, no indels, no chromosome 90; X = 49,704, Y = 32,670). Profile, S21, S23, singleton share (31,541 / 62,757 = 50.3%) and start table as printed; grid has 133 rows per release (120 + 12 + 1 naive); the v62 minimum eligible in the grid is 2.41x Day's (v66: 1.95x).
10. **Regenerated post hoc numbers.** Transversions on autosomes S21 = 36 (v62), 113 on all chromosomes; 4,957 total of which 4,844 transitions (97.7%); 4,861 of 4,957 with older-bin minor frequency < 5% (98.1%); 1,540 events dated 6000-7000 .. 500-1000.
11. **Pre-registration integrity.** `c1d_aadr_real.py` is byte-identical to c0a4071. The post hoc script is committed before its run (814f5da), with one bug-fix commit (982366c) before the first successful run; verify script likewise (d308586). The md5s in `c1d.host` match the repo. Extraction output times (02:25) follow the 02:23 pre-registration commit.

## Findings

### 1. MAJOR: a second, fully specified Day method with published counts exists on the same two releases, and C1d did not compute it
R4 says (section 1): "The two-period statistic of Z23046531 is a different quantity and is not computed here." But Z23046531 (sec 2.2-2.4, 3.1-3.2) gives an exact procedure (Neolithic 6000-8000 BP pooled vs date = 0 moderns, autosomes, >= 100 genotyped individuals in each period, locus counted when it reaches 100% or 0% in the modern period, banded by Neolithic MAF) and published outputs: v62 1,143,671 SNPs, 17,814 events (80.9% / 18.9% / 0.22% in the 0-1 / 1-5 / 5-10% bands, one event in 20-30%); v66 1,143,230 SNPs, 3,470 events (86.3% / 13.4% / 0.20%), with 1,372 / 680 (v62) and 395 / 441 (v66) Neolithic / modern individuals. The stored per-SNP group counts can compute this in seconds. My approximation (scratch `/tmp/c1d_review/e.py` on workhorse; V1 pools 7000-8000 + 6000-7000 as Neolithic, the 0-500 BP bin as "modern", >= 100 individuals in each, polymorphic in the Neolithic, 100% or 0% in the modern bin):

| | SNPs tested (Day) | events (Day) | band shares 0-1 / 1-5 / 5-10 % (Day) |
|---|---|---|---|
| v62 | 1,141,037 (1,143,671) | 52,315 (17,814) | 81.6 / 18.1 / 0.3 (80.9 / 18.9 / 0.22) |
| v66 | 1,147,907 (1,143,230) | 43,570 (3,470) | 87.9 / 12.0 / 0.1 (86.3 / 13.4 / 0.20) |

So the genotype-level structure (SNP set within 0.4%, band shares within 1.5 points on both releases) matches Day's second paper, while the totals do not (2.9x on v62, 12.6x on v66). That is useful in both directions and belongs in the write-up: it supports "my decoded data and sample are close to what his pipeline saw", it supports the near-fixed-allele anatomy (his own tables say 99.9% of his events start below 10% MAF), and it shows that even his own two papers give different event totals for the same release. It also shows his samples are not V1: Z23046531 has 680 date-0 Europeans on v62 (V1: 432; the C1c box 486 with Turkey etc.; the KR country regex 462 with Russia, 341 without) and 1,372 Neolithic (V1: 1,249). The fix is to add this comparison as a labelled post hoc row, and to change "a different quantity" to "a different, better-specified method, computed in section X".

### 2. MAJOR: "regional composition alone can produce F of the observed size" (B2e) is not supported by the numbers R4 itself reports
Section 4(ii) compares the pairwise same-time regional F_adj (0.006-0.055) with the whole BA-to-Medieval F_adj (0.0053) and concludes a composition shift "can therefore contribute F of the measured order without drift"; section 8 repeats it as "his own measurement shows regional composition alone can produce F of the observed size". A composition shift only passes on a fraction of the between-region F. For two mixtures of the same regional populations with proportion shifts d_r (sum 0) and pairwise F_rs, F_comp = sum over r<s of (-d_r d_s) F_rs. Using R4's own v66 numbers (proportions from `c1d_v66_groups.json`: BA .13/.37/.21/.07/.22 and Med .05/.65/.07/.16/.07 for Iberia / Central / Italy-Balkans / Scandinavia / East; pairwise F_adj from `c1d_v66_posthoc.json`):

- using the BA-bin pairwise F: F_comp = 0.00082 (v62: 0.00106);
- using the Medieval-bin pairwise F: F_comp = 0.00032 (v62: 0.00037).

That is 6-20% of 0.0053, not "the measured order". Caveats on my number: it covers only the five regions (not within-region ancestry heterogeneity or cemetery clustering), and it uses pairwise regional F that themselves contain relatedness and within-bin date spread (finding 12). It is a counterfactual, not a decomposition. The B2e verdict `contested` can stand on the other reasons R4 gives (lower-bound estimator, unsourced census, correction error, admixture simulation), but the Day-side and critic-side paragraphs should say "composition shifts among these five regions explain on the order of 10% of F, an upper-end reading is the remainder is unattributed". It is also not true that the regional check is "no time elapsed": bins are 1,000-1,500 years wide, so regional samples inside one bin can differ in mean date by several generations.

### 3. MAJOR: "No setting gives tracked 0.65-0.80 (it jumps from 0.96 to 0.57 between m = 20 and m = 50)" is false; the grid skipped the interval where the fraction crosses Day's 0.727
The tracked fraction is monotone in m and the grid has m = 1, 5, 10, 20, 50 only. Scratch run on the stored v62 counts (E1, T2, all11, all SNPs; `/tmp/c1d_review/h.py`):

| m | eligible | tracked fraction | S21 |
|---|---|---|---|
| 20 | 59,789 | 0.959 | 4,794 |
| 30 | 58,416 | 0.885 | 4,534 |
| 35 | 58,330 | 0.826 | 4,309 |
| 40 | 58,281 | **0.755** | 4,030 |
| 45 | 58,241 | **0.671** | 3,704 |
| 50 | 58,196 | 0.572 | 3,301 |

Autosomes only: 0.705 at m = 45. v66 reaches 0.824 at m = 50 and would cross 0.727 only beyond it. So P9 ("falls to 0.65-0.80 at m >= 10 or the intermediate rule") should read **held on v62 at m = 40-45**, not "half held"; and the sentence in section 3 must go. This does not change any verdict (eligible stays 58k, S21 3.7-4.0k, i.e. P5 still fails on the other two criteria), but it is a negative claim over an unsampled range, and it is a lead for Day's unstated threshold (about 40-45 chromosomes per bin).

### 4. MINOR: the "+24%" for BA-to-Medieval mixes two corrections, and the "half" applies only to the pseudo-haploid bins
My reimplementation separates them. BA-Med: (K) correction 0.000985 (mean S); factor-2 fix at mean n (1/n_0 + 1/n_t with the mean chromosome counts 786 / 1,445) 0.001964 gives N_e 9,169 (+17%); the site-wise correction (sum of den x (1/n_0i + 1/n_ti) over sum of den, 0.002251) gives 9,669 (+24%). The remaining 6 points are the Jensen effect of unequal per-SNP depth, which (K)'s mean-S form also ignores. EN-Mod: 10,270 (+6.2%) at mean n, 10,508 (+8.6%) site-wise. Both are legitimate, but "his sampling correction is half the standard one" explains about two thirds of the BA-Med change. Also, the Modern bin is mostly diploid (441 of 559 `.DG`), where 1/(2S) with S in individuals is correct for the diploids; the factor of 2 is about the Early Neolithic ... Medieval bins. Section 7 "his numbers rise 8-24%" understates the range over all windows (+1% Meso to +27% EN-LN relative to (K)).

### 5. MINOR: which keruru code, and what S is
The deposited `adna_stream.r` multiplies S by 2 for the Modern bin (`Sa <- (na_sum/n_used) * (if (dip_a) 2 else 1)`) and prints it as "alleles", then applies `1/(2*Sa)`. If that were what produced the draft's numbers, the Modern bin would also be half-corrected (S = about 950 alleles, correction half of the correct 1/n). But the draft's reported S_b = 476 and its arithmetic (0.014339 - 250/(2 x 9,835) = 0.001629 = 1/(2 x 865) + 1/(2 x 476)) show S_b was the number of called individuals, which is what R4's (K) uses (and why (K) matches). So the reported numbers are not from the code exactly as deposited, or the flag did not fire. R4's "his code feeds it a pseudo-haploid allele count" is true of the ancient bins; it should say which script and note the Modern-bin discrepancy between code and draft. It does not change the replication.

### 6. MINOR: the Nei-Tajima Fc agreement is algebraic, not independent
(m - xy) = m(1-m) + (x-y)^2/4, so Fc and F differ by a relative F/4 in the denominator, 0.2-0.4% at these F. P12's "(C) within 5% of (B)" and "within 0.3%" cannot fail; they confirm the code, not the estimator. Say so.

### 7. MINOR: the bit-order evidence in the write-up is weaker than it reads
(i) The P1 QC (call counts per individual correlate 0.9999997 with the anno) is insensitive to the order of the four 2-bit fields inside a byte: a permutation inside each byte leaves per-individual autosomal call counts essentially unchanged. It validates the record layout, individual order and the SNP set (an exact equality is strong evidence for those), not the in-byte order. (ii) `c1d_verify.py` "independent explicit bit-by-bit decode" uses the same shift expression `6 - 2*(s % 4)` as the LUT, so it checks the matrix code, not the convention. The convention is established by the allele-frequency trajectories (LCT in R4; SLC24A5, SLC45A2, HERC2 and neighbour SNPs in my check above). R4 should name those as the evidence for the bit order.

### 8. MINOR: the transversion headline mixes autosomes with X and Y
v62 transversion S21 = 113 splits as 36 autosomal, 18 X and 59 Y (scratch `d.py`); all-class S21 = 4,957 splits 4,559 autosomal transitions + 36 autosomal transversions + 362 on X/Y. The brief and "who this helps" quote "36-113" and "same order as Day's 21". The 77 sex-chromosome events are haploid (Y: males only, `.DG` males counted as 2 chromosomes) and are lineage-type events, not damage-immune autosomal ones. The autosome number (36 / 44) is the like-for-like one; Z23046531 also analyses autosomes only. Also "about 100-fold" (4,957 vs 36-113) compares counts of unequal site sets; per-site rates are 0.49% (autosomal transitions) vs 0.016% (autosomal transversions), 31x, or 12x with all chromosomes. Reword.

### 9. MINOR: the 0-500 BP wording ("happens to call as 100%") is statistically misleading, and the modern-bin sensitivity is missing
A minor allele at the 1-2% older-bin frequency of most events (2,306 + 1,850 of 4,957 in the 1-5% classes) has probability 1e-4 to 1e-8 of being absent from 901 modern chromosomes by sampling. The events are therefore systematic (an error/damage difference, a real loss under drift plus replacement, or both), not luck. C1c's neutral model with an error term produces the same mechanism, and R4 section 6 says so; the anatomy paragraph should too. Sensitivity of the modern bin, since 84% of S21 sits in it and V1 has 524 against Day's 625 (and 680 in Z23046531), run on the stored v62 counts (`g.py`): modern = diploid `.DG` only: eligible 72,424, S21 8,443; modern = pseudo-haploid only: 130,855 / 26,307; dropping the modern bin from S21 leaves 780 (bins 5000-6000 .. 500-1000). No composition of the modern bin I tried goes near 21, so the conclusion is robust; add the rows.

### 10. MINOR: dating readings and what excludes them
R4 excludes T1 by Day's profile. T3 (forward first passage, literally "an allele that was polymorphic in an earlier bin reached 100% in a later bin") is run post hoc (S21 31,968 / 24,698) but not mentioned in the body; it is excluded by the same kind of argument, since no event can be dated to the oldest bin under T3 (profile 0 at 10000+) while Day's table has 3,038 there. Add that, and note that T2 dating at m = 1 can rest on n = 1 chromosome in the 10000+ bin.

### 11. MINOR: scorecard and labelling
- **P12** is written "Held / borderline", but EN-to-Modern is +8.6% against a registered 3-8%: that sub-prediction failed narrowly.
- **P1** registered het < 1e-4 for pseudo-haploid-labelled individuals; 1 (v62) and 2 (v66) have 1.2-1.6%. R4 mentions this in the QC bullet; the table row says "Held".
- **P10** registered "<= 7000 BP bins"; the anatomy uses all bins older than the event's bin (for a 0-500 event, all ten). Same direction, not the same quantity.
- **"Found among 8 rules"** (the minor >= 2 coincidence): `posthoc.py` computes 10 readings (T3, four minor-count thresholds x two site sets, T3 with minor >= 2).
- **Labelling.** `c1d_figure.py` was committed inside the results commit 0c696f9, not in a commit labelled post hoc, although R4 lists it among the "separate commits and labelled". It computes nothing new, so this is cosmetic.
- All other scorecard rows agree with the docstring and the raw outputs (P2 9 of 11, P3, P4, P6, P7, P8, P11, P13, P14, P15, P16 as stated).

### 12. MINOR: keruru informativeness sources overlap the target groups
`build_groups` takes Yamnaya (Political Entity Russia, which is inside the country regex) and the WHG source from the same data as the target bins: Yamnaya are in the Late Neolithic group and the WHG sample is a subset of the Mesolithic group, so for windows that include those bins (LN-BA; Meso-EN) the informativeness s_i shares sampling noise with F. The sources are also read at >= 6 chromosomes per SNP, which is noisy. Of the five windows stratified, only LN-BA is affected directly, but the quintile gradient there (1.18x) should carry the caveat. R4 already states the intercept method over-corrects in simulation.

### 13. MINOR: scripts search, evidence retained and wording
- **What is retained** in `day-scripts-search-2026-10-09/`: `athos_p1/p2.json` (38 hits, 21 pdf, 3 odt, 15 docx, 1 xlsx; 37 publications + 1 dataset, none with code files), `rec23046531.json` (one pdf, no related identifiers), `rec18525185.json` (one odt). Hashes in R4 match. **Not retained:** the ORCID query (37), the "Day, Vox" listing (39) and the `software` resource-type query (0 hits) are asserted without a saved response. Save them or soften.
- **Scope.** Searched: Zenodo, under two creator names, plus Day's own text for "github". Not searched: the creator's legal name or other spellings, a Zenodo keyword/title query ("AADR", "ancient DNA", "fixation trajectories") across all creators, the record's other versions (the versions endpoint returned 404), OSF, GitHub, or Harvard Dataverse. "Not found on Zenodo under those names" is established; "not found" in general is not.
- **Wording.** The sentence is "Analysis scripts are available from the authors at Zenodo", which can also be read as "on request from the authors; the paper is at Zenodo". "Unfulfilled" and "has no target" (section 1) are stronger than the evidence; "no code is attached to or linked from any Zenodo record found" is what was shown.
- **Format statement.** R4 says both files are TGENO "not the PACKEDANCESTRYMAP that Z23046531 says". Z23046531 says v62.0 was PACKEDANCESTRYMAP and v66.p1 was TGENO converted by PLINK 2. So the mismatch is only for v62, and only between his original v62.0 (not retrievable) and v62.0.p1 (TGENO). The 161-individual difference (17,629 vs 17,468) is the same Papuan removal Z23046531 describes for v66.p1.

## Not wrong, but worth knowing
- `Vindija_snpAD.DG` (a Neanderthal) is in V1's 10000+ bin as a 2-chromosome diploid. It is also in C1c's sample. Negligible for the counts.
- `dph // 2` floors half an allele when an odd number of pseudo-haploid individuals have a het call (1-2 individuals per release). Negligible.
- The 95% CI uses z = 1.96 on 22 blocks (t(21) = 2.08 would widen it 6%); it excludes individual-level and relatedness variance, as the caveats say.
- The Wright arithmetic (0.571 x 1e7 = 5.7e6; F_drift = 9e-6; about 590-600x) is correct.
- The sim table matches its docstring; the K ratio (0.84) is analytic (0.005/(0.005+0.000958)).

## Suggested edits to R4-C1d.md (not applied)
1. Add the Z23046531 two-period comparison (finding 1) and soften "unfulfilled" (13).
2. Replace the "no setting gives 0.65-0.80" sentence and the P9 row (3).
3. Replace the composition sentence in 4(ii) and in section 8 with the F_comp counterfactual (2).
4. State the split of the +24% (4), the code/draft S discrepancy (5), the Fc tautology (6), the bit-order evidence (7).
5. Headline transversion result as autosomes 36 / 44 with X/Y shown separately (8); fix the "100-fold" wording.
6. Add the modern-bin sensitivity rows and the T3 exclusion (9, 10); correct P12/P1/P10 wording and the "8 rules" count (11).
