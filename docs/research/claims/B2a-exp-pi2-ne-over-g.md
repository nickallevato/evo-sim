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


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
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

R4 XT (research/checks/results/R4-XT.md; combined review, 2026-10-09): independent-engine replication in fwdpy11 0.24.7. Reproduced: Kimura u(s,N) within 2%, beneficial t_fix 0.7-1% from the diffusion integral and 2-3x below (2/s)ln2N, exact-chain F_cond within 1.5%, P_fix = 1/2N and time scaling with Ne (not Day N/Ne), the B1c excess 3.8-3.9. NOT reproduced numerically, not localised: B1 counts (21% equilibrium deficit), B1b expansion (0.699 vs 0.733), B3b non-overlapping k/U (0.95-0.96), B3c(e) cohort (0.64, constant in cohort size). The deficit tracks per-gamete U in the runs (hypothesis, untested). Numpy numbers neither overturned nor independently confirmed at the failing rows; no verdict change.

R4 B2f (`research/checks/results/R4-B2f.md`; `b2f_finite_time_formula.py` pre-registered 4213c5e, label criterion-only; combined review #82 `REVIEW-R4-B2f-combined.md`; fix pass de3c1a2; integrated 2026-10-13; low-stakes tier): on 2026-10-13 Day and Athos restated this law in their other paper (Zenodo 22903977, retitled "k ≠ μ: The Finite-Time Collapse of Neutral Substitution Theory", file replaced) as "the closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T)" (Q286), citing this paper: "=" for "∼", "closed-form" added, the domain T ≪ 4Nₑ dropped. This file's Statement (Hard Limits, record unchanged on 2026-10-13) keeps "∼" and "T ≪ 4Nₑ"; **no field here changes** and no new node was made, since a node for the restatement would count this law twice. The readings of the restatement are on B1e (reading-dependent: as a relay of this asymptote `holds`; as a literal equality `non-sequitur` on that paper's own quantities). **Exact prefactor, closing R4 B2's "roughly (Nₑ/T)^1.5":** with x = T/Nₑ the exact conditional law is F(x) = (4π/x)^(3/2) e^(x/16) Σₙ (−1)ⁿ(2n+1) exp(−π²(2n+1)²/x) (the Kimura 1955 series resummed by the Jacobi identity; the two series agree to 3e-14 in the script and to 6e-40 or better post hoc at 120 digits). **For Day:** the exponent is exact in the short-time limit (local exponent π² − 1.5x + x²/16: 9.795, 9.499, 8.432 at x = 0.05, 0.25, 1); the derivation route the new text describes is real (the arcsine coordinate is this paper's own transform, Q295 and R4 P1; the leading term of the resummed eigen-expansion carries exactly this exponent and equals the exact F to 1 part in 10⁸ for T ≤ 4Nₑ), with one wrong word, "eigenvalue" (ledger S-B2f-2); in the stated domain the prefactor does not move the conclusion (at x = 0.25: 2.6e-15 exact against 7.2e-18); the other paper's 15.9% count loss at Nₑ = 10,000 is the exact value (15.87%). **For critics:** as an equality the formula understates F at every T, by (4πNₑ/T)^(3/2) e^(T/16Nₑ) in the limit (3,997x at x = 0.05, 47.4x at 1, 17.8x at 2, 7.15x at 4, 1.48x at 25.2); at the other paper's own inputs (x = 25.2, 5.04, 4.0) it gives 0.676, 0.141, 0.085 against the exact 0.99999, 0.761, 0.606 (audit substitutions; Day prints none of them), and on the ratio convention it is within 25% only for T ≥ 44.2 Nₑ (34.3 Nₑ on the (F − C)/F convention), where F is 1 to eight decimal places; the dominant eigenvalue gives the opposite, long-time law 1 − F ≈ 3 exp(−T/2Nₑ); from a stationary start the flux is exactly μ at every T. Ledger S-B2-1 ("order-one" prefactor) now has its exact size.
