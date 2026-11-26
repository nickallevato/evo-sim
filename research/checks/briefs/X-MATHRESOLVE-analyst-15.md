# X-MATHRESOLVE-analyst-15: P3 compute manifest (the seven open simulation objects)

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE, `next` ("Next: P3"); `docs/research/math/REMAINING.md` phase P3; `docs/research/math/README.md` (pipeline ends in "compute manifest"). The parameters pass is done (EVOA-93, 272868a).

## Gap item
X-MATHRESOLVE, P3 part 1 of n: the manifest only. No check is designed, pre-registered or run here; each manifest row becomes its own later `design-check` task. No verdict, status or claim-tree field moves.

The seven open `resolution: simulation` objects (`math_map.py` lists them): M-301, M-405, M-413, M-501, M-505, M-506, M-604. Load-bearing (in `exit_gap.py`/`lint_research.py` load-bearing list via `used_by`): M-505 (E6, E7, E9, A5b), M-604 (F2). There are no open `regression` objects. The 22 open `data-check` objects are NOT in this task.

## Deliverable
One new file, `docs/research/math/compute-manifest.md`, one section per object, in run order (load-bearing first, then by the number of nodes that rest on it). Each section, at most ~15 lines:
- object id, statement (one line), `used_by`, load-bearing yes/no;
- the model to simulate, in one paragraph, and the `parameters.yaml` keys it reads (name missing keys; don't add them);
- Day-side and critic-side positions from `objects.yaml`, and for each the simulated outcome that would bear it out (both must be reachable; ST-05, MA-24);
- the decisive output (the number that settles the object) and which node field it could move;
- whether a held published simulation or an existing check (`research/checks/results/R4-*.md`, `records/M-*`) already settles it; if so, say "no compute: cite <file>" and stop that section;
- cost: the `compute:` estimate in `objects.yaml`, marked unmeasured, and the smoke test that would measure it (grid size, one line);
- whether it can run inside the workstation limits (one process, <500 MB, <1 min) or needs na-workhorse.

End with a table: id, load-bearing, compute needed (yes / no: cite), est. CPU-h (unmeasured), host, order.

## Allowed paths
- `docs/research/math/compute-manifest.md` (new)

Read anything. Don't edit `objects.yaml` (estimates stay as they are; a wrong one goes in the report), records, parameters.yaml, claim files, results, gap-blockers.yaml, ledgers, QUEUE/REVIEW/RESULTS, argmap, the board, `REMAINING.md`.

## Skill
`design-check`, its rules on reachable outcomes and measured cost only; no script is written. No host, no fetch (O-7), no computation beyond grep and reading.

## Budget
1 commit (2 at most). Fix passes left: 2 of 2. Lead review: `git show --stat` is the manifest only, `math_map.py --lint` and `research/checks/lint_research.py` 0 errors, seeded spot check of 3 sections against `objects.yaml` and the cited files. No other review (D-40).

## Stop when
- the manifest is committed and pushed; OR
- an object's model can't be stated from held text: write "blocked: <what is missing>" in its section and go on; OR
- the work would touch a path outside the list.

## Not in scope
Check scripts, smoke runs, host use; the 22 data-check objects; editing estimates in `objects.yaml`; the "Ideas (not queued)" lines; tooling; people.yaml.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; the final table; objects settled without compute (with citation); wrong `objects.yaml` estimates; missing parameters keys; anything blocked.
