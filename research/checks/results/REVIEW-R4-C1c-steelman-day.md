# Review of R4-C1c: Day-side steelman

Reviewer role: argue for Day as strongly as honesty allows, then judge fairness. Target: `results/R4-C1c.md` (line numbers below refer to it), `research/checks/c1c_call_depth_replacement.py`, `results/raw/c1c_analysis.txt`, `raw/c1c_posthoc_mindepth.out`, claims C, C1a, C2, C4, C5a, C5b, C6, C7, quotes Q96. Day's text was read from `sources/raw/day/zenodo-18525185.txt` and `zenodo-23046531.txt` (read only). Nothing else was edited and nothing was committed. I ran no new simulations; every number below comes from the existing outputs, and the re-derivations I did are simple ratios of table entries.

## Verdict in brief

The check is mostly fair to Day on the narrow question it was built for, and it is honest about its own failures: 3 of 8 pre-registered predictions failed (P4, P6, P7), and P3 was refuted once an error rate was added. It does not blame Day for the non-reproduction of his table: §6 says "The model is still not a valid null for Day's table" and §7 says "a different implementation of his statistic ... is not excluded".

The weakness is §7 (the "who this helps" section), above all the critic bullets at lines 88-89. These put weight on cells that the check's own validity tests reject, and they leave out three results from the same data that favour Day. The headline "the 21 corresponds to neutral only if Ne >= 1e5" is true of the homogeneous-capture grid but not of the capture-matched grid. The strongest Day-side case is below, followed by the numbered findings.

## The strongest honest Day-side case

1. **The deficit survives every lever the check pulled.** Replacement, capture heterogeneity, the error rate and a shorter generation time all push the model S21 up, never down. Only a larger Ne pushes it down (see F1, F4).
2. **The "escape" cells fail tests that matter.** The R0 Ne 1e5-3e5 cells (S21 8-32) have eligible 0.9-1.7k against 22,428, a profile distance of 0.68-0.72, and a tracked fraction of 1.00 against 0.727. Once heterogeneity is added to match the tracked fraction, S21 is 0.8-1.7k at Ne 1e5-1e6 (F1).
3. **The summary statistics disagree about Ne.** The textbook-Ne cell with replacement and an error rate (R2, Ne 1e4, eps 1e-3) matches Day's eligible count and his start-frequency table. The escape cells match only the tail (F2).
4. **The "Ne >= 1e5" escape is not supported by anything either side cites.** The only Holocene temporal Ne in the repo is the critics' own 8-10k (F5).
5. **Stasis is Day's stated model, and the check never tested it** (F6).

## Findings

### F1 (MAJOR) The "consistent" cells assume homogeneous capture, which Day's own tracked fraction contradicts, and §7 does not say so

R4 line 70-71 (§5): "**Consistent:** closed or mildly replaced population (R0, R1) with Ne ~1e5-3e5 (S21 8-32), or R2 at Ne >= 3e5 ... homogeneous capture and no assay error."

R4 line 98 (§8): "my tracked = at least one call per bin (0.95-1.00 vs his 0.727)".

The base model gives a tracked fraction of 1.00 in every cell. Day's is 0.727, so homogeneous capture is already falsified by the data the check compares against. Capture heterogeneity is the largest lever the check found (line 51). When it is tuned to reproduce Day's tracked fraction, the post hoc output `raw/c1c_posthoc_mindepth.out` gives:

| cell | kappa | m | tracked | S21 |
|---|---|---|---|---|
| R0 Ne 1e5 | 1.0 | 20 | 0.80 | 1,064 |
| R0 Ne 1e5 | 0.5 | 20 | 0.75 | 1,667 |
| R2 Ne 1e5 | 0.5 | 20 | 0.73 | 1,400 |
| R2 Ne 1e6 | 1.0 | 20 | 0.78 | 843 |

