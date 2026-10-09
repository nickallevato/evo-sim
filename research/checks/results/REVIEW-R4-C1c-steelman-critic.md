# Review of R4-C1c: steelman from the critics' side

Reviewer stance: the most capable honest defender of the critics' position (keruru, McCarthy, Camestros, Mansfield, the r/DebateEvolution and Peaceful Science commenters). I was asked to argue for them as strongly as honestly possible and then say whether the check gives them their due.

Scope read: `results/R4-C1c.md` (cited as "the note", with line numbers), the script `research/checks/c1c_call_depth_replacement.py` (docstring and code), `results/raw/c1c_analysis.txt`, `c1c_posthoc_variant_gate.txt`, `c1c_posthoc_mindepth.out`, claims `C-adna-zero-fixations`, `C1`, `C1a`, `C4`, `C5`, `C5a`, `C5b`, `C6`, `C7`, `B2e`, the critic quotes in `sources/quotes-critics.md` (KR-01..09, MC-01..13, RF-1..16) and `opponents/keruru.md`, `results/R4-C1b.md`, `results/R4-B3b-C1.md`. I also read keruru's Zenodo draft (`sources/raw/refresh-2026-10-09/zenodo-22184713/x/adna-temporal-ne/adna-draft-1.md`, sha256 prefix 3a115d6a) read-only as text; nothing from `sources/raw` was executed. I edited no other file and did not commit.

**Reviewer scratch computations.** Two throwaway scripts in the session scratchpad import the check's own functions (`make_panel`, `simulate_scenario`, `sample_bins`) on reduced panels (100k and 200k sites, one sampling draw, one seed). Numbers marked "scratch" come from them. They are directional, not publishable; if any is cited it should be re-run as a repo script with a pre-registration.

## Verdict in brief

On process and on the narrow question asked, the note is good for both sides. It refutes the repo's own earlier "handful of calls" hypothesis (a point against the critic-side hope, stated plainly), it reports that 6 of its 8 pre-registered predictions failed, were refuted or held only in part (P2 for R2/R3, P3 once an error term is added, P4, P6, P7, P8 for strong replacement), and it labels its post hoc work. That is what the critics' side needs for the result to be trusted.

Where it under-delivers for the critics, in order of weight:
1. The headline "at the textbook Ne of 1e4, neutral predicts 1.5-3.9k" is a constant-Ne statement. The note's own growth rows (15 to 35 for 1e4 to 1e6 growth) are about 15 to 260 times closer to 21, and the note does not carry them into its summary or verdict (Finding 1).
2. The note feeds keruru's measured Ne (8,139 and 9,835) into the model as if it were the model's drift Ne, and calls the result a "190x" deficit. keruru's own draft says those figures are biased downward; the note's own replacement model shows a temporal estimator across the Neolithic-to-present window returns about 7-14k whatever the true drift Ne is (scratch). The "190x" is the top of a range that is closer to 6-30x once that is allowed for (Finding 2).
3. The note says "neutral also predicts ~0" is false. The repo's claim of that form is about intermediate starting frequencies and Z23046531's two-period statistic. The 21-class events in the check's own model (scratch) start almost entirely at 95-100% in the Neolithic, as Day's own §4.3 says of his events. The intermediate-start claim is untouched, and the note does not say so (Finding 3).
4. The critics' own errors are only partly recorded and not attributed (Finding 7).

Where the critics' case is weak and the note is right (so the review is two-sided): constant Ne = 1e4 with the measured trajectories gives a deficit of two orders of magnitude; every sampling variant that reproduces Day's tracked fraction overshoots by at least 40x; the growth that closes the gap (1e4 to 1e6, a hundredfold) is outside both measured Ne trajectories in the repo (keruru's and Day's C4) ; replacement does not shrink S21; Day's own d = 0.45 does not help Day (Findings 1, 6, 10).

## What the check does well (credit, so the findings below are read in proportion)

- Real depth from the public anno reproduces Day's bin sizes within about 1-5% per bin (note line 7), which makes the call-depth question an empirical one.
- The "handful of calls" hypothesis from the repo's own review #4 is withdrawn in the note itself (line 11, line 77). That is a correction against the critic-side direction and it is stated without softening.
- P3 is reported as "Held for the base grid (0/44), refuted when an error term is added" (line 59), not hidden.
- The 44-cell grid is reported in full, including cells unfavourable to the author's priors (R2/R3 never reach 21).

