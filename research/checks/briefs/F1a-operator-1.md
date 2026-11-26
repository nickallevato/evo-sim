# F1a-operator-1: integrate the R4-F1a fix pass; F1a status `extracted` -> `reviewed` (no verdict move)

**Role:** operator. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row F1a; write-up `research/checks/results/R4-F1a.md` (fix pass 4971d70, lead-approved EVOA-65); reviews `REVIEW-R4-F1a-combined.md` (#20) and `REVIEW-R4-F1a-independent.md` (#24).

## Gap item
F1a (`docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md`), field `status`: `extracted` -> `reviewed`, with comment `# reviews #20, #24; fix pass 4971d70 (F1a-operator-1, 2026-11-26)` (form of 5d9f302). **No verdict value moves** (internal `non-sequitur`, fidelity `n/a`, external `pending` stay; comments unchanged).

## Deliverable
One integration per the `integrate-check` skill, applying R4-F1a.md's "Review resolution (fix pass, 2026-11-26)" and nothing more:
1. No new quotes.
2. `research/checks/REVIEW.md`: one entry for the fix pass (4971d70) answering #20 and #24 by id (I-MAJOR-1 accepted: engine-vs-Kimura check at 4Ns = 40, counts fixed by U_b; dispersion withdrawn, unexplained, not shown). Do not edit the #20 or #23-#25 entries.
3. `RESULTS.md` §F1a (l.581-582): keep the text; append a dated post hoc sentence that the count predictions were fixed by construction (engine check, not independent evidence) and the k = 100 dispersion 1.53 is unexplained. Do not reword "All predictions met" (that is ROADMAP B36, awaiting owner).
4. `QUEUE.md`: F1a fix pass DONE 2026-11-26, status `reviewed`; open: F1a external (one check).
5. Claim file: the `status` line as above. In the "R4 F1a" paragraph (l.73), mark (don't delete) "Supports the first half" with a dated note: fix pass 4971d70, "is consistent with"; the run is an engine consistency check, not independent evidence.
6. Argmap: `rev:R4-F1a-independent` row in `NOTES.md` if absent, and the fix pass on the `chk:F1a` row; no new defeaters; lineage node only if the B3 integration's form (89b484e) calls for one.
7. Gates and counts as in the skill (lint `--write-hierarchy`, `argmap_check.py` 0/0, `argmap_render.py`, counts in `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`, `readme_figs.py`, revert SVGs whose only diff is random ids). Only the `reviewed` status count should change, by one.

## Allowed paths
- `research/checks/REVIEW.md`, `RESULTS.md`, `QUEUE.md`
- `docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md`, `docs/research/hierarchy.yaml`, `docs/research/hierarchy/*.md` (as regenerated)
- `docs/research/argmap/NOTES.md`, `lineage.yaml`
- `docs/arguments/`, `README.md`, `docs/HANDOFF.md`, `docs/img/` figures that `readme_figs.py` / `argmap_render.py` write

Read anything (grep big files by id). Do not edit `R4-F1a.md`, any review file, other claim files, `defeaters.yaml`, `ROADMAP.md`, `gap-blockers.yaml`, `DECISIONS.md`, ledgers, `criticality/` or the board.

## Skill
`integrate-check`. Local lint/render tools only; no host work, no fetch.

## Budget
At most 3 commits. No fix passes apply.

## Stop when
- the integration is committed and pushed to `research`, lint and argmap_check at 0/0; OR
- a step needs a verdict move, a fetch, a new quote, or a path outside the list (report; don't work around it); OR
- a gate fails for a reason outside F1a (report as a possible `upkeep` item).

## Not in scope
Any verdict value or verdict comment; F1a external (next task); F1/F1b; ROADMAP B36/B41/B44 rewording; the board, a milestone post, `git push origin research:master`. Ideas: one line in the report.

## Commit trailer
`Gap: F1a`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`.

## Report (≤ 300 words, as the issue comment)
Commits; shared files changed; counts before and after (expected: `reviewed` +1); every field whose value or governing reading changed (expected: status only); new REVIEW and lineage ids; anything you stopped on; next step (F1a external check).