These are 40-80 times the 21 at the same Ne values where the homogeneous base grid said "consistent". R4 line 51 does state "Day's tracked fraction can therefore be reproduced, but only with S21 in the thousands". But the sentence is in §3, and the §5 "Consistent" bullet, the §7 critic bullet at line 88 ("~20-30 post-5000 BP events at Ne ~1e5 with no clock failure") and the headline do not carry it through.

Qualifications, so this is not overstated:
- Gamma(kappa) heterogeneity is a convenient shape, not measured missingness.
- The m = 20 threshold is a post hoc, single-replicate device that fits one free parameter to one number.
- No Ne above 1e6 and no growth cell was run with heterogeneity, so the Ne at which S21 = 21 under matched tracking is unknown. It is above 1e6 for R2 and probably above 1e6 for R0, but that is an extrapolation.

Fix:
- Add a two-row table to §5 and §7: S21 by Ne under homogeneous capture, and under capture matched to 0.727.
- State in the headline that "Ne* = 1.4e5" is conditional on a tracked fraction the data reject.
- Rerun the matched-tracking variant with all 4 replicates, and at Ne 3e5, 1e6 and the growth cells.

### F2 (MAJOR) The textbook-Ne cell with an error rate matches two of Day's summary statistics, and R4 reports only the cells that match the other two

`raw/c1c_analysis.txt` Table 5, row R2 Ne 1e4 e1e-3:

| quantity | Day | R2 Ne 1e4, eps 1e-3 | R0 Ne 1e5, eps 1e-3 (a "PASS" cell) |
|---|---|---|---|
| eligible | 22,428 | 20,359 | 45,340 |
| start % [99,100) / [95,99) / [90,95) / <90 | 79.2 / 20.2 / 0.5 / 0.2 | 81.7 / 17.8 / 0.5 / 0.0 | 99.8 / 0.2 / 0.0 / 0.0 |
| pre-7000 share | 0.9986 | 0.855 | 0.997 |
| S21 | 21 | 2,411 | 59 |

R4 line 52 does report the failure of the PASS cells: "still fail the profile (TV 0.75; 94% of events in the 10000+ bin) and the start-frequency table (99.8% vs 79.2% in [99,100))". It never reports that the textbook-Ne cell reproduces eligible and the start table, where the PASS cells miss the start table by a wide margin (the eligible count is only 2x off).

The reading for Day: at Ne ~1e4 with replacement and a small error rate, the model reproduces everything about his table except the post-7000 tail, which is exactly where he claims a deficit. The cells that fit the tail fit the start table badly. Different summaries prefer different Ne, which is a sign of misspecification, but it is also evidence R4 should show.

Qualifications: Fst, pulse schedule and eps are all free, so the match could be a coincidence. The pre-7000 share and S21 are the same tail measured twice, so the miss counts once, not twice. The start-table match does not show the tail is a deficit; it shows that the Ne preferred by two non-tail summaries is ~1e4.

Fix:
- Add the start-frequency table to the validity gate.
- Add a "which Ne does each summary prefer" table (eligible, start table, pre-7000, S21, profile).
- Run an eps sweep (see F7) so the joint fit is not a single point.

### F3 (MAJOR) §7 draws a substantive inference from cells that are worst on the profile

R4 line 89: "A 0.1% false-minor-call rate reproduces Day's pre-7000 share (0.98-0.997) and large eligible count, so the pre-7000 cluster is plausibly dominated by old-bin sampling and assay error, not by a burst of fixation."

R4 line 52 gives the profile result for the same cells: TV 0.75-0.76, the worst of any variant in Table 5, and 94% of events in the 10000+ bin. Day's profile is 3,038 / 8,741 / 4,497 over the three oldest bins (18.6% / 53.6% / 27.6%, Z18525185 §4.1). The eps cells put 43k of 45k events in the oldest bin (profile row, R0 Ne 1e5 e1e-3). A model that places the events in the wrong bin by that margin cannot support a claim about what produces the cluster.

