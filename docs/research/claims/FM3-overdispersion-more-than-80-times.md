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
  external: supported   # as a description; the magnitude is set by the window; against a shared-rate null it shrinks to about 2-6 (F2 100 kb: 2.7 H, 2.4 C). Alternative: contested for the implied 'surprising' reading
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

## Check
R4 FM (`research/checks/results/R4-FM.md`), reviews #43-#47. Defeater d394.

## Simulator variables implied
- window size; per-lineage overdispersion statistic; mutation-rate heterogeneity (regional)
