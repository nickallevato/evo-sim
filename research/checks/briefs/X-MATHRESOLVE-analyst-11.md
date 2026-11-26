# X-MATHRESOLVE-analyst-11: records for pilot objects M-109..M-116

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (pilot batch 1 done: EVOA-87, 85cb2b1, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, pilot batch 2: the next 8 open M-1xx `derivation`/`lookup` objects in `docs/research/math/objects.yaml`: M-109, M-110, M-111, M-112, M-115, M-116 (derivation) and M-113, M-114 (lookup). M-117 is a data-check and is not in scope. Source maps: `docs/research/math/sources/evo007.md` .. `evo009.md`, `mailvox.md`, `pgenetics.md` (and the branch maps that cite each object; grep the id). Model to follow: the records `docs/research/math/records/M-101.py` .. `M-108.py` and `M-401.py` .. `M-910.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
For each of the 8 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id, claim file plus quote number, or source-map row), checks each quote verbatim with `held()`, and asserts every number the object's statement claims, including printed figures that are wrong (assert the corrected value and the size of the gap). Inference and model-choice objects without numbers: quote the sentences each position rests on and record both positions (as M-101, M-103, M-706, M-903 did).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Notes per object (closed forms, stdlib):
- M-109: 76.8 x 201,600 x 35e6 / 3.2e9 = 169,344; assert it, and the whole-genome count it is scaled from. Record both positions (which sites the neutral expectation applies to). Cite M-108 for u and M-110 for 201,600 rather than redoing them.
- M-110: 6.3e6 / 25 = 252,000; x 0.80 = 201,600. Cite M-107 for how d enters; say which inputs are held verbatim.
- M-111 (identity): quote the k = mu statement and both positions; the arXiv 2208.00148v1 claim: held text only, else `blocked`. If a held record or check already settles k = mu over a finite window (branch B records), cite it; don't recompute.
- M-112 (model-choice): quote the mailvox rows; "a bottleneck at the optimum only halves the fixation time" is asserted only if the held text gives the derivation; otherwise record that it is unreleased. Gemini output is a relay, not a derivation (rule U).
- M-113 (lookup): the formula as printed against the standard Kimura form; assert the s -> 0 and large-N limits (1/2N, 2s) on a stated example. Cite M-105 / B-branch records where they already use it.
- M-114 (lookup): both parameter sets, each with its `parameters.yaml` key or source-map row; flag any value with no held source (g = 29). No new parameter keys.
- M-115, M-116 (inference): quote both sides (WD/Day, Hancock, Matthews) from the evo008 rows; the highway 3,600 / 360 = 10 is the only number. Cite M-101 and M-103 where they already record the rate-vs-distribution point.
Grep the source maps, quotes files and claim files by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json` for NNN in 109..116
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on those 8 objects. Leave statements, `used_by`, `sources` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If a claim file, `parameters.yaml`, a source map or an object statement has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, all records run and pass, each JSON sha256 matches its script, and a seeded spot check against the source maps and claim files. No other review (D-40).

## Stop when
- all 8 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
M-117 (data-check), M-118..M-126 (later batches), other branches' objects and records, simulation/regression/data-check objects, the map-fix flags carried in the row, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml`, a source map or an object statement the records contradict; next step.
