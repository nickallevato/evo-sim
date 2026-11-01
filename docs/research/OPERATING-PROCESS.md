# Operating process for the autonomous team

Written 2026-10-31 for the owner to hand to the Paperclip team (lead plus `analyst`, `reviewer`, `operator`). The evidence for each rule is in [`PROCESS-REVIEW-2026-10-31.md`](PROCESS-REVIEW-2026-10-31.md). Where this file and `TEAM-BRIEF.md` disagree, this file wins.

## The one goal

Close the exit gap in `PLAN.md`. The gap is computed, not judged:

```sh
research/.venv/bin/python -I research/tools/exit_gap.py            # all open items
research/.venv/bin/python -I research/tools/exit_gap.py --workable # what may start now
```

**If work does not close an item on that list, do not do it.** That covers interesting follow-ups, nicer tooling, extra frameworks and checks on nodes that aren't load-bearing. Put the idea in one line under "Ideas (not queued)" in `QUEUE.md` and move on.

## The loop (lead)

1. Run `exit_gap.py --workable`. If it prints nothing workable (exit code 3): post **one** owner card that lists the blockers, then **stop**. Do not invent work while waiting.
2. Pick the first workable item. Turn its `next` into **one** task with the `scope-task` skill: a deliverable, allowed paths, a budget and a stop condition. Commit the brief and set the row's blocker to `in-flight`.
3. Run the task. When the report comes back, run `git show --stat` on each commit. If a commit touched paths outside the brief, revert that commit and say so in the next owner report.
4. When the item's field moves, or the task ends, rewrite the row's `next` in `gap-blockers.yaml` (or delete the row if `--lint` says the node is closed). Go to 1.

Every commit carries a `Gap: <ID>` trailer (the hook `.githooks/commit-msg` enforces it). ID is an open item, `upkeep` (a failing gate forced it) or `owner` (the owner asked; the body cites the D- id). Never `--no-verify`.

## Limits

| Limit | Value |
|---|---|
| Items in flight (any step from pre-register to integrate) | **2**. Finish and integrate one before designing a third. |
| Agents running at once | 1 (D-22) |
| Rulings per conflict | **1 ruling**, in the fix-pass brief. No fresh check of it (D-38). If the worker disagrees after one round, the owner decides (`maxReviewRounds: 1`). |
| Fix passes per check | **2.** A third means the design was wrong; tell the owner. |
| Brief length | 60 lines. Point at files; don't paste them. |
| Report length | 300 words (unchanged) |
| Source refresh | **Weekly**, as the owner ticked (D-20), plus one before a milestone post. The corpus is frozen (O-7), so a refresh only logs; it never starts a task by itself. |
| Criticality pass | **One, on the R5 draft only** (D-38). Not per milestone. |
| Reviews | One combined review by default; three separate only when a load-bearing verdict field would change; spot check only for math-map work, lookups and arithmetic (D-38). |
| Milestone post | When a gap item closes or two weeks have passed, whichever comes first. |
| Tool fixes | Only when a gate (`lint_research.py`, `argmap_check.py`, `exit_gap.py --lint`) fails, as one `upkeep` task. Matching a figure to the files of record is not a gate failure. |

## Do not

- **Don't start a check on a node that isn't load-bearing** or on a field that is already set. Examples from October: L2 and FMnull-S4 tested external fields that were already `contested`; B1e-Q2, VID-01-score, L5-C1a, C1d-fu and D-fu tested nodes that aren't load-bearing.
- **Don't debug the orchestrator inside the audit.** Paperclip mechanics (lanes, tokens, monitors, routines, `skip_if_active`) go in `docs/research/ops-notes.md`, at most five lines per incident, and never in `DECISIONS.md`. If the orchestrator blocks work, stop and tell the owner. D-29 to D-37 must not happen again.
- **Don't write a decision the owner didn't make.** `DECISIONS.md` gets owner decisions verbatim. A lead ruling goes in the fix-pass brief of the check it rules on.
- **Don't open new process machinery** (new fields, guards, ledgers, scoring frameworks, review tiers) without an owner decision. Propose it in one line on the owner card.
- **Don't re-litigate.** When the owner has decided, apply the decision and move on.
- **Don't refresh sources, re-render figures or patch the board on spec.** Each has its trigger in the limits table.
- **Don't run a review of a review**, or a check of a ruling (D-38).
- **Don't recompute settled maths.** Cite the object's record (`docs/research/math/README.md`, "Records").
- **Never commit or push from a compute host; never `git add -A`.** These already apply and still stand.

## Delegation

| Work | Who | Skill | Gap tag |
|---|---|---|---|
| Choose the next task, write its brief, check its result | lead | `scope-task` | the item |
| Design and pre-register a check | analyst | `design-check` | the item |
| Launch or collect a run | operator | `run-on-host` | the item |
| Write up, fix pass | analyst | `write-up-check`, `fix-pass` | the item |
| Reviews (tier from AGENTS.md) | reviewer, a fresh one each time | `review-correctness`, `review-steelman` | the item |
| Integrate into shared files | operator | `integrate-check` | the item |
| Fix status fields or `gap-blockers.yaml` rows marked `verify:` | operator | `scope-task` brief | the item |
| Refresh, criticality pass, post, board | per `close-batch` | `close-batch` | `upkeep` |

The lead writes briefs, rulings and owner cards. It doesn't author write-ups or edit shared files.

## Talking to the owner

Send one card per stop, and put every question on it. Ask only for what a row marked `owner` needs: text he must supply, a decision only he can make, or approval to publish. A weekly report gives the `exit_gap.py` table, then `exit_gap.py --audit <last report commit>` (the share of commits on-gap), then what changed. If the on-gap share drops below 70%, say why.

## First tasks under this process (2026-10-31)

1. **operator, one task:** resolve every `verify:` row in `gap-blockers.yaml` (A3, B2b, E5, E6, F1a, H5, H8, X-ARGMAP) from the claim files and REVIEW.md. Move status fields only where an existing review covers the node, rewrite each `next`, and leave verdict values alone. `Gap:` the item ids.
2. **B:** answer EVO-83's MAJOR in one fix pass, then integrate. If that fails, send it to the owner; there is no fourth ruling.
3. **A2e:** integrate the fix-passed external value. The publication hold stays with the owner.
4. Then the loop.
