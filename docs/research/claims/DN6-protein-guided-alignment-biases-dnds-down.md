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
  internal: pending   # mechanism stated without code, excluded-codon count or example gene (Q180-Q182); testable by one number (codons kept by the Cactus extraction but dropped by a protein-guided aligner, and their dN/dS). Pre-registered test: L1c (l1c_alignment_method.py, 536b19b), run 2026-10-13: supplies the dropped-codon count and dN/dS for the audit's aligner only (Cactus-paired codons, in-script aligner); not moved
  fidelity: misread   # reading-dependent: R4 L1c (integrated 2026-10-13, reviews #73-#75). Fidelity asks what the cited source did, so only reading a speaks to it: the held CSAC 2005 Methods say the 13,454-gene set came from the BLASTZ genome alignment ("were indirectly aligned to the chimpanzee sequence via the genome alignment"; "BLASTZ154 was used to align non-repetitive chimpanzee regions against repeat-masked human sequence"), Clustal W only for a 7,043-gene subset; Day's Q274 says "what the Consortium's method actually measured is: among the coding positions conserved enough to survive protein alignment". Strict reading a: `misread`. Broad reading a-broad (any conservation-dependent selection behind the 13,454, Q186; CSAC removed "low-quality sequences and likely alignment artefacts"): `partial` or `unverifiable` until the SI criteria are held. Licensed by the held text before the run (docstring pre-run note), not by the run. Counted as reading-dependent
  external: contested   # reading-dependent: field takes reading b2 (mechanism and direction as Q180-Q182 are worded; the reading under which the quoted statements are most defensible, rule RD). Size first: the realistic arms lower dN/dS by 2% to 6% on all genes and 1% to 4% on the real 2005 list, against 71% needed to go from 0.271 to 0.80; direction is Day's in every arm (dropped codons nonsynonymous-enriched, 0.71-0.85 against 0.479). Scope: this genome alignment (hs1 / mPanTro3 Cactus), this annotation (GENCODE v35, human frame projected onto chimp) and the audit's in-script aligner; no external codon aligner, no independent chimp CDS. b1 (the published human-chimp 0.23 is a material protein-guided artefact) `contradicted`; reading a `contradicted`; a-broad not scored here (a gene-set effect credited to DN3); reading d (the genome alignment is itself the conservation-dependent step) extended and NOT tested. Registered rule for Reading A: invalid as registered (BLOCKER-1); the amended `contested` is the result of record. Not to be strengthened past `contested` until an external codon-aware pipeline from an independent chimp CDS has been run (at least on the 2,765 genes with indels or holes). Counted as reading-dependent
verdict_scope:
  external: "Scope: this genome alignment (hs1 / mPanTro3 Cactus), this annotation (GENCODE v35, human frame projected onto chimp) and the audit's in-script aligner; no external codon aligner, no independent chimp CDS."
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

