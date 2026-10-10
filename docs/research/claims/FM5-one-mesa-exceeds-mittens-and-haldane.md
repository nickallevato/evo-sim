---
id: FM5
title: "Day, 'The Fourth Mechanism' FM5: a single mesa shows a human-lineage excess exceeding both the MITTENS fixation ceiling and Haldane's genome-wide maximum"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}]
load_bearing: false  # literal statement only; Day draws no inference in the sentence (rule S)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds   # literal (rule S): R4 FM, 32 human, 29 chimp, 31 bonobo, 19 gorilla mesas exceed 840 (F0 100 kb)
  fidelity: unverifiable   # Day's own Haldane and MITTENS figures are not given with the mesa (rule F); accurate on the audit's 840 / 191 reading
  external: supported   # as a description, non-discriminating: 'human-lineage' is not 'human-specific' (the earlier 'contradicted for any human-specific reading' is withdrawn)
---

## Statement (verbatim)
> A single mesa on a single chromosome shows an excess of human-lineage substitutions that exceeds both the MITTENS fixation ceiling and the maximum that natural selection can theoretically fix across the entire genome according to Haldane.

Source: [Day, "The Fourth Mechanism" (blog)](https://voxday.net/2026/10/10/the-fourth-mechanism/), 2026-10-10, ¶4 (Q166, FM5). Rule RH: dialectic.

## Formal statement
Excess substitutions in one mesa vs (a) the MITTENS ceiling and (b) Haldane's genome-wide maximum; the audit's thresholds are 191 and 840 substitutions (derivation in R4-FM); Day states neither figure nor units.

## Assumptions
- Implicit: comparing a regional count with a genome-wide selection ceiling presupposes the mesa is selected.

## Responses
- Against (critic): the same exceedance occurs in the chimp, bonobo and gorilla lineages; it is a regional-rate effect.
- In support (Day): the sentence is literally true on the public data.

## Primary literature
Haldane 1957 / Nunney 2003 (see H, H8); MITTENS (Q08, Q139).

## Pre-registered prediction
`fm_mesa_replication.py` (d723064) P2.

## Check
R4 FM; Reviews #43-#47 (steelman-day D1: rule S). Defeater d396.

## Simulator variables implied
- per-lineage mesa counts above ceilings