---

## Findings

Summary: 12 findings, **6 MAJOR** (1, 2, 3, 4, 5, 7) and **6 MINOR** (6, 8, 9, 10, 11, 12). Findings 1, 2, 3, 5 and 7 move credit toward the critics. Findings 4 and 6 are mixed. Findings 8, 9 and 10 trim critic-side claims or flag presentation, and are included so the review is two-sided.

### 1. MAJOR. The headline is a constant-Ne statement; the census-explosion family is already in the grid and closes most of the gap, but only in a bullet

**Locator.** Note line 25: "**Textbook Ne = 1e4:** neutral expectation 1.5k-3.9k, i.e. the 21 is 70-190 times below it (R1-R3 and R0)." Note line 26: "**Growth** 1e4 to 1e5 across the window: S21 262 (R0), 276 (R2). Growth 1e4 to 1e6: 35 (R0, 1.7x the 21), 15 (R1), 67 (R2), 220 (R3)." Raw `c1c_analysis.txt` Table 1: `R0_grow1e4-1e6 ... 35.2 | [26, 40]`, `R1_grow1e4-1e6 ... 15.1 | [10, 20]`, and the validity table marks both `S21 ok = True`. The task summary and note line 73 reduce this to "A Holocene Ne of ~1e5 or more is needed".

**Argument for the critics.**
- Holocene Europe is the textbook case of a census explosion. The relevant quantity for a 7,000-year window is not the long-term coalescent Ne (a harmonic mean dominated by bottlenecks), it is the trajectory. The repo's parameters file marks `population.Ne_modern_human` = 1e4 as "textbook, unverified" (C4 file, "Formal statement").
- With the single exponential the note ran, R0 1e4 to 1e6 gives 35 (1.7x the 21) and R1 gives 15 (0.7x). Both are inside the pre-registered S21 band [7, 63]. That is a model with a Neolithic Ne of 1e4 and no stopped clock. In the same family, 1e4 to 1e5 gives 262 and 276, a 12-13x deficit, not 190x.
- The note's constant-Ne ladder shows S21 falling roughly as Ne^-2 near 1e4 to 1e5 (3,925 to 908 per doubling of Ne; Table 1). So the conclusion is exquisitely Ne-sensitive and any honest headline must be a function, not a number.
- The exponential is also a shape choice. The Ne at the start of the S21 window (6,000 BP) in the 1e4 to 1e6 case is 7.3e4 (reviewer arithmetic: 1e4 x 100^(4500/10500)), and the S21 events accumulate when Ne is already large. A Neolithic step (Ne jumps to 1e5 by 8,000 BP, then 1e6) would give a different and probably lower S21. It was not run.

**Where this cuts against the critics (record it).** The two measured Ne trajectories in the repo bound the variation far below 100x. Day's own C4 reports "Drift variance ... varied 3.3-fold" (Z18320599 Abstract) and keruru's draft says the Neolithic-to-present size "roughly doubles" (C5b file). keruru's table (draft §6) runs 938, 6,933, 8,139, 9,835. A hundredfold growth to 1e6 is not what either measurement shows, unless both are strongly biased (Finding 2). And the closed-population growth cells still fail the eligible count (1,359 and 541 against 22,428; note line 72).

**Fix.**
- Replace the headline with a small table: constant Ne; growth 1e4 to 1e5 and to 1e6; the two measured trajectories as explicit scenarios (keruru's piecewise 938 / 6,933 / 8,139 / 9,835; Day's 3.3-4.6x variation); and a Neolithic-step scenario. Report S21/21 for each.
- State in the abstract line that the sign of the verdict flips inside the census-explosion family, with the measured trajectories as the constraint that disfavours the flip.
- Add a one-line statement of the S21 ~ Ne^-2 sensitivity so a reader sees why "Ne about 1e5" is a statement about a steep function.

### 2. MAJOR. keruru's Ne is used against the critics without his own stated direction of bias, and without the model's own evidence that the estimator does not track drift Ne under replacement

