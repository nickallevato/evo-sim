# Review of R4 B3g (combined, low-stakes tier)
Date 2026-10-10. Method: read `R4-B3g.md`, `raw/b3g.out`, the pre-registered docstring at ef6e8aa (`git show`); recomputed the arithmetic by hand; confirmed the script is unchanged since ef6e8aa (`git diff ef6e8aa HEAD` empty). Nothing rerun, raw texts not re-grepped (the quote results come from `b3g.out`). Same-agent-family review (independence caveat). Escalation check: bookkeeping only, no verdict moves; no three-review tier.

## 1. Correctness
Recomputed: 2 x 1e4 x 37.2 = 7.44e5 (Day 740,000; 0.5%); 2.5e11 / 7.44e5 = 3.36e5 (Day 330,000; 2.4%, within the 3% bound); 2.5e11 / 74.4 = 3.36e9 (write-up "3.36e9"); 1e5/3300 = 30.3, 5e4/3300 = 15.15, 3e5/33000 = 9.09, 1e6/33000 = 30.3, 8e9/1e4 = 8e5; B4: 6 x 2/60.6 = 0.198 My, 7 x 2/24.3 = 0.576 My (reported 198/576 kya vs Day 200/580), reversal factors 30x and 12x. All match the write-up. P1-P3, P5 scored correctly against the docstring; the script is unedited since pre-registration, so there is no post hoc change to disclose.
- **MINOR-1.** Undisclosed gap between docstring and write-up in P3. The docstring says the concession changes each value by "15x to 800,000x"; the result (and the write-up table) is "9.1x to 800,000x" because chimp-low is 9.1. The prediction's range was wrong at the low end; the write-up should say so in one clause rather than silently using the correct figure. No effect on scoring (both far above R1's 25%).
- **MINOR-2.** The "19-46" mammal figure (Z18429937) is listed as "removed, error-level". That figure is a census/N_e ratio, an empirical claim about populations. What the concession removes is its use as a k/mu multiplier. The write-up should say "its use as a k/mu factor is removed; the ratio claim itself is untouched (and is external, not tested here)". As worded it overstates the reach.
- **MINOR-3.** P4 is scored "holds" but is a classification from stated bases, not a computation; the write-up labels it so (good). The scoring table should not count it toward the "ALL MECHANICAL PREDICTIONS" line; the script's own line correctly lists P1-P3, P5 only. Consistent, just keep it that way at integration.
- **MINOR-4.** "Zenodo records are unrevised" (versions ledger) is stated as fact in the "removes" section, but the Limits section says the quote check does not show the live pages are unchanged since fetch. Date the claim to the fetch ("unrevised as fetched on <date>").
- **NOTE-1.** E4 matched only after normalisation (sha recorded); acceptable under the pre-registered P1 wording. Q105 matched exactly in `comments.json`.
- **NOTE-2.** Day's "does not touch his repaired algebra" is correctly treated as a supply-ratio statement; the write-up does not claim the 330,000 figure has a source (rule F kept).

## 2. Day-side steelman
- **MINOR-5.** Day can say the concession was always scoped: the 08-27 post (para 3) already carries the covariance objection, and the post withdraws only the N/N_e leg. The write-up credits this, but the "Removed" bullet reads as if Day withdrew the whole B4 recalibration. Day's own text withdraws the algebra, not (in the quotes checked) the 200-580 kya clock by name. The B4 reversal is the repo's inference from eq. (7) with ratios set to 1, not a quoted Day statement. Label it "follows from, not stated by".
- **NOTE-3.** Q105 (1/(2N_e), 09-15) vs E4 (1/(2N), 10-06): in an ideal population N = N_e, so Q105 can be shorthand. Correctly left as a versions-ledger item, not an error (R1).
- **NOTE-4.** Credit stands: correcting a load-bearing formula publicly within a day.

## 3. Critic-side steelman
- **MINOR-6.** The critics (keruru, McCarthy) can add that the concession arrives with the still-uncorrected Zenodo records and the B3f 800,000 line, so any reader of the papers still meets the withdrawn numbers. The write-up says this; it could also note that 0.743 and 32.3 being "not removed" is a classification the critics need not accept: 32.3 has no derivation at all (B3d), so "not removed" should not read as "survives". The write-up's P4 limit gestures at this; make it explicit in the Day-side bullet.
- **NOTE-5.** The write-up correctly declines to decide whether genotype-fecundity covariance bears on neutral P(fix); no model tests it.

## Verdict
Sound; arithmetic reproduces, no post hoc changes. Fix the wording in MINOR-1, 2, 4, 5 before integration. No verdict changes (B3g stays holds / accurate / supported). Counts: 0 MAJOR, 6 MINOR, 5 NOTE.
