# F1a-analyst-1: fix pass on R4-F1a answering independent review MAJOR-1 and the dispersion MINOR (no verdict move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row F1a; `research/checks/results/REVIEW-R4-F1a-independent.md` (MAJOR-1 l.5, MINOR-1..5); `REVIEW-R4-F1a-combined.md` (MINOR-1..4, NOTE-1).

## Gap item
F1a (`docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md`), field `status` (`extracted`). This fix pass is the precondition for `reviewed`; the status field itself moves later, in an integration task. **No verdict value moves** (internal `non-sequitur`, fidelity `n/a`, external `pending` stay).

## Deliverable
One edit of `research/checks/results/R4-F1a.md`: replace the one-line "Review resolution" (l.29-30) with "Review resolution (fix pass, 2026-11-26)" that answers, by id, every MAJOR and MINOR of both reviews (independent MAJOR-1, MINOR-1..5; combined MINOR-1..4): accepted, in part, or not accepted, with the reason and what changed.
- **MAJOR-1 (near-circular design):** say plainly in the write-up what the run does and does not add beyond B0 (engine reproduces Kimura at 4Ns = 40; supply sets the count by construction), and correct any sentence that presents the met predictions as independent evidence. Registered wording stays; new sentences are labelled post hoc.
- **Dispersion (independent MINOR-1, combined NOTE-1):** var/mean 1.53 at k = 100 is about 2.5 SE above 1. Either show the overlap explanation from the existing `results/raw/f1a.json` per-replicate counts, or withdraw it and record the overdispersion as unexplained. If you compute, use a post hoc script (below), committed and pushed **before** it runs, with a docstring saying what was already seen and what each side expects. Original outputs are never overwritten.

## Allowed paths
- `research/checks/results/R4-F1a.md` (edit)
- `research/checks/f1a_posthoc_dispersion.py` (new, optional) and `research/checks/results/raw/f1a_posthoc_dispersion*` (its output, optional)

Read anything; grep big files by id. Do not edit the claim file, the review files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `gap-blockers.yaml`, ledgers, argmap, `DECISIONS.md` or the board.

## Skill
`fix-pass`. Any computation on na-workhorse only, per AGENTS.md "How to run" (one process, reading the existing raw file, no new simulation); never commit from the host.

## Budget
At most 3 commits. Fix passes left: 2 of 2 (this is the first). No new simulation runs; no fetches.

## Stop when
- the fix pass is committed and pushed to `research`; OR
- an input is missing (e.g. `f1a.json` lacks per-replicate counts and the answer would need a rerun): record "not shown" in the resolution, report it, don't rerun; OR
- the work would touch a path outside the list, need a new quote, or change a rule.

## Not in scope
F1a external (a separate check after this); F1/F1b; status or verdict field moves; integration; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: F1a`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; one line per review item (id, accepted / in part / not, what changed); the dispersion result if computed; whether the write-up is ready for status `reviewed`; next step.
