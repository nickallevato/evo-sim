---
id: FM4
title: "Day, 'The Fourth Mechanism' FM4: dense windows cluster into contiguous blocks with 'sharp boundaries' ('mesas')"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}]
load_bearing: false  # premise of FM10; clustering is shared across lineages (R4 FM)
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a   # descriptive; no derivation to score
  fidelity: n/a   # no cited number
  external: supported   # R4 FM: CLUSTERING supported and shared (32-53% of human-mesa windows inside chimp mesas vs 0.56-1.0% background; shared-rate null reproduces 64-69% of human mesas at 100 kb). 'Sharp boundaries' is PENDING (fix pass 2 T1: calibrated E1 indeterminate; 100 kb unresolved). Alternative for the whole sentence: pending
---

## Statement (verbatim)
> Dense regions cluster next to other dense regions, forming contiguous blocks of elevated substitution with sharp boundaries in a pattern we call mesas.

Source: [Day, "The Fourth Mechanism" (blog)](https://voxday.net/2026/10/10/the-fourth-mechanism/), 2026-10-10, ¶4 (Q165, FM4). Rule RH: dialectic.

## Formal statement
Mesa = contiguous block of dense windows (FM rule in `fm_mesa_replication.py`); sharpness measured by `fm_mirror.edge_stats` (5 kb inside/outside) and calibrated against a perfect step (`fm_fix2.py` T1).

## Assumptions
- Implicit: clustering and sharpness distinguish a discrete event from a smoothly varying rate landscape.

## Responses
- Against (critic): clustering is covariation of regional rate across lineages (H~C density correlation 0.84, H~G 0.66); the same mesas appear in chimp, bonobo and gorilla.
- In support (Day): the blocks exist and are contiguous; at 10 kb the observed edges reach about 90% of a perfect step's S (q 0.76 / 0.63), so "not sharp" is not shown either.

## Primary literature
Not applicable (empirical description).

## Pre-registered prediction
`fm_mesa_replication.py` (d723064) and `fm_fix2.py` T1 (6aa9bb6, post hoc).

## Check
R4 FM; Reviews #43-#47. Defeater d395.

## Simulator variables implied
- regional rate landscape (step vs graded); mesa caller; edge-sharpness estimator
