---
id: B1a
title: "E[F(T)] ≈ muL(T − 4Ne) and its numerical application"
side: day
branch: B
parent: B1
edges: [{type: supports, target: B1}]
load_bearing: false  # B1 stands or falls on the start-state question (B1c), not on this algebra, which is exact
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> ∫₀ᵀ F_X(u) du = T − ∫₀ᵀ (1 − F_X(u)) du ≈ T − 4Nₑ

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), p.2 (§3)

> Using 252,000 generations since the split (approximately 6.3 million years at 25 years per generation) and μL ≈ 30 neutral mutations per generation: Steady-state calculation (k = μ applied naively): 30 × 252,000 = 7,560,000 fixations

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), p.3 (§4 The Numbers)

## Formal statement
E[F(T)] ≈ μL (T − 4Nₑ), valid for T ≫ E[X] = 4Nₑ.

**Arithmetic audit (derived, python3 -I):**
| Case | Day's figure | Recomputed | Note |
|---|---|---|---|
| steady state 30 × 252,000 | 7,560,000 | 7,560,000 | matches |
| Nₑ = 10⁴: 30 × (252,000 − 40,000) | 6,360,000 (loss 1.2M, 15.9%) | 6,360,000; loss 1,200,000 = 15.87% | matches |
| Nₑ = 5×10⁴: 30 × 52,000 | 1,560,000 (loss 79.4%) | 1,560,000; 6.0M/7.56M = 79.37% | matches |
| Nₑ = 63,000 (4Nₑ = T) | 0 (100%) | 0 | T = 4Nₑ is **outside** the stated regime T ≫ 4Nₑ; the exact integral is positive, so 0 is a lower bound |
| §6 prose | "reaches nearly 50% at the upper end of human estimates" | table reaches 100% | internal inconsistency of wording |
| per-lineage count vs requirement | 7.56M | 7.56M vs 17.5M SNV (Z23003785) = 2.3× short; vs 20M = 2.6×; vs 205M = 27× | the uncorrected neutral expectation is already below the SNV requirement at μL = 30 |
Relayed critic figure: see B5d (6 My ÷ 25 × 30 = 7.2M).

## Assumptions
- Stated: T ≫ E[X]; stochastic transit-time distribution with mean 4Nₑ; μL ≈ 30.
- Implicit: Empty start (B1c). μL = 30 is unsourced (pedigree-based haploid μL = 38.4, derived). F_X is the conditional-on-fixation CDF, so μL must be the destined-to-fix flux, which equals the total neutral input L μ only because 2Nμ × 1/(2N) = μ.

## Responses
- Against: Mansfield (B6/B1c) disputes the start state only; no one in the corpus disputes the algebra.
- In support: RESULTS B1: Day's U∫F_X reproduced to within SE at T = 200–2000 (N=100).
- Weaknesses in the responses: The support check cannot confirm the premise (it is constructed from it).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | mean time to fixation (conditional) = 4Nₑ; first moment only, no SD | accurate; the SD ≈ 0.538×4Nₑ in IR §3 is not in this paper (see F5) |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Simulated expected count from an empty start equals μL∫F_X, tending to μL(T−4Nₑ).
- Under the opposing model: From an equilibrium start the count is μL·T; the formula applies only to the empty case.
- Result that would change a verdict: Exact (non-asymptotic) evaluation at T = 4Nₑ would change the 63,000 row from 0 to a positive value, not the verdict.

## Check
Script: `research/checks/b1_start_state.py` · Result: see B1. Arithmetic audit above: computed with python3 -I, this session. Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

## Simulator variables implied
- Nₑ
- T
- μL
- exact vs asymptotic integral