**Locator.** Note line 73: "keruru's temporal Ne 8,139-9,835 (C5b) puts the 21 in the deficit class, 190x below the neutral expectation." Note line 91: "Cuts against critics: the temporal-method Ne they cite (8-10k, C5b) makes the neutral expectation 190x above 21; the neutral expectation is not "~0" at their own Ne."
keruru draft, `adna-draft-1.md` lines 212-218: "Three known biases, all downward. ... Any residual ancestry turnover deflates the estimate — simulation puts this at up to fivefold under heavy replacement. And close relatives were not removed, which Fournier et al. (2023) note lowers inferred effective size ... The true value is therefore plausibly higher than either figure". Same file, line 703: "No relatedness filtering. Known relatives were not removed; this biases N̂_e downward." And line 637: "Structure inflates the estimate. It does not deflate it."

**Argument for the critics.**
- The note treats 8-10k as the model's constant Ne and reads off the R0 row (3,925 / 21 = 187, hence "190x"). Three things are wrong with that pairing.
  1. The figures are measured on data that include replacement, relatives and a moving sample. The author says they are biased low. The note's own R2 and R3 cells already include replacement variance, so putting Ne = 1e4 into R2 and R3 counts that variance twice.
  2. The 9,835 window (Early Neolithic to present) spans the Anatolian and steppe pulses in the note's own replacement model. Scratch: I applied a Nei-Tajima Fc temporal estimator (my simplified implementation, not keruru's code) to the note's own simulated bins, with real depth sampling. For the 7000-8000 BP bin to the 0-500 BP bin (362 generations), the estimate is: R0 Ne 1e4 gives 10.0k; R0 Ne 1e5 gives 96.8k; R2 Ne 1e4 gives 6.6k; R2 Ne 1e5 gives 12.6k; R2 Ne 1e6 gives 13.9k. For the 5000-6000 BP bin to 0-500 BP (262 generations): R2 gives 4.9k, 8.7k and 9.4k at true Ne 1e4, 1e5, 1e6. So under the check's own R2 replacement model a "temporal Ne of about 10k" across the Neolithic-to-present window is what you measure whether the true drift Ne is 1e4, 1e5 or 1e6. It does not constrain the drift Ne the S21 depends on. keruru's "up to fivefold" under-states the effect in this model.
  3. Closed-population windows do track the true Ne. Scratch, 4000-5000 to 2000-3000 BP (100 generations, after the last pulse): R2 true Ne 1e4 gives 9.97k, 1e5 gives 97.5k. So keruru's 8,139 (Bronze to Medieval, 102 generations) is the cleaner window in the model. In the real record that window has post-Bronze admixture (Iron Age, Roman, migration period, medieval) that the check's model omits, and keruru reports no ancestry control and no relatedness filtering. So the 8,139 is also a lower bound on drift Ne by the author's own account.
- Allowing the author's stated upward correction of up to about 5x (8-10k to roughly 5e4) and reading Table 1 at Ne 5e4: S21 is 120 (R0), 238 (R2), 634 (R3), i.e. 6x to 30x, not 190x. The relatedness bias is extra to the 5x.

**Where this cuts against the critics (record it).** Structure cannot save the critics. keruru's island-model table (draft §6.1, lines 637-650) shows pooling across demes raises the estimate, so a structured-metapopulation explanation of a low Ne is not available. And at the corrected Ne of 5e4 the deficit is still 6-30x. The temporal Ne is evidence for Ne in the range 1e4 to a few 1e4, and the S21 at that range is 100 to 4,000.

**Fix.**
- In §5 and §7 state the deficit as a range tied to keruru's stated bias (about 6x to 190x), not 190x.
- Add to the script (as a separate pre-registered post hoc run) a temporal-Ne observable computed from each simulated cell with the same estimator the critics use, for the Early-Neolithic-to-present and Bronze-to-Medieval windows. Then say which cells reproduce 8,139 and 9,835. That turns the Ne dispute from an argument into a table, and it is the only way to connect the note's grid to the C5b measurement.
- Add a sentence to the C5b / B2e suggested edits: the 9,835 window spans the replacement and is insensitive to drift Ne in the check's model.

### 3. MAJOR. "Neutral also predicts ~0 is false" is a different statistic from the one the repo's claim is about; the 21-class events in the model are near-fixed completions, as Day's own text says

