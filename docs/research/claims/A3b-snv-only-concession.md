---
id: A3b
title: "Day's SNV-only variant: 17.5M required fixations still gives a 91,600-fold shortfall"
side: day
branch: A
parent: A3a
edges: [{type: revises, target: A3a}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> A reasonable objection holds that large structural variants such as inversions, deletions, insertions of mobile elements, should not each count as a single fixation event in the same sense as a point mutation. This is a legitimate methodological concern.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.12 (s7.3).

> Restricting to the approximately 35 million SNVs and apportioning symmetrically: 17.5 million required fixations on the human lineage.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.12 (s7.3).

> At 1,322 gen/fix (non-mutator): 191 achievable. Shortfall: 91,600×. At 105 gen/fix (mutator): 2,407 achievable. Shortfall: 7,271×.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.13 (s7.3).

## Formal statement
R_SNV = 35e6 / 2 = 17.5e6; achievable = 252,000/1,322 = 190.6 (191); shortfall = 17.5e6/191 = 91,623 (paper 91,600); mutator: 252,000/105 = 2,400 (paper 2,407, i.e. G_f = 104.7), 17.5e6/2,407 = 7,270 (paper 7,271). All reconcile (python3 -I). The pass-1 figure ~94,000 is not in the text.

## Assumptions
- Stated: SNV-only is the conservative counting; the shortfall persists at four to five orders of magnitude.
- Implicit: the 35M SNVs are all fixed differences (CSAC: 14–22% polymorphic, A3c); LTEE rate transfers unscaled (A5).

## Responses
- Against: Sparky_6_4 (A5b) shows that after scaling by per-genome mutation supply, the achievable count is about the same as 17.5M.
- In support: this is a self-correction by Day; Camestros's observation (CA-02) that the arithmetic is not wrong applies here too.
- Weaknesses in the responses: A5b's scaling is linear (flagged by its author); using Day's own mutator exponent gives 80–450x residual (A5b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 | 1.23% total, "1.06% or less corresponding to fixed divergence" | verified-partial |

## Pre-registered prediction
Covered by A5/A5b predictions. Result recorded above.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- Preset: SNV-only requirement.
