---
id: G2f
title: "Bowers (as reposted by Day): treating evolution like a serial lottery is a category error"
side: critic
branch: G
parent: G2
edges: [{type: attacks, target: Ga}]  # was attacks G3 (a critic node making the same point). Judgement (2026-10-08): the 'serial lottery' is Day's product-of-probabilities step, Ga
load_bearing: false
sourcing: secondhand
status: extracted
verdicts:
  internal: holds   # against the Dec 2025 abstract / Appendix A serial chain only, within this model (soft, multiplicative, free recombination); not applicable to G_f arithmetic (G1)
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> Treating it like a serial lottery is a category error.

Source: [Day repost of Bowers review, "A Critical Review of Probability Zero"](https://voxday.net/2026/03/04/a-critical-review-of-probability-zero/), 2026-03-04, para 4 (BO-02). Bowers' words, secondhand through Day's repost.

## Formal statement
Qualitative (no numbers). Day's point-by-point reply (same page): "Point 2 claims I model beneficial mutations as neutral drift events with fixation probability 1/N … The reviewer has confused fixation probability with fixation rate." and "Point 3 invokes recombination as a rescue. The Bernoulli Barrier paper addresses this directly and at length."

## Assumptions
- Stated: events are not independent serial draws.
- Implicit: Day multiplies per-event probabilities (Ga).

## Responses
- Against (Day): the reply above; BO-04: "Not a single calculation." (accurate: the seven points contain no numbers).
- In support: Ga multiplies p^n for a pre-specified set.
- Weaknesses in the responses: the Bowers text is quoted only as reposted; the review contains no arithmetic; Day's reply cites Kimura & Ohta 1969 for recombination independence (A5f: misattribution).

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No prediction.

## Check
No script.

R4 G1 (research/checks/results/R4-G1.md): p^n is timing-independent, so a serial reading adds nothing to the Bernoulli arithmetic; the critique lands on the Appendix A chain (G2g), not on G_f (G1). Bowers's specific-targets thesis is credited (G3). Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- None.
