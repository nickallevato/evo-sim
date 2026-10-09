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
  internal: holds   # 35M / 2 = 17.5M
  fidelity: partial   # CSAC 1.23% includes polymorphism (verified-partial); 's7.3 concession' wording is ambiguous on bp vs events (R4 GAP-07)
  external: supported   # R4 GAP-07b: 17.5M is 83% of measured events per lineage (21.05M, hg38 vs panTro6) and brackets the polymorphism-corrected fixed-event count 16.4-18.1M; the omitted indels (~10-12%) and the included polymorphism (14-22% of SNV differences) roughly cancel. The shortfall built on it rises slightly on the measured count (~99,000-110,000 at G_f 1,322; 86,000-95,000 polymorphism-corrected)
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

R4 GAP-07 (research/checks/results/R4-GAPS-04-07-02.md): The SNV-only 17.5M is corroborated in magnitude by the event count (18.2-19.7M calibrated; 20.0M CSAC-observed per lineage); the shortfall built on it (~1e5) is untouched by this check. s7.3 says SVs 'should not each count as a single fixation event in the same sense as a point mutation'; the wording does not settle whether Day regards base-pair counts as wrong. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

R4 GAP-07b (research/checks/results/R4-GAP07b-alignment.md): SNVs are 90% of measured events (37.77 / 42.10M). Day's SNV-only row is neither a lower nor an upper bound on the fixed-event count: with CSAC's fixed share (0.78-0.86) applied, fixed events per lineage are 16.4-18.1M [post hoc], which bracket 17.5M. 'Discount every structural variant ... to zero' (Q103) also drops the 4.3M small indel events (89% are 1-10 bp), so it is an SNV count, not an event count. The SNV-only shortfall at MITTENS 3.0 s7.3 rates is 91,800 on 17.5M (Day prints 91,600), 99,100 on measured SNVs/2 and 110,400 on measured events per lineage; the rate side (G_f) is outside this check. Review: `research/checks/REVIEW.md` (review #8, 2026-10-09).

## Simulator variables implied
- Preset: SNV-only requirement.
