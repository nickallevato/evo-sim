# E5-reviewer-1: one combined review of R4-E5-external (no field move)

**Role:** reviewer (a fresh instance; you did not design, run or write up E5 external). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row E5; design EVOA-58 (4cfe7e5), run EVOA-59 (0bfdfbf), write-up EVOA-60 (cbf1e5f); D-40 (one combined review: correctness plus a Day-side and a critic-side section of equal depth).

## Gap item
E5, field `verdicts.external` of `docs/research/claims/E5-ara2-ara5-counts.md` (now `pending`; proposed `supported`). **It does not move in this task.** The move is a later operator integration.

## Deliverable
`research/checks/results/REVIEW-R4-E5-external-combined.md`, one file. Target: `research/checks/results/R4-E5-external.md` (cbf1e5f; brief `E5-analyst-2.md`). Three sections, same severity labels (BLOCKER / MAJOR / MINOR / NOTE), numbered findings with evidence and an exact fix:
1. **Correctness.** Every printed value and the BANDS line in the write-up against `raw/e5_external.{out,json}`; the md5s against `raw/e5_external.host`; the band logic and the verdict mapping against the docstring of `research/checks/e5_external.py` (registered at 4cfe7e5; any change since is post hoc); the scorecard (each registered prediction present, scored right); the post hoc arithmetic (23.0; 3,228; -239.5 / -285.1; S 41.5-87.1; the clone-pair / E2 ratios); the RE-03, RE-04, RE-10 quotes against `quotes-*.md` by grep.
2. **Day-side steelman.** Strongest case for `contested` (or a value more favourable to Day): D_min is not a floor; Day's rebuilt S (41-87) against 708 near-fixed fits a minority-lineage clone (B2 in substance); `contradicted` was unreachable on the disclosed L6 data, so the test was severe for one side only.
3. **Critic-side steelman**, same depth. Strongest case for `supported` as registered: both cells meet the registered bands; the population count by Day's own s3.2 rule is 708 / 730; Ara+5's 0 has no sample behind it; post hoc caveats do not reopen a registered band.

Starting list (not the scope): whether D_min's omission of M_lo and sub-detection private load is a design flaw that voids the A2 call or a caveat for a scope note; whether `supported` should carry a scope note (write-up, Open 2); whether the Ara+4 0/0/0 row shows a `nearest()` defect that also touches the Ara-2 or Ara+5 cells; the audit's E2 range miss.

Close with finding counts, a one-line verdict (value licensed as proposed / licensed with changes / not licensed, and if not, which value is licensed) and the list of wrong items (old -> right).

## Allowed paths
- `research/checks/results/REVIEW-R4-E5-external-combined.md` (new)

Read anything; grep by id or heading. Never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Don't edit the write-up, script, raw outputs, claim files, quotes files, ledgers, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md`, argmap or the board.

## Skill
`review-correctness` for section 1, `review-steelman` (both sides) for sections 2 and 3, in one file (D-40).

## Budget
At most 2 commits. No runs, no fetches, no computation beyond trivial arithmetic on printed values. Fix passes left on the write-up: 2.

## Stop when
- the review is committed and pushed to `research`; OR
- an input is missing or does not match (a raw md5 differs from `.host`, a printed value is absent): report it, don't work around it; OR
- the work would touch a path outside the list, or would need a run or a fetch.

## Not in scope
The fix pass, integration, E6, re-running L6 or E5, fetching the Tenaillon `.gd` files, rule changes (a proposed change is one line in the report, for the owner card). Ideas: one line in the report.

## Commit trailer
`Gap: E5`, then the attribution lines your issue gives you, in one trailer block. Explicit paths only; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (at most 300 words, as the issue comment)
Commits; finding counts by section and severity; each BLOCKER and MAJOR in one line; the verdict on the proposed value; where the two steelman sections conflict (the lead rules once in the fix-pass brief); next step.
