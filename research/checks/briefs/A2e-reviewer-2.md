# A2e-reviewer-2: steelman-day review of R4-L3 (asymptotic MK alpha against the A2e flip)

**Role:** reviewer (a fresh instance; you did not write R4-L3 or its correctness review). **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e. L3 feeds A2e external, which is load-bearing, so it gets three reviews (D-23). This is review 2 of 3, **Day side only**. Steelman-critic follows as a separate task.

## Gap item
A2e. Field: `verdicts.external` of `docs/research/claims/A2e-ltee-as-ceiling.md` (now `pending`, D-21). **It does not move in this task.**

## Deliverable
`research/checks/results/REVIEW-R4-L3-steelman-day.md`, one file, written per the skill (Day side). Target: `research/checks/results/R4-L3.md` (commit 78d9d11).

Inputs:
- registration: `research/checks/l3_amk.py` at f5b7e5e (docstring = predictions, bands, move rows, combination rule);
- outputs: `research/checks/results/raw/l3_main.out`, `l3_result.json`, `l3_counts.json`, `l3_amk.host`;
- briefs `research/checks/briefs/L3-analyst.md`, `A2e-analyst-1.md`;
- correctness review `research/checks/results/REVIEW-R4-L3-correctness.md` at 8432a1c (read it; agree or disagree by id where it bears on Day's side, especially MINOR-2 and NOTE-10);
- claim `docs/research/claims/A2e-ltee-as-ceiling.md`; rule file `research/checks/results/R4-X1-verdict-rule.md` (S, C, RD, N, R1). Day quotes by Q id: grep the quotes files, never read them whole.

Starting list (not the scope):
1. Does R4-L3 test what Day actually claimed in A2e, or a broader or narrower claim? Readings of his verbatim words under which he is right (rule RD), and whether they get their due weight.
2. Audit choices scored against him: model choice (exponential vs linear fallback, NOTE-10), the upper-case-AA reading (MINOR-2), bins, thresholds h and l, and the S1-S5 rows.
3. Could the test have produced an outcome on Day's side at all? Name the band and what it would have taken.
4. Section 8 "Who this helps": credit to Day as prominent as the errors? Conclusions worded more broadly than tested?
5. Any unlabelled post hoc number that cuts against him.
6. What the evidence costs Day: state it plainly.

Computation: reading and arithmetic on the committed json only (one local process, <500 MB, <1 min, `research/.venv/bin/python -I`). No runs, no fetches. Label any number of your own "post hoc (reviewer)".

## Allowed paths
- `research/checks/results/REVIEW-R4-L3-steelman-day.md`

Read anything you need; grep by id or heading. Never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. **Do not read `REVIEW-R4-L3-steelman-critic.md`** if it exists. Do not edit `R4-L3.md`, the script, raw outputs, the correctness review, claim files, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md` or `DECISIONS.md`.

## Skill
`review-steelman` (`.claude/skills/review-steelman/SKILL.md`), Day side.

## Budget
At most 2 commits. Fix passes left on L3: 2 (none done; the fix pass is a later task).

## Stop when
- the review is committed and pushed to `research`; OR
- an input is missing or does not match (script md5 `ae4a764eec0ff8100c05d120fb41ecb4`, a raw file absent or unparsable): report it and do not work around it; OR
- the work would touch a path outside the list above, or would need a run or a fetch.

## Not in scope
The critic-side steelman, the fix pass, integration, the hand-patch provenance task, A2e part (1), the publication hold, tooling, other nodes. Ideas go in one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths only; `git pull --rebase origin research` before `git push origin research`. Do not push to `master`.

## Report (at most 300 words, as the issue comment)
Commits; finding counts by severity; each BLOCKER and MAJOR in one line; any finding that would change the band, the move row or the licensed value; disagreements with the correctness review by id; next step.
