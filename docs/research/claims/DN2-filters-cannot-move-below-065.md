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
  internal: pending   # filter thresholds unstated. R4 L1 fix pass: 0.64 against 'below 0.65' in the same paragraph is a 1.5% slip (S-DN2-1); the 10-gene stack offered as robustness is ledgered (S-DN2-2, N2d candidate limited by N1)
  fidelity: n/a
  external: pending   # R4 L1 fix pass, proposed for integration: contradicted as a statement about human-chimp coding sequence: all 32 stacks give 0.23-0.28 on a correct extraction, and no correct extraction leaves a near-empty strict stack (13,610 genes; 258 with a terminal-stop convention). As a report of his pipeline it is plausible: a within-gene contaminated extraction is filter-robust (0.76-0.85, post hoc)
---

## Statement (verbatim)
> No combination of quality filters moves the number below 0.65.

> The most aggressive combined filter stack we could construct, requiring no stop codons in either species, low gap frequency, minimum substitution count, length threshold, and outlier removal, still produced dN/dS = 0.64 on 10 remaining genes.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶17 (Q175). RH tag: dialectic.

## Formal statement
min over filter combinations of pooled dN/dS >= 0.65; full stack n = 10 genes, dN/dS 0.64.

## Assumptions
- Implicit: a stop-free requirement removes few correctly extracted genes. On a correct extraction 96% of human-chimp pairs have no internal stop in either species (R4 L1). If the filter also counts the terminal stop codon (95% of human CDS end in one), a correct extraction still leaves 861 genes alone and 258 in the full stack (R4 L1 fix pass), so a stack of 10 is not produced by a correct extraction under either convention.

## Responses
- Against (audit, R4 L1, fix pass): filters move a correct-frame result by < 0.05 (0.234-0.281); the near-empty stack is not reproduced by a correct pipeline (13,610 genes; 258 with the terminal-stop convention). A gene-level frame-error mixture is contradicted by this very report (filters would pull it to 0.24). A within-gene chimp-side contamination of every gene plus the terminal-stop convention gives 73 genes at 0.83 (exploratory, post hoc).
- In support (Day): his observation that filters do not matter much is reproduced in kind (the range is narrow), at a different level.

## Primary literature
None cited.

## Pre-registered prediction
L1 D5 (868bb60): a correct frame leaves > 80% of genes stop-free and thousands after the full stack.

## Check
R4 L1 (`research/checks/results/R4-L1.md`; reviews a352991; fix pass with the per-gene run c04a1f8).

## Simulator variables implied
- none
