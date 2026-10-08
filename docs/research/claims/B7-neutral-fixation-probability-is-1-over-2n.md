---
id: B7
title: "Neutral fixation probability is 1/(2N), the starting frequency, not 1/(2Ne); Day's own Hard Limits paper says so"
side: critic
branch: B
parent: B3
edges: [{type: attacks, target: B3a}, {type: supports, target: B5}]
load_bearing: true  # decisive for the N/Nₑ leg of B3 and for B4's recalibration
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> Maruyama’s invariance principle (1970, 1974) holds that under conservative migration the neutral substitution rate is exactly μ and the neutral fixation probability exactly 1/(2N)

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Third Objection (Day's own paper, 2026-08-27)

> Every neutral mutation begins as a single copy in a single individual, at a frequency of 1/(2N).

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Transit Time

> Yes, and that’s the problem. 1/2N is the fixation probability. It tells you the chance that a given neutral mutation will eventually fix, given unlimited time.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶6 of extracted text

## Formal statement
P_fix(neutral) = p₀ = 1/(2N) where p₀ is the starting frequency of the new copy (martingale/optional stopping: E[Δp] = 0 and absorption ⇒ P(fix) = p₀). Nₑ sets the timescale (4Nₑ), not the probability. This is the glossary's pinned definition.
Day's three statements of 1/(2N) in 2026 (above) sit alongside the 1/(2Nₑ) in Z18429937, Z18525547, Z18637333 and the 2026-02-04 post (B3a). Day withdrew the latter on 2026-08-27 (B3g).

## Assumptions
- Stated: Day's own text.
- Implicit: Single-copy start; exchangeable offspring distribution (B3 check; non-exchangeable settings pending B3b).

## Responses
- Against: Day's earlier position (B3a); Day (RESP) contests keruru's chains as setting covariance between who breeds and what they carry to zero (B3g discussion).
- In support: B3 check; keruru's exact chains (B7c); Kimura 1962/1969 (B7a, B7b).
- Weaknesses in the responses: The Hard Limits paper still defines X using Nₑ ≈ 0.57 N while assuming 1/(2N) (B2b); the critics have not tested a non-exchangeable reproduction law (B3b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene." | verified-accurate |
| Kimura & Ohta 1969 | "the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation)" | verified |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B3; the check has run).
- Under the claimant's model: (Critic) P_fix = 1/M for every Nₑ; t_fix scales with Nₑ.
- Under the opposing model: (Day, pre-retraction) P_fix = 1/(2Nₑ).
- Result that would change a verdict: A neutral non-exchangeable model with P_fix ≠ p₀ (B3b).

## Check
Script: `research/checks/b3_N_vs_Ne.py` (seed 13) · Result: P_fix = 0.00250/0.00252/0.00257/0.00248/0.00257 vs 1/(2N) = 0.00250 for Nₑ = 200/160/100/40/19; Day's 1/(2Nₑ) would give 0.0025–0.0268. Provisional (pending B3b). Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

## Simulator variables implied
- starting-frequency definition
- Nₑ via variance
