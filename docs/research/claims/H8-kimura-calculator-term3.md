---
id: H8
title: "Kimura's Fixation Calculator: k_real = min(input flux, polymorphism ceiling, selection-cost ceiling), with Term 3 k_sel = s_max d / [2 L ln(2Ne)] and s_max ≈ 1 binding for every sexual eukaryote"
side: day
branch: H
parent: H
edges: [{type: supports, target: H}, {type: depends-on, target: C2}, {type: depends-on, target: B3}]
load_bearing: true  # Source of the "k = mu N/Ne" and cost-ceiling predictions and of the 10^-12 adaptive limit that survives the retraction (H1). Its Term 3 uses d and s_max; its numbers disagree with Haldane + d (H).
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # arithmetic
  fidelity: pending
  external: "contested"   # 17.1x Haldane + d on the same basis. R4 H3: the R = 2 form matched in a 10k window (if R = 2 is intended; s_max*d = ln R is the audit mapping), overshoots the long-run cap over 252k; R-independence not claimed by Day
---

## Statement (verbatim)
> "Selection cannot operate without reproductive differential, and the differential available to any individual is bounded by what the organism can physically achieve."

Source: [Kimura's Fixation Calculator](https://zenodo.org/records/19984826), Z19984826, 2026-05-02, §3.3 "Selection-Limited Rate".

> "ksel = smax · d / [2L · ln(2Nₑ)] = 1 · 0.45 / [2 · 3.1 × 10⁹ · ln(6,600)] = 0.45 / [2 · 3.1 × 10⁹ · 8.79] ≈ 8.3 × 10⁻¹²"

Source: Z19984826, §4.3 (human worked case, Ne = 3,300).

> "None of them raises smax above order unity, and the reason is the same in all three cases."

Source: Z19984826, §3.3.1 (truncation selection, soft selection, composite fitness).

> "The defense is partially correct and entirely fails to deliver k = μ."

Source: Z19984826, §6.4 (reply to "most substitutions are neutral, so Term 3 does not apply").

## Formal statement
n_max = s_max / s̄ concurrent sweeps (sum of s_i <= s_max); each sweep takes tau = (2/(s̄ d)) ln(2Ne) generations (Charlesworth 1994 for the diploid overlapping-generations form, per the paper); K_sel = n_max/tau = s_max d / [2 ln(2Ne)]; per site k_sel = K_sel / L. Human case (§4.3): N ~ 10^8, Ne = 3,300 (attributed to Day & Athos 2026a, the drift-variance paper, Z18320599), N/Ne about 3e4, d = 0.45, L = 3.1e9, s_max = 1. Z18320599 contains no absolute Ne of 3,300 (searched: 0 occurrences) and says its absolute Ne values (0.3 to 1.4) "are not interpretable as true effective population sizes" (C4). The source of 3,300 is therefore unlocated in the corpus.

derived (R2 recompute):
- 0.45/(2 x 3.1e9 x ln 6,600) = 8.25e-12 (paper 8.3e-12; holds). K_sel = 8.25e-12 x 3.1e9 = 0.0256 per generation = one adaptive substitution per 39 generations.
- Over 260,000 generations: 6,650 adaptive substitutions. Required 17.5M / 6,650 = 2,630 (paper: 2,700x at 6.5 MYA; holds within rounding).
- Same formula with Ne = 1e4 (parameters.yaml `population.Ne_modern_human`): 7.3e-12 per site, one per 44 generations.
- Haldane + d (H): one per 300 generations, i.e. 487 in 146,250 effective generations. Term 3 (1/39 per nominal generation, d included) therefore allows about 17.1 times more adaptive substitutions per generation than Haldane + d (0.45/300 = 1/667 per nominal generation). The earlier 7.7 (300/39) mixed bases (Term 3 with d over Haldane without d) and is withdrawn; without d on both sides the ratio is also 17.1 (10x from the budget, 1.7x from D). The corpus contains two cost-based figures for the same species, 300 and 39 generations per substitution, which the papers do not reconcile.
- The formula's structure: Ne appears only through ln(2Ne); the s̄ cancels; d multiplies; "s_max ≈ 1" is the single input standing in for Haldane's 10% mortality (s_max = 0.1 would give 390 generations per substitution at d = 0.45, close to 300; derived).
- Term 2 (§6.4): k_cap = pi_max/(4 Ne) = 1e-3/(4 x 3,300) = 7.6e-8; human required k at 6.5 MYA = 2.2e-8 (17.5M/(3.1e9 x 260,000) = 2.17e-8; holds), "six-fold shortfall" refers to 4.7e-7 at the 300 kya date (the paper's own recalibration).

## Assumptions
- Stated: Σ s_i <= s_max ≈ 1; the maximum differential is "the highest-fitness individual leaves twice as many descendants as the average"; truncation, soft selection and multiplicative fitness only redistribute the budget.
- Implicit: that s_max = 1 is a property of the population mean (Nunney's simulation shows the cost depends on M and on hard versus soft selection); that Haldane's death-count and a sum of s_i are the same budget; that d (a rescaling of time, C2) enters inside the cost bound; that "most substitutions are neutral" is downstream of k = mu.

## Responses
- Against: Nunney 2003 (H2): soft selection "inevitably reduces or eliminates the cost" and the cost is "substantially less" for M > 1/2; Keightley 2012 (H7). Day's own 2026-05-07 retraction (H1): Term 3 is a bound on adaptive substitutions only, not total k, "a category error".
- In support: Hössjer (H5), Nesslig20 on scope (H6).
- Weaknesses in the responses: no critic engaged the formula or the s_max ≈ 1 argument; Day's reply to soft selection (§3.3.1) does not cite Nunney; the retraction has no revised Zenodo version.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1957 | via Nunney: "a typical allelic substitution required about 30N genetic deaths" | accurate secondary; the paper's use of the "reproductive ledger" and s_max = 1 is not Haldane's 10% mortality number |
| Wallace 1975 (soft selection); Maynard Smith 1968 (truncation); Crow & Kimura 1970 (composite fitness) | cited at §3.3.1 | not retrieved; unverified |
| Charlesworth 1994 | the diploid overlapping-generations sweep time | not retrieved; unverified |
| Lynch 2010; Lynch et al. 2016 (drift barrier) | cited | not retrieved |
| Frankham 1995 | Ne/N about 0.1 | `population.Ne_over_N` unverified |

## Pre-registered prediction
- Under the claimant's model: in a forward simulation of sexual diploids with hard selection and R = 2, the sustainable genome-wide adaptive substitution rate is s_max d/(2 ln 2Ne) = 0.0256 per generation (Ne = 3,300, d = 0.45).
- Under the opposing model (Haldane; Nunney): the hard-selection rate depends on M and on R; at small M it is near 1/300 per generation; the Term 3 value 1/39 is a factor 17.1 higher on a same-basis comparison (1/39 vs 1/667), and under soft selection there is no ceiling of this form.
- Result that would change a verdict: the H simulation giving a sustainable rate in agreement with either figure under stated M, R, K.

## Check
R4 H (research/checks/results/R4-H-C2.md): 0.45/(2 x 3.1e9 x ln 6,600) = 8.25e-12 per site (holds); 0.0256 per generation (one per 39). Implied per-substitution cost 2 ln(2Ne) = 17.6 against s_max = 1.0, vs Haldane's D = 30 and 0.10; same-basis ratio to Haldane + d is 17.1. In H2's hard model the cap is ln R / D, so s_max = 1 corresponds to a large reproductive excess (ln R = 1, R ~ 2.7), not Haldane's 10%. The two cost figures in the corpus are not reconciled. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: `research/checks/h_cost_of_selection.py` (planned, H). · Result: not run · Review: pending

R4 H3 (research/checks/results/R4-H3-human.md): Term 3's 0.0296 per generation at R = 2 matched the pre-registered form in a 10k window (lambda50 = 0.0345 [0.0330, 0.0368]) if R = 2 is the intended value; at the R implied by the audit's s_max*d = ln R mapping (1.57) it fails (lambda50 ~ 0.020). Over 252k it is above the long-run cap (phi_252k = 0.59 at R = 2). The R-independence tested as D2 was not claimed by Day; it holds only if s_max = 1 is read as a constant. Review: `research/checks/REVIEW.md` (review #7, 2026-10-09).

## Simulator variables implied
s_max (or R), d, Ne, L, concurrent-sweep count, hard/soft switch.
