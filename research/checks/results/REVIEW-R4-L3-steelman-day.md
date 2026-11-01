# REVIEW R4-L3: steelman, Day's side

Reviewer: fresh reviewer instance (Paperclip EVOA-7, brief `A2e-reviewer-2.md` at a26de08), 2026-11-01. Skill:
`review-steelman`, Day side. Review 2 of 3 (D-23). I did not author R4-L3, its registration or the correctness review,
and I did not read any critic-side steelman of L3 (none exists at a26de08).
Under review: `research/checks/results/R4-L3.md` (78d9d11), against the registration (`l3_amk.py` docstring l.1-279,
f5b7e5e, md5 `ae4a764eec0ff8100c05d120fb41ecb4`, checked). Read: `raw/l3_main.out`, `l3_result.json`, `l3_counts.json`
(all parse); briefs `L3-analyst.md`, `A2e-analyst-1.md`; `REVIEW-R4-L3-correctness.md` (8432a1c); claim
`A2e-ltee-as-ceiling.md`; Q130, Q131, Q133, Q138, Q139 by grep; `R4-A2e-alpha.md` by grep (Gayà-Vidal rows).
Local work: two `python -I` processes on `l3_result.json`, seconds each. No run, no fetch, npz not loaded.
Every number below that is not printed in `l3_main.out` is **post hoc (reviewer)**, descriptive, and enters no band.
Severity labels as in the correctness review.

**Summary: 0 BLOCKER, 2 MAJOR, 5 MINOR, 8 NOTE.** None changes the band (B5), the move row (B5) or the licensed value
(`contested`), and none changes "no move against `pending` by L3 alone". The check is honest and its registration is
even-handed on paper. From Day's side two things are wrong in the write-up: B5 is presented as a shortfall for Day
when it is the best outcome the test could realistically give him (D1), and the large MK correction is used against
Gayà-Vidal's 0.2% when L3's corrected value in fact lands on it (D2).

## Findings

**D1 MAJOR (section 8 "Critic side" bullet 1; section 7 item 3; headline). B5 is Day's ceiling outcome on this design,
and the write-up books "no band below B5" as a critic point.** On L3's own interval widths (GOV bootstrap
[-0.0743, 0.0921] around P -0.0200; post hoc (reviewer)):
- B6, the only band that licenses a Day-direction value (`contested, leaning supported`), needed U < l = 0.00556, i.e.
  P ≤ l - (U_boot - P) = **-0.107**. A true adaptive fraction cannot be below 0. If Day is exactly right (true alpha in
  [0, 0.0175]), an estimate 0.11-0.12 below the truth is needed: under 1% chance by a normal approximation with the
  bootstrap SE 0.042 (width/3.92), and less with the narrower lower half-width (0.054). The MC interval makes it worse:
  a flat spectrum, the Day-side shape, leaves c poorly identified (sd 7.4 against 9.7, correctness MINOR-4), and the MC
  upper bound then exceeds 1 (GOV 48.9, S3 5.6, S4 1.5). Through the envelope that alone blocks B6.
- B2 (`contradicted`) needed L > h, i.e. P > h + (P - L_boot) = **0.072**; B1 needed P ≥ 0.107. Uricchio's aMK on the
  same 661 samples (0.076) would have been B2. In a critic world with an aMK expectation of 0.076, B1/B2 come out about
  half the time (same approximation).
- The alpha\* band is 0.0119 wide (h - l); the bootstrap interval is 0.1664, **13.9x** wider. L3 can detect a critic
  world with alpha ≥ ~0.07. It cannot tell "Day exactly right" from "Day wrong by a few-fold". Every outcome a
  Day-right world can produce (B4, B5) licenses `contested`.
The registration is not at fault: the width comes from the data, and the registration states the B6 → lean
asymmetry (HM7) in advance. The smoke reached B6 on synthetic tables (ST-05), not at exome-scale gene-bootstrap
widths. But section 8 reads "No band below B5 was reached" as if B6 were a live outcome that Day failed to reach.
**Fix:** in section 7 add, labelled post hoc: "On these widths B6 needed P ≤ -0.107, below any possible true value;
B2 needed P > 0.072, which Uricchio's aMK 0.076 would have met. B5 is the strongest result the design could
realistically give the Day side; the critic side had a realistic path to `contradicted`." In section 8 move "no band
below B5 was reached" out of the critic bullet, or pair it with that sentence. In the Day bullet add: "L3 returned the
best outcome its precision allowed for the Day side."

