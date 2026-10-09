# R4 C1d: Day's aDNA "21" statistic on the real AADR genotypes, and a replication of keruru's measured temporal N_e (B2e)

Revised in the review fix pass (2026-10-09). Section 10 answers every finding of the three reviews. New runs are labelled post hoc.

Scripts: `research/checks/c1d_aadr_real.py` (pre-registered in commit c0a4071, predictions P1-P16 in its docstring, before the main run). Post hoc, each committed before it was run: `c1d_posthoc.py` (event anatomy, substitution class, rival readings, regional F), `c1d_verify.py`, `c1d_posthoc2.py` (library type and damage with matched random controls, Day's two-period pipeline, country-list sample, minimum-call grid, modern-bin variants; predictions L1-L3, T1-T4 in its docstring), `c1d_posthoc3_keruru.py` (arithmetic on stored outputs), `c1d_posthoc4_tp.py` (Neolithic minor-copy scan), `c1d_figure.py` (revised in its own commit). Raw outputs: `results/raw/c1d_*` (`_day`, `_ne`, `_groups`, `_posthoc`, `_verify`, `_ph2`, `_ph4` for v62 and v66; `c1d_sim.json`, `c1d_posthoc3_keruru.*`, `c1d.host`). Figure: `results/R4-C1d-real-vs-day.png`.
Everything ran on na-workhorse (host and md5s in `raw/c1d.host`; the fix-pass runs used at most 6 processes while load was 6-13). The genotypes were downloaded there only and are not on the workstation or in git.

## Result in brief
Both sides get credit below; items are in the order of the evidence, not of who benefits.
1. **Day's table is not reproduced on the real genotypes by the literal reading of his method or by any of the 132 grid cells.** v62.0.p1, his European sample, E1 eligibility, T2 dating: 62,757 eligible alleles (Day 22,428), 4,957 events dated 5000-6000 BP or younger (Day 21), pre-7000 share 0.909 (Day 0.9986), tracked fraction 1.000 (Day 0.727). v66: 48,888 and 3,649. 84% of the 4,957 sit in the 0-500 BP bin (Day: 2).
2. **Day's own documented two-period pipeline (Z23046531) reproduces his sample and SNP count but not his event count.** With a European country list plus Russia the sample is 1,377 Neolithic and 683 modern individuals (his 1,372 and 680); autosomes with at least 100 genotyped individuals per period give 1,143,870 tested SNPs (his 1,143,671) and 2 events from Neolithic MAF >= 10% (his 1). The event total is 63,631 against his 17,814 (3.6x) and the band shares are 77.1 / 22.6 / 0.38 % against 80.9 / 18.9 / 0.22 %. No Neolithic minor-copy threshold fixes both the total and the shares. So the gap is not a sample or SNP-filter choice that his text documents.
3. **The transition excess is not explained by library type or damage rate.** 97.7% of the 4,957 events are transitions (panel: 77.6%). At the 0-500 BP events the minor-allele frequency in the older bins is 1.4% in non-UDG ("minus") libraries, 2.1% in "half" and 2.2% in fully corrected ("plus") ones; dropping minus-library reads at transition SNPs lowers S21 less than dropping the same number of random individuals (3,071 against 2,097). I therefore do not call it damage. What it is (real loss of low-frequency alleles that the ancient bins carry at 1-5%, hypermutable transitions, reference or capture bias) is open.
4. **Restricted to transversions the count is small:** S21 = 36 (v62) and 44 (v66) on autosomes, 113 and 66 with X and Y, eligible 6.0-10.0k, pre-7000 share 0.98-0.99. Per eligible allele that is 0.57% against 9.5% for autosomal transitions (16.7x); per panel site 0.016% against 0.49% (31x on v62, 19x on v66). Day's 21 is 0.094% of his eligible alleles. Whether this class sits above or below a neutral expectation at textbook N_e is open (section 3.5).
5. **Wins for Day in the data:** the start-frequency table reproduces to 0.4 points on v62 (79.0 / 19.8 / 0.7 / 0.5 % against 79.2 / 20.2 / 0.5 / 0.2); his §4.3 description ("completion events for alleles already near fixation") is confirmed in kind (98.8% of v62 eligible alleles start at 95-100% in the Neolithic); the pre-7000 share in the transversion class (0.98-0.99) is close to his 0.9986; and keruru's formula under-corrects pseudo-haploid sampling by a factor of 2.
6. **Wins for the critics:** his table does not reproduce under the stated method; the thousands are real data (reproduced in two releases and two samples); C1c's model with an error term predicted them within 20%; keruru's temporal N_e replicates (7.8k and 9.7k with his own formula, within 1-8% of all seven published values); and "Day's N_e near 2" (C5a) is excluded.
7. **Open:** whether temporal N_e contradicts Wright's N_e = 4N/(V_k+2). The estimate is a lower bound on a drift N_e. For Wright's formula to hold the BA-to-Medieval F would have to be 83% non-drift at N = 1e5, 98% at 1e6, 99.8% at 1e7; composition shifts among five regions explain 6-17% of it; within-region N_e values do not move toward Wright. RF-12 ("wrong by three orders of magnitude") is not established at the unsourced census of 1e7 but a gap of at least 6x survives at any census of 1e5 or more; RF-13 ("measurably wrong where it can be tested") is the fairer reading and is partly supported.

## 1. Day's scripts (step 1)
- **Not found on the Zenodo records searched.** Two creator names ("Day, Vox", 39 records; "Athos, Claude", 38) and the ORCID (37) return only pdf/docx/odt/xlsx files; `resource_type` software returns 0 for both names; a title query returns the single record 23046531 (one pdf, one version per its own `versions` link, no related identifiers); a keyword query for AADR and trajectories across all creators returns 836,048 unrelated hits, none by these authors. Responses are saved in `sources/raw/day-scripts-search-2026-10-09/` (gitignored): `orcid_p1/p2.json`, `dayvox_p1/p2.json`, `athos_p1/p2.json`, `dayvox_software.json`, `athos_software.json`, `kw_title2.json`, `kw_aadr.json`, `kw_voxday_code.json`, `versions_23046531_own_link.json`, `rec23046531.json`, `rec18525185.json`.
- **Beyond Zenodo (read-only, 2026-10-09):** GitHub repository searches for "Vox Day" AADR, Athos with molecular clock, and aDNA trajectories return 0; a GitHub account `voxday-athos` (created 2026-01-08, identity unverified) has one public repository, `finch-vcf` ("data for analysis"), nothing on AADR; OSF node searches for "molecular clock" and "Vox Day" return nothing relevant; the saved Day blog corpus (`sources/raw/day/blog-*.txt`) and the two Zenodo papers contain no code or repository link for the aDNA analysis and no mention of damage, UDG, transversions or quality filters. Nothing found was executed or cloned.
- **Which paper promises scripts.** The sentence "Analysis scripts are available from the authors at Zenodo" is in Z23046531 s5 (the two-period statistic), not in Z18525185 (the "21"), whose Appendix B names only the AADR (quotes-day Q112, Q116). It can also mean "on request"; no author was contacted (rule 6). The 22,428 / 21 statistic was reconstructed because no code was promised for it. Wording to carry forward: "no code attached to or linked from any Zenodo record found; the promise is in Z23046531 and may mean on request".
- Method text used (registered verbatim as quotes-day Q106-Q117): Z18525185 s3.1, s3.3, s3.4, s4.1, s4.3, Appendix B; Z23046531 s2.1-2.4, s5.

## 2. Data (steps 2-3)
- AADR v62.0.p1 (Dataverse 11.0, 7 June 2026; file ids 13994086 geno, 13987485 snp, 13987487 ind, 13994492 anno). md5 equal the Dataverse API values (geno 24419bba..., snp 50f66178..., ind 3f23dd87..., anno 6468eb19...); no md5sum file is published for v62. Day cites "v62.0", the original of 16 Sept 2024 (Dataverse 9.0), which the API no longer serves. The p1 anno has 17,468 rows against his 17,629 individuals for v62.0; the difference (161) equals the number of Papuan moderns that Z23046531 s2.1 says were removed in v66.p1, so the patch probably removed non-European moderns (inference, not proof).
- AADR v66.p1 1240K (file ids 13994829, 13994513, 13994514, 13994515); md5 equal the published `v66.p1__files.md5sum`.
- Format: Z23046531 s2.1 says v62.0 was PACKEDANCESTRYMAP and v66.p1 was TGENO converted by PLINK 2 (Q117). Both files retrieved here are TGENO (transposed, 48-byte header, 2-bit codes high bits first), so the mismatch is only between his v62.0 and the v62.0.p1 file. The script reads TGENO and GENO (checked on synthetic files of both kinds).
- Streaming: 1,024-SNP blocks over the selected individuals, per-group sums by matrix product, 6 processes; peak RAM well under 14 GB. Per-SNP group counts stay on workhorse (about 0.7 GB per release; 1.8 GB for the fix-pass groups).
- **QC and the evidence for the decoding.** Decoded autosomal call counts equal the anno "SNPs hit" column exactly (correlation 0.9999997 v62, 1.0 v66). This validates record layout, individual order and SNP set; it is insensitive to the order of the four 2-bit fields inside a byte. The bit order is established by trajectories: rs4988235 (LCT) counted-allele frequency by keruru bin 0.987 / 0.999 / 1.000 / 0.966 / 0.902 / 0.739 / 0.743 on v62 and ending at 0.733 on v66 (his draft: 0.732); the correctness review's independent decode of SLC24A5, SLC45A2 and LCT-neighbour SNPs gives the textbook trajectories. `c1d_verify.py`'s "explicit bit-by-bit decode" uses the same shift expression as the lookup table, so it checks the matrix code, not the convention. Pseudo-haploid-labelled individuals have median heterozygote rate 0 (1-2 per release at 1.2-1.6%); `.DG` median 0.27. A brute-force Python day_events on 20,000 random SNPs matches the vectorised code.

## 3. Day's statistic on the real data

### 3.1 Cell by cell (v62.0.p1 and v66.p1; E1, T2, any call counts, tracked = observed in all 11 bins, all 1,233,013 SNPs; pseudo-haploid = 1 chromosome, diploid = 2)
Samples: V1 = C1c's lat/long rule (v62: 8,808 individuals, per bin 167 / 133 / 669 / 579 / 726 / 1,155 / 1,015 / 1,000 / 2,125 / 715 / 524 against Day's 168 / 129 / 668 / 573 / 721 / 1,141 / 980 / 952 / 2,093 / 688 / 625). **dayE** = a European country list on the Political Entity field, no Russia (post hoc; 8,937 on v62: 168 / 136 / 669 / 577 / 725 / 1,152 / 1,016 / 996 / 2,125 / 735 / 638, closer than V1 in the 10000+ and 0-500 BP bins). Bins oldest to youngest: 10000+, 8000-10000, 7000-8000, 6000-7000, 5000-6000, 4000-5000, 3000-4000, 2000-3000, 1000-2000, 500-1000, 0-500.