## Readings (rule RD; updated by R4 L1c, integrated 2026-10-13)
| reading | content | external | fidelity | sets a field? |
|---|---|---|---|---|
| a | "This is how the Consortium's 0.23 was produced" (a protein-guided alignment). Q180 + Q182 + Q184 + Q186 jointly; said outright in Q274 | `contradicted` (held CSAC text; U0 reproduces 0.219 / 42.6% on the real list with no protein step) | **`misread`** | fidelity: yes |
| a-broad | "A conservation-dependent alignment" (Q186) means any selection on alignment quality behind the 13,454 ("After removing low-quality sequences and likely alignment artefacts") | not scored here: a gene-set effect, credited to DN3 (real list 0.219 against 0.271 on all genes; NOT23 0.344) | `partial` or `unverifiable` until the SI criteria are held | no (the less defensible reading of Q186, which says "not a matter of gene selection, quality filtering") |
| b1 | "At human-chimp divergence, protein-guided alignment lowers dN/dS by a material amount; the published 0.23 is this artefact" | **`contradicted`** on this alignment, annotation and in-script aligner: realistic arms 2.3% to 5.8% (ALL), 1.3% to 3.7% (real list), all flags `none`; R1's line is 25%; 71% needed | n/a | no |
| b2 | "Protein-guided alignment excludes divergent codons, those codons are nonsynonymous-enriched, and dN/dS is lowered" (Q180-Q182 as written: mechanism and direction, no size) | **`contested`**: direction true in every arm; size 2% to 6%; 35% from the audit's stress arm (PAF2, dropped codons dS-normal on clean genes); large on synthetic near-total replacement runs; not tested from an independent chimp CDS or with an external aligner | n/a | **external: yes** |
| b2 as registered | the same, scored by the registered rule | "invalid as registered (BLOCKER-1)" as printed; `supported` only by substituting PAF2 for PF2 (the write-up's derivation) | n/a | no: shown beside the result of record, with the docstring's precedence sentence as the reason |
| c | "The 0.80 (not the 0.23) is the correct value" | out of scope here (DN1, external `contradicted`) | | |
| d | "The genome alignment that feeds the audit's U0 is itself the conservation-dependent step" | **extended; not tested by L1c.** Bounded: cannot carry 0.80 or 0.65 unless the left-out 1.40% of annotated sense codons reads like unrelated sequence (pN 0.67 needed); a rise of the order of 10% is open. Day's own post exempts the step (Q273); CSAC's 13,454 also came from a genome alignment (BLASTZ). Test: follow-up (b), not run | n/a | no: a different object from the protein alignment of Q180 and Q182 |

Verdict fields: external takes b2, fidelity takes a; each answers its own question. Both counted as reading-dependent (two reading-dependent verdicts). The earlier version of this file had fidelity follow reading b (`n/a`); the L1c fix pass proposed the split and it is applied here.

## Responses
- Against (audit): the CSAC methods text contradicts Reading a; at about 1% nucleotide divergence a gap penalty should drop few codons; Day's own filter stack leaving 10 genes (Q175) suggests a noisy extraction, so excluded codons may be misalignments, not diverged orthologs; N/S in Day's rows is a constant 3.54 (refresh maths review 2).
- In support (Day, credit): a clearly stated, falsifiable mechanism that names the deciding observable; he changed his explanation after his own gene-set test failed (Q185, Q186), recorded in `ledgers/versions.md`; the hypothesis direction is recognised for deep comparisons.
- Weaknesses in the responses: the audit has not yet measured the excluded-codon share on human-chimp (L1c pre-registered, not run); the CSAC genome alignment is itself an upstream step whose artefact filter ("removing low-quality sequences and likely alignment artefacts") is not described numerically.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 Methods, Genome alignment | "BLASTZ154 was used to align non-repetitive chimpanzee regions against repeat-masked human sequence" (BLAT for the more repetitive regions; chained; "only best reciprocal alignments were retained") | Reading a: misread (method) |
| CSAC 2005 Methods, Gene annotation | "were indirectly aligned to the chimpanzee sequence via the genome alignment" ; "realigned using Clustal W158 for the lineage-specific analyses" (7,043-gene subset) | Reading a: misread (method); reading b: n/a |
| CSAC 2005 Methods, Rates of divergence | "K A/K S for a set of genes was calculated by summing the number of substitutions and the number of sites" | estimand = pooled; N S/N A = 0.36 (N/S 2.78) is stated for the divergent-vs-polymorphic comparison |

## Pre-registered prediction
`research/checks/l1c_alignment_method.py` (536b19b): bands DAY / HIGH-NOT-METHOD / NOISE / MIDDLE / CRITIC; Day side: protein-guided arms P/PG give dN/dS well below the unguided Cactus-style arm U0 with excluded codons enriched for nonsynonymous change; critic side: arms agree within noise and the excluded share is small.

## Check
R4 L1c (see the paragraph below). Earlier: pending L1c. Gene list now held: CSAC 2005 Table S23 (13,454 RefSeq NM_ ids, `bib-literature.md`, 2026-10-12).

## Simulator variables implied
- none

## R4 L1c (integrated 2026-10-13)
`research/checks/results/R4-L1c.md` (pre-registered 536b19b, amended post hoc before any data, 0e0e840; main run and synthetic `transfer` on na-workhorse; reviews #73-#75: 3429895, 02b87c6, 8742998; fix pass 140a69a; post hoc `transfer-excl` 6c5d8cf, 40e4021). Band **CRITIC** on the registered and the amended rule. Scope of every sentence: this genome alignment, this annotation, the audit's in-script aligner (Cactus-paired codons re-paired by a Gotoh aligner, BLOSUM62).

**Who this helps: Day.** Q182 is right in direction on real data: dropped codons are nonsynonymous-enriched in every arm (0.71-0.85 against 0.479) and every realistic arm lowers dN/dS. A strict protein-score filter is not harmless: PAF2 removes 0.92% of codons and 37% of all nonsynonymous differences and lowers the estimate by a third, on dS-clean gene sets as well; any pipeline with a filter of that kind would understate dN/dS by a material amount (qualifier: none is shown to use one). On synthetic genes with near-total replacement of 15-residue runs the lenient trim and the Gblocks rule read 55% to 65% below truth: the mechanism exists in principle. On a register-broken extraction the protein family lowers 0.85 to 0.34 or 0.19, so his observation that two kinds of pipeline disagree widely is reproducible; the dispute is over which input is right. The registered rule would have scored Reading A `supported` once a valid strict arm stood in for the invalid one; the `contested` comes from an amendment after a miniature had shown that outcome. A gene-set effect exists on the real list (+24%, NOT23 0.344). The site model matters: 0.271 becomes 0.385 at kappa-hat, and the real list reads about 0.265 at CSAC's own site ratio, above 0.23. The 1.40% of annotated sense codons no arm sees (351 genes) are not bounded to nothing: a rise of the order of 10% is open (reading d). Not run: an external codon aligner or an independent chimp CDS (follow-up (b)).

**Who this helps: critics.** The published 0.23 was not made by a protein-guided alignment: the held CSAC text gives a BLASTZ genome alignment for the 13,454 genes and Clustal W only for the 7,043-gene subset; this needs no simulation (fidelity `misread` on reading a). The low value needs no protein guidance on these data: U0 reads 0.271 on all genes, 0.238 on one2one, 0.219 on the 12,724 mapped genes of the real list (nonsynonymous share 42.6% against Day's own row 0.2300 and ~40%). Whatever the realistic arms remove, signal or error, is 2% to 6% on all genes and 1% to 4% on the real list, against the 71% the claim needs; under 1% in genes with no length difference. Synthetic: with no or moderate clustering the realistic arms return the truth (one exception, PAF1), and the naive arm reads 0.81 to 0.83 at a truth of 0.22 with correctly gapped indels in 15% of genes; every route to 0.80 the audit constructed is an error model (L1b's counterpoint stands beside it: the 74% nonsynonymous share is also what unconstrained sequence gives). "Day's pipeline is register-broken" is a candidate only.

**Against the critics.** The sign is Day's in every arm, so the reading of the mechanism and direction is `contested`, not `contradicted`. The uncorrected like-for-like is not theirs to claim: at CSAC's site ratio the real list reads 0.265, above 0.23. "The aligner question is closed" is not shown (no external codon aligner).

**Against the audit.** The registered protein arm was invalid (BLOCKER-1); the four registered critic-side predictions naming it fail on it and hold on the valid arm. The amended x discriminator does not separate a saturated real run from misalignment; the amended Reading A had two outcomes and could not come out `contradicted`, the registered one could not come out other than `supported`. Misses: A10 (PA not neutral under extreme clustering), N/S at kappa-hat, CSACp against ALL, UT 0.853. Q183 (uniform nonsynonymous fraction) has no registered rule and is not scored.

**Verdicts applied (rule RD).** External `contested` (reading b2); fidelity `misread` (reading a); internal `pending`. Each reading is in the Readings table above. DN1 and DN3 not moved by L1c; the real-list gene-set figures (ALL / CSAC23 = 1.24, NOT23 - CSAC23 = +0.126) are added to DN3's credit as description. Open: follow-up (b); PAF1 to PAF2 threshold dose-response; Day's per-gene table, excluded-codon count and the CSAC SI criteria.
