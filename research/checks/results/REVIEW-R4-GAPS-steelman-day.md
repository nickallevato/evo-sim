# Review of R4-GAPS-04-07-02 (steelman, Day's side)

Reviewer role: argue as Vox Day's most capable and honest defender would. Question asked: does the check test Day's claims as he stated them, is it fair to him, and are the credits he is owed prominent enough?

Reviewed: `research/checks/results/R4-GAPS-04-07-02.md`; scripts `gap04_weissman_barton.py`, `gap04_posthoc_concurrency.py`, `gap07_event_counts.py` and `gap02_sweep_window.py` (docstrings and main tables); raw outputs `raw/gap04.out`, `raw/gap07.out`; `docs/research/ledgers/gaps.md`; claims A3, A3a, A3b, A3c, A3x, Gc, F2 and B (branch table); Day sources read-only: `sources/raw/day/zenodo-23003785.txt` (abstract; s4.3; s7.1 to 7.3; s8.2), `zenodo-18452504.txt` (s4.3 lines 316 to 333), `zenodo-18441321.txt` (s3.1). I ran no code. Numbers marked "(hand)" are my arithmetic and should be re-run.

Overall: the arithmetic is careful, the pre-registration discipline is real, and many Day-favourable results are in the prose (the 3.3 to 4.5x credit, the Hernandez and Yoo sweep-rarity points, the 327 Mb to 0.35 to 0.9 Gb SV point, the indel under-count). The weaknesses are (a) the all-fixations reading, which is Day's own stated model, is presented as an optional reading nobody holds; (b) several results are stated only for the critic-favourable end of a range (Eq. 7 instead of Eq. 13, K_a stopping at 10^6, interference-only "feasible", one comparator class, K = 3,200 only); (c) the bp-versus-events section does not engage the strongest bp reading. None of these reverses a headline direction. Several narrow the "critic" credits and sharpen the Day credits.

Counts: 7 MAJOR, 7 MINOR.

---

## MAJOR

### 1. The all-fixations reading is Day's stated model, not a side reading (GAP-04, "Who it helps", Day paragraph; suggested A comment; gaps.md GAP-04 beneficiary)

**Locator.** R4-GAPS "Who it helps" says the all-fixations reading "treats neutral substitutions as sweeps, which W&B do not. No critic holds it, and Day concedes Term 3 limits 'adaptive substitution only' (H1)." The suggested A comment ends "on any α-based reading it is not binding".

**Argument.** Testing Day "as he stated" means testing this reading.
- MITTENS 3.0 s4.3 (`zenodo-23003785.txt` lines 292 to 293): "MITTENS measures total throughput — every fixation, regardless of mechanism. The 1,322 gen/fix rate already includes beneficial sweeps, neutral hitchhikers, compensatory mutations, and everything else."
- s8.2 (lines 585 to 600), on humans: "The remainder are hitchhikers, and the hitchhiking throughput is bounded by the beneficial sweep rate, which is what MITTENS already measures." He adds "The drift channel is not slow. It is off."
- Z18441321 s3.1 "First" (line 117): the 1,600 gen/fix "is the selection-driven rate".

So for node A, Day's claim is that all 17.5 to 20M fixations are carried by the sweep process, and that the neutral channel does not run independently. The "H1 concession" is about Term 3 (Haldane), not about MITTENS node A. Citing it as a reason the all-fixations reading is "not live" mixes two nodes.

The premise "neutral substitutions need no sweep" is the critics' k = μ premise (branch B: B5 "contested", B2/B3 "pending"). The write-up uses it to qualify Day's credit ("W&B do not") and to say the bound "is not binding on any α-based reading". That uses an undecided branch-B premise as if settled.

**Honest counterpoint (sound against Day).** Day's own s4.3(1) block arithmetic (lines 318 to 322) shows hitchhiking cannot carry the load: 20M differences over 3,200 to 32,000 blocks is 600 to 6,000 per sweep, far above heterozygosity. His claim that neutral fixation is all hitchhiking is therefore doubtful on his own numbers. That is a branch-B point, not a W&B point.

**Fix.**
- Replace the sentence with: "On Day's stated model (all fixations are sweep-carried, s8.2), the requirement is 3.3 to 4.5x above the W&B asymptote and supply-infeasible beyond it. On the critics' model (neutral fixations independent of sweeps), the bound does not bind. Which model holds is branch B, not decided here."
- Drop "No critic holds it" from the argument. It is true, but it describes who holds the reading, not whether it is Day's.
- Correct the H1 reference: it limits Term 3 only.
- Suggested A comment: lead with the two-model split, not "on any α-based reading".

