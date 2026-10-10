# Overnight watcher (2026-10-09/10)

A session cron fires hourly and runs `research/tools/watch/check.sh`.
- **No run newly finished:** the main session replies in one line and does nothing else.
- **A run finished:** the main session spawns **one Sonnet subagent** (`model: "sonnet"`) with the brief below, then stops.
- **Nothing is left running** (`STILL_RUNNING: 0`) and the last collection is done: the session deletes the cron (CronDelete) and posts a short summary.

## Collection brief for the Sonnet subagent
Repo /home/na/projects/evo-sim, branch `research`. Read AGENTS.md first and obey it: the Hard rules, the Token budget, the review tiers, and the workhorse rules. Never compute on the workstation.

For each run that has finished, according to `check.sh` output and `research/checks/QUEUE.md`, but has not been collected yet:
1. **Collect.** rsync `research/checks/results/raw/<id>*` back. QUEUE.md has the exact command for each run.
2. **Write up.** Write `results/R4-<id>.md` (or complete it, for D15: `R4-D15-status.md` → `R4-D15.md`). Score every pre-registered prediction, disclose everything that was post hoc, and include a "Who this helps" section that credits both sides.
3. **Reviews, by tier:**
   - **Low-stakes (XT, G2c rerun):** write one combined review, then fix and integrate per lifecycle step 6. For G2c, restore the external verdict only if L1–L3 all pass.
   - **Load-bearing (D15, H8/H5, A2e):** write the write-up only. Mark them "awaiting three reviews (Opus)" in QUEUE.md. Do not review or integrate them.
4. **Re-review queue, once only, when the first collection happens:** write independent combined reviews of E5/E6, F1a and B2b. The original reviews were self-reviews by the agent that ran them. Use the filenames `REVIEW-R4-<id>-independent.md`.
5. **Commit and push.** Commit with explicit paths, then push with `git push origin research` and `git push origin research:master`. Leave no ssh session attached.
6. **Report** in 200 words or fewer: what was collected, the results against the predictions, and any verdict changes.

Do not start new runs. Do not do the milestone post, the board patch, or the source refresh; those are for the daytime session.
