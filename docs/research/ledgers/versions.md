# Version and Drift Ledger (Day corpus)
Each row is a quantity that changed across sources or versions. Evidence is in `sources/quotes-day.md`.

| Quantity | Values by source/date | Note |
|---|---|---|
| Required fixations | 30M (2019 blog) → 20M (Z18165980, 2025) → 205M (Z23003785, 2026) | 205M = (35M SNV + 187 Mb + 1,140 inversions → 410M) / 2. This mixes units; Yoo 2025 contains neither 410 nor 187 Mb. |
| G_f (gens/fixation) | 1600 (2019; "Nature 2009" → later "Good 2017") → 1,322 (≥95% rule, Z23003785) → ~1,587 (strict counts, Z23105291, derived) | Day's own data paper says the ≥95% rule inflates counts by 37%. |
| 4,615 "NS-only max" | blog 2026-09-30 only | Z23003785 gives ~1,408 per beneficial fixation. |
| Ara+2 | 909 = 60,000/66 (blog) vs 917 = 60,500/66 (Z23105291 Table 1) | Derived. |
| Max fixations (2019 post) | table 125 / text 562 / arithmetic 450,000/1600 = 281 | Internal inconsistency. |
| d | 0.45 in both Zenodo papers, computed on different loci (LCT/SLC24A5/HERC2 vs LCT/SLC45A2/TYR) | MITTENS 3.0 drops d. |
| SNV-only shortfall | 91,600× (Z23003785) | Pass 1 said ~94,000×. |
| Bernoulli 10^−34,000,000 | Appears in Z18165980 (MITTENS), not in Z18167588 (Bernoulli paper) | The Bernoulli paper uses n=157,000, p=0.5 → 10^−47,262. Its "~230 sweeps" is stated as "working backward from the constraint". |
| k/μ | 0.743 (Z18525262) and 32.3 (blog 2026-10-01, no derivation) | The two values are mutually inconsistent in direction. |
| aDNA fixations | 0 of 1,211,499 loci (blog 2026-01-14) → 1 (v62) / 3 (v66) completing from the 50–90% start range, 0 from <50% (Z23046531, 1,143,671 SNPs) | |
| CHLCA | 6.3–9 My → 200–580 kya (Z18525547) → 68 kya (Z18637333) → 250 kya–1.3 Mya (retraction, 2026-05-07) | |
| Retraction 2026-05-07 | targets Term 3 (Haldane cost limit) of Z19984826 | |
| Z23003785 | created 2026-09-28, modified 2026-10-04 | Check for content changes before quoting. |
