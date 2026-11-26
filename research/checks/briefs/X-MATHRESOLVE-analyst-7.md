# X-MATHRESOLVE-analyst-7: records for branch G's open derivation and lookup objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch F done: EVOA-83, 26a2614, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch G batch: the 11 open `derivation`/`lookup` objects with ids M-7xx in `docs/research/math/objects.yaml`: M-701, M-702, M-703, M-704, M-706, M-707, M-708, M-711, M-712, M-713 (derivation) and M-709 (lookup). Source map: `docs/research/math/sources/branch-G.md`. Model to follow: the branch D to F records `docs/research/math/records/M-401.py` .. `M-606.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves. M-705 (already blocked) and M-710 (data-check) are not in this batch.

## Deliverable
For each of the 11 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), and has an `assert` for every number the object's statement claims, including printed figures the statement says are wrong (assert the corrected value and the size of the gap).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Derivations: closed forms in stdlib, in log10 where the numbers underflow (M-703: 10^-33,979,400, 10^-47,262, 10^-86,020,600; M-701: 1.01^1,474 = 2.34e6 against the printed 14.7, 1,570/14.74 = 106.5). M-704: the binomial mean, SD and the 527 sigma distance in closed form; lambda_50 = 12.3-17.2 is computed if a closed form or a short Poisson sum does it in seconds, otherwise quoted from the held result that reports it (R4 D1) with a locator. M-712: theta = 4 Ne mu in closed form; the simulated heterozygosity ratios (0.97-1.03, 1.00-1.01) are quoted from R4 G2c, not re-simulated. M-706 and M-713 are structural: assert the identities (serial = aggregate only with no overlap; F_max has no mu, N or s term) symbolically on rationals or at two test points, and quote the source sentences each one rests on.
Lookup (M-709): the counts ("Bernoulli" once, "averaging problem" 0) come from the held re-fetch with its sha256, if it is in `sources/raw/`. If it isn't in this checkout, quote the counts from the held result or claim file that reports them and say in the record that the record can't repeat the count (as M-416, M-603 did). Don't fetch.
Grep the quotes files and claim files (G and its children) by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json` for NNN in 701, 702, 703, 704, 706, 707, 708, 709, 711, 712, 713
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on those 11 objects. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If a claim file, `parameters.yaml` or an object statement has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, all records run and pass, each JSON sha256 matches its script, and a spot check of a seeded sample against the claim files. No other review (D-40).

## Stop when
- all 11 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects and records, the M-1xx pilot objects, simulation/regression/data-check objects (M-710), the X-MATHMAP review flags carried in the row (Gd row cites M-604, M-106 G2h no citing row: later map-fix pass), tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml` or an object statement the records contradict; next step.