### 2. W&B Eq. 13 (exponential DFE, R/4) is computed but not carried to human scale (GAP-04, Procedure item 3, human-scale table, F2 and A comments)

**Locator.** The R4-GAPS "Sources" list cites Eq. 13 (Λ ≈ Λ0 / (1 + 4Λ0/R), "twice the interference of fixed s"). `raw/gap04.out` section A computes it for the F2 grid (e.g. 0.387 vs F2 0.617 at 0.1 M, 2N·U_b = 2). Section B (human scale) uses Eq. 7 only.

**Argument.** Fixed s for every adaptive mutation is the less realistic case. GAP-01 relies on Uricchio's "72% weakly adaptive", i.e. a spread DFE. For the paper's own exponential DFE the interference is doubled and the large-supply asymptote halves to R/4 (my reading of Eq. 13 as the c = 4 case; the audit's write-up says the same in words; hand check below).
- R/4 = 8.75 to 9.5 per generation. Day's 17.5 to 20M requirements (3.3 to 4.5x over R/2) become about 6.5 to 9.1x over the cap (hand).
- GAP-01 K_a = 10^6: Λ0/R ≈ 0.11, Eq. 13 loss ≈ 30 to 31% (not 21 to 23%), and the rate is 2.2 to 2.4x under the cap (not 4.4 to 4.8x) (hand).
- The F2 grid is itself evidence of how much this matters: the c = 2 formula over-predicts interference at 0.1 M by up to 2.8x, so the formula direction is not uniformly favourable to Day. But the omission of c = 4 at human scale is one-directional: it removes the version that is least favourable to the critics.

**Fix.** Add Eq. 13 columns to the human-scale table and the suggested comments. State the Day credit as "3.3 to 4.5x (fixed s) to 6.5 to 9x (exponential DFE)". Restate the critic credit as "interference loss 23% (fixed s) to 31% (exponential DFE) at 10^6". Re-run and confirm my hand figures.

### 3. The K_a rows stop at 10^6 (about 6% of the differences); the disputed interval is not tabulated (GAP-04 human table; "Who it helps", Critics paragraph)

**Locator.** Human-scale table rows "GAP-01 K_a = 10^3 to 10^6"; Critics paragraph: "'Recombination makes parallel adaptation feasible' (argued) is supported at the GAP-01 rates".

**Argument.** The top row (10^6, 5.7% of 17.5M) is where the audit's unsourced a_nc grid (0 to 5%) ends. The substantive dispute is the adaptive share between about 6% and 100%. The W&B asymptote sits inside that gap: R/2 × 252,000 = 4.4 to 4.8M per lineage, i.e. about 25 to 27% of the 17.5M differences, or 13 to 14% under the exponential DFE (hand). The framing "GAP-01 range" therefore imports the critics' premise that the adaptive share is small, without saying how small it has to be.

The critics did argue that recombination removes the limit. They did not argue an α-based number (gaps.md GAP-01: "never give a number"). The α-based reading is the audit's.

**Fix.**
- Add a "crossing fraction" row: "W&B binds if more than about 13 to 27% of the differences are adaptive".
- Retitle the Critics credit: "for adaptive shares below that crossing".
- State in the headline that the crossing sits between GAP-01's top row and Day's reading, and that the noncoding α is the unmeasured input.

### 4. "Feasible" for the critics is an interference-only result; the cost leg is untested at the same rates (GAP-04 Critics paragraph; suggested F2 comment)

**Locator.** "Interference costs ≤ 23% at 10^6 and ≤ 0.2% at 10^4"; F2 comment: "'human-scale untested' caveat is bounded analytically for α-readings".

**Argument.** The F2 claim file lists the untested items as "human-scale active loci, hard selection combined with linkage, N = 1e4, DFE". W&B model soft selection (polygamous Wright-Fisher, fixed N). The same gaps.md GAP-01 entry gives the audit's hard-selection cap: H2-hard ln R/D = 0.0048 to 0.035 per generation (about 1,200 to 8,700 per lineage). Against that, K_a = 10^4 to 10^6 is 1 to 800x above it. For GAP-01 rows ≥ 10^4 the interference check passes while the cost check, which the audit itself computed, fails or is unresolved. The write-up mentions "cost of selection (H) is separate" only in the Gc paragraph. Readers will take "supported at the GAP-01 rates" as an overall feasibility finding.

The R/2 rate also implies a mean log-fitness gain of v = Λ·s per generation: 17.5 × 0.01 = 0.175 per generation at the asymptote, 0.04 per generation at the 10^6 row with s = 0.01 (hand). A reader seeing "4.4x under the cap" is not told that sustained gain is itself the Haldane problem.

**Fix.**
- Qualify every critic credit: "on the interference leg only".
- Add the H2-hard cap column (1,200 to 8,700 per lineage) next to the W&B column in the human-scale table, from gaps.md.
- Keep the F2 "human-scale untested" caveat as "partly bounded (interference); hard selection with linkage still untested".

### 5. GAP-02 comparator inconsistency: haplotype-scan counts disqualify one way, then set the ceiling the other way (GAP-02 "Procedure", "Answer to the brief")

**Locator.** Procedure: "Only SFS/diversity scans count as detectors of completed lineage-wide sweeps. Haplotype scans target incomplete or population-specific sweeps (Voight; Sabeti's XP-EHH)." Answer: "Not evidence against a coding-scale adaptive count. K_a ≈ 10^3 to 10^4 … predicts 4 to 400 … That is the order of the per-scan counts."

**Argument.** The audit rules the Voight (~250) and Sabeti (> 300) counts invalid as comparators for completed sweeps. It then compares K_a = 10^3 to 10^4 to "the per-scan counts", and uses Akey's 722 replicated and 5,110 union regions (unions of the same haplotype-heavy scans, with Akey's own "poor concordance") as the ceiling for "tension". On the audit's own rule the only SFS-type comparators in hand are Yoo's SweepFinder2 counts (11 to 62 per ape taxon; saltiLASSI 4 to 18) and Hernandez's trough test.
- Against Yoo's counts, K_a = 10^4 predicts 159 to 397 (power 1) or 44 to 111 (f_strong = 0.28): about 2 to 18x the median taxon (22) (hand). K_a = 10^3 (16 to 40; 4 to 11) matches.
- So "coding-scale K_a not excluded" holds at 10^3 and is borderline at 10^4 under the audit's own comparator rule. Yoo is apes (different N_e and windows), so this is a caveat, not a refutation.

