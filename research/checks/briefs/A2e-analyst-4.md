# A2e-analyst-4: fix pass 1 on R4-A2e-fidelity, with the lead's ruling (no field move)

**Role:** analyst. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e; D-40 (one combined review); D-38 (one ruling per conflict, no check of it).

## Gap item
A2e, field `verdicts.fidelity` of `docs/research/claims/A2e-ltee-as-ceiling.md` (`pending`). **It does not move in this task.** The move is a later operator integration with the owner approval stage.

## Deliverable
`research/checks/results/R4-A2e-fidelity.md` with a new section "Review resolution (fix pass 1, 2026-11-01)" that answers every MAJOR and MINOR of `REVIEW-R4-A2e-fidelity-combined.md` (61fc014: MAJOR-1..2, MINOR-1..10) by id, plus the edits in place. NOTEs optional (NOTE-4 is cheap; take it).

## Ruling (conflict 1: U6 against the uncited Lenski 2023 entry; final, D-38)
**Critic side, with the Day side's record.** An entry in the reference list that no sentence calls does not cite a numeric input under rule F: rule F's "without citation" is about the input, and an uncalled entry ties 3 × 10⁷ to no source and no page. U6 stays scored `unverifiable`, and the proposed value stands.
- A2's Barrick 2009 row is not a precedent against this: A2's "Primary literature" table lists works in the paper's reference list and checks what they say; it does not use an uncalled entry to source a specific Day number. Say that in one line.
- Take MAJOR-1's fix as a record, not a value change: add C(iv) to U6 (Lenski 2023, "Revisiting the Design of the Long-Term Evolution Experiment …", l.732-733, no in-text call; the obvious design source) with outcome "not a citation under rule F (ruling, fix-pass brief A2e-analyst-4)". In section 4 add the Day side's reading as a recorded alternative that does not set the field. In Open 2, put Lenski 2023 first: a fetch that finds Ne ≈ 3 × 10⁷ there is the strongest Day-side route to revisiting U6.
- MAJOR-2: answered by the same text; record that the Day side's `pending` reading was weighed and not taken, with the reason above.
- MINOR-7: take the relabel only (U2 and R-attributed: "`n/a` (K2 gap rule: borrowed, qualitative, uncited; rule F's `n/a` definition does not fit)"). The status stays `n/a`; K2 is criterion text and is not changed.

## Other findings
Accept as written: MINOR-1, -2 (post hoc note; K3 text unchanged), -3, -4 (pick the first sentence if it holds: human Ne only orders 3 × 10⁷ against ≤ 3.3 × 10⁴), -5 (sensitivity row only), -6 (no text change), -8, -9, -10. Registered sections (section 1, 0fd4581) keep their wording; additions are separate sentences labelled post hoc.

## Allowed paths
- `research/checks/results/R4-A2e-fidelity.md`

Grep the quotes files, `REVIEW.md` and `HANDOFF.md` by id; never read them whole. Do not edit the review, claim files, quotes files, ledgers, `parameters.yaml`, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md`, argmap or the board.

## Skill
`fix-pass` (`.claude/skills/fix-pass/SKILL.md`).

## Budget
At most 2 commits. No computation beyond one trivial local process (sha256, grep); no runs, no fetches. Fix passes on this write-up: this is 1 of 2.

## Stop when
- the fix pass is committed and pushed to `research`; OR
- an input is missing or does not match (held `main.txt` sha256 `0287f54b…`): report it, don't work around it; OR
- the work would need a path outside the list, a run or a fetch.

## Not in scope
Integration, the field move, fetching Lenski 2023 or U3-U5, rule F changes, A2e external and internal, other nodes. The review's owner-card lines (a)-(c) go to the owner card, not into the write-up. Ideas: one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (≤ 300 words, as the issue comment)
Commit(s); a table of finding id → accepted / in part / not accepted; the ruling, if you disagree (once; then the owner decides); next step.
