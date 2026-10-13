---
id: FM10
title: "Day, 'The Fourth Mechanism' FM10: 'neither natural selection nor neutral diffusive drift can still be considered viable candidates'"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}, {type: depends-on, target: FM3}, {type: depends-on, target: FM4}, {type: depends-on, target: FM5}]
load_bearing: true  # the ROOT-level conclusion of the post
sourcing: firsthand
status: reviewed
verdicts:
  internal: pending   # R4 FM: no derivation from FM3-FM5 is stated. Rule-N grep of Day's corpus at integration (2026-10-10): no text states or defends 'drift implies a uniform rate'; N2b not triggered (see R4 FM paragraph); the N2d reading ('stronger than its premises') is available but needs a deliberate call. Left pending. Owner decision 2026-10-10: stays pending until Day releases his method/window/statistic; rule N2d open, revisit on release
  fidelity: n/a
  external: contested   # R4 FM: every pre-registered discriminating cell (P3, P4, P5, P7) falls on the critics' side; mirror test M1 and fix pass 2 leave one orthologous chrX window; leaning critic. A human-specific autosomal mesa signal is contradicted on alignable sequence (a premise, not a verdict on FM10)
---

## Statement (verbatim)
> What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable candidates. And there is no need to take my word for anything with regards to this, all of the data has been provided by the T2T Primate Consortium (Yoo et al. 2025) aligned with Progressive Cactus (Armstrong et al. 2020).

Source: [Day, "The Fourth Mechanism" (blog)](https://voxday.net/2026/10/10/the-fourth-mechanism/), 2026-10-10, ¶8 (Q171, FM10). Rule RH: dialectic. The original reads "can still be considered viable candidates" (no bracketed "[not]"); read in context it means "can no longer be considered viable". Quoted as published.

## Formal statement
Unstated. The step from FM3-FM5 requires a premise of the form "neutral diffusive drift implies a uniform per-window rate and a lineage-symmetric excess".

## Assumptions
- Implicit: the premise just stated. The qualifier "diffusive" leaves non-diffusive drift (relictation, Day's own E4 class) outside the claim.

## Responses
- Against (critic): the pattern is shared across lineages and reproduced by a shared-rate null (64-69% of human mesas at 100 kb); the residual phi_res 2.3-2.7 is an upper bound, not a mechanism.
- In support (Day): the invitation to replicate is real; the chrX F1 cell and the F0 excess (SD sequence) are Day-side observations; the shared-rate null borrows other lineages' variation and is not a mechanistic neutral model.

## Primary literature
Yoo et al. 2025; Armstrong et al. 2020 (named data sources).

## Pre-registered prediction
`fm_mesa_replication.py` (d723064) P3, P4, P5, P7; `fm_mirror.py` (737648e) M1-M6; `fm_fix2.py` (6aa9bb6) T1-T5.

## Check
R4 FM (`research/checks/results/R4-FM.md`), reviews #43-#47. Defeaters d397-d398.

R4 FMnull (`research/checks/results/R4-FMnull.md`; reviews #76-#79; integrated 2026-10-13). **No verdict change**: internal stays `pending` (owner decision 2026-10-10, until Day releases his method), external stays `contested`. The registered rule does not license a quantitative defeater against the audit's reconstructed premise (drift implies a uniform rate; not Day's words): CRITIC on every reading is not met, and the finding is recorded only with its power statement. **Critics:** no measured cell exceeds three times the neutral upper bound at any W from 1 kb to 10 Mb; at W <= 1 Mb, where Q164 is true, the measured index is inside or below the band (index / N_hi 0.11-0.91); the index is lineage-shared (phi_H / phi_C 0.97-1.04 from 1 kb to 3 Mb; corr(H, C) 0.87 at 100 kb, 0.96 at 1 Mb); F2 phi_HC lies 22-31 times below the dominant planted scenario at matched exposure. **Day:** the check had power against a dominant one-lineage block mechanism and little against one below f e^2 of about 0.02 (a doubling over 2% of the genome scores CRITIC or MARGINAL-IN); no Day-side criterion could be met by a mechanism smaller than the one Q169 (b) asserts, and S2 not even by that one off the window grid, a defect of the audit's criteria on Day's side; F2 phi_HC is above the gBGC-only bound (lambda_M = 0) at 1-10 kb (a lineage-specific mutational share of 0.04-0.07 absorbs it); six cells at 3-10 Mb lie above the Francioli-edge bound (none DAY). **Both:** the F0 human excess is a reference-projection effect (R4 FM mirror test); the audit's own errors (P4/P5 label bug, grid-phase dependence of P8 (ii), the unreachable S2 criterion) lower confidence in its engineering for both sides; Day has released no window, statistic or code. The shared-rate sentence left open by R4 FM is answered as description only; any defeater would attach to that R4 FM sentence, reading-dependent, not to FM10's verdict.

## Simulator variables implied
- shared regional rate; lineage-specific rate; reference-projection of duplicated sequence