The weakness is the model's, not Day's. One pooled panmictic population per bin cannot represent Mesolithic and early-Neolithic bins that mix very differentiated ancestries (R4 §8 line 95 lists this). So the "assay error" explanation is a hypothesis from a mis-profiled model, and the model is no more likely to be right about the 22,428 than Day's reading of them as fixations.

Fix: delete the clause "so the pre-7000 cluster is plausibly dominated by ..." from §7 or mark it "hypothesis, unsupported at profile level (TV 0.75)". The same applies to the abstract-level sentence on line 73.

### F4 (MAJOR) The eligible shortfall and the S21 deficit are not independent, and the check treats them as separate

In the model the modern bin has ~1,040 called chromosomes, so a site is eligible essentially only if the allele's modern frequency is below about 1/1,000, or the site is fixed. The number of such sites is set by two unmeasured inputs: the flat density of low-frequency sites (1.86 per unit q, from the c1 D2 chain) and the 7% of sites assumed fixed in the ancestor (R4 line 96). The events that populate S21 come from the same class of sites.

So whatever fixes the 13-70x eligible shortfall in the "consistent" cells would scale S21 up with it. A panel with more rare variants than the flat density, or fewer sites monomorphic in Europeans, is the obvious candidate. R4 line 96 notes "a panel richer in rare variants would raise [eligible]" but not that it would raise S21 and push Ne* up.

The one place where eligible and S21 move at different rates is the eps cells, where the extra eligible sites come from errors on the assumed-fixed class, and the S21/eligible ratio (1.3e-3 for R0 Ne 1e5 eps; Day 9.4e-4) is close to Day's. That is a point for the critic reading, and it should be reported. But it makes the match depend on the 7% assumption and on eps (F7), neither of which is measured.

Fix:
- Report S21/eligible alongside S21 and eligible (Day 9.4e-4).
- Measure the two inputs from public data: the modern AADR bin or 1000 Genomes European frequencies at the 1240k sites give the real low-q density and the monomorphic fraction.
- Rerun the key cells with the measured values before quoting any Ne* from the absolute S21.

### F5 (MAJOR) Ne >= 1e5 is not "ad hoc" in principle, but R4's support for it is unsourced, contradicted by the one measurement cited, and the strongest alternative route (growth) is under-reported

R4 line 88: "literature Holocene European Ne (growth, structure) is plausibly well above 1e4."

The sentence has no citation. The repo's only Ne parameter is `population.Ne_modern_human: {value: 1.0e4, source: textbook, verified: false}` (parameters.yaml line 48). A grep of the sources, ledgers and REVIEW.md finds no Holocene Ne estimate from IBD or demographic inference. By the repo's rule 2 and 8 this is an unverified claim from memory.

On the substance:
- **The principle is defensible.** The textbook 1e4 is a long-term value dominated by deep-time bottlenecks, and pooled samples from a structured metapopulation drift more slowly than any local deme. A critic who says "Holocene pooled-sample Ne could be much larger than 1e4" is not making an ad hoc move. This general point is not from the repo and would need sources.
- **The only measurement either side cites is against it.** C5b: "Nₑ = 8,139 over 102 generations ... Early Neolithic to present gives 9,835 over 250" (keruru, 2026-08-31, "What we found") and "effective size roughly doubles from the Neolithic to the present". A doubling from ~8-10k gives ~2e4, where R4 gives 396-908 for R1-R0 (Table 1), i.e. 19-43 times the 21.
- **The escape also cuts against the critics' own argument.** B2e rests on that same temporal Ne being ~1e4. Adopting Ne >= 1e5 to explain the 21 abandons it. R4 line 91 makes the first half of this point (the neutral expectation is "190x above 21" at keruru's Ne) but not the second.
- **Growth is the more plausible route and is under-reported.** Table 1 gives growth 1e4 to 1e6 as S21 35 (R0, 1.7x the 21) and 15 (R1). That is a pass on the S21 criterion without constant Ne >= 1e5, and it is absent from the §5 "Consistent" list. But the implied schedule has Ne ~2e5 at the Bronze Age midpoint, 25 times keruru's 8,139 for the Bronze Age to Medieval interval. If the critics want growth, they must reject their own C5b.
- **The C5b estimate is itself weak.** It is "extracted", unreviewed, LLM-assisted (C5b "Responses"), assumes a closed population, and admixture would lower it. So 8-10k is possibly a lower bound for drift Ne. This is the critics' best reply and R4 should state it.

