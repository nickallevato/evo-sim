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
  external: contradicted   # reading-dependent: (A) 0.80 is a property of the genomes: `contradicted` (sets the field; Q172 says 'aligned positions' and Q173 sets 0.80 against 0.23 as one quantity); (B) 0.80 is a report of what an ungapped comparison of the extracted sequence yields: reproduced in kind by L1b's X1 arm (0.853 pooled), identity with his pipeline `untestable` until code or per-gene table is released (not field-setting: a different object, the output of a pipeline); (C) the value depends on the alignment method (Q180-Q186): not tested by L1b, tested by L1c (DN6). Readings table in the R4 L1b paragraph. the MA-12 condition on L1b (criticality/METHOD-AUDIT-2026-10-12.md) is discharged for this alignment and annotation by R4 L1b (integrated 2026-10-13, reviews #70-#72): now on T2T and Cactus as well (the 'different assembly / complete extraction' route is closed for this alignment): hs1-referenced Cactus MAF, GENCODE v35 CAT, alignment-column extraction, Nei-Gojobori pooled; V0 ALL 0.271, SYN 0.209 (registered band CRITIC). R4 L1 fix pass; verdict set at integration: hg38/panTro5: all genes 0.271, one2one 0.207; Day's own single-SNV count ratio 2.52 vs 0.85 in correctly aligned CDS (estimator-free; no assembly change raises it); T2T cannot add genes (20,400 < 23,183). Open: the alignment-level route (ALL is syntenic-net aligned). [SUPERSEDED 2026-10-13 (MA-28 ii): L1b was run and its registered sentence applied as written; see the "R4 L1b" paragraph below. Kept as history:] L1b overturns only if a T2T CDS extraction vs mPanTro3 gives >= 0.65 and share >= 66% on genes passing a synteny/orthology check Post hoc (L1b, not licensed by the registration, separate from the registered sentence): a position-by-position extraction of the first chimp row of the same data, which does not compare aligned positions after the first length difference, reads 0.853 pooled (share 60.1%, per-gene median 0.189), carried by 13.7% of genes; a candidate error class with a real-data instance, not shown to be his pipeline (LOCATED not licensed). The codons this alignment leaves out (1.16%) are bounded, not tested, by L1b; L1c bounds them further (Reading d).
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

