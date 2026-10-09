---
id: G4
title: "Darwillion: the reciprocal of the probability of the pre-specified fixations; Day: \"nothing more than a rhetorical absurdity\""
side: day
branch: G
parent: G
edges: [{type: depends-on, target: Ga}]
load_bearing: false
sourcing: secondhand
status: checked
verdicts:
  internal: holds
  fidelity: n/a
  external: n/a
---

## Statement (verbatim)
> the Darwillion is nothing more than a rhetorical absurdity to demonstrate how far off the biologists are from the mathematical realities of the situation.

Source: [The Math is Too Hard](https://voxday.net/2026/09/17/the-math-is-too-hard/) (key B2026-09-17), blog, 2026-09-17, ¶8.

> What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations

Source: [Do Try to Keep Up, Dennis](https://voxday.net/2026/09/11/do-try-to-keep-up-dennis/) (key B2026-09-11), blog, 2026-09-11, ¶5. Secondhand: McCarthy's rendering of Day's book calculation, exponent flattened; Day's own formula is in the paywalled book and was not checked.

## Formal statement
Darwillion := 1/P, P = (1/20,000)^(20,000,000) per McCarthy's rendering (sourcing: secondhand). Day, firsthand (2026-01-27 ¶3): "my probability calculation about the likelihood of evolution by natural selection"; a reviewer quoted by Day (2026-01-12 ¶6, secondhand) calls it "the reciprocal of the non-existent odds of TENS accounting for the origins of just two species".
`derived:` (python3 -I) log10 P = 2e7 x log10(1/20,000) = −86,020,600, so the Darwillion ≈ 10^86,020,600. For comparison Ga: 0.02^(2e7) = 10^−33,979,400. The Hard Limits abstract (Q30, branch B2) gives a third number, "about one in ten to the seventy-eight-millionth"; no corpus text derives the Darwillion from either.
Other headline numbers from this family audited: Day's "87,916,307x" (Q51): 642,888/146,250 = 4.3958; x 20,000,000 = 87,916,308 (rounded; reconciles). 642,888 = 2 x 321,444 (Dawkins's recessive figure); 146,250 is the 2025 effective generation count (A4).

## Assumptions
- Stated by Day: the Darwillion is rhetorical, not a model of what happened.
- Implicit: p = 1/20,000 is the per-mutation fixation probability (neutral, 1/2N, with N = 10,000) used with n = 20M.

## Responses
- Against: McCarthy (G3): it prices a specific list. Day agrees it is rhetorical (G4 statement), which concedes the interpretation but not the numbers.
- In support: Day (2026-01-27 ¶14–15): McCarthy used the same 1/20,000.
- Weaknesses in the responses: Day describes it both as "my probability calculation about the likelihood of evolution by natural selection" (2026-01-27) and as "a rhetorical absurdity" (2026-09-17); Day's own p differs between uses (0.02 in Ga, 1/20,000 here).

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No prediction.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 G1 (research/checks/results/R4-G1.md): the book's own preceding step (secondhand) is an "any" comparison: 1 in 22,727 required against 1 in 20,000. Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- None.
