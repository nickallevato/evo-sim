---
id: B2a
title: "F(T) ~ exp(−pi^2 Ne / T) for T << 4Ne (short-time fixation tail)"
side: day
branch: B
parent: B2
edges: [{type: supports, target: B2}]
load_bearing: false  # the exponent is verified; what carries weight is which Nₑ and T are inserted (B2c) and the fill state
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: unverifiable
  external: pending
---

## Statement (verbatim)
> F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ The naive fill fraction T/4Nₑ is not just unproven; it is an overstatement, and a vast one.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.8 (§The Second Objection)

> k(T) = μ · F(T),      F(T) = P(τ ≤ T | fixation)

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection (definition; resolves the "UNVERIFIED reading" flag in RESULTS B2a: Reading 1, conditional on eventual fixation)

> The linear guess says a quarter of them should fix within a quarter of the mean time, some seven hundred fifty fixations; six do.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection (Day's own simulation)

## Formal statement
F(T) = P(τ ≤ T | eventual fixation), τ = fixation time of a new neutral mutant. Claim: ln F(T) → −π² Nₑ/T + lower-order terms.

**Derived comparison (RESULTS B2a, exact WF Markov chain, N=200):**
| G/N | exact conditional F | Day exp(−π²N/G) | exact / Day |
|---|---|---|---|
| 4 | 0.61 | 0.085 | 7× |
| 1 | 2.8e−3 | 5.2e−5 | 54× |
| 0.25 | 1.2e−14 | 7.2e−18 | 1.6e3× |
Fit (empirical, not derived): ln F_cond ≈ −π²/r + 1.5 ln(1/r) + 3.9, r = G/N, i.e. prefactor ≈ 50 r^−1.5; Day states the constant "could be wrong by two orders of magnitude in either direction without shifting the conclusion" (consistent with a ≈ 50× prefactor).
Under Reading 2 (unconditional, F/2N) the claim would be wrong in the other direction at G = 4N (0.61/400 = 1.5e−3 < 0.085); the verbatim definition above is Reading 1.
Day's simulation: 600,000 runs, 200 genes, ≈3,000 fixed, 6 within a quarter of the mean time: 6/3000 = 2.0e−3 (Poisson ±0.8e−3), vs linear 0.25 and vs exp(−π²) = 5.2e−5; the exact-chain value at G/N = 1 is 2.8e−3 (mapping of Day's "200 genes" to the script's N to be confirmed). Day's data thus sit near the exact value, ≈39× above his own formula.

## Assumptions
- Stated: Wright–Fisher diffusion; arcsine transform turns neutral drift into a symmetric random walk of length π√(2Nₑ).
- Implicit: Neutral, panmictic, constant Nₑ; τ conditional on fixation; leading-order only.

## Responses
- Against: None in the corpus addresses the exponent; the critics' objection is relevance (B2d).
- In support: Consistent with −π² (RESULTS B2a, N-convergence at fixed r, N = 100/400/1600, reproduced by `b2a_scaling.py`: −8.33/−7.40/−5.99 vs fit −8.37/−7.40/−5.97).
- Weaknesses in the responses: The harsher comparison (prefactor accuracy at G = 4Nₑ) judges an "of order" statement more strictly than its framing warrants (RESULTS fairness note). No citation is given for the diffusion result.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | first moment (4Nₑ) only; no tail law | the tail law is Day's own |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B2a; the check has run): the exponent is the correct leading-order short-time asymptotic; (G/N)·ln F_cond → −π².
- Under the claimant's model: Exponent −π² (leading order); fill fraction far below T/4Nₑ.
- Under the opposing model: (RESULTS B2a) Exponent correct but an "of order" statement; exact value is orders of magnitude larger than exp(−π²N/G) at moderate G.
- Result that would change a verdict: Pre-registered and already resolved for the exponent. The verbatim definition (Reading 1) removes the Reading-2 branch.

## Check
Script: `research/checks/b2a_hard_limits_chain.py` (exact chain, no randomness) and `research/checks/b2a_scaling.py` · Result: exponent consistent with −π² (limit order N→∞ at fixed r, then r→0; limits ≈ −8.4, −7.45, −6.0 for r = 0.25, 0.5, 1). Internal verdict: holds. Review #3 corrected the limit order. Review: `research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`

## Simulator variables implied
- G/Nₑ ratio
- exact chain vs asymptotic
- conditional vs unconditional F

R4 P1 (research/checks/results/R4-P1.md; `p1_symbolic_proofs.py` pre-registered c17b44a; na-workhorse): the arcsine transform y = arccos(1-2p) gives the neutral diffusion constant variance 1/(2N) and path length pi, so the exponent -pi^2 N/G follows (machine-proved at the transform level). Varadhan's short-time theorem is cited, not proved, and the prefactor is not proved. Verdicts unchanged (re-confirmation).