**D2 MAJOR (section 8 "Critic side" bullet 2). The MK correction does not support setting Gayà-Vidal's 0.2% aside;
L3's corrected value lands on it.** The bullet says Q3 (0.8224) bears out "the audit's own reason for setting aside
Gayà-Vidal's uncorrected 0.2%". But GV's 0.2% is not the all-bins naive value. It is the DAF ≥ 60% value, itself a
frequency-filter correction (R4-A2e-alpha l.47, l.75: "For SNPs with DAF ≥60%, we obtained α = 0.002"). L3's 0.82
correction runs from the all-bins -0.8423 to the asymptote -0.0200. The record set GV aside because its sequence was
"still rising at the last class" (-0.361, -0.142, -0.059, 0.002; R4-A2e-alpha l.80) and the authors call the last
value a possible underestimate. That is the question the asymptotic fit answers. On L3's GOV counts, pooled over the
same DAF classes up to the top bin (post hoc (reviewer), Poisson SE ignoring gene clustering): ≥ 15% -0.035,
≥ 30% -0.007, **≥ 60% 0.0013** (SE 0.023), ≥ 80% 0.020 (SE 0.028). So L3 reproduces GV's 0.002 at DAF ≥ 60% on its
own pipeline, and its asymptote says the curve flattens near 0 (-0.020), not that it keeps rising past the flip.
**Fix:** delete "and the audit's own reason for setting aside Gayà-Vidal's uncorrected 0.2%" from the critic bullet.
Add a Day bullet: "L3's bias-corrected alpha agrees with Gayà-Vidal's DAF ≥ 60% value (0.002; L3's own pooled
DAF ≥ 60% value is 0.0013, post hoc). The 'still rising' objection to GV (R4-A2e-alpha M1) is tested by the asymptote,
which is -0.020." **Honest limit:** GV's value stays a null, not a count (M1 stands); the ≥ 80% class, which takes in
the two bins outside the registered window, is 0.020, about h, so a late rise is not excluded at this precision.
Whether GV's row in R4-A2e-alpha regains standing is for integration, not this review.