| Quantity | Day (Z18525185) | v62 V1 | v62 dayE | v66 V1 |
|---|---|---|---|---|
| eligible alleles | 22,428 | 62,757 (2.8x) | 63,271 | 48,888 (2.2x) |
| tracked | 16,299 (72.7%) | 62,747 (100%) | 63,258 | 48,886 |
| 10000+ | 3,038 | 45,815 | 46,329 | 35,753 |
| 8000-10000 | 8,741 | 10,444 | 10,363 | 8,342 |
| 7000-8000 | 4,497 | 771 | 761 | 627 |
| 6000-7000 | 2 | 760 | 761 | 515 |
| 5000-6000 | 9 | 268 | 260 | 213 |
| 4000-5000 | 7 | 111 | 110 | 66 |
| 3000-4000 | 2 | 144 | 142 | 109 |
| 2000-3000 | 1 | 88 | 75 | 33 |
| 1000-2000 | 0 | 4 | 4 | 1 |
| 500-1000 | 0 | 165 | 174 | 21 |
| 0-500 | 2 | 4,177 | 4,279 | 3,206 |
| pre-7000 share | 0.9986 | 0.9089 | 0.9082 | 0.9148 |
| S21 | 21 | **4,957** | 5,044 | **3,649** |
| S23 | 23 | 5,717 | 5,805 | 4,164 |
| start frequency of the fixed allele, [99,100) / [95,99) / [90,95) / <90 | 79.2 / 20.2 / 0.5 / 0.2 % | 79.0 / 19.8 / 0.7 / 0.5 % | 78.5 / 20.2 / 0.7 / 0.5 % | 87.3 / 12.4 / 0.2 / 0.0 % |

- **Start table (v62):** the only quantity close to Day's, within 0.4 points per cell, and v66 does not match it. It is insensitive to dating and to the post-7000 counts, so it is weak evidence that his sample was v62-like, not evidence that his procedure was reproduced. 50.3% of the 62,757 eligible alleles (31,541) have exactly one copy of the other allele in the pooled 6000-8000 BP sample.
- **Reading sensitivity (v62 V1, S21 in parentheses):** autosomes 54,243 (4,595); E2 eligibility 137,200 (4,957); PASS-only sample V2 60,409 (3,980). T1 dating puts 53,863 of 62,747 events in the 0-1000 BP bins (Day: 2); T1 cannot put events in bins 0-2 under any eligibility rule, where Day has 16,276 of 16,299, so his own table excludes it. T3 (forward first passage: an event is dated at the first 100% bin after an earlier bin below 100%) gives S21 31,968 and no events at all in the 10000+ bin, where Day has 3,038, so it is excluded by the same kind of argument. T2 is the only dating that can give his profile shape, and it does not give his profile. T2 at m = 1 can rest on a single chromosome in the 10000+ bin.
- **Minimum calls per bin (post hoc grid 20-60; the main grid skipped 20-50):** v62 V1 tracked 0.959 / 0.929 / 0.885 / 0.826 / 0.755 / 0.671 / 0.572 / 0.333 at m = 20 / 25 / 30 / 35 / 40 / 45 / 50 / 60 with eligible 59,789 -> 58,154 and S21 4,794 -> 2,101; dayE the same (0.766 at m = 40, 0.684 at 45). So Day's 0.727 is reached at about 42 called chromosomes per bin on v62, as a candidate for his unstated threshold. It leaves eligible at about 58,300 and S21 at about 3,900. On v66 the fraction is still 0.693 at m = 60.
- **Modern-bin sensitivity (post hoc; S21 and eligible):** v62 diploid-only modern bin 8,443 / 72,424, pseudo-haploid-only 26,307 / 130,855, date-0 only 8,694 / 72,799, historical (0 < date < 500) only 28,218 / 134,135, wide box (adds Turkey, Russia and others) 3,715 / 57,460; with the modern bin dropped, S21 over bins 5000-6000 to 500-1000 is 780. v66: 12,430 / 80,862, 9,529 / 82,729, 12,394 / 80,897, 9,735 / 83,257, 2,790 / 45,480, dropped 443. A smaller or lower-depth modern bin gives more events, not fewer; no composition of the modern bin goes near 21.
- **Why the 0-500 BP events are not luck.** An allele at the 1-2% older-bin frequency of most events has probability 1e-4 to 1e-8 of being absent from 901 modern chromosomes by sampling alone. The events are systematic: a difference between the ancient and modern bins in true frequency (loss of low-frequency alleles by drift, replacement or selection) or in measurement. C1c's neutral model with an error term produces the same pattern (section 6).

