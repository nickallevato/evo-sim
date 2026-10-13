# R4 L1b: human-chimp dN/dS on the T2T assemblies (hs1 against mPanTro3, Cactus), and what a naive extraction reads on the same data

**Status: written up, reviewed, fix pass done (2026-10-13), NOT integrated.** Three post-run reviews: `REVIEW-R4-L1b-correctness.md` (0 BLOCKER, 1 MAJOR, 7 MINOR), `REVIEW-R4-L1b-steelman-day.md` (4 MAJOR, 4 MINOR), `REVIEW-R4-L1b-steelman-critic.md` (3 MAJOR, 7 MINOR). Every finding is answered in "Review resolution" at the end. All three reviews agree on the band and on the registered moves; no verdict value changes. Every verdict statement below is a proposal; the owner decides. Band by the registered rule: **CRITIC**.

**Reading guide.** Registered: the script, its predictions, bands and verdict moves (0fe3c7f), and the pre-run note (5e64f0a). Post hoc (after the output was read, each labelled where it appears): the affected/unaffected split of X1, the breakdown of what puts X1 out of register (new run, script 9c4a359), the count of codons V0 leaves out and its bounds, per-gene shares, all arithmetic taken from the reviews. Terms: **column-paired** = bases paired by alignment column (V0, VS, VR, VL); **position-by-position** = the X1 arm, which the registration names "naive ungapped extraction".

## Target
Day, "How Biologists Keep 'Proving' Selection" (voxday.net, 2026-10-11; quotes-day.md Q172-Q177). RH tag: dialectic (numeric claims).
- Q172 (¶7): "We used GENCODE v46 annotations, the same Nei-Gojobori method the original studies used, and the complete extraction of human-chimp aligned positions from the T2T-quality assemblies. And we got a result."
- Q173 (¶9): "Not 0.23. 0.80."
- Q174 (¶13): "We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46 that has coding sequence data in the human-chimp alignment."
- Post body (¶12 of the saved body text, the diagnostics paragraph, as quoted in the registration): "Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for single-SNV codons alone."
- Q175 (¶17): "No combination of quality filters moves the number below 0.65." (same ¶, as quoted in the registration: the strictest stack "still produced dN/dS = 0.64 on 10 remaining genes").
- Q176 (¶22): "If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome."
- Q177 (¶21): "At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution." (DN4; not moved by this check.)

Claims: DN1 (0.80 on 20,400 genes), DN2 (filter robustness), DN3 (Q176 conditional), DN5 (CSAC 0.23 as relayed). L1 (hg38/panTro5, `R4-L1.md`) left the T2T route open and fixed in advance what would overturn DN1's external verdict. This run is that test.

## Files
- Script `research/checks/l1b_t2t_dnds.py`, pre-registered at **0fe3c7f** (before the commit only a synthetic selftest and the annotation-count step were run). Pre-run note `R4-L1b-L5-prerun-notes.md` (**5e64f0a**, before launch): assigns the two outcome regions the bands left unclassified (ST-08) and states the expected band, CRITIC. Script unchanged between registration and run (md5 `aef21cb3...` in `raw/l1b.host`).
- Run: na-workhorse, one process, host record dated 2026-10-13 16:53 UTC. **Wall time 4 min 11 s** (extraction 127 s, analysis 91 s), peak RSS 481 MB. The registered estimate was 1-2 h and under 2.5 GB; the estimate was wrong by a factor of about 15 to 30 on time. Exit status 0.
- Outputs: `raw/l1b.out`, `raw/l1b.json`, `raw/l1b.genes.tsv.gz` (per-gene table, 19,310 rows), `raw/l1b.host`. Collected at c168b65. Segment dump on na-workhorse (`sources/raw/l1b-seg-2026-10-13/seg.json.gz`, gitignored); L1c reads it. Its sha256, unrecorded until the fix pass (post hoc record): `86b0e672d70bb6be1bd2978f869c06519482f191d11fe06d829d21b573afeacd`. The sha256 of `l1b.genes.tsv.gz`, `l1b.json` and `l1b.out` are in `raw/l1b_x1_breakdown.host` (`raw/l1b.host` itself is not edited in the fix pass).
- Post hoc run of the fix pass: script `research/checks/l1b_posthoc_x1_breakdown.py`, committed alone at **9c4a359** before it read the dump; na-workhorse, one process, 41 s, 324 MB; outputs `raw/l1b_x1_breakdown.out`, `.json`, `.host`.
- Data (public, read as text, never executed; hashes in `raw/l1b.host` equal the registered ones): T2T consortium annotation GENCODE v35 projected to CHM13 v2.0 by CAT + Liftoff; Ensembl 116 BioMart orthology file (the L1 file); 8-way T2T-ape Cactus MAF referenced on hs1, chimp mPanTro3.
- **Not Day's pipeline, in three stated ways.** GENCODE v35 projected by CAT, not v46 (Q172, Q174). One transcript per gene by the audit's rule; his transcript choice is unstated. The Cactus MAF; his aligner is unstated. All three are the audit's choices.

Extraction counts: 5,366,631 MAF blocks; 169,678 overlap a chosen CDS; 11,229 of those (6.6%) carry more than one chimp row; 653 carry none; no CDS-overlapping block had the reference on the minus strand, and no block had it out of first position. 19,407 transcripts chosen (33,505,272 CDS bases, of which 33,494,864 lie in a MAF block; this counts human reference bases, not chimp coverage); 97 have no aligned chimp base; **ALL = 19,310 genes**, 33,424,287 CDS bases, 98.87% of them with a first-row chimp base (post hoc, from the gene table; corrected in the fix pass, the earlier sentence gave the transcript-level figure as if it described ALL).

## Results (pooled = ratio of totals, Nei-Gojobori sites, Jukes-Cantor)

Chimp-row variants: V0 first chimp row per block (primary); VS syntenic row; VR random row; VL lowest-identity row (adversarial); X1 naive ungapped extraction of the first chimp row (chimp bases concatenated with gaps removed and chimp-only insertions kept, compared position by position). Set labels: UNMAPPED = gene absent from the BioMart file (48); MAPPED_NON121 = in the file and not one2one (2,438, of which about 1,150 have no chimp homology type listed). `otype` counts in the gene table: one2one 16,824, one2many 1,161, many2many 127, none listed 1,198 (post hoc count).

| variant, set | genes | pooled dN/dS | raw Nd/Sd | N/S | mean of per-gene ratios | median | single-difference codons: nonsyn share | stop-free in both |
|---|---|---|---|---|---|---|---|---|
| **Day (stated)** | 20,400 | **0.80** | | | | | **71.6%** | full stack leaves **10** |
| L1 V0 ALL (hg38/panTro5) | 23,183 | 0.271 | 0.913 | 3.34 | 0.296 | 0.178 | 45.8% | 22,331 |
| **V0 ALL** | 19,310 | **0.271** | 0.919 | 3.36 | 0.271 | 0.163 | **44.9%** | 18,750 (97.1%) |
| V0 O121 (Ensembl one2one) | 16,824 | **0.238** | 0.807 | 3.36 | 0.251 | 0.153 | 42.1% | 16,466 |
| V0 NON121 | 2,486 | 0.459 | 1.543 | 3.33 | 0.417 | 0.289 | 57.5% | 2,284 |
| V0 MAPPED_NON121 / UNMAPPED | 2,438 / 48 | 0.459 / 0.445 | | | | | 57.5% / 56.1% | |
| V0 O121q (+ CSAC-like quality) | 15,678 | 0.208 | 0.705 | 3.36 | 0.242 | 0.148 | 39.8% | 15,648 |
| **V0 SYN** (passes the synteny diagnostic) | 17,606 | **0.209** | 0.707 | 3.36 | 0.249 | 0.150 | **40.2%** | 17,376 |
| V0 NONSYN | 1,704 | 0.491 | 1.694 | 3.39 | 0.495 | 0.396 | 59.5% | 1,374 |
| V0 O121SYN | 15,811 | 0.203 | 0.686 | 3.36 | 0.242 | 0.147 | 39.5% | 15,648 |
| VS ALL / O121 / SYN | 19,310 | 0.246 / 0.217 / 0.209 | | | | | 43.4% (ALL) | 18,919 |
| VR ALL / O121 / SYN | 19,310 | 0.262 / 0.231 / 0.209 | | | | | 44.5% (ALL) | 18,761 |
| VL ALL / O121 / SYN | 19,310 | 0.293 / 0.253 / 0.209 | | | | | 46.4% (ALL) | 18,590 |
| **X1 ALL** (naive ungapped) | 19,310 | **0.853** | 2.890 | 3.36 | **0.345** | **0.189** | **60.1%** | 16,908 (87.6%) |
| X1 O121 | 16,824 | 0.844 | 2.861 | 3.36 | 0.324 | 0.176 | 58.8% | 15,030 |
| X1 NON121 | 2,486 | 0.898 | 3.021 | 3.32 | 0.496 | 0.339 | 67.0% | 1,878 |
| X1 SYN | 17,606 | 0.818 | 2.768 | 3.35 | 0.307 | 0.166 | 56.5% | 16,207 |
| X1 NONSYN | 1,704 | 0.912 | 3.158 | 3.37 | 0.755 | 0.779 | 71.8% | 701 |

