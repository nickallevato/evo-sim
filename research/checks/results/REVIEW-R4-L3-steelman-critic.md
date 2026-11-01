# REVIEW R4-L3: steelman, critics' side

Reviewer: fresh reviewer instance (Paperclip EVOA-8, brief `research/checks/briefs/A2e-reviewer-3.md` at 1185955),
2026-11-01. Skill `review-steelman`, critics' side only. Review 3 of 3 (D-38: A2e is on the exit gap). I did not
author R4-L3, its registration, its run or the other two reviews, and I did not read `REVIEW-R4-L3-steelman-day.md`.
Under review: `research/checks/results/R4-L3.md` at 78d9d11 (line numbers below are that version), against the
registration `l3_amk.py` docstring (f5b7e5e). Inputs checked first: script md5 `ae4a764eec0ff8100c05d120fb41ecb4`
(working tree = brief = `l3_amk.host`); `l3_main.out` c4225ff3…, `l3_result.json` 18940a69…, `l3_counts.json`
925f101e… equal the collection record; both JSON files parse. No run, no fetch. The npz was not loaded.

## Reviewer computations (post hoc, reviewer; one local `python -I` process on `l3_result.json`, under 1 s)
- **Resolving power.** GOV: P - L = 0.0543 (L is the bootstrap lower bound), bootstrap U - P = 0.1121. If the
  interval shifts with the point (an assumption), B2 needed P > 0.0718 and B1 needed P > 0.1068 under the
  registered h = 0.0175. B6 needed P < -0.1065 even on the bootstrap upper bound alone, and was unreachable on the
  MC envelope.
- **Own-Dn edges.** G1/Dn = 0.00667, G2/Dn = 0.00556. h = max(0.0175, 0.00667) raised the critics' edge 2.62x over
  the own-Dn value; l = min(0.0065, 0.00556) lowered Day's edge 1.17x. With h = G1/Dn the B2/B1 lines would have
  been P > 0.0610 / 0.0743.
- **Denominators.** Dn 28,565 is 0.955x Uricchio's NS 29,925, 1.46x N1 (19,570), 2.58x N2 (11,090), 1.57x N3
  (18,180); 0.436 of the S6 two-lineage Dn (65,520).
- **Counts at the bootstrap upper bound 0.0921:** Dn_own 2,631 (13.8x G1); N1 1,803 (9.5x); N2 1,022 (5.4x);
  N3 1,675 (8.8x).
- **Upper bound against published points:** 0.096 (Uricchio ABC-MK lower HPD) - 0.0921 = 0.0039; 0.093 (Boyko,
  pooled) - 0.0921 = 0.0009. S6 bootstrap upper 0.1146.
- **High-frequency pooled alpha, GOV window:** x ≥ 0.3: -0.0234 (12 bins, 8 below zero, mean of bin alphas -0.0238);
  x ≥ 0.5: -0.0181; x ≥ 0.6: -0.0349. S1-S5 points lie GOV -0.0175 to GOV +0.0216.

## Findings

### SC1. MAJOR: the side score presents an outcome that does not discriminate as a Day hit and a critic miss
- **Evidence.** The headline (l.12) and section 8 (l.161-163, l.177) lead with "DS hit, DS+ hit; CS miss, CS+ miss"
  and "The critic side gets no confirmation from L3". But the partition is not like for like. DS is
  *non-exclusion* (B3-B6, four of six bands). It includes B3, where the licensed value is `contested, leaning
  contradicted` (docstring l.206), a lean toward the critics. CS is *exclusion* by the envelope's lower bound. At
  the precision L3 reached, CS needed an aMK point of about 0.072 (B2) or 0.107 (B1) (post hoc, reviewer).
  Below that, DS hit whatever the data said. Second, neither side states a human alpha (docstring l.53-56;
  R4-L3 l.99-100). The brief summarises the critics' position as "most differences are neutral" (unscored, rule S).
  That position predicts alpha near zero just as Day's ceiling does. Day's ceiling is modal: "an unattainable
  ceiling" (Q130 core), "humans can fix mutations faster" (Q138). A realised count at or below 191 is a consequence
  the ceiling needs. It is also what the neutral rebuttal predicts, so as a test of the ceiling this pass is weak.
  What the critics lose here is the *aMK confirmation of the Uricchio-based `contradicted` basis* (SC10). The
  neutral-theory rebuttal does not lose.
