---
id: DN1
title: "Day and Athos: genome-wide human-chimp dN/dS = 0.80 on 20,400 GENCODE v46 genes (Nei-Gojobori, T2T alignment), not 0.23"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}]
load_bearing: false  # new 2026-10-11 data claim; feeds DN4; not among the R5 ROOT-path nodes
sourcing: firsthand
status: checked
verdicts:
  internal: pending   # method unreleased (no code, gene list or per-gene table; Zenodo paper promised, Q176). R4 L1 (awaiting review): no correct-frame Nei-Gojobori computation on any gene set reproduces 0.80 (0.20-0.45); Day's own single-SNV share 71.6% matches out-of-frame reading (~80% of genes broken, post hoc); not scored until the method is released
  fidelity: n/a       # Day's own computation
  external: pending   # R4 L1 (awaiting review): all knownCanonical genes 0.271, Ensembl one2one 0.207 (hg38/panTro5); T2T + GENCODE v46 rerun queued (L1b). Proposed after review: contradicted on hg38, pending on T2T
---

## Statement (verbatim)
> We used GENCODE v46 annotations, the same Nei-Gojobori method the original studies used, and the complete extraction of human-chimp aligned positions from the T2T-quality assemblies. And we got a result.

> Not 0.23. 0.80.

> We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46 that has coding sequence data in the human-chimp alignment.

> Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for single-SNV codons alone.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11 (modified 16:35 UTC the same day), ¶7, ¶9, ¶13 and ¶12 (diagnostics) (Q172, Q173, Q174). RH tag: dialectic (numeric claims). The surrounding "What. The. Fuck?" and "Unlike properly credentialed scientists" are rhetoric (RH-21, `ledgers/slips.md`).

## Formal statement
dN/dS = (Nd/N)/(Sd/S) over 20,400 genes, Nei-Gojobori sites and differences; aggregation (pooled vs mean of ratios), multiple-hit correction, filters and the CDS extraction route are unstated. Implied by Day's two single-SNV numbers: N/S = (71.6/28.4)/0.71 = 3.55 (R4 L1: a correct NG site ratio is 3.34).

## Assumptions
- Stated: synonymous changes are a neutral baseline; the T2T alignment extraction is complete (226 M positions on chr1; 98.8% of coding positions found).
- Implicit: codons are read in the annotated frame and strand for every gene; aligned positions are orthologous.

## Responses
- Against (audit, R4 L1, awaiting review): see Check. No critic has replied yet (refresh-2026-10-11).
- In support (Day): his diagnostics (codon classification samples, single-SNV codons) were reported, and he states the result is provisional ("It's a little too soon to say that I am absolutely confident in our present results").
- Weaknesses in the responses: L1 is not T2T; paralog projection in a whole-genome extraction is untested (L1b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 (Ka/Ks 0.23, 13,454 genes) | not read (DN5) | pending |

## Pre-registered prediction
`research/checks/l1_dnds_genesets.py` (868bb60): Day side O121 ~0.23 and ALL ~0.80; critic side ALL <= 0.35.

## Check
R4 L1 (`research/checks/results/R4-L1.md`, awaiting review): pooled dN/dS 0.271 (all genes), 0.207 (one2one); single-difference nonsyn share 45.8% (Day 71.6%); every filter combination 0.23-0.28; frame errors on ~80% of genes reproduce 0.80 and 72% together (post hoc), but not the "10 remaining genes".

## Simulator variables implied
- none (an empirical summary statistic; the simulator would need per-site selection classes to predict it)