Also, line 73's "190x below" is the R0 value at Ne 1e4; across R1-R3 the ratio is 71-190x (line 25), and no run used Ne 8,139 or an 8k to 2e4 schedule.

Fix:
- Remove "plausibly well above 1e4" or attach a retrieved source; add a retrieval task (Holocene Ne from IBD and ancient-DNA demographic inference) to `gaps.md`.
- Add a column to Table 1 for the Ne trajectory, run keruru's own schedule (8-10k rising to ~2e4), and list growth cells in §5.
- Say plainly that every route to S21 near 21 requires Ne at least 10x the only cited Holocene measurement.

### F6 (MAJOR) The check tests Day's d = 0.45 but not the model he states, and declares stasis "not simulable"

R4 line 28: "The 'stasis' reading (zero frequency movement) is not a simulable model."

Day's own paper states the model as stasis: Z18525185 §5.1 "We observe a discrete event followed by stasis." §4.4 "The substitution process effectively stopped 7,000 years ago." Q96 (comment 335823489, 2026-09-13): "genetic drift isn't happening at all over the last 7000 years".

Stasis is simulable as a limit: infinite Ne. The R0 Ne 1e6 cell is within 5% of it for a 525-generation window, and gives eligible 702 and S21 3.6. Two Day-side points follow:
- The 21 is within a factor of six of what pure sampling of a non-drifting population gives, and within ~2.8 with the 0.1% error (59). So Day's observed count is not "impossible" under his own model.
- Conversely, Day's prediction under stasis is S21 = 0, and the check shows non-zero counts arise from sampling alone. The point is that a model with ~14 times less drift than the textbook (Ne* = 1.4e5, line 18) fits the 21 best, and that is the closest the data come to Q96 in the homogeneous grid.

Counterweights that R4 should state next to this, for balance:
- Frequencies visibly moved in the window (C7 external note, C5b, B2e), so "no drift at all" fails on other evidence.
- Day's own C5a asserts a drift-variance Ne "near 2". Under R4's model that would predict thousands of events, so Day holds two incompatible Ne positions. R4 never puts d = 0.45, Ne near 2, stasis and the textbook value on one Ne axis.
- Ne >= 1e5 is only a fit for the homogeneous-capture cells (F1).

Fix: add a short "Ne axis" paragraph in §2: Ne near 2 (C5a), 0.45-clock (Ne/0.45), textbook 1e4, keruru 8-10k, Ne* 1.4e5, stasis (infinity) against the S21 values. Replace "not a simulable model" with "the limit is the Ne = infinity edge of Table 1".

### F7 (MAJOR) The 0.1% error rate: not unfair to the 21, but unmeasured, a single point, and doing more work than its framing admits

