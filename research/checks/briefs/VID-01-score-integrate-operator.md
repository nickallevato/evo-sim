# Brief: integrate R4 VID-01-score (operator)

Task EVO-76, lifecycle step 6. Committed before the task is released (MA-21). Lead: Big Sim.
Agent: `operator` (Sonnet). Skill: `integrate-check`. One agent at a time (D-22); never two on a
shared file.

## State: everything upstream is closed

| Stage | Commit | Result |
|---|---|---|
| Registration (predictions, before the re-fetch) | `e857d1f` | byte-identical since; hard rule 5 intact |
| Results + claim edits | `31d7f0d` | — |
| Review 1, correctness | `385c443` | 0 BLOCKER / 4 MAJOR / 5 MINOR / 7 NOTE |
| Review 2, steelman-day | `a22bd78` | 0 / 4 / 5 / 6 |
| Review 3, steelman-critic | `98b820a` | 0 / 5 / 5 / 6 |
| Lead rulings R-8..R-15 (D-24) | `9699aa9` | in `briefs/VID-01-score-reviews-reviewer.md` |
| Fix pass (13 MAJOR, 15 MINOR answered by id) | `88c444d` | — |
| Fix pass, post hoc (band 3d) | `83f4f4d` | — |
| Fresh check of R-9 (governing reading) | `13b0fc3` | **sound, applied faithfully, nothing blocks integration** |

**One verdict field moved in the whole task: `Ge internal: pending -> holds`.** A4d `holds`,
A5h `arithmetic-error` / `pending` are unchanged and were confirmed by all three reviews.

## Do not re-open

The rulings R-1..R-7 (`briefs/VID-01-operator.md`) and R-8..R-15 (`briefs/VID-01-score-reviews-reviewer.md`).
No verdict field moves in this task. If integration seems to require one, stop and report instead.

## 1. Shared files

- `research/checks/REVIEW.md`: one entry for this check — the three reviews, the R-9 check, their
  counts, the rulings commit, the fix pass. Log only; the queue lives elsewhere.
- `research/checks/QUEUE.md`: mark VID-01 scoring **DONE**, with the referrals in §4 below as new
  open items. Remove the stale "unblocks the analyst scoring task" wording from the 0a entry.
- `research/checks/RESULTS.md`: the one-paragraph result. It must say that one field moved (Ge),
  that A4d and A5h were tested and held, and that the pass found three audit errors against the
  critics and corrected its own headline.
- `research/checks/PREREG-STATUS.md`: regenerate with `research/tools/prereg_status.py`. This
  check is a **single-commit registration with a blind gate** (predictions committed and pushed
  before the text was fetched); let the tool classify it, do not hand-edit.

## 2. Argmap

- Register `chk:VID-01-score` in `argmap/NOTES.md`, with review ids for the three reviews **and**
  the R-9 check (it is a fourth review artefact, not a fix-pass note).
- `defeaters.yaml`: next free `dNNN`, **both sides where warranted** — at minimum the Day-side
  defeater the steelman-day MAJOR-3 asked for, and the critic-side one from write-up Open item 3
  (§2's "No recombination overhead" bullet, citing GGR-42 and `R4-G1.md`'s 1.029 ± 0.022).
  Note the reading dependence of GGR-13/GGR-14 on the relevant defeater (RD bullet 3).
- Lineage node; mini-form in `argmap/standard-forms.md`.

## 3. Checks, counts, figures

`research/tools/lint_research.py --write-hierarchy`, then `research/tools/argmap_check.py`, then
`argmap_render.py`. Refresh counts in `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`
(the Ge move changes them). Then `research/tools/readme_figs.py`, and `git checkout` any SVG whose
only diff is a random id.

**Reading-dependent counts:** the R-9 check confirmed `HANDOFF.md` line 91 and
`docs/arguments/README.md` line 105 are untouched and should stay so — A4d is **SCOPED, not
reading-dependent** (rule RD line 198; its Formal statement fixes the reading). Do not add it to
that count. If the lint disagrees, report rather than "fix".

