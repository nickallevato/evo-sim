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
  external: contradicted   # the MA-12 condition on L1b (criticality/METHOD-AUDIT-2026-10-12.md) is discharged for this alignment and annotation by R4 L1b (integrated 2026-10-13, reviews #70-#72): now on T2T and Cactus as well (the 'different assembly / complete extraction' route is closed for this alignment): hs1-referenced Cactus MAF, GENCODE v35 CAT, alignment-column extraction, Nei-Gojobori pooled; V0 ALL 0.271, SYN 0.209 (registered band CRITIC). DN2: min over 32 stacks on V0 0.214 (ALL), 0.194 (SYN) against the re-opening line 0.60. R4 L1 fix pass; verdict set at integration: as a statement about human-chimp coding sequence: all 32 stacks give 0.23-0.28 on a correct extraction, and no correct extraction leaves a near-empty strict stack (13,610 genes; 258 with a terminal-stop convention). As a report of his pipeline it is plausible: a within-gene contaminated extraction is filter-robust (0.76-0.85, post hoc) Post hoc (L1b, separate sentence): the position-by-position arm reads 0.82-0.86 in every stack without an internal-stop filter and 0.52-0.58 in every stack with one, below his 0.65; under a stop filter that counts the final codon (S'), half of the 32 stacks hold 8-12 genes on any extraction (19,294 of 19,310 human CDS end in a stop). The A/B split stays: (A) as a statement about the sequence `contradicted` (0.21-0.28 on V0; S' grid up to 0.377 on 12 genes); (B) as a report of his pipeline, consistent with position-by-position pairing under S' and not under S, unverifiable until his table is released.
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
R4 L1 (`research/checks/results/R4-L1.md`; reviews a352991; fix pass with the per-gene run c04a1f8). **Integrated 2026-10-11:** internal pending (thresholds unstated; 0.64 vs "below 0.65" ledgered S-DN2-1), fidelity n/a, external contradicted for a correct extraction.

## Simulator variables implied
- none

## R4 L1b (integrated 2026-10-13)
`research/checks/results/R4-L1b.md` (pre-registered 0fe3c7f; pre-run notes 5e64f0a; reviews #70-#72: 3415770, e163ca2, 8c34996; fix pass 098ac12; post hoc `l1b_posthoc_x1_breakdown.py` 9c4a359). T2T rerun: GENCODE v35 CAT on hs1 against mPanTro3, Cactus MAF, Nei-Gojobori pooled, bases paired by alignment column. Band CRITIC.

Min over 32 filter stacks on V0: 0.214 (ALL), 0.194 (SYN) against the re-opening condition 0.60; full stack 0.225 on 11,743 genes. Verdict `contradicted` stays, now also on T2T.

Readings (the existing A/B split stays; post hoc X1 numbers added). (A) As a statement about the sequence: `contradicted`. (B) As a report of his pipeline: the position-by-position arm (X1) reads 0.82-0.86 in every stack without an internal-stop filter and 0.52-0.58 in every stack with one (below his 0.65); under S' (a stop filter that counts the final codon) half of the 32 stacks hold 8-12 genes on any extraction, because 19,294 of 19,310 human CDS end in a stop. His near-empty stack (10 genes) is thereby reproduced by a column-paired extraction under the literal reading of his stop filter (9 genes); the value on 9 genes gives no useful precision. Whether his pipeline is position-by-position is unverifiable until his table is released. **Day:** his strict-stack count is not evidence of a fault; the filter list matches. **Critics:** no column-paired stack reaches 0.65 (V0 maximum 0.283; S' grid up to 0.377 on 12 genes; adversarial row VL 0.306).