**Locator.** Note line 83: ""Neutral also predicts ~0" (the critic-side reading of this statistic) is false unless Ne >= ~1e5 (closed) and is false at any Ne <= 1e6 under strong replacement."
Claim file `C-adna-zero-fixations.md`, verdict comment: `internal: "non-sequitur"   # neutral also predicts ~0 from <50% and 0.04-0.11 from 50-90%`. `R4-B3b-C1.md` line 60: "headline "0 from <50%, 0-3 from 50-90%" is the neutral expectation at Ne ~1e4 (0.04-0.11)". `R4-C1b.md` line 28 labels the same phrase differently: "Day-side ("neutral also predicts ~0, no power"): not supported within this model".
Day Z18525185 §4.3 (quoted in `C6` file): "This confirms that essentially all "fixations" were completion events for alleles already near fixation—not new substitutions traversing the frequency spectrum."
keruru KR-03 (para 14): "Integrated across a million loci starting from intermediate frequencies, the expected number of fixations is somewhere near 10⁻²⁹."

**Argument for the critics.**
- Every critic-side zero in the repo (KR-03, C5, C7, claim C) is a statement about starts at intermediate frequency. None is a statement about alleles that begin at 95-100%. The note's S21 is computed over all start frequencies, so "false" is true of a different quantity.
- Scratch, 200k-site panel, the note's own model and sampling: of the S21 events (tracked E1-T2, dated 5000-6000 BP or younger) at R0 Ne 1e4 (693 events), 24% start at sample frequency 99-100%, 73% at 95-99%, 3% at 90-95%, 0% below 90%. At R2 Ne 1e4 (434 events): 34% / 64% / 2% / 0%. The thousands at Ne 1e4 are near-fixed completions, exactly the class Day's §4.3 says his events belong to (his start table: 79.2 / 20.2 / 0.5 / 0.2%). At higher Ne there are too few events to tabulate (8 and 5).
- So the intermediate-start prediction that critics made, and the repo's claim C verdict (non-sequitur because neutral predicts ~0 from below 50%), are not contradicted by C1c. If anything the start-band profile supports them. The note reports start frequencies only for the whole eligible set (Table 6) and not for the S21 events, so a reader cannot see this.
- Attribution is also inconsistent. C1b labels this phrase "Day-side"; C1c labels it "critic-side". No published critic quote in `quotes-critics.md` says it about the 21 (MC-01..13 and RF-1..11 are branches A, B and G; the only C-branch critic items are KR-03, KR-04, RF-12..16). It is the repo's own audit phrase from claim C. The note therefore corrects a position no critic is on record as holding.

**Fix.**
- Add start-band columns for the S21 events themselves (the script already computes `cat` per eligible event; restrict to the T2 >= bin 4 events). Report them beside Day's §4.3 table.
- Rewrite note line 83 as two lines: intermediate starts (<90%): about 0 in every cell, unchanged and supporting claim C, C5, C7; near-fixed starts (>=95%): thousands at Ne 1e4, falling steeply with Ne.
- Make the attribution of the phrase consistent (it is the repo's, not a quoted critic's), and keep it out of the "critic-side reading" wording.

### 4. MAJOR. Ascertainment: the unmodelled design effects are first order in both S21 and eligible, so the density-free ratio should be the headline; the note does not report it

**Locator.** Script lines 30-31: "Panel sites ... start with ancestral frequency y0 ~ U(0,1) (this is the flat folded density 1.86 per unit q of the c1 chain D2; ascertainment on an African male heterozygote)." Note line 96: "Panel density flat in folded frequency (1.86 per unit q, from the c1 D2 chain) down to 0, 7% of sites fixed in the ancestor and excluded, no mutations. Eligible counts at high Ne depend directly on this low-frequency end; a panel richer in rare variants would raise them." Keruru RF-16: "The 1240K panel was designed on modern variation." C1: the panel is "SNPs in present-day humans", with array and European-discovery components alongside the African-male component.

