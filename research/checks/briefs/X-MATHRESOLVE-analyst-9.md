# X-MATHRESOLVE-analyst-9: records for the ROOT/FM open derivation and lookup objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch H done: EVOA-85, 3ca6f84, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, ROOT/FM batch: the 6 open M-9xx objects with resolution `derivation` or `lookup` in `docs/research/math/objects.yaml`: M-901, M-903, M-904, M-907, M-910 (derivation) and M-909 (lookup). Source maps: `docs/research/math/sources/branch-ROOT.md`, `branch-FM.md`. Model to follow: the records `docs/research/math/records/M-401.py` .. `M-808.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
For each of the 6 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), checks each quote verbatim with `held()`, and asserts every number the object's statement claims, including printed figures the statement says are wrong (assert the corrected value and the size of the gap). Inference objects without numbers: quote the sentences each position rests on and record both positions (as M-706, M-713, M-803 did).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Notes per object (closed forms, stdlib):
- M-901: 252,000 / 1,322 = 190.6; 2.05e8 / 190.6 = 1.0754e6 (6.03 orders) against the stated 1,075,000; the mechanism catalogue counts (9 computed or bounded, 3 partial, 5 asserted, relictation) from the ROOT-M claim file as held; the two post dates (2026-09-30 vs 2026-10-05) on ILS, quoted. Cite M-713 for F_max rather than recomputing it.
- M-903: no numbers in the source; quote ROOT-FM q3 and FM5 q1 and assert only what's held (no counts, units, window or ceiling). Record both positions. If the claim is unscoreable without mesa counts, `resolved` with that finding is fine; `blocked` only if a held input is missing.
- M-904: the chrX F1 100 kb R values (3.76 hs1, 3.39 chimp-referenced) and the P3/P4/P5/P7 cell outcomes from the R4 FM results files as committed (read only; no rerun); the rule-N grep finding as recorded. Both positions.
- M-907: 1 - 0.80 = 0.20; the A2e-alpha 9-13% band as held; the 0.23 comparison. Quote DN4 q1, q2.
- M-909 (lookup): quote each endorsement and each counter; state which are held and which are in the paywalled book (not retrieved). No numeric score.
- M-910: 6.3e6 x 1.075e6 = 6.7725e12 y; / 13.8e9 = 490.8 (2.69 orders); 6.3e6 x 2.2e5 = 1.386e12 y (about 100 ages). Keen quotes ROOT-K q1, q2.
Grep the quotes files, claim files and results by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json` for NNN in 901, 903, 904, 907, 909, 910
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on those 6 objects. Leave statements, `used_by`, `sources` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If a claim file, `parameters.yaml` or an object statement has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, all records run and pass, each JSON sha256 matches its script, and a spot check of a seeded sample against the claim files. No other review (D-40).

## Stop when
- all 6 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
The M-1xx pilot objects, other branches' objects and records, M-902/905/906/908/911 (not derivation or lookup), simulation/regression/data-check objects, the X-MATHMAP map-fix flags carried in the row, the ROOT roll-ups, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml` or an object statement the records contradict; next step.
