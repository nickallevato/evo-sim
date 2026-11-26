# X-MATHRESOLVE-analyst-4: records for branch D's open derivation and lookup objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch C done: EVOA-80, 01c2503, approved in 1333b7e); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch D batch: the 12 open `derivation`/`lookup` objects with ids M-4xx in `docs/research/math/objects.yaml`: M-401, M-402, M-406, M-407, M-409, M-410, M-411, M-412 (derivation) and M-414, M-415, M-416, M-417 (lookup). Source map: `docs/research/math/sources/branch-D.md`. Model to follow: the branch A to C records `docs/research/math/records/M-0xx.py`, `M-2xx.py`, `M-302.py` .. `M-305.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves. M-403 and the other data-check or simulation objects are not in this batch.

## Deliverable
For each of the 12 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), and has an `assert` for every number the object's statement claims, including the printed figures the statement says are wrong (assert the corrected value and the size of the gap). The JSON holds values, inputs, the script's sha256 and the date. In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Kind `inference` (M-407): the record computes the numbers under **each** side's position (the `positions` lines) side by side and asserts them. It doesn't choose a side. If a position has no number to compute, say so in the JSON.

Big numbers (20^250, 300,000^500): compute in exact integers or `log10` of exact integers, not floats that overflow. Assert the printed mantissa and exponent.

Lookups (M-414 .. M-417): each value is quoted verbatim from held text with a locator, checked by `held()`. Grep the quotes files and claim files by id; don't read big files whole (AGENTS.md token budget). A lookup whose answer needs text that is not held (for example the Wistar volume itself, if no quote is held) is blocked, not inferred.

## Allowed paths
- `docs/research/math/records/M-401.py` .. `M-417.py` and the matching `.json` (the 12 ids above only)
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on the 12 ids above. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. A wrong number in a claim file or `parameters.yaml`: list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`. Anything over a minute of CPU or 500 MB stops the task.

## Budget
At most 3 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, every record runs and its asserts pass, the JSON sha256 matches the script, and a seeded spot check of 4 records against the claim files. No other review (D-40: arithmetic gets a spot check).

## Stop when
- all 12 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects (A, B and C are done; don't touch their records), the M-1xx pilot objects, simulation/regression/data-check objects (M-403's '53 orders' flag stays in the row), the claim-file flags carried in the X-MATHRESOLVE row, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file or `parameters.yaml` the records contradict; next step.
