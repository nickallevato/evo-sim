# A2e-reviewer-3: steelman-critic review of R4-L3 (asymptotic MK alpha against the A2e flip)

**Role:** reviewer (a fresh instance; you did not write R4-L3, its correctness review or its Day-side steelman). **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e. L3 feeds A2e external, a field on the exit gap, so it keeps three separate reviews under D-38. This is review 3 of 3, **critic side only**.

## Gap item
A2e. Field: `verdicts.external` of `docs/research/claims/A2e-ltee-as-ceiling.md` (now `pending`, D-21). **It does not move in this task.**

## Deliverable
`research/checks/results/REVIEW-R4-L3-steelman-critic.md`, one file, written per the skill (critic side). Target: `research/checks/results/R4-L3.md` (commit 78d9d11).

Inputs:
- registration: `research/checks/l3_amk.py` at f5b7e5e (docstring = predictions, bands, move rows, combination rule);
- outputs: `research/checks/results/raw/l3_main.out`, `l3_result.json`, `l3_counts.json`, `l3_amk.host`;
- briefs `research/checks/briefs/L3-analyst.md`, `A2e-analyst-1.md`;
- correctness review `research/checks/results/REVIEW-R4-L3-correctness.md` at 8432a1c (read it; agree or disagree by id where it bears on the critics' side);
- claim `docs/research/claims/A2e-ltee-as-ceiling.md`; rule file `research/checks/results/R4-X1-verdict-rule.md` (S, C, RD, N, R1). Critic and Day quotes by Q/RF id: grep the quotes files, never read them whole.

Starting list (not the scope):
1. Does R4-L3 give the critics' strongest case its due: the published asymptotic-MK and DFE-based alpha estimates for humans, and the reading that Day's ceiling is about strong-effect fixations rather than all of them?
2. Audit choices scored against the critics: thresholds h and l, the GOV basis (human-specific by parsimony) against S6, bins, the cut-off x, the exponential fit, the MC envelope that lifts U above 1, and the S1-S5 rows.
3. Could the test have produced an outcome on the critics' side at all (B1/B2)? Name the band and what it would have taken.
4. Section 8 "Who this helps": is credit to the critics as prominent as credit to Day? Is anything given to Day that the numbers don't carry (e.g. the negative point, the counts at P)?
5. Any unlabelled post hoc number that cuts against the critics.
6. What the evidence costs the critics: state it plainly.

Computation: reading and arithmetic on the committed json only (one local process, <500 MB, <1 min, `research/.venv/bin/python -I`). No runs, no fetches. Label any number of your own "post hoc (reviewer)".

## Allowed paths
- `research/checks/results/REVIEW-R4-L3-steelman-critic.md`

Read anything you need; grep by id or heading. Never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. **Do not read `REVIEW-R4-L3-steelman-day.md`** (fb8b66d); the lead reconciles the two in the fix-pass brief. Do not edit `R4-L3.md`, the script, raw outputs, the other reviews, claim files, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md` or `DECISIONS.md`.

## Skill
`review-steelman` (`.claude/skills/review-steelman/SKILL.md`), critic side.

## Budget
At most 2 commits. Fix passes left on L3: 2 (none done; the fix pass is a later task).

## Stop when
- the review is committed and pushed to `research`; OR
- an input is missing or does not match (script md5 `ae4a764eec0ff8100c05d120fb41ecb4`, a raw file absent or unparsable): report it and do not work around it; OR
- the work would touch a path outside the list above, or would need a run or a fetch.

## Not in scope
The Day-side steelman, the fix pass, integration, the hand-patch provenance task, A2e part (1), the publication hold, tooling, other nodes. Ideas go in one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths only; `git pull --rebase origin research` before `git push origin research`. Do not push to `master`.

## Report (at most 300 words, as the issue comment)
Commits; finding counts by severity; each BLOCKER and MAJOR in one line; any finding that would change the band, the move row or the licensed value; disagreements with the correctness review by id; next step.
