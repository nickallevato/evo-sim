---
id: Gd
title: "Only 2% of beneficial mutations escape drift, so sustaining the pipeline requires about 7.8 million beneficial mutations to arise"
side: day
branch: G
parent: G
edges: [{type: depends-on, target: Gc}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: pending
---

## Statement (verbatim)
> Required input ≈ 230 / 0.02 ≈ 11,500 beneficial mutations per transit period

Source: [The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07), s7.9. The paper then computes "Total required input ≈ (300,000 / 440) × 11,500 ≈ 7.8 million beneficial mutations".

## Formal statement
P_escape = 2s = 0.02 (Kimura 1962). Required input per transit period = C/P_escape = 230/0.02 = 11,500; total = (300,000/440) x 11,500 = 7.84e6 (reconciles).
`derived:` population-level supply of new mutations (Day's N = 10,000; Kong rate 1.2e-8): 77 diploid per individual per generation x 10,000 = 7.7e5 per generation, 2.3e11 over 300,000 generations (McCarthy's version, MC-03: 50,000 per year x 9e6 y = 4.5e11 with Day's inputs). The 7.8e6 beneficial arisings needed would then be 3.4e-5 of all new mutations (python3 -I). Whether the beneficial fraction is that large is the open question, which the paper itself calls "an empirical question".

## Assumptions
- Stated: Kimura's 2s for each beneficial mutation; drift loss and the Barrier are independent constraints.
- Implicit: all required fixations are beneficial (not neutral); s = 0.01 for all.

## Responses
- Against: McCarthy (MC-10): "only 3% of new mutations are deleterious" (uncited); critics' neutral model needs no beneficial mutations (B-branch).
- In support: the arithmetic and Kimura 2s are accurate.
- Weaknesses in the responses: MC-10 is uncited; Day does not quantify the beneficial fraction either.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | "approximately twice the selection coefficient" | verified-accurate |

## Pre-registered prediction
Arithmetic only; supply fraction computed above. Prediction (critics): the beneficial supply needed (3.4e-5 of new mutations) is within any plausible beneficial fraction. Not tested.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 G1 (research/checks/results/R4-G1.md): this is the "any n of M" calculation; supply fraction 3.4e-5 on Gd's 2.3e11 basis (1.7e-5 on 4.5e11). Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- Beneficial-mutation fraction and s distribution as inputs.
