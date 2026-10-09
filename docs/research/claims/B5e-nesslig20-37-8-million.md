---
id: B5e
title: "Nesslig20: mu_G = 75 per generation, k = 75, 2 × 75 × 252,000 = ~37.8 million fixed neutral mutations"
side: critic
branch: B
parent: B5
edges: [{type: attacks, target: B1}, {type: attacks, target: B3a}]
load_bearing: false  # null-model comparison; its basis halves the headline match
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # arithmetic 2 x 75 x 252,000 = 37.8M
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: "contested"   # basis unstated; on a haploid SNV basis 18.9M + ancestral ~15M
---

## Statement (verbatim)
> Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]. That means [ k = 75 ] mutations will fix per generation.

Source: [Nesslig20, "Response to Will Duffy | PART I - Population Genetics" (Peaceful Science)](https://discourse.peacefulscience.org/t/18094), 2026-10-05, post 1 by Nesslig20, §2.2

> So, the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million based on this rough calculation.

Source: [Nesslig20, "Response to Will Duffy | PART I - Population Genetics" (Peaceful Science)](https://discourse.peacefulscience.org/t/18094), 2026-10-05, post 1 by Nesslig20, §2.2

## Formal statement
**Arithmetic audit (derived, python3 -I):** 2 × 75 × (6.3e6/25 = 252,000) = 37.8M ✓. The post defines μ_G via "the neutral mutation rate per haploid genome per generation" (§2.1) and then writes: "Estimates vary from 100 to 200 per generation. Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]." The basis of 75 is not stated: if it is a zygote-level count, the haploid value is 37.5 and 2 × 37.5 × 252,000 = 18.9M (derived), about 0.54 of the 35M SNV total (the balance ledger flags this factor of 2); if it is a halved 100–200 range, the product stands as written. The harvest note read it as the first case; the text does not settle it. The post uses P_fix = 1/(2Nₑ) and supply 2Nₑ μ_G in the same expression, so the cancellation is internally consistent.
Reference-genome note (Nesslig20): "since they use one (or a few) reference genomes, not all of the differences they identified between genomes are actually fixed" — the same polymorphism caveat as CSAC (14–22%).

## Assumptions
- Stated: Neutral drift at k = μ_G; both lineages; 6.3 My, 25 y.
- Implicit: 75 is a haploid-genome count (unstated derivation); no neutral-fraction constraint; full pipe.

## Responses
- Against: Possible factor-2 basis question (balance ledger; text does not settle it).
- In support: Order-of-magnitude agreement with 31–62M SNVs (1–2%).
- Weaknesses in the responses: a rough calculation by the author's own words; the 1–2% range is wide.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Chimpanzee Sequencing and Analysis Consortium 2005 | polymorphism accounts for 14–22% of observed divergence | verified (ledger) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: ~37.8M neutral fixed differences.
- Under the opposing model: (if 75 is zygote-level) ~18.9M; ratio to 35M ≈ 0.54.
- Result that would change a verdict: B4a.

## Check
Script: none (arithmetic computed with python3 -I).

R4 B4a (research/checks/results/R4-B1c-B4a.md; REVIEW-R4-steelman-critic): if mu_G = 75 is a zygote-level count, the haploid value gives 18.9M (= 2muT, B4a), and the observed ~35M is ~19M post-split plus ~15M ancestral polymorphism, so the 37.8M match would be a double count (same issue as B5c). The post does not state the basis. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / unverifiable. N3 (revised): stated conclusion 'close to 31-62M'; with the ancestral term 58.1M (HCG, inside) or 68.2M (HCB, +10% over the top, under 25%): survives; 75 non-standard and uncited (F) Charitable reading tried: tried the haploid-events reading of 75 (stated per haploid genome).

## Simulator variables implied
- haploid vs diploid basis
- neutral fraction
