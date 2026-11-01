# B-analyst-1: fix pass 3 on B internal, answering EVO-83

**Role:** analyst. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/OPERATING-PROCESS.md`, "First tasks" item 2 ("answer EVO-83's MAJOR in one fix pass, then integrate. If that fails, send it to the owner; there is no fourth ruling"). This is the last fix pass B gets (limit: 2 per check, plus this one by the owner's first-tasks list).

## Gap item
B. Field: `verdicts.internal` of `docs/research/claims/B-neutral-theory-cannot-rescue.md`. **It does not move in this task.** It stays `pending`. The write-up's proposed value (scoped `holds`, section 4) stays a proposal until integration, which is a separate task.

## Deliverable
`research/checks/results/R4-B-internal.md` with a new section "Review resolution 3 (fix pass 3, 2026-11-01): EVO-83 (`REVIEW-R4-B-internal-ruling-check-2.md`, 36617f9)". It answers every finding of that review by id. Apply the corrections in place in sections 3a and 4 where needed, and mark each one `[fix pass 3]`.

## Lead errata to B-R11..B-R13 (these adopt EVO-83's fixes as written; this is not a new ruling)
- **E1 (MINOR-2, B-R11/SL1):** replace "the only place HL introduces and applies 'lineage duration'" with EVO-83's wording: "every use of the exact term 'lineage duration' (l.130, l.150, l.248) is the G of the census ceiling; HL uses 'the lineage' in the completion sense at l.416-417 and l.433".
- **E2 (MAJOR-1, B-R12/SL2):** strike "They are not the inputs of C" and every argument that rests on Q157's input list. Ground "not a different object" on HL's own statements of S_L's proposition (E3).
- **E3 (NOTE-3 and MAJOR-5, B-R11/SL1):** "it is Day's own computation" becomes "HL states it (l.166-169, l.251-253, l.436-438)". Quote l.436-438 verbatim, because it uses Q157's verb "fills" with a census subject. Check each quote against `sources/raw/b-steelday-2026-10-13/hl.txt`, sha256 `3182a5b6cd3a8ac822017d6d7f509c234ab147b334546d62f88623142d9dbfe2`, first. If the hash differs, stop.
- **E4 (MAJOR-4(i), B-R13 / section 3a "What this costs"):** add one sentence saying that this reverses the recorded effect of D-15 (`R4-X1-verdict-rule.md` l.198: "B internal moves from `holds` to `non-sequitur`"), and that SL4 (the inference read at census level, l.353-354) is the whole ground of the difference from the 2026-10-11 S row.
- **MAJOR-4(ii) and (iii)** (a note under D-15 in `DECISIONS.md`, and an annotation of RD l.198 under the freeze procedure) are **for the owner**. The lead has put them on the issue. Record them as "referred to the owner, 2026-11-01" and do not edit either file.
- **MAJOR-5, the L-R12 half:** out of scope (L5, EVO-82, owner). Record that B's admission of S_L holds under both the strict and the loose test, as the review found.
- **MAJOR-6, MAJOR-7, MAJOR-8, MINOR-9, NOTE-10, NOTE-11 (B-R21 tooling):** answer each by id from what landed: B-R22..B-R30 in `docs/research/DECISIONS.md` and `research/checks/QUEUE.md` l.33-46 (lint clean, `verdict_scope` in `hierarchy.yaml`, `scope_guard.py`). For each one, name the file and line that closes it, or say it is still open. The publication hold stands either way. **If any of MAJOR-6/7/8 is not closed by what landed, say so plainly and stop there.** Do not fix tooling.

## Allowed paths
- `research/checks/results/R4-B-internal.md`

Read anything you need. Grep by id or line; never read `REVIEW.md`, the quotes files or `HANDOFF.md` whole. Write nothing else: no claim file, no `DECISIONS.md`, no rule file, no `gap-blockers.yaml`, no `QUEUE.md`.

## Skill
`fix-pass` (`.claude/skills/fix-pass/SKILL.md`). No post hoc computation is needed. If you think one is needed, stop and report instead.

## Budget
At most 2 commits. Fix passes left after this one: 0. If any finding cannot be answered under the errata above, record both positions and stop. Do not choose.

## Stop when
- the deliverable is committed and pushed to `research`; OR
- an input is missing (hash mismatch, a cited line that does not say what EVO-83 quotes) or a MAJOR-6/7/8 tooling item is still open: report it and do not work around it; OR
- the work would touch a path outside the list above.

## Not in scope
Integration (claim file, REVIEW.md, QUEUE.md, argmap, lint renders), L5/L-R12, the board, publication, DECISIONS.md, rule files, other nodes, tooling. Ideas go in one line in the report.

## Commit trailer
`Gap: B`, then the attribution lines your issue gives you. Use explicit paths only. Run `git pull --rebase origin research` before `git push origin research`. Do not push to `master`.

## Report (at most 300 words, as the issue comment)
Commits; a table of EVO-83 findings 1-11, each with accepted / in part / not accepted / referred, and the section changed; whether the proposed field comment (section 4) changed; anything still open for the owner.
