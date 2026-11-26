# X-MATHRESOLVE-analyst-8: records for branch H's open derivation objects

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE (branch G done: EVOA-84, 83dc821, lead-approved); `docs/research/math/README.md` ("Object schema", "Records", owner D-38); `docs/research/math/REMAINING.md` P2.

## Gap item
X-MATHRESOLVE, branch H batch: the 8 open `derivation` objects with ids M-8xx in `docs/research/math/objects.yaml`: M-801, M-802, M-803, M-804, M-805, M-806, M-807, M-808. Source map: `docs/research/math/sources/branch-H.md`. Model to follow: the branch D to G records `docs/research/math/records/M-401.py` .. `M-713.py` (same `held()`, `near()`, `finish()` shape; a stale JSON fails the script). Each one moves `status: open` to `resolved` (with a record) or to `blocked` (with `blocked_on`). No claim verdict moves.

## Deliverable
For each of the 8 objects, one of:
- **resolved:** `docs/research/math/records/M-NNN.py` plus `M-NNN.json`, per math/README "Records". The script is self-contained (stdlib), states every input with its `parameters.yaml` key or quote id (Q id or claim file plus quote number), checks each quote verbatim with `held()`, and has an `assert` for every number the object's statement claims, including printed figures the statement says are wrong (assert the corrected value and the size of the gap).
  In `objects.yaml` set `status: resolved` and `resolved_by: docs/research/math/records/M-NNN.json`.
- **blocked:** an input can't be read from held material (`docs/research/**`, `research/checks/**`, `sources/raw/`, read only, no fetch, O-7). Set `status: blocked` and `blocked_on: "owner: <exact text or file needed>"` (or `outside:`). Don't estimate around it.

Notes per object (closed forms, stdlib):
- M-801: 30/0.10 = 300 and the 30 N cost; the statement says the 300 is verified only as Nunney 2003 reports it (Haldane 1957 not retrieved). Quote Nunney's report; don't treat Haldane as held.
- M-802: 146,250, 487 (487.5 truncated), 41,068-fold, 1,083; assert the truncation and the d step as stated.
- M-803 (model-choice): no numeric fit. Assert Nunney's M = 2Ku threshold structure (C below Haldane's for M > 1/2, rising below) only as far as held text gives a formula; otherwise quote the sentences each reading rests on and record both positions, as M-706/M-713 did.
- M-804: W = e^(-U) at U = 2.2 and 0.35, 20 x (1 - W) = 17.8; the U inputs from held quotes (Keightley 2012 as the claim files cite it).
- M-805: the three Hössjer factors (127, 15,800, 10 million) and the gap the statement names (cost step not computed).
- M-806: 2 x 321,444 = 642,888, / 146,250 = 4.3958, x 2e7 = 87,916,307x; Dawkins figures are secondhand, say so.
- M-807: 1/300 = 0.0033; the 300-bit equivalence; the 300x factor at one bit per substitution.
- M-808: K_sel = s_max d / [2 ln(2Ne)], per site / L: 8.25e-12 (paper 8.3e-12), 0.0256 per generation (one per 39), the total over 260,000 generations, and the Ne = 1e4 value. The map-fix list carries "about 6,650 in H1/H8 vs about 6,690 in H5 l.39": assert the closed-form total and list which printed figure it matches in the report; don't edit claim files.
Grep the quotes files and claim files (H and its children) by id. Don't read big files whole (AGENTS.md token budget). Anything over a minute of CPU or 500 MB: stop and report.

## Allowed paths
- `docs/research/math/records/M-NNN.py` and `M-NNN.json` for NNN in 801..808
- `docs/research/math/objects.yaml`: only `status`, `resolved_by`, `blocked_on` on those 8 objects. Leave statements, `used_by` and `positions` as they are.

Don't edit claim files, `parameters.yaml`, source maps, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS or the board. If a claim file, `parameters.yaml` or an object statement has a wrong number, list it in the report.

## Skill
`design-check`, adapted: no host run and no pre-registration commit. Its rules on asserting every input and label apply. Records run locally in seconds: `research/.venv/bin/python -I docs/research/math/records/M-NNN.py`.

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `research/tools/math_map.py --lint` at 0 errors, all records run and pass, each JSON sha256 matches its script, and a spot check of a seeded sample against the claim files. No other review (D-40).

## Stop when
- all 8 are resolved or blocked, committed and pushed; OR
- a record needs more than a minute of CPU, a fetch, or a path outside the list (report it).

## Not in scope
Other branches' objects and records, the M-1xx pilot objects, ROOT/FM objects (M-9xx), simulation/regression/data-check objects, the X-MATHMAP map-fix flags carried in the row, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; a table of id, status, key asserted values (or `blocked_on`); lint output; any number in a claim file, `parameters.yaml` or an object statement the records contradict; next step.