**Argument for the critics.**
- The 1240k design plausibly changes the density of sites near the boundary in Europe in the Neolithic (q below about 5%). That density is what S21 and eligible both scale with, and it is the least validated input: the model uses one African-male-derived flat density, drifted by an assumed Fst of about 0.09-0.11. It has no out-of-Africa bottleneck and no European-discovery arrays (HO and 610-Quad) that would remove sites monomorphic in modern Europeans.
- The proper critic point is that the absolute S21 is therefore uncertain by the factor by which the real boundary density differs from the model's. But this point has a limit the note should state: S21 and eligible scale together, so the ratio S21/eligible is nearly density-free. From `c1c_analysis.txt` Table 1 and 7 (tracked S21 over eligible, tracked fraction 1.00): R0 Ne 1e4 base 3,925/15,220 = 25.8%; R0 Ne 1e5 base 31.8/1,659 = 1.9%; R0 Ne 1e6 base 3.6/702 = 0.51%; R0 grow 1e4-1e6 35.2/1,359 = 2.6%; R2 Ne 1e6 base 25.8/540 = 4.8%. Day: 21/16,299 = 0.129% (or 21/22,428 = 0.094% on all eligible). No base cell reaches Day's ratio. The only cell in the same range is R0 Ne 1e5 with eps 1e-3: 58.8/45,340 = 0.130%. That is a notable coincidence of one assumed error rate and one Ne, not a fit, but it is the closest the grid comes to Day's table on a density-free quantity.
- So the answer to "do ascertainment and the 1240k design bias toward no fixations in a way not modelled" is: possibly, in the absolute counts; but a density change cannot move the ratio, and the ratio is where Day's table differs from every no-error cell. This is a point for the critics (the table has the signature of an inflated eligible set), and a point against the idea that ascertainment alone rescues the critics at Ne 1e4.

**Where this cuts against the critics.** Day's own near-fixed completions are mostly ascertained African-discovery sites in the 90-99% band (C1 point 2: D2 enriches 10-90% starts and suppresses >=90% by 5-30x). The C1 chain, with the same density idea, reproduced Z23046531's 17,806 newly-100% loci within 1.3x at Ne 1e4 (`R4-B3b-C1.md` line 52). That is an independent anchor that favours Ne near 1e4 for the panel's near-fixed behaviour. I did not run the equivalent for Ne 1e5. It should be run, because it tests the note's "Ne >= 1e5" reading on a statistic Day published with large counts.

**Fix.**
- Add the S21/eligible ratio column to Tables 1 and 7 and state Day's 0.129% (tracked) beside it.
- Run the two-period newly-100% statistic of Z23046531 (window 240-280 generations, sizes 1,372 / 680) in the C1c panel at Ne 1e4 and 1e5. If Ne 1e5 gives about an order of magnitude fewer than the observed 17,806, that is a Day-favouring constraint on the Ne reading; if it does not, the critics' reading gains a constraint. Either way it is a second equation in the same two unknowns.
- Add the out-of-Africa bottleneck and a "European-discovery arrays remove modern-monomorphic sites" variant as density sensitivities, clearly labelled assumptions.

### 5. MAJOR. The 0.1% error result is the one pre-registered prediction that flipped to the critics' favour, and it is missing from the verdict and the headline; its single assumed value is not anchored to data that are already local

**Locator.** Note line 59: "Held for the base grid (0/44), refuted when an error rate is added: R0 Ne 1e5 and R2 Ne 1e6 at eps 1e-3 pass the three numbers (but not the profile or start table)." Note line 52: "A 0.1% false-minor-call rate inflates eligible 4-27x and pushes the pre-7000 share to 0.98-0.997, as in Day's table (0.9986) ... The 1e-3 value is an assumption, not a measured AADR error rate." Note line 89 (critics): "the pre-7000 cluster is plausibly dominated by old-bin sampling and assay error, not by a burst of fixation." Note line 76 (verdict): "The model is still not a valid null for Day's table (0/44 gate; profile TV >= 0.56 ...; eps variants pass only the three summary numbers)."
Script line 288: `xe = x * (1 - eps) + (1 - x) * eps if eps > 0 else x`.

**Argument for the critics.**
- Day's table is 99.86% pre-7000. In the note's grid, the only mechanism that produces that share together with an eligible count above 10k is the error term (0.917-0.997 with eligible 10k to 61k), and no sampling-only variant does it (kappa variants lower the share, to 0.37-0.84). That is the critics' strongest mechanical story: most of the 22,428 "fixations" are sites that are 100% all along and appear polymorphic in a deep old bin through a few false minor calls, then get dated to the oldest bin where a 100% sample appears. The same table has 21 in the signal class.
- It also matches the density-free ratio of Finding 4 (0.130% against 0.129%) at R0 Ne 1e5.
- The only value tried is 1e-3. The note says it is not measured, but the data to anchor it are already on disk: the anno header (verified, columns 34, 36, 37, 38 of the v62 `.anno`) has "Damage rate in first nucleotide on sequences overlapping 1240k targets", "ANGSD MOM 95% CI" and "hapConX 95% CI" contamination estimates, and "Library type (minus=no.damage.correction ... plus=damage.fully.corrected ...)". These give a per-bin share of damage-uncorrected libraries and a contamination estimate, from which a per-bin eps range could be set without any new download.
- The combination variant `k0.5e1e-3` was run (`c1c_analysis.txt` Table 7) but is not in the note's variant table. It matters: with kappa 0.5 the error term does not rescue anything (S21 15-20k at every Ne).

