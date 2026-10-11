# Milestone 13: Day's dN/dS post checked, "ten of twelve" and 410 M recounted, and published alpha against the 191 flip
*2026-10-11 · stage: R4 (in progress) · A2e-alpha `49824e0`, `651e0d3`, `164837e`, `e7ecda6`, `7ea7290`; GAP-06/GAP-07t `49824e0`, `547bcd5`, `1b068bc`; refresh and test-methods review `448a7b6`; L1 `868bb60`, `36c5b85`; L6 `0b478dd`, `10cfe1e`; L7 `5b44f3d`, `42df167`; integration `524603e`*

This milestone covers what was done since [milestone 12](2026-10-10-12-mesas-replicated-median-25-and-k-to-64000.md):
- **A2e-alpha:** published alpha estimates against the roughly 191 adaptive-substitution threshold in A2e;
- **GAP-06 and GAP-07t:** Yoo 2025's mutation rate and generation times through Day's numbers; the divergence-event count on the T2T ape alignment;
- **The 2026-10-11 source refresh and a review of the test methods** proposed by both sides;
- **Day's 2026-10-11 post "How Biologists Keep 'Proving' Selection"** (Q172 to Q179): **L1** (dN/dS on two gene sets), **L6** ("ten of twelve" LTEE populations), **L7** (410 M versus 35 M).

L1 is the only load-bearing check here; the others are low-stakes (one combined review each). Reviews #51 to #60 are logged in `research/checks/REVIEW.md`. Nothing here has been peer-reviewed. **The H follow-ups (HF) are not final** and appear only in their own section below.

## Corrections of the audit's own errors
Five statements from this round's drafts are withdrawn. Each was caught by a review of the audit's own check and is recorded as the audit's error, not Day's or the critics'.
- **L1, frame-error attribution.** The first write-up attributed Day's 0.80 to a reading-frame error in part of the gene set. A gene-level mixture of frame errors cannot give his figure while leaving thousands of intact genes, and Day's own Q175 (no filter stack goes below 0.65) contradicts it. **Withdrawn**; the cause of his number is unidentified.
- **L1, "0.70 to 0.91".** An agent report said per-gene mean or median ratios gave 0.70 to 0.91. The raw output (`raw/l1_dnds.out`) gives a per-gene mean of 0.245 to 0.438 and a median of 0.15 to 0.31 on a correct frame. **The figure was wrong and is withdrawn.**
- **L7, the 0.83 base rate.** A pre-registered test of whether 410 M is a special number used a random-target pool that contained the readings themselves. **Withdrawn.** On a primitive pool, 410 M sits at the 92nd to 100th percentile of random targets (ratio 1.3 to 1.7), so near-matches are common and the route is unconfirmed rather than confirmed.
- **A2e-alpha, "29 to 49" for Gayà-Vidal.** A pre-registered mapping turned a published alpha of 0.2% into a count of 29 to 49. The 0.002 is a McDonald-Kreitman null in a still-rising sequence (-0.361, -0.142, -0.059, 0.002; FI 1.00), not a count. **Withdrawn.**
- **A2e-alpha, the "100-fold disagreement".** The draft said the literature disagrees about 100-fold. That framed an uncorrected null, which its own authors flag as biased low, as one side of a dispute. **Withdrawn as false balance.**

## A2e-alpha: published alpha estimates against the 191 flip
A2e (the LTEE as ceiling) survives only if the human lineage had about 191 adaptive coding substitutions or fewer (alpha at or below about 0.65 to 1.75% of coding substitutions).
- **Bias-corrected estimates all land above it.** Boyko 9.3% (95% CL 5.4 to 12.8%; 1,031 to 1,691 central, 599 to 982 at the lower CL); Uricchio 0.135 (abstract only, full text queued); Eyre-Walker's conditional 40%. The lowest compounded Day-charitable row (lower CL, 25% human share) is 299 (1.57 times 191). A2e survives only if about 36% or more of Boyko's residual is model artefact.
- **The lowest value is not a count.** Gayà-Vidal's 0.2% is an uncorrected null (see above). Its 198 accelerated genes, mapped post hoc after the critic-side review, give 228 (bootstrap 112 to 323), or 67 to 136 after an ascertainment correction: at the threshold, straddling 191.
- **All of these are model inferences.** None observes fixations.
- **Verdict:** A2e internal non-sequitur (unchanged), fidelity n/a for Day, external **contested, leaning contradicted**. It moves to contradicted with a full-text Uricchio, or any other bias-corrected human-branch alpha above about 1%.

