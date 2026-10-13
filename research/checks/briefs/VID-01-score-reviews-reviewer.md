# Brief: three reviews of R4 VID-01-score (reviewer)

Task EVO-76, review stage. Committed before the reviews are released (MA-21). Lead: Big Sim.
Agent: `reviewer` (Opus), a **fresh instance each time** that did not author the work and did not
write either of the other two reviews. Three tasks, **one after another** under the one-agent cap
(D-22).

| # | Review | Skill | Output file |
|---|---|---|---|
| 1 | correctness | `review-correctness` | `research/checks/results/REVIEW-R4-VID-01-score-correctness.md` |
| 2 | steelman, Day's side | `review-steelman` | `research/checks/results/REVIEW-R4-VID-01-score-steelman-day.md` |
| 3 | steelman, critics' side | `review-steelman` | `research/checks/results/REVIEW-R4-VID-01-score-steelman-critic.md` |

## Why three and not one combined

Not the low-stakes tier. `hierarchy.yaml` marks neither A4d nor A5h nor Ge `load_bearing`, but
D-23 triggers twice independently: (i) the registration carried a verdict-field flip and one was
applied (**Ge `internal` `pending` → `holds`**); (ii) branch G (G, G1) is a listed feeder of a
load-bearing node in `R5-draft.md` §1.3, and Q3 scores against it. Do not re-litigate the tier.

## What is under review

`research/checks/results/R4-VID-01-score.md` — predictions pre-registered at commit `e857d1f`
**before** the MITTENS 3.0 text was re-fetched; results and claim-file edits post hoc at `31d7f0d`.
Brief: `research/checks/briefs/VID-01-score-analyst.md` (`9e96f51`). Upstream and binding:
lead rulings **R-1..R-7** in `research/checks/briefs/VID-01-operator.md` — **not reopened.**

Claim files touched: `A4d-d-dropped-in-mittens-3.md` (comment and R4 paragraph only, verdict
unchanged), `A5h-supermutator-38400-slip.md` (unchanged), `Ge-bb-omitted-from-3-0.md`
(**`internal` moved**).

Both fetch directories are present and readable (gitignored, do not commit their contents):
`sources/raw/vid01-2026-10-13/` (transcript, captions, info.json) and
`sources/raw/vid01-score-2026-10-13/` (the re-fetched MITTENS 3.0 `main.txt`, `addendum.txt`,
PDFs, `record.json`). You can therefore re-run every search and re-check every quote yourself.
**Do this rather than trusting the write-up's counts** — that is the whole point of review 1.

## Review 1: correctness

Recompute, do not read. Specifically:

1. **Gate G0.** `sha256sum` both PDFs against the pinned `bib-day.md` line 50/51 values
   (`22bb4ef8…`, `d55e8a03…`). If they do not match, everything downstream of Q1 and Q4 falls.
2. **Every token count in Q1 and Q4.** Re-run the searches over `main.txt` **and** `addendum.txt`:
   standalone `d`, `0.45`, `450,000`, `225,000`, `202,500`, `252,000`, `turnover`, `selective
   turnover`, `Bio-Cycle`, `overlapping generations`, `Bernoulli`, `Averaging`, `averaging
   problem`, `law of large numbers`, `load`. The write-up claims specific counts (0, 0, 0, 0, 0,
   10×, one unrelated hit, …) and "252,000 … never multiplied". Check each, including that the
   PDF-to-text extraction did not swallow a standalone `d` or hyphenate a number across a line
   break — a false zero here is the one failure mode that would silently rescue A4d.
3. **Every GGR quote the write-up relies on**, as an exact substring of
   `sources/raw/vid01-2026-10-13/AqC1ZM4icms.transcript.txt`, with the `t=` matching the caption
   chunk: GGR-04, 12, 13, 14, 19, 20, 27–29, 31–34, 41–46.
4. **The flagged MINOR-1 extension.** The EVO-69 fix pass re-attributed **GGR-11 and
   GGR-27..GGR-29** to `panel` on the unsupported-attribution pattern, beyond the ids review
   EVO-57 named. That extension has had **no independent review**. Check each against the actual
   transcript turns: was a name spoken in or adjacent to the turn or not? GGR-27..GGR-29 are the
   second point of the panel's infinitesimal-model answer and so feed Q3.
5. **Every hit/miss call in the scoring table against the registration at `e857d1f`.** Read the
   predictions from the *committed* version, not from the current file. Two misses are
   self-reported (non-exhaustive Q1 band table; the declined RD instruction) — check that no
   further prediction was quietly re-scored as a hit, and that no band was widened after the fact.
