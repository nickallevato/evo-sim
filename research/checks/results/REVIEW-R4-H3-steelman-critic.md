# Review of R4-H3 (H-human): steelman from the critics' and mainstream side

Reviewer stance: the most capable, honest defender of the critics (Nesslig20, KITTENS, Gutsick Gibbon / Hancock, Mansfield, Camestros, McCarthy) and of the mainstream resolutions of Haldane's dilemma (Wallace, Nunney, Maynard Smith, Sved, Kimura and Crow, Nei, Felsenstein, Ewens, Matheson et al.).

Scope: `research/checks/results/R4-H3-human.md` (line numbers below refer to it), `research/checks/h3_human_scale.py`, `h3_posthoc.py`, `h3_tables.py`, and the raw summaries in `results/raw/h3_*_summary.json`. Context read: claim files H, H1, H2, H5-H8; `docs/research/sources/prior-art.md` (PA-03 to PA-17, PA-36); `docs/research/ledgers/gaps.md` (GAP-01, GAP-02, GAP-04); `opponents/`; Day's Z19984826 §3.3 (pdftotext only); the Gutsick Gibbon / Hancock transcripts and the Nesslig20 thread under `sources/raw/critics/` (read and grepped only, never executed).

Overall: the arithmetic and the pre-registration discipline are good, and most of the choices that favour Day are labelled in the caveats (ceiling regulation, bin-level background selection, K = 1000, the treadmill itself). I found no arithmetic error. The problem is the gap between the caveats and the headline lines. Sections 5, 6 and 8 state "fits / does not fit" with the conditions left in §7. The mainstream resolutions are mostly neither modelled nor named. Several critic arguments in the corpus are uncredited, and one "neither side has said this" claim is contradicted by a source in the corpus. I also list, honestly, the points where the check is right and a critic should concede.

Numbers marked "reviewer scratch" were done by hand or in a throwaway session, are not saved to the repo, and should be re-run through a proper script before being cited. Items marked "recollection" are from my memory of the literature and are unverified.

---

## MAJOR findings

### 1. MAJOR. Every "does not fit" verdict is conditional on hard, treadmill selection. The conditions are in §7 only, and the mainstream resolutions are not modelled

**Locator.** §7 first caveat (line 314), §2 "Reading" (lines 145-150), §5 "Does not fit" bullets (lines 283-288), §8 ROOT-M and H rows (lines 335, 342), §6 KITTENS bullet (line 305); script `run()` lines 341-410 (`f = min(R, K/N)` then `keep = rng.random(J) < w`).

**Argument.** The model has three features that together are Haldane's premise, not a neutral test of it.

- (a) An exogenous process opens loci at rate λ, and the ancestral allele's absolute survival falls by e^{-s} per copy. Adaptation is therefore always a restoration of lost fitness.
- (b) Fecundity regulation (`f = min(R, K/N)`) comes before viability, so there is no density-dependent mortality that selective deaths could replace. Every selective death is an additional death. This is the hard-selection assumption in its purest form.
- (c) Costs add across loci (log-additive survival).

The mainstream resolutions the brief lists deny exactly one or more of these.

- Wallace and Nunney: selective deaths replace deaths that density regulation would cause anyway.
- Absolute fitness can rise without prior deterioration.
- Maynard Smith, Sved, Kimura and Crow: truncation or epistasis make costs non-additive.

The report's own §7 says "The model is the Day-favourable framing". The verdict text then drops that conditionality:

- §5 "Does not fit" says "any noncoding adaptive share a_nc ≳ 1% under hard selection at any plausible R". That one does say "hard".
- The §8 ROOT-M row says "the cost of selection binds Day's own counts and any a_nc ≳ 1%". It does not.
- §8 row H says "a_nc ≥ 1% does not fit under hard selection". That one does say "hard".

Three more problems.

