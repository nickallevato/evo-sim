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
  internal: pending   # method unreleased (no code, gene list or per-gene table; Zenodo paper promised, Q176). R4 L1 fix pass (reviewed a352991): no correct-frame computation on any gene set, estimator or filter reproduces 0.80 (0.15-0.45); ¶12 'The code is correct. The data is complete. The number is real.' is an N2d candidate (the diagnostics test neither frame, strand nor orthology), limited by N1; slip S-DN1-1 (implied N/S 3.55 vs 3.34) ledgered
  fidelity: n/a   # Day's own computation
  external: contradicted   # conditional on L1b (like-for-like T2T rerun not yet run), see criticality/METHOD-AUDIT-2026-10-12.md MA-12. R4 L1 fix pass; verdict set at integration: hg38/panTro5: all genes 0.271, one2one 0.207; Day's own single-SNV count ratio 2.52 vs 0.85 in correctly aligned CDS (estimator-free; no assembly change raises it); T2T cannot add genes (20,400 < 23,183). Open: the alignment-level route (ALL is syntenic-net aligned). L1b overturns only if a T2T CDS extraction vs mPanTro3 gives >= 0.65 and share >= 66% on genes passing a synteny/orthology check
---

## Statement (verbatim)
> We used GENCODE v46 annotations, the same Nei-Gojobori method the original studies used, and the complete extraction of human-chimp aligned positions from the T2T-quality assemblies. And we got a result.

> Not 0.23. 0.80.

> We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46 that has coding sequence data in the human-chimp alignment.

> Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for single-SNV codons alone.

> The code is correct. The data is complete. The number is real.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11 (modified 16:35 UTC the same day), ¶7, ¶9, ¶13 and ¶12 (diagnostics and the closing sentence) (Q172, Q173, Q174). RH tag: dialectic (numeric claims). The surrounding "What. The. Fuck?" and "Unlike properly credentialed scientists" are rhetoric (RH-21, `ledgers/slips.md`).

## Formal statement
dN/dS = (Nd/N)/(Sd/S) over 20,400 genes, Nei-Gojobori sites and differences; aggregation (pooled vs mean of ratios), multiple-hit correction, filters and the CDS extraction route are unstated. Implied by Day's two single-SNV numbers: N/S = (71.6/28.4)/0.71 = 3.55 (R4 L1: a correct NG site ratio is 3.34).

## Assumptions
- Stated: synonymous changes are a neutral baseline; the T2T alignment extraction is complete (226 M positions on chr1; 98.8% of coding positions found).
- Implicit: codons are read in the annotated frame and strand for every gene; aligned positions are orthologous.

## Responses
- Against (audit, R4 L1, fix pass): see Check. Day's single-SNV codons give 2.52 nonsynonymous per synonymous; correctly aligned human-chimp CDS give 0.85 and unconstrained sequence about 3. A raw count needs no estimator. No critic has replied yet (refresh-2026-10-11).
- In support (Day): his diagnostics (codon classification samples, single-SNV codons) were reported, the single-SNV one is estimator-free and closes the critics' easy explanations (site normalisation, averaging), and he states the result is provisional ("It’s a little too soon to say that I am absolutely confident in our present results", ¶22; recorded for balance, not R1d, since ¶12 says "The number is real").
- Weaknesses in the responses: L1 is not T2T; its 'all genes' set is already orthology-filtered at the alignment level (syntenic nets), so Day's complete-extraction route and paralog projection are untested (L1b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 (Ka/Ks 0.23, 13,454 genes) | not read (DN5) | pending |

## Pre-registered prediction
`research/checks/l1_dnds_genesets.py` (868bb60): Day side O121 ~0.23 and ALL ~0.80; critic side ALL <= 0.35.

## Check
R4 L1 (`research/checks/results/R4-L1.md`; three reviews a352991; fix pass): pooled dN/dS 0.271 (all genes), 0.207 (one2one); single-difference nonsyn share 45.8% (Day 71.6%); every filter combination 0.23-0.28; per-gene mean 0.25-0.44 and median 0.15-0.31 on a correct frame. No gene-level frame-error mixture fits Day's filter report (it leaves 2,253-3,045 genes at 0.24-0.26 in the full stack; withdrawn). An unidentified extraction/alignment problem inside nearly every gene fits his numbers; the one tested instance is a chimp-only frame shift downstream of a random point (pooled 0.845, share 72.7%, no stack below 0.756; post hoc), not a finding about his code. **Integrated 2026-10-11 (review #56-#58):** internal pending (method unreleased), fidelity n/a, external contradicted (gene-list and correct-frame versions; the alignment-level T2T route stays open, L1b).

## Simulator variables implied
- none (an empirical summary statistic; the simulator would need per-site selection classes to predict it)

## R-refresh 2026-10-12
Day's follow-up "The Method is the Conclusion" (2026-10-12) restates the figure as 0.7989 on 20,400 genes with subset rows 0.7956, 0.7939 (nested) and 0.8237 and a uniform 73.8-74.4% nonsynonymous share (Q183, Q184). Verdicts unchanged: internal `pending` (no code, gene list or per-gene table; Zenodo still 39 records), external `contradicted` (L1). Refresh maths review: all rows imply one constant N/S of about 3.54, so the uniformity restates one dN/dS, it is not independent evidence; 74% nonsynonymous is close to the no-constraint expectation (~75-78% of sites), which alignment noise also produces. Credit: the rows are mutually coherent. Day now attributes the gap to alignment method, not gene curation (DN6, DN3 R-refresh). Pending: L1c.
