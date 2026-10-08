---
id: F3
title: "t ≈ (2/s) ln(2Ne) for a beneficial allele (called \"Kimura's equation\")"
side: day
branch: F
parent: F
edges: [{type: supports, target: F}, {type: depends-on, target: F3a}]
load_bearing: false  # used in the Q&A (19,800) and "six/seven fixations"; the throughput question dominates (F1)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶6 of extracted text

> Time to fixation calculated using t ≈ (2/s_eff) × ln(2N_e) for N_e = 10,000, from initial frequency p = 0.01 to p = 0.99.

Source: [Z18166426 (Day & Athos)](https://zenodo.org/records/18166426), Zenodo 2025-12-25 (record modified 2026-01-06), ¶135 of extracted text

## Formal statement
Deterministic logistic sweep: time from p₀ to 1 − p₀ at selection s (per Day's parametrisation) is (2/s) ln((1−p₀)/p₀) ≈ (2/s) ln(2Nₑ) when p₀ = 1/(2Nₑ). The stochastic conditional mean time is (2/s)(ln(4Ns) + γ) (RESULTS review #2 correction). Derived (python3 -I) at N = 10⁴: s = 0.001: (2/s)ln(2N) = 19,807 vs (2/s)(ln 4Ns + γ) = 8,532; s = 0.01: 1,981 vs 1,314; s = 0.0005: 39,614 vs 14,292.
Zenodo calculator Z19984826 writes the selected-sweep time as (2/(s̄·d)) ln(2Nₑ) and cites Charlesworth 1994 for it; the blog attributes the formula to Kimura.

## Assumptions
- Stated: Kimura; Nₑ = 10⁴; s = 0.001 (F3a).
- Implicit: Deterministic path from 1/(2Nₑ) (or 0.01) to near fixation; unconditional on loss; the 0.01→0.99 version in Z18166426 omits the stochastic early phase.

## Responses
- Against: RESULTS B0.4: overshoot 1.6–2.2× at tested points, ≈2.3× at Day's parameters.
- In support: RESULTS B0.4: (2/s)ln(2N) is a standard deterministic sweep-time approximation, used legitimately as such.
- Weaknesses in the responses: Attribution to Kimura is not supported by Kimura & Ohta 1969 (4Nₑ only) in this corpus; Z19984826 cites Charlesworth 1994. The overshoot concerns the conditional mean latency, which is not the quantity that sets throughput (F1).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Charlesworth 1994 (cited in Z19984826) | sweep time (2/(s̄ d)) ln(2Nₑ) | not retrieved; unverified |
| Kimura & Ohta 1969 | 4Nₑ (neutral); selected cases presented numerically in the paper | accurate for 4Nₑ |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B0.4; the check has run).
- Under the claimant's model: (Day) t ≈ (2/s) ln(2Nₑ).
- Under the opposing model: Simulated t_fix ≈ the Kimura–Ohta diffusion integral (tolerance 5%); (2/s)ln(2N) overshoots both.
- Result that would change a verdict: n/a (done).

## Check
Script: `research/checks/beneficial_fix_time.py` (seed 7) · Result: confirmed. N = 500, s = 0.01: sim 698±3, diffusion 703, (2/s)ln2N 1382, (2/s)(ln4Ns+γ) 715; N = 1000, s = 0.005: 1405±9 / 1407 / 3040 / 1429; N = 2500, s = 0.01: 1043±6 / 1033 / 1703 / 1036; N = 5000, s = 0.01: 1177±7 / 1173 / 1842 / 1175; N = 10⁴, s = 0.001: diffusion 8,480, (2/s)ln2N 19,807, corrected asymptote 8,532. Review #2: asymptote corrected from ln(2Ns) to ln(4Ns). Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

## Simulator variables implied
- s
- N, Nₑ
- p₀ (1/2N or 0.01)
- deterministic vs conditional mean time
