# X-MATHRESOLVE-analyst-1: records for branch A's open derivation and lookup objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (unblocked when X-MATHMAP closed, 41f5057); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch A batch: the 14 open `derivation`/`lookup` objects with ids M-0xx in `docs/research/math/objects.yaml`: M-001, M-002, M-003, M-005, M-006, M-007, M-012, M-013, M-014, M-015, M-016, M-017, M-018, M-019. Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
For each of the 14 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), and has an `assert` for every number the object's statement claims, including the printed figures the statement says are wrong (assert the corrected value and the size of the gap). The JSON holds values, inputs, the script's sha256 and the date. In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Kinds `inference` and `model-choice` (M-005, M-006, M-012, M-016, M-018, M-019): the record computes the numbers under **each** side's position (the `positions` lines) side by side and asserts them. It doesn't choose a side. The choice stays with the claim verdicts. Resolved means the arithmetic of both readings is fixed and cited. If a position has no number to compute, say so in the JSON and set the object to blocked only if a number the statement claims can't be checked.

Lookups (M-002, M-003, M-014): each value is quoted verbatim from held text with a locator. Grep the quotes files and claim files by id; don't read big files whole (AGENTS.md token budget).

## Allowed paths
- `docs/research/math/records/M-001.py` .. `M-019.py` and the matching `.json` (the 14 ids above only)
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on the 14 ids above. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. A wrong number in a claim file or `parameters.yaml`: list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`. Anything longer stops the task.

## Budget
At most 3 commits. Fix passes left: 2 of 2. Lead review: `math_map.py --lint` at 0 errors (it checks that each `resolved_by` exists), every record runs and its asserts pass, the JSON sha256 matches the script, and a seeded spot check of 5 records against the claim files. No other review (D-40: arithmetic gets a spot check).

## Stop when
- all 14 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects, the M-1xx pilot objects, simulation/regression/data-check objects, the minor findings carried for other branches in the X-MATHRESOLVE row, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file or `parameters.yaml` the records contradict; next step.
