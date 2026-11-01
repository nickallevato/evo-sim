# A2e-analyst-1: write up L3 (asymptotic MK alpha against the A2e flip)

**Role:** analyst. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e, part (2). Part (1), integrating the fix-passed external value, waits on the owner: EVO-83 MAJOR-7/8 (bare renderers and tallies) name A2e external too, and B-analyst-1 (EVOA-4) found them still open.

## Gap item
A2e. Field: `verdicts.external` of `docs/research/claims/A2e-ltee-as-ceiling.md`. **It does not move in this task.** L3 feeds it. The write-up proposes only the moves the docstring licenses. Three reviews follow as separate tasks, because A2e is load-bearing (D-23).

## Deliverable
`research/checks/results/R4-L3.md`, written from the committed outputs of the registered run:
- script `research/checks/l3_amk.py`, registered at f5b7e5e (md5 `ae4a764e…`, the same in the host record and the working tree; check this first);
- `research/checks/results/raw/l3_main.out`, `l3_result.json`, `l3_counts.json`, `l3_amk.host` (collected at a8d14b8).

Score every registered prediction and every band line exactly as printed (`l3_main.out` ends: governing band B5, licensed `contested`; the Q1-Q9 score line). Say which A2e reading the alpha speaks to (any-effect-size count vs strong-only / fitness-weighted; see `research/checks/briefs/L3-analyst.md`, "What the lead has already seen"). A2e external is now `pending` (D-21), not `contested`, so state what the licensed move would be against `pending`.

**Input provenance:** `l3_amk.host` records that the registered `sites.vcf.gz` was hand-patched (a 500-byte window copied between two corrupt downloads; the result passes `gzip -t`, sha256 `381d2ece…`). Report it verbatim under "Things that looked wrong" for the reviews to rule on. Do not judge whether it invalidates the run.

## Allowed paths
- `research/checks/results/R4-L3.md`

Read anything you need. Grep by id or heading; never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Do not write `R4-A2e-alpha.md`, claim files, `parameters.yaml`, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers, argmap data, `gap-blockers.yaml` or `DECISIONS.md`.

## Skill
`write-up-check` (`.claude/skills/write-up-check/SKILL.md`). No computation beyond reading the printed outputs. Anything you derive by hand is labelled post hoc and descriptive. If a new run seems needed, stop and report it. Do not run one.

## Budget
At most 2 commits. Fix passes left on L3: 2 (none done).

## Stop when
- the deliverable is committed and pushed to `research`; OR
- an input is missing or does not match (script md5, a raw file absent, an output that does not parse): report it and do not work around it; OR
- the work would touch a path outside the list above.

## Not in scope
Reviews, integration, A2e part (1), the B-R20/B-R21 publication hold, RG-03, the board, tooling, refreshes, other nodes. Ideas go in one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Use explicit paths only. Run `git pull --rebase origin research` before `git push origin research`. Do not push to `master`.

## Report (at most 300 words, as the issue comment)
Commits; a table of the registered predictions (each side's) with hit/miss and the printed number; the governing band and the licensed move against `pending`; the reading it speaks to; things that looked wrong; anything for the owner.
