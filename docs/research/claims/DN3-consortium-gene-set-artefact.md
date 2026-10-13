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
  external: contradicted   # the MA-12 condition on L1b (criticality/METHOD-AUDIT-2026-10-12.md) is discharged for this alignment and annotation by R4 L1b (integrated 2026-10-13, reviews #70-#72): now on T2T and Cactus as well (the 'different assembly / complete extraction' route is closed for this alignment): hs1-referenced Cactus MAF, GENCODE v35 CAT, alignment-column extraction, Nei-Gojobori pooled; V0 ALL 0.271, SYN 0.209 (registered band CRITIC). DN3 extended to the alignment-level version as registered (ALL - O121 = +0.033, O121 0.238; the registered `supported` needed >= +0.40 with O121 <= 0.30). R4 L1 fix pass; verdict set at integration: for the gene-list version: one2one 0.207 vs all genes 0.271 on one pipeline; credit: a real gene-set effect in Day's direction, material by R1 (+31%, a pipeline-level upper bound; orthology filtering has a methodological rationale), against +0.57 needed. Alignment-level version: now tested (L1b) Credit to Day, restated with the T2T value (R4 L1b; no materiality label added or removed): a real gene-set effect in Day's direction on both pipelines, +31% hg38, +14% T2T (+30% against the CSAC-like set, +3% among syntenic genes); non-one2one genes read 1.9-2.2 times one2one on both; size depends on annotation and gene-set composition (2,486 non-one2one genes here, 6,417 in L1); against +0.57 needed; Day's own Q184 table shows +0.003. Not marked pipeline-specific (gap >= +0.02).
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

## R4 L1b (integrated 2026-10-13)
`research/checks/results/R4-L1b.md` (pre-registered 0fe3c7f; pre-run notes 5e64f0a; reviews #70-#72: 3415770, e163ca2, 8c34996; fix pass 098ac12; post hoc `l1b_posthoc_x1_breakdown.py` 9c4a359). T2T rerun: GENCODE v35 CAT on hs1 against mPanTro3, Cactus MAF, Nei-Gojobori pooled, bases paired by alignment column. Band CRITIC.

The gene-set effect on T2T: ALL over one2one +0.033 (ratio 1.14, +14%), +30% against the CSAC-like set O121q, +3% among syntenic genes (+0.006); non-one2one genes read 1.93 times one2one (0.459 against 0.238; L1: 0.447 against 0.207). Registered rule: `supported` only if ALL - O121 >= +0.40 with O121 <= 0.30; observed +0.033 and 0.238, so the external verdict `contradicted` stays, now extended to the alignment-level version. Credit to Day restated with the T2T value: "a real gene-set effect in Day's direction on both pipelines: on hg38/multiz +31% over one2one (L1); on T2T/CAT/Cactus +14% over one2one, +30% over the CSAC-like set O121q, +3% among syntenic genes; non-one2one genes read 1.9-2.2 times one2one on both; size depends on annotation and gene-set composition (2,486 non-one2one genes here against 6,417 in L1); against +0.57 needed; Day's own Q184 table shows +0.003". Not marked pipeline-specific (the gap exceeds +0.02). No materiality label is added to the T2T value (the lead ruled out post hoc R1 grading of the credit in either direction); the L1 label stands as integrated. Composition: about 1,150 of the 2,486 non-one2one genes have no Ensembl chimp homology type. **Day:** a real effect with his sign on a second pipeline. **Critics:** the T2T gap is +0.033 against the +0.57 the claim needs and, among syntenic genes, +3%.

## R4 L1c (integrated 2026-10-13)
`research/checks/results/R4-L1c.md`. Descriptive addition to the credit, no value change: on the real CSAC 2005 list, ALL / CSAC23 = 1.24 and NOT23 - CSAC23 = +0.126 (CSAC23 0.219 on 12,724 mapped genes; NOT23 0.344). A gene-set effect in Day's direction is also what a quality selection of genes gives (reading a-broad of DN6, credited here and not scored there). DN3 external and internal not moved.