What eps does, from the output: it raises S21 by only 1.4-1.9x at Ne >= 1e5 (line 62, P6) but raises eligible 4-27x and the pre-7000 share to 0.98-0.997. So it does not "explain away" the 21; its large effect is on the 22,428. The risk of explaining away a real signal is therefore on the numerator, not the 21. That is a different and larger claim (that most of Day's "fixations" are error), made on a flat assumed rate.

Concerns:
- R4 line 52: "The 1e-3 value is an assumption, not a measured AADR error rate." It is a single value; no sweep (1e-4, 3e-4, 3e-3), so "reproduces the pre-7000 share" cannot be told apart from tuning.
- The rate is flat and symmetric, applied to every pseudo-haploid call (`xe = x*(1-eps) + (1-x)*eps` in `sample_bins`). Real damage and error are strongly site- and library-specific (transitions versus transversions, UDG treatment), so a flat rate misplaces the polymorphism.
- The AADR anno has per-individual data that could replace the assumption: column "Damage rate in first nucleotide" (col 34), "Library type" (col 38), "Pulldown Strategy" (col 19) and "ASSESSMENT WARNING" (col 42). None is used. A transversions-only rerun is a standard robustness check.

Fix: sweep eps (at least 1e-4 to 3e-3), compute it from the anno where possible, add a transversions-only variant, and word §7 as "the cluster could be inflated by error at rates of order X" with X from the sweep.

### F8 (MAJOR) T2 was selected because it resembles Day's profile; his text reads two ways, and the E1/T2 reconstruction is less independent than §1 suggests

Day, Z18525185 §3.4: "For each fixed allele, we traced its frequency trajectory through time to identify when it first reached 100%. This was determined as the oldest time bin in which the allele appeared fixed, working backward from the present."

"First reached 100%" is T2 (oldest bin at 100%, gaps allowed). "Working backward from the present" is literally T1 (the start of the unbroken run). R4 line 99 reports "T1 gives 2-3 orders more events" and treats T2 as "the only reading with a profile resembling Day's" (line 30). That choice came from c1b P1 and was pre-registered, so it is not a post hoc selection, but it is selection by the output being matched: a reading is adopted because it resembles the table, and then the table is not reproduced anyway (TV >= 0.56 under T2 too).

Two things follow. First, the failure to reproduce is not shown to be the model's rather than a different Day implementation; R4 line 84 acknowledges this possibility in a single sentence. Second, there is a decisive, cheap route that R4 does not take, which would settle whose fault it is:
- Z23046531 §5: "Analysis scripts are available from the authors at Zenodo." The repo tracks 39 Day Zenodo records; I found no note on whether the scripts record was fetched or checked.
- AADR v62.0 genotypes are public (the anno is already used). Running E1/T2 and T1 on the real genotype file gives the actual eligible count, profile and 21 directly, with no SFS, Fst, eps or capture assumptions. If it returns 22,428 and 21, Day's procedure is as reconstructed and the question is only interpretation. If it does not, his table is not reproducible from his stated method, and that is a finding about Day, not the model.

Fix: add a "direct replication on real AADR genotypes" check to the queue as the next C1c step (workhorse job, read-only data, no outward action), and a check of the Zenodo scripts. Until then, soften "reconstruction" claims and keep the §6 verdict "not reproducible" attributed to "this model family" rather than "no model".

### F9 (MINOR) Day-side findings are present but not prominent

R4 has no top-of-file summary; the first lines are script and run details. The Day-valid points (the 21 is not a sparse-call artefact; neutral at the textbook Ne gives thousands; replacement widens the gap) sit in §7 lines 82-85, after §6 and well after the critic-favourable §5. §6 "Verdict and suggested edits" lists only the correction of review #4 and the C6 wording, not these Day-valid results. Fix: add a short "Result in brief" at the top giving the six results in neutral order: 21 not a depth artefact; 1.5-3.9k at Ne 1e4; reaching 21 needs Ne >= 1e5 only in homogeneous-capture, error-free cells; no cell reproduces his table; matched capture gives 0.8-5k; the error-rate cells pass only the three-number gate.

### F10 (MINOR) The §5 "Consistent" label is too strong

Line 71 labels R0/R1 at Ne 1e5-3e5 and R2 at Ne >= 3e5 "Consistent". Those cells fail eligible (0.3-1.7k vs 22.4k), profile (TV 0.57-0.72), tracked (1.00 vs 0.727) and, for the eps variants, the start table. Fix: relabel as "S21 within 3x of 21, in cells that fail 3 of the 4 other checks".

### F11 (MINOR) Two sentences overstate, and one range is imprecise

- Line 25 / line 73: "190x" is the R0 value only; the range R1-R0 is 71-187x. Use the range.
- Line 82: "the neutral expectation at the textbook Ne = 1e4 is thousands" holds for R0-R3 (1.5-3.9k); fine, but it is under homogeneous capture and without error; add that capture heterogeneity raises it to 4-20k (line 51).
- Line 36 / headline "No model reproduces Day's table" is accurate only for this model family (single pooled population, flat SFS, 7% fixed, no mutations). Replace with "none of 44 base cells and none of the 5 variants passes the full gate".

### F12 (MINOR) Modern-bin and generation-time inputs

The anno gives 524 modern individuals against Day's 625, and the depth table rescales calls to Day's n (`sc = nday/na`, `build_depth`). The modern bin carries the 100% requirement, so its chromosomes per site (1,039) drive eligibility. Give a sensitivity with the unscaled 524. Separately, the 25-year generation cell (2.5k at Ne 1e4, 73 at R2 Ne 1e5) lowers S21 by 0.6-0.7x only, which is correct, but note that the pooled-sample, deme-structured reading raises the effective generation count slightly the other way.

### F13 (MINOR) Quote and locator hygiene

- R4 is internally consistent with its tables; I re-checked the S21 ratios (R2/R0 0.58 / 3.2 / 7.2; R3 up to 39; kappa 2 multiplies by 14-16) and the post hoc values against `c1c_analysis.txt` and `c1c_posthoc_mindepth.out`. No arithmetic error found.
- Line 82 typo: "Calls depth" for "Call depth".
- In the claim files, C6 (line "Likely cause: per-site call depth in old bins") needs the correction R4 §6 proposes. It is the same correction the Day-side wants, since the "handful of calls" story was a critic-side hope.

## Answers to the assignment's questions

1. **Does E1/T2 match what Day did, and is the failure the model's?** Not shown either way. E1 matches his "between Neolithic and modern" wording; T2 matches "first reached 100%" but not "working backward from the present" (F8). The model's own failures (profile TV >= 0.56 in all 44 cells, 94% in the 10000+ bin, single pooled population) are at least as likely as a different Day implementation. R4 does not assign blame to Day, which is fair. The decisive step is a direct replication on real genotypes (F8).
2. **Is Ne >= 1e5 a plausible escape?** Not ad hoc in principle (F5), but unsupported by anything retrieved in the repo, contradicted by the only Holocene measurement either side cites (8-10k, "roughly doubles"), and, once capture is matched to Day's tracked fraction, not an escape at all (F1). Growth to 1e6 is the more plausible route, and it needs Ne ~2e5 where keruru reports 8,139.
3. **Is eps = 1e-3 fair?** It is unmeasured and a single point (F7). It does not explain away the 21 (1.4-1.9x); it explains away most of the 22,428, which is a bigger claim than the check should rest on a flat assumed rate. Eligible and the start table are matched by the textbook-Ne cell, not by the escape cells (F2).
4. **Are Day's valid points prominent enough?** They are all present (§1, §4 P1, §7) but not at the front, and three further Day-favourable results are missing: matched-capture S21 (F1), the textbook-Ne cell matching eligible and the start table (F2), and the stasis limit (F6). Also missing is the critics' tension between Ne >= 1e5 and their own C5b / B2e (F5).

## What the check gets right, for the record

- The "handful of calls" hypothesis is refuted with real depth (49 / 62 / 282 chromosomes per site in the three oldest bins). This favours Day and is stated plainly (lines 11, 82).
- The reconstructed sample reproduces Day's bin sizes to within a few percent (8,808 vs 8,738).
- Failed predictions are reported without softening (§4), including the two errors in the author's priors (line 66).
- The check does not claim to have replicated his number, and says that a different implementation is not excluded (line 84).
- The critics' own cited Ne is shown to put the 21 far below the neutral expectation (line 91).
