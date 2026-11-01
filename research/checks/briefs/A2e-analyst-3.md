# A2e-analyst-3: A2e fidelity from held material (one write-up, no field move)

**Role:** analyst. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e (645b21d): external waits on the owner (B, EVO-83 MAJOR-7/8; O-17), so the workable field is fidelity.

## Gap item
A2e, field `fidelity` (now `pending`). This task **proposes** a value; it moves no field. The move happens later, in an operator integration with the owner approval stage, after one combined review (D-40).

## Deliverable
One file: `research/checks/results/R4-A2e-fidelity.md`, containing:
1. **Criterion first.** Before any scoring, state which cited uses are scored and the rule that decides each (verdict rule S, F, U, C, RD; `R4-X1-verdict-rule.md`), and commit that section alone first (the pre-registration equivalent for a non-computational check; one commit).
2. **The cited uses.** From the two A2e Statement quotes (MITTENS 3.0, Z23003785, p.2 and p.4) and their paragraph, every cited or implied source use: what Day relies on the LTEE literature for (ceiling, "effectively unlimited mutation supply", "no recombination overhead", Ne, selection strength). Grep `docs/research/sources/quotes-*.md`, `ledgers/fidelity.md` (Tenaillon 2016, Good 2017 rows), A2/A2a-A2d claim files. Uses with no citation: say so and apply rule F.
3. **Scoring table:** use, source, verbatim quote with locator (only quotes already in the quotes files; do not fetch), status (accurate / partial / misread / unverifiable), rule applied. Under RD: every plausible reading and its value; the field value is the reading under which the statement is most defensible.
4. **Proposed field value** with a one-line basis, and the comment text an operator would paste.
5. **Who this helps:** Day side, critic side, "Both / the audit's own errors" (e.g., the claim table marks both works "verified" while the field is `pending`; say why if you can tell).
6. Open list (anything that needs a fetch or an owner text goes here, not worked around) and things that looked wrong.

## Allowed paths
- `research/checks/results/R4-A2e-fidelity.md` (new). Nothing else.

Read anything. Do not edit the claim file, quotes files, ledgers, `fidelity.md`, REVIEW/RESULTS/QUEUE, `gap-blockers.yaml`, `DECISIONS.md`, argmap or the board.

## Skill
`write-up-check`, adapted: there are no raw outputs; the "registered predictions" are the criterion section of step 1. No computation, no host, no fetch.

## Budget
At most 3 commits (criterion; write-up; one tidy-up). Fix passes left for this write-up: 2.

## Stop when
- the write-up is committed and pushed to `research`; OR
- the value turns on a source text not held under `sources/raw/` or not quoted in the quotes files (record it in Open; if no value is possible without it, propose `unverifiable` only if rule F licenses it, else stop and report what is missing); OR
- the work would touch a path outside the list.

## Not in scope
A2e external, internal, the D-21 value, the AA README quote, other A-branch nodes (A2i, A2j fidelity), the review, the integration, any fetch. Ideas: one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; the criterion commit hash; the scoring table in short; proposed fidelity value and basis; anything missing or stopped on; next step (expected: one combined review).
