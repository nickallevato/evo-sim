---
id: G3b
title: "Day: either the specific fixations matter (Darwillion applies) or they are interchangeable neutral noise"
side: day
branch: G
parent: G3
edges: [{type: attacks, target: G3}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur   # incomplete dilemma: the middle case (several interchangeable routes per needed change) is unaddressed; flip at lambda_50 = 12.3-17.2; the 'neutral is not functional' half is valid
  fidelity: n/a
  external: contested   # R4 D1 measures the middle case: per-locus alternatives give lambda ~1-6 at s = 0.01 (specific horn stands at locus level); a gene-level pool of 51 beneficial SNVs (median; 0-1,760) clears the flip for k ~10 needed changes, not k >= 25, not at s = 0.001 (Table C); the within-gene beneficial fraction is 82-1,600x G1's requirement for n <= 2e5 and 8-16x for n = 2e7 at p = 0.02 (Table B)
---

## Statement (verbatim)
> There is no blunder at all. Either the specific fixations matter — in which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t explain the observed functional divergence.

Source: [The Education of a Population Geneticist](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/) (key B2026-10-01-the-education-of-a-population-geneticist), blog, 2026-10-01, ¶28. Replies to a quoted critic: "And his formula for the probability of 20 million changes is set up to calculate the probability of just one set of 20 million fixations, another colossal blunder on his part."

## Formal statement
Dilemma: (specific) → P_specific = p^n; (interchangeable) → neutral, not adaptive. No formal statement. Day (2026-01-27 ¶13): "McCarthy’s calculation is correct for the number of mutations that enter the population … He has confused mutation with fixation."

## Assumptions
- Stated: functional divergence needs specific changes.
- Implicit: a large fraction of the 20M differences are functional (not quantified); neutral drift does not count as an explanation of functional divergence.

## Responses
- Against: the horns are not exhaustive: some differences can be functional and interchangeable (many sets of beneficial mutations give similar function), which Bowers raises ("Multiple mutational paths can lead to similar phenotypes").
- In support: Day cites the Hard Limit and k ≠ μ (B2, B3) for the neutral horn.
- Weaknesses in the responses: the functional fraction is not given by Day; the "INCREASED the size of the Darwillion by a factor of 25" reply (G4b) has an unresolved formula.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No prediction.

## Check
R4 D1 (research/checks/results/R4-D1-spike.md, review #11, 2026-10-09): the open item G1 left ("per-site m is not established") is now measured. Per locus (exact RNA structure, DMS beneficial-proxy per codon): lambda ~0.1-6 at s = 0.01, below lambda_50 (7-17), so the specific horn holds at locus granularity. Per gene: a shared pool of 51 proxy-beneficial SNVs (median; 17% of datasets have none) clears the flip for about ten needed changes at s = 0.01, not for 25 or more, and not at s = 0.001 (Table C). Any-n-of-M (G3, G3a): the within-gene proxy beneficial fraction (median 3.6%, an upper bound without a noise null) exceeds G1's required fraction by 82-1,600x for n <= 2e5 and 8-16x for n = 2e7 at p = 0.02 (0.8-1.6x at p = 0.002); scaled to a 1% genome share it falls below 1 for n = 2e7 (Table B). The dilemma remains incomplete (the middle case exists at gene granularity); the 'neutral is not functional' half stays valid.

No script.

R4 G1 (research/checks/results/R4-G1.md): the dilemma omits the middle case. Assumptions favour the interchangeable case; per-site m is now measured by R4 D1 (see below) (branch D prevalences are per sequence and not convertible). Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- Functional fraction f of divergence as an input.
