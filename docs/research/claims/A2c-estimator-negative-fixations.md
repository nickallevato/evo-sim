---
id: A2c
title: "The paper's own correction gives −906 fixations for Ara-2 and Ara+5 falls from 38 to 0, so the estimator is not a count"
side: critic
branch: A
parent: A2
edges: [{type: attacks, target: A2}]  # A2c -> A2b attack removed 2026-10-08: A2b (Day, 10-02) abandons the estimator A2c criticises; no source has A2c answering A2b
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: pending
---

## Statement (verbatim)
> Their correction formula then produces minus 906 “true fixations” in Ara−2.

Source: [r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (RE-03).

> Their Ara+5 count drops from 38 such mutations at 30,000 generations to zero at 60,000.

Source: same post (RE-04).

> A count of fixed mutations cannot be negative; the negative value comes from the paper’s own correction

Source: [r/DebateEvolution, Sparky_6_4 (AI-assisted)](https://www.reddit.com/r/DebateEvolution/comments/1wxgsjm/), 2026-10-04, post 1wxgsjm (RE-10).

## Formal statement
The −906 figure appears in Z23003785 s5.2 ("Ara-2 achieved negative net fixations at 50,000 generations: −906 by clone-pair analysis") and in the s5.1 table (Ara-2: −906). Check of the quoted claim against Day's text: the figure exists, so the critic's quotation is accurate (fidelity: accurate). Day's own interpretation is population fragmentation ("The evolutionary mechanism did not accelerate. It broke."), not an estimator artefact.

`derived:` Ara-2 is a mutator; the 1,322 non-mutator headline does not include it. It enters the "all twelve populations" average (104,873-fold; 205e6/1,955 = 104,859). The Ara+5 30,000 → 60,000 drop is relevant to the non-mutator headline only if Ara+5 is in the five-population non-mutator set.

## Assumptions
- Stated: a fixation count cannot be negative, so the estimator has a failure mode.
- Implicit: that Day's correction subtracts a quantity that can exceed the observed count; that the Ara+5 count is for the same definition at both time points.

## Responses
- Against (Day): s5.2 treats the negative value as biology: hypermutation fragments the population, and "One in seven mutator populations — 14% — responded to supermutation by achieving zero fixations."
- In support (critics): RE-10 and RE-03 above; Sparky_6_4 is AI-assisted and discloses citations from memory (RE-11).
- Weaknesses in the responses: Day's interpretation is untested; a "net fixation" metric that is negative is not a count, and the critic has not shown that the non-mutator headline is affected. The Ara+5 claim is not verified here against Z23003785.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Not run. Prediction (critic): re-estimating Ara-2 and Ara+5 with a monotone fixation definition gives non-negative counts and changes the mutator averages but not the non-mutator G_f by more than 20%. Prediction (Day): the strict rule (A2b) reproduces the ordering of populations.

## Check
No script. Review: pending.

## Simulator variables implied
- None directly; informs the counting-rule toggle in A2b.
