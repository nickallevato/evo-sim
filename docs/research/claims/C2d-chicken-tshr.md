---
id: C2d
title: "Chicken TSHR requires d = 1.02 (discrete generations), humans 0.45, so the cross-species validation is decisive"
side: day
branch: C
parent: C2
edges: [{type: supports, target: C2}]
load_bearing: false  # One data point supporting C2; ROOT does not use it.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> "Inverting the calculation, we find that the chicken data require d ≈ 1.02—essentially unity (Table 4)."

Source: [The Bio-Cycle Fixation Model](https://zenodo.org/records/18203514), Z18203514, 2026-01-09, §3.5, ¶112.

> "This cross-species validation is decisive."

Source: same, §3.5 (after Table 4), ¶139.

> "Loog et al. report an ancestral frequency of 0.44, with the derived allele reaching near-fixation (0.97) in modern populations over approximately 900 years (~900 chicken generations). Under the classical model (d = 1.0), this trajectory is consistent with the published selection coefficient. Under the Bio-Cycle model with d = 0.45, the predicted final frequency would be only ~0.68-0.72—inconsistent with observation by nearly 30 percentage points."

Source: same, §3.5, ¶111.

## Formal statement
Inputs (from the paper): p0 = 0.44, observed 0.97, G = 900 generations, s = 0.0049 (Loog 2017, 95% CI 0.0029-0.0088), the TSHR derived allele is recessive ("involves a recessive allele").

derived (python3, R2 recompute):
- Additive recursion p' = p + s p q/(1+sp): d = 1 gives 98.5%, d = 0.45 gives 85.0%.
- Recessive-advantage recursion p' = p + s p^2 q/(1 + s p^2): d = 1 gives 95.0%, d = 0.45 gives 70.7% (matches the paper's "0.68-0.72").
- Required d for 0.97: recessive 1.13, additive 0.84 (paper: 1.02).
- Over Loog's 95% CI for s: required d (additive) 1.43 / 0.84 / 0.47 at s = 0.0029 / 0.0049 / 0.0088; (recessive) 1.90 / 1.13 / 0.63. At the upper CI bound the chicken data are consistent with d near 0.45-0.63.
- Human loci in the same paper use the additive recursion although lactase persistence is commonly treated as dominant (outside the repo's sources).

So the chicken "d ≈ 1.02" depends on the dominance model and on where s falls inside its published interval; the interval spans the human d.

## Assumptions
- Stated: chickens have discrete, annual generations; the sweep started about 1100 AD.
- Implicit: 900 generations in 900 years (one per year); selection constant over the window; the recursion form (dominance); that a single locus can discriminate d = 0.45 from d = 1.

## Responses
- Against: none in the critic corpus.
- In support: none.
- Weaknesses in the responses: not engaged; the repo's derivation is the only scrutiny.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Loog et al. 2017 | s = 0.0049 (95% CI 0.0029-0.0088), per Day's text | not retrieved; unverified |
| Rubin et al. 2010 | TSHR sweep; 264 of 271 birds homozygous for the derived allele (per Day's text) | not retrieved; unverified |
| Flink et al. 2014 | ancient chicken genotypes (44 birds, 2,200 years) | not retrieved; unverified |

## Pre-registered prediction
- Under the claimant's model: with s fixed at the Loog point estimate, d_chicken is within 0.1 of 1.0 for any reasonable dominance model.
- Under the opposing model: d_chicken is not identifiable from one locus; across Loog's CI and the dominance models it spans roughly 0.5-1.9.
- Result that would change a verdict: Loog's posterior (not just the CI) with the matching dominance model giving a required-d interval that excludes 0.45.

## Check
Script: none yet (spec: bundle with `research/checks/c2c_ratio_identity.py`; solve required d over the Loog s posterior for additive, recessive and dominant forms). · Result: not run · Review: pending

## Simulator variables implied
Dominance h, s with uncertainty, generations per year, d.
