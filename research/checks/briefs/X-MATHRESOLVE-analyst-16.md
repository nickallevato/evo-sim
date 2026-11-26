# X-MATHRESOLVE-analyst-16: load-bearing data-check objects, plus the two cite-only simulation objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (P3 manifest done: EVOA-94, db4e99d, lead-approved); `docs/research/math/README.md` ("Records"; l.48: a full R4 check stays the record, and its object points at the R4 file); `docs/research/math/compute-manifest.md`.

## Gap item
X-MATHRESOLVE, data-check part 1: the 7 open `data-check` objects that a load-bearing node uses: M-008, M-202, M-206, M-214, M-215, M-503, M-902. Also the two simulation objects the manifest settles without compute: M-501 (cite `research/checks/results/R4-E.md`) and M-413 (cite `R4-D15.md`). Each object moves `status: open` to `resolved` or to `blocked`. No claim verdict moves.

## Deliverable
For each of the 9 objects, one of:
- **resolved by an R4 file:** an existing `research/checks/results/R4-*.md` (or a `RESULTS.md` entry with its script) already measures what the statement claims, on held data. Set `status: resolved` and `resolved_by: research/checks/results/R4-<ID>.md`. Give the section and the number that settles it in the report. Likely cases: M-214 (R4-B3m), M-202 (R4-B1c), M-902 (R4-FMnull), M-501, M-413. Verify each one; don't assume.
- **resolved by a record:** no R4 file covers it, but held data does (`sources/raw/`, `research/checks/**`, read only). Write `docs/research/math/records/M-NNN.py` plus `.json` in the shape of M-101..M-126 (`held()`, `near()`, `finish()`, stdlib, under a minute, under 500 MB), and assert every number in the statement, including printed figures that are wrong.
- **blocked:** a needed input is not held (no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact file or text>"` (or `outside:`). M-503's strict count is probably blocked on the same Good 2017 clade-aware files as E6 (`R4-E6-external-feasibility.md`). If so, use E6's wording; don't open a second request.
An object can be resolved for one leg and still fail on another. In that case, resolve it only if the open leg is a verdict question and not a number. Otherwise block it, and name the leg.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json`, for NNN in 008, 202, 206, 214, 215, 503, 902
- `docs/research/math/objects.yaml`: only `status`, `resolved_by` and `blocked_on`, on those 9 objects

Don't edit claim files, `parameters.yaml`, R4 results, source maps, `compute-manifest.md`, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. List wrong numbers you find there in the report.

## Skill
`design-check`, adapted as in analyst-12: no host and no pre-registration commit. Its rules on asserting every input and label apply. Grep big files by id; don't read them whole.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `math_map.py --lint` and `lint_research.py` at 0 errors, every new record runs and passes with a matching sha256, `git show --stat` inside the list, and a seeded spot check of 3 objects against the cited R4 sections. No other review (D-40).

## Stop when
- all 9 are resolved or blocked, committed and pushed; OR
- a record needs over a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
The other 15 data-check objects (next part); M-301, M-405, M-505, M-506, M-604; the stale `compute`/`positions` fields the manifest found (M-301, M-505, M-501); tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, `resolved_by` with the settling number (or `blocked_on`); lint output; numbers the records contradict; next step.
