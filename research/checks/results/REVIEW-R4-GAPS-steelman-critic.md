# Review of R4-GAPS-04-07-02: steelman from the critics' side

Reviewer stance: the most capable, honest defender of the critics and the mainstream reading (McCarthy, Mansfield, Camestros, Hancock, Nesslig20, keruru, Bowers, the Reddit/KITTENS authors). I was asked whether the check is fair to them and whether it credits Day more than he is owed. Scope: `research/checks/results/R4-GAPS-04-07-02.md`, `research/checks/gap04_weissman_barton.py`, `gap04_posthoc_concurrency.py`, `gap07_event_counts.py`, `gap02_sweep_window.py` and their `results/raw/*.out`; `docs/research/ledgers/gaps.md`; claims A3, A3a, A3x, A5f, A2e, ROOT-excluded-mechanisms; and `sources/raw/` (critics, day, sources/txt), read or grepped only, never executed.

Overall: the arithmetic is reproducible and unusually well labelled (the P1 failure is reported, post-hoc material is flagged, the brief's "R times a log factor" is corrected). I found no arithmetic error. The problems are of three kinds: (i) verdict wording that is stronger than the paper or the numbers support, in both directions; (ii) a few "credit to Day" lines that rest on comparisons which do not test what they appear to test; (iii) critic arguments in the corpus that the write-up misses. I also found one point in Day's favour that the write-up under-credits (finding 10), and I say so.

Numbers marked "reviewer scratch" were computed quickly by hand or in a throwaway session (nothing saved to the repo) and should be re-run through a script before being cited.

## Summary

- 13 findings: **7 MAJOR** (1, 2, 3, 6, 7, 9, 10) and **6 MINOR** (4, 5, 8, 11, 12, 13).
- GAP-04: 3 MAJOR, 2 MINOR. GAP-07: 2 MAJOR, 1 MINOR. GAP-02: 2 MAJOR, 2 MINOR. Cross-cutting: 1 MINOR.
- Direction of the MAJORs: findings 1, 2, 3, 7 and 9 trim credit to Day or overreach on his side. Findings 6 and 10 are mixed (6 trims an over-large "undercount" and the 22.5M figure; 10 restores credit to Day). Finding 2 also gives the critics something new and concrete.

---

## GAP-04 (Weissman and Barton finite-map cap)

### 1. MAJOR. "3.3-4.5x over the cap" and "a bound ... sits below the requirement" read as a bound; W&B give no hard bound, and the write-up's own envelope column says the requirement is inside what W&B simulate

**Locator.** R4-GAPS "Results: human scale" table (the two multiplier columns) and "Suggested verdict edits" for A: "a mainstream finite-map bound (W&B 2012) sits 3.3-4.5x below the requirement and is supply-infeasible beyond it". Also "Who it helps", Day bullet 2.

**Argument.**
- R/2 is the asymptote of an additive approximation (Eq. 7), not a ceiling. The write-up says this in the body but the verdict text and the first multiplier column use it as the cap.
- W&B's own simulations (Fig. 4 caption: Lambda/R "remaining <3 even for Lambda0/R = 10^3") and the audit's own F2 0.1 M run (2.6x R/2) exceed it.
- Against that simulated envelope, Day's readings sit at 0.54-0.76 of 3R. That is inside what the paper itself shows is achievable, though at very large supply.
- The right sentence is "above the analytic asymptote, inside the simulated envelope, and dependent on supply". "Sits 3.3-4.5x below the requirement" would be quoted by a reader as "mainstream theory forbids Day's rate", which W&B do not say.
- The two ends of the same paper (analytic R/2, simulated up to ~3R, a heuristic log growth above R/2 that the authors say "remains to be carefully investigated") span a factor of ~6. A single "x over R/2" headline hides that.

**Fix.**
- Make the primary column "x over the W&B simulated envelope (3R)" or show both side by side with equal prominence.
- Reword the A comment to: "the 17.5-20M all-fixations reading needs Lambda/R = 1.6-2.3, above the Eq. 7 asymptote (0.5) but inside W&B's simulated range (<3), and only at supply Lambda0/R >~ 30-300".
- Drop "bound" and "cap" from verdict cells; use "asymptote of the additive approximation".

### 2. MAJOR. The table omits Day's own adaptive scenario, which lands about 22x below R/2 with about 5% interference; the "cuts in Day's favour" line is a credit to a reading Day himself abandons

**Locator.** R4-GAPS human-scale table; "Who it helps", Day on node A; the tally paragraph ("GAP-04 both"). Day source: `sources/raw/day/zenodo-18165980.txt` line 66: "Even if 99% of divergence is neutral, 200,000 fixations remain required." `gaps.md` GAP-01 notes that Day concedes neutral fixations "are the great majority" (blog 2026-05-07), and H1 limits Term 3 to adaptive substitution.

**Argument.**
- The table prices 15M, 17.5M, 20M and 205M as if every difference were a selective sweep. W&B apply only to adaptive substitution. Neutral fixation proceeds at k = mu regardless of map length.
- The row that applies W&B to *Day's own* adaptive count is missing: 200,000 fixations (his "99% neutral" case). Reviewer scratch: 200,000 / 252,000 = 0.79 per generation; R/2 = 17.5-19; so ~22-24x below R/2 (28x at 325,000 generations); Eq. 7 interference loss 2*Lambda/R ~ 4.5%.
- So on Day's own fallback adaptive scenario the finite-map cap is not binding, and the "channel capacity / Hill-Robertson limits parallelism" leg is negligible. This is the most direct application of W&B to a number Day wrote down.
- The all-fixations reading is the one where W&B "favour" Day, but only conditionally: "if every difference were adaptive, mainstream theory would struggle". Nobody holds the premise, and Day himself disowns it when pressed. The write-up says this in one bullet; the tally still gives GAP-04 a Day leg at equal weight to the critics' leg.
- The ">= 95% of U_tot" supply figure (finding 3) then reads as a reductio of the premise, not as a point for Day.

**Fix.**
- Add the 200,000 / 252,000 and 200,000 / 325,000 rows with the source locator.
- Recast the Day credit as "conditional on the all-fixations premise, which Day concedes (blog 2026-05-07; Z18165980 line 66 'Even if 99% ...')".
- Keep the tally "Both" if desired, but weight it: Day leg = conditional, critics leg = unconditional at every adaptive count in the corpus.

### 3. MAJOR. "Supply-infeasible beyond it" (U_b of 95% to 1,160% of all new mutations) depends on a by-eye Fig. 4 reading at different s and R, times an e^(4*Lambda*s) factor far outside its validated range, and on an N_e choice that favours Day's side

**Locator.** R4-GAPS "Beneficial supply needed" table; P8 "HELD"; Suggested edits for F2 and A ("supply-infeasible beyond it"); script `gap04_weissman_barton.py` section C, `gap04.out` section C.

**Argument.**
- (a) **Transplanted curve.** Lambda0/R = 30-300 is read by eye from Fig. 4, which is s = 0.05, R = 1 M, N = 10^2-10^6. The target is s = 0.001-0.01 and R = 35 M (R/s = 3,500-35,000 against 20). The write-up gives +-2x on the reading but not for the change of s and R/s. Its own section D shows the growth bound depends on log(Ns).
- (b) **Extrapolated exponential.** The factor e^(4*Lambda*s) (Eq. 8, loosely linked loci) is checked by W&B only for sR << 1 and complete recombination. F2 validated Eq. 1 only to Lambda0 ~ 0.63. The human target has Lambda ~ 69. At s = 0.01 the factor is e^2.8 and at s = 0.1 it is 10^12. That is the entire source of the "unreachable" cells.
- (c) **Wrong constraint.** This exponential is the soft-selection speed limit on the fitness variance in W&B's polygamous model. It is not a finite-map effect. Folding it into a "finite-map limit" check mixes two constraints and overstates what a map-length cap does. The finite-map-only reading (Eq. 7 without the exponential) would need Lambda0/R ~ 30-300, i.e. 2-4 orders of magnitude less supply at s = 0.1 than the table shows.
- (d) **N_e choice.** The table uses 10^4 as the "realistic" value and 10^5 as sensitivity. GAP-07 in the same write-up uses 1.98 x 10^5 (Yoo) for the ancestral population, and `parameters.yaml` lists 132k-198k. Reviewer scratch: at N_e ~ 2 x 10^5 and s = 0.001-0.01 the U_b needed scales as 1/N_e to ~2-21 per haploid genome, i.e. ~5-58% of U_tot, not "~95% to 1,160%". The falsifier for P8 was "<10% at any s" at N_e = 10^4, which was chosen to be Day-favourable for this test.
- (e) The yardstick U_tot = 36.5 counts all new mutations including those in neutral DNA. A beneficial share of 5-50% is already absurd, so the qualitative conclusion survives; the quantitative table does not deserve three significant figures.

**Fix.**
- Present the supply result as an order-of-magnitude statement with separate columns for (i) Eq. 7 only (finite-map) and (ii) with the e^(4*Lambda*s) soft-selection factor, flagged as extrapolated.
- Add the N_e = 2 x 10^5 row beside 10^4 and 10^5.
- Replace "supply-infeasible" with "requires a beneficial supply of order 10-100% of the total mutation rate under W&B's soft-selection model; the exponent is extrapolated".
- Note that P8's falsifier was set at the favourable N_e.

### 4. MINOR. The real-genome caveats leave out standing variation, soft sweeps, polygenic adaptation and the DFE correction that cuts against the critics; "helps Day modestly" is unsupported

**Locator.** R4-GAPS "Caveats" (GAP-04) and "Who it helps" critics bullet ("interference costs <= 23% at 10^6").

**Argument.**
- W&B is a new-mutation, hard-sweep, constant-s model (the paper calls it a "best-case scenario"). Standing variation, soft sweeps and polygenic frequency shifts (no fixation needed) are not in it. All of them reduce the relevance of any fixation-rate cap to the biology. The caveats section does not name them; the brief asked.
- To be even-handed in the other direction: the paper's Eq. 13 for an exponential DFE gives R/4, not R/2. The write-up mentions it only in the source list. Applied to the headline it doubles every "x over cap" figure (6.6-9x for 15-20M), and it raises the critics' interference loss at K_a = 10^6 from 21-23% to ~30% (reviewer scratch: 1/(1 + 4*0.105) = 0.70). The critic-side line "<= 23%" is therefore a fixed-s number; a realistic DFE gives "<= ~30%". The conclusion (not binding at 10^3-10^5, modest at 10^6) stands.
- "Background selection would add interference, which helps Day modestly" has no source or number in the check. BGS lowers N_e at linked sites; W&B do not model it. Say "unquantified".

**Fix.** Add a one-sentence caveat naming standing variation, soft sweeps and polygenic adaptation as outside W&B (direction: reduces the cap's bite). State Eq. 13 numbers for the human table (direction: tightens it). Replace "modestly" with "direction only; not quantified".

### 5. MINOR. The post-hoc "33-67x Day's 230" uses the R/2 asymptote, which is the least reachable rate; the relevant comparison is concurrency at the GAP-01 rates, and that is not tiny next to 230

**Locator.** R4-GAPS "POST HOC" paragraph and the Gc suggested edit; `gap04_posthoc.out`.

**Argument.**
- Concurrency at R/2 is a ceiling of ceilings that needs unreachable supply (finding 3). At the rates the critics actually propose, reviewer scratch with the same t_mid = ln 81 / s = 439 at s = 0.01: K_a = 10^5 gives 0.40/gen x 439 ~ 170 concurrent active-zone sweeps; K_a = 10^6 gives ~1,700; K_a = 10^3-10^4 gives ~2-17. So Day's 230 is within a factor of ~1-2 of the concurrency needed at K_a ~ 10^5.
- That is honest information for Day: 230 is not contradicted as a *number* at the upper GAP-01 rows; it is contradicted as a *cap*, because W&B and part D of G1 show nothing caps concurrency near 230. The write-up conflates the two readings under "no support for 230".
- The caveat "overstated at s >= 0.05" misses that at s = 0.01 the e^(-4*Lambda*s) factor is already 0.47-0.50 (from the script's own output), so the realised rate at R/2 would be about half there too.

**Fix.** Report concurrency at the GAP-01 K_a rows alongside R/2, and word the Gc comment as "no support for 230 *as a cap*; the number is of the same order as the concurrency implied by K_a ~ 10^5". Extend the exponential-factor caveat to s = 0.01.

---

## GAP-07 (indel and SV event counts)

### 6. MAJOR. The "1.2-13.5x undercount of observed indels" mixes three separate factors and an uncertain reading of CSAC; "~5 million in each species" is probably not the right per-lineage figure, and the "cuts against the critics' method" sentence is misdirected

**Locator.** R4-GAPS GAP-07 results table (row "indel events"), "Procedure/Results" bullet "Indels: rate-based counts fall 1.2-13.5x below ...", "Who it helps" Day bullet 4, "Fidelity flag", and the suggested A3/A3x/A3a edits. Script `gap07_event_counts.py` section D. Source: `sources/raw/sources/txt/CSAC2005.txt` lines 12, 456-458, 492-493, 1986-1988.

**Argument.**
- **Decomposition.** The range 1.2-13.5x is observed / rate-based at its two extremes: 2.5M / 2.16M and 5M / 0.37M. It is the product of three known effects, not an indel finding:
  - the *clock tension* shared by all classes (M1 / M3 = 0.53 for SNVs, indels and SVs alike; 9.2M against 17.5M for SNVs): ~1.9x;
  - the *rate-source spread* (Besenbacher 4.5 against Kloosterman 1.47 per haploid genome): ~3.1x;
  - the *reading* of CSAC (2.5M against 5M per lineage): 2x.
  - The product 1.9 x 3.1 x 2 ~ 11.6, close to the 13.5 extreme. After the clock-free calibration (M3), Besenbacher's rate gives 2.16M against 2.5M: within 16%.
- **Reading of "events".** The abstract (line 12) says "five million insertion/deletion events" for the whole catalogue. Lines 492-493 compare "~5 million" with "~35 million" substitutions, and the 35M is the *total* across both lineages. Only line 458 says "~5 million events in each species". Independent evidence favours the total reading:
  - the germline indel:SNV rate ratio is 0.04-0.12 (Kloosterman, Besenbacher; Nachman and Crowell ~0.1);
  - CSAC's ratio is 5/35 = 0.14 on the total reading but 10/35 = 0.29 on the per-species reading, 2.4-7x above every germline ratio.
  - The write-up already used the 5/35 vs 4.65/37 match in `gaps.md` as a consistency argument; it then adopts the reading that breaks it.
- **What an "event" is.** CSAC Methods (lines 1986-1988): indel events "were parsed directly from the BLASTZ genome alignment by counting the number and size of alignment gaps". A gap count from a 2005 draft chimp assembly is an upper bound on mutation events: complex events split, sequencing errors add, and the human/chimp "insertion relative to the other genome" labelling mixes ins and del on either lineage.
- **Consequence for the headline.** The "observed basis 20.0-22.5M" upper end is the least supported; the lower end (20.0M) is the better-supported one. 205M / events is then ~10x on the observed basis rather than "9.1-10.2x", which does not change any verdict but is the number Day would be shown.
- **Misdirected sentence.** "The rate method also under-counts ... cuts against the critics' preferred method" is not about indels. The critics' preferred k = mu SNV expectation (9.7M) already undershoots 17.5M by ~1.9x (the B4a/GAP-06 tension, which the write-up cross-references). Because M1 totals are 96% SNV, a 13x indel undercount would move the M1 total from ~10M to ~15M (205M / 15M ~ 14x vs 21x): the unit conclusion is insensitive to it.

**Fix.**
- Report the indel comparison as a decomposition (clock ~1.9x, rate spread ~3x, CSAC reading 2x) and state the clock-free Besenbacher match (2.16M vs 2.5M).
- In the "Fidelity flag", add that the abstract and the 5M-vs-35M sentence support the total reading and only line 458 says "in each species"; say it is unresolved, not that A3/A3x misread.
- Present the observed basis as 20.0M (total reading) with 22.5M as an upper bound only.
- Replace "cuts against the critics' preferred method" with "same clock tension as B4a; the unit conclusion is insensitive to it".
- Optionally cite that CSAC counts alignment gaps.

### 7. MAJOR. The "Day (partial)" credit for SV base pairs compares a k = mu estimate for de novo euchromatic SVs with a Yoo number that is a different kind of quantity, and the point was already made by McCarthy

**Locator.** R4-GAPS GAP-07 "Procedure/Results" bullets on SV base pairs (347/517/666/922 Mb against 327 Mb; "327/517 ~ 0.6 ... plausible"), "Who it helps" Day paragraph ("Under k = mu, SVs alone should deliver ~0.35-0.9 Gb ... not an artefact"), and gaps.md suggested update 3 ("Yoo's megabases correspond to few, large events"). Sources: `sources/raw/sources/txt/Yoo2025.txt` line 87; `A3a-205m-headline.md`; `A3x-bp-vs-events.md`.

**Argument.**
- (a) **What SDRs are.** Yoo (line 87) defines SDRs as sequence that "failed to align or was inconsistent with a simple one-to-one alignment", and says the 5-15x gap divergence is "due to rapidly evolving and structurally variant regions ... as well as technical limitations of alignment in repetitive regions". The SDRs "included centromeres, acrocentric short arms and subterminal heterochromatic caps". These are satellite and heterochromatin regions that the pedigree SV callers (short or mid-read, euchromatic) exclude, and Collins says its estimate "certainly underestimates". The 517 Mb (k = mu) and the 327 Mb (SDRs) cover mostly different parts of the genome. A match, or a ratio of 0.6, carries no evidential weight.
- (b) **Wrong denominator.** 327 Mb is an average over all ape lineages. Day's own figure for the human-chimp comparison is "approximately 187 megabases" (A3a, MITTENS 3.0). If that is the pair total, per-lineage human SDR mass is ~90 Mb and the k = mu number overshoots by ~5x instead of "0.6". I could not verify whether 187 is per pair or per lineage; the write-up should say which.
- (c) **Heavy tail.** The 4.1 kbp mean in the SV bp rate rests on 41 events, one of 327 kbp, which is about 31% of the total (reviewer scratch: 327 / (41 x 25.6 kbp)). The bp rate is therefore a one-event-sensitive estimate. (The coincidence of "327 kbp" and "327 Mb" in the text is accidental and could confuse a reader.)
- (d) **Already said.** McCarthy (MC-11, para 26) said "a single mutational event can cause hundreds, thousands, or even millions of base-pair differences"; the Reddit commenter in thread 1wv4zeg said a 1-Mb inversion "is a single mutational event". Crediting Day with "the base-pair magnitudes are real" credits a fact the critics stated first. The contested point (does it change the fixation count) goes to the critics.

**Fix.**
- Remove the "Day (partial)" bullet, or state it as "no information: the two quantities cover different sequence".
- Remove or relabel "327/517 ~ 0.6 plausible".
- State which of 187 (pair) and 327 (cross-ape average) is the right comparator, and show both.
- Add the single-event sensitivity of the 4.1 kbp mean.
- Credit McCarthy for the hundreds-to-millions-of-bp point.

### 8. MINOR. Critic arguments in the corpus that the write-up omits; and "filled by the audit rather than by the critics" is slightly too strong

**Locator.** R4-GAPS GAP-07 "Who it helps" (critics paragraph).

**Argument.**
- Fun-Friendship4898 (Reddit 1wv4zeg) identified the specific construction error: 410M = 35M SNVs plus 2 x 187 Mb, i.e. doubling an SDR figure and adding it to a count; that SDRs "are spans ... difficult or impossible to align"; that "a good chunk of those 35 million SNVs are already contained within those SDRs" (double counting); and that the true nucleotide difference inside an SDR "might be tiny".
- Nesslig20's thread (ps-topic-18094) relays Panda's Thumb (Neukamm) that gap divergence is dominated by InDels spanning many bp, and quotes Yoo "focused on segments that could be reliably aligned".
- Mansfield (MF-06) gave "around 25 million give or take" (uncited) which is within ~25% of the audit's 18-22M. It is not an independent derivation, but "no independently derived event count" is better phrased "no *sourced* event count".

**Fix.** Add one line crediting the Reddit commenter for the double-counting and overlap points, and the Panda's Thumb relay; soften "filled by the audit rather than by the critics" to "first sourced by the audit".

---

## GAP-02 (sweep detection window)

### 9. MAJOR. Scan candidate counts are used as a comparator for real sweep numbers; the "tension for K_a >= 10^5" and the "722 / 5,110 matching" rest on threshold-limited lists, and the standard confounders are not in the caveats

**Locator.** R4-GAPS GAP-02 "Results" (the line "K_a at which completed strong sweeps would match Akey's replicated 722"), "Answer to the brief" bullet 2 ("Scenarios with >= 2 x 10^4-2 x 10^5 completed strong sweeps per lineage predict more than the 722 replicated scan regions ... in tension with the data"), P3 "HELD", Caveats. Sources named there: Voight 2006, Akey 2009, Yoo 2025.

**Argument.**
- Voight's candidates are 100-kb windows "in the highest 1% of the empirical distribution", and Pickrell uses a 1% tail. A fixed-tail outlier list returns about the same number of hits whether there are 50 or 5,000 true sweeps. Akey's 5,110 union and 722 replicated count overlaps between differently powered scans with, in Akey's own words, "poor concordance". Neither is a count of real sweeps. The write-up says "partly set by the outlier threshold" but then uses the numbers as a threshold in P3 and in the "K_a at which ... would match" lines.
- The genuinely informative constraints are the Hernandez trough test (no excess diversity trough around amino-acid substitutions relative to synonymous) and Murphy 2023 (BGS-only fit; adding sweeps "did not improve"). These bound a *combined* rate x strength and only for classic sweeps at coding substitutions.
- The caveats list omits: demographic confounding (the out-of-Africa bottleneck and expansions distort the SFS and iHS nulls in both directions, which is why Day's own "Tajima's D is close to zero genome-wide" is not a test of anything); background selection as both a mimic and a power-reducer; polygenic adaptation, which needs no sweep; and the distribution of s (Akey: power only at 4N_e*s ~ 400, i.e. s >~ 0.01 at N_e = 10^4, so a DFE with most mass below that is invisible by construction).
- Direction: this weakens the write-up's concession to Day ("real evidence against large strong-sweep counts"), not its defence of the critics. It leaves Hernandez and Murphy as the actual evidence and moves the "tension" from counts to those two.

**Fix.**
- Delete the "K_a that matches 722 / 5,110" calculation, or relabel it "illustrative only; candidate lists are threshold-limited".
- Restate P3's consequence as "in tension with Hernandez/Murphy for classic sweeps", not with scan counts.
- Add to Caveats: demography, BGS, polygenic adaptation, the s-dependence of power, and that the lists are FDR-uncontrolled.

### 10. MAJOR (in Day's favour). The write-up misses that the signature argument is aimed at hitchhiking, which some critics did argue; that is the part of the argument that survives

**Locator.** R4-GAPS GAP-02 "Who it helps" Critics paragraph ("None has made the window argument ... their argued position, 'most differences are neutral', is what the absence of signatures predicts"); `ROOT-excluded-mechanisms.md` row 6. Day source: `sources/raw/day/zenodo-18452504.txt` lines 325-331, in context lines 310-335 ("Linkage and Hitchhiking"). Critic sources: `arctic-tree-1wv4zeg.json` ("Ignores how selective sweeps cause many fixations, mostly for neutral variation"), `arctic-tree-1wss2wj.json` ("ignores that selective sweeps result in the fixation of many loci at once, most of them neutral"), KITTENS in `arctic-title-MITTENS.json` ("the claim that human neutral fixation is mostly hitchhiking ... does not follow ... hitchhiking is confined to the neighborhood of a sweep").

**Argument.**
- The 3,200 sweeps in §4.3(4) come from Day's block calculation (3,200-32,000 independent blocks of 0.1-1 Mb), not from an adaptive count. The passage answers the objection that hitchhiking carries most of the 20M differences.
- That objection *was* made by critics (the two Reddit commenters above). KITTENS answered with a confinement point, not a signature point. So the claim "critics have not engaged §4.3(4)" is true, but the argument is relevant to those critics, and the write-up never says that a hitchhiking-heavy account of the neutral fixations is exposed to Hernandez and Murphy.
- Honest assessment: the audit's window arithmetic (39-98 detectable sweeps for Day's own 3,200) correctly removes the *saturation by count* inference. It does not rescue the hitchhiking-as-main-source account, for which the diversity data (Hernandez; Murphy; Yoo's tens of candidates per taxon) are a real problem. A critic who says "sweeps carry most fixations" has to answer that; a critic who says "most differences are neutral and drift fixed them" does not.
- The "Who it helps" tally "Both" is right, but the Day leg is described only as "classic sweeps are rare". It should say that the rarity is specifically a problem for the hitchhiking-heavy variant of the critic position.

**Fix.** Add a bullet under "Who it helps": "Day: the signature argument is a valid objection to hitchhiking as the main source of lineage fixations (argued by two Reddit commenters); the window removes the count-saturation inference but not the Hernandez/Murphy diversity constraint". Add a cross-link to ROOT-M row 6. Note that the 3,200 comes from the block count.

### 11. MINOR. Count-based E_detect ignores footprint; a genome-coverage version is easier to compare with the data and may change the K_a >= 10^5 verdict

**Locator.** `gap02_sweep_window.py` `E()`; R4-GAPS GAP-02 results table.

**Argument.**
- Day's own footprint is r/s ~ 0.1-1 Mb. Reviewer scratch: his 39-98 in-window sweeps cover ~4-100 Mb, 0.1-3% of 3.1 Gb. That is consistent with "diversity relatively uniform" for his own number.
- For K_a = 10^5 (E = 1,111-3,968 with f_strong 0.28-1) the same footprints would cover 110 Mb up to the whole genome. Hernandez cites ~10% of the genome (310 Mb) as affected by recent sweeps. That implies ~78-280 kb per sweep to match 10% — inside Day's footprint range.
- So a coverage comparison may put K_a ~ 10^5 inside, not outside, the data. Whether it is requires the s distribution and the Hernandez source (which I have not re-read). This directly bears on the "GAP-01's high-a_nc rows (>= 10^5) are in tension with the data" sentence.

**Fix.** Add a coverage column (footprint 0.1 and 1 Mb) and compare with Hernandez's ~10%. Soften the K_a >= 10^5 sentence until that is done.

### 12. MINOR. Window and soft-sweep parameters: the "39" lower end is unsourced and the soft-sweep power 0.2 is invented

**Locator.** R4-GAPS GAP-02 results first row (39-98), Procedure (W = 4,000 unsourced; q_soft = 0.2 assumption); P1.

**Argument.**
- The only sourced window is 10,000 (Hernandez citing Przeworski, whose text was not read). The 4,000 lower end is described as "unsourced", yet the headline "39-98" and the P1 band were built on it. A reader will quote "39-98" as a result.
- Windows depend on the statistic and on N_e history (a longer ancestral N_e means a longer window for older sweeps), so 10,000 may be low as well as high. A window of 20,000 doubles E (still "hundreds"), so the qualitative result is robust either way.
- q_soft = 0.2 is also invented; it only matters in the f_soft = 0.5 sensitivity rows.

**Fix.** State the headline as "98 at the sourced window; 39-200 under a 4,000-20,000 sensitivity", mark 4,000 and 20,000 as unsourced, and mark q_soft as an assumption wherever it appears in a table.

---

## Cross-cutting

### 13. MINOR. Parameter-choice scorecard and tally

**Locator.** R4-GAPS "Tally"; the three Procedure sections.

Which choices lean which way (my reading):

| choice | favours | where |
|---|---|---|
| Headline multiple against the R/2 asymptote instead of the simulated envelope | Day | GAP-04 (finding 1) |
| N_e = 10^4 as "realistic"; falsifier set at that N_e | Day | GAP-04 (finding 3) |
| Fig. 4 transplanted from s = 0.05, R = 1 to s <= 0.01, R = 35 M; e^(4*Lambda*s) extrapolated | Day | GAP-04 (finding 3) |
| Omitting Eq. 13 (R/4) from the human table | Day (understated) | GAP-04 (finding 4) |
| Fixed-s interference loss "<= 23%" | critics (understated by ~7 points) | GAP-04 (finding 4) |
| Post hoc concurrency at R/2 | critics | GAP-04 (finding 5) |
| "5M in each species" reading and the 22.5M upper end | Day (smaller 205M / events ratio) | GAP-07 (finding 6) |
| "Day (partial)" credit for SV bp | Day | GAP-07 (finding 7) |
| Unsourced window 4,000 and q_soft 0.2 | critics (lower E) | GAP-02 (finding 12) |
| Scan candidate counts as comparator | Day | GAP-02 (finding 9) |
| Missing hitchhiking link | critics (credit to Day omitted) | GAP-02 (finding 10) |

Net: the choices are not systematically one-sided; the GAP-04 and GAP-07 choices lean toward Day, and the GAP-02 lower-window and soft-sweep choices lean toward the critics. The cumulative effect on the *labels* is small, because the underlying conclusions (the k = mu unit argument; no saturation at Day's own number; interference small at adaptive rates) survive every adjustment above.

**Suggested tally changes.**
- GAP-04: "Both" is acceptable only if the Day leg is marked *conditional on the all-fixations premise Day concedes* (finding 2).
- GAP-07: "Critics" holds; credit to Day is nil, not "partial" (finding 7).
- GAP-02: "Both" holds; the Day leg is specifically against hitchhiking-as-main-source (finding 10) and the critics' leg is the saturation inference.

---

## Where the write-up is sound and I would leave it alone

- The brief correction: the main W&B cap has no N, U or s dependence; the log appears only in the heuristic growth bound above R/2.
- Reporting that W&B's Eq. 7 reproduces F2 at 1.5 M within 6% (fitted c = 1.79 against 2), that Eq. 1 reproduces the free-recombination cells within 2 SE, and that the functional form fails at 0.1 M (c = 1.02, chi-squared 318). The P1 failure is reported straight, and the "post hoc" label on the tolerance excuse is right.
- Treating clonal runs as outside W&B's domain rather than as a test of the paper.
- The critic-side finding that at every GAP-01 rate interference is small (<= 0.2% at 10^4, <= 23-30% at 10^6) and the supply needed is <= 0.4% of new mutations (with the caveat that it inherits GAP-01's noncoding uncertainty). Here the critics' position, "recombination makes parallel adaptation feasible" (KITTENS section 8 argued it qualitatively), is supported, and Day's "channel capacity" is correctly bounded by map length in Morgans.
- The GAP-07 core: 205M is a bp count; event counts of ~10M (k = mu), 18-20M (clock-free) and ~20M (observed) differ from it by ~10-21x, and the 5.3x worst corner still leaves the unit argument intact. Day conceded this in A3b section 7.3.
- GAP-02's internal result: Day's 3,200 sweeps over 325,000 generations predict only dozens to ~100 detectable completed sweeps, which is what he says the scans find. The saturation inference does not follow from his own number.
- Day-favouring points the write-up correctly keeps: classic sweeps are rare (Hernandez, Murphy, Yoo's tens per taxon); the bonobo 326,000 *selective* fixations are not rescued by the window; the all-fixations reading cannot be sustained by W&B-type theory; the F2 "human-scale untested" caveat is reduced but not removed for readings that exceed R/2.
- The access and pre-registration discipline: Przeworski's text, Sabeti 2006, Jonsson 2017, Kong 2002 and Matise 2007 are flagged as not read; hashes are listed; the "0.1 x 4N_e" bound is flagged as unsourced.
