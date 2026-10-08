---
id: B5c
title: "Hancock: ~76.8 new mutations fixed per generation, ~38 million over 2 × 252,000 generations"
side: critic
branch: B
parent: B5
edges: [{type: attacks, target: B1}, {type: attacks, target: B3a}, {type: attacks, target: A}]
load_bearing: false  # null-model comparison; its haploid/diploid basis halves the headline match
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> that's about 76.8 uh new mutations that are fixed in the population every single generation.

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:51:04

> use 6.4. This is the diploid genome size for the fixation rate because you fix on a hloid genome. So, it should be 3.2 e to the 9.

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:52:48 (in-video correction, preceded by "we can't" at the end of the 01:52:27 chunk; "hloid" = haploid in the auto-caption)

> Um so that's 152 on average. If we divide that in half to take the

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:53:10 (continues in the 01:53:30 chunk: "the hloid genome size that gives us 76.")

> we'll say about 38 million.

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:56:15

## Formal statement
**Arithmetic audit (derived, python3 -I):** 6.4e9 × 1.2e-8 = 76.8 ✓ (diploid bases, the first-pass figure). Haploid: 3.2e9 × 1.2e-8 = 38.4 per generation per lineage. 2 lineages × 252,000 × 76.8 = 38.7M (the quoted "about 38 million"); with 38.4: 19.35M. The first-pass 76.8 used the diploid genome (self-corrected on screen at t=01:52:48). The retained 76 is a different quantity: a cited de novo count of 98–206 per generation (mean 152, including structural variants), halved to the haploid genome: 152/2 = 76 ✓ (derived), then 76 × 2 × 252,000 = 38.3M. That is a count of mutation *events* of all types, so the matching comparator is the CSAC event total (35M SNV + 5M indel events ≈ 40M, derived), not the SNV count alone.
Comparators for the SNV-only haploid version (38.4 per generation): 19.35M vs the CSAC ~35M SNV total (includes polymorphism): ratio 0.55, i.e. 1.8× short (the repo's balance ledger records a ~1.8× doubling in Hancock's headline); vs fixed-only 0.78–0.86 × 35M = 27.3–30.1M: 1.4–1.6× short (derived). Including ancestral coalescence (B4a) with Nₑ,anc = 1.32×10⁵ adds 20.3M (θ = 6.3e-3 × 3.2e9), taking 19.35M to 39.6M.
205M check: Hancock states the number as 205 million and divides to get "something like 407" per generation: 205e6/(2 × 252,000) = 406.7 (derived ✓). Day's 205M is already per human lineage (Q15: "205 million required fixations on the human lineage"), which would give 813/generation (derived), i.e. 10.6× the 76.8 or 21× the 38.4; Hancock's "~5×" is therefore low by 2× if 205M is per lineage.

## Assumptions
- Stated: Neutral substitution rate = mutation rate; both lineages fix at the same rate; self-described as a back-of-the-napkin calculation (GG-16).
- Implicit: All 3.2 Gb are neutral (upper bound); mutation rate 1.2e-8 per bp for the first pass; the final 76 counts events including structural variants, and a structural event fixes as one event, not as many base pairs (consistent with the events-vs-bp point against Day's 205M, A3x); the 205M comparison treats events and bases alike (see below).

## Responses
- Against: Day (CLUE 2026-09-22) replying to a similar message: "confused mutations with fixations" (see B5d).
- In support: Match to the 35M SNV order after the factor-2 correction is partial: ≈ 19M vs 35M.
- Weaknesses in the responses: Auto-captions garble names and figures (the cited paper is rendered "perky at all 2025"). The first-pass diploid basis was a factor-2 slip, corrected on screen. The SNV-only haploid version gives ≈19M, so the match-to-35–40M statement depends on counting SV events in the supply but comparing to a SNV-dominated total.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kong 2012 | μ = 1.20×10⁻⁸ per nucleotide per generation | verified |
| Chimpanzee Sequencing and Analysis Consortium 2005 | "The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species." | verified (ledger) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: Neutral expectation ≈ the 35–40M observed SNVs.
- Under the opposing model: (Day) pipeline not full (B1c); a factor ~2 gap remains after haploid correction.
- Result that would change a verdict: B4a (ancestral term) and B1c.

## Check
Script: none (arithmetic computed with python3 -I). Related: B5.

## Simulator variables implied
- haploid vs diploid genome basis
- μ
- L neutral fraction
- lineages counted
