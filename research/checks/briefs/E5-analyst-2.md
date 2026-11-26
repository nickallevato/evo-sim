# E5-analyst-2: write up the registered E5 external run (write-up only, no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row E5; design EVOA-58 (4cfe7e5), run EVOA-59 (0bfdfbf); D-40 (one combined review follows).

## Gap item
E5, field `verdicts.external` of `docs/research/claims/E5-ara2-ara5-counts.md` (`pending`). **It does not move in this task.** A combined review follows, then an operator integration.

## Deliverable
`research/checks/results/R4-E5-external.md`, written from `research/checks/results/raw/e5_external.{json,out,host}` and the docstring of `research/checks/e5_external.py`. It must contain:
1. The BANDS line and the verdict exactly as printed, and every cell value the bands use (F95, D_min, M_mid, E2 for Ara-2; sample time and F95 for Ara+5).
2. A score for every registered prediction (Day side, critic side, and each number in the audit's own prediction, e.g. its E2 range and Ara+5 F95 range), hit or miss, with the printed number beside it. Misses get the same prominence as hits.
3. The verdict move the docstring licenses, as a proposal only.
4. The two points the row's `next` names for the review to weigh, stated plainly: `contradicted` was unreachable on the disclosed L6 data (C2 and D5 ruled out in advance), and D_min omits M_lo and sub-detection clone-private load, which favours A2 over B2.
5. "Who this helps" with three lists (Day side, critic side, "Both / the audit's own errors"), an Open list, and a list of things that looked wrong.

Anything computed beyond the printed outputs is labelled post hoc and descriptive. No new runs.

## Allowed paths
- `research/checks/results/R4-E5-external.md` (new)

Read `R4-E5E6.md` and `REVIEW-R4-E5E6-combined.md` only by grep for context. Don't edit the script, raw outputs, claim files, ledgers, argmap, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `gap-blockers.yaml` or the board.

## Skill
`write-up-check` (`.claude/skills/write-up-check/SKILL.md`).

## Budget
At most 2 commits. No runs, no fetches, no computation beyond trivial arithmetic on printed values (label it post hoc). Fix passes left on this write-up: 2 of 2.

## Stop when
- the write-up is committed and pushed to `research`; OR
- a raw output is missing or its md5 doesn't match the `.host` record (report it; don't work around it); OR
- the work would need a path outside the list, a run or a fetch.

## Not in scope
E6; re-running L6 or E5; post hoc analyses beyond labelled arithmetic; rule changes; other nodes. Ideas go in one line in the report.

## Commit trailer
`Gap: E5`, then the attribution lines your issue gives you, in one trailer block. Explicit paths; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit(s), the predictions scorecard in short form, the proposed value, and the next step (one combined review).
