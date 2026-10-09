---
id: B3
title: "k differs from mu: the family of Day k/mu values (N/Ne, 0.743, 0.5, 32.3, 800,000) and their status"
side: day
branch: B
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: B3a}, {type: depends-on, target: B3b}, {type: depends-on, target: B3c}, {type: depends-on, target: B3d}]
load_bearing: true  # with B1/B2, one route to closing the neutral escape; but its N/Ne leg was withdrawn by Day on 2026-08-27 (B3g)
sourcing: firsthand
status: reviewed
verdicts:
  internal: pending
  fidelity: partial
  external: "contradicted"   # for the listed values (N/Ne, 0.743, 32.3, 800,000); the qualitative B&L effect is real but small (B3b)
---

## Statement (verbatim)
> In mammals, census populations exceed diversity-derived N_{e} by 19- to 46-fold.

Source: [Z18429937, The N != N_e Problem (Day & Athos)](https://zenodo.org/records/18429937), Zenodo 2026-01-29 (v1), ¶6 of extracted text. abstract

> Applied to four generations of human census data, it yields k = 0.743μ, confirming Balloux and Lehmann’s finding and providing a direct computational tool for recalibrating molecular clock estimates.

Source: [Z18525262, The Real Rate of Molecular Evolution (Day & Athos)](https://zenodo.org/records/18525262), Zenodo 2026-02-08 (v2; v1 Z18517618 2026-02-07 is byte-identical), ¶4 of extracted text

> comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶7 of extracted text

## Formal statement
| k/μ | Where / when | Basis | Direction (clock) | Status in this repo |
|---|---|---|---|---|
| N/Nₑ, 19–46 for mammals | Z18429937 (2026-01-29) | census vs diversity-derived Nₑ | k > μ (clock too slow, dates too old) | B3a; withdrawn by Day 2026-08-27 (B3g) |
| 30.3 / 15.2 (human), 9.1–30.3 (chimp) | Z18525547 (2026-02-08) | N = 50–100k, Nₑ = 3,300; chimp N = 300k–1M, Nₑ = 33,000 | k > μ | B4 |
| 800,000 | blog 2026-04-30 (Grok exchange) | N = 8e9, Nₑ = 1e4 | k > μ | B3f |
| 0.743 | Z18525262 (2026-02-08) | census 1950–2025, four cohorts | k < μ (dates too young) | B3c |
| ≈0.5 or less | blog 2026-02-09, ¶9 (Q42: "k in humans has been approximately 0.5μ or less throughout the entire modern period") | six-country d vs k figure | k < μ | quote verified (Q42, exact match); no claim file; the figure's derivation is not given in the post and is not re-derived here (corrected 2026-10-08 from "not verified (blog only)") |
| 32.3 | blog 2026-10-01 | Bergeron pedigree μ vs Yoo required rate; no derivation | k > μ | B3d |
| 1 (Nₑ never enters) | blog 2026-08-27 | Day's own concession | k = μ | B3g |
| median 25 over 55 vertebrates | blog 2026-05-07 | pedigree μ vs phylogenetic k; source not cited | k > μ | B3d |
The values disagree in direction (0.743, 0.5 vs ≥15) and in basis (census history, N/Nₑ, rate comparison). The version ledger records the 0.743 and 32.3 values as mutually inconsistent in direction.

## Assumptions
- Stated: k = μ fails for real populations (various mechanisms).
- Implicit: Each version assumes its own meaning of k (per generation vs per year; per site vs per genome; fixed substitutions vs observed differences).

## Responses
- Against: "Mutation supply is 2Nμ with N the census count — mutations occur in gametes, and every reproducing individual contributes gametes." ([keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 6 (keruru, retraction of the N/Nₑ leg))
  "and then what you're left with is a neutral substitution rate that's equal to the mutation rate" ([Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:48:19 (Hancock))
- In support: "we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations" ([Balloux & Lehmann 2012, Substitution rates at neutral genes depend on population size under fluctuating demography and overlapping generations, Evolution 66:605-611](https://serval.unil.ch/notice/serval:BIB_2B87D605B70D), 2012, Abstract) (partial support, B3b).
- Weaknesses in the responses: keruru is an LLM-assisted blog author who first endorsed the N/Nₑ leg; his retraction is corroborated by Day himself (B3g), which is stronger evidence than keruru alone. Hancock's derivation is stated verbally (auto-captions).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Balloux & Lehmann 2012 | N-dependence only for overlapping generations plus fluctuating N; non-overlapping: "population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations" | verified-partial (ledger); no 0.743 or 32.3 in the text |
| Kimura 1962; Kimura & Ohta 1969 | U = 1/2N for a neutral gene; fraction 1/2N reach fixation | see B7a, B7b |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: k ≠ μ in real populations by factors of 0.7 to 10⁵ depending on version.
- Under the opposing model: k = μ for any neutral model with E[Δp] = 0 and census-based supply, except in the overlapping-generations-plus-fluctuating-N setting of B&L (RESULTS B3; B3b queued).
- Result that would change a verdict: B3b result for overlapping generations with fluctuating N; the 32.3 basis (B3d).

## Check
Script: `research/checks/b3_N_vs_Ne.py` (seed 13) · see B3a. Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

R4 B3b/B3c (research/checks/results/R4-B3b-C1.md): k != mu under overlapping generations plus fluctuating N is real (B&L eq. 3 reproduced, all |z| < 1.6), but at human-like parameters it is -2% to +38% (sign upward for realistic growth). 0.743 is a window artefact whose mechanism (fixation probability 1/(2N_t)) is falsified by simulation; 32.3 has no derivation and cannot come from B&L. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- mutation-supply N (census | reproducing | user)
- fixation-probability N
- overlap (survival s)
- N(t) fluctuation schedule
- rate unit (per generation | per year | per average generation time)