**D3 MINOR (headline; section 6 first paragraph). "Speaks only to the any-effect-size count reading" is broader than
the logic, against Day.** Strong-effect adaptive substitutions are a subset of all adaptive ones, so true alpha_S ≤
alpha. A high total alpha says nothing about alpha_S (the registration rightly blocks that move), but a low total
alpha bounds alpha_S from above. The registered "no move on strong-only in any band" stands, and the strong-only value
is `contested` already, so nothing moves. **Fix:** "L3 licenses moves only on the any-effect-size count reading. On the
strong-effect-only reading it moves nothing, but its low point is consistent with that reading too, since strong-effect
substitutions are a subset (weakened by HM7's underestimation)."

**D4 MINOR (section 7 item 3; section 8 "Critic side" bullet 3). "0.096 is not excluded" rests on the MC tail above
alpha = 1.** Uricchio's ABC-MK lower HPD 0.096 lies **0.0039 above** L3's gene-bootstrap upper bound 0.0921 (post hoc
(reviewer)). The 95% intervals [-0.074, 0.092] and [0.096, 0.17] do not overlap. 0.096 is "inside" only the MC interval,
whose upper bound (48.9) comes from draws with b > 0 and c < 0 together (correctness MINOR-4). Under the registered
envelope "not excluded" is correct. As a description it hides the one comparison that favours Day. In section 8 it is
also an unlabelled post hoc comparison cutting against him. **Fix:** "0.096 lies just outside the gene-bootstrap
interval (by 0.004) and inside the MC interval only through its tail above alpha = 1 (post hoc)." **Honest limit:**
HM7 predicts aMK below ABC-MK; Uricchio's own aMK-to-ABC-MK gap is 0.059. So non-overlap is the expected direction,
not evidence against ABC-MK.

**D5 MINOR (section 9 item 5). The registered strike is hedged after a Day-favourable result.** The docstring
(l.221-223) strikes "aMK baseline (alpha 0.076) 4.4x" from any `contradicted` basis in rows B4-B6, with no condition on
whether 0.076 lies inside L3's interval. The audit itself described Uricchio's aMK as "on the same 661 African samples
and the same ... parsimony divergence" before the run. "Whether the strike follows as worded is for the reviews"
reopens a registered consequence because it went Day's way. The critic side would not accept a like-for-like hedge on
a B2. **Fix:** "Struck, as registered (B5). Context: 0.076 lies inside L3's bootstrap interval; gene set, bins and fit
may differ from Uricchio's." I agree with correctness NOTE-6 in substance and rate it MINOR from Day's side.

**D6 MINOR (section 8). The audit's own critic-leaning expectation failed, and that is filed only under "Both".** Q2
(P in [0.03, 0.15]) and Q8 (move row B2, i.e. `contradicted`) are the audit predicting, from Uricchio's 0.076 and
training background, that its pipeline would confirm the critic basis. It did not, and the Day-side DS and DS+ hit.
**Fix:** add to the Day bullets: "The audit pre-registered its own expectation of B2 (`contradicted`, Q8) and
P ≥ 0.03 (Q2). Both missed; the Day-side predictions hit." Keep the "Both" entry too.

**D7 MINOR (section 7 item 1; section 2). The point is not a fit artefact, and the write-up does not say so.** The
strongest critic objection to P is that it extrapolates an exponential whose c is poorly identified. Three
fit-independent or alternative views agree. (i) Pooled window bins above x = 0.3: alpha -0.023 (Pn 5,044, Ps 6,762);
above 0.5: -0.018; above 0.7: -0.019 (post hoc (reviewer)). (ii) The linear fallback on GOV gives 0.0161 (correctness
NOTE-10), still ≤ h. (iii) S2 (linear by AIC) gives 0.0016. All eight point estimates on the record (GOV, S1-S6, GOV
linear) are ≤ h. **Fix:** in section 7 item 1 replace "scatters around zero" with correctness NOTE-10's "at or slightly
below zero (12 bins, mean -0.024, 8 below zero)". Add (i), labelled post hoc.

**N1 NOTE (headline). The headline's U = 48.9101 is an impossible value given without comment.** A reader sees
[-0.07, 48.9] and concludes L3 says nothing, which undersells the Day-side point estimate. It also hides the
informative bound, 0.0921, which cuts against Day (concession 1). Append "(MC upper tail above alpha = 1, registered
behaviour; bootstrap upper 0.0921)".

**N2 NOTE (upper-case AA; agrees with correctness MINOR-2).** The governing upper-case choice is the one less
favourable to Day. Misoriented sites come from the nonsynonymous-rich low-frequency end and land at high x. That lowers
alpha(x) there and drags P down. Adding the lower-case calls (S4, 31,775 more AA calls) does lower P (-0.0286 vs
-0.0200). There is no top-bin downturn (x 0.925: 0.001; 0.975: 0.048). So a low P is not a polarisation artefact.
Add this to MINOR-2's fix text if the analyst wants; the band does not depend on it.

**N3 NOTE (model choice; agrees with correctness NOTE-10).** The AIC choice of the exponential (by 2.87) costs Day
nothing: the linear fit's 0.0161 is B4, also `contested`, also "one step down" against `contradicted`.

**N4 NOTE (basis choice; credit to the audit).** GOV is human-specific by parsimony; S6 (pooled human-chimp) is
report-only. That answers the earlier Day-side complaint (REVIEW-R4-A2e-alpha-steelman-day D2) that pooled
divergence favours the critics. S6's higher point (0.0144 vs -0.0200) has the direction that complaint predicted.

**N5 NOTE (thresholds).** h takes the published edge 0.0175 and l takes L3's own G2/Dn 0.00556, each the side harder
for the side that must clear it. G1 uses Day's own 1,322 and "191 achievable" (Q139). No goalposts moved.

**N6 NOTE (hand-patched VCF; agrees with correctness MINOR-1).** The patch has no direction: 500 B at 98.7% of the file,
CRC-checked to EOF, GB 0/872,626. It cannot carry a Day- or critic-side effect of band size.

