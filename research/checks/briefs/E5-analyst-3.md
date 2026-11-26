# E5-analyst-3: fix pass 1 of 2 on R4-E5-external (no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row E5; review `research/checks/results/REVIEW-R4-E5-external-combined.md` (cf1fbf1, approved as EVOA-61); registration `research/checks/e5_external.py` docstring (4cfe7e5); hard rule 5; D-40; OPERATING-PROCESS (one ruling per conflict, no fresh check of it, D-38).

## Gap item
E5, field `verdicts.external` of `docs/research/claims/E5-ara2-ara5-counts.md` (`pending`; proposed `supported`). **It does not move in this task.**

## Lead ruling (the one ruling on the steelman conflict D-1 vs K-1)
**For K-1. The proposal stays `supported` (A2 | G5, as registered), and it carries a scope note.** Reasons:
1. Hard rule 5: the docstring fixed A2 with G5 -> `supported` before the run. Post hoc analysis can add a scope note; it cannot move a band.
2. D-1's point is not new information. The docstring stated D_min's limits before the run (l.45-46), and B2's registered threshold (M_mid >= 3,228) was missed by 7.1x on the band's own terms.
3. K-2: mechanism (i), a cross-clade pair from a structured population, is the critics' registered model (claim l.60: "the correction formula applied to an unstructured-sample assumption violated by lineage coexistence"). So on the record D-1 cites, the critics' prediction still holds. (i) does not turn the node toward Day.
4. D-1 is recorded, not dropped. Its evidence (Ara-2 94 whole-population / 1,816 within-lineage, E5 l.42; rebuilt S 41.5-87.1 = 0.44-0.93 of 94) goes into the post hoc section, labelled post hoc, and into the scope note: `supported` is not a finding that Ara-2's sub-population structure is an artefact. Open 2 closes on this ruling.

## Deliverable
`research/checks/results/R4-E5-external.md`, edited in place, plus a new section "Review resolution (fix pass 1, 2026-11-26)". Answer every MAJOR and MINOR by id (C-1, C-2, C-3, D-1, D-2, D-3, D-4, K-1, K-2, K-3): accepted, in part, or not accepted, with the reason and what changed. Per the ruling:
- Apply the review's wrong items 1-7. Item 6 is the scope note on the proposed move (l.76). Keep its content: the -906 is the n = 2 clone-pair correction, not a fixation count; Ara-2 is positive under every rule on record; likely a cross-clade pair, so not a finding that the structure is an artefact; Ara+5's 0 at 60K is beyond the last sample, and that diagnosis is the audit's, not RE-04's.
- Add D-1's two post hoc bullets, D-3's Day bullet and K-3's critic bullet in "Who this helps", at equal depth for both sides. NOTEs (C-4, C-5, K-4) are optional, one clause each.
- Registered wording stays registered; new findings go in separate sentences labelled post hoc.
- End with the proposed claim-file comment line for integration (value and scope together, so `scope_guard.py` passes later).

## Allowed paths
- `research/checks/results/R4-E5-external.md`

Grep other files by id; never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Don't edit the script, raw outputs, the review, claim files, ledgers, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md`, argmap or the board.

## Skill
`fix-pass` (`.claude/skills/fix-pass/SKILL.md`).

## Budget
At most 2 commits. No runs, no fetches, no computation beyond trivial arithmetic on printed values. Fix passes left after this one: 1.

## Stop when
- the fix pass is committed and pushed to `research`; OR
- a cited line or value is missing or differs from its file (report it; don't fix it); OR
- the work would need a path outside the list, a run or a fetch. If you disagree with the ruling, record your position in the resolution, apply the ruling, and say so in the report. The owner decides after one round.

## Not in scope
Integration; E6; re-running L6 or E5; fetching the Tenaillon `.gd` files; the recount's Ara+4 coverage gap beyond the C-1 wording; rule changes. Ideas: one line in the report.

## Commit trailer
`Gap: E5`, then the attribution lines your issue gives you, in one trailer block. Explicit paths; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; each finding id with its resolution in one line; the final proposed value and comment line; next step (operator integration: field `pending` -> `supported` with the scope note).
