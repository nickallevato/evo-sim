# R4 L1b: human-chimp dN/dS on the T2T assemblies (hs1 against mPanTro3, Cactus), and what a naive extraction reads on the same data

**Status: written up, NOT reviewed, NOT integrated.** Three post-run reviews are owed (correctness, steelman-day, steelman-critic; tier as registered in the docstring). Every verdict statement below is a proposal; the owner decides. Band by the registered rule: **CRITIC**.

## Target
Day, "How Biologists Keep 'Proving' Selection" (voxday.net, 2026-10-11; quotes-day.md Q172-Q177). RH tag: dialectic (numeric claims).
- Q172 (¶7): "We used GENCODE v46 annotations, the same Nei-Gojobori method the original studies used, and the complete extraction of human-chimp aligned positions from the T2T-quality assemblies. And we got a result."
- Q173 (¶9): "Not 0.23. 0.80."
- Q174 (¶13): "We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46 that has coding sequence data in the human-chimp alignment."
- Post body (diagnostics ¶, as quoted in the registration): "Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for single-SNV codons alone."
- Q175 (¶17): "No combination of quality filters moves the number below 0.65." (same ¶, as quoted in the registration: the strictest stack "still produced dN/dS = 0.64 on 10 remaining genes").
- Q176 (¶22): "If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome."
- Q177 (¶21): "At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution." (DN4; not moved by this check.)

Claims: DN1 (0.80 on 20,400 genes), DN2 (filter robustness), DN3 (Q176 conditional), DN5 (CSAC 0.23 as relayed). L1 (hg38/panTro5, `R4-L1.md`) left the T2T route open and fixed in advance what would overturn DN1's external verdict. This run is that test.

## Files
- Script `research/checks/l1b_t2t_dnds.py`, pre-registered at **0fe3c7f** (before the commit only a synthetic selftest and the annotation-count step were run). Pre-run note `R4-L1b-L5-prerun-notes.md` (**5e64f0a**, before launch): assigns the two outcome regions the bands left unclassified (ST-08) and states the expected band, CRITIC. Script unchanged between registration and run (md5 `aef21cb3...` in `raw/l1b.host`).
- Run: na-workhorse, one process, host record dated 2026-10-13 16:53 UTC. **Wall time 4 min 11 s** (extraction 127 s, analysis 91 s), peak RSS 481 MB. The registered estimate was 1-2 h and under 2.5 GB; the estimate was wrong by a factor of about 15 to 30 on time. Exit status 0.
- Outputs: `raw/l1b.out`, `raw/l1b.json`, `raw/l1b.genes.tsv.gz` (per-gene table, 19,310 rows), `raw/l1b.host`. Collected at c168b65. Segment dump on na-workhorse (`sources/raw/l1b-seg-2026-10-13/seg.json.gz`, gitignored); L1c reads it.
- Data (public, read as text, never executed; hashes in `raw/l1b.host` equal the registered ones): T2T consortium annotation GENCODE v35 projected to CHM13 v2.0 by CAT + Liftoff; Ensembl 116 BioMart orthology file (the L1 file); 8-way T2T-ape Cactus MAF referenced on hs1, chimp mPanTro3.
- **Not Day's pipeline, in three stated ways.** GENCODE v35 projected by CAT, not v46 (Q172, Q174). One transcript per gene by the audit's rule; his transcript choice is unstated. The Cactus MAF; his aligner is unstated. All three are the audit's choices.

Extraction counts: 5,366,631 MAF blocks; 169,678 overlap a chosen CDS; 11,229 of those (6.6%) carry more than one chimp row; 653 carry none; no block had the reference on the minus strand or out of first position. 19,407 transcripts chosen, 97 with no aligned chimp base, **ALL = 19,310 genes** covering 33,494,864 of 33,505,272 CDS bases.

## Results (pooled = ratio of totals, Nei-Gojobori sites, Jukes-Cantor)

