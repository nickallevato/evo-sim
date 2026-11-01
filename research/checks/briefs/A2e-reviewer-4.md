# A2e-reviewer-4: one combined review of R4-A2e-fidelity (no field move)

**Role:** reviewer (a fresh instance; you did not write R4-A2e-fidelity). **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e; D-40 (always one combined review: correctness plus a Day-side and a critic-side section of equal depth).

## Gap item
A2e, field `verdicts.fidelity` of `docs/research/claims/A2e-ltee-as-ceiling.md` (now `pending`). **It does not move in this task.** The move is a later operator integration with the owner approval stage.

## Deliverable
`research/checks/results/REVIEW-R4-A2e-fidelity-combined.md`, one file. Target: `research/checks/results/R4-A2e-fidelity.md` (criterion 0fd4581, write-up 0f8f64a; brief `A2e-analyst-3.md`). Three sections, same severity labels (BLOCKER / MAJOR / MINOR / NOTE), numbered findings with evidence and an exact fix:
1. **Correctness.** Every Day quote and line number against the held `sources/raw/vid01-score-2026-10-13/main.txt` (check its sha256 against section "Held material"); every literature quote against `docs/research/sources/quotes-literature.md`; every status against rule F as written in `research/checks/results/R4-X1-verdict-rule.md`; K3's node rule against the record's practice (A2, A5f); whether the scoring follows the criterion commit 0fd4581 unchanged.
2. **Day-side steelman.** Strongest case for `n/a` or `accurate`; whether rule F's closed exempt list should cover LTEE Ne; whether U6 belongs inside scope K1(c).
3. **Critic-side steelman**, same depth. Strongest case for `partial` or `misread`; whether R-attributed is the more defensible reading; whether the uncited "documented" mechanisms (U2) or the advantage list should score higher than `n/a`.

Starting list (not the scope): K1(c) scope, since the value turns on U6 alone; the K2 "uncited qualitative = n/a" step; the conditionality on the three unheld works (U3-U5); the "audit's own errors" in section 5.

Close with finding counts, a one-line verdict (value licensed as proposed / licensed with changes / not licensed) and the list of wrong items (old -> right).

## Allowed paths
- `research/checks/results/REVIEW-R4-A2e-fidelity-combined.md` (new)

Read anything; grep by id or heading. Never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Do not edit the write-up, claim files, quotes files, ledgers, `parameters.yaml`, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md`, argmap or the board.

## Skill
`review-correctness` for section 1, `review-steelman` (both sides) for sections 2 and 3, in one file (D-40).

## Budget
At most 2 commits. No computation beyond one trivial local process (sha256, grep). No runs, no fetches. Fix passes left on this write-up: 2.

## Stop when
- the review is committed and pushed to `research`; OR
- an input is missing or does not match (held text absent, sha256 differs): report it, do not work around it; OR
- the work would touch a path outside the list, or would need a fetch.

## Not in scope
The fix pass, integration, A2e external and internal, other A-branch nodes, fetching U3-U5 or an Ne source, rule changes (a proposed rule F change is one line in the report, for the owner card). Ideas: one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths only; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (at most 300 words, as the issue comment)
Commits; finding counts by section and severity; each BLOCKER and MAJOR in one line; the verdict on the proposed value; where the two steelman sections conflict (the lead rules once in the fix-pass brief); next step.
