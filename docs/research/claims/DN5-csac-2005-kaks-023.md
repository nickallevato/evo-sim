---
id: DN5
title: "CSAC 2005 (as relayed by Day): human-chimp Ka/Ks = 0.23 on 13,454 orthologous genes"
side: literature
branch: ROOT
parent: DN1
edges: []
load_bearing: false
sourcing: secondhand
status: extracted
verdicts:
  internal: n/a   
  fidelity: accurate   # R-refresh 2026-10-12: CSAC 2005 text held; "The K A/K S ratio for the human–chimpanzee lineage (q hominid) is 0.23" and "the value of 0.23 obtained with all human–chimpanzee orthologues" (13,454); machine-checked quotes in quotes-literature.md. Relay rule U still bars an internal score
  external: supported   # R4 L1 fix pass; verdict set at integration: (in kind): an independent pipeline gives 0.207 on Ensembl one2one genes (release 116) and 0.200 with CSAC-like quality filters; fidelity waits for CSAC 2005 and an independent ML estimate to be fetched (critic-side review #3)
---

## Statement (verbatim)
> When the same 2005 Consortium reported the canonical Ka/Ks ratio, which is advertised as the measure of natural selection's strength in coding sequences, they reported 0.23.

Source: Day's relay, [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶5 (Q173 note). Primary: CSAC 2005, Nature 437:69 (not read for this value).

## Formal statement
Ka/Ks = 0.23 over 13,454 human-chimp 1:1 orthologs (CSAC 2005, per Day).

## Assumptions
- Implicit: 1:1 orthologs with complete, well-aligned CDS.

## Responses
- Against (Day, DN3): the 13,454 set is curated and excludes a third of genes.
- In support (audit, R4 L1): the value reproduces in kind on an independent pipeline.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 | "The K A/K S ratio for the human–chimpanzee lineage (q hominid) is 0.23." (13,454 orthologues; pooled by summing substitutions and sites) | accurate |

## Pre-registered prediction
L1 critic side: O121 in 0.20-0.30.

## Check
R4 L1 (`research/checks/results/R4-L1.md`; reviews a352991; fix pass). **Integrated 2026-10-11:** internal n/a (relay, rule U), fidelity pending (CSAC 2005 and an independent ML estimate to be fetched), external supported in kind.

## Simulator variables implied
- none

## R-refresh 2026-10-12
CSAC 2005 text and Supplementary Table S23 (13,454 RefSeq NM_ ids) are now held (`bib-literature.md`, `harvest-log-literature.md`). Fidelity of Day's relay (0.23, 13,454): accurate. Method facts from the Methods text: the 13,454 came from 16,045 genes "indirectly aligned to the chimpanzee sequence via the genome alignment" after removing low-quality sequences and likely alignment artefacts; Clustal W only for a 7,043-gene subset; K_A/K_S for a set is pooled ("summing the number of substitutions and the number of sites"), so no mean-of-ratios estimand mismatch (this corrects the refresh maths review 4, which relied on memory). Day's Q180 reading a (the 0.23 came from a protein-guided alignment) is contradicted by this text; reading b is pending L1c (see DN6). Day's 10-12 "~40%" for the 0.23 and N/S 3.54 vs CSAC's own N_S/N_A = 0.36 (N/S 2.78) stays a slip-ledger candidate, not an error (R1).
