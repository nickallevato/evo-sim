# A2e-reviewer-1: correctness review of R4-L3 (asymptotic MK alpha against the A2e flip)

**Role:** reviewer (a fresh instance; you did not write R4-L3). **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e. L3 feeds A2e external, which is load-bearing, so it gets three reviews (D-23). This is review 1 of 3. Steelman-day and steelman-critic follow as separate tasks, one at a time.

## Gap item
A2e. Field: `verdicts.external` of `docs/research/claims/A2e-ltee-as-ceiling.md` (now `pending`, D-21). **It does not move in this task.**

## Deliverable
`research/checks/results/REVIEW-R4-L3-correctness.md`, one file, written per the skill. Target: `research/checks/results/R4-L3.md` (commit 78d9d11).

Inputs:
- registration: `research/checks/l3_amk.py` at f5b7e5e (docstring = predictions, bands, move rows, combination rule). Check the md5 is `ae4a764eec0ff8100c05d120fb41ecb4`;
- outputs: `research/checks/results/raw/l3_main.out`, `l3_result.json`, `l3_counts.json`, `l3_amk.host` (collected at a8d14b8);
- design brief: `research/checks/briefs/L3-analyst.md`; write-up brief: `research/checks/briefs/A2e-analyst-1.md`.

Recompute from the raw json, do not trust the write-up. Starting list (not the scope):
1. Every number in R4-L3 sections 1-5 against the raw files; every hit/miss against the exact docstring wording (13 predictions, DS..Q9).
2. Band B5 and move row B5 against the docstring's band and robustness lines (h, l, S1-S5 points).
3. Section 6: is the stated move against `pending` exactly what the docstring licenses? Its two "not covered" combination-rule cases (section 10, item 4): real gaps, or does the docstring cover them?
4. Section 9, item 1, the hand-patched `sites.vcf.gz`: **rule on it** as a finding with a severity. Does the host record give enough to accept the run, or is a re-fetch / re-run needed? Do not fetch or run anything; say what would be needed.
5. Section 9, items 2 and 4 (MC upper bounds above alpha 1; negative or impossible counts): are they registered behaviour, or a code-path bug? Read the code path before accepting the write-up's explanation.
6. Every post hoc label (section 7).

Computation: reading and arithmetic on the committed json only (one local process, <500 MB, <1 min, `research/.venv/bin/python -I`). No runs, no fetches.

## Allowed paths
- `research/checks/results/REVIEW-R4-L3-correctness.md`

Read anything you need; grep by id or heading. Never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Do not edit `R4-L3.md`, the script, raw outputs, claim files, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md` or `DECISIONS.md`.

## Skill
`review-correctness` (`.claude/skills/review-correctness/SKILL.md`).

## Budget
At most 2 commits. Fix passes left on L3: 2 (none done; the fix pass is a later task).

## Stop when
- the review is committed and pushed to `research`; OR
- an input is missing or does not match (script md5, a raw file absent or unparsable): report it and do not work around it; OR
- the work would touch a path outside the list above, or would need a run or a fetch.

## Not in scope
The two steelman reviews, the fix pass, integration, A2e part (1), the publication hold, tooling, other nodes. Ideas go in one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths only; `git pull --rebase origin research` before `git push origin research`. Do not push to `master`.

## Report (at most 300 words, as the issue comment)
Commits; finding counts by severity; each BLOCKER and MAJOR in one line; your ruling on the hand-patched input; wrong numbers (old -> right); next step.