### 3.2 Anatomy of the post-6000 BP events (post hoc, v62 / v66)
| Subset | n | transition share | minor allele < 5% in older bins | median minor copies in older bins |
|---|---|---|---|---|
| S23 (6000-7000 BP and younger) | 5,717 / 4,164 | 97.1% / 97.3% | 5,607 / 4,152 | 61 / 77 |
| S21 | 4,957 / 3,649 | 97.7% / 98.2% | 4,861 / 3,640 | 68 / 84 |
| 0-500 BP bin | 4,177 / 3,206 | 98.5% / 99.2% | | 74 / 91 |
| dated 6000-7000 .. 500-1000 BP | 1,540 / 958 | 93.2% / 90.9% | | 6 / 6 |

- Typical event: rs11260588 (chr1), counted allele at 88% / 97.5% / 97% / 98% / 96% / 98% / 98% / 97% / 98% / 98% in the ten older bins and 901 of 901 chromosomes in the 0-500 BP bin. It mirrors the pre-7000 cluster (alleles near fixation that the small old bins call as 100%).

### 3.3 Substitution class, autosomes and sex chromosomes (post hoc; E1/T2, m = 1, all11)
| v62 | eligible | S21 | S21 per eligible | S21 per panel site | pre-7000 | start [99,100) % |
|---|---|---|---|---|---|---|
| all SNPs | 62,757 | 4,957 | 7.9% | 0.40% (of 1,233,013) | 0.909 | 79.0 |
| autosomal transitions (922,079 sites) | 47,937 | 4,559 | 9.5% | 0.494% | 0.891 | 79.0 |
| autosomal transversions (228,560 sites) | 6,306 | 36 | 0.57% | 0.0158% (31x lower) | 0.989 | 99.0 |
| X transversions (34,197) | 1,298 | 18 | 1.4% | | 0.978 | 93.5 |
| Y transversions (13,560) | 1,656 | 59 | 3.6% | | 0.959 | 65.6 |
| all transversions | 9,260 | 113 | 1.2% | 0.041% | 0.982 | 92.3 |
v66: autosomal transitions 3,446 events (0.374% per site), autosomal transversions 44 of 7,614 eligible (0.58%; 0.0193% per site, 19x lower), all transversions 66 of 10,034 (0.66%). Y events come from male-only calls (`.DG` males counted as two chromosomes) and are not like-for-like with autosomal events; the autosomal figures are the ones to compare with Z23046531's autosomes-only convention. On dayE: autosomal transversions S21 = 30 (v62) and 35 (v66). Transversions lose the one quantity the all-SNP reading reproduces: the [99,100) share goes from 79.0% to 99.0% and the 10000+ bin holds 85% of events (Day 18.6%). So no single SNP class reproduces Day: all SNPs fit the start table and miss everything else; transversions fit the pre-7000 share and the order of magnitude of 21, and miss the eligible count, the profile and the start table.

### 3.4 Library type and damage (post hoc 2; v62 and v66; predictions L1-L3 in the docstring)
Per-individual class = worst library present (any minus -> minus; else any half -> half; else plus or USER -> plus; else unknown, which includes shotgun and moderns). V1 ancient individuals by class (v62): minus 1,748, half 4,700, plus 1,069, unknown 859 (plus 432 moderns, all unknown). The classes are very unequal across bins (plus: 1 individual in 10000+, 262 in 2000-3000, 531 in 1000-2000), and a smaller class has fewer chromosomes per bin, which alone changes the statistic; every class result is therefore shown next to a **matched-depth random control** (a random subset of the same size in each bin, fixed seed).

| Test (E1/T2, m = 1) | v62 | v66 |
|---|---|---|
| minor-allele frequency in the ten older bins at transition SNPs that are events dated 0-500 BP: minus / half / plus / unknown | 1.38% / 2.09% / 2.15% / 1.69% | 1.29% / 1.80% / 1.85% / 1.52% |
| same, random controls the size of minus / plus | 1.92% / 1.91% | 1.70% / 1.66% |
| same by damage-rate class: lo (<0.10) / mid / hi (>=0.20) / n.a. | 1.72 / 2.20 / 1.91 / 1.89% | 1.50 / 1.87 / 1.82 / 1.64% |
| class-restricted ancient bins, S21 per eligible: minus (control) | 0.71% (3.1%) | 0.58% (2.2%) |
| half (control) | 5.5% (2.1%) | 5.7% (2.7%) |
| plus (control) | 0.09% (0.79%) | 0.06% (1.1%) |
| M1 transitions from everyone but minus: S21 (control: random individuals of the same number dropped) | 3,071 (2,097) | 2,556 (2,012) |
| M3 transitions from plus + half only: S21 (control) | 2,340 (1,055) | 1,938 (1,285) |
| M4 drop damage-rate >= 0.20 at transitions: S21 (control) | 4,037 (3,881) | 3,103 (3,109) |
| M2 transitions from plus only: S21 (control) | 114 (113) | 69 (66) |
| M5 transitions from damage-rate < 0.10 only: S21 (control) | 151 (145) | 102 (115) |

- **Result:** the transition excess does not depend on library type or damage rate. Fully corrected libraries carry the same minor-allele frequency at the events as non-UDG libraries (if anything higher); the non-UDG class gives a lower S21 per eligible allele than its matched control, not a higher one; removing the putatively most damage-prone individuals from transitions lowers S21 less than removing random individuals; M2 and M5 cut S21 to about 100-150, but so do their controls, because at transition SNPs they leave one to a few chromosomes in the old bins (a depth effect), and in both cases only 1-4% (M2) or 25-49% (M5) of the remaining S21 events are transitions.
- The pre-registered damage predictions failed as stated (section 5, L1). I do not describe the excess as damage. What remains consistent with the data: real differences between the ancient bins and modern Europeans at low frequency (alleles at 1-5% in the older bins that are absent now), possibly concentrated at hypermutable transition sites; residual damage that UDG and USER treatment do not remove; reference or capture-array bias that does not depend on library chemistry. These are not separated here.
- No damage-aware reading reproduces Day's table: in every M reading the 10000+ bin holds 73-93% of the events (Day 18.6%) and the 8000-10000 bin is second. M5 on all chromosomes gives eligible 24,059 (7% above Day's) but S21 151 and the wrong profile.

