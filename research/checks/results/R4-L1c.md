# R4 L1c: does the alignment method manufacture a low human-chimp dN/dS? Day's "protein-guided alignment gaps out divergent codons" tested on the T2T codons of L1b

**Status: main run and synthetic `transfer` table done; three post-run reviews done (correctness 3429895, steelman-day 02b87c6, steelman-critic 8742998); fix pass done 2026-10-13 (last section answers every MAJOR and MINOR by id); NOT integrated.** Band **CRITIC** on the registered rule and on the amended rule, on both source sets. Tier: not load-bearing by the ROOT path (docstring, TIER), kept at three reviews because it decides DN6's external verdict. No verdict value in any claim file is changed by this file; everything about verdicts is a proposal for integration.

**Scope of every conclusion below:** this genome alignment (hs1 / mPanTro3 Cactus), this annotation (GENCODE v35 lifted to hs1, human frame projected onto chimp) and the audit's in-script aligner. Where a sentence omits the three qualifiers they still apply.

**Two results that need no simulation, stated first (fix pass; critic review finding 2, Day review finding 8):**
1. *Fidelity (proposal `misread`, reading-dependent).* The held CSAC 2005 text gives the method behind the published row: the transcripts "were indirectly aligned to the chimpanzee sequence via the genome alignment" (Methods, Gene annotation, CSAC2005.txt ~l.1996); "BLASTZ154 was used to align non-repetitive chimpanzee" sequence and "only best reciprocal alignments were retained" (Methods, Genome alignment, l.1982-1985; verified against the held text in this pass, not yet in `quotes-literature.md`); "A subset of 7,043 of these genes ... were realigned using Clustal W158 for the lineage-specific analyses" (~l.2000-2002); the 0.23 is "the value of 0.23 obtained with all human–chimpanzee orthologues" (~l.891). What Day's filed quotes say: Q180 names "the protein-guided CDS alignment method"; Q182 says the excluded codons "scored poorly in the protein alignment"; Q186 says "The difference" (0.7989 against the row "Published (Consortium 2005)13,4540.2300~40%", Q184) "is a methodological artifact of using a conservation-dependent alignment to measure conservation". No single filed quote says in so many words that the Consortium aligned proteins; the attribution is the conjunction of Q180, Q182, Q184 and Q186. The same post does say it in one sentence that is held locally but not yet filed as a numbered quote (¶14 of the non-empty paragraphs, 2026-10-12 14:12:35 UTC): "So what the Consortium’s method actually measured is: “among the coding positions conserved enough to survive protein alignment, how conserved are they?”". Strict reading (the published 0.23 came from a protein-guided alignment): `misread`. Broad reading (Day review: "a conservation-dependent alignment" means any alignment-quality selection behind the 13,454): `partial` or `unverifiable` until the SI criteria for "removing low-quality sequences and likely alignment artefacts" are held. Both are in the Readings table under "Proposed verdict moves".
2. *Both figures of Day's "Published" row are reproduced with no protein step.* U0 on the 12,724 mapped genes of the real 2005 list reads 0.219 with a nonsynonymous fraction of 0.426, against 0.2300 and "~40%" (Q184). Like for like against CSAC's estimator the value is about 0.265 (at CSAC's site ratio N/S 2.78; post hoc), 15% above the published figure and inside the registered 0.18-0.30 range. Wherever "0.219 against 0.23" appears below, 0.265 is the like-for-like number.

## Target
Day, "The Method is the Conclusion" (voxday.net, 2026-10-12 14:12:35 UTC; quotes-day.md Q180-Q186; claim file DN6). RH tag: dialectic for every quote below, as filed.
- Q180 (¶3): "discovered that the protein-guided CDS alignment method has a circular reasoning problem that's impossible to ignore once you recognize it:"
- Q181 (¶7): "Regions too divergent to score well get gapped out or are left unaligned, so they aren't counted."
- Q182 (¶10): "Those excluded codons are enriched for nonsynonymous substitutions by definition, because that's why they scored poorly in the protein alignment."
- Q183 (¶13): "It's 73.8% nonsynonymous across every subset we tested. The signal is uniform across the genome, it's not concentrated in problematic genes."
- Q184 (¶17-21, table cells run together by text extraction): "A: All GENCODE20,4000.798973.9%", "B: 1:1 chimp orthologs16,9950.795673.8%", "B-HC: High-confidence 1:115,9370.793973.8%", "C: Excluded by filter3,4050.823774.4%", "Published (Consortium 2005)13,4540.2300~40%".
- Q185 (¶13): "We ran the same test on their smaller subset, which I suspected might be cherry-picked. Except they weren't."
- Q186 (¶15): "The difference is not a matter of gene selection, quality filtering, or computational error. It is a methodological artifact of using a conservation-dependent alignment to measure conservation."

## Files and provenance
- Script `research/checks/l1c_alignment_method.py`. Registration **536b19b** (2026-10-12 11:58 -06:00; only a synthetic selftest had run). Pre-run design review `results/REVIEW-R4-L1c-prerun.md` (**017dea9**: 1 BLOCKER, 9 MAJOR, 12 MINOR, with its resolution table). Amendments **0e0e840** (2026-10-12 15:07 -06:00), labelled "post hoc (pre-run, no data seen)". No later commit touched the script before the main run and the `transfer` run; its md5 then equalled the one recorded on the host (`2692334e…`). The fix pass added one additive mode in a commit labelled post hoc (**6c5d8cf**, md5 `c61c39ba…`; see the `transfer-excl` section); registered and amended code is unchanged.
- Blindness of the amendments: by commit order. 0e0e840 precedes the collection of L1b's outputs (c168b65, 2026-10-13 10:59 -06:00) and the L1c launch. Not blind, as the docstring lists: L1 on hg38 (0.271 / 0.207), which already made CRITIC the expected band, and the synthetic selftest miniature of the transfer table.
- Run: na-workhorse, launched 2026-10-13 16:59:22 UTC after L1b was collected, 8 workers, wall 16 min 42 s (script clock 1,001 s), peak RSS 1.33 GB (`/usr/bin/time -v`), exit status 0. Host record `raw/l1c.host`. Outputs `raw/l1c.out`, `raw/l1c.json`, `raw/l1c.genes.tsv.gz`, `raw/l1c.csac23_map.tsv` (commit 90b32ba).
- Inputs (hashes in `raw/l1c.host`): L1b's segment dump `sources/raw/l1b-seg-2026-10-13/seg.json.gz`, sha256 `86b0e672d70bb6be1bd2978f869c06519482f191d11fe06d829d21b573afeacd`; CSAC 2005 Table S23 `S23_MOESM6.xls`, sha256 `ac9e966c…`; GENCODE v35 RefSeq metadata, sha256 `02c7a3e7…`. The MAF was not re-streamed.
- **Not Day's data or pipeline.** His code, alignments and excluded-codon counts are unpublished. Every protein-guided arm here is this audit's own in-script aligner and trimming rules.

### What is REGISTERED and what is AMENDED
| part | label | standing |
|---|---|---|
| Arms U0, UG, UT; noise arms NR, NM, NU; identity bins; sets ALL, O121, SYN, CSACp, HQ, NONHQ; registered band rule | REGISTERED | valid |
| Arms P, PG, PF1, PF2 (frame-0 translation of the ungapped chimp string) | REGISTERED | **invalid as registered** (BLOCKER-1): the frame is lost after any indel or uncovered stretch that is not a multiple of 3. Printed with `!`, never scored alone |
| Arms PA, PAG, PAF1, PAF2 (frame-aware counterparts), PL38, PL16 (local segments), PGB (Gblocks rule), UD (dS-dense windows removed) | AMENDED | REALISTIC = PA, PAG, PAF1, PL38, PGB. STRESS = PAF2, PL16 (upper bounds, decide nothing) |
| Sets CSAC23 (the real 13,454 list), CSAC23nm, NOT23, DSC, NONDSC, HQs | AMENDED | |
| Closed bands; relative-drop flags; excluded-codon pS ratio x (3x band); Reading A on realistic arms only; kappa-hat sensitivity line; `transfer` table | AMENDED | |

BLOCKER-1 was material on these data (audit prediction A8): the registered P reads at least one clean codon out of frame in 1,173 genes (6.1%), 3.65% of clean codons, and agrees with U0 on 97.2% of codons where PA agrees on 99.95%.

## Results (pooled = ratio of totals, Nei-Gojobori sites, Jukes-Cantor, kappa = 1)
19,310 genes; 10,992,384 codons compared in U0. Audit A0: U0 equals L1b V0 exactly on ALL, O121 and SYN (0.27116713, 0.23789970, 0.20896060; printed PASS). UT equals L1b's X1 (0.8531910413 in `raw/l1b.json`).

### Pooled dN/dS per arm and gene set
Set sizes: ALL 19,310; O121 16,824; CSACp 15,037 (the stand-in); CSAC23 12,724 (the real list); NOT23 6,586; HQ 17,504; HQs 17,550; DSC 18,433; NONDSC 877. Drop = U0 minus arm. Flags: absolute (large >= 0.25, moderate 0.10-0.25, small 0.03-0.10, none, reverse) and relative (large >= 50%, moderate 25-50%, small 10-25%, none, reverse).

| arm | ALL | O121 | CSACp | CSAC23 | NOT23 | HQ | HQs | DSC | NONDSC | nonsyn fraction (ALL) | pS (ALL) | drop vs U0, ALL (abs / rel) | flags ALL (abs / rel) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **U0** Cactus, gap codons skipped (= L1b V0) | **0.271** | 0.238 | 0.193 | **0.219** | 0.344 | 0.194 | 0.204 | 0.218 | 0.486 | 0.479 | 0.0177 | | |
| UG U0 + gap-neighbourhood trim | 0.263 | 0.232 | 0.192 | 0.215 | 0.333 | 0.194 | 0.203 | 0.216 | 0.472 | 0.471 | 0.0174 | +0.008 / +2.9% | none / none |
| UD U0 minus dS-dense windows (amended) | 0.264 | 0.232 | 0.196 | 0.214 | 0.340 | 0.199 | 0.207 | 0.222 | 0.632 | 0.472 | 0.0156 | +0.007 / +2.5% | none / none |
| UT naive ungapped (= L1b X1) | 0.853 | 0.844 | 0.800 | 0.827 | 0.883 | 0.805 | 0.809 | 0.848 | 0.866 | 0.743 | 0.0923 | -0.582 / -214.6% | reverse / reverse |
| *Amended, realistic* | | | | | | | | | | | | | |
| **PA** frame-aware protein-guided | 0.265 | 0.233 | 0.191 | 0.216 | 0.334 | 0.193 | 0.202 | 0.216 | 0.468 | 0.473 | 0.0177 | +0.006 / +2.3% | none / none |
| PAG PA + gap trim | 0.262 | 0.231 | 0.191 | 0.215 | 0.331 | 0.194 | 0.202 | 0.216 | 0.467 | 0.471 | 0.0175 | +0.009 / +3.3% | none / none |
| **PAF1** PA + lenient divergence trim | **0.255** | 0.226 | 0.190 | 0.211 | 0.319 | 0.193 | 0.202 | 0.214 | 0.436 | 0.464 | 0.0175 | +0.016 / +5.8% | none / none |
| PL38 local segments, X-drop 38 | 0.263 | 0.232 | 0.191 | 0.215 | 0.331 | 0.193 | 0.202 | 0.215 | 0.465 | 0.471 | 0.0177 | +0.008 / +2.9% | none / none |
| PGB Gblocks rule | 0.260 | 0.229 | 0.190 | 0.213 | 0.326 | 0.193 | 0.202 | 0.214 | 0.456 | 0.468 | 0.0176 | +0.011 / +4.1% | none / none |
| *Amended, stress* | | | | | | | | | | | | | |
| **PAF2** PA + strict trim | **0.177** | 0.162 | 0.146 | 0.151 | 0.215 | 0.148 | 0.154 | 0.161 | 0.261 | 0.375 | 0.0168 | **+0.094 / +34.8%** | small / moderate |
| PL16 local segments, X-drop 16 | 0.262 | 0.231 | 0.191 | 0.214 | 0.330 | 0.193 | 0.202 | 0.215 | 0.463 | 0.470 | 0.0176 | +0.009 / +3.3% | none / none |
| *Registered, invalid as registered (BLOCKER-1)* | | | | | | | | | | | | | |
| P! protein-guided, frame 0 | 0.535 | 0.496 | 0.336 | 0.492 | 0.584 | 0.198 | 0.208 | 0.506 | 0.613 | 0.645 | 0.0413 | -0.264 / -97.4% | reverse / reverse |
| PG! P + gap trim | 0.508 | 0.461 | 0.302 | 0.455 | 0.570 | 0.197 | 0.206 | 0.471 | 0.640 | 0.633 | 0.0317 | -0.236 / -87.2% | reverse / reverse |
| PF1! P + lenient divergence trim | 0.340 | 0.308 | 0.228 | 0.297 | 0.394 | 0.194 | 0.203 | 0.310 | 0.465 | 0.535 | 0.0243 | -0.068 / -25.3% | reverse / reverse |
| PF2! P + strict divergence trim | 0.190 | 0.175 | 0.152 | 0.166 | 0.224 | 0.148 | 0.154 | 0.177 | 0.266 | 0.392 | 0.0184 | +0.081 / +30.0% | small / moderate |

- On CSACp and CSAC23 every realistic arm is `none` on both flags (drops 0.002-0.008). PAF2: CSACp +0.047 (24.4%, small / small), CSAC23 +0.067 (30.8%, small / moderate).
- Other estimators on U0 ALL: p-ratio 0.274; mean of per-gene ratios 0.271 (capped at 2: 0.256); median 0.163; raw Nd/Sd 0.919; single-difference nonsynonymous share 44.9%; NG N/S 3.36; kappa-hat 5.43.
- The registered P family reads high on every set that contains frameshift runs and reads like U0 on HQ (0.198 against 0.194), which excludes them. That is the frame loss, not a protein-guidance effect.

### Excluded-codon accounting (ALL): what each arm drops
Codons compared in U0 and not in the arm. x is the pS of the dropped codons over the pS of the dS-clean arm UD (0.0156); the band fixed before the run reads x <= 3 as ordinary divergence and x > 3 as misalignment (a reading that fails for saturated replacement runs: see "What the dropped codons are"). The last two columns are **post hoc and descriptive**, computed here from `raw/l1c.json`.

| arm | codons dropped | share of U0 codons (ALL / CSACp / CSAC23) | genes | codons gained | nonsyn fraction | dN/dS of dropped (p-ratio) | pS of dropped | x | within 10 codons of a frameshift run | share of all Nd / Sd removed (post hoc) | pN needed for 0.80 (post hoc) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UG | 33,160 | 0.30% / 0.09% / 0.20% | 2,763 | 0 | 0.696 | 0.686 | 0.1119 | 7.2 | 46.3% | 4.8% / 1.9% | 3.17 |
| UD | 56,407 | 0.51% / 0.12% / 0.35% | 1,389 | 0 | 0.521 | 0.338 | 0.4086 | 26.2 | 12.0% | 14.5% / 12.2% | 1.97 |
| PA | 9,109 | 0.08% / 0.01% / 0.03% | 1,026 | 9,950 | 0.733 | 0.844 | 0.1723 | 11.0 | 18.1% | 2.5% / 0.8% | 11.47 |
| PAG | 25,541 | 0.23% / 0.08% / 0.13% | 2,126 | 6,837 | 0.712 | 0.761 | 0.1194 | 7.6 | 12.2% | 4.3% / 1.6% | 4.13 |
| PAF1 | 14,294 | 0.13% / 0.01% / 0.05% | 1,398 | 9,215 | 0.767 | 1.008 | 0.2365 | 15.2 | 24.2% | 6.4% / 1.8% | 7.45 |
| PL38 | 10,007 | 0.09% / 0.01% / 0.03% | 1,243 | 9,493 | 0.752 | 0.926 | 0.1753 | 11.2 | 21.1% | 3.0% / 0.9% | 10.45 |
| PGB | 12,439 | 0.11% / 0.02% / 0.04% | 1,425 | 9,004 | 0.761 | 0.958 | 0.1903 | 12.2 | 25.4% | 4.3% / 1.2% | 8.43 |
| PAF2 (stress) | 101,594 | 0.92% / 0.45% / 0.62% | 11,006 | 7,363 | 0.846 | 1.822 | 0.1100 | 7.1 | 8.3% | **37.3%** / 6.2% | 1.23 |
| PL16 (stress) | 10,622 | 0.10% / 0.01% / 0.03% | 1,270 | 9,286 | 0.750 | 0.917 | 0.1887 | 12.1 | 24.2% | 3.4% / 1.1% | 9.87 |
| P! | 82,195 | 0.75% / 0.12% / 0.49% | 1,738 | 41,351 | 0.674 | 0.606 | 0.0622 | 4.0 | 8.5% | 5.8% / 2.6% | 1.28 |
| PG! | 219,124 | 1.99% / 0.45% / 1.43% | 2,731 | 23,590 | 0.655 | 0.565 | 0.0534 | 3.4 | 7.9% | 12.4% / 6.0% | 0.50 |
| PF1! | 314,814 | 2.86% / 0.61% / 2.11% | 1,995 | 17,985 | 0.663 | 0.577 | 0.0518 | 3.3 | 6.5% | 17.8% / 8.3% | 0.35 |
| PF2! | 452,501 | 4.12% / 1.19% / 3.07% | 11,080 | 9,071 | 0.762 | 0.967 | 0.0537 | 3.4 | 5.7% | 44.1% / 12.7% | 0.28 |

How to read it:
- **Direction, as Day says (Q182).** In every arm the dropped codons are richer in nonsynonymous differences than U0 as a whole (nonsynonymous fraction 0.71-0.85 against 0.479). Every realistic arm lowers the pooled value (by 0.006 to 0.016).
- **Size.** The realistic arms (the audit's label; see "What the arm names mean") drop 0.08% to 0.23% of codons and 2.5% to 6.4% of the nonsynonymous differences. Carrying 0.80 to 0.23 by exclusion alone needs about 71% of them removed with pS unchanged (post hoc arithmetic: 1 - 0.23/0.80). **The size bound does not depend on what the dropped codons are** (critic review finding 3): if every codon these arms remove were real, correctly paired, fast-evolving protein, the bias would be exactly the measured drop, 2.3% to 5.8% on all genes and 1.3% to 3.7% on the real list.
- **What the dropped codons are (reworded in the fix pass; correctness finding 1).** Their pS is 7.6 to 15.2 times the dS-clean pS (0.12 to 0.24 against 0.0156), and 12% to 25% of them lie within 10 codons of a Cactus frameshift run (by `cactus_frame`: 1,228 genes, 2,596 frameshift runs, 2,843 in-frame runs; the diagnostics line's 1,312 genes / 3,474 runs is the registered `indel_runs` definition). **x does not by itself tell misalignment from a saturated real replacement run:** Nei-Gojobori path-averages codons with two or three differences, so a fully replaced run also reads x well above 3 (9.6 in the correctness review's partial regeneration of the synthetic cell nominal 0.8 / clustering 2; the full-cell values are in the post hoc `transfer-excl` section). x does separate misalignment from moderately dense runs (reviewer: 0.5 and 1.3). The reading "what these arms drop looks like mispairing" therefore rests on three observables together, not on x: (i) the nonsynonymous fraction of the dropped codons, 0.71 to 0.77, and (ii) their p-ratio, 0.76 to 1.01, both of which are what unrelated in-frame pairing gives (arm NU: 0.774 and 1.018; NM 1.0: 0.739; UT: 0.743) and not what the synthetic dense runs give (fraction 0.94 to 0.99, p-ratio 4.8 to 30; `transfer-excl` section); (iii) x and the frameshift-run share as supporting facts. Scope of that reading: all genes pooled. It is not established separately for the 2,765 genes with indels or coverage holes, where a dense real run next to an indel cannot be told from mispairing by anything measured here (regime section); and on dS-clean subsets (indel-free, DSC, HQs) the few codons dropped fall between the two signatures and are not classified (`transfer-excl` section). (UD's own x of 26 is by construction: UD selects on synonymous differences.)
- **"pN needed for 0.80" (post hoc).** Hold the kept codons and the overall pS as observed. For the all-codon p-ratio to be 0.80 instead of 0.274, the dropped codons would have to carry 236,625 more nonsynonymous differences than the 122,939 observed in all of U0. Per nonsynonymous site of the dropped codons that is the value in the last column. A proportion cannot exceed 1, and unrelated sequence gives about 0.73 (arm NU). For every valid arm the requirement is impossible (1.23 to 11.5) **as a statement about the codons these arms exclude from the Cactus-paired set; it says nothing about codons no arm sees**, which have their own section ("The codons no arm sees").
- **The stress arm (audit's label) is not small, and on clean genes what it drops is dS-normal.** PAF2 drops 0.92% of codons carrying 37.3% of all nonsynonymous differences and lowers the estimate by a third, on dS-clean gene sets too (HQs 0.204 to 0.154; DSC 0.218 to 0.161). It drops the neighbourhood of any radical replacement by design. Post hoc (correctness finding 4, Day review finding 3; recomputed in the fix pass from `raw/l1c.genes.tsv.gz`): PAF2's x is 7.1 on ALL but 2.8 on the 16,545 indel-free genes (drop 25.5%, 0.484% of codons, nonsynonymous fraction 0.921), 2.0 on DSC (nonsynonymous differences down 26.8% net, 0.54% fewer codons) and 1.6 on HQs (24.8%, 0.47%); 5.8 on CSAC23 (33.2%, 0.60%). On dS-clean sets PAF2 therefore meets all three conditions of the amended Reading A (flag, enrichment, x <= 3).

### What the arm names mean (fix pass; Day review finding 3, critic review finding 5)
"Realistic" and "stress" are the **audit's labels**, fixed in the amendment (0e0e840) before the real data and after the selftest miniature had shown PAF2 reading 30-38% low. Nothing was run between PAF1 and PAF2. The two rules are far apart (printed rules table, `raw/l1c.out` l.330; script `rules_table`): for one replacement between unchanged neighbours, PAF1 (window 5, mean below 1) would need a substitution score below -11 beside residues of self-score 4, and BLOSUM62 has no score below -4, so the lenient rule can never remove an isolated replacement and needs a run of bad positions; PAF2 (window 3, mean below 3) removes a replacement scoring below 1, -1 or -3 beside neighbours of self-score 4, 5 or 6, with its neighbours. Where a published divergence filter falls between them is not measured here.

Correspondence to published pipelines, only as far as files in this repo support it (script docstring, "VERIFICATION OF THE REVIEW'S FROM-MEMORY CLAIMS"):

| arm | rule | source for the rule | standing |
|---|---|---|---|
| U0 | codons as the Cactus nucleotide alignment pairs them | same class as CSAC 2005's method for the 13,454 genes (a nucleotide genome alignment), but Cactus is not BLASTZ best-reciprocal and hs1 / mPanTro3 are not the 2005 assemblies | class match only |
| PA | global Gotoh alignment, BLOSUM62, gap 10 + k, on the chimp protein built in the Cactus frame | none; PAL2NAL's input is verified from fetched text ("a protein alignment plus the corresponding DNA (CDS) sequences"), and PA does **not** start from an independent chimp CDS | unsourced; not a protein-guided pipeline as practised |
| PAG | PA plus removal within 3 codons of a gap | audit's rule | unsourced |
| PAF1, PAF2 | PA plus window trims (5 / mean < 1; 3 / mean < 3) | audit's windows | unsourced |
| PL38, PL16 | local segments by X-drop 38 / 16 | "this audit's rule, not a named pipeline's"; X-drop values from memory of BLAST defaults, not verified | unsourced |
| PGB | Gblocks block selection, defaults for two sequences | Gblocks documentation (fetched mirror; method and defaults verified from the text) | documented rule; not validated against the binary |
| none | MACSE, PRANK (codon model), TranslatorX, Clustal W on proteins, codeml F3x4 | not installed / not verified | not run |

One arm of seven is anchored to a document and none to a pipeline of the literature. Open follow-up: a threshold dose-response on the PA path between PAF1 and PAF2 (windows 3 and 5, mean-score thresholds in steps; drop, share of Nd removed and x on ALL, DSC and CSAC23). Not run.

### Noise arms (U0 material, ALL)
| arm | pooled JC | p-ratio | nonsyn fraction | pS | median per-gene |
|---|---|---|---|---|---|
| U0 | 0.271 | 0.274 | 0.479 | 0.0177 | 0.163 |
| NR 0.002 (random base errors per base) | 0.339 | 0.342 | 0.534 | 0.0196 | 0.281 |
| NR 0.005 | 0.419 | 0.423 | 0.587 | 0.0226 | 0.394 |
| NR 0.01 | 0.516 | 0.521 | 0.636 | 0.0274 | 0.512 |
| NR 0.02 | 0.634 | 0.640 | 0.682 | 0.0371 | 0.644 |
| NR 0.05 | 0.776 | 0.784 | 0.724 | 0.0665 | 0.787 |
| NR 0.10 | 0.856 | 0.866 | 0.742 | 0.1156 | 0.862 |
| NM 0.1 (share of genes misregistered by 1 bp) | 0.673 | 0.682 | 0.696 | 0.0564 | 0.198 |
| NM 0.25 | 0.765 | 0.780 | 0.723 | 0.1125 | 0.285 |
| NM 0.5 | 0.802 | 0.826 | 0.733 | 0.2049 | 0.598 |
| NM 1.0 | 0.807 | 0.861 | 0.739 | 0.3953 | 0.778 |
| NU unrelated in-frame pairing | (JC undefined near saturation; printed 1.165) | 1.018 | 0.774 | 0.7181 | 1.392 |
| UT naive ungapped (real indels, no noise added) | 0.853 | 0.861 | 0.743 | 0.0923 | 0.189 |

- Random base error reaches 0.80 at r* = 6.5% per base (`NR_rstar_080` 0.0648), where pS would be about 0.08 against 0.0177 observed.
- Every route to about 0.80 that this audit constructed on these data carries a nonsynonymous fraction of 0.72 to 0.77 and a pS at least 3.7 times U0's. The no-constraint fraction N/(N+S) is 0.770 at the NG site ratio. Day's rows give 73.8% to 74.4% (Q183, Q184); his pS or identity is not published.
- Conversion printed by the script: Day's 73.9% is Nd/Sd 2.83, which is dN/dS 0.80 at N/S 3.54, 0.85 at 3.34 and 1.02 at CSAC's 2.78.
- **Post hoc, descriptive (read off the printed table):** UT is close to uniform across sets (0.853 / 0.844 / 0.800 / 0.827 on ALL / O121 / CSACp / CSAC23; nonsynonymous fraction 0.743 / 0.741 / 0.730 / 0.738; NOT23 0.748), as Day's table is (0.7989 / 0.7956 / 0.7939; 73.9 / 73.8 / 73.8%; C 74.4%). U0 is not uniform (0.271 / 0.238 / 0.193 / 0.219; fraction 0.479 / 0.446 / 0.395 / 0.426). This is a resemblance, not a location of Day's method: L1b's registration names naive extraction a candidate only. The full comparison has its own section below ("The naive arm against Day's table").

Protein family applied to extractions that read high (amendment 6 ii; pooled JC):

| input | raw | PA | PAF1 | PL38 | PGB |
|---|---|---|---|---|---|
| NM 1.0 (every gene misregistered) | 0.807 | 0.644 | 0.495 | 0.478 | 0.588 |
| NR 0.02 | 0.634 | 0.631 | 0.627 | 0.630 | 0.629 |
| NR 0.05 | 0.776 | 0.774 | 0.765 | 0.773 | 0.772 |
| UT through the registered P / PF1 / PF2 (valid for this purpose: UT is the frame-0 reading) | 0.853 | P 0.535 | PF1 0.340 | PF2 0.190 | |

A protein-guided realignment with trimming does take a high value down by a large amount when the input is register-broken (0.853 to 0.340 with the lenient rule, 0.807 to 0.48-0.49), and does nothing to uniform base error. On the frame-preserving input it has almost nothing to remove.

### Identity bins and coverage strata (U0)
| nucleotide identity of the gene | genes | share | pooled dN/dS | nonsyn fraction | pS |
|---|---|---|---|---|---|
| >= 0.995 | 9,016 | 46.7% | 0.122 | 0.295 | 0.0098 |
| 0.99-0.995 | 6,771 | 35.1% | 0.206 | 0.409 | 0.0178 |
| 0.98-0.99 | 2,489 | 12.9% | 0.332 | 0.521 | 0.0266 |
| 0.95-0.98 | 633 | 3.3% | 0.521 | 0.637 | 0.0479 |
| 0.90-0.95 | 237 | 1.2% | 0.575 | 0.674 | 0.1039 |
| < 0.90 | 162 | 0.8% | 0.528 | 0.661 | 0.2293 |

Genes below 0.98: 1,032 (5.3%), pooled 0.552 (post hoc pooling of the three printed bins). Chimp-coverage strata: >= 0.99: 17,976 genes, 0.226; 0.9-0.99: 724, 0.412; 0.5-0.9: 530, 0.582; < 0.5: 80, 0.645. Diagnostics: median gene identity 0.9947; 1,312 genes with a frameshift run (3,474 runs); internal stops in 79 human and 518 chimp CDS; 877 dS-noisy genes (NONDSC). Sorting genes by identity sorts them by dN/dS by construction, so the gradient alone does not separate noise from fast evolution; the pS column and NONDSC do part of that work.

### The real CSAC 2005 list (CSAC23)
| step | count |
|---|---|
| NM_ accessions in Table S23 | 13,454 (68 without a symbol) |
| mapped through GENCODE v35 RefSeq metadata (NM route) | 12,613 |
| mapped by unique gene symbol (fallback) | 159 |
| unmapped: accession absent from GENCODE v35 | 663 |
| unmapped: transcript not in the annotation / gene not in the L1b universe | 9 / 10 |
| ambiguous accessions | 0 |
| distinct genes (NM route only) | 12,733 (12,577) |
| distinct genes present in ALL | **12,724 = 94.6% of 13,454** |

The floor fixed before the run was 85%; it is met, so CSAC23 is the source set for the amended band and CSACp is descriptive. U0 on CSAC23 is **0.219** (NM route only: 0.218), against the published 0.23 (Q184's last row). That sets a Nei-Gojobori count beside a codeml F3x4 estimate; like for like, at CSAC's own site ratio (N/S 2.78), the value is about **0.265** on the real list and 0.328 on all genes (post hoc), 15% and 43% above the published figure. The stand-in CSACp reads lower (0.193): the proxy was stricter than the real list. Genes outside the list (NOT23) read 0.344, one2one genes outside it (O121NOT23) 0.285. ALL over CSAC23 is 1.24 (post hoc ratio). The docstring's credit rule sends a set effect to the DN3 form of the claim, not to Q186. Limit stated in the amendment: the 2005 membership partly reflects panTro1 coverage.

### Sensitivity to the site model (kappa)
The script recounts synonymous and nonsynonymous **sites** with transitions weighted by kappa and leaves the differences and the Jukes-Cantor correction as they are. kappa = 1 is Nei-Gojobori exactly. kappa-hat is estimated from fourfold-degenerate third positions on U0.

| U0 | kappa 1 (NG) | 2 | 3 | 4 | 5 | 6 | kappa-hat | at CSAC's N/S 2.78 (post hoc: kappa-1 value x N/S / 2.78) |
|---|---|---|---|---|---|---|---|---|
| N/S (ALL) | 3.36 | 2.88 | 2.64 | 2.50 | 2.40 | 2.33 | | |
| ALL | 0.271 | 0.316 | 0.345 | 0.365 | **0.380** | 0.391 | 5.43 | 0.328 |
| O121 | 0.238 | 0.278 | 0.303 | 0.321 | 0.334 | 0.344 | 5.67 | 0.288 |
| CSACp | 0.193 | 0.225 | 0.246 | 0.260 | 0.271 | 0.279 | 6.02 | 0.233 |
| CSAC23 | 0.219 | 0.255 | 0.279 | 0.295 | **0.307** | 0.316 | 5.71 | 0.265 |
| NOT23 | 0.344 | 0.402 | 0.438 | 0.463 | 0.482 | 0.496 | 5.06 | 0.414 |
| PAF1 ALL | 0.255 | 0.298 | 0.325 | 0.344 | 0.358 | 0.369 | | |
| UT ALL | 0.853 | 1.004 | 1.100 | 1.166 | 1.215 | 1.253 | | |

What the 0.38 is: the same codons, the same differences, a transition-weighted site count at the integer kappa nearest kappa-hat (5). With fewer nonsynonymous sites per synonymous site, every arm rises by the same factor of about 1.40, so the gaps between arms keep their proportions and the band stays CRITIC (U 0.380, Uc 0.307, Ud 0.370, Rmin 0.358). The script scores at the nearest integer; at kappa-hat itself (5.43, linear interpolation between the kappa 5 and 6 columns, post hoc) U is **0.385**.

What it is not: it is not an alignment effect, not a move toward Day's method (the naive arm rises too, to 1.22), and not CSAC's estimator. CSAC used codeml F3x4 with N/S 2.78; kappa 5 gives N/S 2.40, past it. The estimator mixes transition-aware sites with a Jukes-Cantor correction, and kappa-hat from fourfold sites is not checked against an ML fit (no ML tool; queue item stays).

What it costs the audit (corrected in the fix pass; correctness finding 6, Day review finding 5): the headline 0.271 depends on the site model.
- **Margin.** At kappa-hat itself U is 0.385, **0.015** under the 0.40 line (0.020 at the integer 5 the script used; 0.009 at kappa 6). kappa-hat on ALL is pulled down by the dS-noisy genes (NONDSC 3.48); on DSC it is 5.91 and on HQs 5.93, nearest integer 6, so 0.009 is the margin that applies to the all-gene value at the kappa of dS-clean genes. A straight line through the kappa 5 and 6 values meets 0.40 near kappa 6.8 (the curve is concave, so the true crossing is somewhat higher).
- **The thresholds are not rescaled.** The docstring fixes the bands for "pooled JC dN/dS, kappa = 1" and calls the kappa line "sensitivity". At kappa-5 sites every arm, and Day's own row, scale by about 1.40 while 0.40 and 0.65 do not, so "0.015 under the line" has no like-for-like meaning; it is reported because a reader will ask. The line is comparable with neither side's estimator: its N/S (2.40 at kappa 5) is below CSAC's 2.78, and Day's rows imply 3.54.
- **17% and 29%.** The amendment's statement that NG "reads ~17% below a transition-aware estimate" is right against the value at CSAC's site ratio (0.271 is 17.2% below 0.328) and too small against the kappa-5 count (28.7% below 0.380), which goes past CSAC's ratio. The first version of this write-up called it "too small" without saying against what; withdrawn.
- **Like for like.** On the real CSAC list the value at CSAC's own site ratio is about 0.265 (post hoc), 15% above the published 0.23 and inside the registered 0.18-0.30 range; on all genes 0.328.

Band by convention (post hoc; U0; the left-out-codon rows are from "The codons no arm sees" below):

| convention | ALL | CSAC23 | NOT23 | against the 0.40 line |
|---|---|---|---|---|
| kappa 1 (Nei-Gojobori; the registered and amended bands) | 0.271 | 0.219 | 0.344 | ALL and the source set under it: CRITIC |
| CSAC's site ratio (N/S 2.78) | 0.328 | 0.265 | 0.414 | ALL and CSAC23 under; NOT23 over |
| kappa 5 (script's sensitivity line) | 0.380 | 0.307 | 0.482 | ALL and CSAC23 under; NOT23 over |
| kappa-hat 5.43 (interpolated) | 0.385 | 0.314 (at its own kappa-hat 5.71) | 0.482 (5.06) | under by 0.015 on ALL |
| kappa 6 | 0.391 | 0.316 | 0.496 | under by 0.009 on ALL |
| kappa 1, left-out codons added at the rates of the 351 worst-covered genes | 0.294 | | | under |
| kappa 5, same addition (0.294 x 1.40, approximate) | about 0.41 | | | **over** |

Threshold asymmetry, from the docstring (amendment 10): "0.40 leaves the critic side +74% above 0.23, 0.65 leaves Day -19% below 0.80; both inherited (0.65 is Day's own Q175 bound), unchanged." So the band at kappa 1 is not in doubt; the answer on transition-weighted sites depends on the kappa used and on what is assumed about the 1.40% of codons outside every arm.

### The codons no arm sees: the genome alignment as a prior filter (fix pass; post hoc, descriptive)
Every arm starts from the codons Cactus paired. The protein arms re-pair that material; none aligns a chimp coding sequence that Cactus did not already place. The two steelman reviews read this fact in opposite directions (Day review finding 2, critic review finding 3). Both are given here side by side. Every number was recomputed in the fix pass from `raw/l1c.json` and `raw/l1c.genes.tsv.gz` (one process, seconds); none is registered and none moves a band. "Left out" is CDS length / 3 less the terminal stop, minus the codons U0 counts; per-gene values carry the rounding of the gene table (about +-1 codon in long genes).

**How many.** 33,505,272 annotated CDS bp in 19,407 chosen genes is 11,149,017 sense codons; U0 compares 10,992,384. Left out: **156,633 codons, 1.40%** (about 130,000 of them inside the 19,310 genes, 1.17% of their codons; the rest in the 97 genes with no U0 codon). The first version of this write-up said "about 1.6%": that counted the 19,407 terminal stop codons as left out (1.58%). The left-out codons are concentrated: 351 genes with 20% or more of their codons not compared hold 78,954 of them (61% of the in-gene total).

**Day's side: Reading d, "the genome alignment that feeds U0 is itself the conservation-dependent step".** Basis in the filed quotes: Q181 says regions "get gapped out or are left unaligned, so they aren't counted" and Q186 says "a conservation-dependent alignment"; neither sentence is limited to protein scoring, and a nucleotide genome aligner also leaves low-scoring regions unaligned. Evidence in its direction, on the input alignment before any protein arm: the more of a gene Cactus leaves out, the higher the part it kept reads, and on dS-clean genes that happens at near-ordinary synonymous divergence.

| share of the gene's codons not compared | genes | U0 pooled | pS | nonsyn fraction | DSC genes | U0 pooled (DSC) | pS (DSC) |
|---|---|---|---|---|---|---|---|
| under 1% | 17,874 | 0.223 | 0.0158 | 0.430 | 17,413 | 0.206 | 0.0146 |
| 1% to 5% | 549 | 0.401 | 0.0280 | 0.577 | 443 | 0.309 | 0.0182 |
| 5% to 20% | 536 | 0.476 | 0.0403 | 0.620 | 397 | 0.415 | 0.0199 |
| 20% or more | 351 | 0.635 | 0.0824 | 0.688 | 180 | 0.466 | 0.0223 |

On dS-clean genes the paired codons read 0.21, 0.31, 0.42, 0.47 as more of the gene goes missing, at a pS between 0.015 and 0.022, all under the audit's own 0.023 gate. Amendment 4 of the docstring describes that pattern: "a fast-evolving protein has ordinary pS and high pN". That is the direction of Q182, seen at the gene level.

What the left-out codons would have to read (they are given U0's split of sites between N and S):

| target for U0 ALL | pN needed in the left-out codons, at U0's pS (0.0177) | at pS 0.05 |
|---|---|---|
| 0.80 (Day's number) | 0.67 | 0.70 |
| 0.65 (his Q175 floor) | 0.48 | 0.50 |
| 0.40 (the band line, kappa 1) | 0.17 | 0.18 |
| 0.40 on the kappa-5 sensitivity line | 0.023 | 0.032 |

(With the terminal stops wrongly counted in, as in the first version, the first row is 0.60; the first version's "near 0.58" did not state its assumption.) If the left-out codons merely read like the paired codons of the 351 worst-covered genes (pN 0.053, pS 0.082), U0 ALL becomes 0.294 at kappa 1 and about 0.41 on the kappa-5 line. So on this reading 0.80 and 0.65 are out of reach, and the Day review says so; a rise of the order of 10% and a crossing of 0.40 on transition-weighted sites are not excluded.

**The critics' side: the bound does not reopen 0.80, and the gradient has another reading.**
- For the left-out codons to lift the pooled value to 0.80 they need a pN of 0.67; to 0.65, 0.48. Unrelated in-frame sequence gives about 0.73 (arm NU). The route requires the left-out sequence to be all but non-homologous, and then it is not a measurement of selection on orthologues.
- Genes with nothing left out read 0.21 (0.210 on the 13,773 genes with at most 0.01 codons left out by the gene table; 0.206 on the 16,666 with under half a codon). Q183 ("The signal is uniform across the genome, it's not concentrated in problematic genes.") predicts about 0.80 there.
- The 351 worst-covered genes are not a sample of fast-evolving single-copy proteins: 73% carry a Cactus frameshift run, 49% are dS-noisy by the audit's rule, 46% are one2one, 29% are on the 2005 list. In the table above pS also rises with the share left out, by half even within DSC (0.0146 to 0.0223) and fivefold on all genes, which is what partial coverage of a paralogue or a broken assembly gives as well.
- On what the arms do remove: even if every codon the realistic arms drop is real signal, the bias is 2% to 6% on all genes (1% to 4% on the real list), against the 71% needed.
- Day's own post exempts this step. Held locally, not yet filed as a numbered quote (same post, ¶11 of the non-empty paragraphs): "The whole-genome alignment we utilize doesn’t have this scoring bias." Reading d is therefore his defender's reading of Q181 and Q186, not one his text adopts; and CSAC 2005's 13,454-gene value also came from a whole-genome nucleotide alignment (BLASTZ).

**Verdict for Reading d: not tested by L1c.** No arm can recover what the alignment left out, and the synthetic table hands U0 the true pairing. Bounded result only: under Reading d the left-out codons cannot carry 0.80 or 0.65 without reading like unrelated sequence; a shift of the order of 10% is open. Under RD it is recorded with that verdict as an extended reading (a different object: the genome alignment, where Q180 and Q182 name the protein alignment) and cannot set the DN6 field. What would test it: chimp coding sequences from an independent chimp annotation, aligned to the human CDS by an external codon-aware aligner, at least on the 351 genes and on the 2,765 genes with indels or holes. That is follow-up (b); it is **not run** (no external aligner on any host).

### The naive arm against Day's table: register loss as a candidate error class (fix pass; post hoc, descriptive)
Critic review finding 4 asked that this not be filed as a passing resemblance. It is given its own section with the same limit L1b set: **a candidate error class with a real-data instance; it cannot identify Day's pipeline**, which is unpublished (rules F and U; L1b: "LOCATED is not licensed").

What UT is: the first chimp row read position by position with gaps closed, so codons are paired out of register after the first length difference. Five features of Day's table (Q183, Q184) that UT reproduces on these data and U0 does not (recomputed in the fix pass from the gene table):
1. **Level.** UT 0.853 on all genes with no noise added (Day: 0.7989).
2. **Uniformity across gene sets.** UT 0.800 to 0.883 over ALL, O121, CSACp, CSAC23, NOT23, HQ, HQs, DSC (Day's rows: 0.7939 to 0.8237). U0 over the same sets: 0.193 to 0.344.
3. **The share.** UT's nonsynonymous fraction is 0.730 to 0.748 (Day: 73.8% to 74.4%); U0's is 0.395 to 0.537.
4. **The order of the rows.** Under UT, genes outside one2one read higher than those inside: 0.898 against 0.844 (2,486 and 16,824 genes), as Day's row C (0.8237) is above row B (0.7956).
5. **"High without protein guidance, low with it."** The registered protein family applied to UT's bases takes 0.853 to 0.535, 0.340 and 0.190 (table above). On a register-broken input a protein alignment restores the register.

Why UT is uniform ("affected" = UT differs from U0 in Sd or Nd; 2,637 genes, as in L1b):

| set | genes | affected | UT, affected genes (nonsyn fraction) | U0 on the same genes | UT, unaffected genes (nonsyn fraction) | affected genes' part of UT's Nd |
|---|---|---|---|---|---|---|
| ALL | 19,310 | 2,637 (13.7%) | 0.960 (0.764) | 0.427 | 0.205 (0.411) | 96.8% |
| O121 | 16,824 | 1,983 (11.8%) | 0.966 (0.764) | 0.364 | 0.196 (0.399) | 96.6% |
| CSAC23 | 12,724 | 1,265 (9.9%) | 0.960 (0.765) | 0.351 | 0.182 (0.382) | 96.3% |
| NOT23 | 6,586 | 1,372 (20.8%) | 0.960 (0.762) | 0.485 | 0.249 (0.456) | 97.2% |
| HQ | 17,504 | 1,256 (7.2%) | 1.005 (0.769) | 0.241 | 0.188 (0.389) | 94.8% |
| DSC | 18,433 | 2,118 (11.5%) | 0.971 (0.765) | 0.314 | 0.196 (0.399) | 96.6% |

In every set 7% to 21% of genes read 0.96 to 1.01 with a fraction of 0.76 to 0.77, the values of unrelated in-frame pairing (NU: 1.018, 0.774), and those genes supply 95% to 97% of the nonsynonymous differences counted. The pool is then close to one constant whatever the gene set: under UT, uniformity marks a pool dominated by one source, not a genome-wide signal. The per-gene median under UT is 0.189, and 80.5% of genes with a defined ratio read below 0.65.

The cause, from L1b's breakdown (`raw/l1b_x1_breakdown.json` / `.out`, verified in this pass): all of the naive arm's excess sits in the 2,637 affected genes. By first cause, in-frame indels carry 55.7% of it (deletions 37.6%, 889 genes; insertions 18.1%, 397 genes), coverage holes 28.8% (class `hole_rowempty` 23.0%, 601 genes), frameshift indels 8.4% (5.4% and 3.0%; 235 and 120 genes), exon edges 7.1%. The 1,138 genes whose only events are in-frame indels read 1.009 under the naive pairing and 0.281 by column. So this is mostly loss of codon register after an ordinary in-frame indel, not loss of reading frame. The synthetic table repeats it where the truth is known: UT reads 0.811 to 0.828 at a truth of 0.211 to 0.218 with correctly gapped indels in 15% of genes, at all three clustering levels.

What this licenses and what it does not:
- Licensed: (i) on Day's stated assemblies, the one extraction this audit built that returns his level, his uniformity, his share and his row order is one that pairs codons out of register after the first length difference; (ii) the same extraction on synthetic genes of known omega 0.22 returns 0.82; (iii) the frame-preserving extraction of the same bases returns 0.19 to 0.34 on the same gene sets; (iv) "low with protein guidance, high without" is what (i) predicts.
- Not licensed: that his pipeline does this. Nothing here has seen it.
- Against the candidate (L1b's Day-side counterpoint, kept): a nonsynonymous fraction of 72% to 76% "is what unconstrained sequence gives under either explanation" (weak constraint, or mispairing), so the share identifies a class of count and not his pipeline; and on its whole set the naive arm misses his single-difference share (L1b: 60.1% against his 71.6%). "Every route to 0.80" in this file means every route this audit constructed.
- On transition-weighted sites the naive arm reads 1.22 (kappa 5), and the script's conversion of Day's 73.9% gives dN/dS 1.02 at CSAC's site ratio: a genome-wide ratio of 1 would mean no constraint on protein sequence at all, which is further than his own "one in five" reading of 0.80.
- The outside input that would separate the two readings (for ROADMAP; to be requested only with the owner's approval): his per-gene table or median. A register-safe pipeline at a true 0.80 has a per-gene median near 0.8; a register-broken one near 0.19. From Day's side the same holds for one number: the count of codons his protein-guided comparison excluded, and their dN/dS.

## Bands and readings, as printed
```
BAND (REGISTERED, invalid as registered where it rests on PF1): CRITIC
BAND (registered rule, PAF1 in place of PF1): CRITIC
BAND (AMENDED, primary): {"band": "CRITIC", "U": 0.27116713099342615, "Uc": 0.21872237211035014, "uc_set": "CSAC23", "Ud": 0.2643265393784459, "pS": 0.01768781759593046, "nonsyn_frac": 0.4787770629363367, "Rmin": 0.25542985127310996, "Rmin_arm": "PAF1", "excl_pS_ratio": 15.152794631803665, "noise_subtag": null}
BAND (AMENDED) by source set: {'CSACp': 'CRITIC', 'CSAC23': 'CRITIC'}
BAND (AMENDED, sites at kappa-hat; sensitivity): {"kappa_hat": 5.428329514891922, "kappa_used": 5, "band": "CRITIC", "U": 0.38008722667191125, "Uc": 0.3070762991201858, "uc_set": "CSAC23", "Ud": 0.3704065893143789, "pS": 0.01768781759593046, "nonsyn_frac": 0.4787770629363367, "Rmin": 0.35801575864864016, "Rmin_arm": "PAF1", "excl_pS_ratio": 15.152794631803665, "noise_subtag": null}
READINGS: {"Q180_182_A": "contested (no realistic arm lowers dN/dS)", "Q180_182_B": "contradicted", "A_upper_bound_stress_arms": {"PAF2": 0.09436423595985091, "PL16": 0.008966457708362074}, "A_registered_PF2": "invalid as registered (BLOCKER-1); drop 0.08130393136958255", "note": "A is scored on REALISTIC arms only; PAF2/PL16 are stress tests and decide nothing. B also needs the synthetic transfer table (mode `transfer`): see docstring amendment 6."}
```
Also printed before the bands, whatever the outcome: "Pre-run, from the held CSAC 2005 text, whatever the band: the 13,454-gene 0.23 came from a BLASTZ genome alignment; Clustal W was used only for the 7,043-gene subset (MINOR-10)."

- **Estimator of the bands.** Docstring: "AMENDED BANDS (pooled JC dN/dS, kappa = 1; first applicable line; every input lands in exactly one)". The kappa-hat line is labelled "sensitivity" and its thresholds are not rescaled (kappa section).
- **Registered band.** CRITIC needs U < 0.40 and Uc < 0.40 on U0 (0.271; CSACp 0.193). Neither clause uses PF1, so the registered band does not rest on the invalid arm here.
- **Amended band.** First applicable line of the decision tree: U 0.271 and Uc 0.219 (CSAC23), both below 0.40. NOISE, GENE-SET, HIGH-NOT-METHOD, DAY, HIGH-PARTIAL-METHOD and MIDDLE all need U >= 0.40 and are not reached.

### The readings in plain words (rule RD)
**Reading A: "protein-guided pipelines can bias dN/dS down, by any amount."** Printed `contested (no realistic arm lowers dN/dS)`. **The printed string must always travel with its gloss:** "lowers" means a flag of at least `small` (0.03 absolute or 10% relative). In plain words all five realistic arms do lower the value, by 0.006 to 0.016 (2.3% to 5.8%), and all five are under the flag line. In the code the printed value rests on that one fact (no realistic arm has a flag). Two further reasons are the write-up's, not the code's:
1. the codons removed are nonsynonymous-enriched (Day's Q182, true in direction) and, pooled over all genes, carry the mispairing signature (nonsynonymous fraction 0.71-0.77 and p-ratio about 1; x 7.6 to 15.2 as a supporting fact only, since x alone does not separate a saturated real run from misalignment: correctness finding 1);
2. the amended rule gives `contested`, not `contradicted`, when no realistic arm lowers it. The amended rule has two outcomes only (`supported`, `contested`). What the one species pair showed is an upper bound on these arms, not an absence of evidence: 2% to 6% on all genes, 1% to 4% on the real list, 0.2% to 0.7% in indel-free genes, against the 71% the 0.80-to-0.23 claim needs.

Upper bound from the stress arms (audit's label): PAF2 0.094 (34.8%), PL16 0.009. They decide nothing under the amendment.

**Result of record, and the registered value beside it (fix pass; correctness ruling 3a).** The result of record is the amended reading as printed: Reading A `contested`, Reading B `contradicted`. Grounds: the docstring's precedence sentence, committed in 0e0e840 before any L1b or L1c data ("Where the two disagree the amended result is the one proposed for integration, and the registered one is shown with the reason"), and the fact that the registered reading has no valid arm under it.
- **What the registered rule printed:** `"A_registered_PF2": "invalid as registered (BLOCKER-1); drop 0.08130393136958255"`. The registered Reading A is therefore **invalid as registered**, not `supported`.
- **What the first version of this write-up said, and what it was:** "As registered, Reading A scores `supported`". That was the write-up's derivation, not a printed result: the registered rule ("supported if any of P/PF1/PF2 has mechanism flag >= small with excluded nonsyn fraction > U0's") applied to PAF2 in PF2's place (0.094; 0.846 against 0.479). The substitution is reasonable (the script does the same for the band with PAF1) but it is a substitution.
- **What the `contested` turns on.** Not the x discriminator: on the 16,545 indel-free genes (85.7% of genes) PAF2 lowers the pooled value by 25.5% (0.2045 to 0.1523), drops 0.484% of codons, and those codons have a nonsynonymous fraction of 0.921 and x = 2.8. There the stress arm meets all three amended conditions (flag, enrichment, x <= 3). The amended `contested` turns on classing PAF2 as a stress arm, which the amendment did before the real data and after the selftest miniature had shown PAF2 reading 30-38% low (docstring, NOT BLIND). The registration itself had called PF2 adversarial ("it removes nonsynonymous changes because they are nonsynonymous").
- **Order of events, in the Day review's words, for the claim file:** the audit wrote a rule under which Day's reading scored `supported`, saw in a miniature that it would, and changed the rule before the real data. The change answers pre-run MAJOR-9 ("Reading A comes out `supported` whatever real pipelines do") and is defensible; it is also the amendment that moved Reading A against him.
- **The other direction (critic review finding 7).** The amendments cost the critics no verdict (Reading B `contradicted` both ways; the move sentence gives `contested` both ways). The registered move sentence read on the arms the amendment calls realistic alone would give "CRITIC with flag none -> contradicted"; the docstring does not license that reading of the sentence (see "Note on DN6 Reading b"), and it is recorded as reading b1 in the Readings table. And after the amendment Reading A cannot come out `contradicted` whatever the data do: a reading with two outcomes that cannot lose is a limit of the amended rule from the critics' side, as MAJOR-9 was from Day's.

**Reading B: "the published 0.23 is this artefact."** Printed `contradicted`. Registered rule: contradicted under CRITIC with the PF2 flag below `large` (it is `small`). Amended rule: contradicted under CRITIC when no realistic arm has a `large` flag (all are `none`). The two agree. Independently of the run, the held CSAC text says the 13,454-gene value came from a nucleotide genome alignment (BLASTZ, best reciprocal). The same text also says the 13,454 were what remained "After removing low-quality sequences and likely alignment artefacts" and are genes "for which it was possible to generate high-quality sequence alignments covering virtually the entire coding region": the label "protein-guided" is contradicted, a selection on alignment quality is not (criteria in the SI, not held; a gene-set effect, which Q186 itself sets aside with "not a matter of gene selection, quality filtering"). The amended rule asks for the transfer table beside Reading B; it is in the transfer section and does not change the value.

**Q183.** Reading A (uniformity shows the gap is not gene-list driven): on U0 the sets are not uniform (0.193 to 0.344). Reading B (73.8% is the misalignment signature): NU 0.774, NM 1.0 0.739, NR 0.05-0.10 0.724-0.742, UT 0.743, against U0's 0.479. Neither reading has a registered verdict rule; numbers only. **Q185** is not decidable here (Day's run on the smaller subset is unpublished); CSAC23 is now the real list, not a proxy. **Q186** ("not ... computational error") bears through the noise arms and identity bins above; no verdict rule was registered for it beyond the band.

## Scoring of the predictions
Hits and misses with equal weight. Where a registered prediction names an arm that is invalid as registered, the registered arm is scored as printed and the frame-aware counterpart beside it. The three transfer rows were scored after the table landed (transfer section).

### Day side
| prediction | value | result |
|---|---|---|
| REG: U0 ALL ~0.80 (>= 0.65) | 0.271 | **miss** |
| REG: nonsyn fraction ~74% (>= 0.66) | 0.479 | **miss** |
| REG: PF1 ALL <= 0.40 | PF1! 0.340; PAF1 0.255 | met numerically, empty: U0 is already 0.271, and the invalid PF1! is above U0 |
| REG: drop U0 - PF1 >= 0.25 | PF1! -0.068; PAF1 +0.016 | **miss** |
| REG: excluded codons pooled dN/dS >= 2 | PF1! 0.577; PAF1 1.008 (PAF2 1.82) | **miss** |
| REG: excluded nonsyn fraction > U0's | PF1! 0.663, PAF1 0.767, against 0.479 | **hit** |
| REG: O121, CSACp, ALL within 0.05 | 0.238, 0.193, 0.271 (spread 0.078) | **miss** |
| REG: N/S (NG) ~3.5 | 3.36 | hit at the ±25% tolerance used in L1/L1b; it does not separate 3.54 from the audit's 3.20-3.40 |
| AM: amended band DAY | CRITIC | **miss** |
| AM: Ud >= 0.65 | 0.264 | **miss** |
| AM: pS <= 0.023 | 0.0177 | **hit** on this half; the amended text is one conjunction ("Ud >= 0.65 and pS <= 0.023"), which as written is a miss |
| AM: a realistic arm with a large flag, excluded codons x <= 3 and dN/dS >= 2 | all `none`; x 7.6-15.2; dN/dS 0.76-1.01 | **miss**. The x <= 3 clause was unreachable even in the synthetic cell built to let the mechanism work (x about 10 there; correctness finding 1 and the `transfer-excl` section): a defect of the audit's amendment, on Day's side. The miss stands on the flag clause alone (all `none`) |
| AM: CSAC23 within 0.05 of ALL on U0 | 0.219 against 0.271: 0.052 | **miss**, by 0.002 |
| AM: transfer, some realistic arm <= 0.40 at true 0.8 | PAF1 0.239, PGB 0.308 at clustering 2 (truth 0.683); none at clustering 0 or 1 | **hit** (kept as a hit; **not blind**: PAF1 0.25 and PGB 0.29 against a truth of 0.66 had been seen in the selftest miniature before the amended predictions were fixed; extreme clustering only; see the transfer section) |

### Critic side
| prediction | value | result |
|---|---|---|
| REG: U0 ALL 0.20-0.35 | 0.271 | hit |
| REG: CSACp 0.18-0.30 | 0.193 | hit |
| REG: P within ±0.03 of U0 | P! 0.535; PA 0.265 | **miss** on the registered arm (invalid); hit on PA |
| REG: PF1 drop < 0.03 | PF1! -0.068 (reverse); PAF1 +0.016 | met in the letter on PF1! with the wrong sign (invalid); hit on PAF1 |
| REG: PF1 excluded share < 2% | PF1! 2.86%; PAF1 0.13% | **miss** on the registered arm (invalid); hit on PAF1 |
| REG: P-U0 codon agreement >= 98% | P! 97.2%; PA 99.95% | **miss** on the registered arm (invalid); hit on PA |
| REG: NU nonsyn fraction 0.68-0.80 | 0.774 | hit |
| REG: NR r* >= 2 x U0 pS | 0.065 against 0.035 | met; a restatement of U <= 0.40 (amendment 10), not counted |
| REG: NM(1.0) >= 0.60 | 0.807 | hit |
| REG: genes with identity < 0.98 are < 10% of ALL and carry >= 0.50 | 5.3%; 0.552 | hit (the second clause is near automatic) |
| AM: band CRITIC on both source sets | CRITIC, CRITIC | hit |
| AM: PA within ±0.01 of U0; agreement >= 99.5% | 0.006; 99.95% | hit, **near automatic by construction**: PA's chimp protein is the Cactus pairing with the gaps closed, so on the 16,545 indel-free genes (85.7%) the aligner is handed the same string in the same register and returns the diagonal (PA differs from U0 in 3 of them). Not independent confirmation |
| AM: every realistic arm `none` on both flags | none on ALL, CSACp, CSAC23 | hit |
| AM: realistic excluded share < 1% of U0 codons | 0.08-0.23% | hit |
| AM: with x > 3 | 7.6-15.2 | hit |
| AM: CSAC23 0.18-0.30 on U0 | 0.219 | hit |
| AM: NOT23 above CSAC23 by >= 0.10 | +0.126 | hit |
| AM: NM(1.0) p-ratio >= 0.60; NU nonsyn fraction 0.68-0.80 | 0.861; 0.774 | hit |
| AM: NM(1.0)>PAF1 at least 0.25 below NM(1.0) | 0.807 to 0.495 (-0.313) | hit |
| AM: transfer, realistic arms within 10% of truth on clean cells at clustering 0 and 1 | PAF1 -13.5% at nominal 1.0, clustering 1; the other 39 arm-cells within 10% | **miss** (this was the one blind transfer prediction) |

### Audit
| prediction | value | result |
|---|---|---|
| A0 U0 equals L1b V0 to 1e-9 | identical on ALL, O121, SYN | hit |
| A1 NG N/S on U0 ALL 3.20-3.40 | 3.36 | hit |
| A1 kappa-hat in 3-6 | 5.43 | hit |
| A1 N/S at kappa-hat in 2.6-3.0 | 2.40 at kappa 5 (2.33 at 6) | **miss** |
| A1 no arm but UT and noise with NG N/S >= 3.50 | maximum 3.38 (post hoc scan of the json) | hit |
| A2 median <= pooled <= mean-capped on U0 ALL | 0.163, 0.271, 0.256 | **miss** (capped mean below pooled) |
| A2 CSACp against ALL within 0.06 | 0.078 | **miss** |
| A3 PF2 drop in 0.03-0.15 | PF2! 0.081 (invalid arm); PAF2 0.094 | hit on both |
| A4 UG within 0.03 of U0 | 0.008 | hit |
| A4 UT 0.28-0.60 | 0.853 | **miss** (as in L1b) |
| A5 excluded codons of PF1: pooled dN/dS > 1 | PF1! 0.577; PAF1 1.008 (JC 1.010, post hoc) | **miss** on the registered arm; hit on PAF1 by 0.01 |
| A5 second clause: identity of the genes carrying them below the ALL median (0.9947) | PF1! 0.9882; PAF1 0.9261 | hit (clause replaced by A5' as near automatic) |
| A5' PAF1 excluded codons have x > 3 | 15.2; 24.2% within 10 codons of a frameshift run | hit |
| A6 band hits < 1% of genes; P skipped < 2% | 22 widened (0.11%), 0 final; 0 skipped | hit |
| A7 cap-skipped genes < 0.5% per family | 0 | hit |
| A8 registered P out of frame in > 1% of genes | 1,173 genes (6.1%) | hit: BLOCKER-1 was material |
| A9 CSAC23 floor met (>= 85%) | 94.6% | hit |
| A10 transfer: PA = U0 on clean cells; UD within 5% of U0 (no clustering); U0 >= 25% above truth under misreg25 | PA below U0 by 1.4% to 24.5% at clustering 2; UD +0.5% to +1.3%; U0 +19% or less in some cells at nominal 0.8 and 1.0 | **miss** (clause ii hit; i and iii miss; clause i was foreseeable from the selftest miniature, PA 0.58 against 0.66) |

Tally (excluding the uncounted restatement): Day side 4 hits (1 of them not blind), 1 empty, 9 misses. Critic side: 14 hits (1 near automatic), 1 miss (transfer); 4 further registered predictions name the protein arms that are invalid as registered and fail there (3 misses, 1 met with the wrong sign) while holding on the frame-aware counterparts; that failure is the audit's implementation, not the critics' expectation. Audit: 12 hits, 5 misses (A10 among them), and 1 split (A5 first clause: miss on the registered arm, hit by 0.01 on PAF1).

By label (fix pass; correctness note 8): Day REG 2 hits, 1 empty, 5 misses; AM 2 hits, 4 misses. Critic REG 5 hits, 4 on invalid arms, 1 uncounted; AM 9 hits, 1 miss. Audit A0-A6: 8 hits, 4 misses, 1 split; A5', A7-A9: 4 hits; A10 miss.

What L1c itself added (fix pass; Day review finding 6). U0 was fixed by L1b before L1c was launched (audit A0), so several rows above restate known facts: on Day's side "U0 ALL ~0.80", "nonsyn fraction ~74%", "O121, CSACp, ALL within 0.05", "band DAY", "Ud >= 0.65" (known misses) and "N/S ~3.5", "pS <= 0.023" (known hits); on the critic side "U0 ALL 0.20-0.35", "CSACp 0.18-0.30" and "band CRITIC" (known hits). Limited to what L1c added (flags, excluded-codon table, CSAC23, noise arms, transfer): **Day 2 hits (excluded codons nonsynonymous-enriched; transfer, not blind), 1 empty, 4 misses; critics 11 hits, 1 miss, 4 on the invalid arm.**

## Transfer table (synthetic; amendment 6 i)
Run: na-workhorse, `transfer research/checks/results/raw/l1c 8 2000 300`, wall 15 min 5 s (script clock 905 s), peak RSS 182 MB, exit status 0; outputs `raw/l1c.transfer.out`, `raw/l1c.transfer.json` (collected in 9d61b8a). Same script file as the main run. 48 cells (4 nominal omegas x 3 clustering levels x 4 noise settings), 2,000 synthetic genes of 300 codons per cell, every arm. No real data enters.

What the generator does (script, `_tf_gene`; all rates are ASSUMED design values, uniform codon usage, kappa 1):
- Synonymous divergence 1.2%. "Truth" in the table is what U0 reads on the clean cell of the same omega and clustering, not the nominal omega (0.216 for 0.23; 0.757, 0.729, 0.683 for 0.8 at clustering 0, 1, 2: multiple hits lower it).
- **U0 is exact by construction here** (fix pass; Day review finding 2). The generator hands every arm the true pairing. No synthetic sequence passes through a nucleotide genome aligner and no cell has a coverage hole, so the table says nothing about what a genome alignment leaves out, and "U0 returns the truth" in a clean cell is not a finding.
- **Clustering 0:** every codon has the same omega. **Clustering 1:** 2% of codons, in runs of 15, hold 50% of the replacements (omega 25 times the nominal inside a run). **Clustering 2:** 1% of codons, in runs of 15, hold 80% of the replacements. Inside a clustering-2 run the codon omega is 80 times the nominal (64 at nominal 0.8), so each base is hit with probability 0.77 and the 15-residue stretch is close to fully replaced, at ordinary synonymous divergence. A 300-codon gene carries such a run with probability 0.2. It is the extreme level by design.
- Noise: `indel` = 10% of genes with one in-frame 3/6/9-bp indel and 5% with a 1-bp indel, all correctly gapped; `misreg05` / `misreg25` = 5% / 25% of genes with a 40-codon stretch shifted by one base with no gap.

Compact table (pooled JC dN/dS; nominal 0.23 and 0.80 in full, 0.50 and 1.00 clean cells only; the full 48 x 15 table, including the registered arms, is in `raw/l1c.transfer.out`):

| nominal omega | clustering | noise | truth (U0, clean cell) | U0 | UT | UD | PA | PAF1 | PL38 | PGB | PAF2 (stress) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.23 | 0 | clean | 0.216 | 0.216 | 0.216 | 0.217 | 0.216 | 0.216 | 0.216 | 0.216 | 0.147 |
| 0.23 | 0 | indel | 0.216 | 0.211 | 0.816 | 0.213 | 0.213 | 0.213 | 0.213 | 0.210 | 0.146 |
| 0.23 | 0 | misreg05 | 0.216 | 0.406 | 0.406 | 0.220 | 0.363 | 0.250 | 0.359 | 0.265 | 0.152 |
| 0.23 | 0 | misreg25 | 0.216 | 0.723 | 0.723 | 0.221 | 0.600 | 0.358 | 0.592 | 0.402 | 0.172 |
| 0.23 | 1 | clean | 0.211 | 0.211 | 0.211 | 0.212 | 0.211 | 0.210 | 0.211 | 0.211 | 0.130 |
| 0.23 | 1 | indel | 0.211 | 0.222 | 0.811 | 0.223 | 0.224 | 0.222 | 0.223 | 0.220 | 0.136 |
| 0.23 | 1 | misreg05 | 0.211 | 0.451 | 0.451 | 0.225 | 0.402 | 0.261 | 0.395 | 0.287 | 0.141 |
| 0.23 | 1 | misreg25 | 0.211 | 0.715 | 0.715 | 0.223 | 0.608 | 0.355 | 0.599 | 0.408 | 0.155 |
| 0.23 | 2 | clean | 0.218 | 0.218 | 0.218 | 0.219 | 0.218 | 0.190 | 0.218 | 0.218 | 0.078 |
| 0.23 | 2 | indel | 0.218 | 0.228 | 0.828 | 0.229 | 0.230 | 0.197 | 0.230 | 0.226 | 0.082 |
| 0.23 | 2 | misreg05 | 0.218 | 0.414 | 0.414 | 0.201 | 0.361 | 0.217 | 0.354 | 0.251 | 0.083 |
| 0.23 | 2 | misreg25 | 0.218 | 0.718 | 0.718 | 0.225 | 0.608 | 0.341 | 0.601 | 0.409 | 0.107 |
| 0.50 | 0 | clean | 0.446 | 0.446 | 0.446 | 0.452 | 0.446 | 0.446 | 0.445 | 0.446 | 0.299 |
| 0.50 | 1 | clean | 0.475 | 0.475 | 0.475 | 0.478 | 0.475 | 0.457 | 0.474 | 0.475 | 0.250 |
| 0.50 | 2 | clean | 0.473 | 0.473 | 0.473 | 0.474 | 0.467 | 0.256 | 0.466 | 0.411 | 0.088 |
| 0.80 | 0 | clean | 0.757 | 0.757 | 0.757 | 0.760 | 0.757 | 0.757 | 0.756 | 0.757 | 0.511 |
| 0.80 | 0 | indel | 0.757 | 0.768 | 0.919 | 0.776 | 0.764 | 0.763 | 0.763 | 0.762 | 0.514 |
| 0.80 | 0 | misreg05 | 0.757 | 0.800 | 0.800 | 0.744 | 0.749 | 0.724 | 0.747 | 0.730 | 0.491 |
| 0.80 | 0 | misreg25 | 0.757 | 0.898 | 0.898 | 0.788 | 0.795 | 0.723 | 0.789 | 0.744 | 0.495 |
| 0.80 | 1 | clean | 0.729 | 0.729 | 0.729 | 0.733 | 0.729 | 0.661 | 0.728 | 0.728 | 0.343 |
| 0.80 | 1 | indel | 0.729 | 0.729 | 0.914 | 0.733 | 0.725 | 0.656 | 0.724 | 0.722 | 0.341 |
| 0.80 | 1 | misreg05 | 0.729 | 0.804 | 0.804 | 0.743 | 0.753 | 0.664 | 0.752 | 0.733 | 0.340 |
| 0.80 | 1 | misreg25 | 0.729 | 0.911 | 0.911 | 0.778 | 0.799 | 0.670 | 0.793 | 0.745 | 0.363 |
| 0.80 | 2 | clean | 0.683 | 0.683 | 0.683 | 0.684 | 0.599 | 0.239 | 0.595 | 0.308 | 0.110 |
| 0.80 | 2 | indel | 0.683 | 0.651 | 0.889 | 0.650 | 0.565 | 0.239 | 0.562 | 0.296 | 0.113 |
| 0.80 | 2 | misreg05 | 0.683 | 0.756 | 0.756 | 0.675 | 0.651 | 0.278 | 0.644 | 0.342 | 0.122 |
| 0.80 | 2 | misreg25 | 0.683 | 0.862 | 0.862 | 0.680 | 0.733 | 0.378 | 0.724 | 0.469 | 0.146 |
| 1.00 | 0 | clean | 0.948 | 0.948 | 0.948 | 0.955 | 0.948 | 0.948 | 0.946 | 0.948 | 0.639 |
| 1.00 | 1 | clean | 0.915 | 0.915 | 0.915 | 0.922 | 0.913 | 0.792 | 0.913 | 0.907 | 0.401 |
| 1.00 | 2 | clean | 0.750 | 0.750 | 0.750 | 0.730 | 0.566 | 0.262 | 0.562 | 0.227 | 0.133 |

Scored statements, as printed:
```
Scored statements (docstring amendment 6):
  omega 0.80 cluster 0 clean    : realistic arms reading <= 0.40: none; stress arms: PAF2 0.511, PL16 0.756
  omega 0.80 cluster 0 indel    : realistic arms reading <= 0.40: none; stress arms: PAF2 0.514, PL16 0.763
  omega 0.80 cluster 0 misreg05 : realistic arms reading <= 0.40: none; stress arms: PAF2 0.491, PL16 0.735
  omega 0.80 cluster 0 misreg25 : realistic arms reading <= 0.40: none; stress arms: PAF2 0.495, PL16 0.767
  omega 0.80 cluster 1 clean    : realistic arms reading <= 0.40: none; stress arms: PAF2 0.343, PL16 0.728
  omega 0.80 cluster 1 indel    : realistic arms reading <= 0.40: none; stress arms: PAF2 0.341, PL16 0.724
  omega 0.80 cluster 1 misreg05 : realistic arms reading <= 0.40: none; stress arms: PAF2 0.340, PL16 0.742
  omega 0.80 cluster 1 misreg25 : realistic arms reading <= 0.40: none; stress arms: PAF2 0.363, PL16 0.774
  omega 0.80 cluster 2 clean    : realistic arms reading <= 0.40: ['PAF1', 'PGB']; stress arms: PAF2 0.110, PL16 0.487
  omega 0.80 cluster 2 indel    : realistic arms reading <= 0.40: ['PAF1', 'PGB']; stress arms: PAF2 0.113, PL16 0.454
  omega 0.80 cluster 2 misreg05 : realistic arms reading <= 0.40: ['PAF1', 'PGB']; stress arms: PAF2 0.122, PL16 0.506
  omega 0.80 cluster 2 misreg25 : realistic arms reading <= 0.40: ['PAF1']; stress arms: PAF2 0.146, PL16 0.597
```

### What it shows, both directions
**Day side: the mechanism exists in principle, and these arms can detect it.**
- At nominal 0.8 with clustering 2, realistic arms read far below the truth of 0.683 on the clean cell: PAF1 0.239 (-65%), PGB 0.308 (-55%); PA, PAG and PL38 0.586 to 0.599 (-12% to -14%). PAF1 stays at or below 0.40 in all four noise settings (0.239, 0.239, 0.278, 0.378); PGB in three (0.308, 0.296, 0.342; 0.469 under misreg25). A lenient divergence trim and the Gblocks rule do carry a high value into the published range when replacements sit in dense runs. The check was not built so that it could only find nothing. What the hit takes: 80% of replacements in 1% of codons, omega 64 inside a run, i.e. near-total replacement of 15-residue stretches in a fifth of genes. One level down (50% in 2% of codons, omega 20 inside runs) no realistic arm reaches 0.40 and four of five are within 1% of the truth. This row was **not blind** (seen in the selftest miniature).
- Plain frame-aware protein guidance with no trimming (PA) also reads low in that regime: -12% at nominal 0.8 and -25% at nominal 1.0 (0.566 against 0.750). Corrected in the fix pass (correctness finding 3): this is **not** the mechanism of Q181 ("gapped out or are left unaligned"). Gapping a 15-residue run would cost more than pairing it, and the aligner does not do it. In about a fifth of saturated runs the global alignment shifts part of the run by one or two residues because the shifted pairing scores higher by chance; PA then reads lower mainly because synonymous differences rise (reviewer, 1,344 genes of that cell: Sd +7%, Nd -6%, 0.03% of codons excluded). Any score-maximising aligner does this to unalignable sequence. It does not occur in real indel-free genes (PA differs from U0 in 3 of 16,545).
- At clustering 1 the lenient trim is already off: PAF1 -9.3% at nominal 0.8 and -13.5% at 1.0; -3.8% at 0.5.
- The bias also acts on a low truth: at nominal 0.23 with clustering 2, PAF1 reads 0.190 against 0.218 (-12.7%).
- The strict filter is biased everywhere: PAF2 reads about 32% low with no clustering at all, 38% to 56% low at clustering 1, 64% to 84% low at clustering 2.

**Critic side: without extreme clustering the arms return the truth, and the errors that inflate are the naive ones.**
- At clustering 0, every realistic arm is within 0.3% of the truth on the clean cell at every omega. At clustering 1, PA, PAG, PL38 and PGB are within 1%.
- At nominal 0.23 (truth 0.211 to 0.218), clean and indel cells: realistic arms read 0.210 to 0.230, except PAF1 at clustering 2 (0.190, 0.197).
- Misregistration inflates the unguided arm at a low truth: U0 reads 0.406 to 0.451 under misreg05 and 0.715 to 0.723 under misreg25, 3.3 times the truth. UD returns 0.201 to 0.225 in the same cells: the dS-window filter removes it.
- The gap-tolerant arm UT reads 0.811 to 0.828 under correctly gapped indels at a truth of 0.211 to 0.218, with only 15% of genes carrying an indel. That is the direction and the size of L1b's naive arm on real data (0.853).
- The protein arms repair misregistration only in part (misreg25, clustering 0, truth 0.216: PA 0.600, PL38 0.592, PGB 0.402, PAF1 0.358).
- The registered frame-0 arm P! reads 0.519 under correctly gapped indels at a truth of 0.216: BLOCKER-1 reproduced on synthetic data.

### Which clustering regime are real coding sequences in? (rewritten in the fix pass; correctness finding 2, Day review finding 4, critic review finding 3)
No within-gene clustering statistic was computed, and the identity bins (per gene) say nothing about clustering within genes. The committed gene table does bound the regime, in two halves that must be read together. Everything in this section is **post hoc and descriptive**, recomputed in the fix pass from `raw/l1c.genes.tsv.gz` and `raw/l1c.transfer.json`. "Indel-free" is the correctness review's rule: `fs_runs` = 0, `inframe_runs` = 0, `fs` = 0, `ins` = 0, `cov` = 1, `U0_gapfrac` = 0.

| | genes | share of all Nd | U0 | PA | PAG | PL38 | PGB | PAF1 | PAF1 codons dropped (share of the subset's U0 codons) | PAF2 (stress) |
|---|---|---|---|---|---|---|---|---|---|---|
| **indel-free genes** | 16,545 (85.7%) | 52.5% | 0.2045 | -0.19% | -0.19% | -0.39% | -0.40% | -0.70% | 407 in 95 genes (0.005%) | -25.5% |
| **genes with an indel run, an insertion, a coverage hole or a gapped codon** | 2,765 (14.3%) | 47.5% | 0.4247 | -4.8% | -5.2% | -5.7% | -7.7% | **-10.5%** | 13,887 (0.67%) | -42.8% |
| synthetic clean cells, clustering 2 (no indels; compare with the first row) | | | | | | | | -12.7% / -46% / -65% at nominal 0.23 / 0.5 / 0.8 | 0.086% / 0.53% / 0.80% | |
| synthetic clean cells, clustering 1 | | | | | | | | -0.4% / -3.8% / -9.3% | 0.003% / 0.061% / 0.225% | |

**Half 1: bounded, for the 16,545 genes with no length difference.** Like for like (the synthetic clean cells have no indels), the real PAF1 exclusion of 0.005% is 17 times below the lowest clustering-2 cell and sits between the clustering-1 cells at nominal 0.23 and 0.5. The realistic arms move the pooled value by 0.2% to 0.7% there; on the 11,397 indel-free genes of the real list (90% of the 12,724) by 0.04% to 0.6% (U0 0.1817; PA 0.1816, PGB 0.1812, PAF1 0.1807). PA differs from U0 in 3 genes (ZNF860, UGT3A1, UGT3A2). 97.2% of what PAF1 drops (13,887 of 14,294 codons) lies in the other 2,765 genes. So the 2% to 6% on ALL does not arise in genes without indels or holes. Two limits on this half, from the Day review: the subset is chosen on an outcome (no length difference, full coverage), so it is the set of genes least likely to hold dense runs and the bound does not transfer to the other half; and PA = U0 here is near automatic (same string, same register), not independent confirmation of anything.

**Half 2: open, for the 2,765 genes with indels or coverage holes.** They hold 47.5% of all nonsynonymous differences and read 0.4247 on U0. There the realistic arms read 4.8% to 10.5% lower, and PAF1 passes the 10% relative line. Fast-evolving regions are where indels are, so a dense real replacement run that coincides with an indel cannot be told from mispairing in these genes by anything measured here: x does not separate the two (correctness finding 1), and the fraction / p-ratio signature of PAF1's dropped codons in this subset (0.764 and 0.99) matches mispairing but was validated only on synthetic cells without indels inside runs (`transfer-excl` section). The check cannot say whether the 5% to 10% in these genes is error removed or signal removed. Half of PAF1's excluded Nd sits in 50 genes (53.7%; the first twelve are WDR87, MUC17, FLG, MUC3A, AC236972.4, SAMD9L, TCHH, AC242842.3, NBPF19, IGFN1, AHNAK2, ZNF227; chimp coverage as low as 0.22, identity 0.72 to 0.96); without those 50 genes U0 reads 0.2565, PAF1 0.2473 (-3.6%) and PGB 0.2494 (-2.7%).

**What both halves leave standing whatever the dropped codons are** (critic review finding 3): the total effect of the realistic arms is their measured drop, at most 5.8% on all genes and 3.7% on the real list; the 0.80-to-0.23 claim needs a factor of 3.5.

- The combination Day's reading needs in the synthetic table, a high true value together with extreme clustering, is a cell in which U0 itself returns the high value (0.68) because the generator gives it the true pairing; the real U0 reads 0.271. That comparison assumes the real U0 is as complete as the synthetic one, which is the open point of "The codons no arm sees" below, not something the transfer table can settle.
- Open follow-ups, not run: nonsynonymous differences per 15-codon window against a Poisson expectation from the segment dump, on the 2,765 genes; an external codon-aware pipeline from an independent chimp CDS annotation on the same genes.

### Predictions scored and what changes
| prediction | value | result |
|---|---|---|
| Day AM: some realistic arm reads <= 0.40 at true 0.8 | PAF1 and PGB at clustering 2 (0.239, 0.308; truth 0.683); none at clustering 0 or 1 | **hit**, at the extreme level only; not blind (seen in the selftest miniature) |
| Critic AM: realistic arms within 10% of truth on clean cells at clustering 0 and 1, every omega | 39 of 40 arm-cells within 10%; PAF1 at nominal 1.0, clustering 1: -13.5% (0.8, clustering 1: -9.3%) | **miss** (the one blind transfer prediction) |
| A10 (i) PA equals U0 on clean cells | equal at clustering 0 and 1 (largest gap 0.2%) and at 0.23 clustering 2; -1.4%, -12.4%, -24.5% at clustering 2 for 0.5, 0.8, 1.0 | **miss** (foreseeable from the miniature) |
| A10 (ii) UD within 5% of U0 on clean cells without clustering | +0.5% to +1.3% | hit |
| A10 (iii) U0 above truth by >= 25% under misreg25 | 3.3x at 0.23, +66% to +79% at 0.5; +19% to +26% at 0.8; -1% to +22% at 1.0 | **miss** at high omega (holds at 0.23 and 0.5) |

**Printed READINGS: unchanged.** The transfer mode does not rewrite them; the docstring has the table "reported beside" Reading B.
- Reading B. The docstring: "if no realistic arm takes 0.8 to <= 0.40 at any clustering, the mechanism is insufficient in principle; if one does only at the extreme level, the real-data question is whether realistic arms exclude that kind of codon (dS-normal, replacement-dense) in quantity, which the excluded-codon table answers." The second branch applies: PAF1 and PGB do it, at clustering 2 only. The docstring's test ("dS-normal, replacement-dense") is defective in one word: a saturated run is not dS-normal by the Nei-Gojobori pS (correctness finding 1), so the real-data question is answered here on quantity and on the fraction / p-ratio signature instead. Quantity: the realistic arms drop 0.08% to 0.23% of codons on all genes, 0.005% (PAF1) in indel-free genes against 0.80% in the cell that produces the hit. Signature: nonsynonymous fraction 0.71-0.77 and p-ratio about 1, against 0.94 and above with a p-ratio of 4.8 or more in synthetic dense runs. Not answered: the 2,765 genes with indels or holes (regime section). So the mechanism is **not** "insufficient in principle", and Reading B stays `contradicted` on band CRITIC and on quantity.
- Reading A. The docstring: "In principle (synthetic): the transfer table says for which clustering a realistic arm can move omega." Answer: strongly at clustering 2 (PAF1, PGB; PA, PAG, PL38 by 12% to 30% at nominal 0.8 and 1.0), mildly at clustering 1 (PAF1 only), not at clustering 0. The printed real-data value stays `contested`.
- **Bearing on DN6 Reading b.** No rule in the docstring ties the transfer table to the move, so it changes no proposal by rule. As evidence it cuts both ways: the mechanism of Q181-Q182 works on synthetic data with near-total replacement runs (PAF1, PGB), and it needs that extreme level to matter.

## Post hoc: what each arm drops on the synthetic cells (`transfer-excl`; fix pass, 2026-10-13)
**Post hoc, additive, decides no band, reading or verdict proposal.** Asked for by correctness finding 1. New mode `transfer-excl` in the same script (commit **6c5d8cf**, labelled "post hoc:", pushed before the run; no registered or amended function, constant or rule is changed; the mode reuses `_tf_one`, `agg` and `excl_agg` with the seeds of `transfer`). Windows and predictions X1-X5 are in the docstring. Run: na-workhorse, launched 2026-10-13 18:06:17 UTC, 2 workers (another job held 8 cores), 24 cells (clean and misreg25) x 2,000 genes x 300 codons, wall 16 min 6 s, peak RSS 182 MB, exit status 0. Host record `raw/l1c.transfer_excl.host` (script md5 `c61c39ba…`); outputs `raw/l1c.transfer_excl.out`, `raw/l1c.transfer_excl.json`.

**Blindness, as disclosed in the docstring:** the windows and predictions were written before any execution of the mode and not changed afterwards, but a 30-gene smoke test was run and seen before the commit (X3 5 of 5, X4 8 of 8), so commit order does not prove blindness. The correctness reviewer had already measured three of the clean cells in part. The real-data values were known when the windows were drawn (the MISPAIRING window was set around arm NU, 0.774 and 1.018, and the real realistic arms were known to fall inside it). This run is a confirmation at full size, not a blind test.

Windows fixed before the run (the audit's choice, like the 3x band), on the dropped codons' nonsynonymous fraction and p-ratio: MISPAIRING = fraction <= 0.80 and p-ratio <= 1.5; DENSE-RUN = fraction >= 0.90 and p-ratio >= 3.0; otherwise AMBIGUOUS. Scored for PAF1 and PGB where the arm drops at least 50 codons. x is the dropped codons' pS over the same cell's UD pS.

| prediction | result |
|---|---|
| X1 (audit) pooled dN/dS per arm equals the committed transfer table on every cell rerun | **hit**: maximum difference 0.000e+00 over 24 cells x 15 arms. The `transfer` table is reproduced from the committed script (answers correctness note 11 for these cells) |
| X2 (audit; not blind) clean, nominal 0.8, clustering 2: x > 3 for PAF1 and PGB | **hit**: 9.5 and 9.4. The amended DAY clause "x <= 3" was unreachable in that cell |
| X3 (critic side) every clean clustered cell is in DENSE-RUN for PAF1 and PGB | **hit**: 11 of 11 arm-cells with at least 50 dropped codons (5 arm-cells had fewer and are not scored) |
| X4 (critic side) every misreg25 clustering-0 cell is in MISPAIRING with x > 3 | **hit**: 8 of 8; x 62.6 to 64.6 |
| X5 (Day side) some clean clustered cell falls in MISPAIRING | **miss**: none |

Dropped codons, PAF1 / PGB (full table for eight arms in `raw/l1c.transfer_excl.out`):

| cell | codons dropped (share of U0) | pS | x | nonsyn fraction | p-ratio |
|---|---|---|---|---|---|
| clean, 0.23, clustering 2 | 513 (0.086%) / 9 | 0.013 / n.a. | 1.1 / n.a. | 0.990 / n.a. | 30.3 / n.a. |
| clean, 0.5, clustering 1 | 365 (0.061%) / 0 | 0.031 | 2.6 | 0.973 | 11.6 |
| clean, 0.5, clustering 2 | 3,171 (0.53%) / 844 (0.14%) | 0.062 / 0.058 | 5.0 / 4.7 | 0.963 / 0.969 | 8.5 / 9.8 |
| clean, 0.8, clustering 1 | 1,348 (0.225%) / 10 | 0.034 / n.a. | 2.8 / n.a. | 0.973 / n.a. | 11.6 / n.a. |
| clean, 0.8, clustering 2 | 4,806 (0.80%) / 4,170 (0.70%) | 0.121 / 0.120 | **9.5 / 9.4** | 0.948 / 0.949 | 5.9 / 5.9 |
| clean, 1.0, clustering 1 | 2,220 (0.37%) / 121 (0.02%) | 0.042 / 0.034 | 3.5 / 2.8 | 0.970 / 0.979 | 10.4 / 15.0 |
| clean, 1.0, clustering 2 | 4,447 (0.74%) / 5,218 (0.87%) | 0.177 / 0.176 | **13.4 / 13.3** | 0.937 / 0.937 | 4.8 / 4.8 |
| misreg25, clustering 0, four omegas | 14,029-15,149 (2.4-2.5%) / 13,031-14,338 | 0.75 | 62.6-64.6 | 0.752-0.757 | 0.99-1.02 |
| misreg25, clustering 2 (mixed), four omegas | 15,011-19,598 / 13,295-19,548 | 0.59-0.75 | 45.5-62.2 | 0.758-0.802 | 1.02-1.32 |
| **real data, ALL (realistic arms)** | 9,109-25,541 (0.08-0.23%) | 0.12-0.24 | 7.6-15.2 | 0.71-0.77 | 0.76-1.01 |

What it shows, both directions:
- **x fails as a discriminator, as the correctness review said.** In clean cells with dense runs x runs from 1.1 to 13.4 with the density of the runs; at nominal 0.8 and 1.0 with clustering 2 it is 9.4 to 13.4, inside the real-data range of 7.6 to 15.2. On x alone the real dropped codons could be saturated real replacement runs. Every sentence of the first version that read x > 3 as "misalignment" overstated, and the amended Day-side clause x <= 3 could not be met where his mechanism works. This is the audit's defect and it lay on Day's side.
- **The fraction / p-ratio pair separates the two on synthetic data.** Dense real runs: fraction 0.937 to 0.990, p-ratio 4.8 to 30. Misregistered stretches: fraction 0.75, p-ratio 1.0. No clean clustered cell falls in the MISPAIRING window. The real realistic arms on ALL (0.71-0.77; 0.76-1.01) fall inside it. On this evidence "what the realistic arms drop, pooled over all genes, looks like mispairing" may stand, resting on the pair and not on x.
- **Limits, for Day's side.** (i) The real dropped codons are not pure synthetic misregistration either: their pS is 0.12 to 0.24, where a shifted stretch gives 0.75 (x about 63). They are a mixture that the generator has no single cell for; the mixed cells (misreg25 with clustering 2) stay near the mispairing values (one of eight, PGB at nominal 1.0, is AMBIGUOUS: 0.802, 1.32), but no cell mixes a dense run with an indel inside it. (ii) By the same windows, on real dS-clean subsets the dropped codons are **AMBIGUOUS, not MISPAIRING** (fix-pass recomputation from the gene table): indel-free genes, PAF1 0.829 / 1.39 on 407 codons, PGB 0.917 / 2.20 on 170 codons; DSC, PAF1 0.813 / 1.34, PGB 0.832 / 1.46; HQs, PAF1 0.805 / 1.27, PGB 0.843 / 1.56. In the 2,765 genes with indels or holes they are in the MISPAIRING window (PAF1 0.764 / 0.99; PGB 0.757 / 0.94), and CSAC23 is borderline (PAF1 0.791 / 1.14; PGB 0.809 / 1.25). So the little that is dropped from clean genes is not classified, and the classification that holds is for the pool, which the 2,765 genes dominate. (iii) The stress arm PAF2 is in the DENSE-RUN window in every clean cell, including clustering 0 (fraction 0.975, p-ratio 13.5 at nominal 0.8), and on real dS-clean sets (0.92 to 0.95; 4.1 to 6.3): what it removes from clean genes is real replacement at ordinary synonymous divergence, not mispairing. (iv) The windows are the audit's, drawn with the real values known; the generator has uniform codon usage, kappa 1, runs of 15 codons.
- **For the critics' side.** Whatever the classification, the quantity is the bound: the realistic arms drop 0.08% to 0.23% of real codons (0.005% for PAF1 in indel-free genes), against 0.53% to 0.87% in the clustering-2 cells where they move the estimate by half or more.

## Interpretation
All six points carry the scope stated at the top: this genome alignment (Cactus), this annotation and the in-script aligner.
1. **Fidelity, from the held source and not from the run.** CSAC 2005's 13,454-gene 0.23 came from a BLASTZ genome alignment; Clustal W was used only for the 7,043-gene subset. A statement that the published 0.23 was produced by protein-guided alignment misreads the source (proposal `misread`, reading-dependent; top of this file and the Readings table).
2. On the hs1/mPanTro3 Cactus codons, an extraction with no protein guidance reads 0.271 on all genes and 0.219 on the real 2005 gene list (0.265 at CSAC's site ratio), with a nonsynonymous fraction of 0.426 against Day's "~40%" for the published row. On the codons Cactus pairs, the low value does not need a protein-guided step. This does not show what a protein-guided pipeline started from an independent chimp CDS would return, and it is silent on what Cactus left unpaired (1.40% of codons; Reading d, not tested).
3. Re-pairing the Cactus-paired codons with the in-script aligner, gap trimming, lenient divergence trimming, local segments or the Gblocks rule moves the pooled value by 0.006 to 0.016. The mechanism of Q181-Q182 exists in sign and is 2% to 6% in size here (1% to 4% on the real list): 0.2% to 0.7% in the 16,545 genes with no length difference, 5% to 10% in the 2,765 genes with indels or coverage holes.
4. What those arms remove, pooled over all genes, has the signature of mispaired sequence (nonsynonymous fraction 0.71-0.77, p-ratio about 1; a fifth to a quarter beside frameshift runs), not that of dense real replacement on synthetic data. This is not established for the 2,765 genes taken alone, where error removed and signal removed are not separated. Whichever it is, the size in point 3 is the whole effect.
5. The mechanism becomes large in two situations: a deliberately strict filter (PAF2, the audit's stress arm, minus a third; no pipeline is shown to use such a rule, and nothing was run between it and the lenient rule), and a register-broken input (0.853 to 0.340, 0.807 to 0.48). The second reproduces the pattern Day reports, "high without protein guidance, low with it". Register loss is a candidate error class with a real-data and a synthetic instance and five matched features of his table; his pipeline is unseen, and the dispute is over which input is right.
6. The gene list matters modestly: ALL is 24% above the real CSAC list. That is DN3's form of the claim, which Q186 sets aside.
7. The site model matters more than any alignment arm: transition-aware sites raise every value by about 40% (ALL 0.380 at kappa 5, 0.385 at kappa-hat, 0.015 under a line that was set for kappa 1). It does not approach 0.80 and does not change the band at kappa 1; on transition-weighted sites the answer for all genes depends on the kappa used and on the left-out codons.

## Proposed verdict moves (band CRITIC; proposals for integration only; no claim-file value is changed by this file)
The docstring's text: "new alignment-circularity claim external: DAY -> supported; HIGH-NOT-METHOD -> contradicted (mechanism) while DN1 -> contested; NOISE or CRITIC with flag none -> contradicted; CRITIC with flag small/moderate -> contested (direction real, size insufficient), with the numbers. DN1/DN3: as L1b's bands; L1c adds the method dimension, never overrides L1b's band on the same codons." The amendment keeps these ("Verdict proposals as registered") and adds moves only for bands not obtained here.

| claim | field | now | basis | proposal |
|---|---|---|---|---|
| DN6 | external (reading-dependent; field takes Reading b2) | `pending` | Readings table below; move sentence "CRITIC with flag small/moderate -> contested (direction real, size insufficient)" | **`contested`**, `reading-dependent:` comment listing a, b1, b2, d; the comment opens with the size (2% to 6% on all genes, 1% to 4% on the real list; 71% needed) and carries the three scope qualifiers |
| DN6 | fidelity (reading-dependent) | `pending` | held CSAC text (pre-run note in the docstring: "under the reading '0.23 was produced by protein-guided alignment' fidelity is `misread` regardless of this run") | **`misread`**, `reading-dependent:` comment (strict `misread`; broad `partial` / `unverifiable`), licensed by the held text before the run, not by the run |
| DN6 | internal | `pending` | none registered | not moved. The claim file names the missing observable (codons dropped and their dN/dS); this run supplies it for the audit's aligner only |
| DN1, DN3 | external | as L1b | "as L1b's bands ... never overrides" | **not moved by L1c** |
| DN3 | credit to Day | as L1b | credit rule (amendment 7): a set effect goes to the DN3 form | descriptive addition to L1b's restatement (real list: ALL / CSAC23 = 1.24, NOT23 - CSAC23 = +0.126); no value change |
| DN4, DN5 | all | | | not moved (the kappa line is offered to integration as a possible DN5 comment; no rule licenses a move) |

### Readings table for DN6 (rule RD: every plausible reading with its verdict)
| reading | content | external | fidelity | sets a field? |
|---|---|---|---|---|
| a | "This is how the Consortium's 0.23 was produced" (a protein-guided alignment). Q180 + Q182 + Q184 + Q186 jointly; said outright in the unfiled ¶14 | `contradicted` (held CSAC text; and on these data U0 reproduces 0.219 / 0.426 on the real list with no protein step) | **`misread`** | fidelity: yes |
| a-broad (Day review finding 8) | "A conservation-dependent alignment" (Q186) means any selection on alignment quality behind the 13,454 ("After removing low-quality sequences and likely alignment artefacts") | not scored here: a gene-set effect, credited to DN3 (real list 0.219 against 0.271 on all genes; NOT23 0.344) | `partial` or `unverifiable` until the SI criteria are held | no (see below) |
| b1 (critic review finding 1) | "At human-chimp divergence, protein-guided alignment lowers dN/dS by a material amount; the published human-chimp 0.23 is this artefact" | **`contradicted`** on this alignment, annotation and in-script aligner: realistic arms 2.3% to 5.8% (ALL), 1.3% to 3.7% (real list), all flags `none`; R1's line is 25%; 71% needed. This is the script's Reading B | n/a | no (see below) |
| b2 | "Protein-guided alignment excludes divergent codons, those codons are nonsynonymous-enriched, and dN/dS is lowered" (Q180-Q182 as written: a mechanism and a direction, no size) | **`contested`**: direction true in every arm; size 2% to 6% from realistic arms; 35% from the audit's stress arm, whose dropped codons are dS-normal on clean genes; large on synthetic near-total replacement runs; not tested from an independent chimp CDS or with an external aligner. This is the script's Reading A, as amended | n/a | external: yes |
| b2 as registered | the same, scored by the registered rule | "invalid as registered (BLOCKER-1)" as printed; `supported` only by substituting PAF2 for PF2 (the write-up's derivation) | n/a | no: shown beside the result of record with the docstring's precedence sentence as the reason |
| c | "The 0.80 (not the 0.23) is the correct value" | out of scope here (DN1) | | |
| d (Day review finding 2) | "The genome alignment that feeds the audit's U0 is itself the conservation-dependent step" | **not tested by L1c**. Bounded: cannot carry 0.80 or 0.65 unless the left-out 1.40% reads like unrelated sequence; a rise of the order of 10% is open. Test: follow-up (b), not run | n/a | no: extended (a different object from the protein alignment of Q180 and Q182; and the post's own ¶11 exempts the whole-genome alignment) |

**Which reading sets each field under RD, and why (no owner question; RD: "do not pick one reading").**
- *External: b2, `contested`.* RD puts the field on the reading "under which the speaker's *quoted statement* is most defensible (closest to literally true, best supported)", "not the reading that yields the best verdict for the speaker". Q180-Q182 as written state a mechanism and a direction and no size, and that is the reading under which they are closest to literally true: the direction holds in every arm. b1 is also a fair reading of the post (Q186 is about one gap, 0.7989 against 0.23), and its verdict is `contradicted`; it is the less defensible reading of the quoted words, so it is recorded and does not set the field. The critic review's objection is recorded with it: b2 as the claim file words it ("pipelines in general") is wider than the post, and after the amendment its rule has two outcomes and cannot lose. The answer adopted here is to word b2 as the quotes do, without "in general" and without "any size", so that it is not an extended reading; and to open the field's comment with the size, so that `contested` is not read as "half right". The correctness ruling 3b is the second ground: the docstring licenses `contested` and does not license `contradicted` for this reading.
- *Fidelity: a, `misread`.* Fidelity asks what the cited source did; only reading a makes a statement about the source. The broad reading is recorded beside it. It is the less defensible reading of the quoted statement on the quote's own words: Q186 says the difference is "not a matter of gene selection, quality filtering", which is what an alignment-quality selection of genes is. The claim file's present comment has the fidelity field follow Reading b (`n/a`); the proposal is that fidelity and external take their own readings, since they answer two questions.
- Counted as reading-dependent in both fields.

**Note on DN6 Reading b: what the licensed text gives (rewritten in the fix pass; correctness ruling 3b and finding 5).** The first version of this note counted "two of three routes" and cited RD for choosing between routes through a scoring rule. Both are withdrawn: RD chooses between readings of a quote, and the text gives one answer. Four grounds, from the docstring:
1. The flag in the move sentence is defined in the registration: "Mechanism-size flag, separately, for P, PF1 and PF2 on ALL and CSACp", with the gloss "CRITIC + mechanism small (PF1 or PF2) = Day's bias exists in direction but is an order of magnitude too small (credit Q180-Q182 Reading A, not B). CRITIC + none = no bias at human-chimp divergence." The sentence's flag therefore includes PF2. PF2 is `small`; its valid counterpart PAF2 is `small` / `moderate`. That is the branch "CRITIC with flag small/moderate -> contested (direction real, size insufficient)".
2. The amendment keeps the sentence ("Verdict proposals as registered") and nowhere restricts its flag to realistic arms. Amendment 8 restricts "Reading A", not the move sentence.
3. The amended Reading A rule has two values only, `supported` and `contested`; `contradicted` is outside its range, the script prints `contested`, and by the precedence sentence the amended reading governs where the texts disagree.
4. The gloss of the other branch, "no bias at human-chimp divergence", is not what was observed: the sign is Day's in every realistic arm.

Condition attached to the proposal (Day review finding 1): Reading b2 is not to be strengthened beyond `contested` until one external codon-aware pipeline has been run from an independent chimp CDS annotation, at least on the 2,765 genes with indels or holes. The docstring's "not needed for the verdict" for that queue item is superseded by this condition for any move past `contested`.

## Who this helps
**Day**
- Q182 is right in direction on real data: in every arm the dropped codons are nonsynonymous-enriched (0.71-0.85 against 0.479), and every realistic arm lowers dN/dS.
- A strict protein-score filter is not harmless: PAF2 removes 0.92% of codons and 37% of all nonsynonymous differences, and lowers the estimate by a third, on dS-clean gene sets as well, where what it drops is dS-normal by the audit's own band (x 1.6 to 2.8). Any pipeline with a filter of that kind would understate dN/dS by a material amount (R1's 25% line is passed). Qualifier from the critic review: no pipeline is shown to use such a rule; it deletes an isolated replacement with its neighbours when the replacement scores 0 or less beside common residues, so that it lowers dN is arithmetic, and the registration called it adversarial.
- On synthetic genes with near-total replacement of 15-residue runs (clustering 2: omega 64 inside a run) the lenient trim and the Gblocks rule read 55% to 65% below the truth: the mechanism of Q181-Q182 exists in principle and these arms can show it. Plain protein guidance (PA) reads 12% to 25% low in the same cells for a different reason (part of a saturated run re-paired out of register, synonymous differences up), not by gapping. The row was not blind.
- On a register-broken extraction the protein family lowers 0.85 to 0.34 or 0.19. His observation that the two kinds of pipeline disagree widely is reproducible; the dispute is over which input is right.
- The registered rule would have scored Reading A `supported` once a valid strict arm stood in for the invalid one. The `contested` comes from an amendment made after a miniature had shown that outcome, and it turns on the stress label alone.
- The amended Day-side clause "x <= 3" could not have been met even in the synthetic cell built to let the mechanism work. That is a defect of the audit's amendment and it was on his side of the table.
- The registered protein-guided arms were invalid as written. The audit's first design would have produced a wrong protein-guided result, and only the pre-run review caught it.
- The check never runs protein-guided alignment as practised (from each species' own CDS). Every protein arm re-pairs what Cactus already paired; on 85.7% of genes its agreement with U0 is near automatic.
- The aligner is the audit's own in-script code: not MACSE, PRANK, PAL2NAL, Clustal W or any pipeline Day has in mind. The X-drop values rest on unverified memory of BLAST defaults; the Gblocks rule is not validated against the binary.
- In the 2,765 genes with indels or coverage holes, which hold 47.5% of the nonsynonymous differences, the realistic arms read 5% to 10% lower and the check cannot say whether that is error or signal.
- The audit's headline depends on the site model: 0.271 becomes 0.385 at kappa-hat, 0.015 under the band line; the real CSAC list reads about 0.265 at CSAC's own site ratio, above 0.23.
- A gene-set effect exists on the real list (+24%, NOT23 0.344), his earlier DN3 point.
- No arm sees codons that Cactus does not align: 1.40% of annotated sense codons, concentrated in 351 genes, and the part of a gene that Cactus kept reads higher the more of it is missing (0.21 to 0.47 on dS-clean genes). For those codons to lift the pooled value to 0.80 at the observed pS they would need a pN of 0.67, close to unrelated sequence (0.73); for a rise of 10%, or for 0.40 on the kappa-5 line, they would need far less (Reading d, not tested).

**Critics**
- The published 0.23 was not made by a protein-guided alignment: the held CSAC text describes a BLASTZ genome alignment for the 13,454 genes and Clustal W only for the 7,043-gene subset. This needs no simulation.
- The low value needs no protein guidance on these data: 0.271 on all genes, 0.238 on one2one, 0.219 on 12,724 genes of the real 2005 list, from a nucleotide alignment, with the nonsynonymous share Day's own table gives for the published row.
- Whatever the realistic arms remove, signal or error, its total size is 2% to 6% on all genes and 1% to 4% on the real list, against the 71% the claim needs; in genes with no length difference it is under 1%.
- Pooled over all genes, what is removed carries the mispairing signature, and half of PAF1's share sits in 50 low-coverage, low-identity genes.
- Every route to 0.80 that this audit constructed is an error model, and each one carries about 74% nonsynonymous with an inflated pS. (L1b's counterpoint stands beside it: that share is what unconstrained sequence gives under either explanation.) Uniformity across gene sets is a property of the naive arm, not of the frame-preserving one, and under the naive arm it comes from 7% to 21% of genes that supply 95% to 97% of the differences.
- Synthetic: with no or moderate clustering the realistic arms return the truth at every omega (one exception, PAF1), and the naive arm reads 0.81 to 0.83 at a truth of 0.22 with correctly gapped indels in 15% of genes.

**Against the critics**
- The sign is Day's in every arm, and the mechanism-and-direction reading is `contested`, not `contradicted`. (No critic-side prediction required a zero effect: the registered wording was "within ±0.03" and "< 0.03", and both are met on the valid arm.)
- Synthetic miss: the critic-side "within 10% of truth" fails for PAF1 at nominal 1.0 with moderate clustering. It was the one blind transfer prediction.
- The uncorrected like-for-like is not theirs to claim: at CSAC's site ratio the real list reads 0.265, above 0.23, and all genes 0.328. On these data the critics' number is "0.22 to 0.27 on the 2005 list depending on the site model".
- "The aligner question is closed" is not shown: no external codon aligner was run. "Day's pipeline is register-broken" is not shown: candidate only.

**Against the audit**
- The registered protein arm was invalid (BLOCKER-1). The four registered critic-side predictions that name it fail on it and hold on the valid arm (PA 0.265 against 0.271; PAF1 drop 0.016; excluded share 0.13%; agreement 99.95%). The failure is the audit's implementation.
- The x discriminator, added by amendment, does not separate a saturated real run from misalignment; the first version of this write-up said "by construction a clustering-2 run has ordinary pS", which is false for the statistic measured and is withdrawn. The amended DAY clause that used it was unreachable.
- The amended Reading A has two outcomes and cannot come out `contradicted`; the registered one could not come out other than `supported`. Neither was a test that could fail in both directions.
- A10 fails: PA is not neutral under extreme clustering. Other audit misses: N/S at kappa-hat (2.40, not 2.6-3.0), the estimand ordering, CSACp against ALL (0.078, not within 0.06), UT (0.853, not 0.28-0.60). The stand-in CSACp was stricter than the real list (0.193 against 0.219): had the proxy stayed the source set, the low value would have been flattered by 0.026.
- The first version of this write-up gave the kappa margin as 0.02 (it is 0.015 at kappa-hat), the left-out share as 1.6% (1.40%), the pN needed as 0.58 (0.67; 0.60 on the uncorrected count), and called the amendment's "~17%" too small (it is right against CSAC's site ratio).

## Limits and caveats
1. **Follow-up (b) not run:** no external codon aligner (MACSE, PRANK with a codon model) is installed on any host, and no independent chimp CDS annotation is used; the queue item stays and is now a condition on any move past `contested`. Every protein-guided result is for the in-script Gotoh aligner (BLOSUM62, gap cost 10 + k) and this audit's trimming rules, applied to codons Cactus had already paired.
2. **BLAST defaults unverified** (gap costs, X-drop 38 / 16 from memory); TranslatorX behaviour unverified; Gblocks from its documentation only; F3x4 not modelled. The held CSAC quote for the 7,043-gene subset says "realigned using Clustal W"; it does not say whether proteins or nucleotides were aligned, and the docstring's gloss "protein-aware realignment (Clustal W)" has no quote under it.
3. **Day's pipeline unseen.** Nothing here shows what he ran. Register loss is a candidate error class.
4. The amendments are post hoc relative to the registration. They are blind to L1b and L1c data by commit order, not blind to L1 or to the selftest miniature. The classification of PAF2 as a stress arm was made after the miniature showed it reading low; PF2 was already called adversarial in the registration. The Day-side transfer prediction and A10 (i) were not blind either.
5. The Cactus-projected human frame stands in for a chimp annotation. Where the chimp CDS has a different exon structure no arm sees it. 1.40% of annotated sense codons are outside every arm.
6. One species pair at 1.2% synonymous divergence. Deeper comparisons and other aligners are not tested.
7. The identity-bin gradient and the A5 second clause are near automatic, and so is PA = U0 on indel-free genes. The x discriminator separates misalignment from moderately dense runs and not from saturated ones; the fraction / p-ratio pair that replaces it in this file was proposed by a reviewer after the run and checked post hoc on synthetic cells only (`transfer-excl`), with a generator that has uniform codon usage, kappa 1, runs of 15 codons and no indels inside runs. A mutation hotspot with elevated synonymous divergence is not modelled.
8. The kappa line mixes transition-aware sites with a JC correction; it is a sensitivity line, not an estimate, and its thresholds are not rescaled. (Correctness note 12, from the reviewer's memory and not verified against a held text: kappa-weighted sites with unweighted differences may be a published modification of Nei-Gojobori; to be checked at the next refresh.) The script applies ALL's integer kappa to every set.
9. CSAC23 covers 94.6% of the list; 663 accessions are absent from GENCODE v35. Membership reflects 2004 assembly coverage.
10. O121 comes from Ensembl's protein-tree orthology, itself protein-guided (docstring, amendment 10): an instance of Day's concern at the gene level. U0 on ALL uses none of it.
11. Columns, tables and sentences marked post hoc were computed for this write-up or its fix pass from the committed raw files. They are descriptive and score nothing. The indel-free subset and the left-out bins are outcome-defined.
12. The transfer table is synthetic: assumed rates, uniform codon usage, kappa 1, 300-codon genes, runs of 15 codons. Its clustering levels are design choices, not estimates of real proteins. U0 is exact in it by construction. `raw/l1c.host` has no line for the `transfer` launch (the json stores no script hash); the correctness reviewer's partial regeneration of three cells from the committed script agrees with the json, and the post hoc `transfer-excl` run reproduces the 24 cells it reruns (see its section). (The first version of this write-up, b9e83e0, reported the table as pending; it was collected in 9d61b8a.)
13. Two quotes used in this file are held locally and verified against the saved text but are not yet numbered quotes: the post's ¶11 and ¶14 (Day), and the BLASTZ sentence of the CSAC Methods. They should be filed at integration before any claim file cites them.
14. Q183 has no registered verdict rule ("numbers only"). On these data both of its readings come out against it (U0 not uniform; UT uniform because concentrated). A rule should be registered before the next check that touches it.

## Open
- Done in this pass: the synthetic check of what each arm drops (`transfer-excl`, post hoc).
- Three reviews done; this fix pass done. Integration is not done here (DN6 claim file and its Readings table, defeaters for each reading on both sides, QUEUE, REVIEW.md, filing of the two unnumbered quotes).
- Follow-up (b): an external codon-aware pipeline from an independent chimp CDS annotation, first on the 351 worst-covered genes and the 2,765 genes with indels or holes. Tests Reading d and half 2 of the regime question. Not run.
- A threshold dose-response between PAF1 and PAF2 on the PA path. Minutes of compute; not run in this pass (it needs the segment dump and a new arm, i.e. more than an additive report mode).
- Replacement density per 15-codon window against a Poisson expectation, on the 2,765 genes, from the segment dump. Not run.
- A registered verdict rule for Q183.
- Outside inputs, only with the owner's approval (ROADMAP): Day's per-gene table or median; his count of excluded codons and their dN/dS; the CSAC SI criteria for "likely alignment artefacts".
- Queue items unchanged: an ML codon model for the site ratio; the source for the kappa-weighted-site estimator.

## Review resolution (fix pass, 2026-10-13)
Reviews answered: `REVIEW-R4-L1c-correctness.md` (3429895; C1-C12), `REVIEW-R4-L1c-steelman-day.md` (02b87c6; D1-D10), `REVIEW-R4-L1c-steelman-critic.md` (8742998; K1-K9). Every MAJOR and MINOR is answered by id; the NOTEs are answered as well. Where the two steelman reviews conflict, both positions are recorded side by side as readings with their verdicts (hard rule 1; rule RD), and no reading is put to the owner as a question.

What this pass did not do: it changed no band, no printed reading, no hit / miss call, no registered or amended logic in the script, and no verdict value in any claim file. Every reviewer number used above was recomputed in this pass from the committed raw files (`raw/l1c.json`, `raw/l1c.genes.tsv.gz`, `raw/l1c.transfer.json`, `raw/l1b_x1_breakdown.json` / `.out`; one process, seconds, workstation) and is labelled post hoc. All reproduced, with these small differences: codons left out inside the 19,310 genes 129,715 here against the Day review's 130,047 (gene-table rounding; "about 130,000" is used); genes with nothing left out 13,773 or 16,666 depending on the cut-off, against the reviews' 13,307 (all three read 0.21); PGB without the top 50 genes -2.7% against the critic review's -2.8%. One new run was made, post hoc and additive (`transfer-excl`, commit 6c5d8cf before the run), reported in its own section.

Numbers corrected in place: kappa margin 0.02 -> **0.015** with U **0.385** at kappa-hat; pN needed in the left-out codons "near 0.58" -> **0.67** (0.60 on the first version's own count, which included the terminal stops); left-out share "about 1.6%" -> **1.40%**; "too small" for the amendment's ~17% withdrawn (17.2% against CSAC's site ratio, 28.7% against kappa 5); PAF1 at nominal 0.23 / clustering 1 is -0.4%.

### Correctness review
| id | sev. | ruling | reason and what changed |
|---|---|---|---|
| C1 | MAJOR | **Accepted** | The x discriminator does not separate a saturated replacement run from misalignment. "By construction a clustering-2 run has ordinary pS" and the regime-table column "ordinary synonymous divergence by construction" are deleted. "What the dropped codons are", Reading A's reasons, Interpretation 4 and the Critics bullet now rest the mispairing reading on the nonsynonymous fraction and p-ratio of the dropped codons, with x and the frameshift-run share as supporting facts, and limit it to all genes pooled. (c) is recorded three times: in the Day scoring row, in "Who this helps" (Day, and Against the audit) and in limit 7: the amended DAY clause x <= 3 was unreachable, a defect of the audit's amendment, on Day's side. The queued extension was run post hoc: `transfer-excl` (6c5d8cf), 24 cells. x is 9.5 / 9.4 in the saturated cell (X2) and 1.1 to 13.4 across dense-run cells; the fraction / p-ratio pair puts all 11 scored clean clustered arm-cells in the dense-run window and all 8 misregistered ones in the mispairing window (X3, X4 hit; Day-side X5 miss); not blind, as disclosed. It also shows that on real dS-clean subsets the dropped codons are AMBIGUOUS by the same windows, which is stated. |
| C2 | MAJOR | **Accepted**, with Day review D4 beside it | "Nothing in it fixes the regime on its own" and the unlike comparison (0.13% / 5.8% against 0.09% / 13%) are deleted. The regime section is rewritten in two halves with the subset rule stated: bounded for the 16,545 indel-free genes (realistic arms 0.2% to 0.7%; PAF1 exclusion 0.005% against 0.086% in the lowest clustering-2 cell); open for the 2,765 genes with indels or holes (47.5% of Nd; PAF1 -10.5%). The two open points are kept. The window statistic goes to Open (not run: it needs the segment dump on the host). |
| C3 | MINOR | **Accepted** | PA's shortfall under clustering 2 is described as re-pairing part of a saturated run out of register (Sd +7%, Nd -6%), not as gapping (Q181). In "Who this helps" PAF1 and PGB stay under Q181-Q182 and PA is described separately. A10 (i) is marked foreseeable. |
| C4 | MINOR | **Accepted** (lead ruling 1) | Result of record: the amended readings as printed (A `contested`, B `contradicted`). The registered value is reported as printed, "invalid as registered (BLOCKER-1)"; `supported` is stated to be the write-up's derivation by substitution of PAF2. "Rests on three things together" is corrected: the code rests on one. The missing fact is added: on indel-free genes PAF2 meets all three amended conditions (drop 25.5%, fraction 0.921, x 2.8), so the `contested` turns on the stress classification alone. Both values go to the Readings table with the precedence sentence. |
| C5 | MINOR | **Accepted** (lead ruling 2) | The "two of three routes" count and the RD citation for choosing between routes are withdrawn. The note now gives the four textual grounds of ruling 3b. RD is used only for the choice of reading. |
| C6 | MINOR | **Accepted** | 0.385 and 0.015 beside the integer values; DSC / HQs kappa-hat (5.91 / 5.93) and the 0.009 margin that goes with them; the docstring's "kappa = 1" quoted where the bands are stated; thresholds said not to be rescaled; both 17% and 29% given; "too small" withdrawn. ML-fit queue item kept. |
| C7 | MINOR | **Accepted** (lead ruling 10) | The Day transfer row reads "hit (kept as a hit; not blind ...)", A10 (i) "foreseeable from the miniature", and the critic-side transfer row is marked as the one blind transfer prediction. Limit 4 says so. |
| C8 | NOTE | Accepted | Tally by label added; the pS / Ud conjunction noted in the row. |
| C9 | NOTE | Accepted | "Near 0.58" replaced: 0.60 on the count with terminal stops (assumption stated: left-out codons get U0's split of sites), 0.67 with the stops removed. |
| C10 | NOTE | Accepted | The `cactus_frame` counts (1,228 genes; 2,596 frameshift and 2,843 in-frame runs) are cited beside the column. |
| C11 | NOTE | **In part** | Not done: appending to `raw/l1c.host` (this pass may touch only the write-up and new raw outputs). Done instead: limit 12 states the gap; the new `raw/l1c.transfer_excl.host` records host, date, script md5 and the md5 of `l1c.transfer.json`, and the rerun reproduces the 24 cells it covers (X1). |
| C12 | NOTE | Left as is | Recorded in limit 8 as unverified, for the next refresh (hard rule 8: not from memory). |

### Steelman review, Day's side
| id | sev. | ruling | reason and what changed |
|---|---|---|---|
| D1 | MAJOR | **Accepted** (lead ruling 8) | A scope paragraph opens the file and every conclusion carries "this genome alignment (Cactus), this annotation and the in-script aligner". (a) The PA agreement prediction is marked near automatic by construction on indel-free genes, not independent confirmation. (b) Interpretation 2 and 3 reworded; "cannot be what produces it" replaced by "does not need a protein-guided step on the codons Cactus pairs"; "now also on data" removed from the verdict table. (c) The condition is attached to the proposal: nothing past `contested` for Reading b2 until an external codon-aware pipeline has been run from an independent chimp CDS. |
| D2 | MAJOR | **Accepted in part** (lead ruling 4) | Accepted: Reading d is added to the Readings table; the gradient table, the needed-pN table and the worst-bin figure are in Results in their own section, recomputed; the 1.6% is corrected to 1.40%; the transfer section says U0 is exact by construction; the test is in Open. Not accepted as asked: Reading d is recorded as an **extended** reading that cannot set the field, with verdict "not tested by L1c". Reason: Q180 and Q182 name the protein alignment as the object, and the post's own ¶11 says the whole-genome alignment "doesn’t have this scoring bias", so the reading is his defender's and not his text's. The critics' reading of the same facts (critic K3) stands beside it. |
| D3 | MAJOR | **Accepted in part** (lead ruling 7) | (b) and (c) done: "What the arm names mean" says the labels are the audit's, that nothing was run between PAF1 and PAF2, and gives the arm-to-pipeline table with a source only where a repo file supports one (one arm of seven); PAF2's dS-normal dropped codons on clean genes are stated (x 2.8, 2.0, 1.6). The registered arm names are kept. (a) The threshold dose-response is **not run**: it needs a new arm on the real segment dump, which is more than an additive report mode; it is in Open. |
| D4 | MAJOR | **Accepted** (lead ruling 5) | Both halves, with the 2,765-gene row beside the indel-free row; the bound is worded "genes with no length difference"; the outcome-selection of the subset is stated; Interpretation 4 does not extend "looks like mispairing" to the 2,765 genes taken alone. |
| D5 | MINOR | **Accepted** | "Band by convention" table with the left-out rows; threshold asymmetry quoted beside it; 0.265 set beside "0.219 against 0.23" at the top, in the CSAC23 section and in the interpretation. |
| D6 | MINOR | **Accepted** | The printed string carries its gloss where it is explained; the order-of-events sentence is in the write-up for the claim file; a second tally limited to what L1c added is given for both sides (Day 2 hits, 1 empty, 4 misses). |
| D7 | MINOR | **Accepted**, all six rows | Interpretation 1 (now 2), Interpretation 4 (now 5: "the dispute is over which input is right"), "every route to 0.80 that this audit constructed" with L1b's counterpoint, the DN6 row, the Reading B paragraph (next clauses of the same source added), and the excluded-codon sentence (joined to its limit). |
| D8 | MINOR | **Accepted in part** (lead ruling 3) | Both fidelity readings are recorded (strict `misread`; broad `partial` / `unverifiable`). The field proposal is `misread`, not the broad reading: fidelity asks what the cited source did, and Q186's own words ("not a matter of gene selection, quality filtering") tell against the broad reading. The Clustal W point is accepted: limit 2 says the held quote does not say proteins and that the docstring's "protein-aware" gloss has no quote; the write-up itself never used the word. The docstring is not edited in this pass. |
| D9 | NOTE | Noted | Nothing to change. |
| D10 | NOTE | Accepted | Day's missing number is named in the register-loss section and in Open as an outside input, owner's approval required. |

### Steelman review, critics' side
| id | sev. | ruling | reason and what changed |
|---|---|---|---|
| K1 | MAJOR | **Accepted in part** (lead ruling 2; owner directive RD) | Accepted: Reading b is split in the Readings table (b1 human-chimp, material: `contradicted`; b2 mechanism and direction: `contested`); the objection that the amended Reading A cannot lose is recorded under "Result of record" and "Against the audit"; the field's comment is to open with the size. Not accepted: putting the choice to the owner, and b1 setting the field. Reasons: RD forbids asking the owner to pick; the correctness ruling 3b finds that the docstring licenses `contested` and not `contradicted` for this reading; and b2, worded as Q180-Q182 are written (no "in general", no "any size"), is not an extended reading but the one under which the quoted words are closest to literally true. b1 keeps its `contradicted` in the table. |
| K2 | MAJOR | **Accepted** (lead ruling 3) | Fidelity `misread` is proposed, stated second in the file (after the status line) and as Interpretation 1, with the CSAC quotes and their locators and with what Day's filed quotes do and do not say. The sentence that U0 reproduces both figures of the "Published" row is added. The verdict table reads "licensed by the held text before the run". The Day review's broad reading is recorded beside it under RD. |
| K3 | MAJOR | **Accepted**, with Day review D2 / D4 beside it | The size bound is stated wherever the question "signal or misalignment" is raised (excluded-codon section, regime section, Interpretation 4, Critics bullets): if all of it is signal the bias is 2% to 6% (1% to 4% on the real list). The left-out bound is in Results with 0.67 and 0.48 and the profile of the 351 genes. Reading A's former item 3 now says what the one pair showed (an upper bound). Not adopted: "the regime hedge is unjustified"; the hedge is kept for the 2,765 genes, as the correctness review and the Day review both ask. |
| K4 | MAJOR | **Accepted** (lead ruling 9) | Own section "The naive arm against Day's table" with the five features, the affected / unaffected table (recomputed) and the L1b breakdown (verified). Wording: "candidate error class"; it cannot identify Day's pipeline. L1b's Day-side counterpoint and the single-difference miss (60.1% against 71.6%) are kept in the same section. The outside input is named for ROADMAP. |
| K5 | MINOR | **Accepted in part** (lead ruling 10) | Accepted: the transfer row is labelled not blind everywhere and the tallies say "1 of them not blind"; the omega-64 description and "no pipeline is shown to use such a rule" are added to the Day bullets. Not accepted: taking the row out of the hit count. The prediction was registered before the full table and the table met it; it stays a hit with its label, as the correctness review asks. |
| K6 | MINOR | **Accepted** | "Against the critics and the audit" is split in two. The invalid-arm bullet is under "Against the audit" and says the four predictions hold on the valid arm. "No bias is not shown" is replaced by a sentence that no critic-side prediction required a zero effect. |
| K7 | MINOR | **Accepted** | One paragraph under "Result of record" states both directions: what the amendment cost Day, and what the registered sentence read on realistic arms alone would have given the critics. |
| K8 | NOTE | Accepted | Limit 14 and Open: a verdict rule for Q183 before the next check that touches it. |
| K9 | NOTE | Accepted | The four "should not claim" points are in "Against the critics". |

### Conflicts between the steelman reviews, and how each is recorded
| question | Day review | critic review | recorded as |
|---|---|---|---|
| Which reading sets DN6 external | b stays `contested`, not strengthened | b1 `contradicted` should be able to set the field | both in the Readings table; field b2 `contested` under RD and correctness ruling 3b; b1 `contradicted` recorded |
| Fidelity | two readings, broad `partial` / `unverifiable` | `misread`, proposed now, stated first | both in the Readings table; field `misread` |
| Left-out codons / Cactus as a prior filter | Reading d, open for about 10% and for the kappa margin | cannot reopen 0.80; 351 genes are noisy | side by side in one section; Reading d "not tested by L1c", extended |
| Regime | open in the 2,765 genes | bounded where the published number lives; moot given the size | two halves plus the size bound |
| PAF2 / "stress" | label alone decides Reading A | adversarial by registration; no pipeline uses it | both stated; labels are the audit's; dose-response open |
| Transfer hit | scored at equal weight | not a prediction | hit, labelled not blind |
| Register loss | "the dispute is over which input is right" | undersold | own section; candidate error class |

Not blind in this pass: the author of the fix pass had read all three reviews and their numbers before recomputing them.
