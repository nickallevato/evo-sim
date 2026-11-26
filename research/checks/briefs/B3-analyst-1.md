# B3-analyst-1: rule RD on the B3 umbrella's internal verdict (write-up only, no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row B3; rule RD (`R4-X1-verdict-rule.md` l.196-202, owner 2026-10-11); D-40 (one combined review follows).

## Gap item
B3, field `verdicts.internal` of `docs/research/claims/B3-k-neq-mu-values-umbrella.md` (`pending`: "components differ, no single value"). **It does not move in this task.** A combined review follows, then an operator integration.

## Deliverable
`research/checks/results/R4-B3-internal.md`, which proposes one internal value for B3 under rule RD, or argues that RD can't set one and says what can. It must contain:
1. **Readings table:** every plausible reading of B3's quoted statements taken together (claim file l.17-29) as one internal claim, for example "some listed value is a valid k/mu derivation", "the family is mutually consistent", or "each listed value holds". Each row gives the reading, its RH tag, the internal verdict, and the component verdicts it rests on (B3a, B3c, B3d, B3f, B3g as they stand in their claim files; cite them and don't re-score them).
2. **Field value:** the reading under which the quoted statements are *most defensible* (RD l.198: not the one best for Day), and the resulting value. Extended readings are reported but can't set the field (RD l.202).
3. **Applicability:** one paragraph on whether RD fits an umbrella of three separately quoted statements, or whether this is `SCOPED` (RD l.198). If neither rule fits, say so and propose `pending` with the reason. That outcome is acceptable; don't invent a new rule.
4. **Who this helps:** credit both sides at equal depth (hard rule 1).
5. The proposed `reading-dependent:` comment line and the Readings table for the claim file, as text in the write-up only.

## Allowed paths
- `research/checks/results/R4-B3-internal.md` (new)

Grep `quotes-*.md`, `REVIEW.md`, `R4-B3.md` and `HANDOFF.md` by id; never read them whole. Don't edit claim files, `hierarchy.yaml`, ledgers, argmap, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `gap-blockers.yaml`, `DECISIONS.md` or the board.

## Skill
`write-up-check` (`.claude/skills/write-up-check/SKILL.md`). No pre-registration script: this is a reading analysis of settled component verdicts, with no computation. There are no registered predictions to score, so use the skill's structure: "Who this helps" with three lists, an Open list, and a list of things that looked wrong.

## Budget
At most 2 commits. No runs, no fetches, no computation beyond grep. Fix passes left on this write-up: 2 of 2.

## Stop when
- the write-up is committed and pushed to `research`; OR
- a component verdict it rests on is missing or contradicts the B3 claim file (report it; don't fix it); OR
- the work would need a path outside the list, a run or a fetch.

## Not in scope
B3 fidelity and external; re-scoring any component (B3a-B3m); B3h's `pending`; rule changes to RD or C; other nodes. Ideas go in one line in the report.

## Commit trailer
`Gap: B3`, then the attribution lines your issue gives you, in one trailer block. Use explicit paths; run `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit(s), the Readings table in short form, the proposed value and its reading, and the next step (one combined review).
