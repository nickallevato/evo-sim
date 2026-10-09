---
id: B2e
title: "keruru (Zenodo draft): a temporal N_e measured from ancient genomes is about three orders of magnitude below Wright's 4N/(V_k+2) applied to the Bronze Age census, so the input to Day's census ceiling is wrong where it can be tested"
side: critic
branch: B
parent: B2b
edges: [{type: attacks, target: B2b}]
load_bearing: false  # attacks the input of a load-bearing node (B2b); unreviewed draft
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # direction is right: if N_e << 4N/(V_k+2) at a given census, 4N_e < G holds up to a much larger census, so X = (V_k+2)G/16 understates the ceiling; 0.57 / (6.9e-4 to 8.1e-4) = 700-820x
  fidelity: n/a
  external: pending   # Draft 1, '[CHECK]' marks, ratio stated three ways (1e-4, 4e-4, 8e-4); census 1e7 assumed; temporal N_e in an admixing population is model-dependent; needs independent AADR replication before B2/B2b can move
---

## Statement (verbatim)
> "Wright's N_e = 4N/(V_k + 2) is the input to that argument. In the one period where it can be checked against a direct measurement it is wrong by three orders of magnitude"

Source: [keruru (C. Kereru), Zenodo 22184713](https://zenodo.org/records/22184713), Draft 1, 2026-08-31, adna-draft-1.md s6, line 689 (RF-12).

> "We do not claim the ceiling argument is refuted. We claim its input is measurably wrong where it can be tested"

Source: same, line 696 (RF-13).

## Formal statement
Day's ceiling (B2b): 4N_e < G with N_e = 4N/(V_k+2) gives N < X = (V_k+2)G/16. keruru: for Bronze Age Europe at census N ~ 1e7, Wright's formula with Day's V_k gives N_e/N ~ 0.57 (4/7, V_k = 5); measured temporal N_e = 6,933 (Bronze Age) or 8,139 (Bronze Age to Medieval), i.e. N_e/N ~ 7e-4 to 8e-4. `derived:` 0.57/8.1e-4 = 700; 0.57/6.9e-4 = 820. With N_e ~ 1e4, 4N_e = 4e4 generations is 1.4-15.1% of a ~260,000-generation lineage across his four bins (keruru's table; RF-13 note).

## Assumptions
- Stated: the temporal estimator needs no mutation rate or coalescent (C5b); island-model, moving-frame and V_k simulations do not reproduce a ratio this low (s6.2: "saturation floor ... about 5 x 10^-2", RF-14).
- Implicit: a Bronze Age census of order 1e7; admixture and structure in the AADR bins do not bias the estimator downward by the needed factor; the B2b ceiling is read as a census bound.

## Responses
- Against (Day): C5a (Day's N_e near 2 from aDNA) and C4 (Day's own caution that drift-variance N_e cannot be read as population size) cut against reading temporal N_e as the B2b input. Day has not responded to the draft.
- In support: C5b (the same author's blog result); the standard N_e/N ratio for humans is of order 1e-3 to 1e-6 (draft, line 682), which is textbook, not new.
- Weaknesses in the responses: keruru's draft is internally inconsistent on the ratio (abstract "of order 10^-4", s6 "4 x 10^-4", s6.2 "8 x 10^-4"; 8,139/1e7 = 8.1e-4, derived) and carries [CHECK] marks; it reports no ancestry control or relatedness filtering (RF-16 note).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wright 1938 (N_e = 4N/(V_k+2)) | as used by Day (B2b) | see B2b |

## Pre-registered prediction
Not run. A replication would estimate temporal N_e from AADR frequency series with ancestry-stratified bins.
- Under keruru's model: N_e/N <= 1e-3 in every well-powered bin.
- Under the B2b input: N_e/N ~ 0.5.
- Result that would change a verdict: an independent replication within a factor of 3 of keruru's N_e would move B2b external toward contradicted (as a census bound); a replication near 0.5 N would support B2b's input.

## Check
None yet (proposed: independent AADR temporal-N_e replication; queue in `research/checks/REVIEW.md`). From the 2026-10-09 corpus refresh (C-9).

## Simulator variables implied
Census N and N_e as separate inputs; N_e/N ratio; admixture pulses (cf. C1c).
