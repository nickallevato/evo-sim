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
  external: supported   # R4 L1 fix pass; verdict set at integration: (in kind): an independent pipeline gives 0.207 on Ensembl one2one genes (release 116) and 0.200 with CSAC-like quality filters; fidelity waits for CSAC 2005 and an independent ML estimate to be fetched (critic-side review #3) R4 L1b (2026-10-13): stays `supported`; Ensembl one2one genes on the T2T assemblies read 0.238 (0.208 with CSAC-like quality filters; 0.209 syntenic), inside the registered 0.18-0.30.
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

## R4 L1b (integrated 2026-10-13)
`research/checks/results/R4-L1b.md` (pre-registered 0fe3c7f; pre-run notes 5e64f0a; reviews #70-#72: 3415770, e163ca2, 8c34996; fix pass 098ac12; post hoc `l1b_posthoc_x1_breakdown.py` 9c4a359). T2T rerun: GENCODE v35 CAT on hs1 against mPanTro3, Cactus MAF, Nei-Gojobori pooled, bases paired by alignment column. Band CRITIC.

O121 (Ensembl one2one) reads 0.238 on the T2T pipeline (0.208 with CSAC-like quality filters; 0.209 syntenic), inside the registered 0.18-0.30; external `supported` stays. Fidelity `accurate` not moved (the independent ML estimate and the CSAC SI criteria are still outstanding). **Day:** he relayed 0.23 correctly and it is reproduced in kind on the assemblies he names. **Critics:** 0.23 is reproduced a second time, from a nucleotide genome alignment.

## R4 L1c (integrated 2026-10-13)
`research/checks/results/R4-L1c.md`; DN5 not moved. The real-list value is 0.219 at kappa = 1 and about 0.265 at CSAC's own site ratio (N/S 2.78), so like for like the audit reads 15% above the published 0.23, inside the registered range. The kappa line is offered as a possible DN5 comment; no rule licenses a move. The published row's 0.2300 and "~40%" nonsynonymous share (Day's Q184) are both reproduced with no protein step (0.219, 42.6%). CSAC 2005 used the BLASTZ genome alignment for the 13,454 genes (quotes-literature.md, CSAC2005, Methods, Genome alignment).
