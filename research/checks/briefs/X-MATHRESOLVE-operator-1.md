# X-MATHRESOLVE-operator-1: one map-fix pass (objects.yaml and source maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE ("Fix in one operator map-fix pass after the record batches, not inside them"); `docs/research/math/README.md` (schema, "Records"). All derivation and lookup objects are now settled (EVOA-90, 9280424), so this pass is due.

## Gap item
X-MATHRESOLVE, map-fix part. No object `status`, claim field or verdict moves. The fix list is in the row's `next` (grep `Fix in one operator map-fix pass`); the items are copied here:
1. M-403 statement: "53 orders" spans Axe vs Taylor only (about 65 with Keefe-Szostak). Say which sources the span covers.
2. `branch-E.md`: quotes wrapped twice; wrap once in straight `"..."`.
3. M-115 `used_by` E2 has no citing row; M-501 statement should read carrier frequency 1/280.
4. `branch-F.md` F3 q2: window p = 0.01-0.99 sits against ln 2Ne; note it in the row.
5. `used_by` entries with no citing row: M-105 F3, M-106 F1, M-116 F1, M-125 F6, M-126 F, M-106 G2h, M-120 H10. For each, add the row if the claim file has a quote that uses the object; otherwise remove the node from `used_by`.
6. `branch-G.md` Gd row cites M-604, but Gd is not in M-604 `used_by`: add it.
7. H Term 3: about 6,650 in H1/H8 (M-805, M-808) vs about 6,690 in H5 l.39. Say in M-805/M-808 statements which files print which (M-808 record: 6,651.6 closed form).
8. ROOT-M q4: add the ILS `candidate:` flag to its row if the claim file does not already state it.
9. M-801 `sources`: add FM5#q1.
10. `evo010.md` row evo010@L22: speaker is Vox Day, but L18-L26 sit between "I asked Claude Athos" (L17) and "I also asked the Red Team" (L27). Mark the speaker as relayed Athos output (rule U).
11. `evo005.md` M-105 row: 76,050.6 should be 76,050.4 (closed form; Day printed 76,051).
12. M-901 statement: 220,000x is held only in `quotes-day.md` row 14 and `PLAN.md`, not `ledgers/versions.md`.
13. M-904 statement: "contradicts" the uniform-rate premise; claim ROOT-FM says N2b is not triggered. Give both, as the M-904 record does.
14. M-507 statement: the 2N = 30 peak is 1.148 at f = 60% (20.6%), not 1.146.
15. M-126 critic position: "can be shorter or longer ... (a derivation, not done)" has no held source. Reword per the M-126 record: rate unchanged (Maruyama, M-209); latency not held.
M-705 (blocked on the book) needs no change.

## Deliverable
One commit editing the files below. Before committing, run every record (`for f in docs/research/math/records/M-*.py; do research/.venv/bin/python -I "$f" || echo FAIL $f; done`) and `research/tools/math_map.py --lint`, as separate commands. Records quote `objects.yaml` and source maps verbatim: if a fix breaks a record, undo that fix and list it in the report. Don't edit records.

## Allowed paths
- `docs/research/math/objects.yaml` (statements, positions, `sources`, `used_by` only)
- `docs/research/math/sources/*.md`

You can read any file. Don't edit records, claim files, `parameters.yaml`, `hierarchy*`, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS, argmap or the board.

## Skill
`deref-source` (merge-step rules: one wrap per quote, `used_by` and rows consistent both ways). No host, no fetch (O-7).

## Budget
At most 1 commit. Fix passes left: 2 of 2. Lead review: lint 0 errors, all records pass, `git show --stat` inside the allowed paths, and a seeded spot check of 4 fixed items. No other review (D-40).

## Stop when
- all 15 items are fixed or listed as skipped (with reason), committed and pushed; OR
- a fix needs a path outside the list, a fetch, or a judgment the claim file does not settle (list it; don't guess).

## Not in scope
The "Carried ... claim-file pass" and parameters notes in the row (next task); M-117 and other open data-check, simulation and rhetoric objects; tooling; `people.yaml`. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; items fixed / 15; skipped items with reason; records run (pass count); lint output; next step.