Chimp-row variants: V0 first chimp row per block (primary); VS syntenic row; VR random row; VL lowest-identity row (adversarial); X1 naive ungapped extraction (chimp bases concatenated with gaps removed and chimp-only insertions kept, compared position by position).

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
- **Day's four-part triple** (pooled 0.70-0.90; share 66-77%; min over stacks >= 0.60; full stack <= 200 genes). V0, VS, VR, VL: 0 of 4 under S; 1 of 4 under S' (the survivor count). **X1: 1 of 4 under S (pooled only); 3 of 4 under S' (pooled, filter minimum, survivor count). The part X1 misses under both conventions is the single-difference share: 60.1% against the 66% floor.** No variant meets the triple.
- **Terminal-stop convention.** 19,294 of 19,310 human CDS end in a stop codon in this annotation (post hoc count from the per-gene table). S' alone therefore keeps 12 genes on V0, and the S' full stack keeps 9 (L1's annotation: 861 and 258).

## Band
`band()` as registered reads V0 ALL = 0.271, V0 SYN = 0.209, share on SYN = 40.2%, and whether VR, VL or X1 meets the triple on ALL under S or S'.
- DAY needs ALL >= 0.65: no.
- LOCATED needs ALL >= 0.65 **or** one of VR/VL/X1 meeting the triple, with SYN < 0.40. SYN < 0.40 holds. The `other` clause did not fire: X1 under S' has parts [1, 0, 1, 1], missing only the share (60.1% < 66%). A share 5.9 points higher would have put the run in LOCATED.
- MIDDLE: neither value in [0.40, 0.65).
- **CRITIC: ALL < 0.40 and SYN < 0.40.**

Neither region assigned in the pre-run note (DAY-VALUE, MIDDLE anomalous) was reached. The pre-run note stated CRITIC as the expected band, so the band is not a surprise (ST-08 row: the weight comes from the assemblies and alignment being the ones Day names). The X1 result was a surprise; see below.

## Scoring of the pre-registered predictions
Hits and misses are listed with equal weight. "~" predictions use the tolerance L1 used (±25%, R1's line).

| prediction (registered) | value | result |
|---|---|---|
| Day: V0 ALL ~0.80, at least >= 0.65 | 0.271 | **miss** |
| Day: single-diff nonsyn share ~72% (>= 66%) | 44.9% | **miss** |
| Day: no 32-stack combination below 0.65 | all 32 below 0.65 (max 0.283) | **miss** |
| Day: O121 ~0.23 | 0.238 | **hit** |
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

Tally: Day 1 of 5; critic 6 of 6; carry-over 3 of 3; audit A1-A6 11 of 12 parts, with the one miss on the prediction that mattered most for locating Day's number.

Note on A3's second part. The json does not carry this number. It is computed post hoc from the per-gene table as the length-weighted mean of `dup` (CDS bases in blocks with more than one chimp row), which is 5.10%; values in the table are rounded to four decimals. 1,907 genes have dup > 0.

**The A4 miss and its stated reason.** A4's reason was "real human-chimp CDS indels that are not multiples of 3 are too rare to put most genes out of register". The premise about "most genes" held (next section: 13.7% of genes are affected). The conclusion did not follow. X1 compares position by position, so any unhandled length difference, in frame or not, pairs every downstream codon with a non-homologous one, and a pooled ratio weights genes by their differences. The audit did not anticipate that a minority of genes would carry the pooled value.

## What the X1 result does and does not show

**Post hoc and descriptive; computed from `raw/l1b.genes.tsv.gz` after reading the output; no registered prediction.** A gene is called "affected" if its X1 difference counts differ from its V0 counts.

| genes | n | X1 pooled | X1 share | V0 pooled on the same genes | share of all X1 differences |
|---|---|---|---|---|---|
| unaffected (X1 counts = V0 counts) | 16,673 (86.3%) | 0.205 | 39.8% | 0.205 | 5.9% |
| affected | 2,637 (13.7%) | **0.960** | **73.6%** | 0.427 | **94.1%** |
| all | 19,310 | 0.853 | 60.1% | 0.271 | 100% |

- X1 counts 2,714,597 differences against V0's 256,778. Half of the excess sits in 381 genes (2.0%), 90% in 1,458 genes (7.6%).
- Affected share by set: 8.9% of SYN genes, 11.8% of O121, 26.3% of NON121. Because pooling weights by differences, the pooled X1 value is nearly the same in every set (ALL 0.853, O121 0.844, SYN 0.818, NON121 0.898) although the affected fraction differs threefold.
- Per gene, X1 is 0.65 or higher in 19.5% of genes with a defined ratio (V0: 9.8%). Mean 0.345, median 0.189.
- Of the affected genes, 2,291 have at least one gapped or uncovered chimp codon on V0 (a chimp deletion or missing coverage); 346 have none (consistent with a chimp-only insertion; not checked gene by gene).
- A stop filter removes much of it: S alone gives 0.554 on 16,908 genes; every stack containing S reads 0.52-0.58; every stack without S reads 0.82-0.86.

What this supports:
1. **A pipeline can read Day's headline number on these assemblies.** One extraction choice, applied to the same alignment and annotation, moves the pooled value from 0.271 to 0.853. Day's 0.80 lies between them, closer to X1.
2. **X1 as built is not Day's pipeline.** Against his reported numbers it misses the share (60.1% against 71.6%), the filter floor under an ordinary stop filter (0.524 against "none below 0.65"), and the strict-stack size under S (10,673 against 10). Under the terminal-stop convention S' it matches the filter floor (0.818) and the survivor count (8 against 10) and still misses the share; its strict-stack value is 0.861 against his 0.64, on 8 genes.
3. **The share is the discriminating datum, as in L1.** His 71.6% is 2.52 nonsynonymous per synonymous single-difference codon. V0 ALL gives 0.82, X1 ALL 1.51, X1 on the affected genes alone 2.79. His count behaves like X1's affected genes, not like X1's whole set. A pipeline that matched his share would need mispaired sequence in most of the codons it counts, which X1 on this alignment does not produce.
4. **The audit has not seen Day's pipeline.** "His 0.80 is an extraction artefact" is a candidate explanation, located as a class and now shown to be reachable on real T2T data. It is not shown. L1's W2 was a synthetic break in every gene; X1 is a real-data instance of the same class that reaches the pooled value and not the signature.

One observation outside this check's targets, recorded for L1c and DN6 and not scored here. Day's later post ("The Method is the Conclusion", 2026-10-12) reports "It's 73.8% nonsynonymous across every subset we tested. The signal is uniform across the genome, it's not concentrated in problematic genes." (Q183), with a table of pooled values near 0.80 for all genes, 1:1 orthologs and the excluded set (Q184). X1 also gives a nearly uniform pooled value across gene sets while 86% of its genes are untouched, so uniformity of a pooled value across sets does not show uniformity across genes. X1's share is not uniform (56.5% to 71.8% by set) and is below his in every large set, so the resemblance is partial. His per-gene table would separate the two readings.

## Interpretation
- **The T2T route does not reach 0.80 with a frame-preserving extraction.** On hs1 against mPanTro3 from the Cactus alignment, all genes give 0.271, the same value to three decimals as L1 on hg38/panTro5 with UCSC multiz. The chimp-row choice moves it between 0.246 (syntenic) and 0.293 (lowest-identity row, an adversarial bound). The 32 filter stacks move it between 0.214 and 0.283.
- **Paralog choice is not the route either.** Blocks with more than one chimp row hold 5.1% of CDS bases, and always taking the worst row adds 0.022.
- **The Consortium-type value is reproduced a second time**: 0.238 on Ensembl one2one, 0.208 with CSAC-like quality filters, 0.209 on the syntenic set.
- **The gene-set effect is real in kind and smaller than in L1.** ALL exceeds O121 by +0.033 (ratio 1.14; L1 +0.064, 1.31). The registered carry-over band held, in its lower third. The per-gene value of non-one2one genes is unchanged (0.459 against L1's 0.447); the gap is smaller because this annotation has 2,486 such genes against L1's 6,417 (9.8% of nonsynonymous sites against 18.8%) and because O121 is higher (0.238 against 0.207). Under R1's 25% line the L1 gap (+31%) was material and this one (+14%) is not. Q176 needs +0.57.
- **Synteny carries most of the gene-set difference.** SYN and O121SYN read 0.209 and 0.203; NONSYN reads 0.491. The syntenic-row variant VS brings NON121 to 0.427 only, so the higher value of non-one2one genes is not removed by picking the syntenic copy.
- **Strict-stack size is a convention effect, not a signature.** With a stop filter that counts the final codon, a correct extraction also leaves 9 genes (Day: 10). The value on those 9 is 0.302 (his: 0.64). The near-empty stack that L1 treated as part of his signature is reproduced here without any extraction fault; the value on it is not.

## Proposed verdict moves (band CRITIC; exactly as registered under "WHAT MOVES WHICH VERDICT"; proposals, the owner decides; three reviews still owed)

| claim | field | now | registered rule | value | proposal |
|---|---|---|---|---|---|
| DN1 | external | `contradicted` (comment: conditional on L1b, MA-12) | CRITIC: stays, "now on T2T and Cactus as well (the 'different assembly / complete extraction' route is closed for this alignment)" | ALL 0.271, SYN 0.209 | **stays `contradicted`**; the comment's "conditional on L1b" clause is discharged for this alignment and annotation |
| DN1 | internal | `pending` | stays `pending` (method unreleased) | | stays |
| DN2 | external | `contradicted` | re-opened (`contested`) only if min over 32 stacks on V0 ALL or SYN >= 0.60 | 0.214, 0.194 | **stays `contradicted`** |
| DN3 | external | `contradicted` (gene-list version) | `supported` only if ALL - O121 >= +0.40 with O121 <= 0.30 on V0; otherwise stays, "now also for the alignment-level version" | +0.033, O121 0.238 | **stays `contradicted`, extended to the alignment-level version** |
| DN3 | credit to Day | +31%, material by R1 (L1) | "restated with the T2T value; if the gap is < +0.02 the credit is marked pipeline-specific" | +0.033, ratio 1.14 | **restated: +14% on T2T (L1: +31%)**; gap >= +0.02, so not marked pipeline-specific. The T2T value is below R1's 25% line; whether the comment keeps "material by R1" for L1 only is a wording question for the reviews |
| DN5 | external | `supported` | stays if O121 in 0.18-0.30 | 0.238 | **stays `supported`** |
| DN5 | fidelity | `accurate` | not moved here | | not moved |
| DN4 | all | | not moved | | not moved |

No verdict value changes. The moves are comment-level: one condition discharged (DN1, and the same MA-12 clause on DN2 and DN3), one scope extended (DN3), one credit restated (DN3).

**Separate proposal, post hoc, not licensed by the registration.** The registered CRITIC wording says the "complete extraction" route is closed. X1 shows that this needs a qualifier. Suggested wording for the DN1 and DN2 external comments, for the reviewers to accept, change or reject:
- "closed for a frame-preserving extraction on this alignment and annotation; a naive ungapped extraction of the same data reads 0.853 pooled (share 60.1%, per-gene median 0.189), carried by 13.7% of genes";
- naive extraction named as a **candidate** error class, not a located one. The registration licensed naming the class only under band LOCATED, and the run missed LOCATED on the share;
- DN2's existing sentence that his filter report is plausible as a report of his own pipeline gains a real-data instance: X1 is filter-robust at 0.82-0.86 in every stack without an internal-stop filter, and at 0.82 or higher in every stack under S'.

## Who this helps
- **Day.**
  - His stated assemblies were testable because he named them, and his O121-type expectation (~0.23) is met at 0.238.
  - The gene-set effect has his sign on T2T as well, inside the band the audit registered for it.
  - A pipeline can read his number on these data. The audit predicted it could not (A4) and was wrong. L1's inference placed the mispairing "in most genes" (R4-L1.md, Derivation). For the pooled value alone that is too strong: mispairing in 14% of genes reaches it. For his share and his filter report it still stands.
  - His near-empty strict stack (10 genes) is reproduced on a correct extraction under a terminal-stop convention (9 genes), so that part of his report is no longer evidence of a fault.
  - The annotation, the transcript rule and the aligner are the audit's, not his. GENCODE v46 was not used. "Extraction artefact" remains a candidate until his pipeline or per-gene table is seen.
  - Severity limit: CRITIC was the expected band (pre-run note, ST-08 row), so the band result alone is a weak surprise; it is a test of the data statement, and only a partial test of what his pipeline did.
- **Critics.**
  - On the T2T assemblies Day names, with a frame-preserving extraction, pooled dN/dS is 0.25-0.29 under every chimp-row choice and 0.21-0.28 under every filter stack. All six critic-side predictions hit.
  - The "different assembly" and "complete gene set" routes to 0.80 are closed for this alignment and annotation: paralog choice adds at most 0.022, and non-one2one genes would need a pN/pS of 3.95.
  - The published 0.23 is reproduced in kind a second time (0.238; 0.208 with quality filters; 0.209 syntenic).
  - The one tested way to read about 0.80 on these data is an extraction that leaves chimp sequence out of register, and in the genes where it does so the single-difference share is 73.6%, next to his 71.6%.
- **Both.** The single-difference share again separates the candidates, and Day reported it. His per-gene table (Q176) would show at once whether his high value sits in most genes or in a minority.

## Caveats for the reviewer
1. GENCODE v35 by CAT/Liftoff, not v46. ALL is 19,310 genes against his 20,400; O121 16,824 against the 13,454 of CSAC 2005.
2. One alignment (Cactus, hal2maf, hs1 reference). A different aligner is L1c's subject and is not tested here.
3. X1 is one naive extraction among many possible. Its definition was registered; everything in "What the X1 result does and does not show" was computed after the output was read.
4. The "affected" split uses a count-equality rule on a table rounded to four significant digits. Recomputed pooled values from the table match the json (V0 ALL 0.2712, X1 ALL 0.8532).
5. The SYN diagnostic is the audit's own (cov >= 0.5, modal share >= 0.95, dup <= 0.05, no inversion, span bound). Of the 1,704 NONSYN genes, 1,670 fail on dup, 385 on modal share, 376 on inversions, 275 on span, 80 on coverage (overlapping; post hoc counts).
6. The Q176 arithmetic targets a JC ratio with a p-ratio, as in L1 (difference below 1% at these p).
7. Tolerance for "~" predictions (±25%) is L1's, applied because the registration fixed none.
8. The run finished in 4 minutes against an estimate of 1-2 hours. The block and base counts above (all 5.37 million blocks read, 33.49 of 33.51 Mb CDS covered, no skipped reference rows) are the evidence that the stream was complete; a reviewer should confirm.

## Open
- Day's per-gene table and Zenodo paper (Q176): not released as of the last refresh. The docstring lists the columns needed for a gene-by-gene comparison; `raw/l1b.genes.tsv.gz` has the same columns.
- L1c (alignment method against dN/dS, Q180-Q186) is running and reads this run's segment dump. The Q183/Q184 observation above belongs to it.
- GENCODE v46 lifted to hs1: a registered possible later variant, not run.
- Which indel classes put the 2,637 genes out of register under X1 (in-frame, frameshifting, missing coverage): not broken down; the segment dump allows it.
- Three post-run reviews, fix pass, integration.