- **Fix.** Headline: after the score line, add "DS is non-exclusion; at this precision CS needed an aMK point of
  about 0.07 or more (*post hoc*)". Section 8, Day bullet 1: add "an outcome the critics' neutral-theory position
  (unscored) also predicts; it does not separate the ceiling from that position". Section 8, critic bullet 4:
  replace "The critic side gets no confirmation from L3" with "The `contradicted` basis gets no aMK confirmation
  from L3; the critics' neutral-theory rebuttal is not tested by it". No change to band, move row or licensed value.

### SC2. MAJOR: the critics' strongest technical case appears only as the generic HM7 caveat. A critic-favourable overstatement next to it needs correcting
- **Evidence (for the critics).** Section 6 (l.115-120) states that L3 speaks to the any-effect-size reading. Section 8
  (l.170-173) gives the critics only HM7's "tendency toward underestimation". The audit's own record is more
  specific. The bias aMK leaves uncorrected is the weakly adaptive component. On the any-effect-size reading that
  component is part of what is being counted, and in humans it is the larger part: Uricchio 2019, "estimate α =
  0.135 in human protein-coding sequences, 72% of which is contributed by weakly-adaptive variants"
  (quotes-literature l.651). On the same 661 samples and the same divergence basis, "our method nearly doubles the
  estimated human adaptation rate (to α = 0.135)" from aMK's 0.076 (R4-A2e-alpha l.137). L3's -0.020 is an aMK
  point, so for the reading it is scored on, it is biased downward by a mechanism that is documented in humans.
  That is the reason the registration capped B6 at a lean (l.209-213). The write-up should say it in those words,
  with those numbers.
- **Evidence (against the critics).** Section 7 item 3 (l.149-151) and section 8 critic bullet 3 (l.176) say the
  0.096 lower HPD is "not excluded" by L3's intervals. That rests on the MC envelope only, and the write-up itself
  calls the MC upper tail impossible (alpha > 1; l.199-203; correctness MINOR-4). The gene bootstrap, the
  interval that carries gene-level heterogeneity, excludes 0.096 by 0.0039 (post hoc, reviewer). The honest
  statement has two parts. (a) On L3's bootstrap, the critics' basis point lies just outside. (b) That is a
  cross-estimator comparison. ABC-MK is built to correct the bias HM7 names, so the bias predicts an aMK interval
  that ends just below an ABC-MK HPD. It is weak evidence against ABC-MK, not none. Boyko's 0.093 is pooled over
  both lineages, so the like-for-like row is S6, whose bootstrap upper bound (0.1146) includes it.
- **Fix.** Section 6 and section 8 critic side: add the 72% quote and "on the same samples ABC-MK gives 0.135
  (0.096-0.17) against aMK 0.076; aMK leaves the weakly adaptive component uncorrected, and the any-effect-size
  reading counts it". Section 7 item 3 and section 8 bullet 3: "0.096 lies 0.004 above the gene-bootstrap upper
  bound and inside the registered MC envelope; across estimators, so weak evidence against ABC-MK". No change to
  band, move row or licensed value.

