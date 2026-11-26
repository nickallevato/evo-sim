# X-MATHRESOLVE-analyst-12: records for pilot objects M-118..M-125

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (pilot batch 2 done: EVOA-88, 59afa3a, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, pilot batch 3: the next 8 open M-1xx `derivation`/`lookup` objects in `docs/research/math/objects.yaml`: M-119, M-120, M-125 (derivation) and M-118, M-121, M-122, M-123, M-124 (lookup). M-117 is a data-check and M-126 is the next batch; neither is in scope. Source maps: `docs/research/math/sources/evo008.md`, `evo010.md`, `pgenetics.md`, `pykf.md`, `gene-flow.md`, `smokescreen.md` (and the branch maps that cite each object; grep the id). Model to follow: the records `docs/research/math/records/M-101.py` .. `M-116.py` and `M-401.py` .. `M-910.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
For each of the 8 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id, claim file plus quote number, or source-map row), checks each quote verbatim with `held()`, and asserts every number the object's statement claims, including printed figures that are wrong (assert the corrected value and the size of the gap). Inference and model-choice objects without numbers: quote the sentences each position rests on and record both positions (as M-101, M-103, M-115, M-116 did).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Notes per object (closed forms, stdlib):
- M-118 (lookup): which edition the critics used. Held text only (evo008@L61 is Duffy relayed); if no held page/figure comparison of the two editions exists, `blocked` naming the two files needed.
- M-119 (inference): quote the circularity claim and both positions. If a resolved record already settles how divergence dates and k = mu relate (M-111, branch B/C records), cite it; don't recompute.
- M-120 (model-choice): assert Day's thresholds 1/(2N_e) at 10,000 / 10 million / 80 million (5e-5, 5e-8, ~6.25e-9) and the N_e/N = 0.01 step; record both readings (visibility criterion vs differential survival). Cite branch A/H records where they already use 1/(2N_e).
- M-121 (lookup): 0.86 and 0.015 from held text; "the chart" only if held, else say it is not held. Cite M-110 (0.80) and M-114 (0.45); no new parameter keys.
- M-122, M-123 (lookup): the LTEE counts (9 of 12, 5 of 9, 3 of 5) and the slowdown are checked against held spreadsheets only. If the spreadsheets are not in `sources/raw/` or `research/checks/**`, `blocked` naming the file; the quote itself can still be checked verbatim.
- M-124 (lookup): Athos is an LLM relay (rule U), not a source. Assert nothing it says; record what held literature (if any) states on pykF/spoT function, else `blocked`.
- M-125 (derivation): "about half" and "under 8%" from smokescreen@L15; assert them against Day's held relictation and selection counts if held (cite the record that has them), and the "tens of millions" remainder against 35M (M-109). Hitchhiking and relictation as routes: quote only.
Grep the source maps, quotes files and claim files by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json` for NNN in 118..125
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
M-117 (data-check), M-126 (next batch), other branches' objects and records, simulation/regression/data-check objects, the map-fix flags carried in the row, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml`, a source map or an object statement the records contradict; next step.