## 4. Referrals — raise as queue items, do NOT execute here

1. **`C2-bio-cycle-d.md` (ruling R-13).** Its line 8 asserts MITTENS 3.0 "drops d" without the
   qualification R-8 established (an overlap correction survives by citation inside the §8.6
   rate, denominated in *effective* generations). **C2 is `load_bearing: true`, so this gets its
   own three-review task.** Do not edit C2.
2. **MA-08 / the `contested` vocabulary (ruling R-14).** The registered Q2 criterion is stricter
   than the audit's operative `contested`. A rule change: it takes the freeze procedure in
   `DECISIONS.md`. Route to the **batch-15 criticality pass**, which must also cover the D-23 tier
   change already queued.
3. **`Ge external: pending -> contested`** (write-up Open 1). Proposed, outside the registered
   bands. **A verdict move, so not an operator task** — queue it as a scored follow-on.
4. **A new critic-side node for the infinitesimal-model answer** (Open 2, GGR-43/GGR-44, child of
   G). You **may** create this one, because it carries no verdict: `internal: pending`, Statement
   verbatim from the quotes file with its `t=` locator, `_TEMPLATE.md` structure, side `critic`.
   If anything about parent or edges is unobvious, queue it instead.
5. **GGR-46 into `A4`'s Responses** (Open 4) — A4 was outside the scoring task's file list. A
   quote already harvested and credited; add it.
6. **Balance-ledger row for branch G** (Open 5), best-for-each-side as the write-up states.
7. **The lost `sources/raw/day/zenodo-23003785.txt`** (Open 6). A4d's `holds` rested for some days
   on a search of a file the audit no longer had. Whether to re-establish a canonical local copy
   is a **bookkeeping decision for the owner** — raise it, do not decide it.
8. **GGR-19's Reddit original is unlocated** (Open 7); branch G is scored against a relay (rule U).
9. **NOTE-6: the unpinned `yt-dlp`** (2026.8.19, installed `--no-deps`) against
   `research/requirements.txt` and `HOWTO-refresh.md` §5. This is the bookkeeping item carried
   over from EVO-69 and it is **in scope for you**: pin it or document why not, and update §5.

## 5. Two small corrections from the R-9 check

- **MINOR-1:** stale self-locators — the write-up says "lines 477 and 502" at what are now lines
  799 and 983. The fix itself is done; only the locators are stale.
- **NOTE-2:** the Readings tables say "partly accurate", which is not in the fidelity vocabulary
  (`accurate | partial | misread | unverifiable | pending | n/a`). **No field is mis-typed** — this
  is prose in a Readings table, inherited from ruling R-8. Normalise the wording to `partial`
  where it is used as a verdict value, and leave it as prose where it is plainly prose. If that
  distinction is unclear anywhere, leave it and report.

## 6. Do NOT publish, and do not merge to master

- **No board patch and no republish in this task.** The `Ge` move makes the published board stale,
  and under D-26 a board may not be published that was written before a verdict field moved — so
  the patch must be built against the files of record at the **batch close**, not now. Record in
  `QUEUE.md` that the live board is stale with respect to `Ge`.
- **No `git push origin research:master`.** Other work is in flight on `research` (EVO-28 L5-C1a,
  EVO-43 L2) and master also serves the public Pages board. Merging is the batch-close step.
- No milestone post here.

## Constraints

Push to `origin research` only. Commit with explicit paths, never `git add -A`; `git pull --rebase`
first — another run holds the workspace concurrently. No computation beyond the lint and render
tools (local, trivial). `na-workhorse` is busy with `ph2` until 2026-10-16 and nothing here needs
it. Report in ≤300 words: commits, which shared files changed, the counts before and after, the
queue items raised, anything you stopped on rather than forced.
