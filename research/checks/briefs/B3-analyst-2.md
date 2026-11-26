# B3-analyst-2: fix pass 1 of 2 on R4-B3-internal (no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row B3; review `research/checks/results/REVIEW-R4-B3-internal-combined.md` (38e19ef, approved as EVOA-55); rule RD (`R4-X1-verdict-rule.md` l.196-202); D-40; OPERATING-PROCESS (one ruling per conflict, no fresh check of it, D-38).

## Gap item
B3, field `verdicts.internal` of `docs/research/claims/B3-k-neq-mu-values-umbrella.md` (`pending`). **It does not move in this task.**

## Lead ruling (the one ruling on the steelman conflict D-1 vs C-1 / K-1)
**For C-1 / K-1. The proposal becomes `pending`, not `holds`.** Reasons:
1. RD ranks readings of a quote (l.197-198). §3 itself concedes that R-a and R-b read every quote the same way, so l.198 gives no ranking (C-1).
2. D-1 is declined. R-b is not a "wider claim" the audit assembled (l.202). It is S1's default, which scores the node "on its verbatim Statement quotes" (l.40), and B3-2 is one of them (K-2). The disjunction drops B3-2's quoted claim, and that is the reading best for the speaker (K-1, D-15).
3. The SCOPED route (C-1 fix (a)) is also declined. A lead ruling that writes "k ≠ μ, convergent" into the Formal statement makes the same choice of joining, by fiat. Choosing how an umbrella aggregates its children is new process machinery and needs an owner decision (K-1; ROADMAP B5 is the related open proposal). The lead puts it on the owner card as one line. This task does not ask the owner.
4. D-3 is recorded: `pending` withholds a credit that B3d earned on Day's own arithmetic. The reason is the audit's missing rule, not his error. The claim-file comment must say so.

## Deliverable
`research/checks/results/R4-B3-internal.md`, edited in place, plus a new section "Review resolution (fix pass 1, 2026-11-26)". Answer every MAJOR and MINOR by id (C-1, C-2, C-3, C-4, D-1, D-2, K-1, K-2, K-3, K-4): accepted, in part, or not accepted, with the reason and what changed. Per the ruling:
- §2 and §3: the proposed value is `pending`, with §3's reason ("the verdict depends on how the node aggregates its quotes, not on how any quote is read; no current rule sets it"). Keep the Readings table as the record an owner rule would use. Give R-a and R-b equal standing; neither sets the field.
- Apply the reviewer's wrong-items list 1-5 (B3-1 as quoted = a ratio with no k/μ and no Q-id; R-c's grounds; §2 point 3 changed to a counting note; B3b added). Add the K-3 facts and the D-2 row R-b″, unscored. C-5 is optional, as one clause.
- §5: rewrite the proposed claim-file comment for `pending` (no `reading-dependent:` prefix, no `holds`). It names the aggregation gap, the D-3 cost to Day, and the one-route and external-`contradicted` limits (K-4).
- §4 "Who this helps": update it for `pending`, both sides at equal depth.

## Allowed paths
- `research/checks/results/R4-B3-internal.md`

Grep other files by id; never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Don't edit claim files, the review, ledgers, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md`, argmap or the board.

## Skill
`fix-pass` (`.claude/skills/fix-pass/SKILL.md`).

## Budget
At most 2 commits. No runs, no fetches, no computation beyond grep. Fix passes left after this one: 1.

## Stop when
- the fix pass is committed and pushed to `research`; OR
- a cited line or component verdict is missing or differs from its file (report it; don't fix it); OR
- the work would need a path outside the list. If you disagree with the ruling, record your position in the resolution, apply the ruling, and say so in the report. The owner decides after one round.

## Not in scope
Re-scoring any component (B3a-B3m); B3 fidelity or external; proposing the umbrella aggregation rule itself (one line in the report at most); other nodes.

## Commit trailer
`Gap: B3`, then the attribution lines your issue gives you, in one trailer block. Explicit paths; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; each finding id with its resolution in one line; the final proposed value and comment line; next step (operator integration of the comment, field stays `pending`; row to `owner` for the aggregation rule).