1. Line 150 says "Neither side in the corpus has drawn this distinction" (treadmill versus absolute-fitness gain), and line 314 says "neither side has addressed it". This is contradicted by the corpus. Hancock, in the Gutsick Gibbon video (`yt/_Vu0ZVVjwHc.transcript.txt`, 02:08:20-02:09:03), says the cost "is important in populations that are really small... and most of the issues come from being poorly adapted to your environment... if you are a population that's well adapted... most of the selective interactions are actually competitive between individuals that are well adapted... a completely different kind of model of selection". At 02:07:18 he also separates hard selection (a cold snap) from soft (the wolf that "can only eat so many bunnies"). Nunney 2003 (H2) states the same scope limit: "soft selection is only important when natural selection is driven by intraspecific competition", and "hard selection will dominate" under directional environmental change. The distinction has been drawn by a critic, in prose. The report is right that nobody quantified it.
2. §6 (line 305) says the KITTENS clause "far weaker under soft, competitive selection" "was not tested as a persistence limit here (soft selection has no demographic cap in this model)", and then says it "stays contested" because R4-H-C2 found soft selection slower at tracking. Those are two different soft implementations. In H3's soft load, parent weights are exp(-s_d k) and are not capped by R, so soft has no cap by construction. The stage B result (soft U = 2.2 persists exactly like no load, line 194-200) then supports the clause on *cost*. In C2, soft selection chooses survivors among R·K juveniles, so the differential is capped by R. Both are legitimate modelling choices, and the report should say plainly that "soft removes the extinction cost, but whether a rate limit remains depends on how soft selection is implemented". At present a reader sees only "contested".
3. The mainstream resolutions are not named in the report at all (grep for truncation, epistasis, Sved, Kimura/Crow, Wallace, Ewens in R4-H3-human.md gives no hits except the Keightley quote). The earlier REVIEW-R4-steelman-critic (items 11-20) already asked for truncation and polygenic variants and a standing-variation start. They were not done, and the H3 report does not say so.

Honest point for Day: Nunney himself judges that hard selection likely dominates adaptation under directional environmental change, so the treadmill is not an illegitimate framing. The critics cannot simply assume it away. The issue is labelling and scope, not legitimacy.

**Fix.**
- Add a short "not modelled, with direction" table to §7: soft or density-dependent mortality (reduces cost; implementation-dependent), absolute-fitness gain (no cost), truncation and synergistic epistasis (reduces cost; R4-H-C2 shows the Fmax threshold falls from about 18 to 12 with synergistic epistasis at U = 2.2), standing variation (smaller D), polygenic shifts (no fixation needed).
- Prefix every "does not fit" line in §5, §6 and §8 with "under hard, additive, treadmill selection".
- Replace lines 150 and 314 with: "Hancock (video, 02:08) and Nunney both say this in prose; nobody has quantified it".
- Cheap run: a soft-adaptive variant using the existing parent-weight code (`soft_w`) at the same λ, with and without an R-capped differential, to separate cost from rate limit.

### 2. MAJOR. R ≈ 1.1 is Haldane's illustrative 10% translated, not a hominid fecundity. The check leads with it, and its own load results make R ≤ 1.4 incompatible with a hard load

**Locator.** §1.2 (lines 89-92), §4.1 "Haldane's own regime reproduced" (line 188), §6 Day 1 (line 293), §7 (line 316), §8 row H (line 335).

**Argument.**

