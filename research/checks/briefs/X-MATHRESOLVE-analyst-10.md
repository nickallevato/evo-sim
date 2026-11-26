# X-MATHRESOLVE-analyst-10: records for pilot objects M-101..M-108

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (ROOT/FM done: EVOA-86, 23451b3, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, pilot batch 1 of 4: the first 8 of the 25 open M-1xx `derivation`/`lookup` objects in `docs/research/math/objects.yaml`: M-101, M-102, M-103, M-105, M-106, M-107, M-108 (derivation) and M-104 (lookup). Source maps: `docs/research/math/sources/evo005.md` .. `evo010.md` (and the branch maps that cite each object; grep the id). Model to follow: the records `docs/research/math/records/M-401.py` .. `M-910.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
For each of the 8 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id, claim file plus quote number, or source-map row), checks each quote verbatim with `held()`, and asserts every number the object's statement claims, including printed figures that are wrong (assert the corrected value and the size of the gap). Inference and model-choice objects without numbers: quote the sentences each position rests on and record both positions (as M-706, M-713, M-803, M-903 did).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Notes per object (closed forms, stdlib):
- M-101 (inference): an average rate X/Y as a bound for a stochastic process. Quote both sides from the evo006/007/009 rows; no number to assert unless the rows print one.
- M-102: 398,673,272 / 6.3e6 = 63.281 bp/y; the six-ape mean 62.7 and x 25/0.8 = 1,958.81 bp per effective generation (assert which unrounded mean gives 1,958.81; the factor 25/0.8 is inferred, say so).
- M-103 (model-choice): LTEE transfer to humans (clonal start, no recombination, no standing variation). Quote each position; cite the A2e/A5 records or claim files where they already carry a number; don't recompute settled ones (cite the record).
- M-104 (lookup): 0.875 x 0 + 0.125 x 0.0012 = 1.5e-4; alpha 12.5% and N_e s = 12 / 10,000 as held (McDonald-Kreitman, Tataru). Say which inputs are held verbatim and which only as relayed.
- M-105: (2/s) ln(2 N_e s) at s = 1.5e-4, N_e = 1e4, 1e5, 1e6 = 14,648, 45,349, 76,051; / 0.80: 14,648 -> 18,310 and 40,000 -> 50,000.
- M-106: sum(s_i) <= s_max, sum = n x s-bar, so the DFE shape cancels. Assert the identity on a held example if the source gives one; otherwise quote and record both positions. Cite M-808 for K_sel rather than redoing it.
- M-107 (model-choice): d vs N_e scaling (WD, Hancock, Day). Quote each; cite the branch A/B/C records that already settle d's arithmetic.
- M-108: 76.8 / 3e9 = 2.56e-8, against the ~35M SNV divergence; assert the ratio the source draws, and say whether the comparison is like for like.
Grep the source maps, quotes files and claim files by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json` for NNN in 101..108
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on those 8 objects. Leave statements, `used_by`, `sources` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If a claim file, `parameters.yaml` or an object statement has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, all records run and pass, each JSON sha256 matches its script, and a seeded spot check against the source maps and claim files. No other review (D-40).

## Stop when
- all 8 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
M-109..M-126 (later batches), other branches' objects and records, simulation/regression/data-check objects, the X-MATHMAP map-fix flags carried in the row, tooling (the shared `held/near/finish` module idea stays an idea), new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml` or an object statement the records contradict; next step.