**Where this cuts against the critics.** The eps cells that pass the three-number gate are the high-Ne cells (R0 Ne 1e5, R2 Ne 1e6). At the textbook Ne the same eps gives S21 4,217 (R0) and 2,411 (R2) with eligible 61k and 20k. So the error term helps the critics only conditional on the Ne claim, as the note says in other words. The profile (94% of events in the 10000+ bin) and start table (99.8% in the top band against 79.2%) still fail. Symmetric flat miscalls are one error type; contamination by modern Europeans adds the allele that is fixed in the modern bin, which pushes old bins toward 100% and works against eligibility (hypothesis, not tested).

**Fix.**
- Put the eps result in the verdict and the summary line, with its conditions: "with a 0.1% false-minor-call rate (assumed), two high-Ne cells reproduce the three summary numbers and the density-free ratio, not the profile".
- Run eps in {1e-4, 3e-4, 1e-3, 3e-3} at Ne 1e4, 1e5 and 1e6 (post hoc), and add an eps set from the anno damage and library-type columns per bin.
- Show `k0.5e1e-3` in the variant table.

### 6. MINOR. Verdict: reproducibility should lead, and the Day-side bullets are stated without the gate caveat that the critic-side bullets carry

**Locator.** Note line 82, first Day bullet: "The 21 is not an artefact of sparse calls: at real AADR depth and with the Neolithic and Bronze Age replacement included, the neutral expectation at the textbook Ne = 1e4 is thousands, and replacement does not remove the gap". Note line 76: "The model is still not a valid null for Day's table ... Neither "neutral predicts ~0" nor "deficit vs neutral" is supported without fixing Ne." Script line 43: "PRIMARY, the only dating consistent with Day's profile in c1b". C6 file: abstract's "99.8% ... within a single 2,000-year window (8000-10000 BP)" is 53.6% in the table; five different fold figures.

**Argument for the critics.**
- Day's method and code are unpublished, the "tracked" threshold is unstated, and 44 of 44 cells fail the note's own validity gate. The reading used (E1-T2) was chosen because it is the one most resembling Day's profile (script line 43), and it still has TV distance 0.56-0.76. A statistic that no implementation of its stated procedure on the real call depths reproduces cannot be a measurement of anything, including a Holocene Ne. The note says this once, in the C6 verdict line; it then writes the Day-side "who this helps" bullets as unconditional findings ("the neutral expectation ... is thousands") from the same invalid model.
- The honest asymmetry check: the critic-side bullets each carry a caveat (eps assumed; passing cells fail the profile). The Day-side bullets mostly do not.

**Where this cuts against the critics.** The model does give a robust one-sided fact: any cell that matches Day's eligible count at base (R0/R1/R2/R3 at Ne 1e4) has S21 two orders too high, and every sampling variant that reproduces Day's tracked fraction (post hoc min-depth, kappa 0.5 and 1 with m = 20) gives 840 to 5,000. That is the strongest part of the Day-favouring result; it should be stated as the model-robust residue.

**Fix.**
- Open §6 with: "The 21 cannot be used as a measurement by either side; the Ne map below is a model-conditional sensitivity, and the model fails the gate."
- Add the same conditional wording to the Day-side bullets. Separate "model-robust" (matching eligible at Ne 1e4 overshoots by 190x; matching tracked fraction overshoots by 40x or more) from "model-dependent" (the Ne where 21 is reached).
- Keep the claim-file verdict as `untestable`; it is the right category.

### 7. MAJOR. The critics' own errors are only partly recorded and are not attributed, and none appears in the suggested claim edits

**Locator.** Note line 91 (the only place): "Cuts against critics: the temporal-method Ne they cite (8-10k, C5b) makes the neutral expectation 190x above 21". Note §6 (lines 75-78) suggests edits to C6 and a correction to review #4 only. `C5b` verdict: `external: pending`. `C7` external: `pending   # ... the C1c question`.

