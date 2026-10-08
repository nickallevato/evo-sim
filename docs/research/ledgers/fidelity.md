# Citation-Fidelity Ledger

This ledger records whether each cited source actually says what it is cited for. It applies to both sides.

Status legend:
- **verified-accurate:** the cited use matches the source.
- **verified-partial:** the source supports the use only in part.
- **verified-misread:** the source does not support the use.
- **unverified:** we could not read enough of the source to judge.
- **not-found:** we could not locate the source, or the cited figure is absent from it.

Evidence is in `sources/quotes-literature.md`. Every quote there was machine-checked as an exact match to the extracted text.

## R1 pass 2 (2026-10-07) — supersedes the pass-1 ledger in PLAN.md
| Source | Cited for (by) | Status | Evidence / note |
|---|---|---|---|
| Kimura 1962 | fixation prob ≈ 2s; 1/(2N) (Day, critics) | **unverified** (pass 1 said accurate) | PMC bot challenge; no abstract. Result is textbook; B0.1/B0.3 reproduce it numerically. |
| Kimura & Ohta 1969 | t̄ = 4Nₑ, SD ≈ 2.15Nₑ (Day) | **unverified** (pass 1 said accurate) | Same block. B0.2 reproduces it numerically. |
| Kimura & Ohta 1969 | "fixation time does not depend on recombination" (Day) | unverified | Was recorded as a misread in pass 1; not re-checked. |
| Haldane 1957 | ~1 substitution / 300 gens (Day) | **verified-accurate, via Nunney 2003 only** | Primary text not retrieved. |
| Nunney 2003 | cost of selection | verified | Cost "substantially less" than Haldane's for M > 1/2; soft selection "eliminates" it. This is the only H-branch rebuttal in the corpus. |
| Chalub 2022 | k = μ is a misapplied steady-state identity (Day) | **verified-partial** | Math correct. The model is neutral, two alleles, "without mutation or selection", so it says nothing about the substitution rate k. That limits its relevance to B1. |
| "Chalub 2012" | Kimura's followers ignored time (Day) | **not-found** | The nearest are Chalub & Souza 2009, 2014 and 2017. |
| Balloux & Lehmann 2012 | k ≠ μ; 0.743μ (Day) | **verified-partial** | N-dependence arises only with overlapping generations *plus* fluctuating N. Under non-overlapping generations, fluctuations "do not affect substitution rates at neutral loci". 0.743 and 32.3 are not in the paper. → Defines B3b precisely. |
| Zeng 2021 | s = 0.001 for beneficial mutations (Day) | **verified-misread** | ~0.001 is the mean coefficient of *negative* selection on complex traits. |
| Yoo 2025 | 410 Mb, ~205M required fixations (Day) | **not-found** (figure) | SDRs average 327 Mb per lineage. 1,140 inversions is a six-ape count. Neither 410 nor 187 Mb appears anywhere. |
| Yoo 2025 | 6.3 My split (Day) | **verified-accurate** | 5.5–6.3 My (min–max). |
| Yoo 2025 | ancestral Nₑ | verified | 198k (HCB ancestor), 132k (HCG ancestor). Our placeholder 5e4–1e5 is superseded. Relevant to B1b/B1c. |
| Yoo 2025 internal | SNV divergence | discrepancy | SI text says 0.15–0.16%; Table III.14 says 1.46%. Unresolved. |
| CSAC 2005 | ~35M SNV, 5M indel (both sides) | **verified-partial** | One genome per species, including polymorphism; polymorphism is 14–22% of divergence. Fixed divergence ≤1.06% vs 1.23% total. |
| Langergraber 2012 | 6–7 My via fossils (Day, Bio-Cycle paper) | **verified-misread** | Says "at least 7–8 million years", independent of fossil calibration. |
| Bergeron 2023 | 40× variation in mutation rate | verified-accurate | Human value is in SI Table 8 (not retrieved). |
| Keightley 2012 | μ ≈ 1.1e-8 | verified-partial | Abstract only. |
| Good 2017 | ≥95% fixation rule (Day MITTENS 3.0) | **unverified** | Not in the main text; SI not retrieved. Good reports clade coexistence and rejects sweep-by-sweep models. |
| Tenaillon 2016 | neutral accumulation constant | verified | "neutral mutations accumulate at a constant rate" in non-mutators. |
| Mathieson 2015 | LCT/SLC24A5 s values (Day) | unverified | Not in main text or ED legends. SLC24A5 rise attributed "mostly" to migration. |
| Mathieson 2015 / Fu 2015 / Mallick 2024 | 1240k panel design (C1) | verified | Targets array SNPs (Human Origins, 610-Quad) plus functional SNPs, i.e. ascertained on present-day variation. Supports the C1 check premise. |
| Wistar 1967 | Eden 10^325 vs 10^52 (Day) | verified-accurate | p.7. Ulam (pp.21–22) says the random-construction framing "is not the problem at all". Wright (p.118) rebuts. Schützenberger argues a "gap", not a probability. |
| "Weasel 540,000 gens" | (Day) | n/a | Day's own calculation (blog 2026-09-12), not from Wistar. |
| Axe 2004 | 1 in 10^77 functional | verified-accurate (abstract) | One β-lactamase domain, extrapolated. Counter-estimates (Taylor 2001, Keefe & Szostak 2001) are abstract-only and not directly comparable. |
| Frankham 1995, Maruyama 1970/74, Cannings 1974, Crow & Kimura 1970, Kimura 1983, ReMine 2005, Wright Nₑ | various | unverified | Record only. |

## Retrieval blocked — manual browser download requested from the user
Kimura 1962; Kimura & Ohta 1969; Keightley 2012; Haak 2015; Prado-Martinez 2013; Taylor 2001.

All are free on PMC, but its bot challenge blocked automated download. We did not try to get around the challenge.