6. **The arithmetic**: 252,000 / 1,322 = 190.6; 252,000 × 0.45 = 113,400; 205e6 / 85.8 = 2.39e6;
   450,000 × 0.45 = 202,500; e^−384 ≈ 1.7e−167; 0.999^384 = 0.68.
7. **The Ge move.** Does `internal: holds` follow from the evidence, under the registered band 4a
   as written? Is the `external` field correctly left `pending` with its proposal recorded?
8. **The §8.6 locator correction** in A4d's Weaknesses line: verify that MITTENS 3.0 has no
   Appendix D, that §8.6 reads as quoted, and that the Appendix D cited there is *Day and Athos
   2025*'s.

**Rule explicitly on the RD departure.** The analyst declined the brief's instruction to mark A4d
`reading-dependent:`, on the ground that rule RD governs verdicts that *depend* on the reading and
this one does not — the re-fetched text settles 3.0 under every reading — and that what is
reading-dependent is the critic statement GGR-13/GGR-14, which has no claim file. Read rule RD in
`research/checks/results/R4-X1-verdict-rule.md` and say whether that is right. Give a severity and
a one-line fix either way; the lead will rule if the steelman reviews disagree with you (D-24).

## Review 2: steelman for Day

Argue Day's side as strongly as the evidence honestly allows — not further. Test at least:

- Is the Q1 conclusion **stronger** than the write-up states? It treats reading (a) as governing
  and (c) as "partly accurate" against Day. Does the §8.6 Bio-Cycle citation actually concede
  anything, given that it is a citation to a *different* paper's appendix for a rate, not a
  multiplier on the generation count? If (c) is worth less than the write-up gives it, say so.
- Ge: is `holds` under-stated? Does the single §1 rhetorical mention of "Bernoulli" damage the
  blog claim at all, under rule C?
- Q2: the write-up keeps A5h `external: pending`. Day's side might argue the GGR-34 objection,
  adopted, moves A5h's **direction** toward `supported` rather than leaving it pending. Test it —
  and test it against the fact that A5h's `internal` is `arithmetic-error`, which is not in
  question and which you may not soften.
- Q3: does the panel's recombination answer actually reach GGR-19, or is the write-up too generous
  in calling it "on point against §2"? `R4-G1.md`'s 1.03 ± 0.02 is free recombination; Day's
  position concerns the linked and clonal cases (0.84 / 0.65 / 0).
- Are the three credits (GGR-04 under R-4, GGR-45, GGR-46) given the prominence hard rule 1
  requires, and is GGR-04's governing literal reading correctly applied?

You may **not** reopen R-1..R-7, and you may not argue against A5h's `arithmetic-error` or A4d's
verified absence of a d term — the text is hash-matched and the search is reproducible.

## Review 3: steelman for the critics

Argue the critics' side as strongly as the evidence honestly allows. Test at least:

- **Is band 3b's "on point / adjacent" criterion set too high for a video roundtable?** The
  analyst raised this against itself. A panel naming recombination and the infinitesimal model in
  conversation is not going to derive anything; is "meets GGR-19" being scored at a height no
  spoken reply could clear, and is that the right height? If the criterion is wrong, say what the
  right one is — but note it was fixed before the evidence was read, so a change is post hoc.
- **Ge `internal: holds` turns on reading "omitted" charitably.** Test the opposite: invoking the
  Bernoulli Barrier by name in §1's framing while omitting its defence is having it both ways.
  The analyst thinks rule C decides it. Does it?
- **Q2's criterion** ("external moves only if the objection weakens the direction") may be too
  demanding — one could argue `contested` should record any substantive located objection. It was
  registered before looking, so disagreeing makes the change post hoc. Say which way the
  vocabulary in `R4-X1-verdict-rule.md` actually cuts.
- Reading (c) at Q1: is it worth **more** than "partly accurate"? An overlapping-generations
  correction is still in play inside the §8.6 rate while d is dropped from the generation count,
  and 3.0 nowhere explains that.
