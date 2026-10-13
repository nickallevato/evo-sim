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