- (a) Haldane's 10% is the fraction of deaths (of N per generation) that can be selective. The report converts it to ln R = 0.105 and then calls R ≈ 1.1 "Haldane's own regime". That is a re-expression of an assumption, not a fecundity estimate. The report admits "R for ancestral hominins is not sourced" (line 316), but §6 item 1 and the §8 row H then lead with the R = 1.1 result and add "Day's number holds at R ≈ 1.1".
- (b) The report's own stage B result cuts against R ≈ 1.1. With a hard amino-acid-class load (U = 0.35, Keightley 2012), R ≤ 1.42 is extinct (lines 202-206). If that load were hard, a population with R ≈ 1.1 could not exist at all. The Day-favourable reading therefore needs the deleterious load to be soft while the adaptive selection is hard. That is a coherent position (Keightley and Charlesworth both say the load is mostly soft or stabilising; Nunney says adaptation is likely hard), but it is a specific assumption, and the report never states that the 1/300 result depends on it. The same applies to U = 2.2: if it were hard, humans exist only if R ≥ 9 (about 18 offspring per female, PA-16), so the "R < 9" part of the Day-favourable list (line 288) describes a regime that cannot occur for an existing species.
- (c) Day's own later framework does not use R ≈ 1.1. Z19984826 §3.3 says "the highest-fitness individual leaves twice as many descendants as the average, which puts the aggregate smax at order unity". The report itself maps that to R ≈ 1.6-2 (§6 Day 3, line 295), where the cap is about 10 times Haldane's 1/300 (λ50 = 0.035). That is 17 times Haldane's own count, as R4-H-C2 already found. Placing "Day's number holds" next to this without comment makes the statement more favourable than the corpus warrants. Day uses two incompatible budgets.
- (d) Which R is the right one depends on the hard/soft question of finding 1. For a hard-post-regulation model, R is the *additional* fecundity physiologically available above current births, not the ratio of births to replacement. Recollection (unverified, must be sourced before use): natural-fertility foragers average about 6 births per woman and high-fertility groups (Hutterites, Aché) 8-10, which gives an elasticity of roughly 1.3-1.7. At R = 1.5 the report's own mean-field cap is 0.020 per generation (about 5,100 per lineage, D = 20), about 6 times Haldane's 1/300. For a soft or density-regulated model, R is the existing excess of births over replacement (about 3), and the cap is larger still. Neither reading is close to 1.1. Matheson et al. 2025 (PA-36), which Nesslig20 cites, measure the selective-death share at 8.5-95% against Haldane's 10%, with the caveat that it is one annual plant.