**Fix.** Pick one comparator class per row. Tabulate E_detect against both (a) the SFS-type counts (Yoo; Hernandez) and (b) the mixed-scan union (Akey), and say which is the right class. Rewrite "that is the order of the per-scan counts" to "K_a ≈ 10^3 matches SFS-type counts; 10^4 is 2 to 18x above the ape SweepFinder2 median".

### 6. GAP-02: "non-sequitur" rests on K = 3,200 only, N_e = 10^4 only, and tautological "predictions" (GAP-02 Results, Predictions table, suggested claim verdicts)

**Locator.** Predictions P1 to P6 "HELD"; suggested new claim internal verdict "non-sequitur".

**Argument.**
- (a) **K range.** In Z18452504 s4.3 the number 3,200 is the *minimum* of Day's block range "3,200 to 32,000 independent sweeps" (line 318), not a count he claims. His "3,200+" in bullet (4) is the lower end. At K = 32,000 and the audit's own windows E_detect = 394 to 985 (hand), which is "hundreds" and above Akey's 722 replicated at W = 10,000. "Does not follow" is true at the low end only.
- (b) **N_e.** The audit scales W with 4N_e for bonobos (N_e = 20,000) but fixes N_e = 10^4 for humans. Day's own range is 10,000 to 33,000 (MITTENS 3.0 s8.2). At W = 33,000 and K = 3,200, E = 325; at K = 32,000, E ≈ 3,250 (hand). The window is scaled in one direction (shorter) for the human case.
- (c) **Predictions.** The falsifiers cannot be hit by construction: P1 (E > 1,000 for K = 3,200; the maximum possible is 98.5), P2 (E > 722 for K ≤ 10^4; maximum 397), P4 to P6 are identities of the formula. "6/6 HELD" reads as an empirical test. The verdict depends entirely on the unvalidated model: uniform in time, power 1 inside W, detection fixed at the Hernandez window.
- (d) **Direction.** E_detect at power 1 is an upper bound on detections. The match "39 to 98 in the window vs 'dozens to hundreds' observed" therefore shows consistency with Day's counts, not that Day's inference is wrong.

**Fix.**
- Report E_detect over K = 3,200 to 32,000 and N_e = 10^4 to 3.3 × 10^4.
- Relabel P1 to P6 as "arithmetic consequences of the model", not as tests.
- Soften the internal verdict to "does not follow at K = 3,200 and W = 10^4; follows weakly at the top of Day's own range".

### 7. GAP-07: the bp reading is rebutted, not engaged (GAP-07 "Who it helps", "Fidelity flag"; claim A3a Assumptions)

**Locator.** "Day already concedes the unit concern (A3b, §7.3)"; suggested A3a external "contradicted as an event/fixation count".

