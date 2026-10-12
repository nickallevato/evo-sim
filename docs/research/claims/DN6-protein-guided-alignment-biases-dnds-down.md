---
id: DN6
title: "Day: the protein-guided CDS alignment method has a circular reasoning problem: divergent codons are gapped out, so dN/dS is biased downward (the 2005 Consortium's 0.23 is called a methodological artefact)"
side: day
branch: ROOT
parent: DN1
edges: [{type: revises, target: DN3}, {type: depends-on, target: DN1}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: pending   # mechanism stated without code, excluded-codon count or example gene (Q180-Q182); testable by one number (codons kept by the Cactus extraction but dropped by a protein-guided aligner, and their dN/dS). Pre-registered test: L1c (l1c_alignment_method.py, 536b19b), not yet run
  fidelity: pending   # the claim about CSAC's own method is Reading a; CSAC 2005 methods text now held (2026-10-12) and does not describe a protein-guided realignment for the 13,454 set (see Readings); the verdict field takes Reading b
  external: pending   # reading-dependent: Reading a (this is how CSAC's 0.23 was produced) is contradicted by the CSAC methods text; Reading b (protein-guided pipelines in general bias dN/dS down) is pending L1c. Verdict field takes b, the reading most defensible to Day (rule RD)
---

## Statement (verbatim)
> discovered that the protein-guided CDS alignment method has a circular reasoning problem that's impossible to ignore once you recognize it:

> Regions too divergent to score well get gapped out or are left unaligned, so they aren't counted.

> Those excluded codons are enriched for nonsynonymous substitutions by definition, because that's why they scored poorly in the protein alignment.

> The difference is not a matter of gene selection, quality filtering, or computational error. It is a methodological artifact of using a conservation-dependent alignment to measure conservation.

Source: [Day, "The Method is the Conclusion"](https://voxday.net/2026/10/12/the-method-is-the-conclusion/), 2026-10-12 14:12:35 UTC, ¶3, ¶7, ¶10, ¶15 of the non-empty paragraphs (Q180, Q181, Q182, Q186). RH tag: dialectic (a mechanism with an observable). "Impossible to ignore" is rhetoric (intensifier, no verdict).

## Formal statement
Let A be the set of aligned codons from a nucleotide/genome alignment (Cactus, no protein scoring) and P the subset kept by a protein-guided aligner (BLOSUM-type scoring, gaps). Claim: dN/dS(P) < dN/dS(A) because A minus P is enriched for nonsynonymous change. Observable: |A minus P| / |A| and dN/dS(A minus P). Day does not give either; Q181's premise requires that human-chimp protein sequences (about 99% identical, not verified by Day) have enough divergent stretches to matter.

## Assumptions
- Stated: the pipeline behind the published 0.23 is a protein-guided CDS alignment (Q180, Q186: "the original studies").
- Implicit: excluded codons are diverged real orthologous sequence, not misaligned paralogs or assembly error (the alternative reading of a poor score; then they carry no information about selection and the 0.80 would be a noise floor, cf. the refresh maths review 5).

## Readings (rule RD)
| Reading | Content | Verdict | Basis |
|---|---|---|---|
| a | "This is how the Consortium's 0.23 was produced." | external `contradicted` as a statement about CSAC 2005; fidelity `misread` for the method description | CSAC 2005 Methods, Gene annotation: 16,045 genes "indirectly aligned to the chimpanzee sequence via the genome alignment"; Clustal W "for the lineage-specific analyses" on a 7,043-gene subset only; K_A/K_S for a set is a pooled (summed) ratio. Quotes in `quotes-literature.md` (CSAC2005). Residual in Day's favour: the 13,454 were chosen for "high-quality sequence alignments covering virtually the entire coding region", so alignment quality did select the genes (a gene-set effect, but Q186 itself rules out "gene selection") |
| b | "Protein-guided alignment pipelines in general (and later ones in particular) gap out divergent codons and so bias dN/dS downward." | external `pending` (L1c decides; the bias direction is plausible for deep comparisons, its size at 1.2% divergence is unmeasured) | Refresh maths review 7: legitimate hypothesis, falsifiable, one number needed |
| c | "The 0.80 (not the 0.23) is the correct value." | out of scope here (DN1, external contradicted) | |

Verdict field: reading b (most defensible to Day). Counted as reading-dependent.

## Responses
- Against (audit): the CSAC methods text contradicts Reading a; at about 1% nucleotide divergence a gap penalty should drop few codons; Day's own filter stack leaving 10 genes (Q175) suggests a noisy extraction, so excluded codons may be misalignments, not diverged orthologs; N/S in Day's rows is a constant 3.54 (refresh maths review 2).
- In support (Day, credit): a clearly stated, falsifiable mechanism that names the deciding observable; he changed his explanation after his own gene-set test failed (Q185, Q186), recorded in `ledgers/versions.md`; the hypothesis direction is recognised for deep comparisons.
- Weaknesses in the responses: the audit has not yet measured the excluded-codon share on human-chimp (L1c pre-registered, not run); the CSAC genome alignment is itself an upstream step whose artefact filter ("removing low-quality sequences and likely alignment artefacts") is not described numerically.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 Methods, Gene annotation | "were indirectly aligned to the chimpanzee sequence via the genome alignment" ; "realigned using Clustal W158 for the lineage-specific analyses" (7,043-gene subset) | Reading a: misread (method); reading b: n/a |
| CSAC 2005 Methods, Rates of divergence | "K A/K S for a set of genes was calculated by summing the number of substitutions and the number of sites" | estimand = pooled; N S/N A = 0.36 (N/S 2.78) is stated for the divergent-vs-polymorphic comparison |

## Pre-registered prediction
`research/checks/l1c_alignment_method.py` (536b19b): bands DAY / HIGH-NOT-METHOD / NOISE / MIDDLE / CRITIC; Day side: protein-guided arms P/PG give dN/dS well below the unguided Cactus-style arm U0 with excluded codons enriched for nonsynonymous change; critic side: arms agree within noise and the excluded share is small.

## Check
Pending: L1c (queued after `ph` and L1b). Gene list now held: CSAC 2005 Table S23 (13,454 RefSeq NM_ ids, `bib-literature.md`, 2026-10-12).

## Simulator variables implied
- none