Honest point for Day: 1/300 at R ≈ 1.1 is simply ln R / D = 0.095/30 (Haldane's own arithmetic), so it is robust and not a simulation artefact (see Concessions below). The criticism is about which R is central, not about the arithmetic.

**Fix.**
- Rename the R = 1.1 cell "Haldane's assumed 10%", not "Haldane's own regime reproduced", in §4.1 and §8.
- Add one sentence to §6 Day 1: "this requires the deleterious load to be soft (finding 2b) and R to be at Haldane's illustrative value; Day's own smax ≈ 1 implies R ≈ 2".
- Add a sourcing task for R, separate for hard (fecundity elasticity) and soft (existing excess) readings, to the open items.
- Remove the "R < 9" bullet from the Day-favourable list, or add "(excluded for a species that exists)".

### 3. MAJOR. D ≥ 20 (a rare new mutation, hard sweep) is the default behind "does not fit", while the corpus and the report's own tables point to lower D for much of the adaptive count. The robustness of a_nc ≥ 1% is conditional on both

**Locator.** §1.5 (lines 120-131), §5 table (lines 267-273), "Does not fit" (lines 283-288), §6 Day 5 (line 297), §8 ROOT-M (line 342); `gaps.md` GAP-02 and GAP-01.

**Argument.**

- (a) The default column in the "does not fit" statements is D = 20 (e.g. "any adaptive count at Haldane's own R ≈ 1.1 above ~1-2×10³ (D ≥ 20)"). D = 20 corresponds to p₀ ≈ 5×10⁻⁵, a single new mutation at N = 10⁴. The report's own D = 10 column corresponds to p₀ ≈ 0.007, and the tables stop there.
- (b) Three corpus items point to lower D for a substantial share of adaptation:
  - GAP-02 (Hernandez 2011, Murphy 2023): classic hard sweeps from new mutations are rare, so most adaptation, if it exists, is soft, from standing variation, or polygenic.
  - Uricchio et al. 2019 (GAP-01): 72% of the adaptive α is weakly adaptive.
  - Hancock (video 02:12:32): "the frequency doesn't have to be very low. It could have been a neutral allele... at intermediate frequencies."
  - For an allele that was neutral before the change and then fixes, the starting frequency is weighted towards high values. By my reasoning (reviewer scratch, not verified against Hermisson and Pennings 2005), p₀ is roughly uniform on (0, 1) among alleles that go on to fix, so mean D is a few units, not 10-20.
- (c) The break-even D for a_nc = 1% is instructive. From the report's own formula ln R ≥ D·K_a/T with K_a = 1.7×10⁵ and T = 252,000: ln R ≥ 0.675·D. At R = 10, D must be ≤ 3.4 (p₀ ≥ 0.18). So the claim "a_nc ≥ 1% does not fit at any plausible R" is robust to D down to about 3-4, which is a strong statement. But it is not robust to finding 1 (soft selection or absolute-fitness gain), and a_nc itself is unsourced (GAP-01: Keightley 2005 "very low"; Murphy 2023 α < 10⁻⁹). The report says "the binding unknown is a_nc". The "Does not fit (Day's side)" label should carry the same conditional.
- (d) The credit in §6 Day 5 ("Day-favourable result nobody in the corpus has stated... credit goes to the argument's structure") sits awkwardly with the report's own §6 keruru bullet (line 301), which says KR-09 is "the one corpus statement that runs the α-type comparison". Credit to Day's structure is also thin: his argument (H §4.2) compares 487 with 20M all-differences, and the report itself says H1 disposes of that comparison. Day concedes adaptive fixations are "comparatively rare" (blog 2026-05-07, quoted in GAP-01). The a_nc ≥ 0.1% scenario is a hypothesis nobody in the corpus endorses.

Honest point for Day: lower D is not free for the human case. Site-specific beneficial supply is small (see Concessions, item c), which pushes D back up, and GAP-02 cuts both ways (hard sweeps rare implies fewer adaptive substitutions through that route, but then α should also be low).

**Fix.**
- Extend §1.5 and §5 with D = 3 and D = 5 columns, and state the break-even D at R = 3 and R = 10 for a_nc = 0.1% and 1%.
- Mark "Does not fit" bullets as "conditional on hard treadmill selection, D ≥ 5, and the stated a_nc".
- Reword §6 Day 5 to "conditional on an a_nc that no source supports; KR-09 ran the same comparison (unsourced count)".
- Credit Hancock's intermediate-frequency point (video 02:12:32).

### 4. MAJOR. Truncation selection and epistasis (Maynard Smith, Sved, Kimura and Crow, Kondrashov) are not modelled or cited, and "costs add across loci" is the model's silent premise

**Locator.** §7 simplifications (lines 319-326: "additive (log-scale) dominance only"), script header lines 41-62, `w = wa * wd` (line 406), `logwa = -s * anc` (line 394).

**Argument.** Survival is exp(-s · number of ancestral copies), summed over all open loci. That is the multiplicative, independent-loci assumption under which Haldane's costs add. The two oldest mainstream replies (PA-04 Maynard Smith 1968; PA-05 Sved 1968; PA-06 Kimura and Crow 1969; PA-15 Crow and Kimura 1979) say that when survival depends on a threshold or on synergistic interaction, one selective death removes several disfavoured alleles, so the load does not add. The report names none of this. The model also cannot test it, because cost is additive by construction. Two things make this matter.

