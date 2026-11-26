# X-MATHRESOLVE-analyst-6: records for branch F's open derivation and lookup objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch E done: EVOA-82, 1344843, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch F batch: the 5 open `derivation`/`lookup` objects with ids M-6xx in `docs/research/math/objects.yaml`: M-601 (derivation: sweep latency (2/s) ln(2Ne) against the stochastic conditional mean), M-602 (derivation: the human 19,807 divisor and the 6.3 / 7.4 fixation counts), M-603 (lookup: s = 0.001 attributed to Zeng et al. 2021), M-605 (derivation: fixation probability u against rate k = 2N x flux x u) and M-606 (lookup: SD of the conditional neutral fixation time, 0.538 x 4Ne). Source map: `docs/research/math/sources/branch-F.md`. Model to follow: the branch D and E records `docs/research/math/records/M-401.py` .. `M-507.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves. M-604 and other branch F objects of other kinds are not in this batch.

## Deliverable
For each of the 5 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), and has an `assert` for every number the object's statement claims, including printed figures the statement says are wrong (assert the corrected value and the size of the gap).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Derivations (M-601, M-602, M-605): closed forms in stdlib. Assert 19,807 / 1,981 / 39,614, 8,532 / 1,314 / 14,292, the 2.32x ratio, the window logarithms 4.595 / 9.190 against ln(2Ne) = 9.9035, 6.3 and 7.4, and the k identities (k_neutral = mu, k_ben = 4N s U_b) symbolically or at two test points. M-602's inputs that the statement calls a claim-file reconstruction are labelled as such, not as Day's.
Lookups (M-603, M-606): each figure quoted verbatim from held text with a locator, checked by `held()`. M-606: compute sqrt(pi^2/3 - 3) and assert 0.538 and 2.15; the simulated 2.105 / 2.108 are quoted from the held result that reports them, not re-simulated. A "not in Kimura and Ohta 1969" finding needs the held text it rests on; if the paper itself is not held, say so in the record, as M-416 did.
Grep the quotes files and claim files (F, F1a, F3, F3a, F4a, F5) by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-601.py`, `M-601.json`, `M-602.py`, `M-602.json`, `M-603.py`, `M-603.json`, `M-605.py`, `M-605.json`, `M-606.py`, `M-606.json`
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on M-601, M-602, M-603, M-605, M-606. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If a claim file, `parameters.yaml` or an object statement has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, all five records run and pass, each JSON sha256 matches its script, and a spot check of a seeded sample against the claim files. No other review (D-40).

## Stop when
- all 5 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects and records, the M-1xx pilot objects, simulation/regression/data-check objects, the X-MATHMAP review flags carried in the row (F3 q2 window wording, used_by rows with no citing row M-105/106/116/125/126: these go to a later map-fix pass), tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml` or an object statement the records contradict; next step.
