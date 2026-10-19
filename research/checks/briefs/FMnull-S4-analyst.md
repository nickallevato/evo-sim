# Brief FMnull-S4 (analyst): criterion S4 and the Poisson re-estimate

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

## Goal

Finish the two pieces `R4-FMnull.md` registered or named and did not run:

1. **Criterion S4 — tree-incongruent sharing above the ILS rate.** S4 was registered and
   never run. Either run it or **drop it with a stated reason written into the results
   file**; an unrun registered criterion is a pre-registration defect, and the criticality
   layer will score it as one either way. Say which you did and why, in the registration
   language.
2. **The Poisson GLM re-estimate of the covariate-adjusted index.** Needed only if S1's
   covariate clause is to be used. It needs `fm_bins.npz`, which lives on `na-workhorse`.
   If you conclude the covariate clause is not going to be used, say so and skip it —
   explicitly, not silently.

Both are **post hoc** relative to the original FMnull registration. Label them so, in the
docstring and in the write-up, and commit the script before the run (rule 5).

## What the lead has already seen

- `research/checks/results/R4-FMnull.md` (integrated 2026-10-13, reviews #76-#79, fix pass
  `2802425`): Day's "> 80 times more variable" is true at W ≥ 1 Mb in every lineage and
  never outside the neutral band where true (index / N_hi 0.11-0.91); little power below a
  dominant block mechanism. **No verdict value moved**: FM3 external `supported` as a
  description and non-discriminating; FM10 internal `pending` (owner decision); no defeater
  against FM10 licensed.
- The ILS sigma upper edge (0.30-0.54) is one of the write-up's **unsourced brackets**. S4
  is a test against the ILS rate, so it stands or falls on that bracket: source it or carry
  it as a declared range across the whole result, and register the band before you look.
- Two items the integration left for the lead, **not yours**: the criticality-layer record
  beside ST-10, and the DECISIONS.md proposal for a fair Day-side criterion (K12).

## Review tier

**Load-bearing: three reviews** (correctness, steelman-day, steelman-critic). FMnull feeds
**FM3** and **FM10**, both marked `load_bearing: true` in `docs/research/hierarchy.yaml`,
and S4 is the criterion most able to move FM10's internal verdict off `pending`. Register
in advance, exhaustively, which S4 outcomes would license a defeater against FM10 and which
would not — the previous round's S2 criterion defect (write-up C8, D10: a margin symmetric
about the stacked upper corner, taken on the value) is the failure mode to avoid.

## Files you may write

- `research/checks/fmnull_s4.py` (or similarly named; pre-registered, committed before the
  run, predictions and bands in the docstring)
- `research/checks/results/R4-FMnull.md` — **new sections only**, appended, labelled post
  hoc; do not rewrite the scored sections
- `research/checks/results/raw/` outputs and the `.host` record

Not yours: claim files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers, the argmap data,
`DECISIONS.md`, the criticality folder.

## Constraints

- `AGENTS.md` hard rules and token budget. Read `R4-FMnull.md` by heading, never whole.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16 02:00-08:00 -06:00.** Nothing
  launches there before the `ph2` collect task is done. Design, pre-register and smoke-test
  locally (one process, under 500 MB, under a minute); the run is a separate later task.
  When it does run: at most 11 busy processes across all agents, RAM under ~12 GB, check
  `uptime` first, launch with `< /dev/null`, record hostname and md5s in `raw/<x>.host`.
- Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits (the pre-registration commit first); the registered bands for S4 and which FM10
moves each would license; whether the Poisson re-estimate is in scope and why; failures;
next step.

## Lead ruling before the write-up (Big Sim, 2026-10-18, S4-R1..R8)

Added after the collect (`ef81a45`) and before EVO-16 starts, so the write-up is scored
against the registration and not against the result. The run is complete and clean: the full
registered grid at the registered 1000 Mb (no fallback), all 48 corners plus `central`, Q1,
Q2 and T1-T6 present, no error or traceback in any `fmnull_s4*.out`, peak worker RSS 334 MB,
`fmnull_s4.done` written 20:43:27 UTC. Nothing here is a re-reading of a band; where the
registration is silent or wrong, the ruling says so and leaves it silent or wrong.

- **S4-R1. Score as registered; the governing outcome is `S4-MARGINAL`.** `AGGREGATE`
  prints `S4-MARGINAL` on F2, F3 and F0, F2 governing. Per the registration's VERDICT MOVES:
  **no value moves**, the result is reported for **both** sides as undecided, and **no
  defeater** is licensed in either direction. FM3 and FM10 are untouched; FM10 internal stays
  `pending` under D-09 and FM10 external stays `contested`. No `verdict_scope` field moves,
  so the fresh-reviewer requirement for a value-moving ruling (AGENTS.md step 4) does not
  fire. Review tier is unchanged: **three reviews, run one after another** under D-22.