**N7 NOTE (counts, section 5).** Negative counts at P are arithmetic, as written. The Day-side reading is "no detectable
adaptive excess", not "zero adaptive substitutions"; see concession 4.

**N8 NOTE (agreement with the rest of the correctness review).** I agree with MINOR-3 (the `pending` case is covered:
no move by L3 alone), MINOR-4, NOTE-5, NOTE-7, NOTE-8 (a lean is stored as `contested` plus a comment) and NOTE-9.
**Disagreement by id:** NOTE-6 only on severity (NOTE there, MINOR here, D5). Nothing in the correctness review cuts
against Day unfairly.

## Readings of Day's words (rule RD; the field's reading is fixed by the owner, not re-litigated)

| Reading of Q130/Q131/Q138 + Q139 | What L3 says | Status |
|---|---|---|
| Any-effect-size adaptive count, coding-only (formal statement; the field) | point ≈ 0, below 191 on every denominator; bootstrap upper 2,631 on Dn_own (13.8x G1), 1,022 on N2 (5.4x) (post hoc (reviewer)) | B5, `contested`, as registered |
| Strong-effect-only | no move (registered); the low point is consistent with it (D3) | `contested`, unchanged |
| Fitness-weighted | no bearing | `contested`, unchanged |
| Total throughput, "every fixation, regardless of mechanism" (Q133) | not tested; see concession 5 | not L3's field; waits on A5c |

## What the evidence costs Day (concessions that stand)
1. **The critic world is not excluded.** The gene-bootstrap upper bound 0.0921 is 5.3x h. As counts it gives 2,631
   on L3's own Dn (13.8x G1) and 1,022 on the Day-charitable N2 (5.4x) (post hoc (reviewer)).
2. **The registered asymmetry is real.** aMK "may still have a tendency toward underestimation" (HM7). Uricchio
   attributes 72% of human alpha to weakly adaptive substitutions (claim file, Uricchio addendum). As an illustration
   only (post hoc (reviewer), not transferable as a correction): Uricchio's own aMK-to-ABC-MK gap of 0.059, added to
   L3's P, gives 0.039, 2.2x h.
3. **The test could have gone against Day and did not; that does not make it a confirmation.** B2 was reachable
   (D1); B5 is "point below, interval reaches", which is `contested` by registration. DS and DS+ are the audit's
   reading of what Day needs, not a scored Day quote (rule S).
4. **alpha ≈ 0 is a null, not a count.** A negative point means the estimator's residual (slightly deleterious
   fixations, demography) is not fully removed on human data. Day cannot claim "no adaptive substitutions", only
   "none detected", with values up to about 9% (bootstrap upper 0.0921) not excluded.
5. **Day's own total-throughput basis (Q133) is costly on L3's raw data.** L3 counts 67,757 human-specific coding
   substitutions by parsimony at sites not polymorphic in 1000 Genomes (`div_hs`; Dn 28,565 + Ds 39,192), 355x G1
   (post hoc (reviewer)). This is a count, not a model inference, so the "all estimates are model inferences" defence
   does not reach it. It is not registered for any verdict here and bears on A5c, not on the field under review.
6. Coding-only leaves out non-coding adaptation (RG-03), which can only add to the human count. A2e internal
   `non-sequitur` is untouched.

## Could the test have produced an outcome on Day's side?
Yes in name: DS covers B3-B6 and was hit (B5). In substance no better than `contested`: B3 licenses `contested,
leaning contradicted`, B4 and B5 `contested`. B6, the one Day-direction value, needed P ≤ -0.107 on these widths (D1).

## Verdict view (Day steelman)
B5 and licensed `contested` are right, and from Day's side they are the best this design could return. Against
`pending`: no move by L3 alone (agree MINOR-3). Against a D-21 value of `contradicted`: the registered one step down,
with the 0.076 line struck as registered (D5). I do not argue for two steps; the registration fixes one. Nothing here
supports moving A2e toward `supported`.

## Counts
BLOCKER 0, MAJOR 2 (D1, D2), MINOR 5 (D3-D7), NOTE 8 (N1-N8).
Findings that change band, move row or licensed value: none. Wrong numbers in R4-L3: none found beyond the
correctness review's. Disagreement with the correctness review: NOTE-6, severity only.
