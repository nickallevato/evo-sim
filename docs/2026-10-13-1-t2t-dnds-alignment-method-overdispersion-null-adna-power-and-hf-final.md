# Milestone 14: dN/dS on the T2T assemblies, the alignment-method claim, a neutral null for "80 times", ancient-DNA power, and HF final
*2026-10-13 · stage: R4 (in progress) · HF `edfe33c`, `c2ac2c3`, `06978f1`; L1b `0fe3c7f`, `5e64f0a`, `188ea43`, `098ac12`; L1c `536b19b`, `0e0e840`, `b9e83e0`, `140a69a`; L1b/L1c integration `cf03b3b`; FMnull `48241c7`, `408ba53`, `b3c0ab3`, `2802425`, `7c0e33e`; L5 `0e6da82`, `1ffdade`, `0b0431c`, `cb5ed16`; refresh `10bdee6`; criticality pass vii `20bcecf`; catch-up items `db2d16d`, `e03f516`, `3f881b0`, `44cf0c5`*

This milestone covers everything since [milestone 13](2026-10-11-1-dnds-ten-of-twelve-410m-and-alpha.md).

**What a reader most needs first.**
- **No verdict value moved toward either side's conclusion today.** The one claim decided today is DN6 (Day's statement that protein-guided alignment produces the low dN/dS): external `contested`, fidelity `misread`, both reading-dependent. External takes reading b2 (the mechanism and its direction, as Q180 to Q182 are worded); the stricter reading b1 (the published 0.23 is this artefact) is `contradicted` and is recorded beside it. Fidelity takes reading a (the Consortium's 0.23 was produced by a protein-guided alignment); the broad reading is `partial` or `unverifiable`.
- **Three registered bands came out CRITIC** (L1b, L1c, L5). **FMnull has no band:** no class, no move. In parts of three of the four new checks a Day-side outcome could not have been reached, so "three CRITIC bands" is true and is not a score (see the reachability table in the method-audit section).
- **The registered L5 verdict flip was withheld.** The script registered C external `contested` to `contradicted` (scoped) for band CRITIC. The band came out CRITIC and the flip was not applied, for two reasons: the result at low selection was arithmetic already contained in the registration, so the run did not test the move; and the post that carries Day's comparator states no selection coefficient, so the reading under which the move holds is not the only plausible one.
- **A critic video reply now exists and has not been reviewed by the audit** (4:14:03, posted 2026-10-13; no captions at fetch time). Nothing in this post says critics have, or have not, replied in substance to the dN/dS posts or to "The Fourth Mechanism". No written critic reply was found.

HF, L1b, L1c and FMnull had three post-run reviews each (HF's post hoc run `ph` one combined review); L1c and FMnull also had a pre-run design review; L5 had one combined review. Reviews #61 to #80 are logged in `research/checks/REVIEW.md`. **Every reviewer was an instance of the same model that wrote the checks. Nothing here has been peer-reviewed.**

## Corrections of the audit's own errors
Each item is the audit's error, not Day's or the critics'. "Favoured" means whom the error helped before it was caught (the classification is the method audit's, section 6 of [`METHOD-AUDIT-2026-10-13.md`](research/criticality/METHOD-AUDIT-2026-10-13.md)).

| Error | Caught by | Favoured before it was caught |
|---|---|---|
| **L5, two launch bugs.** Launch 1 stopped on an unpicklable task tuple; launch 2 on `sel(1.0, 0.003)` returning 1 + 2^-52. Both fixed post hoc before any task output existed (`369354d`, `30e1302`) | the launches | nobody; no result existed |
| **L5, the V3 bias direction.** A selftest validation missed at tight linkage. Before the run the lead wrote that the miss biased expected counts "toward Day's band". **Withdrawn.** A rerun at n = 1,500 does not reproduce the miss; the formula's real fault is in the distribution and understates two of Day's statistics (Z50, Z10) at strong selection, which runs against Day | combined review, post hoc rerun (`c9f3d69`) | critics: it made CRITIC look conservative and hid an understatement that runs against Day |
| **FMnull, label bug since registration.** The code mapped the label `1Mb`; the input file calls the cell `1000kb`. Twenty 1-Mb cells were silently dropped from predictions P4 and P5 | write-up author, confirmed by review | neither clearly; no hit, miss or direction changes after the fix |
| **FMnull, grid-phase dependence.** Prediction P8 (ii) (a dominant planted block model gives an index above 100) hit at 103 only because blocks and windows shared a grid; off the grid it reads 52.5 to 72.5, a miss | review, post hoc `simphase` | the audit's own prediction record |
| **Run-cost estimates.** L1b: 1 to 2 hours estimated, 4 minutes observed. FMnull `analytic`: under 1 minute and 300 MB estimated, 11 min 26 s observed | the runs | nobody |
| **Unreachable Day-side outcomes.** L5: half of the DAY band (expected count at least 3 at s = 0.003 and 0.01) was excluded by the registration's own arithmetic. FMnull: criterion S2 cannot fire for any planted model off the window grid. L1c: the amended Day-side clause "x <= 3" could not be met even in the synthetic cell built to let the mechanism work | L5: the severe-testing pass (ST-09), before launch. FMnull: the Day-side review. L1c: the post-run reviews | critics in all three (a Day-side outcome that could not occur). "Not DAY" and "S2 unmet" are not counted against Day |
| **Claim-text figures "5.7" and "4.8".** Claim C said "5.7 expected panel-site events" and claim C1 "4.8 events", from uniform scaling. The L5 model puts 1,376 to 3,836 swept standing-variant sites on the panel. Both were low by about two orders and had stood since before this batch | L5 review | critics: they overstated what the panel hides |
| **L1b, missed prediction A4.** The audit predicted that a naive position-by-position extraction (arm X1) would read 0.28 to 0.60. It read **0.853** | the run | critics: L1's inference that the mispairing sits "in most genes" is withdrawn for the pooled value; 13.7% of genes are enough |
| **HF `ph`, missed predictions.** PC-1 (b): 1.6 substitutions per generation not sustained on the rule at the 20k horizon. PM5: the mean field overstates the limit at R = 2. PN3: the audit predicted a backlog at 1.6 for genotypic share 0.1, and 1.6 was sustained | the run | PC-1 (b) and PM5 had favoured the critic-side reading; PN3 had favoured Day's |
| **FMnull, missed prediction P8 (i).** Hand estimate: a block model doubling the human rate over 2% of the genome gives an index above 10. It gives 5.06 on the grid and 4.27 at random phase | the run, `simphase` | the miss shows a limit on Day's side: a mechanism of that size is not flagged by the check |
| **L1c, registered protein-guided arms invalid as written.** They translated the ungapped chimp string in frame 0, so the frame is lost after any indel that is not a multiple of 3 (1,173 genes, 6.1%). Frame-aware arms were added by amendment before any L1b or L1c data | pre-run design review (BLOCKER-1) | mixed: four registered critic-side predictions fail on the invalid arm and hold on the valid one |

Smaller items, in the write-ups: L5 printed "more than 15 orders of magnitude" as a margin (it was not one; withdrawn) and credited Day with a "240 to 670 times" figure as a test of C1a's sign (withdrawn; the sign is untested). The lead's first `ph` text dropped a Day-side clause, scored a 4-of-8 tie without a flag, used the smallest available ratio as the headline and said "near Haldane's" where that holds at one R only; the combined review corrected all four. L1c's first write-up gave three wrong numbers (left-out share 1.6% for 1.40%; kappa margin 0.02 for 0.015; pN needed 0.58 for 0.67). L1b's first write-up proposed to narrow a registered sentence after the result; withdrawn.

## L1b: the dN/dS rerun on the T2T assemblies
Write-up: [`R4-L1b.md`](../research/checks/results/R4-L1b.md). Milestone 13 left one route open for Day's 0.80: a complete extraction on the assemblies he names. L1b runs it: GENCODE v35 lifted to hs1, chimp mPanTro3, the Cactus alignment, the same estimator as L1.

| Gene set (bases paired by alignment column) | Pooled dN/dS |
|---|---|
| All genes (19,310) | **0.271** |
| Ensembl one2one | 0.238 (0.208 with CSAC-like quality filters) |
| Syntenic | 0.209 |
| Non-one2one | 0.459 |
| Every chimp-row choice, all genes | 0.246 to 0.293 |
| All 32 filter stacks, all genes | 0.214 to 0.283 |

- **Band CRITIC by the registered rule.** Day's Q175 says "No combination of quality filters moves the number below 0.65."; every stack is below it. For the non-one2one genes to carry 0.80 they would need a ratio of 3.95; the 1,090 genes not in this set about 10.
- **A gene-set effect exists in Day's direction on T2T too:** all genes over one2one +0.033 (+14%), +30% over the CSAC-like set, +3% among syntenic genes (L1 on hg38: +31%). Day's own later table (Q184) shows +0.003.
- **Credited to Day:** he named testable assemblies; his 98.8% completeness is reproduced (98.87% of CDS bases); his near-empty strict stack (10 genes) is reproduced (9 genes) under the literal reading of his stop filter.
- **The surprise (credited to neither side).** A naive position-by-position extraction of the first chimp row reads **0.853** pooled. It is carried by 13.7% of genes; the other 86% read about 0.205. First cause of the excess: an in-frame indel 55.7%, a coverage hole 28.8%, a frame-changing indel 8.4%, an exon edge 7.1%. Wording of record: "a candidate error class with a real-data instance". The registered band LOCATED is **not licensed**: the arm missed the registered share test (60.1% against 66%). Day's pipeline has not been seen.
- **Predictions.** Day-side 1 of 5 parts; critic-side 6 of 6; audit 11 of 12 parts, the miss being A4. These are predictions the audit wrote for each side, the critic bands with L1's values already in hand; rows are not independent and the counts are not error rates (MA-06). Day's post of 2026-10-12 also changed his position: under it his one hit becomes a miss and one miss is no longer his prediction.
- **Readings of DN1 (rule RD).** (A) 0.80 is a property of the genomes: `contradicted` on this alignment and annotation; sets the field. (B) 0.80 is a report of what an ungapped comparison yields: reproduced in kind by X1, identity with his pipeline `untestable` until code or table is released. (C) the value depends on the alignment method: L1c. The write-up says the choice of A over B is arguable.
- **Not tested:** GENCODE v46 (Day's stated annotation) on hs1; the 1.16% of codons the column pairing leaves out (129,092; bounded here only to 0.56 to 0.85); any second aligner. L1 and L1b share one counting code, so the wording is "contradicted for an alignment-column extraction on two assembly and alignment pairs, one estimator".

## L1c: does the alignment method produce the low value?
Write-up: [`R4-L1c.md`](../research/checks/results/R4-L1c.md). Day's post of 2026-10-12 says the gap between 0.80 and 0.23 "is a methodological artifact of using a conservation-dependent alignment to measure conservation." (Q186), by this mechanism: "Regions too divergent to score well get gapped out or are left unaligned, so they aren't counted." (Q181).

- **Fidelity, from the held source and not from the run.** Day writes: "So what the Consortium’s method actually measured is: “among the coding positions conserved enough to survive protein alignment, how conserved are they?”" (Q274). The held CSAC 2005 Methods say the 13,454-gene set was aligned through the BLASTZ genome alignment; Clustal W was used only for a 7,043-gene subset. On that reading the source is `misread`.
- **The low value needs no protein step on these data.** The plain extraction on 12,724 genes of the real 2005 list reads 0.219 with a nonsynonymous fraction of 42.6%, against the 0.2300 and "~40%" of Day's own "Published" row (Q184). Like for like at CSAC's site ratio the value is about 0.265.
- **Size of the mechanism.** The audit's realistic protein-guided arms lower pooled dN/dS by **2.3% to 5.8%** on all genes and 1.3% to 3.7% on the real list. The claim needs 71%.
- **Direction is Day's in every arm.** Dropped codons are nonsynonymous-enriched (0.71 to 0.85 against 0.479), as Q182 says. A deliberately strict stress arm (PAF2) lowers the estimate by about a third. No pipeline is shown to use such a rule.
- **Synthetic table.** Realistic arms return the truth at moderate clustering. With near-total replacement of 15-residue runs, a lenient trim and the Gblocks rule read 55% to 65% low: the mechanism exists in principle. A register-broken extraction reads 0.81 to 0.83 at a truth of 0.22.
- **Site model.** 0.271 becomes 0.385 with transition-aware sites. That moves the audit's headline more than any alignment arm does and does not approach 0.80.
- **Band CRITIC** on the registered and the amended rule, both source sets.
- **Predictions.** Day-side: 4 hits (1 not blind), 1 empty, 9 misses. Critic-side: 14 hits (1 near automatic), 1 miss; 4 more name the invalid registered arm and fail there. Audit: 12 hits, 5 misses, 1 split. Several rows restate what L1b had already fixed; limited to what L1c added, Day-side 2 hits, 1 empty, 4 misses and critic-side 11 hits, 1 miss, 4 on the invalid arm. The same caution applies: the audit wrote both sides' predictions and the counts are not error rates.
- **Readings of DN6 (rule RD).** a: `misread` (sets fidelity). a-broad (any selection on alignment quality): `partial` or `unverifiable`. b1 (the published 0.23 is this artefact): `contradicted`. b2 (mechanism and direction, no size): `contested` (sets external). d (the genome alignment that feeds the audit's own extraction is itself the filter): extended, **not tested**.
- **How the `contested` was reached, stated for Day's side.** The registered rule would have scored the mechanism reading `supported` once a valid strict arm stood in for the invalid one. The audit amended the rule before the real data, after a miniature had shown that outcome. The amended reading has two outcomes only and cannot come out `contradicted`; the registered one could not come out other than `supported`. Neither could fail in both directions.
- **Not tested.** No external codon aligner (MACSE, PRANK) and no independent chimp CDS annotation: every protein arm re-pairs codons Cactus had already paired, with the audit's own in-script aligner. No arm sees the 1.40% of codons Cactus does not align (concentrated in 351 genes). They cannot carry 0.80 unless they read like unrelated sequence (pN 0.67 needed); a rise of the order of 10% is open. DN6 is not to move past `contested` until an external aligner has been run.

## FMnull: a neutral null for "more than 80 times more variable"
Write-up: [`R4-FMnull.md`](../research/checks/results/R4-FMnull.md). Target, Q164: "The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts." Day has released no window size, statistic, lineage unit, masking rule or code, so his number cannot be given one class. The check builds a lookup table (window size by divergence, under eight parameter sets) and asks where the held alignment itself shows an index near 80.

- **Day's sentence is true of the data.** Read as variance over mean (R1, the reading "overdispersed" names), "more than 80" holds at windows of 1 Mb and above in all ten lineage-by-masking cells. Repeat-masked single-copy sequence at 1 Mb: human 89.4, chimpanzee 89.5, bonobo 88.3, gorilla 85.1, unpolarised human-chimp differences 253.
- **It is as true of the other apes as of human.** The human-to-chimp ratio of the index is 0.97 to 1.04 from 1 kb to 3 Mb. No parameter enters this comparison.
- **Where it is true it is not anomalous.** In the cells at 1 Mb and below where the index is 80 or more, the measured index is 0.11 to 0.91 of the neutral upper bound under all eight sets. No measured cell is above three times any upper bound at any window from 1 kb to 10 Mb. Pedigree de novo mutation data alone reach the measured 1-Mb dispersion.
- **The null does not absorb everything.** A planted dominant one-lineage block mechanism scores DAY at 100 kb on masked sequence; the data are 22 to 31 times below it at matched exposure.
- **The check has little power.** Every non-dominant planted block scenario, down to a doubling of the human rate over 2% of the genome, scores CRITIC or MARGINAL-IN. No Day-side criterion could have been met by a mechanism smaller than the dominant one, and criterion S2 not even by that one off the window grid. The outcome observed (no DAY) is the weakly tested one (ST-10).
- **Against the critic-side reading.** Six cells at 3 to 10 Mb are above the upper bound under four of the parameter variants (1.07 to 1.47 times; none DAY). On single-copy sequence the human-chimp index is above one bound at 1 to 10 kb; a lineage-specific mutational share of 0.04 to 0.07 absorbs it. Most parameter brackets are unsourced, and the parameter sets that survive the data at the low edge are the wide ones.
- **Untested.** At windows of 10 kb and below, 80 as a number would exceed every band, but the index measured there on alignable sequence is 1.4 to 10.4 for single lineages. Day stated no window, so this is an extended reading: `unverifiable` (rule F). A reading as a ratio of standard deviations (R2, the audit's addition) is true in no measured cell. Only sequence alignable to hg38 and orangutan is measured (about 86% of autosomal 1-kb bins).
- **Predictions.** The "Day side" and "critic side" expectations inside P1 to P8 are audit gloss, not statements of Day or of any critic, so no side is scored. Of the audit's own: P1, P2, P3 (main clause) and P6 hit; P7 two parts hit and one depends on how its own wording is read; P8 (i) missed, (ii) hit only on the grid; P4 and P5 earn no credit.
- **Result.** Neither registered clause is met. **No verdict move.** FM3 external stays `supported` as a description, non-discriminating (reading-dependent, R1 sets the field). FM10 external stays `contested` and internal `pending`; no defeater against FM10 is licensed.

## L5: could Day's ancient-DNA test have seen his required rate?
Write-up: [`R4-L5.md`](../research/checks/results/R4-L5.md). Day compares a required "approximately 15,500 fixations per 7,000-year period" (Q275) with an observed zero (Q53, Q55) and concludes: "This result decisively favors the MITTENS prediction over the Modern Synthesis expectation." (Q276). L5 simulates his sampling, his statistics and the 1240k panel, and asks how many events each model expects. The required rate is taken at face value: 15,556 completions in the window, no panel scaling.

| Selection strength of the required completions | Expected count of his zero statistics | What the zero says |
|---|---|---|
| s <= 0.01 (registered scope; descriptively the same at 0.02) | effectively 0; no simulated sweep registers | nothing about the rate: zero is what the required rate itself predicts |
| s = 0.03 | median 0.099 (new mutations), 3.08 (standing variants); 9.7 to 57 at Day's 20-year generation | the edge |
| s >= 0.05 | medians 286 to 3,924 on the blog statistic | zero excludes the required rate (P(0) below 1e-69) |
| Mainstream model | at most 4.7e-31 | zero is expected |

- **The low-s result is arithmetic, not simulation.** A sweep at s <= 0.01 takes about 1,000 generations; the window is 280. The simulation resolves only 24 to 184 events per cell, so "at most 1" rests on that arithmetic and on a post hoc trajectory bound. s = 1e-3 is the only beneficial s in Day's held corpus (Q44, a different post).
- **Why the power is zero at low s: the window, not the panel.** No simulated completion at s <= 0.02 began below 50% at 7,500 BP. The panel does not hide strong sweeps: linked panel SNPs carry them, and the swept site itself is on the panel in 8.8% to 24.7% of standing-variant completions.
- **For Day:** the observation stands, and every model reproduces it. At strong selection his zero does what he says: it excludes any rescue of the required rate by strong sweeps. No critic claim in the corpus invokes such a rescue. Two of his statistics (Z50, Z10) are understated by the model at strong selection, by an unsized factor, against him.
- **For the critics:** at the selection strengths anyone has attached to these fixations, the zero carries no information on the rate. "7,000 years is too short" is the operative mechanism.
- **Band CRITIC.** The test could not have come out DAY at s <= 0.01 (registered arithmetic), so "not DAY" says nothing against him.
- **Predictions.** Day-side band 0 of 1, critic-side band 1 of 1; of the audit's eight, two hit in full and six missed at least in part. Two misses (P4, P5) mean the audit expected the panel to hide more than it does; two (P3b, P7b) mean it expected power to begin at lower s. Written by the audit; not error rates.
- **Readings of claim C (rule RD).** R-a (s = 1e-3, imported from Q44) and R-b (any s <= 1e-2): `contradicted`, scoped to the inference from zero to a refuted rate. **R-c (the source states no s): `contested`; sets the field.** R-d (s >= 0.05): `supported`, scoped; extended, since no source gives it. R-e (total substitutions, no mechanism): the existing internal `non-sequitur`.
- **Unresolved:** which selection strength Day's argument implies. Also open: the sign Day asserts in C1a (no unascertained comparator was computed); which of his three statistics is primary; the size of the Z50 and Z10 understatement; sweep independence at 15,556 strong sweeps (about 28,000 would be in flight at once); the second panel design is only a partial sensitivity.

## HF: the H follow-ups, final
Write-up: [`R4-HF.md`](../research/checks/results/R4-HF.md). Milestone 13 listed HF as not final, pending the post hoc run `ph`. `ph` is done: 410 jobs, 454.8 CPU-hours, 209 jobs run on two hosts with 0 mismatches. By its own docstring every `ph` prediction was written after the main run had been seen, so it can neither rescue nor sink a pre-registered score.

| Selection regime (in-model) | Sustainable substitution rate |
|---|---|
| Hard selection | the hard cap reproduces; Haldane's 1/300 is conservative at R = 1.111 for every population size tested |
| 30% hard (h = 0.3) | about 1.3 to 1.7 times the hard cap at the same R; 0.83 and 1.05 times Day's Term 3 |
| 10% hard (h = 0.1) | about 2.6 to 3.5 times at R = 1.111 (marginal: a 4-of-8 tie on eight runs); about 3.5 times at R = 2 (sharp) |
| Purely relative fitness, or truncation holding N = K | at least 0.8 to 1.6 per generation at R >= 1.111 (at least 217 times the hard cap); the population cannot go extinct in this model |
| Truncation on a noisy phenotype | 1.6 per generation kept down to a genotypic share of 0.1 (the limit tested) |

- **For Day:** a modest hard component restores a limit near the hard cap, and Term 3 holds as a rate bound in-model when 30% of selection is hard. In no soft or truncation arm is the cost per substitution reduced; it is not charged, and under noisy truncation it rises about six-fold (18.3, 31.1, 114.7 against about 16). Sweep residence time grows with the number of concurrent sweeps. On the Drift Deathmarch, selection alone lowers the harmful count 4.5 times.
- **For the critics:** the soft-selection "failures" in the main run were a fill lag (80 of 80 long-burn runs pass), with no population-size effect up to 1.6 per generation at R = 1.111. Ten per cent hardness leaves a few-fold above the cap. Truncation keeps its rate when the phenotype is mostly noise. Quadratic synergy against an absolute optimum lowers the rate.
- **Predictions in `ph` (all post hoc):** Day-side 1 of 4, critic-side 3 of 3 (one on the tie), audit 10 of 15. Written by the audit; not error rates.
- **What it turns on.** The hardness h and the reproductive excess R. **Neither has a source for humans.** Every row above is a statement about the model.
- **Verdicts:** H, H8 and H5 external stay `contested`; the h-scope text and the latency-against-throughput caveat are now in the claim files.
- **Not run:** the long burn at 0.8 and 1.6 for R = 1.05; more runs at the h = 0.1 tie; a synergy arm under relative fitness; a density-compensating arm.

## Integrated earlier and not yet posted (2026-10-11 and 2026-10-12)
These were integrated after milestone 13 and had no post. Detail is in `research/checks/RESULTS.md` and [`criticality/README.md`](research/criticality/README.md).

- **B9** (Q104: "the human species would have been rendered infertile and gone extinct within centuries"; review #61). Under fully relaxed selection, fitness halves in 338 to 3,457 years on Lynch's published declines; Day's own premise 2 gives 12 to 970 years; the literal reading (harmful substitutions fixing like neutral ones) gives 1.0 to 1.6 million years. External `contradicted`, scoped: premises 1 and 2 as worded are false; the conditional's arithmetic is supported. Internal reading-dependent: `holds` on the mutation-load reading, `non-sequitur` on the literal one. For Day: his worry is a mainstream mutation-load concern. For critics: the antecedent never obtains.
- **RH closeness tests** (reviews #62, #63). The owner's test for whether a statement is dialectic or rhetoric ("remotely close", 3x band, all readings reported) was run on Day's C7 and Hard Limits peroration and, symmetrically, on Hancock, Myers and Mansfield. Tags are reading-dependent on both sides. B internal moved `pending` to `non-sequitur`. No critic node verdict changed; Myers's "sequential" description of MITTENS 3.0 went to the slip ledger.
- **A2e-alpha, Uricchio 2019 full text** (review #64). Human-lineage, bias-corrected alpha 0.135 (HPD 0.096 to 0.17): 798 on the most Day-charitable row, 4.2 times the 191 threshold. **A2e external moved to `contradicted`, scoped** to the per-generation count of adaptive fixations of any effect size; strong-only (lower HPD 0) and fitness-weighted readings stay `contested`. It is a model inference; 72% of the estimate is weak selection.
- **GAP05** (review #65). A sourced coding DFE gives about 15,000 to 21,000 slightly deleterious fixations per lineage and a log-fitness decline of 0.29 to 0.43 on the pre-registered base (about 0.8 to 1.1 on a post hoc calibrated base, against ln 3 = 1.10). For Day: the premise is supported. For critics: no pre-registered row reaches ln 3, and the DFE reproduces dN/dS with no fitted parameter.
- **Rules RD and RH6** (owner, 2026-10-11). Where a verdict depends on the reading, every plausible reading is recorded; the field takes the reading under which the quoted statement is most defensible, not the one with the best verdict for the speaker.
- **Refresh of 2026-10-12.** Day's "The Method is the Conclusion" (Q180 to Q186) created claim DN6. The CSAC 2005 text was obtained: DN5 fidelity `pending` to `accurate`, DN3 fidelity `pending` to `partial`.
- **Six criticality passes (2026-10-12).** The audit was examined by a method audit (MA-01 to MA-20), Day's own Triveritas system, AMSTAR 2 and ROBIS, a severe-testing pass, an argument-structure pass and a GRADE-style certainty pass. No verdict, rule or claim changed. All six found no independence (one model family wrote, reviewed and audited). Five found external verdicts worded beyond their evidence and rules fixed with results in view. The audit cannot yet state a conclusion about Day's root claim or his critics' positive thesis, nor an error rate for either side.

## The method audit of this batch (MA-21 to MA-30)
File: [`METHOD-AUDIT-2026-10-13.md`](research/criticality/METHOD-AUDIT-2026-10-13.md). It was written by a fresh instance of the same model, briefed by the lead; it is not independent. Ten findings: 4 MAJOR, 5 MINOR, 1 COSMETIC.

**The four MAJOR findings.**
1. **The lead is author, briefer and judge (MA-21).** One instance wrote the `ph` scoring, the pre-run notes, both launch fixes and every ruling between the Day-side and critic-side reviews, and briefed each reviewer with its own suspicions. The briefs are not in the repository. Rulings reached the claim files 4 to 8 minutes after each fix pass.
2. **"Extended reading" and "registered wording governs" are applied case by case (MA-22).** Rule RD says extended readings cannot set a verdict field and gives no test for "extended". Four fields rest on such calls: DN1 external, DN6 external, DN6 fidelity, C external. Their direction is mixed (two harsher for Day, three milder, one milder for a critic claim), and they are not reproducible from the rule text.
3. **One review for a check carrying a registered flip (MA-23).** L5 registered three reviews and a verdict flip; one combined review was done. It found 7 MAJOR and 10 MINOR. The flip was withheld, so no verdict value rests on it.
4. **Day-side outcomes were unreachable in parts of three of the four new checks (MA-24).**

| Check | Could a Day-side outcome have occurred? |
|---|---|
| L1b | Yes. His value on his named assemblies would have given DAY; LOCATED missed by 5.9 points of share |
| L1c | Partly. The DAY band was reachable in principle; the amended mechanism reading could not come out `contradicted` and the registered one only `supported`; the "x <= 3" clause was unreachable |
| FMnull | Only for a dominant mechanism at 100 kb on masked sequence |
| L5 | No at s <= 0.01; yes at s >= 0.03 |
| HF `ph` | n/a (post hoc) |

**Symmetry tally.** Of 24 conflicts between the two steelman reviews, 5 rulings went to the Day-side reviewer, 5 to the critic-side reviewer and 14 were split. Of the errors listed above, by the method audit's own loose count, five leaned to the critics before being caught, one to Day, three were mixed and four leaned to neither.

**Sound, by the same file.** Registration order holds for all four checks against the host records. No verdict was moved on a weak test. The reviews reversed the lead in both directions.

**Smaller findings.** The `blind` pre-registration label overstates L1c, FMnull and L5, and `ph` has no row (MA-25). One agent wrote both L1c steelman reviews (MA-26). A reading fixed before a run was wrong (MA-27). Two small drifts between write-up and claim file (MA-28). Side tallies printed without saying the audit wrote them (MA-29; this post says so each time). Three subagents ran at once against a cap of two (MA-30).

**Closed:** MA-12, ST-08, ST-09. **Held back, not applied:** proposal (l), a fairer Day-side criterion for FM10; proposal (m), an operational test for "extended reading".

**Open owner decisions** (`docs/research/DECISIONS.md`): O-24 the subagent cap; O-25 the review tier when a check proposes a verdict flip; O-26 who rules conflicts between steelman reviews, and whether briefs may name suspected issues; O-27 whether to take up proposal (l).

## Refresh (2026-10-13)
File: [`refresh-2026-10-13.md`](research/sources/refresh-2026-10-13.md), checked about 18:55 to 19:40 UTC.

- **Day has released nothing new on method:** no per-gene table (Q176), gene list, code, window size, statistic or coordinates, for dN/dS or for "The Fourth Mechanism".
- **Four new Day posts** tagged evolution, none with new dN/dS or FM data. One, under the name "Claude Athos", says "The entire internet has been the reviewer. The result is zero successful challenges." (Q282; tagged rhetoric, not fact-checked) and gives a new headline figure: "The corrected figure for modern humans: a fixation probability of approximately 10^(−78,000,000)." (Q284; not checked against the paper). Another describes his compute: "And twin 96-core 512GB digital abacuses." (Q285).
- **One Zenodo record silently revised.** Record 22903977 was retitled and its file replaced on 2026-10-13; the new PDF adds a closed-form completion fraction (Q286) that needs its own check. The other 38 records are unchanged.
- **A critic video.** Gutsick Gibbon posted "Six Scientists Roast One Racist Loser (Heartwarming) (Four Hours) (Hopecore)", 4:14:03, on 2026-10-13. The title is rhetoric about the person and is not scored. **Not reviewed:** no captions existed at fetch time, so whether it addresses the dN/dS posts or FM is unknown. Day announced it and wrote: "I’ll respond to the substantive matters in writing, as I always do." (Q281).
- **Written critic replies:** none found on the Substack archives and Bluesky as of 19:30 UTC.
- **Not checked this pass:** Reddit, Peaceful Science, Camestros Felapton and Pharyngula were not re-walked; X, Gab, Telegram, Rumble, Locals and UATV are inaccessible; the video's comments were not harvested.

## Verdict changes
**Today (2026-10-13).** Each row is a field whose value or governing reading changed.

| Claim, field | Before | After | Check |
|---|---|---|---|
| DN6 external | pending | **contested**, reading-dependent (b2 sets the field; b1 `contradicted`; d not tested) | L1c |
| DN6 fidelity | pending | **misread**, reading-dependent (reading a; broad reading `partial` / `unverifiable`); licensed by the held CSAC text, not by the run | L1c |
| DN1 external | contradicted, conditional on L1b | contradicted, now reading-dependent (A sets the field; B `untestable`; C is DN6); condition discharged for this alignment and annotation | L1b |
| DN2, DN3 external | contradicted, conditional on L1b | contradicted; condition discharged; DN3 extended to the alignment-level version | L1b |
| C external | contested | contested, now reading-dependent (R-c sets the field; `contradicted` scoped under R-a, R-b; R-d extended) | L5 |
| FM3 external | supported (as a description) | supported, now reading-dependent (R1 sets the field): as a description, non-discriminating | FMnull |
| H, H8, H5 external | contested | contested; h-scope text added | HF |

**Since milestone 13, before today.**

| Claim, field | Before | After | Source |
|---|---|---|---|
| A2e external | contested, leaning contradicted | **contradicted**, scoped to the any-effect-size count | Uricchio addendum |
| B9 internal / external | non-sequitur / pending | **holds** on reading A (field), non-sequitur on reading B / **contradicted**, scoped | B9 |
| B internal | pending | **non-sequitur**, reading-dependent (`holds` scoped to B2 recorded alongside) | RHclose, rule RD |
| C7 | non-sequitur / contradicted | values unchanged; reading-dependent | RHclose |
| DN5 fidelity | pending | **accurate** | CSAC 2005 text |
| DN3 fidelity | pending | **partial** | CSAC 2005 text |
| DN6 | new (2026-10-12) | pending / pending / pending until today | refresh |

**Candidates that did not move, and why.**
- **C external to `contradicted`** (registered for band CRITIC): withheld. The run did not test the move, and reading R-c is unresolved.
- **DN1, naming the error class as located:** the registered share test missed (60.1% against 66%).
- **DN6 external to `contradicted`** (reading b1): the registered move sentence licenses `contested` for a real direction of insufficient size; b1 is recorded. **To `supported`:** the registered reading has no valid arm under it.
- **DN2 re-opened:** needed a minimum of 0.60 over the filter stacks; observed 0.214. **DN3 to `supported`:** needed a gap of +0.40; observed +0.033.
- **FM10 external, and a defeater against FM10:** neither registered clause was met. FM10 internal stays `pending` by owner decision until Day releases his method.
- **C1 external to `contested`** for the wider reading (ascertainment is why the test saw nothing): recorded as a reading; the field keeps the reading as written. **C1a:** its sign was not tested.
- **H, H8, H5:** the answer turns on h and R, which are unsourced.
- **Drift Deathmarch and HO-11 statements:** proposed verdicts exist in the HF write-up; no claim files exist, so none is applied.

Totals as carried in `docs/HANDOFF.md` at `20bcecf`: internal 131 hold, 19 non-sequitur, 2 arithmetic error, 52 pending; fidelity 44 accurate, 39 partial, 11 misread, 58 unverifiable, 10 pending; external 34 supported, 115 contested, 18 contradicted, 6 untestable, 48 pending. Six claims carry a reading-dependent verdict.

## Who this helps
| Result | Helps Day | Helps the critics |
|---|---|---|
| L1b | His assemblies were testable because he named them; the gene-set effect has his sign on T2T (+14%); his completeness figure and near-empty strict stack reproduce; a simple extraction reads 0.85 on his data, so his number is reproducible in kind, which the audit did not expect | Column-paired dN/dS is 0.25 to 0.29 on the assemblies he names; no filter stack exceeds 0.283; the published 0.23 reproduces in kind a second time; the complete-extraction route is closed for this alignment |
| L1c | Q182 is right in direction in every arm; a strict filter lowers the estimate by a third; the mechanism is large on synthetic near-total replacement; the rule was amended against his reading before the data; no external aligner was run; 1.40% of codons are seen by no arm | The published 0.23 did not come from a protein-guided alignment; the low value needs no protein step; the realistic effect is 2% to 6% against 71% needed |
| FMnull | His sentence is true of the data at 1 Mb and above; the check has little power below a dominant mechanism; no Day-side criterion could fire for a smaller one; most brackets are unsourced | Where the sentence is true it is inside the neutral band; it is as true of chimpanzee, bonobo and gorilla; pedigree mutation data alone reach the 1-Mb dispersion; the data are 22 to 31 times below the dominant model |
| L5 | His observation stands; at s >= 0.05 his zero excludes the required rate; the panel does not hide strong sweeps; the test could not have come out for him at low s; two of his statistics are understated at strong selection | At s <= 0.01, his own 1e-3 included, the zero carries no information on the rate; the mainstream model expects zero; the 7,000-year window is too short |
| HF | A 30% hard component restores a limit near the hard cap; Term 3 holds there; the cost is never reduced, only not charged | The soft-selection failures were a fill lag; 10% hardness leaves a few-fold; truncation survives a mostly-noise phenotype |
| Earlier items | B9: his worry is a mainstream mutation-load concern, and "centuries" holds on Lynch's upper value. GAP05: his premise is supported. A2e: a model inference, strong-only not interval-secure | B9: the antecedent never obtains. GAP05: no pre-registered row reaches ln 3. A2e: a second full-text estimate 4.2 times above the threshold |

**Both / the audit's own errors.** The X1 result (0.853) is the audit's missed prediction and is credited to neither side. So are the reading added by the audit to FMnull (R2), the unmasked FMnull cells (a reference-projection effect), and every item in the corrections table. Before being caught, more of those errors leaned to the critics than to Day; all were found by the audit's own reviews, and the count is small.

Reading across the table: the numbers that carry Day's dN/dS conclusion (0.80, and the alignment artefact as its explanation) were not reproduced by any column-paired extraction or realistic alignment arm tried here, and his descriptive statements (overdispersion above 80, the zero in ancient DNA, completeness) are granted. What the batch did not do is test his pipeline, his window, or a mechanism smaller than the largest one.

## What stays uncertain
- **Where Day's 0.80 comes from.** Register loss is a candidate error class. His pipeline and per-gene table are unseen.
- **The aligner question.** No external codon-aware aligner from an independent chimp CDS has been run; reading d of DN6 is untested.
- **Day's window and statistic for "80 times".** Unreleased. Small one-lineage block mechanisms are not excluded by FMnull.
- **Which selection strength Day's ancient-DNA argument implies,** and the sign in C1a.
- **h and R for humans.** No source.
- **The content of the critic video**, and any written reply Day makes to it.
- **The four reading choices of MA-22** and the owner decisions O-24 to O-27.
- **Independence.** No outside or non-Claude reviewer has seen any of this.
- Carried from milestone 13: DN5's independent ML estimate; E10's Good 2017 SI 5.2; the chrX 57.3 Mb window; the B3m 2-versus-25 gap; XT's unexplained deficit.

## Next
- Review the critic video when captions exist; score valid points and errors with equal weight. Track Day's written reply (Q281).
- L1c follow-up: an external codon-aware aligner on the 351 worst-covered genes and the 2,765 genes with indels or holes; a dose-response between the lenient and strict filters; a registered rule for Q183.
- L1b follow-up: GENCODE v46 on hs1.
- L5 follow-ups: a random-SNP comparator for C1a's sign; sizing the Z50 and Z10 understatement.
- L2: source the hardness h from public data. HF long burns at R = 1.05 and the h = 0.1 tie.
- New from the refresh: check the closed-form F(T) in the revised Zenodo record; check Q283 against the versions ledger.
- Integrator fixes listed by the method audit: done the same day in `0bb9070` (pre-registration table regenerated with a row for HF `ph`; claim C's scope wording; DN1's superseded sentence; the note that one agent wrote both L1c steelmen). Still open: the DN1 side-tally gloss (MA-29), the HF `ph` push order, which is not shown to the second, and whether reviewer briefs go in git (O-26).
- Stage R5 begins when the load-bearing claims without a reviewed check are resolved.

```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