- The R4-H-C2 epistasis run already in the repo (`R4-H-C2.md` line 60) found that synergistic epistasis lowers the hard-selection persistence threshold at U = 2.2 from Fmax ≈ 18 (multiplicative) to 12. The H3 report does not carry that over.
- Day does not accept these resolutions. His answer (Z19984826 §3.3, §3.3.1) is the Bernoulli Barrier: with n concurrent loci the coefficient of variation is 1/(2√n), so truncation selects on noise. R4-G1 and its reviews already dispute that (in Day's own multiplicative model per-locus response does not fall with n). So the H3 report is sitting on an open question between G1 and H. It should say that it takes Day's side by modelling additive cost, and cross-reference G1.

**Fix.**
- Add a line in §7: "Truncation and epistasis are not modelled: costs are additive across loci by construction. Direction: would lower the cost (R4-H-C2 line 60); Day disputes via the Bernoulli Barrier (Z19984826 §3.3.1); G1 review disputes Day's variance argument."
- Optionally, a truncation-on-polygenic-score variant of `run()` (survival depends on whether the total ancestral count exceeds a quantile), which the earlier review already asked for.

### 5. MAJOR. The hard-load results are presented as Day-favourable outcomes although they depend on K = 1000 and on a uniform s_d = 0.02, and hard accounting of U = 2.2 is the thing the cited literature rejects

**Locator.** §4.2 (lines 207-210), §4.6 S5 and D3 (lines 255, 260), §6 Literature (line 310), §8 row H7 (line 340), §5 "Does not fit" (line 288).

**Argument.**

- (a) The report flags that hard U = 2.2 at R = 20 failed because equilibrium N ≈ K·e^{-U} ≈ 110 (N·s_d ≈ 2) and that this "is not tested at larger K". Yet D3 lists "hard U = 2.2 extinct at R ≤ 20 at K = 1000" among the "Day-favourable outcomes reported regardless", and §8 row H7 repeats it. A pre-registered prediction that failed for a stated scale reason belongs in the artefact column, not the Day-favourable one.
- (b) The deleterious spectrum is a single s_d = 0.02. Real U = 2.2 is dominated by sites with N_e·s < 1 (Kondrashov 1995, PA-17; Lesecque et al. 2012, PA-16; Galeota-Sprung et al. 2020, PA-18). Hard accounting of those is exactly what these papers reject ("a mutation-free individual is exceedingly unlikely to exist"). With one s_d the hard-load simulation tests a regime that the literature says does not occur. The report's phrase (§6) "Keightley's statement is supported" is true as stated (hard accounting is implausible), and it should be read as supporting the critics (and Keightley), not Day.
- (c) The bins have no recombination within 0.1 M, so background selection is overstated (line 63). That is labelled as Day-favourable, which is honest, but the effect on hard-load persistence is not estimated.

**Fix.**
- Move the U = 2.2 R = 20 item to "failed prediction, K artefact" and drop it from D3's Day-favourable list.
- State in §4.2 and §8 that the hard-load rows are bounding cases that Keightley, Lesecque et al. and Charlesworth 2013 (PA-16, PA-17) argue do not describe humans.
- If the number is wanted, one or two runs at K = 10⁴ on na-workhorse (N ≈ 1,100 at equilibrium, N·s_d ≈ 22) would remove the confound.

### 6. MAJOR. Credit gaps in §6 and the "no critic" statements

**Locator.** §6 Critics block (lines 303-306); lines 150, 314.

**Argument.** Items found in the corpus that are absent from the adjudication.

- (a) **Hancock / Gutsick Gibbon** (`yt/_Vu0ZVVjwHc.transcript.txt`, 02:06:13-02:13:12; the source KITTENS §11 relays). The report credits KITTENS and treats the video's point as a relayed clause. The video is the primary and contains three arguments the report lists as open unknowns:
  - hard versus soft, and "when is selection actually occurring? Is it on zygotes, infants, old people?" (02:09:03);
  - frequency "doesn't have to be very low" (02:12:32);
  - poorly adapted versus well adapted populations (02:08:20).
  It also gives a correct verbal statement of the cost mechanism: replace "all the other individuals that died", constrained by "a reproductive ceiling of how quickly those individuals can reproduce" (02:11:51). Hancock thus states the premise of ln R / D without the formula. Caveat in the other direction: his "touch grass" and "completely useless" remarks are rhetoric, and the video is replying to the 22 September text and an earlier version of the parallel-fixation argument (G2 note).
- (b) **Nesslig20** (Peaceful Science 18094, §2.1) writes "There are other solutions that allow selection to exceed the limit argued by Haldane (see this recent paper)", linking Matheson, Exposito-Alonso and Masel 2025. The H6 claim file records the sentence. The report credits only "does not apply to drift" and says he gave no adaptive count. Matheson's measured selective-death share (8.5-95%) is the empirical analogue of the R / I parameter the report calls the missing input. This is a pointer, not a number, but it is the right pointer.
- (c) "**No critic gives ln R / D, the Nei/Felsenstein spacing, a value of R, or an adaptive count with a source**" (line 306). As a statement about formulas this is accurate (my grep of `sources/raw/critics/` found no formula; the only hits for the cost are Hancock's verbal account, Nesslig20's restatement of 30N/0.1N, and the AI-assisted `ck-` posts quoting Haldane's C ≈ 2 ln(1/p₀) and R_max ≈ k/C on Day's side). "A value of R" is too strong given (b). Suggest: "no critic gives the formula; Hancock states the mechanism; Nesslig20 points to the source of the missing parameter."
- (d) **Mansfield** MF-08 ("biologically naive") and prior-art's note that soft selection is invoked in prose by "Mansfield" and the Reddit guest are not in H3. Minor: MF-08 only concedes the selection question is distinct.

**Fix.** Add (a) and (b) to §6 Critics; reword line 306 as in (c); fix lines 150 and 314 (finding 1).

---

## MINOR findings

### 7. MINOR. "Haldane's regime reproduced" mixes two offsetting model features
**Locator.** §4.1 (line 188), §8 row H.
The 1/300 at R = 1.1 comes from D_obs ≈ 15 (K = 1000) times φ ≈ 0.53 (s = 0.01). At human D = 20-30 the mean-field value is 1/210-1/315; with φ = 0.53 it is 1/400-1/600. The report says this (line 188, "not as the mean-field ln 1.1/30"), but the bold "**1.00**" in the λ50 × 300 column suggests precision the data lack. λ50 at R = 1.1 is pinned by a grid point at exactly 1/300 with 8/16 persisting (Wilson [0.28, 0.72]). Fix: show λ50 × 300 as a range "0.7-1.4" for R = 1.1 and R = 1.05, and drop the bold. The substantive statement ("order of magnitude 1/300 at R ≈ 1.1") stands.

### 8. MINOR. P3 (K = 4000) cannot support "no rise in φ"
**Locator.** §4.5 P3 (line 239), §7 (line 317).
R = 1.1 gives 0/6 at K = 4000 against 4/16 at K = 1000 at x = 0.75 (Fisher exact p ≈ 0.3 by my hand count), and R = 2 gives 4/6 against 9/16. The Wilson intervals overlap entirely. "No rise" and "a rise" are both consistent. By a reflected-random-walk argument (reviewer scratch, not run): the extinction barrier is ln(K/20), so tripling K from 1,000 to 4,000 adds only ln 4 ≈ 1.4 to a barrier of about 3.9. Little K-dependence in φ is therefore expected, which supports the report's value but not on the strength of P3. Fix: say "P3 is underpowered; a logarithmic dependence on K is expected from barrier depth".

### 9. MINOR. The persistence criterion (50% over 10,000 generations) is generous to the sustainable rate. This is a point for Day
**Locator.** §4.1 λ50 definition (line 65), §4.5 P2, §7 (line 317).
A lineage that must persist 252,000 generations needs far better than 50% over 10,000. Under a constant hazard, 10/16 persisting over 10,000 generations at R = 1.1, λ = 0.0031 gives about 0.15 over 40,000 (observed 0/8) and about 10⁻⁵ over 250,000. The sustainable λ at R = 1.1 is therefore below 1/300 over the full lineage, likely nearer 1/500-1/700 (x = 0.25, 16/16 persisted over 10,000). The report mentions this in caveats but both §5 tables use λ50. A critic should concede this and ask that the §5 table carry a note "λ50 over 10,000 generations overstates the sustainable rate; over 250,000 generations it would be lower". It partly offsets the points above.

### 10. MINOR. Item 5 of Day's credit and KR-09 are inconsistent
**Locator.** §6 Day 5 (line 297) versus Allies keruru (line 301).
Day 5 says "Day-favourable result nobody in the corpus has stated". The keruru bullet says KR-09 runs the α-type comparison. Reword Day 5 to "no source with a number", and note that keruru's January post is superseded (`opponents/keruru.md`).

### 11. MINOR. Single s, single s_d, immediate re-seeding
**Locator.** §7 simplifications (lines 319-326), script lines 462-465.
- The treadmill re-seeds a lost beneficial copy in the same generation (`G[j, rng.integers(0, 2*N)] = 1`), which is a high-supply assumption (effective M of order 0.1-1 per locus per generation). It favours the critics relative to a realistic M ≪ 1 (see Concessions c), and the report should say which direction it goes. S6 failed in the critics' direction (D = 6.5 at M = 1), and that is the case the report uses to say "fits for R ≳ 1.1-1.9".
- Adaptive s is single-valued per run (0.003, 0.01, 0.03 in separate runs). A beneficial DFE would mix them. Because φ falls as s rises (line 229), the right φ for a mixture is a weighted one. Fix: state that §5's two tables bracket this.

### 12. MINOR. The "mean-field column is an upper bound" is only tested to x = 1
**Locator.** §4.5 P1 (line 236), §7 (line 317).
At s = 0.003, R = 1.1, 5/8 persisted at x = 1.0 (Wilson [0.31, 0.86]). The data show φ ≳ 0.75 is not excluded, not that φ ≈ 1. Burn-in 4,000 is about 1.3 mean fixation times (ttf ≈ 3,000), so the window starts partly before stationarity (k_obs/λ = 0.94-0.98, close to 1, so the effect is small). Fix: write "φ ≥ about 0.75-1" for s = 0.003.

### 13. MINOR. §1.2 and §6 treat Term 3 "d = 0.45" as ln R
**Locator.** §1.2 (line 92), §6 Day 3.
Writing 0.0256 = ln R / D with ln R = 0.45 maps Day's turnover coefficient d onto a reproductive-excess parameter. R4-H-C2 found d is a unit conversion. The mapping is arithmetic, but it should be flagged "audit mapping, not Day's derivation". Day's own smax = 1, "twice as many descendants as the average" (Z19984826 §3.3), is the better anchor (R ≈ 2, ln R ≈ 0.69).

### 14. MINOR. Caveat on "Human M unsourced" can be partly closed with corpus numbers
**Locator.** §7 (line 329), §5 "Fits (critics' side)" last bullet.
The corpus has μ = 1.1×10⁻⁸ (Keightley 2012) and N ≈ 10⁴. Then 2Nμ ≈ 2×10⁻⁴ per site per generation (reviewer scratch). An adaptive locus with L_t beneficial target sites has M ≈ 2×10⁻⁴·L_t. M ≥ 1 therefore needs L_t of about 4,500 sites. For a single site or a short element M ≈ 0.0002-0.02, and D rises (S6: 17-22 at M = 0.1; more below). The "D ≈ 6.5 at M ≳ 1" branch of the critic-side "Fits" bullet is therefore the generous end. Fix: give this hand arithmetic as the sourced scale and state which branch it favours (Day).

---

## Do the parameter choices systematically favour Day?

Mixed, with a net lean toward Day on the headline "does not fit" statements.

**Choices that favour Day** (stated: A, D, E, F; unstated: B, C, G)
- A. Treadmill, fecundity-before-viability, hard selection (stated in §7; not carried into verdicts).
- B. Additive costs; no truncation, epistasis, soft or absolute-fitness adaptive variants (not named).
- C. D ≥ 20 as default; tables stop at D = 10 (partly stated).
- D. R = 1.1 as the anchor, unsourced (stated as unsourced).
- E. s = 0.01 for the φ table (stated; the s = 0.003 case is shown).
- F. Bin-level background selection overstated; N < 20 extinction; K = 1000 (stated).
- G. Hard-U results listed as Day-favourable outcomes despite the K artefact (stated as likely artefact; listed anyway).

**Choices that favour the critics** (all but the 50% criterion are stated)
- Ceiling regulation (the compensatory-fecundity premise).
- Immediate re-seeding (high beneficial supply).
- 50% persistence over 10,000 generations (overstates the sustainable rate; partly unstated).
- Stage A λ50 interpolated up from a grid that includes λ = 1/300 as a point.

Net: the Day-leaning choices act on the verdict text (what "does not fit"); the critic-leaning choices act mainly on the numbers in the tables. If the report adopted findings 1-5, the verdict text would read: hard, additive, rare-start selection with an unsourced R caps adaptive substitutions at roughly ln R / D; the only counts that fail by orders of magnitude are those that assume a noncoding adaptive share the literature does not support.

## Concessions: where the report is right and a critic should concede

a. **1/300 at R ≈ 1.1 is not a simulation artefact.** It is ln R / D = 0.095/30 (Haldane's own arithmetic) and the simulation lands within a factor of 2-3 at s = 0.003, 0.01 and K = 1000, 4000. The honest reading of s = 0.01 / K = 1000 sensitivity is "within a factor of 2-3", not "an artefact".
b. **Day's 17.5M-205M do not fit under any setting** (ln R in the hundreds to tens of thousands). Even finding 1's mainstream resolutions cannot bring it to a feasible regime. This is right, and it follows from H1 as well.
c. **Site-specific supply is small** (finding 14 arithmetic). The cheapest critic-side branch (M ≥ 1, D ≈ 6.5) needs large targets.
d. **Nunney's own judgement that hard selection likely dominates directional change**, and the report's inclusion of stage C, are fair to the literature. Stage C reproduces Nunney's qualitative M-dependence.
e. **The report credits the critics correctly** on the two clauses it states: "does not apply to drift" (Nesslig20) and "concerns selected substitutions only" (KITTENS), and it states plainly that its own result on soft selection is "not tested".
f. **P2** (R = 1.1 at 40,000 generations fails) and the stage S result (s = 0.03 worse) are reported against the grain of the s = 0.003 mean-field case; I find no suppression.
g. **Hard sweeps being rare** (GAP-02) is a Day-favourable fact. It lowers K_a (hard-sweep route) but does not by itself raise D. It sits uneasily with α ≈ 0.1-0.2 only if most adaptation is weak or soft, which is also the critics' lower-D case.

## Suggested edits, in priority order

1. Add the conditional ("under hard, additive, treadmill selection with Haldane's R") to every "does not fit" line in §5, §6, §8; add the "not modelled" table (findings 1, 4).
2. Replace "Haldane's own regime reproduced" with "Haldane's assumed 10%"; add the Day-smax R ≈ 2 note and the hard-load consistency note (finding 2).
3. Add D = 3, 5 columns and the break-even D (finding 3).
4. Move the U = 2.2 R = 20 item out of D3's Day-favourable list; label hard-load rows as bounding cases (finding 5).
5. Credit Hancock's three points and Nesslig20's Matheson pointer; correct lines 150, 306, 314 (finding 6).
6. Minor items 7-14 (precision, power, criterion note, wording).

No file other than this one was edited.
