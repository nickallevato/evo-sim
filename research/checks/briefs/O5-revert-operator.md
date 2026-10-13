# Brief O5-revert (operator): put B internal and A2e external back to `pending`

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/integrate-result/SKILL.md`.
Authority: owner decision **D-21** of 2026-10-13, verbatim: "Put them back to `pending`
until three reviews are done". Do not re-argue the decision; carry it out.

## Goal

Two load-bearing verdict fields moved in Day's favour on 2026-10-11 on one review each,
where the tier rule asks for three (audit finding MA-03). The owner has ruled that both go
back to `pending` until three reviews are done on each. Nothing is being decided about
whether the values were right; they are being un-landed until the process that the rule
requires has run.

1. `docs/research/claims/B-neutral-theory-cannot-rescue.md`, `verdicts.internal`:
   `non-sequitur` → `pending`.
2. `docs/research/claims/A2e-ltee-as-ceiling.md`, `verdicts.external`:
   `contradicted` (scoped) → `pending`.

## How to do it

- **Keep every word of the superseded reasoning.** Move the current comment body into a
  clearly marked block in the same field comment: `SUPERSEDED 2026-10-13 (D-21), was
  <value>: <the existing text unchanged>`, then a new line giving the reason for `pending`
  (one review where three are required, MA-03; reviews commissioned, see below). A reader
  must be able to see exactly what the value was and why it stood. Delete nothing.
- The readings tables in both files stay as they are. Rule RD is not being revisited.
- **ROADMAP B7 in the same pass:** the stale "most charitable to Day" comments in C7 and
  B9 (they predate the D-15 consistency fix) are corrected to the D-15 wording. That is a
  no-decision fix and was already waiting on this decision.
- Then the integration housekeeping of lifecycle step 6 for a verdict change: `REVIEW.md`
  is untouched (no new review yet), but `QUEUE.md`, `RESULTS.md`, the argmap lineage note,
  `lint_research.py --write-hierarchy`, `argmap_check.py`, `argmap_render.py`, the counts
  in `docs/arguments/README.md`, `README.md` and `docs/HANDOFF.md`, and
  `research/tools/readme_figs.py` all need to follow, because two verdict fields change.
  `git checkout` any SVG whose only change is a random id.
- A board patch is **not** part of this task; the next `upd` patch picks the new counts up.
  Say in your report what the new tallies are so the patch can use them.

## Constraints

- Concurrency is **one agent at a time** (owner, 2026-10-13, D-22). You are that agent
  while this runs. Do not spawn a second.
- Shared files: you have `QUEUE.md`, the claim files, the ledgers and the argmap to
  yourself for the duration. Finish or stop cleanly; do not leave them half-written.
- No computation on the workstation; nothing here needs a host.
- Commit with explicit paths, `git push origin research`, and `git push origin
  research:master` only if the lifecycle step you are in calls for it (it does not here —
  push `research` only).

## Report (≤ 300 words)

Commits; the two fields before and after; the C7/B9 comment fix; the new tallies for the
board; anything in the files that contradicted the decision and what you did about it.
