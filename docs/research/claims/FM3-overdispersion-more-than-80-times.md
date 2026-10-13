---
id: FM3
title: "Day, 'The Fourth Mechanism' FM3: substitution density across the genome is 'more than 80 times more variable than a uniform-rate process predicts'"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}]
load_bearing: false  # a premise of the FM10 conclusion, but the statistic is shared by all lineages and only descriptive (R4 FM)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds   # R4 FM: > 80 is reachable (weak sense) with phi at W >= 1 Mb (>= 100 kb for DHC), every lineage; the statistic and window are unreleased
  fidelity: unverifiable   # rule F: window and statistic unreleased; phi grows roughly linearly with W (H at F0: 3.3, 10.4, 36.9, 136 at 1 kb to 1 Mb), so the same data give 3x or 800x
  external: supported   # reading-dependent: R4 FMnull (integrated 2026-10-13, reviews #76-#79; value unchanged). Field takes R1 (variance over mean, the reading "overdispersed" names; rule RD, most defensible reading): `supported` as a description, non-discriminating. "More than 80" is true of the held alignment at W >= 1 Mb in all ten lineage-by-masking cells (F2 at 1 Mb: H 89.4, C 89.5, B 88.3, G 85.1, DHC 253), and wherever it is true at W <= 1 Mb the measured index is inside or below a mechanistic neutral band (index / N_hi 0.11 to 0.91 over eight parameter sets; post hoc). R2 (SD ratio > 80, the audit's reading): true in no measured cell. R1 at W <= 10 kb: extended reading, UNTESTED, `unverifiable` until Day releases W. Earlier (R4 FM): against a shared-rate null it shrinks to about 2-6 (F2 100 kb: 2.7 H, 2.4 C). Alternative: contested for the implied 'surprising' reading
---

## Statement (verbatim)
> The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts.

Source: [Day, "The Fourth Mechanism" (blog)](https://voxday.net/2026/10/10/the-fourth-mechanism/), 2026-10-10, ¶4 (Q164, FM3). Rule RH: dialectic.

## Formal statement
Dispersion = variance of per-window substitution density relative to a uniform-rate (Poisson) process, window and statistic unstated. R4 FM uses phi = Var/mean-type overdispersion per lineage at W = 1 kb to 1 Mb.

## Assumptions
- Stated: the T2T alignment is adequate. Implicit: a uniform-rate process is the relevant comparison (no one in population genetics assumes it).

## Responses
- Against (critic): overdispersion is the standard result of mutation-rate heterogeneity; against a null with shared regional rate variation it falls to about 2-6.
- In support (Day): the data are public; above 80x is reproduced at 1 Mb for every lineage (R4 FM).

## Primary literature
Yoo et al. 2025 and Armstrong et al. 2020 (named by Day); not re-read here.

## Pre-registered prediction
See `research/checks/fm_mesa_replication.py` (d723064): P1 (above 80x at a stated window).

## Readings (rule RD; R4 FMnull, integrated 2026-10-13; counted as a reading-dependent verdict)
| reading | whose | where "more than 80" is true of the held data | class where true / status | sets the field? |
|---|---|---|---|---|
| R1: D = Var / mean, normalised for aligned bases | the reading "overdispersed" selects | W >= 1 Mb, all ten lineage-by-masking cells (DHC from 30 kb F0, 300 kb F2) | inside or below the band at W <= 1 Mb under all eight sets (index / N_hi 0.11-0.91); six cells MARGINAL-OUT at 3-10 Mb under the Francioli-edge variants; none DAY | **yes**: `supported` as a description, non-discriminating |
| R1x: D - 1 > 80 | numerically R1 | same cells (smallest 85.1) | same | same as R1 |
| R1u: D on counts not normalised for aligned bases | audit's addition | from 300 kb for single lineages, 30-100 kb for DHC | MARGINAL-IN, CRITIC or ALN-dependent; none DAY; at F2 the index largely measures the mask | no |
| R2: SD ratio > 80, D > 6,400 | audit's addition | nowhere (largest normalised SD ratio 53.5, DHC F0, 10 Mb; 25.5 single lineage) | the number 6,400 is DAY against every band at W <= 1 Mb (P3), a class of the number, not of the data | no; neither side's credit |
| R1 at W <= 10 kb (DHC W <= 3 kb) | extended reading (a window Day did not state) | not true on alignable sequence: single lineages 1.4-10.4, DHC 2.2-20.6 | 80 as a number would be DAY in all six variants; UNTESTED as his claim, `unverifiable` (rule F) | no (extended readings cannot set the field) |
| TREE, PAIRS, BP units | audit's sub-readings of "substitution density across the genome" | not measurable on `fm_bins.npz` | UNTESTED; unsourced inputs | no |

## Check
R4 FM (`research/checks/results/R4-FM.md`), reviews #43-#47. Defeater d394.

R4 FMnull (`research/checks/results/R4-FMnull.md`; pre-registered `fm_mesa_null.py`; reviews #76-#79; fix pass 2802425). **Day:** the sentence is true on the public data at W >= 1 Mb in every lineage and both maskings; the check had little power against any block mechanism smaller than the dominant one (all eight non-dominant planted scenarios score CRITIC or MARGINAL-IN), and no Day-side criterion could be met by such a mechanism. **Critics:** it is as true of chimpanzee, bonobo and gorilla as of human (phi_H / phi_C 0.97-1.04 from 1 kb to 3 Mb), and wherever it is true at W <= 1 Mb the measured index is not outside a neutral band; pedigree de novo mutation variation alone reaches the measured 1-Mb dispersion. **Both:** the number is a description, non-discriminating; Day has released no window, statistic or code (fidelity `unverifiable`, rule F); the audit's own errors (P4/P5 label bug, grid-phase dependence of P8 (ii), invalid covariate-adjusted index) are recorded in the write-up. Defeaters d462-d466.

## Simulator variables implied
- window size; per-lineage overdispersion statistic; mutation-rate heterogeneity (regional)