**Argument.** Equal scrutiny (AGENTS.md rule 1) requires that the critics' errors be recorded as prominently as Day's. The ones this check touches:
1. keruru, KR-03 / C5: a number "somewhere near 10⁻²⁹" built on Ne = 1e4 that keruru later withdrew; the repo's own derivation gives 1.2e-46 for the same start, an 11-order spread between the two (C5 file, "Formal statement"). Both are negligible, but the critic's figure is not reproduced. It is also a statement about intermediate starts only (Finding 3), which the post-hoc claim "the aDNA window cannot discriminate" is silent about for near-fixed starts, where the same Ne gives thousands.
2. keruru's draft: the Ne trajectory (938 to 9,835) and "roughly doubles" are used by critics to argue Ne is about 1e4 and stable, while the same draft says the figure is biased downward by replacement, relatives and power (lines 212-218). A critic position of "Ne about 1e4, and so the 21 is what neutral expects" is internally inconsistent by the check's own numbers: at Ne 1e4 neutral gives 1.5-3.9k. Nobody in `quotes-critics.md` is recorded holding that exact conjunction, but the repo's claim C and C7 verdict wording ("neutral also predicts ~0") invites it, and the note should say which critic, if any, holds it.
3. keruru RF-14 / B2e: the ratio is stated three ways (1e-4, 4e-4, 8e-4) in one draft, and the draft carries [CHECK] marks and says "Nothing here has been through a review pass." A finding that rests on it (B2e) is weaker than C5b implies.
4. keruru, same draft line 637: "Structure inflates the estimate. It does not deflate it." That is correct for a pooled island model, and it is a point against any critic who invokes structure to dismiss a low temporal Ne.
5. McCarthy: the corpus has no aDNA, Ne or C-branch quote from McCarthy (MC-01..13, RF-6, RF-7 are branches A, B, G). His only recorded slip is the 35 M versus 20 M arithmetic (RF-6, branch B3/A3), unrelated to C1c. The task framing lists McCarthy among the sources for C1c; the note cannot be faulted for omitting a position that is not in the corpus, but it should say that none is on record.

**Fix.**
- Add a short "Where the critics were wrong or unsupported" block to the note's §7 listing items 1-4 above with locators, and a line stating that no McCarthy aDNA claim is on record.
- Add to §6 suggested edits: C5 (internal: the 10⁻²⁹ and 4e-35 and 1e-46 figures do not agree and apply to intermediate starts only), C5b (the 9,835 window spans replacement; downward bias stated by author), B2e (internal inconsistency of the ratio, already flagged by harvester).

### 8. MINOR. Capture-heterogeneity "strongest lever" rests on independent modern and ancient site efficiencies, and the regime is Ne-independent

**Locator.** Note line 51: "Capture heterogeneity is the strongest upward lever on S21." Script lines 280-281: `w_anc = rng.gamma(kappa, 1.0 / kappa, size=S)` and `w_mod = rng.gamma(kappa, 1.0 / kappa, size=S)`. Raw Table 7: R0 / R2, kappa 0.5, S21 between 15,077 and 20,199 at every Ne.

**Argument.** Independent Gamma draws for the ancient and modern bins make "modern call count tiny, ancient large" cases common. The modern bin is mostly Human Origins array data (513 of 625 individuals diploid) and the ancient bins are capture, so some independence is real, but the real structure (the HO array covers a subset of the 1240k sites; the anno carries a separate HO-snpset hit column) is systematic, not a per-site gamma. When S21 is 15-20k at every Ne, the model is in a regime where the statistic measures the sampling scheme, not drift. That is useful (it tells us the 27% untracked fraction is not innocuous) but "strongest lever" is an unproved mechanism; the note itself says "I did not run an attribution test" (line 66).

**Fix.** Either remove "strongest" or run a one-factor attribution (kappa on modern only, ancient only, both). Use the anno's HO-snpset hit column to build the modern-bin subset structure explicitly.

### 9. MINOR. Sampling noise is under-modelled in a direction that could shift events toward the oldest bins (hypothesis)

**Locator.** Note line 98: "Call depth: Binomial(n, mean p) per bin (slightly over-dispersed against the true Poisson-binomial)." Keruru draft line 703 (no relatedness filtering; cemetery families).

**Argument.** Real bins contain related individuals and cemetery clusters, and the model draws independent chromosomes. Kin clustering lowers the effective sample size, raises the chance that an allele at 97-99% looks 100% in a deep bin by chance, and moves T2 to an earlier bin. That moves events out of the S21 set and into the pre-7000 set, which is the direction of Day's table. This is a hypothesis; I did not test it, and the same clustering also inflates false eligibility.

