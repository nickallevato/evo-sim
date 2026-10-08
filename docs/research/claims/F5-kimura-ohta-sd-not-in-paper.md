---
id: F5
title: "Mean 4Ne with SD ≈ 0.538 × 4Ne \"under Kimura's diffusion treatment\""
side: day
branch: F
parent: F
edges: [{type: supports, target: B1a}]
load_bearing: false  # the SD is used to describe the breadth of the fixation-time distribution; the E[F(T)] formula needs only the mean
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: unverifiable
  external: n/a
---

## Statement (verbatim)
> a broad distribution around that mean (SD ≈ 0.538 × 4Nₑ under Kimura's diffusion treatment)

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §3 The Empty Pipe

## Formal statement
0.538 × 4 = 2.152, i.e. SD ≈ 2.15 Nₑ. Our simulation (RESULTS B0.2): SD of t_fix/N = 2.105 (N=50) and 2.108 (N=200) vs diffusion ≈ 2.15 (derived consistency). The figure is not in Kimura & Ohta 1969, which derives the first moment and says higher moments can be obtained step by step (fidelity ledger).

## Assumptions
- Stated: Kimura's diffusion treatment gives SD ≈ 0.538 × 4Nₑ.
- Implicit: Conditional on fixation, p₀ → 0.

## Responses
- Against: n/a
- In support: RESULTS B0.2.
- Weaknesses in the responses: Fidelity: the attribution is to a later or derived source; the paper contains the first moment (Eq. 15) only.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | Eq. 15: t̄(0) = 4Nₑ; no SD | not-found in this paper (ledger) |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: SD ≈ 2.15Nₑ.
- Under the opposing model: n/a
- Result that would change a verdict: n/a

## Check
Script: `research/checks/baseline_textbook.py` · Result: SD 2.105, 2.108 vs ≈2.15 (diffusion). Review #2 corrected the mean target.

## Simulator variables implied
- fixation-time SD display
