---
id: B1e
title: "Chalub 2022 shows k = mu is an asymptote / 1/(2N) is imported from Wright-Fisher"
side: day
branch: B
parent: B1
edges: [{type: supports, target: B1}, {type: supports, target: B7}]
load_bearing: false  # cited as support, not as a step in any calculation
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: partial
  external: pending
---

## Statement (verbatim)
> Chalub (2022), solving the neutral Kimura equation explicitly in terms of Gegenbauer polynomials, derives the time-dependent fixation probability as a series of exponential decay terms that converge to the steady-state value only as t → ∞.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §1 The Identity

> Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model. It is not a result produced by the mathematics.

Source: [Day, "Chalub and the Kimura Cancellation" (blog)](https://voxday.net/2026/08/23/chalub-and-the-kimura-cancellation/), 2026-08-23, ¶5 of extracted text

## Formal statement
Chalub 2022: PDE for a two-allele neutral population "without mutation or selection", classical solution decays; two point masses at the boundaries plus integral constraints (probability conservation, conservation of mean frequency) fix the split between fixation and loss. Day's reading: the 1/(2N) is imported, not derived.

Note (derived reasoning, not a verdict): conservation of mean frequency is the definition of neutrality (equal expected offspring), so it is the neutral assumption itself rather than an extra premise. Day's point that the PDE alone does not fix the boundary split is consistent with the paper's abstract.

## Assumptions
- Stated: The diffusion machinery cannot independently confirm P_fix = p₀.
- Implicit: Chalub's model (no mutation, no selection) bears on k = μ only through P_fix and time-dependence; k also needs mutation input, which the paper does not model.

## Responses
- Against: Ledger: math correct but the paper does not address the substitution rate k. The Day post itself says Chalub "gives no sign that he is even aware that anyone is contesting neutral theory".
- In support: The literature quote below confirms the integral-constraint structure.
- Weaknesses in the responses: Day's own post also states the outcome: "Impose that assumption and the fixation probability comes out equal to the starting frequency", which agrees with the critics' P_fix = 1/(2N) at the census start (B7); the same author later conceded N/Nₑ (B3g).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Chalub 2022 | "we consider a population of two types evolving without mutation or selection, the so-called neutral evolution" | verified-partial (ledger): relevant to finite-time P_fix, not to k vs μ |
| Chalub 2022 | "Its solution is required to satisfy not only the equation but a series of conservation laws formulated as integral constraints." | accurate |
| Chalub 2022 | "Finally, the time-dependent fixation probability is given by" | finite-time P_fix is given for a stated initial condition |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: If the 1/(2N) were an assumption absent from the mathematics, exact finite chains with a different offspring law could give a different P_fix.
- Under the opposing model: Any exchangeable neutral model has P_fix = p₀ by the martingale property; exact chains give 1/(2N_census) (keruru KR-02; B3 check).
- Result that would change a verdict: A neutral, non-exchangeable model with E[Δp] = 0 but P_fix ≠ p₀ would support Day; none is in the corpus.

## Check
Script: none specific. Related: `research/checks/b3_N_vs_Ne.py` (B3).

## Simulator variables implied
- neutral model class selector (exchangeable Cannings | non-exchangeable)