### SC3. MINOR: the "second-order Day point" rests on the audit's own description and its own missed prediction, and it cuts both ways
- **Evidence.** Section 8, Day bullet 2 (l.164-167): "two aMK estimates on what the registration calls the same
  samples differ by 0.096, which is wider than the whole alpha* band". The 0.096 gap is the size of the audit's
  Q2 miss: Q2 was set from 0.076 (docstring l.234). "Same samples" holds for the 661 AFR genomes and the
  hg19/panTro4/ponAbe2 parsimony basis. It does not hold for the gene set: Uricchio's estimate is "not directly
  comparable" because of its larger gene set (R4-A2e-alpha l.176), and his cut-offs and window are not on record.
  Day's position as the brief gives it, "K is not derivable from first principles", makes no prediction about
  pipeline spread. On overlapping data the gap is about 2.3 L3 bootstrap standard errors (post hoc, reviewer). That
  overlap means the gap mostly reflects pipeline choice, not sampling. To that extent it is a real point, but it
  applies to L3's -0.020 exactly as much as to 0.076.
- **Fix.** Move the bullet to "Both / the audit's own errors", worded: "pipeline choices on overlapping data move
  aMK by up to 0.096, more than the whole alpha* band; this weakens L3's point as much as the 0.076 line". The
  strike stays, because it is registered (I agree with correctness NOTE-6 on the rule). Its text should read: "not
  reproduced as a point by L3's registered pipeline (same 661 samples and divergence basis, different gene set);
  inside L3's bootstrap interval".

### SC4. MINOR: L3's own registered Dn gives the critics credit that the write-up leaves out, and the h = max rule cost the critics far more than l = min cost Day
- **Evidence.** Dn = 28,565 is registered output (Q4 hit). The docstring calls it "a lower bound on the exome count"
  (l.91). It is 0.955x Uricchio's NS 29,925, measured on the same parsimony basis, and 2.58x N2, the audit's "most
  Day-charitable" denominator (post hoc, reviewer). This is direct evidence on a Day-side point the claim file keeps:
  "the paper's NS = 29,925 is unreconciled with N1-N3 (candidate: scaling by gene count, unverified)" (A2e claim
  file, l.76). On a near-whole-exome gene set the audit's own count lands at Uricchio's size. The flip on L3's Dn
  is 0.67% (G1) / 0.56% (G2). The registered rule "least favourable to each side" raised the critics' edge 2.62x
  (to 1.75%) and lowered Day's edge 1.17x (post hoc, reviewer). That is symmetric in form and asymmetric in effect.
  It does not matter for this outcome: P < l under either edge, so the band is B5 either way.
- **Fix.** Section 8, critic side, add: "L3's own human-specific Dn (28,565, a registered lower bound) matches
  Uricchio's 29,925 on the same divergence basis and is 2.6x N2 (*post hoc*)". Section 2: one *post hoc* sentence on
  the 2.62x / 1.17x effect of the edge rule. The bearing on the claim file's kept Day point is for integration, not
  for this write-up.

### SC5. MINOR: the critic end of the counts is shown only as an absurd number
- **Evidence.** Section 5 (l.107) prints counts at U from the MC envelope: "Dn_own 1397118 (7329.32x G1)". The
  printing is registered and the write-up flags it (l.110-111). But a reader sees the critic end of the interval
  only as a number above Dn itself, while the Day end (counts at P and L) reads as ordinary arithmetic. At the
  bootstrap upper bound the counts are Dn_own 2,631 (13.8x G1), N2 1,022 (5.4x) (post hoc, reviewer).
- **Fix.** Under the printed block, add a *post hoc* line with the counts at the bootstrap upper bound 0.0921.

### SC6. MINOR: Day credit in section 8 is worded more broadly than what was tested
- **Evidence.** l.161-163: "the human lineage shows no adaptive excess over the flip at ~1%", and alpha "comes out at
  or below zero". What was tested is coding sites in 19,504 autosomal knownCanonical transcripts, upper-case AA,
  AFR. Coding-only is not neutral between the sides. A coding count above G1 is enough for the critics, because it
  is a lower bound. A coding count below G1 does not bound the genome-wide count (RG-03, non-coding adaptation, is
  outside L3; l.119). An adaptive fraction cannot be negative. P = -0.020 is consistent with zero, and the bootstrap
  interval reaches 0.092.
