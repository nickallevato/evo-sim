# X-MATHRESOLVE-analyst-14: claim-file correction pass (plus four map-fix leftovers)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE, `next` step (1); `docs/research/math/README.md` ("Records"). The map-fix pass is done (EVOA-91, 33d0f28); this is the claim-file half of the "Carried ..." notes in the same row.

## Gap item
X-MATHRESOLVE, claim-file part. No verdict field, status field or claim-tree edge moves. The parameters.yaml keys (d = 0.80, N_e 33,000, g = 29; day_alt 32.5) are NOT in this task; they are the next one.

The list is the row's `next` (grep `Carried from`). Work through every "Carried ... claim-file pass" note for branches A, B, C, D, E, G, H, ROOT/FM and pilot batches 1-3. For each note:
- a wrong number or word in a claim file (e.g. A6 l.46 600 -> 625; B4 494 -> 495.0; B RHclose 2.25x -> 2.32x; claim H l.72 27.8/278 -> 27.63/276; E4 `derived:` 1.146 -> 1.148, 20.6%; D3a "matches" -> 10^55.02, just over; DN4 9-13% -> up to 13.5%; H7 70 -> [60, 100]): correct it in the claim file, with a dated `<!-- X-MATHRESOLVE 2026-11-26: was ..., M-NNN record -->` comment;
- a number printed in an R4 results file (R4-H-C2 l.10, l.111; R4 G1 flip table; R4-FM chrX): don't edit the results file; add the correction as one line in the affected claim file's R4 paragraph, citing the M-NNN record;
- a note marked "note only", "not a record fix" or "within rounding" (M-416, M-502, M-601/606/603, M-702, M-709, M-123, M-125, H8 2,631): no edit; list it as "no change" in the report.

Map-fix leftovers (EVOA-91 report), one ruling each:
1. evo010@L22 speaker: set the speaker cell to relayed Athos output (rule U), and update the M-120 record's quote of that row to match.
2. evo005 M-105 row: 76,050.6 -> 76,050.4; update the M-105 record's quote of the row.
3. M-126 `used_by` F: **ruling:** remove F and add a `new_claim` proposal, "Gene flow adds a stage to every fixation and works against divergence, so it cannot close the accounting gap; Day (day side)", as other unclaimed Day objects do. Update the branch-F map note.
4. M-507 statement: "20.4%" -> "20.6%" for 2N = 30; M-103 Day position: add that a standing start cuts sweep time 27-50% (capped at 2x), per the M-103 record.

For records M-105 and M-120 change only the quoted text (and the sha256/json the record writes); rerun them.

## Deliverable
One commit (two if the record edits are cleaner apart). Before committing, run every record (`for f in docs/research/math/records/M-*.py; do research/.venv/bin/python -I "$f" || echo FAIL $f; done`), `research/tools/math_map.py --lint` and `research/tools/lint_research.py`, as separate commands. All must pass.

## Allowed paths
- `docs/research/claims/*.md` (text and comments only; no verdict, status or edge fields)
- `docs/research/math/objects.yaml` (M-103, M-126, M-507 only: statement, positions, `used_by`, `new_claim`)
- `docs/research/math/sources/*.md`
- `docs/research/math/records/M-105.*`, `docs/research/math/records/M-120.*`

Read anything. Don't edit results files, parameters.yaml, hierarchy*, gap-blockers.yaml, ledgers, QUEUE/REVIEW/RESULTS, argmap or the board.

## Skill
`fix-pass` (correction comments, no verdict moves). No host, no fetch (O-7).

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: lints 0 errors, all records pass, `git show --stat` inside the allowed paths, seeded spot check of 4 corrections. No other review (D-40).

## Stop when
- every carried claim-file note is fixed or listed as "no change", and the four leftovers are done, committed and pushed; OR
- a correction would move a verdict, or needs a judgment the M-NNN record does not settle: list it, don't guess; OR
- a fix needs a path outside the list.

## Not in scope
parameters.yaml keys (next task); P3 compute; new checks; tooling; `people.yaml`; the "Idea (not queued)" lines.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; corrections made (count, by branch); "no change" notes; leftovers 1-4; records run (pass count); lint output; anything stopped on.