### 3.5 Neutral comparison for the transversion class: open
C1c's neutral rates (R0, closed population, flat SFS, no error; S21 / eligible): N_e 1e4: 3,925 / 15,200 = 0.26; 2e4: 0.12; 5e4: 0.041; 1e5: 32 / 1,700 = 0.019; 3e5: 0.0085; 1e6: 3.6 / 700 = 0.0051. R2 (replacement) 0.27 / 0.093 / 0.048 at N_e 1e4 / 1e5 / 1e6. Real v62: transitions 0.095 (between the model at N_e 2e4 and 5e4), transversions 0.0057 (the model at about 1e6), Day 0.00094 (below every model cell). On a per-eligible basis the transversion class therefore sits well below the model at textbook N_e and the transition class near it. This is not a calibrated test: the model has a flat site-frequency spectrum and no ascertainment, which matter for the eligible denominator; a transversion-restricted run of the C1c simulator was not made. The comparison is open and is stated as open for both sides in section 8. The earlier statement "roughly 900 expected against 36-113 seen" (3,925 x 0.22 panel share) is withdrawn as uncalibrated.

### 3.6 Day's documented two-period pipeline (post hoc 2 and 4; Z23046531 s2.2-2.4, s3.1-3.4)
Procedure as written (quotes-day Q113-Q117): autosomes; Neolithic 6000-8000 BP against date = 0; at least 100 genotyped samples in each period; frequency = minor-allele proportion among genotyped individuals; events = loci monomorphic in the modern period and polymorphic in the Neolithic. His v62 numbers: 1,143,671 SNPs tested, 17,806 newly 100% + 8 newly 0% = 17,814; 1,372 Neolithic and 680 modern individuals; bands 80.9 / 18.9 / 0.22 % (0-1 / 1-5 / 5-10 % Neolithic MAF); one event with MAF >= 10%. His v66: 1,143,230; 3,469 + 1; 395 and 441 individuals (his own explanation: an ID-matching problem), 3 events with MAF >= 10%.

