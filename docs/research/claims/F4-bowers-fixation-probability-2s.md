---
id: F4
title: "Bowers (via Day's repost): the correct approximation for a beneficial mutation is roughly 2s, not 1/N"
side: critic
branch: F
parent: F
edges: [{type: attacks, target: F}]  # judgement (kept): the reposted review names no Day equation; F is the node where Day uses 1/(2N) and fixation times
load_bearing: false  # correct textbook statement; no calculation in the review, and Day's use is of rates (F4a)
sourcing: secondhand
status: extracted
verdicts:
  internal: holds
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> The correct approximation for a beneficial mutation is roughly 2s (in diploids under weak selection), not 1/N.

Source: [Bowers review as reposted by Day, "A Critical Review of Probability Zero"](https://voxday.net/2026/03/04/a-critical-review-of-probability-zero/), 2026-03-04, para 3. **secondhand** (Bowers's seven-point review as reposted by Day; the original was not found)

## Formal statement
u ≈ 2s (Haldane 1927/Kimura 1962), so per-generation adaptive substitution rate k_ben = 2N·U_b·2s = 4N s U_b. B0.3 check: Kimura u at N=100, s=0.01: sim 0.019995 vs 0.020171 (z = −0.56); N=500: 0.019745 vs 0.019801; N=1000, s=0.005: 0.010225 vs 0.009950 (z = +1.22).

## Assumptions
- Stated: Fixation probability of a beneficial mutation under weak selection ≈ 2s.
- Implicit: Large N, additive.

## Responses
- Against: Day (F4a): confusion of probability with rate.
- In support: Kimura 1962; RESULTS B0.3.
- Weaknesses in the responses: Known only through Day's repost; contains no calculation (Day's reply is accurate on that).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | "the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient" | verified-accurate |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B0.3; the check has run).
- Under the claimant's model: u ≈ 2s.
- Under the opposing model: n/a
- Result that would change a verdict: n/a

## Check
Script: `research/checks/baseline_textbook.py` (seed 20261007) · Result: B0.3 all pass (z = −0.56, −0.18, +1.22).

## Simulator variables implied
- s
- N
- dominance
