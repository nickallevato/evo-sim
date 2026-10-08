# Version and Drift Ledger (Day corpus)
Each row is a quantity that changed across sources or versions. Evidence is in `sources/quotes-day.md`.

| Quantity | Values by source/date | Note |
|---|---|---|
| Required fixations | 30M (2019 blog) → 20M (Z18165980, 2025) → 205M (Z23003785, 2026) | 205M = (35M SNV + 187 Mb + 1,140 inversions → 410M) / 2. This mixes units; Yoo 2025 contains neither 410 nor 187 Mb. |
| G_f (gens/fixation) | 1600 (2019; "Nature 2009" → later "Good 2017") → 1,322 (≥95% rule, Z23003785) → ~1,587 (strict counts, Z23105291, derived) | Day's own data paper: the strict count (5,496) is 37% lower than the ≥95%-rule count (8,679), i.e. the ≥95% rule counts 58% more. |
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
| N vs Nₑ in k | k = μN/Nₑ (Z18429937, Z18525547, Z18637333; Jan–Feb 2026) → **conceded 2026-08-27**: Nₑ never enters the Kimura identity (supply 2Nμ, fixation 1/(2N)); Hard Limits "accepts k=μ throughout" → k = 32.3μ reappears (blog 2026-10-01) | The Zenodo records were not revised after the concession. The concession came one day after keruru's retraction. |
| Pipeline start state | Intrinsic Irrelevance assumes an empty pipe at the split → blog 2026-10-01: the pipe was "full, but much shorter" (228,000 gens) | Contradicts the empty-start premise (claim B1d). |
| Hard Limits ceiling | abstract "about ten thousand" vs its own Table 1 (35,000–114,000) | 3.5–11× gap (claim B2b). |
| Implied Nₑ/N | Hard Limits implies Nₑ = 0.57N; the recalibration paper uses Nₑ = 3,300 for the same census | Cross-paper inconsistency. |