| v62, autosomes, >= 100 individuals | sample neo / modern | tested SNPs | events | bands 0-1 / 1-5 / 5-10 % | MAF >= 10% |
|---|---|---|---|---|---|
| Day | 1,372 / 680 | 1,143,671 | 17,814 | 80.9 / 18.9 / 0.22 | 1 |
| S1 (V1 lat/long box) | 1,249 / 432 | 1,140,804 | 65,076 | 74.7 / 24.7 / 0.59 | 5 |
| S3 (keruru's regex) | 1,281 / 462 | 1,143,765 | 63,865 | 76.5 / 23.2 / 0.36 | 2 |
| S4 (country list, no Russia) | 1,247 / 562 | 1,140,845 | 61,472 | 74.9 / 24.6 / 0.57 | 3 |
| **S5 (country list + Russia)** | **1,377 / 683** | **1,143,870** | **63,631 (3.6x)** | 77.1 / 22.6 / 0.38 | **2** |
v66, S5: sample 1,912 / 683 (his 395 / 441, not reproducible), tested 1,101,898 (his 1,143,230), events 53,748 (his 3,470; 15.5x), MAF >= 10%: 0 (his 3).

- The sample reconstruction is good: S5 matches his sample size to 0.4% and his tested-SNP count to 0.02% on v62, and the MAF >= 10% completions (2 against 1) are of the same size as his. That is a real convergence for claim C's headline count.
- The event total is not: 3.6x on v62 and 15.5x on v66 (the latter is not a like-for-like target). Requiring at least k copies of the other allele in the Neolithic sample (post hoc 4; k counted in individual dosage) gives 37.7k at k = 3, 25.4k at 5 and 19.5k at 8 on v62 S5, but the band shares move away from his (61 / 38 % at k = 3, 28 / 71 % at k = 8, against 80.9 / 18.9 %). No minor-copy threshold reproduces both his total and his shares. His own two papers also disagree with each other for the same release (22,428 in the 11-bin paper, 17,814 in the two-period paper).
- Conclusion: the processing difference between my reconstruction and his is not in the sample or the SNP filter that his text documents; it is in something not documented (what counts as "newly 100%", how missing calls or relatives were handled, or an error). Neither side can say which.

## 4. keruru's temporal N_e (step 5; B2e, C5b)
Recipe as in his draft (v66.p1; Political Entity country regex with no UK or England in it; ASSESSMENT contains PASS; at least 10,000 autosomal SNPs hit, moderns exempt; 7 bins; 27 y per generation; F = sum (x-y)^2 / sum m(1-m); at least 20 individuals called). Forms: (K) his formula, (B) the same F with correction `1/n0 + 1/nt` in called chromosomes, (C) Nei-Tajima Fc (denominator m - xy). Groups: Meso 322, EN 1,665, LN 1,557, BA 1,846, Iron 1,828, Med 2,974, Modern 559.

| window (v66) | t (gen) | his reported | (K) here | (B1) correct 1/n at mean n | (B) site-wise [95% jackknife CI] | (C) |
|---|---|---|---|---|---|---|
| BA to Medieval | 102 | 8,139 | 7,812 | 9,165 | 9,665 [9,267-10,098] | 9,691 |
| EN to Modern | 250 | 9,835 | 9,672 | 10,271 | 10,508 [9,926-11,162] | 10,555 |
| EN vs Mesolithic | 111 | 938 | 866 | 863 | 872 | 887 |
| EN to LN | 65 | 4,922 | 4,706 | 5,585 | 5,954 | 5,973 |
| EN to BA | 120 | 6,933 | 6,761 | 7,792 | 8,273 | 8,303 |
| EN to Iron/Roman | 176 | 9,792 | 9,691 | 11,107 | 11,520 | 11,561 |
| EN to Medieval | 222 | 8,530 | 8,410 | 9,100 | 9,302 | 9,341 |

- (K) reproduces all seven published values within 1-8% (BA-Med -4.0%, EN-Modern -1.7%); SNP counts agree to 0.3%, mean sample sizes to 0.4-7%. My v62 values: BA-Med (K) 6,368, (B) 8,228; EN-Modern (K) 7,269, (B) 8,086. Generation time 25-31 y: BA-Med (B) 10,438-8,418.
- **The sampling correction.** The factor-of-2 point is exact for pseudo-haploid bins: pure binomial sampling of n0 and nt alleles gives E[F] = 1/n0 + 1/nt, and Nei-Tajima's 1/(2S) is that with S diploid individuals. His own code comments say S is the allele count (`adna_validate.r` L45-46; `adna_temporal_ne.r` L13-17; `adna_tgeno.r` L74-77) and then apply `1/(2S)` (`adna_validate.r` L50; `adna_tgeno.r` L88-89; `adna_trajectory.r` L32-33), and the draft's power rule says "S >= 10 N_e/t alleles" (draft L190). The scripts that produce the draft's numbers use called individuals as S (S = 476 for Modern in the draft); only the superseded reader `adna_stream.r` (L67-70) doubles S for the Modern bin, so it is not the source of the draft's values. His validation simulation (`adna_validate.r` L43, `samp_pseudohap` draws S alleles) therefore carries the same under-correction, which is of the size of the 0.82 recovery he reports at the power margin (draft L193, which he attributes to power; my inference from the size match). He also states that the residual biases run downward ("Three known biases, all downward", draft L212): the direction of the effect was disclosed.
- **Size of the effect.** Decomposition (post hoc 3, v66): BA-Med +17.3% from the factor of 2 at mean depth, +5.5% more from unequal per-SNP depth (site-wise correction), +23.7% in total against (K); EN-Modern +6.2% and +2.3% (+8.6%). Over the seven windows the total uplift against (K) runs from +0.7% (Meso) to +26.5% (EN-LN); against his published numbers the two headline windows rise +18.7% and +6.8%. In the Modern bin (mostly diploid) 1/(2S) with S in individuals is already right; the halving applies to the pseudo-haploid bin(s) of each window. The Nei-Tajima agreement (C within 0.3% of B) is algebraic: m - xy = m(1-m) + (x-y)^2/4, so it confirms the code, not the estimator.
- **Against Wright's frame.** With V_k = 5, N_e = 4N/(V_k+2) = 0.571 N. The measured corrected F_adj for BA-Med is 0.00527 (v66; 0.00619 on v62). Census sensitivity (v66): at N = 1e5, Wright's N_e = 5.7e4, drift-only F = 8.9e-4, so 5.9x below the measured F and 83% of it would have to be non-drift for Wright to hold; N = 3e5: 17.7x, 94.4%; N = 1e6: 59x, 98.3%; N = 3e6: 177x, 99.4%; N = 1e7 (keruru's unsourced census): 591x, 99.83%. Wright matches the measured N_e of 9,665 only if the whole sampled population is 16,900 (14,400 on v62).
- **What F contains.** (i) Ancestry informativeness along the three source axes (per-SNP variance across WHG, Neolithic-Turkey and Yamnaya source samples, 1.0 M SNPs, quintiles; the sources are drawn from the same data as the target bins and Yamnaya sit inside the Late Neolithic group, so for windows including those bins, here LN-BA and EN-Meso, the informativeness shares sampling noise with F and the 1.18x gradient for LN-BA carries that caveat): F_adj by quintile for BA-Med is flat (0.00536 -> 0.00516; top/bottom 0.96; intercept N_e 9,530); EN-Modern 0.0104 -> 0.0136 (1.31x; intercept 11,996); EN-BA 0.0047 -> 0.0102 (2.14x; intercept 12,150); EN-Medieval 1.63x. (ii) **Composition counterfactual (replaces my earlier claim).** For two mixtures of the same regional populations with proportion shifts d_r and pairwise F_rs, the F from the shift alone is F_comp = sum over r<s of (-d_r d_s) F_rs. With the five regions (Iberia / Central / Italy-Balkans / Scandinavia / East: BA 13 / 37 / 21 / 7 / 22 %, Medieval 5 / 65 / 7 / 16 / 7 % on v66), F_comp = 0.00082 (15.5% of the BA-Med F_adj) with the BA-bin pairwise F and 0.00032 (6.1%) with the Medieval-bin pairwise F; v62 0.00106 (17.2%) and 0.00037 (6.0%). Composition shifts among these five regions therefore explain at most about a sixth of the F; within-region ancestry heterogeneity, cemetery clustering and relatedness are not included, and the pairwise regional F contain within-bin date spread (bins are 1,000-1,500 years wide, so "same-time" samples can differ by several generations) and relatedness. (iii) **Within-region N_e (form B, BA to Medieval, v66):** Iberia 4,442 (S 79/56), Central Europe 3,407 (S 262/887), Italy-Balkans 7,166 (S 168/112), Scandinavia 14,637 (S 51/220), Eastern Europe 3,909 (S 179/112), against 9,665 pooled. Only Central Europe is close to the power rule S >= 10 N_e/t (ratio 0.78; the others 0.04-0.29), and its value is the lowest. A composition artefact predicts within-region values at or above the pooled one; four of five are lower. They point away from composition as the main driver. They are also what local structure (cemeteries, sub-regions) and small samples give, so they do not show the absence of structure. (iv) Not tested: relatedness filtering (his draft states it is unfiltered), library and damage batch effects.
- **Reading.** Every non-drift term adds to F, so 9-10 thousand is a lower bound on a drift N_e; the rise from 872 to 10,508 across windows is what a growing population produces and what progressively less concentrated sampling produces. The measurement is real; it contradicts Wright's formula only if F_nondrift is a small fraction of F. At the unsourced census of 1e7 that fraction would have to be below 0.2%, which nothing measured supports; at 1e5 it would have to be below 17%, which the composition counterfactual (6-17%), the weak ancestry gradient and the within-region values also do not support. Day's N_e near 2 (C5a) is excluded: the observed F_adj of 0.005-0.014 is nowhere near the saturation that N_e = 2 implies.
- **Credit to keruru.** His draft already tests three artefact explanations in §6.1 (island model: structure inflates the estimate, N_e/N 0.83-2.44; a moving sampling frame does essentially nothing, 1.02-1.13; reproductive variance: 0.535 against Wright's 0.571 at V_k = 5, flattening near 0.05 at high V_k) and a spatial-spread check in §3.2, and states the bias direction. My simulation below tests admixture only and does not test his island or moving-frame results. His own simulation shares the under-correction above, so his recoveries are biased low by the same few to fifteen per cent.

### Simulation of the estimator (c1d_sim.json; WF, N_e = 1e4, t = 100, 200k loci, pseudo-haploid n 800 / 1500, source drifted 700 generations, pulse at generation 50)
| pulse m | F | (K)/true | (B)/true | intercept/true |
|---|---|---|---|---|
| 0 | 0.00692 | 0.84 | 1.00 | 1.00 |
| 0.05 | 0.00674 | 0.86 | 1.04 | 1.06 |
| 0.10 | 0.00676 | 0.86 | 1.03 | 1.11 |
| 0.20 | 0.00736 | 0.78 | 0.92 | 1.23 |
| 0.40 | 0.01077 | 0.51 | 0.56 | 1.48 |
Closed N_e 3e4 and 1e5: (B)/true 1.00 and 0.99. Admixture invalidates the estimator only for large pulses from a differentiated source (m >= 0.2 with source Fst about 0.04). The informativeness-intercept correction over-corrects (1.23, 1.48): a diagnostic, not an estimator.

## 5. Pre-registered predictions: what held
Main run (`c1d_aadr_real.py`):
| P | Prediction (credence) | Result |
|---|---|---|
| P1 | layout/QC (95%); pseudo-haploid het < 1e-4 | **Held for the layout** (corr 0.9999997; ratio 1.000), **het sub-prediction failed narrowly** (1 individual on v62 and 2 on v66 at 1.2-1.6%, all others 0). |
| P2 | V1 within 5% in 9 of 11 bins, 8,808 total (90%) | **Held** (9 of 11; 2000-3000 BP +5.04%; 0-500 BP -16%). |
| P3 | eligible within 2x of 22,428 (50%) | **Failed.** 62,757 (2.8x); v66 2.2x. |
| P4 | S21 >= 105 (60%) | **Held.** 4,957 / 3,649. |
| P5 | a grid configuration reproduces eligible, S21 and tracked (25%) | **None did.** The closest eligible count in the grid is 2.4x Day's. |
| P6 | pre-7000 share >= 0.99; 10000+ below 50%; 8000-10000 the plurality | **Failed on all three.** 0.909; 73%; 8000-10000 second (17%). |
| P7 | [99,100) share 60-95%; <90% share <= 1%; singletons >= 40% | **Held on all three** (79.0%; 0.5%; 50.3%). |
| P8 | T1 puts >= 500 events in 0-1000 BP (90%) | **Held** (53,863). |
| P9 | tracked >= 0.90 at m = 1; falls to 0.65-0.80 at m >= 10 or the intermediate rule | **Held on v62 with the full m-grid:** 1.000 at m = 1; 0.755 at m = 40 and 0.671 at m = 45 (the main grid skipped 20-50, so the earlier "half held" was an artefact of the grid). On v66 the fraction is still 0.693 at m = 60. |
| P10 | >= 80% of post-5000 events have older-bin minor frequency < 5% (65%) | **Held** (98.1%), measured over all bins older than the event's bin (for a 0-500 event, ten bins), not the "<= 7000 BP bins" registered; same direction. |
| P11 | his recipe reproduces BA-Med and EN-Modern within 10% | **Held** (-4.0%, -1.7%). |
| P12 | (B) 10-25% above (K) for BA-Med; 3-8% for EN-Modern; (C) within 5% of (B) | **BA-Med held (+23.7%); EN-Modern failed narrowly (+8.6%); (C) within 0.3%** (algebraic, so it could not fail). The factor of 2 is analytic, not an independent prediction. |
| P13 | trajectory shape as reported | **Held** (872; 1.07-1.21x). |
| P14 | top/bottom informativeness quintile >= 2x (EN-Modern), >= 1.3x (BA-Med) | **Failed** (1.31x, 0.96x). |
| P15 | drift-only N_e < 1e5 (85%) | **Held** (9,530-14,089). |
| P16 | closed (B) within 10%; (K) 10-20% low; 10% pulse drives (B) below 0.7x | **Mixed:** (B) 1.00, (K) 0.84; **10% pulse refuted** (1.03); intercept within 25% to m = 0.2, 1.48 at 0.4. |
Post hoc 2 (predictions written before the run):
| P | Prediction | Result |
|---|---|---|
| L1 | damage: (a) transition share >= 90% in every class; (b) minus S21 per eligible >= 2x its control and >= 2x plus; (c) older-bin minor frequency at 0-500 events >= 2x higher in minus than plus | **All three failed.** (a) minus 0.92 / half 0.98 held, plus 0.57 (7 events) and unknown 0.82 failed; (b) minus is 0.23x its control; (c) 0.64x (v66 0.70x). |
| L2 | M2 cuts S21 below 1,000 but eligible not within 2x of 22,428; control cuts less than M2; no reading reproduces the profile | **M2 cuts S21 to 114 but eligible is 16,100 (within 2x) and the control cuts it equally (113); no reading reproduces the profile (held).** |
| L3 | a reading near 21 has eligible < 12,000 | **Failed narrowly** (M2 autosomes: 37 with 12,340; M5 autosomes 70 with 19,273; autosomal transversions 36 with 6,306). |
| T1 | S5 two-period: sample within 2%; SNPs within 2%; events 15k-60k and not within 10% of 17,814; bands within 3 points; MAF >= 10% <= 20; v66 well above 3,470 | **Held:** 0.4%, 0.02%, not within 10%, 2 events with MAF >= 10%, v66 53,748. **Failed:** events 63,631 (just above 60k); bands 3.7-3.8 points off. |
| T2 | the S4 country-list sample gives eligible and S21 within 25% of V1's | **Held** (+0.8%, +1.8%). |
| T3 | tracked fraction crosses 0.727 between m = 35 and 50; S21 > 3,000 and eligible > 50,000 across the range | **Held for m <= 50** (S21 2,101 at m = 60). |
| T4 | modern-bin variants never below 700 or above 30,000; dropping the modern bin leaves 400-1,200 | **Held** (min 2,790; max 28,218; dropped 780 and 443). |
Systematic errors in my priors: I expected the real data to look like the C1c model with eligibility within 2x and a non-dominant 10000+ bin; I expected library type to matter; and I expected strong admixture structure in the temporal F. None held.

## 6. Link back to C1c
C1c's model with R0, N_e = 1e4 and a 0.1% false-minor-call rate gave eligible 61,353 and S21 4,217. The real v62 literal reading gives 62,757 and 4,957 (v66 48,888 and 3,649), and the real events are transitions at 1-5% older-bin frequency, a pattern the model reproduces by assumption of an error term but which the library test says is not damage. The agreement is within about 20% and is partly coincidence (profile, tracked fraction and start table were not fitted; the model's error term and the real excess have different causes as far as tested). It does not make the model a valid null for Day's table, because his table is still not reproduced.

## 7. Verdict suggestions (not applied; claim files untouched)
- **C6 (the 11-bin statistic): external `untestable` -> `contradicted` for the literal rule.** The statistic was tested, not untestable: the stated method on the public data gives 62,757 / 4,957 (v62) and 48,888 / 3,649 (v66) against 22,428 / 21, a profile in which 8000-10000 BP holds 17% not 53.6% of events, and 9% (not 0.14%) of events after 6000 BP; 132 grid cells and the documented two-period pipeline do not close it. State Day's best reading in the comment: the method as published is underspecified (no damage handling, quality filter, coverage threshold or country list is stated), and a different unpublished pipeline may have produced 22,428 and 21; the library test shows that damage handling is not the missing piece. If he documents the pipeline, re-open as `contested`. The sentence "cannot adjudicate pending a call-depth model" should be replaced. Keep internal `arithmetic-error` (the 99.8% / 2,000-year window wording).
- **C (two-period statistic, 1 and 3 of 1,143,671): external `contested` stays; add that the count reproduces in kind** (S5 gives 2 events with Neolithic MAF >= 10% on v62 and 0 on v66, against his 1 and 3; sample and SNP filter reproduced to 0.4% and 0.02%) while his event total (17,814) is 3.6x below the reproduction. Internal `non-sequitur` unchanged. The "neutral also predicts ~0" wording in C's internal comment is the repo's own earlier audit wording, not a critic's, and is corrected by C1b/C1c; the 21-statistic result does not by itself change C's verdicts.
- **C5b: internal `pending` -> `arithmetic-error` (minor: 1/(2S) with S an allele count under-corrects pseudo-haploid bins by half; raises N_e by 0.7-26.5% against his formula); external `pending` -> `supported`** as a measurement of the sampled series' variance N_e (replicates to 1-8% in two releases; corrected values 9.7k and 10.5k), with the comment that it is a lower bound on a drift N_e and that C5a's N_e near 2 is excluded.
- **C7: external `pending` -> `contradicted` for "no allele-frequency movement"** (F_adj between bins 0.002-0.014 across 28-250 generations, far from zero); attribution to drift versus admixture, structure and composition stays open (B2e). Internal `non-sequitur` unchanged.
- **B2b: unchanged, `contested`.** The temporal data neither support nor contradict the Wright input; the lower-bound property means they cannot show it wrong, and the census sensitivity shows what non-drift share would have to hold.
- **B2: unchanged, `contested`.** No new evidence on the ceiling itself.
- **B2e: external `pending` -> `contested`; score RF-12 and RF-13 separately.** RF-12 ("wrong by three orders of magnitude"): not established at the unsourced census of 1e7 (needs F_nondrift below 0.2%); a gap of at least 6x at any census of 1e5 or more is robust to the non-drift terms tested (ancestry axis under 4%, composition 6-17%). RF-13 ("measurably wrong where it can be tested", explicitly not a refutation): partly supported; the measurement is real and replicates, and is a lower bound. Internal `holds` stays; add the factor-of-2 correction and keruru's own §6.1 simulations to the comment.

## 8. Who this helps
**Day / allies**
- The start-frequency table reproduces to 0.4 points on v62 and the sample of his second paper reproduces to 0.4%; his §4.3 description is right in kind (98.8% of v62 eligible alleles start at 95-100%).
- In the transversion class the pre-7000 share is 0.98-0.99, close to his 0.9986, and the post-6000 count is 36-44 on autosomes (113 and 66 with X and Y), one to five times his 21. Per eligible allele that class is 0.57%, against 0.094% for his figure.
- The method text is short and gives no damage, quality, coverage or country-list rule, so the failure to reproduce is as much a documentation gap as a verdict on his result; the damage hypothesis was tested and failed, so that gap is not simply a missing UDG filter.
- The comparison of the transversion class with a neutral expectation at textbook N_e is open (section 3.5). The per-eligible rate in that class (0.0057) lies well below the C1c model at N_e 1e4 (0.26) and near its N_e 1e6 value; if a calibrated, SFS-matched model confirms this, it is a deficit against neutral at textbook N_e that the thousands in the all-SNP statistic conceal.

**Critics**
- His table does not reproduce under the stated method nor under his own documented two-period pipeline (3.6x on events), so neither "99.8% before 7000 BP" nor "essentially zero afterwards" is supported by the published procedure on the public data; the post-6000 events are 9% of the literal total, not 0.14%.
- The thousands are real and reproducible (two releases, two samples) and the transition-class concentration is not removed by any library or damage filter; C1c's neutral-plus-error model predicted the all-SNP numbers within 20% (section 6).
- keruru's N_e replicates to 4% in two releases with his own recipe; the ancestry-axis stratification does not remove it; the corrected sampling term raises it; his §6.1 simulations are real tests that the review had not credited; admixture matters little for BA-to-Medieval and only for windows crossing the steppe arrival.
- Day's N_e near 2 (C5a) is excluded.

**Open or neutral**
- Whether temporal N_e contradicts Wright's N_e: a lower bound; census-dependent (6x at 1e5, 59x at 1e6, 591x at 1e7); the non-drift share needed is 83%, 98.3% and 99.8%; composition among five regions explains 6-17%; within-region values do not move toward Wright but are themselves structured and under-powered.
- The neutral comparison for the transversion class (section 3.5), for both sides.
- What the transition excess is (section 3.4).

**Cuts against critics**
- The "assay or damage error" reading of the thousands (item in earlier drafts of this note, and C1c's error term) is not supported by the library-type test; the excess is not specific to damage-prone libraries.
- The damage-immune transversion count (36-113) is near Day's number, so "neutral predicts thousands" is not the whole picture once the transition class is set aside.
- keruru's formula under-corrects pseudo-haploid bins by half (0.7-26.5% on N_e; disclosed direction of bias); his N_e/N of 1e-4 to 8e-4 rests on an unsourced census (inconsistent across the draft, RF-14); the region regex excludes Britain and relatives are unfiltered (disclosed by him; not quantified here).
- The "neutral also predicts ~0" reading is the repo's own earlier wording (C's internal comment, C6 "earlier audit wording"), not a critic's claim; it is false for the literal 11-bin rule, which is a correction of the repo's audit.

## 9. Caveats
- Day's procedure is a reconstruction from prose; unpublished choices (quality filters, calibrated-date field, what "tracked" requires, sex chromosomes, how moderns were chosen) may differ from mine. The v62.0.p1 patch is not the v62.0 original he used. His modern bin has 625 individuals against 524 in V1 and 638 in dayE; the two-period paper's 680 moderns are reproduced only by a country list that includes Russia.
- The 132 grid cells (120 on V1 plus 12 on V2), the m-grid, the library classes, the damage-aware readings and the post hoc rules (T3, minor-count >= k, transversions) are exploratory and were not fitted to hit his numbers; the dayE and S5 samples were chosen after an anno-only count of individuals against his sample sizes (a calibration of the sample, not of the statistic). The grid does not exhaust possible implementations.
- Library classes are defined by the worst library in a merged individual and are very unequal across bins; the matched random controls remove the depth effect but not all composition effects (class membership is correlated with site, date and region). The damage-rate column is a merged-data first-nucleotide rate that is missing for many individuals. UDG-half and USER treatment leave some residual damage that this test cannot see.
- Temporal N_e: jackknife CIs by chromosome (22 blocks, z = 1.96) understate individual-level, relatedness and linkage variance. The informativeness intercept over-corrects in simulation. The composition counterfactual covers five regions only. The Wright formula and the census N = 1e7 are used as keruru frames them and were neither retrieved nor tested.
- All counts are on the 1240K panel with its own ascertainment; no mutation or selection model; V1 and dayE are not Day's exact samples.

## 10. Review resolution
Reviews: `REVIEW-R4-C1d-correctness.md` (0 BLOCKER, 3 MAJOR, 10 MINOR), `REVIEW-R4-C1d-steelman-day.md` (4 MAJOR, 6 MINOR), `REVIEW-R4-C1d-steelman-critic.md` (5 MAJOR, 4 MINOR). "Applied" means the text or a run now does what the finding asks.

**Correctness**
| # | Sev | Finding | Resolution |
|---|---|---|---|
| 1 | MAJOR | Day's documented two-period pipeline not computed | **Applied.** Section 3.6 (post hoc 2, 4): sample 1,377 / 683, SNPs 1,143,870, MAF >= 10% 2, events 3.6x; "a different quantity" replaced. |
| 2 | MAJOR | Composition claim unsupported by the numbers | **Applied.** Section 4: F_comp counterfactual 6-17% of F; "no time elapsed" removed (bins are 1,000-1,500 years wide); the claim in the Day bullet and in section 8 is withdrawn; within-region N_e interpreted. |
| 3 | MAJOR | "No setting gives tracked 0.65-0.80" false (m-grid hole) | **Applied.** Section 3.1 m-grid 20-60; P9 held on v62 (0.755 at 40, 0.671 at 45), v66 reaches 0.693 only at 60. |
| 4 | MINOR | +24% mixes two corrections | **Applied.** +17.3% factor of 2 and +5.5% depth heterogeneity (BA-Med); per-window 0.7-26.5%; Modern bin note. |
| 5 | MINOR | Which keruru code; Modern S doubling | **Applied.** Section 4 cites adna_validate.r, adna_tgeno.r, adna_trajectory.r and the superseded adna_stream.r (Modern doubling), and that the draft's S = 476 shows it is not the source. |
| 6 | MINOR | Fc agreement is algebraic | **Applied** (section 4, P12 row). |
| 7 | MINOR | Bit-order evidence weaker than stated | **Applied** (section 2: trajectories are the evidence; QC validates layout; verify.py uses the same shift expression). |
| 8 | MINOR | Transversion headline mixes autosomes with X and Y; "100-fold" | **Applied.** Section 3.3 splits 36 / 18 / 59; per-site rates 31x (v62), 19x (v66) on autosomes, 12x and 16x with all chromosomes; per-eligible 16.7x; brief rewritten. |
| 9 | MINOR | "Happens to call as 100%" misleading; modern-bin sensitivity missing | **Applied.** Section 3.1 (probability argument; diploid-only, pseudo-haploid-only, date-0, historical-only, wide box, dropped). |
| 10 | MINOR | T3 exclusion; n = 1 in 10000+ bin | **Applied** (section 3.1). |
| 11 | MINOR | P12, P1, P10 wording; "8 rules" (10); figure script commit | **Applied** for P12 (EN-Modern failed narrowly), P1 (het sub-prediction failed narrowly), P10 (all older bins), and the rule count is now 10 (T3, four minor-count thresholds x two site sets, T3 with minor >= 2); the figure script cannot be moved out of commit 0c696f9 without rewriting history (**declined**), but this revision of it is in its own post hoc commit. |
| 12 | MINOR | Informativeness sources overlap the target groups | **Applied** (section 4(i) caveat for LN-BA and EN-Meso). |
| 13 | MINOR | Scripts search: evidence retained, scope, wording, format statement | **Applied.** ORCID, creator, software and title queries saved; GitHub, OSF and blog searched read-only; wording "not found on the records searched"; TGENO statement corrected (v62.0 PACKEDANCESTRYMAP, v66.p1 TGENO; the retrieved v62.0.p1 is TGENO). |

**Day-side steelman**
| # | Sev | Finding | Resolution |
|---|---|---|---|
| F1 | MAJOR | Damage lever missing; "not reproduced under any reading" too strong | **Applied.** Section 3.4: library classes, damage-rate classes, five damage-aware readings, matched random controls, event attribution; all three predictions failed; the headline now says "literal reading or any of the 132 grid cells", transversions are reported with their mismatches, and "false under his own rule" is gone. The note no longer says the excess is damage (it says it is not explained by library type or damage rate). |
| F2 | MAJOR | Scripts attached to the wrong paper; Zenodo-only; 404 artefact | **Applied.** Section 1 (promise is in Z23046531 s5, may mean on request; GitHub, OSF, blog searched; versions lookup repeated on the record's own link, one version). |
| F3 | MAJOR | Two-period pipeline as calibration | **Applied.** Section 3.6; v66 flagged as not like-for-like (his 395 / 441). |
| F4 | MAJOR | Transversion-vs-neutral stated in opposite directions | **Partly applied.** Both bullets now say the comparison is open; per-eligible rates against C1c's R0 and R2 reported (section 3.5); the "roughly 900" figure withdrawn. A transversion-restricted run of the C1c simulator was not made: the model has no substitution classes or ascertainment, so a restricted run would only rescale the same flat-SFS assumptions. |
| F5 | MINOR | p1 vs original v62.0; modern-bin definition | **Applied.** The 161 arithmetic and the v66.p1 match (an inference); date-0, historical and wide-box variants (section 3.1). |
| F6 | MINOR | m-grid coarse where tracked crosses 0.727 | **Applied** (m = 25-45 added). |
| F7 | MINOR | Precision of headline numbers | **Applied.** 97.1% (S23) and 97.7% (S21) stated separately; factors given; both classes in every one-line summary; "in the grid" kept. |
| F8 | MINOR | Scope of the factor of 2; quoted range | **Applied** (0.7-26.5% against (K); +18.7% and +6.8% against his published values). |
| F9 | MINOR | Credit to Day buried | **Applied.** Result in brief item 5 and section 8. |
| F10 | MINOR | Method quotes not registered | **Applied.** `docs/research/sources/quotes-day.md` Q106-Q117, verified verbatim against the saved texts. |

**Critic-side steelman**
| # | Sev | Finding | Resolution |
|---|---|---|---|
| F1 | MAJOR | Transversion result over-used and inconsistent | **Applied.** Rate per eligible, 10000+ share 85%, lost start table, 36 vs 113 stated; "same order" and "near Day's number" removed from the critics' bullet; both bullets say the neutral comparison is open. |
| F2 | MAJOR | Damage asserted in section 8, disclaimed in section 3; test cheap | **Applied.** The UDG split was run (section 3.4): not damage by library type; the critics' "error-class artefact" wording is withdrawn and listed under "cuts against critics". |
| F3 | MAJOR | `untestable` wrong; scripts on the wrong paper; compute the two-period statistic | **Applied.** Section 7 proposes `contradicted` for the literal rule with the underspecification caveat; scripts moved to C / Z23046531; two-period statistic computed as post hoc (not pre-registered: noted). |
| F4 | MAJOR | "Not established" hides an asymmetry | **Applied.** Census sensitivity (1e5, 3e5, 1e6, 3e6, 1e7), break-even N 16,900, non-drift share needed; RF-12 and RF-13 scored separately; keruru's §3.2 and §6.1 credited. |
| F5 | MAJOR | Regional-F point mis-scaled, contradicted, misattributed | **Partly applied.** F_comp counterfactual replaces it (6-17%); within-region N_e interpreted with the power caveat; "his own measurement shows" deleted. The post-stratified recomputation (reweighting Medieval to the BA regional composition and re-estimating N_e) was not run: the sampling-variance correction for a weighted mixture of small regional samples (25-80 chromosomes in several cells) would be dominated by noise, so the arithmetic counterfactual is reported instead. |
| F6 | MINOR | Correction is an error by his own comments; cite lines | **Applied** (code lines in section 4; effect +17% from the factor of 2; direction disclosed). |
| F7 | MINOR | Critic-error list: repo's own wording, unquantified items at full weight, omitted credits | **Applied.** "Neutral predicts ~0" relabelled as the repo's earlier wording; regex and relatives marked disclosed / unquantified; P14, P16 and C1c-prediction credits added. |
| F8 | MINOR | Day/allies block holds critic-qualifying items | **Applied.** Moved to "Open or neutral" and "Cuts against critics". |
| F9 | MINOR | "do not exist" vs "not found"; 84% in the youngest bin | **Applied.** |
