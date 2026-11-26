# X-MATHRESOLVE-analyst-5: records for branch E's open derivation and lookup objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch D done: EVOA-81, 5e2e8ef + de6e47b, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch E batch: the 2 open `derivation`/`lookup` objects with ids M-5xx in `docs/research/math/objects.yaml`: M-502 (lookup: which LTEE populations are mutators and by what route) and M-507 (derivation: relictation under the Cannings jackpot model, t/4Ne above the Wright-Fisher baseline). Source map: `docs/research/math/sources/branch-E.md`. Model to follow: the branch D records `docs/research/math/records/M-401.py` .. `M-416.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves. M-501, M-503..M-506 (simulation, data-check) are not in this batch.

## Deliverable
For each of the 2 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), and has an `assert` for every number the object's statement claims, including printed figures the statement says are wrong (assert the corrected value and the size of the gap). In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

M-507 is an exact Markov chain: compute it in stdlib (fractions or floats, a small matrix or recursion) for the population sizes and jackpot fractions the statement names, and assert the 14.9%, 20.4% and 28.8% figures and the Wright-Fisher baseline. If the statement's figures come from a run whose parameters aren't all held, compute what is held and block the rest. Anything over a minute of CPU or 500 MB: stop and report (it then becomes a simulation object, not a record).

M-502 (lookup): each population and route quoted verbatim from held text with a locator, checked by `held()`. Grep the quotes files and claim files (E, E3, E8) by id; don't read big files whole (AGENTS.md token budget). Assert the counts (six at 50,000, seven at 60,000, the 96.5% share) against the quotes.

## Allowed paths
- `docs/research/math/records/M-502.py`, `M-502.json`, `M-507.py`, `M-507.json`
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on M-502 and M-507. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. A wrong number in a claim file, `parameters.yaml` or an object statement: list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, both records run and pass, the JSON sha256 matches the script, and a spot check of both records against the claim files. No other review (D-40).

## Stop when
- both are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects and records, the M-1xx pilot objects, simulation/regression/data-check objects, the X-MATHMAP review flags carried in the row (branch-E quote wrapping, M-115 used_by E2, M-501 carrier frequency: these go to a later map-fix pass), tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml` or an object statement the records contradict; next step.
