# R4 L1c: does the alignment method manufacture a low human-chimp dN/dS? Day's "protein-guided alignment gaps out divergent codons" tested on the T2T codons of L1b

**Status: main run done and written up; NOT reviewed (three post-run reviews owed: correctness, steelman-day, steelman-critic); NOT integrated. The synthetic `transfer` table was still running when this was written and is reported as pending.** Band **CRITIC** on the registered rule and on the amended rule, on both source sets. Tier: not load-bearing by the ROOT path (docstring, TIER), kept at three reviews because it decides DN6's external verdict.

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
- Script `research/checks/l1c_alignment_method.py`. Registration **536b19b** (2026-10-12 11:58 -06:00; only a synthetic selftest had run). Pre-run design review `results/REVIEW-R4-L1c-prerun.md` (**017dea9**: 1 BLOCKER, 9 MAJOR, 12 MINOR, with its resolution table). Amendments **0e0e840** (2026-10-12 15:07 -06:00), labelled "post hoc (pre-run, no data seen)". No later commit touches the script; its md5 here equals the one recorded on the host (`2692334e…`).
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
Codons compared in U0 and not in the arm. x is the pS of the dropped codons over the pS of the dS-clean arm UD (0.0156); the band fixed before the run reads x <= 3 as ordinary divergence and x > 3 as misalignment. The last two columns are **post hoc and descriptive**, computed here from `raw/l1c.json`.

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
- **Size.** The realistic arms drop 0.08% to 0.23% of codons and 2.5% to 6.4% of the nonsynonymous differences. Carrying 0.80 to 0.23 by exclusion alone needs about 71% of them removed with pS unchanged (post hoc arithmetic: 1 - 0.23/0.80).
- **What the dropped codons are.** Their pS is 7.6 to 15.2 times the dS-clean pS (0.12 to 0.24 against 0.0156), and 12% to 25% of them lie within 10 codons of a Cactus frameshift run. On the band fixed before the run that is the signature of misalignment, not of fast protein evolution at ordinary synonymous divergence. Their dN/dS is 0.76 to 1.01, not above 2. (UD's own x of 26 is by construction: UD selects on synonymous differences.)
- **"pN needed for 0.80" (post hoc).** Hold the kept codons and the overall pS as observed. For the all-codon p-ratio to be 0.80 instead of 0.274, the dropped codons would have to carry 236,625 more nonsynonymous differences than the 122,939 observed in all of U0. Per nonsynonymous site of the dropped codons that is the value in the last column. A proportion cannot exceed 1, and unrelated sequence gives about 0.73 (arm NU). For every valid arm the requirement is impossible (1.23 to 11.5). This bounds what these arms exclude; it says nothing about codons no arm sees (limits, below).
- **The stress arm is not small.** PAF2 drops 0.92% of codons carrying 37.3% of all nonsynonymous differences and lowers the estimate by a third, on dS-clean gene sets too (HQs 0.204 to 0.154; DSC 0.218 to 0.161). It drops the neighbourhood of any radical replacement by design.

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
- Every route to about 0.80 on these data carries a nonsynonymous fraction of 0.72 to 0.77 and a pS at least 3.7 times U0's. The no-constraint fraction N/(N+S) is 0.770 at the NG site ratio. Day's rows give 73.8% to 74.4% (Q183, Q184); his pS or identity is not published.
- Conversion printed by the script: Day's 73.9% is Nd/Sd 2.83, which is dN/dS 0.80 at N/S 3.54, 0.85 at 3.34 and 1.02 at CSAC's 2.78.
- **Post hoc, descriptive (read off the printed table):** UT is close to uniform across sets (0.853 / 0.844 / 0.800 / 0.827 on ALL / O121 / CSACp / CSAC23; nonsynonymous fraction 0.743 / 0.741 / 0.730 / 0.738; NOT23 0.748), as Day's table is (0.7989 / 0.7956 / 0.7939; 73.9 / 73.8 / 73.8%; C 74.4%). U0 is not uniform (0.271 / 0.238 / 0.193 / 0.219; fraction 0.479 / 0.446 / 0.395 / 0.426). This is a resemblance, not a location of Day's method: L1b's registration names naive extraction a candidate only.

Protein family applied to extractions that read high (amendment 6 ii; pooled JC):

| input | raw | PA | PAF1 | PL38 | PGB |
|---|---|---|---|---|---|
| NM 1.0 (every gene misregistered) | 0.807 | 0.644 | 0.495 | 0.478 | 0.588 |
| NR 0.02 | 0.634 | 0.631 | 0.627 | 0.630 | 0.629 |
| NR 0.05 | 0.776 | 0.774 | 0.765 | 0.773 | 0.772 |
| UT through the registered P / PF1 / PF2 (valid for this purpose: UT is the frame-0 reading) | 0.853 | P 0.535 | PF1 0.340 | PF2 0.190 | |

A protein-guided realignment with trimming does take a high value down by a large amount when the input is frame-broken (0.853 to 0.340 with the lenient rule, 0.807 to 0.48-0.49), and does nothing to uniform base error. On the frame-preserving input it has almost nothing to remove.

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

The floor fixed before the run was 85%; it is met, so CSAC23 is the source set for the amended band and CSACp is descriptive. U0 on CSAC23 is **0.219** (NM route only: 0.218), against the published 0.23 (Q184's last row). The stand-in CSACp reads lower (0.193): the proxy was stricter than the real list. Genes outside the list (NOT23) read 0.344, one2one genes outside it (O121NOT23) 0.285. ALL over CSAC23 is 1.24 (post hoc ratio). The docstring's credit rule sends a set effect to the DN3 form of the claim, not to Q186. Limit stated in the amendment: the 2005 membership partly reflects panTro1 coverage.

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

What the 0.38 is: the same codons, the same differences, a transition-weighted site count at the integer kappa nearest kappa-hat (5). With fewer nonsynonymous sites per synonymous site, every arm rises by the same factor of about 1.40, so the gaps between arms keep their proportions and the band stays CRITIC (U 0.380, Uc 0.307, Ud 0.370, Rmin 0.358).

What it is not: it is not an alignment effect, not a move toward Day's method (the naive arm rises too, to 1.22), and not CSAC's estimator. CSAC used codeml F3x4 with N/S 2.78; kappa 5 gives N/S 2.40, past it. The estimator mixes transition-aware sites with a Jukes-Cantor correction, and kappa-hat from fourfold sites is not checked against an ML fit (no ML tool; queue item stays).

What it costs the audit: the headline 0.271 depends on the site model. At kappa-hat the band holds with a margin of 0.02 under the 0.40 line (0.009 at kappa 6). The amendment's own statement that NG "reads ~17% below a transition-aware estimate" is too small on these data: 0.271 is 29% below 0.380. On the real CSAC list the value at CSAC's own site ratio would be about 0.265 (post hoc), 15% above the published 0.23 and inside the registered 0.18-0.30 range.

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

- **Registered band.** CRITIC needs U < 0.40 and Uc < 0.40 on U0 (0.271; CSACp 0.193). Neither clause uses PF1, so the registered band does not rest on the invalid arm here.
- **Amended band.** First applicable line of the decision tree: U 0.271 and Uc 0.219 (CSAC23), both below 0.40. NOISE, GENE-SET, HIGH-NOT-METHOD, DAY, HIGH-PARTIAL-METHOD and MIDDLE all need U >= 0.40 and are not reached.

### The readings in plain words (rule RD)
**Reading A: "protein-guided pipelines can bias dN/dS down, by any amount."** Printed `contested (no realistic arm lowers dN/dS)`. "Lowers" means a flag of at least `small` (0.03 absolute or 10% relative). The five realistic arms lower the value by 0.006 to 0.016 (2.3% to 5.8%), all under that line. The `contested` rests on three things together:
1. the drops are real in sign in every realistic arm but below the smallest flag;
2. the codons removed are nonsynonymous-enriched (Day's Q182, true in direction) but dS-saturated (x 7.6 to 15.2 against the 3x band), so by the amended rule even a larger drop of this kind would count as noise removal, not as a conservation bias;
3. the amended rule gives `contested`, not `contradicted`, when no realistic arm lowers it: the reading is general, and this run tests one aligner, five rules and one species pair at 1.2% divergence.

Upper bound from the stress arms: PAF2 0.094 (34.8%), PL16 0.009. They decide nothing under the amendment.

**Registered against amended, a disagreement that matters to Day.** The registered Reading A rule was: supported "if any of P/PF1/PF2 has mechanism flag >= small with excluded nonsyn fraction > U0's". PF2 has flag `small` (0.081) and its excluded codons a fraction of 0.762 against 0.479. As registered, Reading A scores **`supported`**, on an arm that is invalid as registered; its valid counterpart PAF2 meets the same rule (0.094; 0.846). The amendment (MAJOR-9, made before the run) restricted Reading A to realistic arms, where it scores `contested`. The registration itself called PF2 adversarial ("it removes nonsynonymous changes because they are nonsynonymous"), and the selftest miniature had shown PAF2 reading 30-38% low before the amendment (docstring, NOT BLIND). By the amendment's own rule the amended result is the one proposed; the registered one is shown here with the reason. The reviewers should rule on it.

**Reading B: "the published 0.23 is this artefact."** Printed `contradicted`. Registered rule: contradicted under CRITIC with the PF2 flag below `large` (it is `small`). Amended rule: contradicted under CRITIC when no realistic arm has a `large` flag (all are `none`). The two agree. Independently of the run, the held CSAC text says the 13,454-gene value came from a nucleotide genome alignment. The amended rule asks for the transfer table beside Reading B; it is pending.

**Q183.** Reading A (uniformity shows the gap is not gene-list driven): on U0 the sets are not uniform (0.193 to 0.344). Reading B (73.8% is the misalignment signature): NU 0.774, NM 1.0 0.739, NR 0.05-0.10 0.724-0.742, UT 0.743, against U0's 0.479. Neither reading has a registered verdict rule; numbers only. **Q185** is not decidable here (Day's run on the smaller subset is unpublished); CSAC23 is now the real list, not a proxy. **Q186** ("not ... computational error") bears through the noise arms and identity bins above; no verdict rule was registered for it beyond the band.

## Scoring of the predictions
Hits and misses with equal weight. Where a registered prediction names an arm that is invalid as registered, the registered arm is scored as printed and the frame-aware counterpart beside it. "Pending" = needs the transfer table.

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
| AM: pS <= 0.023 | 0.0177 | **hit** |
| AM: a realistic arm with a large flag, excluded codons x <= 3 and dN/dS >= 2 | all `none`; x 7.6-15.2; dN/dS 0.76-1.01 | **miss** |
| AM: CSAC23 within 0.05 of ALL on U0 | 0.219 against 0.271: 0.052 | **miss**, by 0.002 |
| AM: transfer, some realistic arm <= 0.40 at true 0.8 | | pending |

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
| AM: PA within ±0.01 of U0; agreement >= 99.5% | 0.006; 99.95% | hit |
| AM: every realistic arm `none` on both flags | none on ALL, CSACp, CSAC23 | hit |
| AM: realistic excluded share < 1% of U0 codons | 0.08-0.23% | hit |
| AM: with x > 3 | 7.6-15.2 | hit |
| AM: CSAC23 0.18-0.30 on U0 | 0.219 | hit |
| AM: NOT23 above CSAC23 by >= 0.10 | +0.126 | hit |
| AM: NM(1.0) p-ratio >= 0.60; NU nonsyn fraction 0.68-0.80 | 0.861; 0.774 | hit |
| AM: NM(1.0)>PAF1 at least 0.25 below NM(1.0) | 0.807 to 0.495 (-0.313) | hit |
| AM: transfer, realistic arms within 10% of truth on clean cells | | pending |

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
| A10 transfer checks | | pending |

Tally (excluding pending and the uncounted restatement): Day side 3 hits, 1 empty, 9 misses. Critic side: 14 hits; 4 further registered predictions name the protein arms that are invalid as registered and fail there (3 misses, 1 met with the wrong sign) while holding on the frame-aware counterparts. Audit: 12 hits, 4 misses, and 1 split (A5 first clause: miss on the registered arm, hit by 0.01 on PAF1).

## Transfer table (synthetic; amendment 6 i)
**Pending: transfer run not finished at the time of writing.** `raw/l1c.transfer.out` on na-workhorse was empty at both collection attempts (start and end of this write-up) and `raw/l1c.transfer.json` did not exist. Nothing from it is used above. Owed when it lands: the table (`transfer-report <json>`), the three pending predictions (Day AM, critic AM, A10), and the in-principle half of Readings A and B. Known beforehand and not blind (docstring): in the 100-gene miniature, at true 0.8 with 80% of replacements in 1% of codons, PAF1 read 0.25 and PGB 0.29 against a truth of 0.66, so a realistic arm can carry a high value to the published range when replacements are extremely clustered.

## Interpretation
1. On the hs1/mPanTro3 Cactus codons, an extraction with no protein guidance reads 0.271 on all genes and 0.219 on the real 2005 gene list. The low value is there before any protein-guided step, so on these data the protein-guided step cannot be what produces it.
2. Adding protein guidance, gap trimming, lenient divergence trimming, local segments or the Gblocks rule moves the pooled value by 0.006 to 0.016. The mechanism of Q181-Q182 exists in sign and is 2% to 6% in size here.
3. What those arms remove looks like misalignment (pS 8 to 15 times normal, a fifth to a quarter beside frameshift runs), not like fast-evolving protein at ordinary synonymous divergence.
4. The mechanism becomes large in two situations: a deliberately strict filter (PAF2, minus a third), and a frame-broken input (0.853 to 0.340, 0.807 to 0.48). The second reproduces the pattern Day reports, "high without protein guidance, low with it", but the high value is then the extraction's, not the genome's.
5. The gene list matters modestly: ALL is 24% above the real CSAC list. That is DN3's form of the claim, which Q186 sets aside.
6. The site model matters more than any alignment arm: transition-aware sites raise every value by about 40% (ALL 0.38). It does not approach 0.80 and does not change the band.

## Proposed verdict moves (band CRITIC; exactly as the docstring licenses; proposals only, the owner decides; three reviews owed)
The docstring's text: "new alignment-circularity claim external: DAY -> supported; HIGH-NOT-METHOD -> contradicted (mechanism) while DN1 -> contested; NOISE or CRITIC with flag none -> contradicted; CRITIC with flag small/moderate -> contested (direction real, size insufficient), with the numbers. DN1/DN3: as L1b's bands; L1c adds the method dimension, never overrides L1b's band on the same codons." The amendment keeps these ("Verdict proposals as registered") and adds moves only for bands not obtained here.

| claim | field | now | licensed rule | value | proposal |
|---|---|---|---|---|---|
| DN6 | external, Reading a of the claim file (= Q180-182 B: the 0.23 was produced this way) | `contradicted` from the CSAC text | Reading B `contradicted` under CRITIC with no large flag | CRITIC; largest flag small / moderate (stress arm) | **stays `contradicted`**, now also on data: U0 on the real list reads 0.219 with no protein guidance |
| DN6 | external, Reading b (= Q180-182 A: protein-guided pipelines in general bias dN/dS down); the verdict field takes this reading (RD) | `pending` | see below: the move sentence gives two values depending on which flags count | realistic flags all `none` (drops 0.006-0.016); stress PAF2 small / moderate (0.094, 34.8%); registered PF2! small / moderate | **`contested`**, with the numbers, `reading-dependent:` comment; see the note |
| DN6 | internal | `pending` | none registered | | not moved. The claim file names the missing observable (codons dropped and their dN/dS); this run supplies it for the audit's aligner only |
| DN6 | fidelity | `pending` | pre-run note: under the reading "0.23 was produced by protein-guided alignment" fidelity is `misread` regardless of this run; under the charitable reading the test is U0 CSACp against U0 ALL | 0.193 against 0.271 (real list 0.219) | no value licensed by the run; the numbers go in the comment. A set effect is credited to DN3 |
| DN1, DN3 | external | as L1b | "as L1b's bands … never overrides" | band CRITIC, same as L1b | **not moved by L1c** |
| DN3 | credit to Day | as L1b | credit rule (amendment 7): a set effect goes to the DN3 form | real list: ALL / CSAC23 = 1.24, NOT23 - CSAC23 = +0.126 | descriptive addition to L1b's restatement; no value change |
| DN4, DN5 | all | | not moved | | not moved |

**Note on DN6 Reading b: the licensed text does not give one answer.**
- Move sentence with the flags as registered (P, PF1, PF2): PF2 `small` gives "CRITIC with flag small/moderate -> contested (direction real, size insufficient)". The arm is invalid as registered; PAF2 gives the same.
- Move sentence with realistic arms only (amendment 8 restricts Reading A to them and says stress arms decide nothing): all `none` gives "CRITIC with flag none -> contradicted".
- Printed Reading A under the amended rule: `contested`.

Two of the three routes give `contested`, and rule RD puts the field on the reading most defensible for the speaker, so `contested` is proposed. The amendment did not say which flags the move sentence uses. That is a gap in the amendment, recorded here, for the reviewers and the owner.

## Who this helps
**Day**
- Q182 is right in direction on real data: in every arm the dropped codons are nonsynonymous-enriched (0.71-0.85 against 0.479), and every realistic arm lowers dN/dS.
- A strict protein-score filter is not harmless: PAF2 removes 0.92% of codons and 37% of all nonsynonymous differences, and lowers the estimate by a third, on dS-clean gene sets as well. Any pipeline with a filter of that kind would understate dN/dS by a material amount (R1's 25% line is passed).
- On a frame-broken extraction the protein family lowers 0.85 to 0.34 or 0.19. His observation that the two kinds of pipeline disagree widely is reproducible; the dispute is over which input is right.
- Under the registration as written, Reading A scores `supported` (through PF2 / PAF2). The `contested` comes from an amendment.
- The registered protein-guided arms were invalid as written. The audit's first design would have produced a wrong protein-guided result, and only the pre-run review caught it.
- The aligner is the audit's own in-script code: not MACSE, PRANK, PAL2NAL, Clustal W or any pipeline Day has in mind. The X-drop values rest on unverified memory of BLAST defaults; the Gblocks rule is not validated against the binary.
- The 3x pS band that classifies dropped codons as misalignment is the audit's choice. The registered (invalid) arms sit close to it (x 3.3 to 4.0).
- The audit's headline depends on the site model: 0.271 becomes 0.38 with transition-aware sites, 0.02 under the band line; the real CSAC list reads about 0.265 at CSAC's own site ratio, above 0.23.
- A gene-set effect exists on the real list (+24%, NOT23 0.344), his earlier DN3 point.
- No arm sees codons that Cactus does not align. Post hoc and approximate: the annotation holds 33,505,272 CDS bp (about 11.17 M codons) in 19,407 chosen genes and U0 compares 10.99 M codons in 19,310, so at most about 1.6% of annotated codons are outside every arm. For them to lift the pooled value to 0.80 at the observed pS they would need a pN near 0.58, close to unrelated sequence (0.73). Open in principle, and then indistinguishable from non-orthologous sequence.

**Critics**
- The low value needs no protein guidance: 0.271 on all genes, 0.238 on one2one, 0.219 on 12,724 genes of the real 2005 list, from a nucleotide alignment.
- Frame-aware protein guidance pairs 99.95% of codons as Cactus does and moves the value by 0.006. Realistic trimming removes 0.08-0.23% of codons.
- What is removed is dS-saturated, and a fifth to a quarter of it lies beside frameshift runs.
- Every route to 0.80 on these data is an error model, and each one carries about 74% nonsynonymous with an inflated pS. Uniformity across gene sets is a property of the naive arm, not of the frame-preserving one.
- Fidelity: the held CSAC text describes a BLASTZ genome alignment for the 13,454 genes; Clustal W only for the 7,043-gene subset.

**Against the critics and the audit**
- "No bias" is not shown: the sign is Day's in every arm, and the general claim is `contested`, not `contradicted`.
- Four registered critic-side predictions fail as registered, because the arm they name was invalid. They hold only on the amended arm.
- Audit misses: N/S at kappa-hat (2.40, not 2.6-3.0), the estimand ordering, CSACp against ALL (0.078, not within 0.06), UT (0.853, not 0.28-0.60). The stand-in CSACp was stricter than the real list (0.193 against 0.219): had the proxy stayed the source set, the low value would have been flattered by 0.026.
- The amendment's "~17%" for the NG shortfall is 29% here.

## Limits and caveats for the reviewers
1. **Follow-up (b) not run:** no external codon aligner (MACSE, PRANK with a codon model) is installed on any host; the queue item stays. Every protein-guided result is for the in-script Gotoh aligner (BLOSUM62, gap cost 10 + k) and this audit's trimming rules.
2. **BLAST defaults unverified** (gap costs, X-drop 38 / 16 from memory); TranslatorX behaviour unverified; Gblocks from its documentation only; F3x4 not modelled.
3. **Day's pipeline unseen.** Nothing here shows what he ran. The UT resemblance is descriptive.
4. The amendments are post hoc relative to the registration. They are blind to L1b and L1c data by commit order, not blind to L1 or to the selftest miniature. The classification of PAF2 as a stress arm was made after the miniature showed it reading low; PF2 was already called adversarial in the registration.
5. The Cactus-projected human frame stands in for a chimp annotation. Where the chimp CDS has a different exon structure no arm sees it.
6. One species pair at 1.2% synonymous divergence. The general form of Reading A (deeper comparisons, other aligners) is not tested.
7. The identity-bin gradient and the A5 second clause are near automatic; the pS-based discriminator is the informative one, and it assumes that local synonymous saturation marks misalignment rather than a mutation hotspot. x of 7 to 15 leaves room, but the assumption is not tested here.
8. The kappa line mixes transition-aware sites with a JC correction; it is a sensitivity line, not an estimate.
9. CSAC23 covers 94.6% of the list; 663 accessions are absent from GENCODE v35. Membership reflects 2004 assembly coverage.
10. O121 comes from Ensembl's protein-tree orthology, itself protein-guided (docstring, amendment 10): an instance of Day's concern at the gene level. U0 on ALL uses none of it.
11. Columns and sentences marked post hoc were computed for this write-up from `raw/l1c.json` or read off the printed tables. They are descriptive and score nothing.
12. An empty, untracked `raw/l1c.transfer.out` sits in the working tree from the collection attempt; it is not committed.

## Open
- Collect and report the transfer table; score the three pending predictions.
- Three post-run reviews; then the fix pass and integration (DN6 claim file, defeaters, QUEUE). None of that is done here.
- For the reviewers to rule on: Reading A as registered (`supported` via PF2 / PAF2) against amended (`contested`); which flags the verdict-move sentence takes; whether the kappa sensitivity belongs in the DN5 comment.
- Queue items unchanged: external codon aligner; an ML codon model for the site ratio.