**Argument.** Two weak spots.
- (a) **The concession text.** MITTENS 3.0 s7.3 (line 530 onward) says SVs "should not each count as a single fixation event in the same sense as a point mutation." That does not say bp-weighted counts are wrong. Read at its strongest it says an SV is not commensurate with one point mutation, and Day then sets all SVs aside "as a freebie". The paper's abstract (line 24) and the 2nd-edition post ("410 million base pairs separating the two lineages") still carry the bp figure. The write-up's reading is plausible and probably what he meant. It is stated as fact.
- (b) **The strongest bp reading is not computed.** For tandem-repeat and satellite divergence (a large share of T2T "gap divergence"), the natural mutational unit is the repeat unit, not the whole array. The write-up's "327 Mb ≈ 1.3 × 10^4 events of mean size" assumes single-event SVs. At unit scale, 327 Mb / 171 bp (alpha-satellite monomer; to be verified) is about 1.9 × 10^6 events, and for few-bp units it can reach 10^7 to 10^8 (hand). That sits between the 20M events of the SNV-plus-indel count and the 205M bp count; the 9 to 21x ratio does not hold at that unit. I do not claim Day argued this. The write-up is meant to test the strongest form.

**Honest counterpoint (sound against Day).** Day's own G_f counts events. In s4.3 the 20.5 neutral hitchhikers are μ_genome × G, an event count, and 56.0 fixations are events. Dividing a bp count by an events-per-generation rate is a unit mismatch inside Day's method under any reading. This should be stated as the main reason bp does not work, in place of the concession.

**Fix.**
- Add a repeat-unit-scale row (with the unit size labelled as an assumption).
- State that the 9 to 21x ratio is for the event reading.
- Give the units-inside-G_f argument as the decisive point.
- Change "Day already concedes" to "Day sets SVs aside in s7.3 (wording ambiguous on bp versus events)".

---

## MINOR

### 8. GAP-07 headline ratio and "three independent routes" (GAP-07 Results; "Who it helps")

M1 and M3 are both k = μ-type routes: M3 assumes each class fixes in proportion to its mutation rate relative to SNVs. Day disputes k = μ in branch B. Only the CSAC observed basis is rate-free, and it gives 9.1 to 10.2x. M1 also under-counts SNVs by 1.9x (9.2M vs 17.5M observed) and indels by 1.2 to 13.5x by the write-up's own tables, so its 19.8 to 21.4x is an upper bound on the ratio. The headline "9 to 21x" and "three independent routes" overstate. At Yoo's N_anc and Day's T (grid, T = 252,000), the rate-based total is 22 to 30M, above Day's 2025 20M; ratio 6.9 to 9.2x. **Fix:** headline "about 9 to 11x (observed and calibrated); M1 up to 21x, an upper bound"; describe the routes as one data-based and two rate-based with stated assumptions.

### 9. GAP-07 tally: the event count corroborates Day's 2025 figure (GAP-07 "Who it helps"; tally "critics, modest")

The corrected event count is 20.0 to 22.5M per lineage. That is at or above Day's SNV-only 17.5M and his 2025 20M. The per-species reading of CSAC p.73 ("5 million events in each species") raises the 2025 figure to 22.5M, a Day-favourable correction labelled as a "both sides" fidelity flag. The shortfall stays about 10^5 (20M / 191, hand). The 205M headline falls, but the 17.5M and 20M versions, and the five-orders-of-magnitude conclusion built on them, are corroborated. **Fix:** add a Day-credit line: "event count 20 to 22.5M corroborates A3 (2025) and A3b; the five-order shortfall is unchanged". Consider "critics: unit argument; Day: A3/A3b magnitudes" in the tally.

### 10. GAP-02 "Day's other bullets … not tested" omits bullet (6) (GAP-02 Caveats; Z18452504 lines 333 to 335)

The window addresses diversity, EHH, Tajima's D and LD signatures, which decay over about 10^4 generations. Bullet (6) concerns the *clustering of fixed differences in blocks*, which does not decay. It is testable and is not mentioned. Likewise "20M / 3,200 = 6,250 fixed differences per sweep" is a window-free implausibility that supports Day's block argument. The suggested external verdict for the new claim ("contested") bundles a supported empirical premise (classic sweeps are rare; Hernandez, Yoo) with a failed inference. **Fix:** list bullet (6) as untested; split the external verdict into "premise supported / saturation inference does not follow".

### 11. GAP-04 supply statement carries more precision than its basis (GAP-04 Section C; A comment "supply-infeasible beyond it")

