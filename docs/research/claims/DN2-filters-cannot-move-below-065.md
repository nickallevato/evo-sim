---
id: DN2
title: "Day: no combination of quality filters moves dN/dS below 0.65; the strictest stack gives 0.64 on 10 genes"
side: day
branch: ROOT
parent: DN1
edges: [{type: supports, target: DN1}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: pending   # filter thresholds unstated; R4 L1 (awaiting review): on a correct frame the same filter list gives 0.23-0.28 and keeps 13,610 genes, so '10 remaining genes' signals stop codons in almost every extracted gene (a frame or extraction signature)
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> No combination of quality filters moves the number below 0.65.

> The most aggressive combined filter stack we could construct, requiring no stop codons in either species, low gap frequency, minimum substitution count, length threshold, and outlier removal, still produced dN/dS = 0.64 on 10 remaining genes.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶17 (Q175). RH tag: dialectic.

## Formal statement
min over filter combinations of pooled dN/dS >= 0.65; full stack n = 10 genes, dN/dS 0.64.

## Assumptions
- Implicit: a stop-free requirement removes few correctly extracted genes. On a correct extraction human GENCODE CDS are stop-free by construction and 96% of human-chimp pairs are stop-free in both (R4 L1), so a stack that leaves 10 of 20,400 genes implies internal stops in nearly all extracted sequences.

## Responses
- Against (audit, R4 L1, awaiting review): filters move a correct-frame result by < 0.05 (0.234-0.281); the near-empty stack is not reproduced by a correct pipeline (13,610 genes) and only partly by frame errors (46-125 genes).
- In support (Day): his observation that filters do not matter much is reproduced in kind (the range is narrow), at a different level.

## Primary literature
None cited.

## Pre-registered prediction
L1 D5 (868bb60): a correct frame leaves > 80% of genes stop-free and thousands after the full stack.

## Check
R4 L1 (awaiting review).

## Simulator variables implied
- none