**Filters** (the five of L1: S no internal stop, G <= 5% gapped codons, M >= 5 differences, L >= 300 bp, O per-gene dN/dS <= 2; all 32 combinations; S' = S that also counts the final codon).

| variant, set | min over 32 (stack, genes) | max over 32 | full stack S+G+M+L+O | S' convention: min; full stack |
|---|---|---|---|---|
| Day (stated) | none below 0.65 | | 0.64 on 10 genes | |
| V0 ALL | 0.214 (S+G+L+O, 16,298) | 0.283 (M, 13,023) | 0.225 on 11,743 | 0.229; **0.302 on 9 genes** |
| V0 SYN | 0.194 | 0.218 | 0.204 on 11,141 | 0.199; 0.225 on 7 |
| VS / VR / VL ALL | 0.208 / 0.210 / 0.221 | 0.257 / 0.274 / 0.306 | 0.220 / 0.221 / 0.233 | 0.217 / 0.224 / 0.246; 9 genes each |
| X1 ALL | **0.524** (S+G+O, 15,350) | 0.864 (M+L, 13,254) | **0.551 on 10,673** | **0.818** (G+O); **0.861 on 8 genes** |
| X1 SYN | 0.509 | 0.833 | 0.537 on 10,226 | 0.807; 0.896 on 6 |

- **Q176 arithmetic.** NON121 holds 9.8% of nonsynonymous sites. For ALL to reach 0.80 with O121 as observed, NON121 would need a pooled pN/pS of **3.95** (observed 0.459; L1 needed 2.42).
- **Gene-set gap.** ALL - O121 = **+0.033**, ratio **1.14** (L1: +0.064, 1.31).
- **Day's four-part triple** (pooled 0.70-0.90; share 66-77%; min over stacks >= 0.60; full stack <= 200 genes). V0, VS, VR, VL: 0 of 4 under S; 1 of 4 under S' (the survivor count). **X1: 1 of 4 under S (pooled only); 3 of 4 under S' (pooled, filter minimum, survivor count). The part X1 misses under both conventions is the single-difference share: 60.1% against the 66% floor.** No variant meets the triple. Two of the three parts X1 meets under S' are met by the convention and not by X1: every variant, V0 included, meets the survivor count under S', and the filter minimum is met because the 16 stacks that contain S' hold 8 or 9 genes each.
- **Terminal-stop convention.** 19,294 of 19,310 human CDS end in a stop codon in this annotation (post hoc count from the per-gene table). S' alone therefore keeps 12 genes on V0, and the S' full stack keeps 9 (L1's annotation: 861 and 258).

## Band
`band()` as registered reads V0 ALL = 0.271, V0 SYN = 0.209, share on SYN = 40.2%, and whether VR, VL or X1 meets the triple on ALL under S or S'.
- DAY needs ALL >= 0.65: no.
- LOCATED needs ALL >= 0.65 **or** one of VR/VL/X1 meeting the triple, with SYN < 0.40. SYN < 0.40 holds. The `other` clause did not fire: X1 under S' has parts [1, 0, 1, 1], missing only the share (60.1% < 66%). A share 5.9 points higher would have put the run in LOCATED. That is arithmetic and should not be read as a technicality in either direction: under the ordinary stop filter S, X1 misses three of Day's four reported numbers (share 60.1%; filter floor 0.524 against 0.65; 10,673 genes against 10), and it meets three of four only under S'. The registered share test was applied to X1 on ALL. The 66% floor was set (c04a1f8) for a fault in every gene, as in L1's W2; the share in the genes X1 actually puts out of register is higher (73.6%), and that figure is post hoc on a subset defined by X1's own output, so it cannot stand in for the registered test. LOCATED is not licensed.
- MIDDLE: neither value in [0.40, 0.65).
- **CRITIC: ALL < 0.40 and SYN < 0.40.**

Neither region assigned in the pre-run note (DAY-VALUE, MIDDLE anomalous) was reached. The pre-run note stated CRITIC as the audit's expected band (ST-08 row: the weight comes from the assemblies and alignment being the ones Day names). Expected by the audit is not the same as unable to fail: Day's registered prediction put V0 ALL at 0.65 or more on the assemblies he names, DAY and DAY-VALUE were reachable, and L1 had left this route open. As a test of his statement about the T2T assemblies it could have failed; it is not a test of his code. The X1 result was a surprise; see below.

**One datum, two uses (stated so the asymmetry is visible).** The pre-run note fixed that a high value on V0 without Day's single-difference share would still have moved DN1 ("The missing signature does not reduce the move"). On X1 the missing share is what keeps the run out of LOCATED. Both follow from what was registered: V0 tests the data statement, where his number alone would have counted for him; the triple on X1 tests whether a named error class reproduces his whole report, where every part was required. The same symmetry binds the other way: the registered CRITIC wording is not reduced by unregistered evidence either (see "Proposed verdict moves").

## Scoring of the pre-registered predictions
Hits and misses are listed with equal weight. "~" predictions use the tolerance L1 used (±25%, R1's line).

| prediction (registered) | value | result |
|---|---|---|
| Day: V0 ALL ~0.80, at least >= 0.65 | 0.271 | **miss** |
| Day: single-diff nonsyn share ~72% (>= 66%) | 44.9% | **miss** |
| Day: no 32-stack combination below 0.65 | all 32 below 0.65 (max 0.283) | **miss** |
| Day: O121 ~0.23 | 0.238 | **hit** (registered reading of Q176's antecedent, fixed 2026-10-11; Day's own later table, Q184, reports 0.7956 on 1:1 orthologs, so on his pipeline the antecedent is not met either) |
| Day: gap ALL - O121 ~ +0.57 | +0.033 | **miss** (sign right) |
| Critic: V0 ALL 0.20-0.35 | 0.271 | hit |
| Critic: O121 0.18-0.30 | 0.238 | hit |
| Critic: SYN 0.18-0.32 | 0.209 | hit |
| Critic: share on ALL 35-50% | 44.9% | hit |
| Critic: every 32-stack value on V0 ALL < 0.40 | max 0.283 (S' grid max 0.377, on 12 genes) | hit |
| Critic: Q176 arithmetic fails (needed NON121 p-ratio > 1.5) | 3.95 | hit |
| L1 carry-over: ALL - O121 in [+0.02, +0.12] | +0.033 | hit (lower third of the band) |
| L1 carry-over: ALL/O121 in [1.08, 1.60] | 1.14 | hit |
| L1 carry-over: NON121 0.30-0.60 | 0.459 | hit |
| A1: V0 ALL 0.22-0.32 | 0.271 | hit |
| A1: N/S 3.2-3.4 | 3.36 | hit |
| A2: VS ALL within 0.03 of V0 ALL | 0.246 against 0.271 (0.025) | hit (narrow) |
| A2: SYN holds >= 80% of ALL genes | 17,606 / 19,310 = 91.2% | hit |
| A2: NONSYN pooled > SYN pooled | 0.491 > 0.209 | hit |
| A3: VR and VL raise ALL by <= 0.10 | VR -0.009, VL +0.022 | hit |
| A3: share of CDS bases with dup > 0 below 10% | 5.1% (see note) | hit |
| **A4: X1 ALL pooled 0.28-0.60** | **0.853** | **miss** |
| A4: X1 does not meet the triple | 1 of 4 (S), 3 of 4 (S') | hit by the rule; near miss under S' |
| A5: ALL holds 18,000-20,000 genes | 19,310 | hit |
| A6: stop-free in both species > 90% (V0 ALL) | 97.1% | hit |
| A6: full stack keeps > 10,000 genes | 11,743 | hit |

Tally: Day 1 of 5 parts (four registered clauses; "O121 ~0.23, i.e. the gap ~ +0.57" is one clause, scored as a hit and a miss); critic 6 of 6; carry-over 3 of 3; audit A1-A6 11 of 12 parts, 5 of 6 predictions (A4 is registered as one conjunction and is a miss as written), with the one miss on the prediction that mattered most for locating Day's number.

How to read the tally (added in the fix pass; the rows above are unchanged).
- It is not a scoreboard of independent tests. The critic, carry-over and A1 bands were written by the audit with L1's 0.271 and 0.207 in hand, the gap row is not independent of the ALL and O121 rows, and CRITIC was the expected band. The one audit prediction that could fail in an informative way, A4, failed.
- Day's side was fixed on 2026-10-11 from Q172-Q176. His post of 2026-10-12 (Q184-Q186) puts 1:1 orthologs at 0.7956 and says "The difference is not a matter of gene selection, quality filtering, or computational error." (Q186). Under that later position the gap row is no longer his prediction (that would remove a miss) and his one hit, O121 ~0.23, becomes a miss (he now reports about 0.80 there). The pre-run note of 2026-10-13 did not update his side. Scoring stays as registered; both effects are recorded.
- Robustness of the critic rows (post hoc reading of registered outputs): the five that can be evaluated per variant also hold under VS, VR and VL (ALL 0.246 / 0.262 / 0.293; O121 0.217 / 0.231 / 0.253; SYN 0.209; share 43.4% / 44.5% / 46.4%; stack maxima 0.257 / 0.274 / 0.306). The highest column-paired value on any set cut from the gene table is 0.599 (the 691 genes that fail both the synteny diagnostic and one2one; post hoc), below Day's stated floor of 0.65.

Note on A3's second part. The json does not carry this number. It is computed post hoc from the per-gene table as the length-weighted mean of `dup` (CDS bases in blocks with more than one chimp row), which is 5.10%; values in the table are rounded to four decimals. 1,907 genes have dup > 0.

**The A4 miss and its stated reason.** A4's reason was "real human-chimp CDS indels that are not multiples of 3 are too rare to put most genes out of register". The premise about "most genes" held (next section: 13.7% of genes are affected). The conclusion did not follow. X1 compares position by position, so any unhandled length difference, in frame or not, pairs every downstream codon with a non-homologous one, and a pooled ratio weights genes by their differences. The audit did not anticipate that a minority of genes would carry the pooled value.

## What the X1 result does and does not show

**Post hoc and descriptive; computed from `raw/l1b.genes.tsv.gz` after reading the output; no registered prediction.** A gene is called "affected" if its X1 counts differ from its V0 counts in any of the four columns Sd, Nd, s1, n1 (with S and N added to the rule the count is 2,646 instead of 2,637; no conclusion moves).

| genes | n | X1 pooled | X1 share | V0 pooled on the same genes | share of all X1 differences |
|---|---|---|---|---|---|
| unaffected (X1 counts = V0 counts) | 16,673 (86.3%) | 0.205 | 39.8% | 0.205 | 5.9% |
| affected | 2,637 (13.7%) | **0.960** | **73.6%** | 0.427 | **94.1%** |
| all | 19,310 | 0.853 | 60.1% | 0.271 | 100% |

- X1 counts 2,714,599 differences against V0's 256,778 (json totals; the rounded gene table sums to 2,714,597). Half of the excess sits in 381 genes (2.0%), 90% in 1,458 genes (7.6%).
- Affected share by set: 8.9% of SYN genes, 11.8% of O121, 26.3% of NON121. Because pooling weights by differences, the pooled X1 value is nearly the same in every set (ALL 0.853, O121 0.844, SYN 0.818, NON121 0.898) although the affected fraction differs threefold.
- Per gene, X1 is 0.65 or higher in 19.5% of the 17,722 genes with a defined ratio (V0: 9.8% of 17,861). X1 median 0.189, and 70.5% of genes read below 0.40 (V0: median 0.163, quartiles 0.046 and 0.354, 78.3% below 0.40, 6.5% at 0.80 or above). The pooled 0.853 is carried by 13.7% of genes.
- Of the affected genes, 2,291 have at least one gapped or uncovered chimp codon on V0; 346 have none. What these are is now broken down from the segment dump (next section).
- Controls from the correctness review (post hoc, recomputed here): '+' strand genes read 0.848 under X1 and '-' strand genes 0.858, with 13.8% and 13.5% affected, so no strand fault. The 444 affected genes with no internal stop in either species under X1 read **1.004** (V0 on the same genes 0.365): whole-codon shifts read as high as frame shifts.
- A stop filter removes much of it: S alone gives 0.554 on 16,908 genes; every stack containing S reads 0.52-0.58; every stack without S reads 0.82-0.86.

What this supports:
1. **A pipeline can read Day's headline number on these assemblies.** A naive ungapped extraction of the first chimp row, applied to the same alignment and annotation, moves the pooled value from 0.271 to 0.853. Day's 0.80 lies between them, closer to X1. What moves it is every place where the first chimp row and the human CDS differ in length: alignment indels, in frame or not, and stretches where the first row has no chimp base (next section).
2. **X1 as built is not Day's pipeline.** Against his reported numbers it misses the share (60.1% against 71.6%), the filter floor under an ordinary stop filter (0.524 against "none below 0.65"), and the strict-stack size under S (10,673 against 10). Under the terminal-stop convention S' it matches the filter floor (0.818) and the survivor count (8 against 10) and still misses the share; its strict-stack value is 0.861 against his 0.64, on 8 genes.
3. **The share is the discriminating datum, as in L1.** His 71.6% is 2.52 nonsynonymous per synonymous single-difference codon. V0 ALL gives 0.82, X1 ALL 1.51, X1 on the affected genes alone 2.79. His count behaves like X1's affected genes, not like X1's whole set (post hoc; the affected set is defined by X1's own output). A pipeline that matched his share by this route would need mispaired sequence in about half or more of the codons it compares (rough two-component estimate from the correctness review), which X1 on this alignment does not produce (12.0% of codons are out of register). Two limits. A share of 72-76% is what any pairing without constraint gives (L1's W2: 72.7%), and it is also the no-constraint expectation under Day's own reading of his number, so the share alone identifies a class of count and not a cause; the per-gene distribution separates the two readings. And the match is not to every number: X1's affected genes read 0.84 on single-difference codons alone (N/S 3.31) against his stated 0.71, and 0.96 pooled against his 0.80.
4. **The audit has not seen Day's pipeline.** Position-by-position pairing is **a candidate error class with a real-data instance**. Shown on the data: (a) column pairing gives 0.21-0.29 on his assemblies; (b) his pooled value is reached by an extraction that compares codons the alignment does not pair; (c) in the genes it mispairs, the single-difference share is the one he reports. Not shown: that his pipeline does this. It is unreleased, DN1 internal stays `pending`, and nothing here scores his method. L1's W2 was a synthetic break in every gene; X1 is a real-data instance of the same class that reaches the pooled value on ALL and not the registered signature.

**Uniformity of the share across gene sets (post hoc; outside this check's targets; recorded for L1c and DN6, not scored here).** Day's later post ("The Method is the Conclusion", 2026-10-12) reports "It's 73.8% nonsynonymous across every subset we tested. The signal is uniform across the genome, it's not concentrated in problematic genes." (Q183), with pooled values near 0.80 for all genes, 1:1 orthologs and the excluded set (Q184: "A: All GENCODE20,4000.798973.9%", "B: 1:1 chimp orthologs16,9950.795673.8%", "C: Excluded by filter3,4050.823774.4%"; cells run together by text extraction).

| gene set | V0 share, whole set | X1 share, whole set | X1 share, affected genes only (n) | X1 pooled, affected genes only |
|---|---|---|---|---|
| O121 | 42.1% | 58.8% | **73.5%** (1,983) | 0.966 |
| NON121 | 57.5% | 67.0% | **74.1%** (654) | 0.933 |
| SYN | 40.2% | 56.5% | **73.2%** (1,568) | 0.976 |
| NONSYN | 59.5% | 71.8% | **74.5%** (1,069) | 0.919 |
| Day, Q184 (A, B, B-HC, C) | | 73.9%, 73.8%, 73.8%, 74.4% | | |

- Column-paired shares are not uniform: 39.5% (syntenic and one2one) to 64.9% (neither) across the 2x2 of the two classifications, a spread of 25 points.
- Whole-set X1 shares are not uniform either (56.5% to 71.8%) and are below his in every large set. The earlier draft stopped here and called the resemblance partial.
- In the genes X1 puts out of register the share is the same to within 1.3 points in all four sets, at his reported value. A pooled value that is nearly the same in every set (X1: 0.818 to 0.912) also does not show uniformity across genes: 86% of X1's genes are untouched.
- What this licenses, and what it does not. On these assemblies a share that is the same in one2one orthologues and in the excluded genes is given by codons paired out of register and is not given by column pairing. The affected set is outcome-defined, and 72-76% is what unconstrained sequence gives under either explanation (Day's: weak constraint; the audit's candidate: mispairing), so the share identifies a class of count. It does not identify X1 and it does not identify his pipeline. His per-gene table would separate the readings: his high value in most genes, or in a minority.

## Post hoc: what puts X1's genes out of register (fix pass, 2026-10-13)

**Post hoc and descriptive. Not registered as a test; no band, prediction or verdict move depends on it.** It answers correctness finding 1 (MAJOR) and finding 2 (MINOR). Script `l1b_posthoc_x1_breakdown.py`, committed alone at 9c4a359 before it read the segment dump; its docstring lists what had already been seen (the L1b outputs, the three reviews, one diagnostics line of `raw/l1c.out`), the classes, and one prediction from each side. Inputs: the segment dump (sha256 `86b0e672...afeacd`, checked by the script), L1b's annotation, `raw/l1b.genes.tsv.gz`. Outputs `raw/l1b_x1_breakdown.out` and `.json`.

Method. X1's offset against the alignment changes wherever the number of first-row chimp bases differs from the number of human CDS bases. Each such place is one event:
- **indel** (in frame, or frame-changing): a gap run in the chimp row or in the human row with first-row chimp sequence on both sides and chimp coordinates running on without a break. The alignment itself asserts a length difference between the two assemblies;
- **hole**: human CDS bases with no first-row chimp base and no continuous chimp sequence across them in the dump (the block has no chimp row; the first row has no base over the CDS slice; a gap run at a block boundary inside an exon where the row does not continue; bases in no block);
- **exon edge**: a gap run that meets an exon edge. The flank is not in the dump, so deletion and hole cannot be told apart.
A gene is assigned to its first event in transcript order, and separately to the combination of classes it holds.

Checks of the method.
- **Block order (correctness finding 2): 0 of 19,407 transcripts** have segments out of genomic order in the dump, and none has overlapping segments. X1 concatenates in transcript order in every gene.
- The offset model reproduces X1 exactly where it claims to: among the codons it calls in register in the 2,765 genes that have an event, **0** have an X1 codon that differs from the column-paired codon. All 2,637 affected genes have at least one event; no gene without an event is affected; 128 genes have an event and unchanged counts (10,909 out-of-register codons that add no difference).
- The CDS bases with no first-row chimp base sum to 378,989 by class, the figure the gene table gives independently (33,424,287 x (1 - 0.98866)).

| first cause in the gene | affected genes | share of genes | share of X1's excess differences | X1 pooled | X1 share | V0 pooled, same genes |
|---|---|---|---|---|---|---|
| in-frame indel (deletion 889, insertion 397) | 1,286 | 48.8% | **55.7%** | 0.996 | 73.1% | 0.367 |
| hole (first row has no base over the slice 601; row breaks at a block boundary 113; block has no chimp row 75; no block 1) | 790 | 30.0% | **28.8%** | 0.922 | 74.8% | 0.436 |
| frame-changing indel (deletion 235, insertion 120) | 355 | 13.5% | **8.4%** | 0.871 | 71.9% | 0.501 |
| exon edge (deletion or hole, not separable) | 206 | 7.8% | 7.1% | 0.921 | 76.3% | 0.534 |
| all affected | 2,637 | 100% | 100% (2,457,819 differences) | 0.960 | 73.6% | 0.427 |

By combination of classes (same run):
- genes whose **only** events are in-frame indels: 1,138 genes, 45.0% of the excess, X1 **1.009**, V0 0.281;
- genes with only holes: 577 genes, 20.7% of the excess, X1 0.916, V0 0.300;
- genes with a frame-changing indel anywhere: 590 (22.4% of affected genes), 18.9% of the excess; genes with none: 2,047, 81.1% of the excess, X1 0.974.

By codon: 1,332,292 of 11,141,429 codons (12.0%) are out of register under X1. Of these 805,038 are shifted by whole codons, 402,287 are out of frame and 124,967 lie beyond the end of the X1 string (padding, not compared). The events that cause this are small: in-frame indels total 35,979 bases in 2,437 runs, frame-changing indels 7,927 bases in 1,357 runs, holes 307,671 bases, exon-edge gaps 37,457 bases. Flags: 530 affected genes (20.3% of the excess) also have a first-row change of chimp sequence or strand, or a step back in chimp coordinate, between consecutive segments.

Each side's stated criteria (docstring, before the run):

| criterion | value | met |
|---|---|---|
| Day side: a frame-changing indel is the first cause in more than 50% of affected genes | 13.5% | no |
| Day side: those genes carry more than 50% of the excess | 8.4% | no |
| Day side: hole classes carry less than 25% of the excess | 28.8% | no |
| Critic side: holes, in-frame indels and exon-edge gaps carry at least 50% of the excess | 91.6% | yes |
| Critic side: a frame-changing indel is the first cause in fewer than 50% of affected genes | 13.5% | yes |
| Critic side: genes with no frame-changing indel read 0.85-1.15 under X1 | 0.974 on 2,047 genes (V0 0.350) | yes |

What it supports, by side.
- **Critics.** All three critic-side criteria are met and none of the Day-side ones. X1's high value is not carried by genes whose chimp reading frame is broken. The largest class is in-frame length differences, and genes with nothing else read 1.009 under X1 against 0.281 when the same sequence is paired by column. An in-frame indel of a few codons leaves every downstream codon intact; X1 compares each of them with its neighbour. In-frame indels total about 36 kb, and about 700,000 codons are out of register downstream of one. The excess is a property of what is paired with what.
- **Day.** The correctness review's concern that X1 might be mostly an artefact of missing first-row coverage is not borne out: genes that start with a hole carry 28.8% of the excess, and 64.1% starts at a length difference that the alignment itself asserts, with chimp sequence continuous on both sides. Those are differences between the two assemblies as Cactus aligns them, in 1,641 genes, and a column-paired count passes over the codons they occupy. That is the kind of position his Q181 is about ("Regions too divergent to score well get gapped out or are left unaligned, so they aren't counted."). X1 is therefore a fair real-data instance of position-by-position pairing on his named assemblies, not an accident of the audit's row choice. The audit's own stated expectation (frame-changing indels the largest class by genes) was wrong.
- **What it does not show.** (1) It cannot identify Day's pipeline, which is unreleased; whether his extraction pairs by position is not known. (2) An alignment gap is the aligner's statement: "length difference" means as Cactus aligns these two assemblies, and an assembly or annotation error in either genome looks the same. (3) Under every class the excess differences are differences between codons the alignment does not pair; none of them is a substitution count for the codons that were skipped. What the skipped codons hold is the next section's subject and L1c's. (4) First-cause attribution gives each gene to one class; the combination rows show how far that matters.

## Post hoc: the codons V0 leaves out (fix pass, 2026-10-13)

**Post hoc arithmetic on the gene table and the breakdown run; the counts were first given by the Day-side review and are recomputed here.** V0 skips every codon with a gapped or missing chimp base. Day's Q181 says such regions "aren't counted", and Q182 that "Those excluded codons are enriched for nonsynonymous substitutions by definition". L1b's column-paired arms hold fixed what those sentences dispute, so the size of what is held fixed is reported.

- **Left out: 129,092 codons, 1.16% of 11,141,429, in 2,411 genes.** V0 counts 256,778 differences in all, so the left-out codons are half as numerous as the differences counted.
- By base, the 378,989 CDS bases with no first-row chimp base are 81.2% holes (307,671), 9.9% exon-edge gaps (37,457) and 8.9% alignment deletions (33,861). Most of what V0 leaves out is sequence for which the first chimp row offers nothing to compare, not sequence aligned and then gapped.
- **Bounds on the pooled value if the left-out codons were counted.** At V0's own rates: 0.27 (unchanged). If every left-out codon held one nonsynonymous difference: **0.56**. Two each: **0.85**. So L1b does not close the left-out-codon route by arithmetic: the registered CRITIC sentence is a statement about the codons this alignment pairs. Neither V0 nor X1 tests the claim that the left-out codons carry the difference. X1 does not add them back; it shifts what lies downstream of them.
- **What the same data cost that route.**
  - The 16,899 genes (87.5%) in which V0 leaves out no codon read **0.212** pooled with a share of 40.3%. Q183 ("The signal is uniform across the genome, it's not concentrated in problematic genes.") predicts about 0.80 there. The 2,411 genes with a left-out codon read 0.435 on the codons that are paired.
  - Cactus is a nucleotide whole-genome aligner, not the "protein-guided CDS alignment method" Q180 names, and it still reads 0.27.
  - X1 with a stop filter reads **0.52-0.58** in every stack that contains S (0.524 to 0.580), below his stated floor of 0.65.
  - The gene count is not the route: for ALL to reach 0.80, the **1,090 genes** that separate this set from his 20,400 would need a pooled pN/pS **near 10** (10.1; pN 0.18, 37 times the observed), at average size and the observed pS.
- **A credit inside the same numbers.** His diagnostics paragraph says "98.8% of coding positions are found." (¶12 of the saved body text of 2026-10-11; not yet a Q entry, to be added at integration). First-row chimp coverage here is 98.87% of CDS bases and 98.84% of codons are paired. His input coverage looks like the audit's, so the difference between his number and this one lies downstream of extraction coverage.
- The alignment-method question itself (Q180-Q186, DN6) is L1c's. For L1c, both directions: points (a)-(d) of Day-side finding 3 are the four bullets above.

## Interpretation
- **The T2T route does not reach 0.80 with an extraction that pairs bases by alignment column.** On hs1 against mPanTro3 from the Cactus alignment, all genes give 0.271, the same value to three decimals as L1 on hg38/panTro5 with UCSC multiz. The chimp-row choice moves it between 0.246 (syntenic) and 0.293 (lowest-identity row, an adversarial bound). The 32 filter stacks move it between 0.214 and 0.283 on V0. Three limits. (i) Keeping the reading frame is not sufficient: in-frame length differences mispair as well (X1 reads 1.00 in genes with no stop and 1.009 in genes whose only events are in-frame indels), so the contrast is column pairing against position-by-position pairing, not frame-preserving against frame-breaking; the earlier draft's "frame-preserving" was the wrong word. (ii) The statement is about the codons this alignment pairs; 1.16% of codons are left out and neither V0 nor X1 tests what they hold (DN6, L1c; not pre-judged here). (iii) L1 and L1b share the estimator, site counts, filters and single-difference code (`l1_dnds_genesets.py`, imported unchanged) and the orthology file, so agreement to three decimals is agreement of two assembly and alignment pairs under one counting code, not of two independent pipelines.
- **Paralog choice is not the route either.** Blocks with more than one chimp row hold 5.1% of CDS bases, and always taking the worst row adds 0.022.
- **The Consortium-type value is reproduced a second time**: 0.238 on Ensembl one2one, 0.208 with CSAC-like quality filters, 0.209 on the syntenic set.
- **The gene-set effect is real in kind; its size depends on the comparator and on the annotation.** The registered carry-over band held, in its lower third. All the numbers, none ranked above another:
  - ALL exceeds Ensembl one2one by +0.033, **+14%** (ratio 1.14; L1 on hg38: +0.064, **+31%**);
  - ALL exceeds the CSAC-like set O121q (0.208) by **+30%** (L1: +36% against its O121q of 0.200). Q176 names "the Consortium's curated subset", and O121q is the audit's analogue of it;
  - among syntenic genes the effect is **+3%** (SYN 0.209 against O121SYN 0.203, +0.006);
  - non-one2one genes read 1.93 times one2one (pooled 0.459 against 0.238; L1: 0.447 against 0.207, 2.16). A gene-class difference survives synteny at the gene level (syntenic non-one2one genes: 0.276 on 1,795 genes against 0.203);
  - the pooled gap is smaller than in L1 mostly because this annotation holds **2,486** non-one2one genes against L1's **6,417** (9.8% of nonsynonymous sites against 18.8%), and because O121 is higher. Nearly half of the 2,486 (1,198) are genes for which Ensembl lists no chimp homology type. Day's own table has 3,405 excluded genes (Q184).
  - Q176 needs +0.57.

  No materiality label is attached to the T2T value. The registration says only that the credit is "restated with the T2T value", with a "pipeline-specific" mark if the gap is below +0.02, which it is not (+0.033). Rule R1 is a test of whether correcting an author's slip moves his conclusion by more than 25%; using it after the run to mark a credit down (+14% against one comparator) or up (+30% against another) would be a new use chosen with the result in hand. The earlier draft's sentence "Under R1's 25% line the L1 gap (+31%) was material and this one (+14%) is not" was such a use, was not labelled post hoc, and is withdrawn. The L1 credit keeps the wording it was given at L1's integration.
- **Synteny carries most of the gene-set difference.** SYN and O121SYN read 0.209 and 0.203; NONSYN reads 0.491. The syntenic-row variant VS brings NON121 to 0.427 only, so the higher value of non-one2one genes is not removed by picking the syntenic copy.
- **Strict-stack size is a convention effect, not a signature.** Day's ¶17 says "requiring no stop codons in either species" (same ¶ as Q175). Read literally, a terminal stop is a stop codon, so S' is a plain reading of his filter and not a rescue. Under it a column-paired extraction also leaves 9 genes (Day: 10). The near-empty stack that L1 treated as part of his signature is reproduced here without any extraction fault. The value on those 9 genes is 0.302 (his: 0.64 on 10); a pooled ratio on 9 genes has no useful precision and no interval was computed, so the two values are not scored as a discrepancy. The other half of the same reading: 19,294 of 19,310 human CDS end in a stop here, so under S' the 16 of 32 stacks that contain the stop filter hold 8 to 12 genes each and test nothing. If that is his convention, Q175 ("No combination of quality filters moves the number below 0.65.") rests on at most 16 informative stacks (slip S-DN2-2), and on V0 the S' grid still reads 0.229 to 0.377, so the sentence is not true of a column-paired extraction under either convention.
- **The typical gene reads low under every pairing.** Per-gene median 0.163 on V0 ALL (0.147-0.153 on the one2one and syntenic sets); 78.3% of genes with a defined ratio read below 0.40 and 9.8% reach 0.65. Under X1, which reproduces his pooled number, the median is 0.189 and 70.5% of genes read below 0.40. Limit: his headline is a pooled ratio and the pooled comparison is the like-for-like one; per-gene ratios at about 1% divergence are noisy, and 1,449 genes have none. Q183 is L1c's target.
- **On Day's own later table the gene-set explanation is absent, and the disagreement sits inside the one2one set.** Q184 reports "B: 1:1 chimp orthologs16,9950.795673.8%" beside "A: All GENCODE20,4000.798973.9%": a gap of +0.003 on his pipeline. So Q176's antecedent is not met on his own numbers either, and his pipeline and a column-paired extraction differ by a factor of 3.3 within one2one orthologues (0.7956 against 0.238), where gene list, paralogy and assembly gaps are held as fixed as they can be. Rule N (non-sequitur) is not licensed: Q176 is a conditional, Q184 is a later post, and DN3's claim file already records that he withdrew the explanation (Q185, Q186; rule SC).

## Proposed verdict moves (band CRITIC; exactly as registered under "WHAT MOVES WHICH VERDICT"; proposals, the owner decides)

| claim | field | now | registered rule | value | proposal |
|---|---|---|---|---|---|
| DN1 | external | `contradicted` (comment: conditional on L1b, MA-12) | CRITIC: stays, "now on T2T and Cactus as well (the 'different assembly / complete extraction' route is closed for this alignment)" | ALL 0.271, SYN 0.209 | **stays `contradicted`**, with the registered sentence as written; the comment's "conditional on L1b" clause is discharged for this alignment and annotation. Readings table below (rule RD) |
| DN1 | internal | `pending` | stays `pending` (method unreleased) | | stays |
| DN2 | external | `contradicted` | re-opened (`contested`) only if min over 32 stacks on V0 ALL or SYN >= 0.60 | 0.214, 0.194 | **stays `contradicted`** |
| DN3 | external | `contradicted` (gene-list version) | `supported` only if ALL - O121 >= +0.40 with O121 <= 0.30 on V0; otherwise stays, "now also for the alignment-level version" | +0.033, O121 0.238 | **stays `contradicted`, extended to the alignment-level version** |
| DN3 | credit to Day | +31%, material by R1 (L1) | "restated with the T2T value; if the gap is < +0.02 the credit is marked pipeline-specific" | +0.033, ratio 1.14 | **restated with the T2T value**; gap >= +0.02, so not marked pipeline-specific. Proposed text below; no materiality label on the T2T value |
| DN5 | external | `supported` | stays if O121 in 0.18-0.30 | 0.238 | **stays `supported`** |
| DN5 | fidelity | `accurate` | not moved here | | not moved |
| DN4 | all | | not moved | | not moved |

No verdict value changes. The moves are comment-level: one condition discharged (DN1, and the same MA-12 clause on DN2 and DN3), one scope extended (DN3), one credit restated (DN3).

**The registered wording stays registered.** For DN1, DN2 and DN3 the external comments take the docstring's own sentence, which is already scoped: "now on T2T and Cactus as well (the 'different assembly / complete extraction' route is closed for this alignment)". The earlier draft proposed to narrow it after the result to "closed for a frame-preserving extraction ...; a naive ungapped extraction of the same data reads 0.853". That proposal is **withdrawn** (critic-side MAJOR-1): it reduced a registered sentence on unregistered evidence, with a variant that does not compare aligned positions, where Q172 describes "the complete extraction of human-chimp aligned positions". The sentence is also not broadened: "this alignment" means the hs1-referenced Cactus MAF with the GENCODE v35 CAT annotation, an alignment-column extraction, and one estimator (Day-side MAJOR-1 and MAJOR-3, NOTE 10).

**Separate sentence on X1, post hoc, not licensed by the registration; for integration to accept, change or reject.**
- For the DN1 external comment: "Post hoc: a position-by-position extraction of the first chimp row of the same data, which does not compare aligned positions after the first length difference, reads 0.853 pooled (share 60.1%, per-gene median 0.189), carried by 13.7% of genes; a candidate error class with a real-data instance, not shown to be his pipeline. The codons this alignment leaves out (1.16%) are not tested here (L1c)."
- LOCATED is not licensed and the class is not named as located. The registration licensed naming the class only under band LOCATED, and the run missed it on the registered share test.
- For the DN2 external comment, both halves: "Post hoc: the position-by-position arm reads 0.82-0.86 in every stack without an internal-stop filter and 0.52-0.58 in every stack with one, below his 0.65; under a stop filter that counts the final codon, half of the 32 stacks hold 8-12 genes on any extraction". DN2's existing A/B split stays as it is: (A) as a statement about the sequence, `contradicted` (0.21-0.28 on V0; S' grid up to 0.377); (B) as a report of his pipeline, consistent with position-by-position pairing under S' and not under S, unverifiable until his table is released.

**DN1 Readings table (rule RD; proposal for integration, post hoc).** After X1, how Q172-Q173 are read changes what the run says about them.

| reading of Q172-Q173 ("And we got a result." "Not 0.23. 0.80.") | tag | external verdict under that reading | basis |
|---|---|---|---|
| **(A)** 0.80 is a property of the genomes: the human-chimp coding dN/dS on the T2T assemblies | dialectic | **`contradicted`** on this alignment and annotation | V0 ALL 0.271, SYN 0.209; 0.246-0.293 under every chimp-row choice; registered band CRITIC |
| **(B)** 0.80 is a report of what an ungapped comparison of the extracted sequence yields | dialectic | reproduced in kind by X1 (0.853 pooled; O121 0.844, NON121 0.898, the ordering of his Q184 rows); identity with his pipeline **unverifiable** until code or per-gene table is released (`untestable` for now) | post hoc; X1 misses his share on ALL and his filter floor under S |
| **(C)** the value depends on the alignment method (Q180-Q186) | dialectic | **not tested by L1b.** Tested by L1c, whose main run finished on 2026-10-13 with band CRITIC on every rule and gene set (raw outputs from na-workhorse, collected at 90b32ba; write-up and reviews pending) | DN6 |

Which reading sets the verdict field. RD gives the field to "the reading under which the speaker's quoted statement is most defensible (closest to literally true, best supported)", and says that extended readings (a different object, or a wider claim) cannot set it.
- **Proposed: (A) sets the field, which stays `contradicted`, with the comment beginning `reading-dependent:` and listing A, B and C.** Reasons. Q172 itself says "aligned positions", and X1 does not compare aligned positions after the first length difference. Q173 sets 0.80 against 0.23 as the same quantity, and Q176 and Q177 draw conclusions about the genome from it. The claim's title is "genome-wide human-chimp dN/dS = 0.80 ... not 0.23". Reading B changes the object from the genomes to the output of a pipeline, which RD treats as an extended reading; and what his pipeline did is the internal field's question, which stays `pending`. The Day-side review says A is the reading his words carry, and the critic-side review reads the quote the same way.
- **The other way, stated because it is arguable.** As a sentence, "we got a result ... 0.80" is most defensible, in the sense of closest to literally true, as a report of his computation: nobody disputes that his code printed about 0.80, and X1 shows such a number can be had from these data. If the owner holds that B is a plain reading of the quote and not an extended one, RD would put B's value in the field (`untestable` until release), with A recorded as `contradicted` beside it. The audit's proposal is A because a report of an output with no claim about the genome would not be the claim DN1 records or the one Day argues from; the choice is the owner's.
- Either way the Readings table goes into the claim file's R4 paragraph, the verdict is counted among the reading-dependent ones, and C stays open until L1c is written up and reviewed. The MA-12 condition "conditional on L1b" is discharged as registered; whether the comment then says "alignment-method route: see L1c" is a wording point for integration.

**DN3 credit, proposed text (all numbers, no materiality label on T2T):** "a real gene-set effect in Day's direction on both pipelines: on hg38/multiz +31% over one2one (L1); on T2T/CAT/Cactus +14% over one2one, +30% over the CSAC-like set O121q, +3% among syntenic genes; non-one2one genes read 1.9-2.2 times one2one on both; size depends on annotation and gene-set composition (2,486 non-one2one genes here against 6,417 in L1); against +0.57 needed; Day's own Q184 table shows +0.003". Not marked pipeline-specific.

## Who this helps
- **Day.**
  - His stated assemblies were testable because he named them. His O121-type expectation (~0.23) is met at 0.238 as registered; it is an expectation taken from Q176 on 2026-10-11, and his own table of 2026-10-12 does not show it (Q184: 0.7956 on 1:1 orthologs).
  - The gene-set effect has his sign on T2T as well, inside the band the audit registered for it: +14% over one2one, +30% over the CSAC-like set, +3% among syntenic genes; non-one2one genes read 1.93 times one2one.
  - His near-empty strict stack (10 genes) is reproduced by a column-paired extraction under the literal reading of his stop filter (9 genes), so that part of his report is no longer evidence of a fault.
  - His completeness statement is reproduced: "98.8% of coding positions are found." (¶12) against 98.87% of CDS bases and 98.84% of codons here. His list of filters (¶16) is the five the audit ran.
  - The codons a column-paired count leaves out are not negligible in number (129,092, half as many as the differences counted), and L1b does not bound what they hold below his value (0.56 to 0.85 if each held one or two nonsynonymous differences). That route is tested by L1c, not here.
  - Post hoc breakdown: 64.1% of X1's excess starts at a length difference the alignment itself asserts, not at a coverage hole. The two assemblies do differ in CDS length in 1,641 of these genes as Cactus aligns them.
  - His Q184 table is internally coherent as a report (three sets near one value, the excluded set slightly higher, is what a pooled value does when a minority of genes carries the differences), and he changed his explanation in public within a day when his own subset test did not show cherry-picking (Q185: "We ran the same test on their smaller subset, which I suspected might be cherry-picked. Except they weren't.").
  - DN5: he relayed 0.23 correctly, and it is reproduced on his stated assemblies.
- **Critics.**
  - On the T2T assemblies Day names, with bases paired by alignment column, pooled dN/dS is 0.25-0.29 under every chimp-row choice and 0.21-0.28 under every filter stack on V0 (the adversarial row VL reaches 0.306 in one stack; the S' grid 0.377 on 12 genes). All six critic-side predictions hit, and they hold under VS, VR and VL as well.
  - The "different assembly" and "complete gene set" routes to 0.80 are closed for this alignment and annotation: paralog choice adds at most 0.022, non-one2one genes would need a pN/pS of 3.95, and the 1,090 genes not in this set would need a ratio near 10 (post hoc arithmetic).
  - The published 0.23 is reproduced in kind a second time (0.238; 0.208 with quality filters; 0.209 syntenic).
  - The typical gene reads 0.15-0.16 on every column-paired set; fewer than one gene in ten reaches 0.65. The 87.5% of genes with no left-out codon read 0.212.
  - On Day's own table the gap between all genes and 1:1 orthologs is +0.003, so the disagreement between his pipeline and this one sits inside the one2one set (0.7956 against 0.238).
  - Post hoc breakdown: all three critic-side criteria are met. Frame-changing indels are the first cause in 13.5% of affected genes (8.4% of the excess); genes whose only events are in-frame indels read 1.009 under X1 and 0.281 by column. The excess is a matter of what is paired with what.
- **Both: the X1 result (post hoc throughout; the audit's own missed prediction A4, so it is entered under neither side).**
  - The audit predicted X1 would read 0.28-0.60 and it read 0.853. L1's inference placed the mispairing "in most genes" (R4-L1.md, Derivation); for the pooled value that is withdrawn, since mispairing in 14% of genes is enough.
  - **Day's half.** A simple pipeline reads 0.85 pooled on the assemblies he names, so his number is reproducible in kind on these data, and the audit did not expect that. The audit has not seen his pipeline; nothing here shows that it pairs position by position.
  - **The critics' half.** 86% of genes are untouched at about 0.205, and the affected 14% read about 0.96-1.00, the value expected of codons paired out of register (two unrelated random CDS read 0.95 under the same estimator, L1 correctness review). The single-difference share in those genes is uniform across gene sets at 73-74%, as in Day's Q184 figures, against 39.5-64.9% under column pairing.
  - **The Day reviewer's counterpoint, beside it.** 72-76% is also what pairing without constraint gives under either explanation, weak constraint or mispairing, so the share identifies a class, not his pipeline. And X1 on its whole set misses his share (60.1%), his single-difference ratio (affected genes 0.84 against his 0.71) and, under the ordinary stop filter, his filter floor.
  - Wording that follows: **a candidate error class with a real-data instance.** LOCATED is not licensed.
  - Day reported the single-difference share, and his per-gene table (Q176) would show at once whether his high value sits in most genes or in a minority.

## Caveats for the reviewer
1. GENCODE v35 by CAT/Liftoff, not v46; one transcript per gene by the audit's rule; the Cactus MAF. All three are the audit's choices, not his. ALL is 19,310 genes against his 20,400; O121 16,824 against the 13,454 of CSAC 2005. The annotation step dropped 25,450 NF-tagged transcripts, 328 not ortholog-class and 238 off-length CDS before any chimp base was read. Bound (post hoc): the 1,090 missing genes would need a pooled pN/pS near 10 for ALL to reach 0.80, so the annotation gap cannot carry 0.80; it can move the size of the gene-set effect. "Extraction artefact" remains a candidate until his pipeline or per-gene table is seen.
2. One alignment (Cactus, hal2maf, hs1 reference). A different aligner is L1c's subject and is not tested here.
3. X1 is one position-by-position extraction among many possible. Its definition was registered; everything in "What the X1 result does and does not show" and the two post hoc sections was computed after the output was read. X1 concatenates segments in MAF stream order; the post hoc run found that order to be genomic order in all 19,407 transcripts.
4. The "affected" split uses a count-equality rule on a table rounded to four significant digits. Recomputed pooled values from the table match the json (V0 ALL 0.2712, X1 ALL 0.8532).
5. The SYN diagnostic is the audit's own (cov >= 0.5, modal share >= 0.95, dup <= 0.05, no inversion, span bound). Of the 1,704 NONSYN genes, 1,670 fail on dup, 385 on modal share, 376 on inversions, 275 on span, 80 on coverage (overlapping; post hoc counts).
6. The Q176 arithmetic targets a JC ratio with a p-ratio, as in L1 (difference below 1% at these p).
7. Tolerance for "~" predictions (±25%) is L1's, applied because the registration fixed none.
8. The run finished in 4 minutes against an estimate of 1-2 hours. All 5.37 million blocks were read (the block count equals GAP-07t's for the same file, correctness review), 33.49 of 33.51 Mb of chosen CDS lies in a block (human reference bases, not chimp coverage), and no reference row was skipped.
9. Severity. CRITIC was the audit's expected band (pre-run note, ST-08 row). As a test of Day's statement about the T2T assemblies it could have failed: his prediction was >= 0.65, and DAY and DAY-VALUE were reachable. It is not a test of his code.
10. Independence. L1 and L1b share one counting code and one orthology file. No DN verdict should be worded more strongly than "contradicted for an alignment-column extraction on two assembly and alignment pairs, one estimator".
11. In the post hoc breakdown, "length difference" means as Cactus aligns the two assemblies; first-cause attribution is one of several possible; holes and deletions cannot be separated at exon edges (7.1% of the excess).

## Open
- Day's per-gene table and Zenodo paper (Q176): not released as of the last refresh. The docstring lists the columns needed for a gene-by-gene comparison; `raw/l1b.genes.tsv.gz` has the same columns.
- L1c (alignment method against dN/dS, Q180-Q186) reads this run's segment dump. Its main run finished on 2026-10-13; write-up and reviews are pending. The share-uniformity table, the left-out-codon counts and points (a)-(d) of Day-side finding 3 go to it.
- GENCODE v46 lifted to hs1: a registered possible later variant, not run. It is the like-for-like annotation.
- For integration (not done here): the "98.8% of coding positions are found." sentence needs a Q entry; `raw/l1b.host` could gain the sha256 values now recorded in `raw/l1b_x1_breakdown.host`; the DN1 Readings table and the reading that sets the field are the owner's decision.
- Integration.

## Review resolution (fix pass, 2026-10-13)

Every MAJOR and MINOR of the three reviews is answered by id. C = correctness, D = steelman-day, K = steelman-critic. No verdict value changes. Where the two steelman reviews pull in opposite directions the lead's rulings were applied: registered wording stays registered; X1 goes under "Both"; DN1 gets a Readings table; the left-out codons are reported; the gene-set credit is stated with all numbers and no materiality label. New run: `l1b_posthoc_x1_breakdown.py` (9c4a359, post hoc). Numbers taken from the reviews were recomputed from `raw/l1b.genes.tsv.gz` and `raw/l1b.json` before use; all reproduced, with one difference noted under D3.

**Correctness review**

| id | sev. | answer | what changed |
|---|---|---|---|
| C1 | MAJOR | **Accepted.** | Post hoc run on the segment dump; new section "Post hoc: what puts X1's genes out of register". Result: first cause in-frame indel 55.7% of the excess, hole 28.8%, frame-changing indel 8.4%, exon edge 7.1%. "One extraction choice" replaced by "a naive ungapped extraction of the first chimp row"; item 1 now names length differences and coverage holes. The X1 sentence for the claim files is separate and labelled post hoc. |
| C2 | MINOR | **Accepted.** | Counted in the same run: 0 of 19,407 transcripts out of genomic order, 0 with overlapping segments. Clause added to caveat 3. |
| C3 | MINOR | **Accepted.** | "frame-preserving" replaced by "pairs bases by alignment column" in the Interpretation and the critics bullet; said once that keeping the frame is not sufficient (Interpretation bullet 1, limit i). The third place, the "Separate proposal", is withdrawn (K1). |
| C4 | MINOR | **Accepted.** | 73.6% labelled post hoc and outcome-defined wherever it is used; "as any pairing without constraint gives (L1 W2 72.7%)" and the single-difference ratio (0.84 against his 0.71) added to item 3 and to "Both". |
| C5 | MINOR | **Accepted in part.** | The unqualified "material by R1" is not carried to the T2T value, and the proposed DN3 text gives both pipelines and says size depends on annotation. Not adopted: the words "below it" for T2T. By the lead's ruling R1 is not applied after the run to grade the credit in either direction (see D4, K6); the T2T value carries no materiality label. |
| C6 | MINOR | **Accepted.** | The hit is kept; the row and the Day bullet now say it is the registered reading of Q176's antecedent and that Q184 reports 0.7956 on 1:1 orthologs. Interpretation bullet added. Carried to L1c/DN3 integration in "Open". |
| C7 | MINOR | **Accepted.** | Coverage sentence corrected in place (transcript-level figures separated from ALL: 33,424,287 CDS bases, 98.87% with a first-row chimp base); caveat 8 reworded. |
| C8 | MINOR | **Accepted in part.** | sha256 of the segment dump recorded in "Files" and checked by the post hoc script; sha256 of the dump and of the three outputs recorded in `raw/l1b_x1_breakdown.host`. Not done: appending to `raw/l1b.host`, which is outside the files this fix pass may touch; listed in "Open" for integration. L1c's host record is L1c's. |
| C9-C17 | NOTE | Applied: both tallies stated (C9); convention clause on the triple (C10); "about half or more" (C11); rule columns and json total 2,714,599 (C12); "no CDS-overlapping block" (C13); "on V0" (C14); "pooled value" (C15); "¶12" (C16). C17 needs no change for this run. | |

**Steelman, Day's side**

| id | sev. | answer | what changed |
|---|---|---|---|
| D1 | MAJOR | **Accepted in part.** | DN1 Readings table (A, B, C) added as a proposal, with the reading proposed for the field argued both ways. B stated in one clause for the comment. Not adopted: replacing "conditional on L1b" by "conditional on L1c" in the verdict field. The registered move discharges the L1b condition, and reading C is recorded in the table as not tested here and pending L1c; how the comment words that is left to integration. The field is not moved to `contested`, as the review itself does not ask. |
| D2 | MAJOR | **Accepted.** | (i) "One datum, two uses" paragraph in the Band section. (ii) The 73.6% is labelled post hoc and outcome-defined, and the comparison with his 71.6% is removed from the critics list; by the lead's ruling the whole X1 result sits under "Both", with both halves. (iii) The no-constraint counterpoint is stated in item 3, under the uniformity table and in "Both". LOCATED is not claimed by any route. |
| D3 | MAJOR | **Accepted in part.** | New section "Post hoc: the codons V0 leaves out": 129,092 codons (1.16%) in 2,411 genes, bounds 0.56 and 0.85, and the costs (a)-(d) with the 98.8% credit. The limit is added to Interpretation bullet 1 and to the proposed X1 sentence. Recomputation: the review's "at V0's own mix, 0.26" comes out as 0.27 here (unchanged from V0 ALL). Not adopted: using the draft's qualified wording "everywhere the registered wording appears". The registered sentence is kept as written, neither narrowed nor broadened (ruling 1); its scope, "this alignment", is spelled out next to it. |
| D4 | MAJOR | **Accepted in part.** | All numbers stated with equal weight (+14%, +30%, +3%, 1.93 times, gene counts); the R1 sentence is withdrawn as an unlabelled post hoc use. Not adopted: "14% or 30% by comparator" as the only statement (the +3% among syntenic genes is given too, K6), and no fresh endorsement of "material by R1" for L1: that wording belongs to L1's integration and is not touched here. |
| D5 | MINOR | **Accepted in part.** | Note under the tally: his position as of 2026-10-12, recorded both ways, and the statement that the tally is not a set of independent tests and that A4 was the one severe audit prediction. Not adopted: replacing the tally line. Counts stay as registered, with the reading note beside them. |
| D6 | MINOR | **Accepted in part.** | S' described as the literal reading of his ¶17; "the value on it is not" replaced by a statement that 9 genes give no useful precision (no bootstrap was run); DN2's two readings stated in the proposal. A formal Readings table for DN2 is left to integration, since DN2's comment already carries the split. |
| D7 | MINOR | **Accepted.** | Bound added to caveat 1 and to the critics bullet (1,090 genes would need a ratio near 10); dropped-transcript counts stated; v46 kept in Open as the like-for-like variant. |
| D8 | MINOR | **Accepted in part.** | "Correct extraction" replaced by "column-paired"; "position-by-position" used for X1 in descriptions. "Naive" is kept where it names the arm, because that is the registered name. "Mispaired" and "out of register" are kept as descriptions of what X1 does relative to the alignment. Day-side results (a)-(e) added to the Day list; the two caveat bullets moved to Caveats. |
| D9-D11 | NOTE | Applied: three-of-four count under S added to the Band sentence (D9); independence sentence in Interpretation and caveat 10 (D10); the two unlabelled items are labelled or withdrawn (D11). | |

**Steelman, critics' side**

| id | sev. | answer | what changed |
|---|---|---|---|
| K1 | MAJOR | **Accepted.** | The post hoc narrowing of the registered CRITIC sentence is withdrawn. DN1, DN2 and DN3 take the docstring's sentence as written. X1 is in a separate sentence labelled post hoc, which says it does not compare aligned positions after the first length difference. Limit, from ruling 1: the sentence is not broadened beyond "this alignment" either. |
| K2 | MAJOR | **Accepted in part.** | X1 moved out of the Day list to "Both", as the audit's own miss; L1's "in most genes" withdrawn for the pooled value; severity bullet moved to Caveats and reworded. Not adopted: entering X1 under Critics. By the lead's ruling it is credited to neither side, and Day's half (his number is reproducible in kind by a simple pipeline, which the audit did not expect) is stated as plainly as the critics' half. |
| K3 | MAJOR | **Accepted, with the Day-side counterpoint beside it.** | "The resemblance is partial" replaced by the split table: whole-set X1 shares 56.5-71.8%, affected-gene shares 73.2-74.5% in all four sets, V0 39.5-64.9%. Labelled post hoc. The inference is stated at class level, with the note that 72-76% is the no-constraint share under either explanation. Handed to L1c in "Open". No verdict move. |
| K4 | MINOR | **Accepted in part.** | Wording "a candidate error class with a real-data instance"; item 4 divides shown from not shown; the Band section says why the registered share test missed and that the affected-gene share is post hoc. Not adopted as worded: "(c) his share, and its uniformity, is the share of mispaired codons" is given as "the share he reports" with the no-constraint counterpoint. |
| K5 | MINOR | **Accepted.** | Interpretation bullet on Q184 (+0.003; 0.7956 against 0.238 inside the one2one set); hit annotated; Day bullet qualified. Rule N is stated as not licensed, as the review itself says. |
| K6 | MINOR | **Accepted in part.** | +3% among syntenic genes (+0.006) stated beside the credit, with the gene-level limit (0.276 against 0.203); composition of NON121 stated. Not adopted: "not material" for T2T and "below R1's line" in the Day bullet (ruling 5: no post hoc use of R1 to grade the credit). The "pipeline-specific" mark is not triggered, as the review agrees. |
| K7 | MINOR | **Accepted.** | Interpretation bullet with the per-gene values (median 0.163; 78.3% of genes below 0.40; X1 median 0.189, 70.5% below 0.40) and the stated limit; cross-reference to L1c. Worded as "carried by 13.7% of genes". |
| K8 | MINOR | **Accepted.** | Bound (pN/pS about 10.1 for the 1,090 genes) recomputed and added to caveat 1, the critics bullet and the left-out-codon section. |
| K9 | MINOR | **Accepted.** | Band paragraph and caveat 9 reworded: expected by the audit, able to fail as a test of the data statement, not a test of his code. Removed from the Day list. |
| K10 | MINOR | **Accepted.** | Strict-stack bullet gives both halves (count reproduced; half the stacks hold 8-12 genes under S', slip S-DN2-2; S' grid on V0 0.229-0.377); the DN2 sentence gives 0.82-0.86 without S and 0.52-0.58 with S. |
| K11-K14 | NOTE | Applied: limits of the critic inference stated in item 3 and "Both" (K11); robustness line under the tally (K12); set labels and `otype` counts defined (K13). K14 needs no change. | |

Not accepted in full, in one list: C5, C8, D1, D3, D4, D5, D6, D8, K2, K4, K6. In each case the part not adopted is either a post hoc change to registered wording or scoring (D1, D3, D5), a post hoc use of R1 to grade the gene-set credit up or down (C5, D4, K6), a side assignment of the audit's own miss (K2), an inference stated beyond class level (K4), a registered name (D8), or an edit outside the files of this pass (C8, D6).
