# Brief: VID-01 scoring against the claim files (analyst)

Task EVO-76. Written and committed before the task is released (MA-21). Lead: Big Sim.
Agent: `analyst` (Opus). Skill: none of the four exactly fits — this is a **scoring pass**,
closest to `write-up-check`; follow the lifecycle step 3 conventions (results file, "Who this
helps", both sides' positions stated) rather than inventing a new format.

## What this is

EVO-55 harvested the Gutsick Gibbon roundtable (`AqC1ZM4icms`, GG-4). EVO-57 reviewed it
(combined, low-stakes tier). EVO-69 ran the fix pass. **No verdict field has moved from this
source yet. This task is the first one permitted to move one.**

## Inputs, in this order

1. `docs/research/sources/refresh-2026-10-13-video.md` — items 1–5, and the
   "Review resolution (fix pass, 2026-10-13)" section from line 164.
2. `docs/research/sources/quotes-critics.md`, section `YT-AqC1ZM4icms`, **GGR-01..GGR-46**
   (grep the ids; do not read the file whole — token budget).
3. `research/checks/results/REVIEW-R4-VID-01-combined.md`.
4. `research/checks/briefs/VID-01-operator.md`, rulings **R-1..R-7** in the addendum.
   **The rulings bind and are not reopened.**
5. Claim files: `A4d-d-dropped-in-mittens-3.md`, `A5h-supermutator-38400-slip.md`,
   `A-mittens-formula.md` (TW-01), `A4-turnover-coefficient-d.md` (`derived:`),
   `A5e-human-derived-rate-27600.md`, `G-bernoulli-barrier.md`, `G1-*`, `G5-matev-cv-*`,
   `Ge-bb-omitted-from-3-0.md`.
6. Rule RD and the rest of the verdict rule:
   `research/checks/results/R4-X1-verdict-rule.md`.

## The MITTENS 3.0 text is not on this workstation

`sources/raw/` was cleared; `sources/raw/day/zenodo-23003785.txt` no longer exists. Items 1
(readings b vs c) and 4 (NOTE-5) cannot be settled without it.

**Re-fetch it** under hard rule 4: read-only `curl` into **its own new directory**
`sources/raw/vid01-score-2026-10-13/`, never executed, text extracted with
`research/.venv/bin/python -I` (local, one process, seconds — within the workstation limit).
Record the sha256 of each file and **compare with the pinned values in `bib-day.md` line 50/51**
(`22bb4ef8eae7d5c4756987e5418bf26d795ac65e58f36072c393735bdf7a37b2` for the main file,
`d55e8a03...` for the addendum). The Zenodo record was already modified once (2026-10-04).
**If a hash differs, stop scoring items 1 and 4, record the diff as a versions-ledger finding,
and say so** — a changed text is a separate result, not a silent substitution.
No full text in git (hard rule 3): hashes and short quotes only.

## What this task must settle

**1. The d-coefficient conflict (GGR-13/GGR-14 vs A4d).** The video: Day "is still using the d
coefficient in mittens", 450,000 generations × d → "like 225,000". A4d: `internal: holds`, no d
term in MITTENS 3.0, 252,000 nominal generations. Three RD readings are recorded with sources
in refresh item 1 and the GGR-13 note; ruling R-3 declared no winner and left A4d untouched.
**Score it under rule RD now.** Record every plausible reading with its verdict; the field takes
the reading under which *the quoted statement* is most defensible — not the reading best for
either side — with a `reading-dependent:` comment and a Readings table, and it counts separately.
Re-run A4d's own text search ("turnover", "d =", "d=", "0.45", "Bio-Cycle") over the re-fetched
3.0 body **and** Appendix D, and report the hits verbatim with locators. That search settling
(b) vs (c) is the point of the re-fetch.

**2. A5h (GGR-33/GGR-34).** The objection contradicts the model behind A5h but not its direction;
both halves sit in one note under ruling R-2, neither applied. **Decide whether anything moves.**
A5h is `internal: arithmetic-error`, `external: pending`. If the honest answer is "nothing moves,
and here is why", that is a result — say it, with the reason, and leave the fields alone. If the
external field moves, note the cost to the critics that R-2 records (on their own e^-U at the
corrected U = 384, carrier fitness ≈ 1.7e-167, and the s = 0.001 escape of 0.68 disappears):
adopting their modelling objection strengthens Day's stated direction. Both halves go in the
write-up, equally prominently.

**3. Branch G (GGR-41..GGR-44 vs GGR-19).** R-1 deliberately left open how far the panel's two
answers — recombination (t=01:57:03, 01:57:44) and the infinitesimal model (t=02:13:47,
02:14:07) — meet GGR-19's coefficient-of-variation / Fisher's-fundamental-theorem formulation of
the barrier. Neither is a derivation; each names a standard mechanism or model. Score against the
branch G claim files and against `R4-G1.md`, whose free-recombination result (joint fixation
1.03 ± 0.02 × p²) and λ threshold (12.3–17.2) are directly on point. State plainly what the
panel's answers do and do not establish, and whether any G-branch verdict or defeater moves.
**Do not let the audit's earlier error against the critics (MAJOR-1) push the scoring the other
way to compensate.** Also engage G5 (Matev: CV falls, variance rises) — it is the audit's existing
node for the same step.

**4. NOTE-5 (GGR-12 vs GGR-20).** Whether the Bernoulli barrier is in MITTENS 3.0. Needs the 3.0
text; settle it against `Ge-bb-omitted-from-3-0.md` and report the search terms used.

**5. The three credits to Day.** GGR-04 (literal concession, governing reading under R-4),
GGR-45, GGR-46 go in the write-up **as prominently as the errors** — hard rule 1, not a footnote.

## Review tier: three reviews

Not the low-stakes tier. `hierarchy.yaml` marks neither A4d nor A5h `load_bearing`, but D-23
triggers twice independently: (i) this registration carries a verdict-field flip (A4d internal,
possibly A5h external); (ii) branch G's G/G1 are listed feeders of load-bearing nodes in
`R5-draft.md` §1.3. So: **correctness, steelman-day, steelman-critic**, three separate reviewer
instances, one after another under the one-agent cap (D-22). State this tier and its two
justifications in the write-up's header so the reviewers do not have to re-derive it.

## Flagged for the reviewers

The EVO-69 fix pass **extended MINOR-1 beyond the ids the review named**: GGR-11 and
GGR-27..GGR-29 were re-attributed to `panel` on the same unsupported-attribution pattern. That
extension has **not** been independently reviewed. The correctness reviewer must check it against
the transcript turns. Note that GGR-27..GGR-29 are load-bearing for item 3 (they are the second
point of the panel's infinitesimal-model answer), so a wrong attribution there affects the branch
G scoring.

## Pre-registration

This is a scoring pass over a committed record, not a simulation, so there is no run to
pre-register. **But** write the predictions down first: before opening the 3.0 text, commit a
short "Predictions" section in the results file giving, for each of the five questions, what each
side's position predicts you will find and which verdict each outcome would produce (hard rule 5).
Then fetch, then score. Anything you change after that is labelled **post hoc** in a separate
commit.

## Files this task may write

- `research/checks/results/R4-VID-01-score.md` (new; the results file).
- `docs/research/claims/A4d-*.md`, `A5h-*.md`, and any branch-G claim file a scored verdict moves
  — **verdict fields and comments only**, with the R4 paragraph lifecycle step 6 requires.
- `docs/research/ledgers/` rows where a reading or a credit belongs there rather than in a verdict.

**Not** this task: `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `hierarchy.yaml`, the argmap, the board,
the counts refresh — all of that is the integration task after the three reviews and the fix pass.
Also not this task: NOTE-6, the unpinned `yt-dlp` against `requirements.txt` and
`HOWTO-refresh.md` §5 (bookkeeping task).

## Standing constraints

One agent at a time (D-22). Never two agents on the same shared file. Another run (EVO-28,
L5-C1a design) holds the workspace concurrently — it touches branch L and C1a, not these files;
commit with explicit paths and `git pull --rebase` before committing. No computation on the
workstation beyond a trivial check (one process, <500 MB, <1 min); `na-workhorse` is busy with
`ph2` until 2026-10-16 and nothing here needs it. Verbatim quotes with locators and dates only.
Report back in ≤300 words: commits, what moved, what did not, failures, next step.
