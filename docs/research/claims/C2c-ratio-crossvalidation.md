---
id: C2c
title: "The constant TYR/SLC45A2 selection-coefficient ratio across d values is a cross-validation showing d is not a fitting artifact"
side: day
branch: C
parent: C2
edges: [{type: supports, target: C2}]
load_bearing: false  # Supports the empirical reality of d (C2). If it fails, C2 rests only on the per-locus fits and on C2a.
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> "The ratio remains constant at ~0.49 across all d values. This confirms that the generation overlap correction is capturing real population dynamics: both pigmentation genes experience the same demographic constraints, differing only in their phenotypic contributions. A fitting artifact would produce inconsistent ratios."

Source: [The Bio-Cycle Fixation Model](https://zenodo.org/records/18203514), Z18203514, 2026-01-09, §3.3 (Table 3 follows), ¶102 of the docx text extraction. The same claim is in the v1 abstract (Z18202768): "confirming that the correction reflects genuine population dynamics rather than a fitting artifact."

## Formal statement
Table 3 (paper): required s for the observed frequencies at d = 0.40, 0.50, 0.60, 1.00: SLC45A2 0.058, 0.047, 0.038, 0.023; TYR 0.028, 0.023, 0.019, 0.011; ratio 0.48, 0.49, 0.49, 0.49.

derived: s x d = 0.0232, 0.0235, 0.0228, 0.0230 for SLC45A2 (constant within 3%); 0.0112, 0.0115, 0.0114, 0.0110 for TYR (constant within 4%); ratio 0.483, 0.489, 0.500, 0.478.

Why: under weak selection the logit gain over G nominal generations is about s x (d G); trajectories identify the product s d. For any two loci with the same G, s_TYR(d)/s_SLC(d) = (s d)_TYR/(s d)_SLC, independent of d. So the constancy is an algebraic consequence for any d, real or invented; it is not a test of d. Day's own sensitivity (Z18202768: +/-25% on s moves mean d to 0.36 / 0.56) is the same identity.

## Assumptions
- Stated: both loci "experience the same demographic constraints".
- Implicit: that a fitting artefact would break the ratio. It would not: any multiplicative rescaling of effective time leaves the ratio unchanged.

## Responses
- Against: no critic engaged it. The repo's derivation above.
- In support: none.
- Weaknesses in the responses: none to record; pending review of the derivation (R4).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none for the cross-validation step | n/a | n/a |

## Pre-registered prediction
- Under the claimant's model: the ratio is constant for d in its plausible range because d is real.
- Under the opposing model: the ratio is constant for every d, including d far from any biological value (for example 0.2, 0.8, 2.0), because only s x d is identified.
- Result that would change a verdict: if the required-s ratio for the same two loci at d = 0.2 and d = 2.0 departs from 0.48 by more than a few percent, the identity argument fails (the recursion would be outside the weak-selection regime, so the result must be checked with the discrete recursion, not the logit approximation).

## Check
Script: none yet (spec: `research/checks/c2c_ratio_identity.py`, planned; solve the discrete recursion for required s at d in {0.2, 0.4, 0.5, 0.6, 0.8, 1, 2} for both loci with the Table 1 inputs; report ratio and s x d). · Result: not run (the Table 3 arithmetic above is a recompute from the paper's own rounded numbers) · Review: pending

## Simulator variables implied
d, s per locus, number of generations, p0.
