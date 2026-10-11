---
id: DN3
title: "Day: the Consortium's 0.23 is an artefact of a curated 13,454-gene set; his proposed test is to rerun both gene sets on one pipeline"
side: day
branch: ROOT
parent: DN1
edges: [{type: attacks, target: DN5}, {type: depends-on, target: DN1}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: pending   # the conditional in Q176 is well formed (credit); its antecedent awaits Day's run. R4 L1 (awaiting review): one2one 0.207 vs all genes 0.271 (+31%); NON121 would need pN/pS 2.42 for the total to reach 0.80
  fidelity: pending   # the 13,454 count and the 'curation' description are not checked against CSAC 2005 (not read)
  external: pending   # proposed after review: contradicted for the size of the effect (0.06, not 0.57); a real gene-set effect in Day's direction is supported
---

## Statement (verbatim)
> If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome.

> The Consortium used 13,454.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶22 and ¶14 (Q176). RH tag: Q176 dialectic (a conditional test); "same old trick", "cherry-picked" and "One guess as to which way their methodology inclines" are rhetoric (RH-22).

## Formal statement
Test T: run one pipeline on gene sets G_C (13,454, reconstructed from Ensembl orthology) and G_A (20,400). Day predicts dN/dS(G_C) ~0.23 and dN/dS(G_A) ~0.80.

## Assumptions
- Stated: the Consortium list "can be reconstructed from Ensembl ortholog annotations".
- Implicit: the pipeline is correct on both sets, so any difference is the gene set.

## Responses
- Against (audit, R4 L1, awaiting review): on one correct pipeline, one2one 0.207 and all genes 0.271; the gene set explains +0.06; the non-one2one genes run at 0.45, below neutral.
- In support (Day; credit recorded in refresh-2026-10-11 and the test-methods review, entry 5): a valid two-gene-set design, proposed by Day before his own rerun; the gene-set effect exists and has his sign.
- Weaknesses in the responses: Ensembl one2one (16,766 genes) is not the 2005 list; L1 is not T2T.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 | not read | pending |

## Pre-registered prediction
L1 (868bb60): Day side ALL ~0.80; critic side ALL/O121 <= 1.3 and required NON121 > 1.5.

## Check
R4 L1 (awaiting review). Day's own run of T is pending (Zenodo paper promised).

## Simulator variables implied
- none
