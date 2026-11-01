---
name: scope-task
description: Lead only. Turn one workable exit-gap item into one bounded task (deliverable, allowed paths, budget, stop condition) and a committed brief, or stop and post an owner card when nothing is workable. Use before creating ANY task.
---
# Scope one task from the exit gap

1. `research/.venv/bin/python -I research/tools/exit_gap.py --workable`. Exit 3: nothing workable. Write ONE owner card listing every `owner`/`outside` row and what it needs, then stop. Do not create tasks.
2. Take the first workable row. Its `next` is the task. If `next` is bigger than one deliverable, split it in `gap-blockers.yaml` and take the first part only.
3. Write the brief at `research/checks/briefs/<ITEM>-<role>-<n>.md`, **at most 60 lines**, with exactly these headings:
   - **Gap item:** the id and the field(s) it should move.
   - **Deliverable:** one file (or one integration), named.
   - **Allowed paths:** an explicit list. Anything else is out of scope.
   - **Skill:** one of the skills in `.claude/skills/`.
   - **Budget:** max commits (default 3), and max fix passes left (2 minus those done).
   - **Stop when:** the deliverable is committed, OR an input is missing (report it, don't work around it), OR the work would touch a path outside the list.
   - **Not in scope:** follow-ups, tooling, refreshes, new rules, other nodes. Ideas go in one line in the report.
   - **Commit trailer:** `Gap: <ITEM>` plus the attribution lines.
4. Commit the brief (`Gap: <ITEM>`), set the row's blocker to `in-flight`, then create the task.
5. On the report: `git show --stat` on each commit. If a commit touched paths outside the allowed list, revert it. If the field moved, update the row (or delete it if `exit_gap.py --lint` says the node is closed). If the task stopped on a missing input, set the row to `owner` or `outside`.

Rulings: at most one per conflict, written in the fix-pass brief, checked once by a fresh reviewer. If that check returns a BLOCKER or MAJOR, the row goes to `owner`. Don't re-rule.
