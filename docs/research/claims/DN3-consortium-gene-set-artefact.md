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
  internal: holds   # R4 L1 fix pass; verdict set at integration: (the conditional's test-design core is well formed; ¶15 arithmetic right: 20,400 - 13,454 = 6,946 = 34%, 20,400/13,454 = 1.516; ¶18 hedged). N2d note: even the antecedent would not show cherry-picking (a difference concentrated in non-one2one genes fits misaligned paralogs equally). 'Cherry-picked', 'artificial' are rhetoric (RH-22)
  fidelity: partial   # R-refresh 2026-10-12: CSAC 2005 now held. Count 13,454 and 'unambiguous 1:1 orthology' accurate; 'curation' partial (CSAC removed low-quality sequences and likely alignment artefacts and required high-quality alignments covering virtually the entire coding region, from 16,045 distinct genes, not from Day's 20,400); 'threw out 6,946 genes' compares different denominators
  external: contradicted   # conditional on L1b (like-for-like T2T rerun not yet run), see METHOD-AUDIT MA-12. R4 L1 fix pass; verdict set at integration: for the gene-list version: one2one 0.207 vs all genes 0.271 on one pipeline; credit: a real gene-set effect in Day's direction, material by R1 (+31%, a pipeline-level upper bound; orthology filtering has a methodological rationale), against +0.57 needed. Alignment-level version untested (L1b)
---

## Statement (verbatim)
> If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome.

> The Consortium used 13,454.

> They threw out 6,946 genes, one-third of the relevant data, through their “curation” pipeline for identifying “1:1 orthologs.” Our dataset includes 51.6% more genes than theirs.

> As far as I can tell so far, the only way to get 0.23 is to start with a pre-selected gene set that has already excluded the genes that don’t fit the expected answer.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶22, ¶14, ¶15 and ¶18 (Q176; ¶15 and ¶18 added in the R4 L1 fix pass, verbatim from the saved body.txt, page sha256 585308fa...). RH tag: Q176 dialectic (a conditional test); ¶15 numbers and ¶18 dialectic; "same old trick", "cherry-picked" and "One guess as to which way their methodology inclines" are rhetoric (RH-22).

## Formal statement
Test T: run one pipeline on gene sets G_C (13,454, reconstructed from Ensembl orthology) and G_A (20,400). Day predicts dN/dS(G_C) ~0.23 and dN/dS(G_A) ~0.80.

## Assumptions
- Stated: the Consortium list "can be reconstructed from Ensembl ortholog annotations".
- Implicit: the pipeline is correct on both sets, so any difference is the gene set.

## Responses
- Against (audit, R4 L1, fix pass): on one correct pipeline, one2one 0.207 and all genes 0.271; the gene set explains +0.06 (+31%, material by R1, pipeline-level upper bound); the non-one2one genes run at 0.45 (0.452 mapped, 0.382 for 482 unmapped transcripts), below neutral. The 'all genes' set is syntenic-net aligned, so only the gene-list version of the test was run.
- In support (Day; credit recorded in refresh-2026-10-11 and the test-methods review, entry 5): a valid two-gene-set design, proposed by Day before his own rerun; the gene-set effect exists and has his sign.
- Weaknesses in the responses: Ensembl one2one (16,766 genes) is not the 2005 list; L1 is not T2T.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 | "an initial catalogue containing 13,454 distinct 1:1 human–chimpanzee orthologues was created" after "removing low-quality sequences and likely alignment artefacts" from 16,045 distinct genes; "for which it was possible to generate high-quality sequence alignments covering virtually the entire coding region" (quotes-literature.md) | partial |

## Pre-registered prediction
L1 (868bb60): Day side ALL ~0.80; critic side ALL/O121 <= 1.3 and required NON121 > 1.5.

## Check
R4 L1 (`research/checks/results/R4-L1.md`; reviews a352991; fix pass). Day's own run of T is pending (Zenodo paper promised). **Integrated 2026-10-11:** internal holds (test design well formed), fidelity pending (CSAC 2005 unread), external contradicted for the gene-list version; the +31% gene-set effect is credited to Day.

## Simulator variables implied
- none

## R-refresh 2026-10-12
Day withdrew this explanation within 24 hours: "The difference is not a matter of gene selection, quality filtering, or computational error. It is a methodological artifact of using a conservation-dependent alignment to measure conservation." (Q186, "The Method is the Conclusion"; new claim DN6). His 10-11 "the only way to get 0.23 is to start with a pre-selected gene set" (¶18) is therefore superseded by its author (rule SC: same author, ledger and credit, `ledgers/versions.md`). He also reports a test on "their smaller subset" that "weren't" cherry-picked (Q185) with no row for the 13,454 list.
Readings (rule RD):
| Reading | Content | Internal | External |
|---|---|---|---|
| A | Self-correction: the 10-11 statement is withdrawn after Day's own gene-set test; the test design (conditional, two gene sets) stays valid | holds (unchanged) | contradicted for the original gene-list wording (L1 +31%), but the claim is no longer defended by its author |
| B | Unannounced reversal: two incompatible explanations in 24 hours | internal tension, no verdict change | same |
| C | Q185 "their smaller subset" = the 13,454 list was rebuilt and run | pending (no number) | untestable until shown |
Readings recorded (rule RD); verdict unchanged under A and B, so not counted as reading-dependent. The verdict field keeps the 10-11 wording's scoring (A); where Q185 is read as C, the result is unreleased. CSAC text now held: it supports Day on one point (the 13,454 were chosen for high-quality, near-full-coverage alignments, so alignment quality did select the set) and the critic side on another (the genes come from the genome alignment, not a protein realignment, and the 0.23 is a pooled ratio).

