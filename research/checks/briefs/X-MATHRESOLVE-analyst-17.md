# X-MATHRESOLVE-analyst-17: the other 15 data-check objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE, Next (2); part 1 done: EVOA-95 (94f7c9a), lead-approved; `docs/research/math/README.md` ("Records"; l.48: a full R4 check stays the record, and its object points at the R4 file).

## Gap item
X-MATHRESOLVE, data-check part 2: the 15 `data-check` objects still `open` in `docs/research/math/objects.yaml`: M-004, M-009, M-010, M-011, M-117, M-307, M-308, M-403, M-404, M-408, M-504, M-710, M-905, M-906, M-911. Each moves from `status: open` to `resolved` or `blocked`. No claim verdict moves.

## Deliverable
For each of the 15 objects, do as in part 1 (`X-MATHRESOLVE-analyst-16.md`, "Deliverable"):
- **resolved by an R4 file:** an existing `research/checks/results/R4-*.md` already measures the statement on held data. Set `status: resolved` and `resolved_by: research/checks/results/R4-<ID>.md`. In the report, give the section and the settling number. Check each one; don't assume.
- **resolved by a record:** held data covers it (`sources/raw/`, `research/checks/**`, read only). Write `docs/research/math/records/M-NNN.py` plus `.json` in the shape of `records/M-008.py` (`held()`, `near()`, `finish()`, stdlib, under a minute, under 500 MB). Assert every number in the statement, including printed figures that are wrong.
- **blocked:** a needed input is not held (no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact file or text>"` (or `outside:`). Where an existing blocker already names the input (E6, M-122, M-124, M-206, M-503), reuse its wording. Don't open a second request.
Mixed legs: resolve an object only if its open leg is a verdict question and not a number. Otherwise block it and name the leg.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json`, for NNN in 004, 009, 010, 011, 117, 307, 308, 403, 404, 408, 504, 710, 905, 906, 911
- `docs/research/math/objects.yaml`: only `status`, `resolved_by` and `blocked_on`, on those 15 objects

Don't edit claim files, `parameters.yaml`, R4 results, source maps, `compute-manifest.md`, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. List any wrong numbers you find there in the report.

## Skill
`design-check`, adapted as in analyst-12 and analyst-16: no host and no pre-registration commit. Its rules on asserting every input and label apply. Grep big files by id; don't read them whole.

## Budget
At most 3 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` and `research/checks/lint_research.py` at 0 errors; every new record runs and passes with a matching sha256; `git show --stat` stays inside the list; a seeded spot check of 3 objects. No other review (D-40).

## Stop when
- all 15 are resolved or blocked, committed and pushed; OR
- a record needs over a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
- Part 1's findings: Q12's "single-nucleotide" label on 40e6, the paper's G_f 104.7, and A3b's 83% vs 72% on T2T. Those wait for the map-fix part.
- The simulation objects M-301, M-405, M-505, M-506 and M-604, and the stale `compute`/`positions` fields (M-301, M-413, M-501, M-505). Also the map-fix part.
- The rhetoric objects M-221 and M-908; tooling; new rules.
Ideas: one line each in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Use explicit paths, never `git add -A`. Run `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, and `resolved_by` with the settling number (or `blocked_on`); lint output; numbers the records contradict; next step.