- **Fix.** "On this estimator, the human lineage's coding sequence (19,504 transcripts) shows no adaptive excess
  over the flip; the point is consistent with zero, and the bootstrap interval reaches 0.092 (5.3x h). A coding
  count bounds the genome-wide count from below only."

### SC7. NOTE: the audit choices on the brief's list, checked for bias against the critics: none acts on this outcome
Window [0.1, 0.9] is the asymptoticMK default (HM5). S1 and S3 agree with GOV, and there is no hidden rise at high x:
pooled x ≥ 0.6 gives -0.035 (post hoc, reviewer). The exponential fit is chosen by AIC. Its linear fallback
(0.0161, correctness NOTE-10) is B4, so the licensed value is the same. Upper-case AA governing is the
critic-favourable choice: all-case S4 is lower (-0.0286). S6 is rightly report-only. It pools the chimp lineage,
whose larger Ne makes a higher alpha the expected result, so it is not a human-lineage estimate. Had it governed,
it would give B4, the same licensed value. S5 (EUR, bottlenecked) is a structural drag on any critic clearance
through the B2→B3 rule (here -0.0175). The rule is inactive at B5. The envelope made B1/B2 harder and B6 out of
reach. The MC tail moved no band.

### SC8. NOTE (against the critics' interest): the registration was already tilted toward the critics where it counted
B3 (the critics' near-miss) licenses `contested, leaning contradicted`. Its mirror, B5 (Day's near-miss, this
result), licenses plain `contested`, on the HM7 asymmetry stated before the run. B6 was all but out of reach
(SC1 computations). The critics cannot claim the licensed value was hedged against them.

### SC9. NOTE: hand-patched input
I agree with correctness MINOR-1. From the critics' side there is no direction to the concern: a 500-byte window
cannot carry 0.07 of alpha.

### SC10. NOTE: what the evidence costs the critics, stated plainly
1. The audit's own pre-registered, bias-corrected human-lineage coding alpha is about zero (P -0.020; every
   S1-S5 point below l; the pooled upper bins below zero). It uses the same 661 African genomes and the same
   divergence basis as the critics' human-lineage source.
2. The condition R4-A2e-alpha set for `contradicted` was "another bias-corrected human-branch estimator, e.g.
   asymptotic MK ... confirming alpha above about 1%" (docstring l.203-204). It is not met, and aMK on these data
   will not meet it.
3. The "aMK baseline (alpha 0.076) 4.4x" line leaves the `contradicted` basis under the registered strike. Against
   F = `contradicted`, L3 proposes one step down.
4. The critics' human-lineage count now rests on one model-based estimator (ABC-MK). Its lower HPD sits 0.004 above
   L3's gene-bootstrap upper bound. The case is now model-dependent, as D6 says. SC2's bias argument is their
   answer, and it is a model argument too.

## On the correctness review (by id)
- **MINOR-1** agree (SC9). **MINOR-2** agree; the upper-case reading is also the critic-favourable choice (SC7).
  **MINOR-3** agree. **MINOR-4** agree, and it bears on SC2: an MC tail that is registered behaviour yet impossible
  should not carry the claim that 0.096 is "not excluded".
- **NOTE-6** agree that the strike follows as registered. I disagree in part: "on the same samples" overstates the
  match, because the gene set differs. Fix the strike text (SC3).
- **NOTE-7, NOTE-8, NOTE-10** agree. NOTE-10's linear B4 is the same licensed value (SC7).
- Band B5, move row B5, licensed `contested`, and no move against `pending` by L3 alone: **confirmed**. No finding
  here changes the band, the move row or the licensed value.

## Counts
BLOCKER 0, MAJOR 2 (SC1, SC2), MINOR 4 (SC3-SC6), NOTE 4 (SC7-SC10).
Wrong numbers: none found. All reviewer numbers above are post hoc (reviewer), from `l3_result.json`.
