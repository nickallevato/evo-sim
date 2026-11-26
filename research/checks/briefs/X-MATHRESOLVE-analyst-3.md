# X-MATHRESOLVE-analyst-3: records for branch C's open derivation objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch B done: EVOA-79, 7324fe9, approved in ea49380); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch C batch: the 5 open `derivation` objects with ids M-3xx in `docs/research/math/objects.yaml`: M-302, M-303, M-304, M-305, M-306. Source map: `docs/research/math/sources/branch-C.md`. Model to follow: the branch B records `docs/research/math/records/M-201.py` .. `M-223.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves. M-301 (simulation), M-307 and M-308 (data-check) are not in this batch.

## Deliverable
For each of the 5 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), and has an `assert` for every number the object's statement claims, including the printed figures the statement says are wrong (assert the corrected value and the size of the gap). The JSON holds values, inputs, the script's sha256 and the date. In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

M-304 is `model-choice`: the record computes the numbers under **each** side's position (the `positions` lines) side by side and asserts them. It doesn't choose a side. If a position has no number to compute, say so in the JSON.

M-303's "exact Wright-Fisher 5.1e-45 per locus from 0.5" at Ne ~ 1e4: a full transition matrix does not fit the local limit. A banded or truncated computation is fine if the record asserts a bound on the truncation error. If no method runs in under a minute and 500 MB, assert the diffusion values, mark that one figure `not_checked_locally` in the JSON with the reason, and list it in the report. Don't go to the host.

## Allowed paths
- `docs/research/math/records/M-302.py` .. `M-306.py` and the matching `.json` (the 5 ids above only)
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on the 5 ids above. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. A wrong number in a claim file or `parameters.yaml`: list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`. Anything over a minute of CPU stops the task.

## Budget
At most 3 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, every record runs and its asserts pass, the JSON sha256 matches the script, and a seeded spot check of 3 records against the claim files. No other review (D-40: arithmetic gets a spot check).

## Stop when
- all 5 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects (A and B are done; don't touch their records), the M-1xx pilot objects, simulation/regression/data-check objects, the claim-file flags carried in the X-MATHRESOLVE row, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file or `parameters.yaml` the records contradict; next step.