**Fix.** Add a design-effect variant (per-bin effective n = n / deff, deff in {1, 1.5, 2}) and report S21, eligible and pre-7000 share.

### 10. MINOR. Placement in "Who this helps" blurs who each result favours

**Locator.** Note line 85 (under "Day / allies"): "His own d = 0.45 does not rescue the number: it gives 739 at Ne 1e4." Note line 92 (under "Critics"): "No model, either side, reproduces Day's bin profile ... so none of these numbers should be quoted as a replication of his result."

**Argument.** The d = 0.45 result is against Day (his own parameter leaves a 35x deficit) and sits under his heading; the "no model reproduces" result is against both and sits under the critics'. A reader skimming either list gets the wrong sign. The note does say what each means, so this is presentation.

**Fix.** Move the d = 0.45 bullet to the critics' list and the "no model reproduces" bullet to a third "Both sides" block.

### 11. MINOR. Two unsourced assertions about Holocene Ne

**Locator.** Note line 88: "literature Holocene European Ne (growth, structure) is plausibly well above 1e4." The textbook 1e4 is marked "unverified" in `parameters.yaml` (C4 file).

**Argument.** The note's own critics bullet leans on a literature statement that is not retrieved or quoted anywhere in the repo, while the 1e4 baseline is also unsourced. Rule 2 and rule 8 both apply to sourcing. I have a recollection of IBD-based European Ne estimates reaching 1e5-1e6 in the last few dozen generations and of 1e4-scale long-term estimates; I have not retrieved them and they should not be cited from memory.

**Fix.** Either quote the sources (with locators) or reword to "Ne in the Holocene is not sourced in this repo; the grid brackets 1e4 to 1e6".

### 12. MINOR. Claim files affected beyond C6

**Locator.** Note §6 (lines 75-78) suggests only C6, review #4 text and "C1/C unchanged".

**Argument.** The note changes how three other claims read. C7 external `pending` (its comment points at C1c and says admixture dominates frequency change) needs the statement that C1c does not isolate drift from replacement. C4 (Ne varied 3.3-4.6-fold) is the measured constraint against hundredfold growth (Finding 1). C5 and claim C need the intermediate-start / near-fixed-start split (Finding 3).

**Fix.** Extend the suggested-edit list to C4, C5, C5b, C7 and the claim C verdict comment, using the wording of Findings 1-3.

---

## Direct answers to the five questions

1. **Ne.** Ne = 1e4 constant is not the right sole comparison for a Holocene with a census explosion, and the note's own growth rows say so (S21 15 to 35 for 1e4 to 1e6; 262-276 for 1e4 to 1e5). It is also not the right Ne to read from keruru's figures (Finding 2). But the measured trajectories (keruru, Day C4) bound the variation to a few-fold, which makes 1e6-scale growth the least supported part of the critic case. Fair summary: the deficit is about 6x to 190x depending on whether keruru's stated downward bias is applied, and zero to 12x inside a growth family that the measured trajectories do not support.
2. **Ascertainment.** Likely biases the absolute counts in ways not modelled (out-of-Africa bottleneck, European-discovery arrays), but S21 and eligible scale together, so the density-free ratio is the right headline and it favours neither side at base (Finding 4).
3. **Reproducibility.** Should lead the verdict and also qualify the Day-side bullets (Finding 6). The `untestable` label itself is right.
4. **Error rate.** Underplayed in the verdict and summary; it is the only mechanism in the grid that reproduces the pre-7000 share and the density-free ratio, but only at high Ne, with one assumed value that the local anno could anchor (Finding 5).
5. **Critic errors.** Partly recorded, not attributed, and absent from the suggested edits (Finding 7). The repo's "neutral predicts ~0" phrase is its own and is about a different start class (Finding 3).

## Suggested pre-registered follow-ups (separate commits, before running)

1. S21 by start band, and S21/eligible, from the existing raw JSON (no new simulation).
2. In-model temporal-Ne observable for each cell and window; list the cells that reproduce 8,139 and 9,835.
3. Scenarios: keruru's measured trajectory, Day's 3.3-4.6x variation, a Neolithic step.
4. Z23046531 two-period newly-100% statistic in the C1c panel at Ne 1e4 and 1e5.
5. eps scan including an anno-derived per-bin value; kappa attribution; design effect for kin clusters.
