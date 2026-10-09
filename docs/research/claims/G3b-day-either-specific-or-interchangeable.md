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
  external: contested
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
No script.

R4 G1 (research/checks/results/R4-G1.md): the dilemma omits the middle case. Assumptions favour the interchangeable case; per-site m is not established (branch D prevalences are per sequence and not convertible). Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- Functional fraction f of divergence as an input.