## R4 L1b (integrated 2026-10-13)
`research/checks/results/R4-L1b.md` (pre-registered 0fe3c7f; pre-run notes 5e64f0a; reviews #70-#72: 3415770, e163ca2, 8c34996; fix pass 098ac12; post hoc `l1b_posthoc_x1_breakdown.py` 9c4a359). T2T rerun: GENCODE v35 CAT on hs1 against mPanTro3, Cactus MAF, Nei-Gojobori pooled, bases paired by alignment column. Band CRITIC.

V0 ALL 0.271 (19,310 genes), one2one 0.238, syntenic 0.209; 0.246-0.293 under every chimp-row choice (VS, VR, VL); 0.214-0.283 over all 32 filter stacks; single-difference nonsynonymous share 40-47% against Day's 71.6%. All six critic-side predictions hit.

**Readings of Q172-Q173 (rule RD; post hoc table, integrated 2026-10-13).**
| reading | tag | external under that reading | basis |
|---|---|---|---|
| A: 0.80 is a property of the genomes (human-chimp coding dN/dS on the T2T assemblies) | dialectic | **`contradicted`** on this alignment and annotation (sets the field) | V0 ALL 0.271, SYN 0.209; 0.246-0.293 under every chimp-row choice; registered band CRITIC |
| B: 0.80 is a report of what an ungapped comparison of the extracted sequence yields | dialectic | reproduced in kind by X1 (0.853 pooled; O121 0.844, NON121 0.898, the ordering of his Q184 rows); identity with his pipeline `untestable` until code or per-gene table is released | post hoc; X1 misses his share on ALL (60.1%) and, under S, his filter floor |
| C: the value depends on the alignment method (Q180-Q186) | dialectic | not tested by L1b; tested by L1c, band CRITIC (DN6) | DN6 |

The field takes A: Q172 says "aligned positions", Q173 sets 0.80 against 0.23 as one quantity, and Q176-Q177 draw conclusions about the genome from it; B changes the object to the output of a pipeline, which RD treats as an extended reading (and what his pipeline did is the internal field's question, `pending`). The other way, stated because it is arguable: "we got a result ... 0.80" is closest to literally true as a report of his computation (nobody disputes his code printed about 0.80); if B were held a plain reading, B's value (`untestable` until release) would go in the field with A beside it. Counted as reading-dependent.

**The registered sentence stays as registered**, scoped to "this alignment" (hs1-referenced Cactus MAF, GENCODE v35 CAT, an alignment-column extraction, one estimator). It is neither narrowed nor broadened; X1 is in a separate post hoc sentence in the external comment.

**Both (X1; the audit's own missed prediction A4, credited to neither side).** The audit predicted X1 at 0.28-0.60; it read 0.853 pooled (share 60.1%, per-gene median 0.189), carried by 13.7% of genes (the other 86% read about 0.205, the affected 14% about 0.96-1.00, the value for codons paired out of register). Post hoc breakdown of X1's excess by first cause: an in-frame indel 55.7%, a coverage hole 28.8%, a frame-changing indel 8.4%, an exon edge 7.1%. Day's half: a simple pipeline reads 0.85 on the assemblies he names, so his number is reproducible in kind on these data, which the audit did not expect. Critics' half: the excess is a matter of what is paired with what, in 14% of genes. Counterpoint: the affected-gene single-difference share (73-74%) is also what pairing without constraint gives under either explanation, so it identifies a class, not his pipeline, and X1 on its whole set misses his share, his single-difference ratio (0.84 against his 0.71) and, under S, his filter floor. Wording: a candidate error class with a real-data instance; LOCATED is not licensed.

**Who this helps: Day.** He named testable assemblies; his O121-type expectation (~0.23) is met at 0.238; the gene-set effect has his sign on T2T; his completeness statement ("98.8% of coding positions are found", Q272) is reproduced (98.87% of CDS bases, 98.84% of codons); his five filters are the five the audit ran; his near-empty strict stack (10 genes) is reproduced under the literal reading of his stop filter (9 genes), so that part of his report is not evidence of a fault; his Q184 table is internally coherent. The 129,092 codons (1.16%) a column-paired count leaves out are bounded here only to 0.56-0.85 (if each held one or two nonsynonymous differences); L1c bounds them further. **Who this helps: critics.** On the T2T assemblies he names, with bases paired by alignment column, 0.25-0.29 under every chimp-row choice; the "different assembly" and "complete gene set" routes to 0.80 are closed for this alignment and annotation (paralog choice adds at most 0.022; non-one2one genes would need a pN/pS of 3.95; the 1,090 genes not in the set about 10); the typical gene reads 0.15-0.16 and fewer than one gene in ten reaches 0.65; on Day's own table the all-genes against 1:1-orthologs gap is +0.003, so the disagreement sits inside the one2one set (0.7956 against 0.238). Verdicts: internal `pending`; fidelity `n/a`; external `contradicted`, no value change. Open: his per-gene table (Q176); GENCODE v46 on hs1.

## R4 L1c (integrated 2026-10-13)
`research/checks/results/R4-L1c.md`; not moved by L1c. Reading C above is tested there: no realistic protein-guided arm moves the value by more than 6%, and the published 0.23 was not made by a protein-guided alignment (DN6). Day's reading d (the Cactus alignment is itself a conservation-dependent step) is open and bounded, not tested: the 1.40% of codons no arm sees would need pN 0.67 to reach 0.80, but a rise of order 10% is open.
