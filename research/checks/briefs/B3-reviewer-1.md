# B3-reviewer-1: one combined review of R4-B3-internal (no field move)

**Role:** reviewer (a fresh instance; you did not write R4-B3-internal). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row B3; rule RD (`R4-X1-verdict-rule.md` l.196-202, owner 2026-10-11); D-40 (one combined review: correctness plus a Day-side and a critic-side section of equal depth).

## Gap item
B3, field `verdicts.internal` of `docs/research/claims/B3-k-neq-mu-values-umbrella.md` (now `pending`). **It does not move in this task.** The move is a later operator integration.

## Deliverable
`research/checks/results/REVIEW-R4-B3-internal-combined.md`, one file. Target: `research/checks/results/R4-B3-internal.md` (26dabc8; brief `B3-analyst-1.md`, 3f0c53e). Three sections, same severity labels (BLOCKER / MAJOR / MINOR / NOTE), numbered findings with evidence and an exact fix:
1. **Correctness.** Every component verdict cited (B3a, B3c, B3d, B3f, B3g, B4, B3m) against its claim file's l.12-14 as it stands; every rule citation (RD l.196-202, S1 l.40, SC l.47, row F l.79, C) against `R4-X1-verdict-rule.md`; D-15 against `DECISIONS.md`; the "Inference: convergent" date (git log of `argmap/standard-forms.md`); the B3 quotes (claim file l.17-29) and their Q-ids against `quotes-*.md` by grep. Whether any component was re-scored, which the brief forbids.
2. **Day-side steelman.** Strongest case for the field as proposed (`holds` under R-a) or for a value more favourable to Day; whether a direction reading (Open 2, R-b″) belongs in the table.
3. **Critic-side steelman**, same depth. Strongest case for `non-sequitur` (R-b as the most defensible reading) or for `pending`; whether R-a is chosen for its verdict despite §2's grounds; whether the row-F double-count analogy holds.

Starting list (not the scope): §3 applicability (can RD rank readings that differ only in how quotes are joined, or is the honest value `pending`?); B3-1's mapping to B3a without a Q-id or k/μ in its own words (Open 3, "Things that looked wrong"); whether the proposed claim-file comment (§5) overstates what `holds` means.

Close with finding counts, a one-line verdict (value licensed as proposed / licensed with changes / not licensed, and if not, whether `pending` is licensed) and the list of wrong items (old -> right).

## Allowed paths
- `research/checks/results/REVIEW-R4-B3-internal-combined.md` (new)

Read anything; grep by id or heading. Never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Do not edit the write-up, claim files, quotes files, ledgers, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md`, argmap or the board.

## Skill
`review-correctness` for section 1, `review-steelman` (both sides) for sections 2 and 3, in one file (D-40).

## Budget
At most 2 commits. No computation beyond grep. No runs, no fetches. Fix passes left on the write-up: 2.

## Stop when
- the review is committed and pushed to `research`; OR
- an input is missing or does not match (a cited line absent, a component verdict differing from its claim file): report it, do not work around it; OR
- the work would touch a path outside the list, or would need a fetch.

## Not in scope
The fix pass, integration, B3 fidelity and external, re-scoring any component (B3a-B3m), rule changes to RD or C (a proposed change is one line in the report, for the owner card). Ideas: one line in the report.

## Commit trailer
`Gap: B3`, then the attribution lines your issue gives you, in one trailer block. Explicit paths only; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (at most 300 words, as the issue comment)
Commits; finding counts by section and severity; each BLOCKER and MAJOR in one line; the verdict on the proposed value; where the two steelman sections conflict (the lead rules once in the fix-pass brief); next step.