U_b ≥ U_tot rests on a by-eye reading of Fig. 4 (s = 0.05, R = 1, ±2x) extrapolated to R = 35 M, times e^{4Λs}. Without interference the same rate needs U_b ≈ 0.17 per haploid genome at N_e = 10^4, s = 0.01 (0.5% of U_tot; hand). Everything above that comes from the extrapolated interference term. N_e = 10^4 is the audit's working value; Day's range is 10,000 to 33,000, where the needed share is 29 to 290% (hand). The sentence is used as a deflator of Day's credit ("Exceeding it by ~2× still needs supply …"). It is also evidence that the required rate is infeasible, which supports Day's conclusion. State both. `raw/gap04.out` also prints "P8_falsifier_hit FAILED" for a False boolean, which reads as the falsifier failing; relabel as "not hit". **Fix:** add the ±2x and extrapolation qualifier to the A comment; state the no-interference baseline; fix the output label.

### 12. Gc post hoc comparison (R4-GAPS "POST HOC" and suggested Gc comment)

Day's "active zone" is a variance-compression mechanism and s6.1 adds a reproductive ceiling (Σs ≤ 1 to 2, i.e. 100 to 200 loci at s = 0.01, which the Gc claim file notes is nearest to 230). W&B model soft selection. At the R/2 asymptote, 7.7 to 15 × 10^3 concurrent sweeps at s = 0.01 give Σs of about 77 to 150, far past that ceiling. The write-up flags "cost of selection untested", which is right, but the suggested Gc comment "no support for 230 from interference theory" can be read as saying 230 is wrong. **Fix:** add: "230 is not an interference limit; the closest candidate is the s6.1 ceiling, which this check does not test, and R/2 concurrency exceeds it by 50 to 100x".

### 13. Verdict wording for A3a and the new G claims (suggested verdict edits)

- A3a "external contradicted as an event/fixation count" scores a figure that Day set aside in s7.3 while the abstract keeps it. Offer "contradicted as events; supported as bp magnitude (Yoo 327 Mb)" instead of a single label.
- New claim for Z18441321 s3.1: "internal holds" with "external supported" is fair, but add that Day's own "First" argument (the 1,600 gen/fix is already selection-driven) does the logical work, not the signature argument.

### 14. Small presentation points

- The Day credit in GAP-04 is in the table (bold) and "Who it helps". It is not in the first paragraph of the section or in the F2 comment, which leads with the critic-favourable range ("4.4 to 4,800x above"). Put the 3.3 to 4.5x credit in the first line of the GAP-04 summary.
- gaps.md tally "no change to beneficiary labels: GAP-04 both" understates the Day side once items 1 to 4 are applied (credits become conditional on branch B; the critic credit becomes interference-only and below the crossing fraction).

---

## Day-side points the write-up should state more prominently

1. For node A as Day states it (all fixations sweep-carried), the mainstream finite-map bound is 3.3 to 4.5x below the requirement (fixed s), 6.5 to 9x (exponential DFE, hand), and exceeding it needs a beneficial supply that W&B's own simulations put near or above the total mutation rate.
2. The critic credit is conditional on three things not tested together: an adaptive share below roughly 13 to 27%, soft selection, and Eq. 7 rather than Eq. 13.
3. The event count (20 to 22.5M) corroborates Day's 17.5M and 20M; only the 205M bp headline falls, and the shortfall stays about 10^5.
4. Day's classic-sweep rarity is supported (Hernandez, Yoo), and on an SFS-type comparator K_a ≈ 10^4 is not clearly "not excluded".
5. The saturation inference is weak at K = 3,200 but not at the top of Day's own block range or his own N_e range.

## Points that stand against Day (sound; the write-up is right)

- W&B's R/2 is 4.4 to 4.8M per lineage, about 2 × 10^3 to 2 × 10^4 times Day's LTEE-based achievable (191 to 2,407). "Linkage limits parallelism" is vindicated in form, not in magnitude. The write-up never states this ratio; it should (it narrows, not removes, the Day credit in item 1 above).
- bp does not convert to events inside G_f (item 7). The 205M headline is not a fixation count under Day's own method.
- At K = 3,200, E_detect (39 to 98) is "dozens to hundreds"; the "saturated" inference fails on his low-end number.
- Day's own block arithmetic (600 to 6,000 differences per sweep) undercuts "all neutral fixations are hitchhikers" (item 1).
- The all-fixations bonobo count (326,000 selective sweeps) is decisively excluded by Yoo's 30, but that supports Day's reductio, not a position anyone defends.
- The write-up's own caveats on F2 (c = 1.02 and chi-squared 318 at 0.1 M), the by-eye Fig. 4 reading, the unsourced 0.1 × 4N_e window, and Przeworski and Sabeti being inaccessible are disclosed honestly.