- The audit has now made **two** errors against the critics from this one source (MAJOR-1 at
  EVO-57, and NOTE-5's invented panel inconsistency, dissolved here). Is there a third still
  standing in this pass?

**Do not** over-correct for those two errors. The analyst was warned against it in its own brief
and the same applies to you: a steelman is the strongest *honest* case, not a counterweight.

## Common requirements for all three

- Severity labels **BLOCKER / MAJOR / MINOR / NOTE**, each finding with an id (`MAJOR-1`, …) so
  the fix pass can answer it by id. State counts in a header line.
- Quote verbatim with locators. Recompute rather than relay.
- Token budget: grep the big files by id; do not read `quotes-critics.md` or `REVIEW.md` whole.
- Write **only** your own review file. No claim-file edits, no `QUEUE.md`, no `REVIEW.md`, no
  argmap, no board — the fix pass and then the integration task handle those.
- Commit with explicit paths, `git pull --rebase` first, push to `origin research` only.
- Report back in ≤300 words: commit, counts by severity, the findings that would move a verdict
  field, next step.

## After the three

Where the Day-side and critic-side steelman conflict, **the lead rules** (D-24) and writes the
ruling into this brief, committed, before the fix pass. Where a ruling moves the governing reading
of a verdict field, a fresh reviewer checks it before integration. Then the fix pass answers every
MAJOR and MINOR by id, then the integration task (`QUEUE.md`, `REVIEW.md`, `RESULTS.md`, argmap,
lint, counts, the seven items under "Open" in the write-up, and NOTE-6's unpinned `yt-dlp`).

---

# Lead rulings R-8..R-15 (D-24), written before the fix pass

All three reviews are in: correctness `385c443` (0/4/5/7), steelman-day `a22bd78` (0/4/5/6),
steelman-critic `98b820a` (0/5/5/6). None moves a verdict field: **A4d `internal: holds`,
A5h `arithmetic-error` / `pending`, Ge `internal: holds` all survive all three.** The rulings below
bind the fix pass and are not reopened by it. Where I rely on a fact I checked it myself; the
locator is given so the fix pass and the next reviewer can re-check me.

**R-8 (Q1 reading (c): steelman-day MAJOR-1/2 vs steelman-critic MAJOR-1/2). Reading (c) keeps
`partly accurate`; the Day-side regrade to "contradicted" is declined — but its evidence is
adopted, against the critic review's dismissal of it.**

Both steelmen are partly right and neither wins outright.

- For the critics: `C2-bio-cycle-d.md` title line defines Bio-Cycle as `g_eff = d x g_nominal`.
  MITTENS 3.0 §8.6 cites a rate "calculated ... using Kimura's fixation time formula and the
  Bio-Cycle correction for overlapping generations ... approximately one fixation per 27,600
  **effective** generations". A rate denominated in *effective* generations has d inside it by
  definition. **A token search establishes the absence of the symbol `d`, not the absence of the
  correction.** GGR-13's core assertion — that the d correction is still in play in "mittens" — is
  therefore accurate as to 3.0.
- For Day: GGR-14's elaboration — that he computes 450,000, multiplies by d, and "is still using
  that number for all his math" — is **not** accurate as to 3.0. The steelman-day evidence
  discriminates here and the steelman-critic's "discriminates nothing" is **overstated**:
  252,000/27,600 = 9.13 against a printed 8 (a 12% gap `A5e` line 26 already records as
  unreconciled), versus 113,400/27,600 = 4.11, which is off by a factor of two. The printed 8 is
  consistent with the **uncut** 252,000 and not with a d-cut count.

Accurate core, inaccurate elaboration, is exactly what `partly accurate` means. The two findings
do not conflict once each is confined to the proposition it actually bears on: GGR-13 and GGR-14
are not the same assertion and must be scored separately in the Readings table.

**R-9 (governing reading: correctness MAJOR-3, steelman-critic MAJOR-1, steelman-day NOTE-3 —
concordant). Reading (a) is struck as governing; (c) governs among in-scope readings.**
Rule RD line 202, verbatim: "Extended readings (a different object, or a wider claim) are reported
with their own verdicts but cannot set the verdict field or the headline tag." Reading (a) is the
pre-3.0 / *Probability Zero* line — a different object from MITTENS 3.0. It stays in the Readings
table with its `accurate` verdict and its TW-01 cross-reference; it may not set the headline.
All three reviewers reached this independently and the Day-side steelman agrees Day does not need
it. **This moves the governing reading, so under the lifecycle a fresh reviewer checks it before
integration** — ordered below.

**R-10 (correctness MAJOR-1/2 vs steelman-day NOTE-2: t=01:49:52). Re-label, keep, and strip of
its corroborating role.** The turn is **GGR-11**, attributed `panel` by the EVO-69 fix pass and
confirmed by the correctness review's transcript check. Three files call it "the host's own
narration": the write-up, `A4d` (R4 paragraph), and **`quotes-critics.md` line 846**, which the
reviews did not name but which carries the same error and the claim that it is "evidence for
(a)/(b) over (c)". All three are corrected. The quote is **not deleted** (steelman-day NOTE-2 is
right): it is a real panel turn and it does support A4d's substance. But it cannot corroborate
reading (a), because the panel is speaking **about 3.0** and GGR-13 is the reply disagreeing with
it. What it shows is that the panel is internally split about 3.0 — which is worth recording in
its own right, and is a point for Day.

**R-11 (correctness MINOR-5 vs steelman-day MAJOR-4 and steelman-critic NOTE-1: the 1.03 ± 0.02
figure). Correctness MINOR-5 is NOT applied.** I checked `R4-G1.md` myself: line 163 is the free
row, pair ratio **1.029 ± 0.022**; line 164 is linked 1 M at **1.015 ± 0.022**. Both steelmen
reached this independently and both are right. A correctness finding is not privileged over two
concurring steelmen plus the source table. The fix pass records it as "not applied, with reason",
and does not silently drop it.

**R-12 (Q3 human density: steelman-day MAJOR-2 vs steelman-critic MINOR-1). The refinement is
weakened, not deleted; both sides' qualifications ride with it.** Each is factually right and
`R4-G1.md` supports both, so the write-up must carry both or neither:
free recombination is Day's own stipulation (s7.10) and gives independence at 1.029 ± 0.022
(line 163); the **only pre-registered** linkage row **failed** (predicted 0.5-0.95, got 1.015,
line 172); the tighter maps giving 0.84 / 0.65 are **labelled post hoc** (lines 165-166); and
~4,500 loci/M "between the two tight maps" (line 173) is an **interpolation, not a run** — no
run exists at human-relevant density. Every clause above goes in. Neither steelman may carry
more weight than its row.

**R-13 (steelman-critic MAJOR-3: the "clean of the d coefficient" headline). Accepted.** Given
R-8, the phrase overstates what a token search can establish. It occurs at `R4-VID-01-score.md`
lines 477 and 502 and in `A4d` line 12 — fix all three to the defensible form: *3.0 contains no
`d` term and applies no d multiplier to its generation count; an overlap correction survives by
citation inside the §8.6 rate.* This is the **third** audit error against the critics from this
source, and the fix pass says so plainly, as it would for a Day-side error.
**Out of scope here, routed on:** `C2-bio-cycle-d.md` line 8 makes the same unqualified assertion
("MITTENS 3.0 ... drops d") in the `load_bearing: true` comment of a load-bearing node. It is
**not** this task's to edit. The integration task raises it, and because C2 is load-bearing it
gets its own tier, not a drive-by edit.

**R-14 (steelman-critic MAJOR-5: Q2's registered criterion vs the audit's operative `contested`).
Recorded, not acted on.** A5h `external` stays `pending`: all three reviews agree the field does
not move, and the registered criterion was fixed before looking. But if MA-08 is right that the
audit's operative `contested` is looser than the criterion registered here, that is an
inconsistency in the **vocabulary**, not in this check. Changing it is a rule change and takes the
freeze procedure in `DECISIONS.md`. The fix pass records it and routes it to the batch-15
criticality pass. It does **not** rescore Q2.

**R-15 (the remaining uncontested findings).** Apply as written, by id:
steelman-day MAJOR-3 (all three "Open" proposals run against Day; add the two symmetric items it
names — A5h's now-inaccurate "In support: none located", and the GGR-11 turn into A4d's Responses
— plus a Day-side defeater; hard rule 1 is the reason, the same reason the Day-side findings were
applied); steelman-critic MINOR-2 (Ge's §1 clause under RH3); steelman-critic MINOR-5 (band 3d
was never checked though a candidate exists at t=01:55:19 — check it and score it);
steelman-critic MINOR-4 (band 3b is **not** too high — a finding against the reviewer's own side,
which closes the question the brief asked and needs no change).
**The correctness review's ruling on the declined RD instruction stands: the analyst was right.**
Rule RD line 198 — "A claim whose formal statement fixes the reading ... is `SCOPED`, not
reading-dependent" — and A4d's Formal statement fixes it. No `reading-dependent:` comment, no
separate count. **The defect was in my registration, not in the analyst's execution**, and the
fix pass records it that way.

## What happens next, in order

1. **Fix pass** (analyst): answer every MAJOR and MINOR of all three reviews by id in a "Review
   resolution" section, including the ones ruled *not applied* (R-11, R-14) with their reason.
   New computation is labelled **post hoc**. May write: the write-up, `A4d`, `A5h`, `Ge`,
   `quotes-critics.md` (the line 846 correction under R-10), `ledgers/slips.md` (RH3 under R-15).
2. **Fresh reviewer check of R-9** before integration, as the lifecycle requires for a ruling that
   moves a governing reading. Narrow scope: the Readings table and the headline only.
3. **Integration** (operator): `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, argmap ids and defeaters,
   lint, counts, the seven "Open" items, the C2 referral from R-13, the MA-08 referral from R-14,
   and NOTE-6's unpinned `yt-dlp`.