## GAP-06 and GAP-07t: Yoo's rates and the T2T event count
- **GAP-06** (combined review #51). Yoo's mu is 4.2% above Day's and his human generation time equals Day's 25 y; the HCB node (24.5 y) adds 2% generations. No propagated number moves by 25% (maximum 19.7% as pre-registered; 4.2% once mu is held per year). Day's printed k = 32.3 matches the 24.5 y basis. Counted versus k = mu route, using GAP-07t's 24.14 M, is 2.15 to 2.58: the clock tension is untouched. No verdict change.
- **GAP-07t** (combined review #52). On hs1 versus mPanTro3: 42.87 M SNVs, 5.40 M indel events, **24.14 M events per lineage** (+14.7% on GAP-07b's 21.05 M; the R1 25% threshold is not triggered). Day's 205 M bp is 8.49 times that raw, 9.2 to 10.9 times polymorphism-corrected, 10.4 times single-copy. A chimp-referenced pass gives 24.03 M. In that pass's raw report the SNV lineage labels are swapped (disclosed, read as swapped). For Day: the count has risen again and is the low end of his roughly 20 M. For the critics: events, not bp, still gives 8.5 times or more. No verdict change.

## Day's dN/dS post (L1)
Day and Athos report a genome-wide dN/dS of 0.80 on 20,400 GENCODE v46 genes, against the Consortium's 0.23 on 13,454 genes (Q173, Q174), and state that "No combination of quality filters moves the number below 0.65" (Q175). Q176, his own proposed test: reconstruct the Consortium's gene list and run the same pipeline on both sets. Q177 draws the conclusion "At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution."
- **Q176 is a valid, discriminating test**, and L1 runs its Ensembl analogue. On hg38/panTro5 codon alignments (UCSC knownCanonical, 23,183 genes), Nei-Gojobori pooled dN/dS is **0.207 on Ensembl one2one genes** (0.200 with CSAC-like filters), **0.271 on all genes** and 0.447 on the non-one2one genes.
- **A gene-set effect exists in Day's direction:** +0.06, +31%, material under rule R1. It is a pipeline-level upper bound.
- **0.80 is not reproduced.** Every one of 32 filter stacks gives 0.23 to 0.28 (the full stack keeps 13,610 genes; 258 with a terminal-stop convention). On a correct frame, the per-gene mean is 0.25 to 0.44 and the median 0.15 to 0.31.
- **His single-SNV count is estimator-free:** 2.52 nonsynonymous per synonymous in his pipeline, against 0.85 on correctly aligned coding sequence, and no assembly change raises it. This points to an unidentified extraction or alignment problem, not a gene-set effect. "All genes" is itself aligned through the syntenic net, so a complete-extraction route is open: **L1b, a T2T rerun, is queued.**
- **Q177 does not follow from its premises by Day's own material (rule N):** his own P6, P20 and P21 treat dN/dS as the purifying/neutral balance of all nonsynonymous changes, not the adaptive fraction (alpha).
- **Pending on both sides:** Day's per-gene table (promised on Zenodo, not yet released); CSAC 2005 text and an independent ML estimate to score the 0.23 relay.

## L6: "ten of twelve" LTEE populations undoing fixations (Q178)
Day writes "ten of the twelve populations even show intervals where fixations are being undone faster than any new ones complete."
- **It reproduces on his rule.** From Good 2017's public trajectories, the count of mutations at or above 95% frequency falls in at least one 10K interval in **10 of 12 populations**, exactly as he says (sign only; 7 of 12 at a net fall of 5 or more, 6 of 12 at 10 or more). 28 of 29 of his tabulated cells match.
- **Good's own fixed calls never fall**, but the fixed state is never left in the published paths (6,834 entries, 0 exits in 34,118), so that is a property of the calls, not a measured absence of reversals.
- **Of 972 exits from the 95%-or-above set, 34% return, 62% hover and 4.6% are lost.** The audit's prediction that at least 30% would be real losses missed.
- **E10: holds / partial / contested.** "Fixations" relabels a snapshot statistic (A2c, E6); the data cannot contradict "undone" except by definition. Open: Good SI 5.2 and the clade-level states.

## L7: 410 M versus 35 M in Yoo 2025's SI (Q179)
Day says the T2T paper's real number involves "an estimated 410 million total genomic differences, not 35 million."
- **410 M reproduces, as base pairs.** Mean SNV plus gap divergence (SI III.14, 13.94%) times hs1 length (III.19) gives 404.2 M (autosomes) and 412.7 M (autosomes plus X); medians give 82 M. His locator is accurate, and the earlier A3x1 label "not found in the paper" was too strong.
- **The route is unconfirmed** (see corrections), and 14.9% is reproduced only approximately (15.05%). Day's printed Zenodo components sum to 222 M (scored at A3a).
- **Every reproducing reading is base pairs**, about 8.5 times the T2T event count (GAP-07t; different units, so an upper-bound contrast). The bp-versus-events point (A3x) stands.
- **Verdicts:** A3z holds / partial / contested; A3x1 unchanged.

## Refresh and test-methods review
The 2026-10-11 refresh (`sources/refresh-2026-10-11.md`) found one new relevant Day post (the dN/dS one), no change in the Zenodo listing (39 records) and no critic reaction yet. `sources/test-methods-review-2026-10-11.md` catalogues 17 proposed test methods from both sides and queued L1 to L7 from it. No verdict changed.

## HF (H follow-ups): not final
The main run finished (696 jobs on two hosts, 1,720 unique, 0 mismatches) and three reviews are done (0 BLOCKER, 10 MAJOR). A post hoc run `ph` (pre-registered, 410 jobs) is in progress on na-workhorse and the builder, about 31 hours. **Provisional, pending `ph`, no claim file changed:** soft-selection and truncation results are scoped to "purely relative fitness" and "noise-free genotype truncation"; some pre-registered scores were rescored (for example CA2 fails marginally at R = 1.111 and DA1 fails at h = 0.1, R = 2; two comparisons of censoring points are unscorable); the "43 times" figure splits into 4.5 times from selection and 9.6 times from Day's premise; and latency (HF-c) and throughput (HF-a) results must be cited together. Full detail is in the Review resolution of `results/R4-HF.md`.

## Verdict changes
| Claim | Before | After |
|---|---|---|
| A2e (LTEE as ceiling) | non-sequitur / n/a / contested | unchanged internal; external **contested, leaning contradicted** |
| DN1 (0.80 genome-wide) | new | pending / n/a / **contradicted** |
| DN2 (filters do not move it below 0.65) | new | pending / n/a / **contradicted** |
| DN3 (gene-set confound, Q176 test) | new | **holds** / pending / **contradicted** (gene-list version) |
| DN4 (0.80 implies selection not primary) | new | **non-sequitur** / n/a / contested |
| DN5 (Consortium 0.23) | new | n/a / pending / **supported** |
| E10 ("ten of twelve") | new | **holds** / partial / **contested** |
| A3z (410 M in Yoo's SI) | new | **holds** / partial / **contested** |
| A3x1 ("not found") | partial | unchanged; label "not found" too strong |
| GAP-06, GAP-07t | n/a | no verdict change |

Totals after integration (232 claims): internal 130 hold, 19 non-sequitur, 2 arithmetic error, 52 pending; fidelity 43 accurate, 38 partial, 10 misread, 58 unverifiable, 12 pending; external 34 supported, 115 contested, 16 contradicted, 6 untestable, 49 pending. The argument map holds 419 typed objections and 232 dated versions.

## Who this helps
| Result | Helps Day | Helps the critics |
|---|---|---|
| L1 | Q176 is a valid, discriminating test; a gene-set effect exists in his direction (+31%, material); his paragraph 15 arithmetic and hedges are credited; "all genes" is itself net-aligned, so the complete-extraction route is open | 0.23 reproduces in kind (0.207 to 0.28); 0.80 is not a gene-set property; his own single-SNV count (2.52 versus 0.85) points to an extraction problem; Q177 does not follow |
| L6 | "Ten of twelve" reproduces exactly on his snapshot rule; 7 of 12 at a net fall of 5 or more | The relabelled statistic is not a fixation count; 34% of exits return and 62% hover; the fixed state is never left in Good's calls |
| L7 | 410 M reproduces from the paper's SI, as he said; his locator is accurate | It reproduces as base pairs (about 8.5 times the event count); the route is unconfirmed; his Zenodo components sum to 222 M |
| A2e-alpha | Gayà-Vidal's 198 accelerated genes give 67 to 228, straddling 191; every value is a model inference, none observes fixations | Bias-corrected estimates all above the flip (299 at the lowest compounded row); the only sub-1% value is a biased null |
| GAP-06 / GAP-07t | His printed k = 32.3 matches the 24.5 y basis; the event count rose to 24.14 M, near his roughly 20 M | Events still give 8.5 times or more; the clock tension is untouched |

Reading across the table: Day's reproducible items (ten of twelve, 410 M as bp, the value of his Q176 design) are credited as such. The numbers that carry his conclusions (0.80, the human alpha at or below 191) were not reproduced by any pipeline tried here. What is left for Day's side is the unidentified source of 0.80 and the possible T2T complete-extraction route; what is left for the critics' side is an independent ML estimate and the full-text Uricchio.

## What stays uncertain
- **Where Day's 0.80 comes from.** L1b (T2T rerun) and his per-gene table are pending.
- **DN5 fidelity:** CSAC 2005 text and an independent ML dN/dS estimate.
- **E10 external:** Good SI 5.2 and the clade-level states.
- **A2e:** a full-text Uricchio (or another bias-corrected human-branch alpha) would settle contradicted.
- **FM10 internal, the chrX 57.3 Mb window, the B3m 2-versus-25 gap, the Hard Limits peroration RH tag** (from milestone 12), and XT's unexplained deficit.
- **HF:** every number in its section is provisional until `ph` is scored.

## Next
- Finish and review HF `ph`, then integrate HF.
- L1b: T2T rerun of L1 on na-workhorse (pre-register first).
- Fetch tasks: CSAC 2005 and an independent ML estimate; Good 2017 SI 5.2; Uricchio full text; Day's per-gene table when released.
- Stage R5 begins when the load-bearing claims without a reviewed check are resolved.

```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
