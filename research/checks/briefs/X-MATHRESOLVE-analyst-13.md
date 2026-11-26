# X-MATHRESOLVE-analyst-13: record for pilot object M-126

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (pilot batch 3 done: EVOA-89, 31168a5, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, last open `derivation`/`lookup` object: M-126 (model-choice, gene flow as "a structural hindrance to the pace of fixation"), in `docs/research/math/objects.yaml`. Source map: `docs/research/math/sources/gene-flow.md` (row gene-flow@L3; grep the id), and `branch-F.md` rows that cite it. Model to follow: the records `M-101.py` .. `M-125.py` (same `held()`, `post()`, `near()`, `finish()` shape; a stale JSON fails the script). It moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
- **resolved:** `docs/research/math/records/M-126.py` plus `M-126.json`, per math/README "Records". Self-contained (stdlib). Every input has its `parameters.yaml` key or quote id. Every quote is checked verbatim with `held()`/`post()`. This is a model-choice object with no numbers of Day's: quote the sentences each position rests on and record both positions (as M-101, M-115, M-116, M-120 did).
  Notes:
  - Day's position: gene-flow@L3, L6, L7 (migrants must carry an allele between demes; gene flow erases differences between lineages).
  - Neutral case: cite M-209 (Maruyama invariance, B7 q1: under conservative migration the neutral substitution rate is exactly μ). Don't recompute it.
  - Selected case: only if a held source (claim files, quotes-literature, R4 results) gives structured-population fixation times. Otherwise say it is not held. Don't derive a new transit-time formula.
  - LTEE comparison: the flasks are isolated and unstructured. Quote held text for this, and cite M-110 or M-115 for the rate comparison.
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-126.json`.
- **blocked:** a needed input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`; read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Grep source maps, quotes files and claim files by id. Don't read big files whole (AGENTS.md token budget). If anything needs more than a minute of CPU or 500 MB, stop and report.

## Allowed paths
- `docs/research/math/records/M-126.py` and `M-126.json`
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on M-126.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If one of them has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-126.py`.

## Budget
At most 1 commit. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, the record runs and passes, the JSON sha256 matches its script, and a spot check against the source map. No other review (D-40).

## Stop when
- M-126 is resolved or blocked, committed and pushed; OR
- the record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
M-117 and other data-check, simulation and regression objects; rhetoric objects; the map-fix flags carried in the row; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Use explicit paths, never `git add -A`. Run `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; status and key quotes or `blocked_on`; lint output; any number in a claim file, `parameters.yaml`, a source map or the object statement that the record contradicts; next step.