- **S4-R2. The aggregate rests on exactly one scored cell, and the write-up must say so in
  the headline, not in a footnote.** `aggregate()` scans `WS` = 10-1000 kb only (3000 kb is
  `WS_DATA`, reported and unscored). Within F2 and `WS` there is exactly one `MARGINAL-OUT`:
  **phi_R at 1000 kb** (15.925). phi_A is `CRITIC` at every scored W from 30 kb up and the
  mesa counts M are `CRITIC` at both 30 and 100 kb. So the one cell that lifts the governing
  aggregate off `S4-NOT-MET` is S4-R, the reading the registration itself predicted would be
  wide (P3 audit: "the FULL band is NON-DISCRIMINATING (width > 9) at W >= 300 kb"), and its
  measured width there is **9.54**, i.e. over the registered threshold.
- **S4-R2b. P2, the one clean critic-side hit, rests on infinitely wide bands, and the
  write-up says so where it reports the hit.** Every scored mesa cell has `E_lo = 0`, so by
  the registration's own counts formula the band width is **infinite** and the
  `NON-DISCRIMINATING` label attaches to all of them — F2 at 30 kb (M = 2, band 0 to 90.7)
  and at 100 kb (M = 0, band 0 to 9.3), and the same at F3 and F0. A `CRITIC` that no value
  below the upper edge could have failed is not evidence for the critic side, and the
  registration anticipated exactly this ("if the CRITIC classes are NON-DISCRIMINATING, the
  item says so"). Under S4-R1 no item is licensed at all, so nothing turns on it; report it
  anyway, beside P2, as the audit's finding against its own criterion.
- **S4-R3. That does not license a reclassification, and I am refusing the obvious one.** The
  `NON-DISCRIMINATING` label was registered as a label "on CRITIC and MARGINAL-IN" only, so by
  the registration's own text it does **not** attach to a `MARGINAL-OUT` cell, and nothing in
  the aggregate rule discounts a wide cell. Extending the label to `MARGINAL-OUT` — which
  would flip the governing aggregate from `S4-MARGINAL` to `S4-NOT-MET` — is a **rule change**,
  post hoc, and goes through the freeze procedure in `DECISIONS.md` as its own proposal if
  anyone wants it; it is not done inside this write-up. Record the gap as a **limitation of
  the criterion**, with the width, under a heading a reader cannot miss. Note in the same
  place that it is immaterial as to verdicts: `S4-MARGINAL` and `S4-NOT-MET` both move no
  value and neither licenses a defeater against FM10, so no side gains or loses from the gap.
  It is a defect of the audit's own criterion, and that is where it is booked.
- **S4-R4. P4 failed, the registered contingency fires, and the replacement text must state
  the measured power with its sign.** P4 `hit: false`. The failure is **only** on the mesa
  count M at 30 kb, under both planted Q168 models: Q1 4.079 against a central 8.159, Q2
  2.830 against 7.547, each outside the registered `max(20%, 3)` tolerance. Every other P4
  cell held, and **no planted class differed from its central class anywhere** (all
  `CRITIC` -> `CRITIC`) — the "leaves every class unchanged" half of P4 held in full.
  Direction matters and the write-up must not round it off: Q168 blocks move the mesa count
  **down**, to roughly half the central value, not up. So the replacement for the "no power
  against Q168" clause is **not** "S4 has measured power against Q168"; it is that the one
  statistic that responds to Q168 at all responds in the **wrong direction**, pushing S4-M
  toward the critic-side classes. A `CRITIC` on S4-M therefore remains unreadable as evidence
  against Q168's mechanism, and on this run the registration's severity paragraph is
  strengthened rather than weakened. State it that way, in the registration's language, and
  label the whole paragraph post hoc. **No value moves either way**, as the registration says.
- **S4-R5. S4 is reachable for Day; the S2-style criterion-defect clause does not fire.**
  `S4_unreachable_for_Day: false`. T5 is `DAY` on S4-A at 1000 kb and T4 is `MARGINAL-OUT`
  or `DAY` on S4-A at 100 kb, so Day's band is demonstrably reachable by a process of the
  registered kind. The P5 **conjunction** nevertheless reads `hit: false`, on one leg: T2 is
  **not** `DAY` on S4-M at 100 kb. Report both facts in the same breath — the conjunction
  missed, and the thing the conjunction was protecting against (an unreachable band scored
  against Day, the S2 failure) did **not** happen. Do not report the miss as if S4 were
  unreachable, and do not report the reachability as if P5 had passed.
- **S4-R6. The audit's own misses are reported as prominently as anyone's (hard rule 1), and
  with their margins.** P1 is `false` on all three sides: the critic-side leg fails only
  because phi_A at 10 kb is `BELOW-NEAR` (1.489), and the **audit's** own leg fails because
  that same 1.489 is under its pre-registered floor of 1.5 — by 0.011, about 0.7%. One value
  drives both misses. Pre-registration is binding, so both are recorded as misses; but each
  must carry its margin in the same sentence, and neither may be inflated into a substantive
  critic-side or audit-side failure. The second half of the audit's P1 leg held
  (phi_A(1 Mb) / phi_A(10 kb) = 1.78, inside the registered 3). P3's audit leg also failed,
  and partially: width 6.40 at 300 kb (under 9) against 9.54 at 1000 kb (over). P2 is the one
  clean critic-side hit (`critic: true`, `day: false`). P7 held (n_mean 48.1, q-bar 0.304,
  a 0.459, all inside their registered brackets). **P6 failed, and it is the audit's bracket
  that is wrong, not the simulator** — every failing leg fails by a small margin at a bracket
  edge. Incongruent-topology fraction: the 35k-N_HC corners come in at 0.186-0.235 against a
  floor of 0.20, and `c_95k_35k_r1.0e-08_h1_bgs0` at 0.461 against a ceiling of 0.45; both
  ends straddle the registration's own HAND values (0.213 at 35k, 0.438 at 95k), so the
  bracket was cut too narrow around its own prediction. q-bar: the four `c_95k_55k` corners
  read 0.4035-0.4056 against a ceiling of 0.40, over by at most 1.4%. The full-exposure `a`
  leg held everywhere (0.4986-0.5026). P6 is a set-up check, so the write-up
  must settle it **before** interpreting any S4 number, and say plainly that a bracket miss of
  this shape puts the bracket in doubt rather than the null — while still recording it as a
  registered miss with its margins, per the first half of this ruling.
- **S4-R6a. Amendment to S4-R6's P6 detail (Big Sim, 2026-10-19), accepting W1 of the
  write-up.** The write-up (`d0c94e2`, section 9 W1) is right that S4-R6's P6 sentence is
  incomplete, and I have re-read `fmnull_s4_post.json` `predictions.P6.detail` to confirm it.
  The corrected detail: the topology **ceiling** is exceeded by **two** corners, not one —
  `c_95k_35k_r1.0e-08_h1_bgs0` 0.46113 and `c_95k_55k_r1.0e-08_h1_bgs0` 0.4514685; the
  topology **floor** is breached by exactly **one** corner, `c_35k_35k_r1.0e-08_h0_bgs0`
  0.185519 (the phrase "the 35k corners come in at 0.186-0.235 against a floor of 0.20" names
  a range, not eight failures). Seven corner-legs fail in total (1 floor + 2 ceiling + 4
  q-bar). Nothing else in S4-R6 moves: the margins are still 0.3-7.2%, both ends still
  straddle the HAND values 0.213 / 0.438, and the reading — the audit's bracket is what is
  wrong, not the simulator — stands. Section 1 of the write-up already reports the raw values
  correctly.
- **S4-R6b. One arithmetic slip in the write-up's section 1, for the correctness review to
  confirm and the fix pass to correct (Big Sim, 2026-10-19).** Section 1 says "The other five
  35k corners read 0.2002-0.2354". There are eight no-BGS 35k-N_HC corners in
  `predictions.P6.detail`, so excluding the one failing corner leaves **seven**, not five; the
  range 0.2002-0.2354 is right (0.2001565 to 0.2353725). This is a count, it changes no call
  and no class, and I record it here rather than leave the three reviewers to each re-derive
  it. It is not a ruling on anything contested.
- **S4-R7. The disagreement across filters is a robustness point and is reported as one.**
  F2, F3 and F0 all aggregate to `S4-MARGINAL`, so the governing outcome survives both the CpG
  filter and the alignment filter. The per-cell disagreements still get reported as registered:
  F3's phi_A is **higher** than F2's at 1000 kb (`MARGINAL-IN` against `CRITIC`), which is the
  opposite direction from the registration's "F3 lower = CpG-dependent" gloss, and F0 is more
  extreme than both (`MARGINAL-OUT` on both statistics at 1000 kb), which is the direction the
  registration predicted for an alignment artefact.
- **S4-R8. Two bookkeeping items the registration already fixed, plus one tooling note.**
  R4-FMnull's "S4 not run" becomes "S4 run post hoc (registered `48241c7`, operationalised in
  `research/checks/fmnull_s4.py`, `75743af`)", and `PREREG-STATUS.md` says so. The Poisson GLM
  re-estimate stays **out of scope** with the reason already accepted on 2026-10-13 (S1's first
  conjunct is unmet on raw phi under every parameter set, and amendment A13 dropped covariate
  correlations as a critic-side criterion), restated in the write-up rather than left implicit.
  Tooling: the sim arm took **12.91 h** against the **2.52 h** the host smoke projected, a
  5.1x miss caused by linear extrapolation from a 2 Mb smoke run; record it as a tooling gap
  against the projection rule, to be re-cut before this script is launched again. It moves no
  number and no verdict.

Where the two steelman reviews conflict, the lead rules in writing before the fix pass
(D-24); that ruling is appended here and committed before EVO-18 starts.
