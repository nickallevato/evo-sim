# E6-analyst-1: design and pre-register one check on E6 external (no run, no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row E6; `research/checks/results/R4-E5E6.md` l.28-29 (what R4-E5E6 settles and does not settle); D-40 (one combined review follows the write-up, not this design).

## Gap item
E6, field `verdicts.external` of `docs/research/claims/E6-strict-vs-95-counts.md` (`pending`). The claim to test: Z23105291's strict lineage-aware count (5,496 whole-population fixations; Q56, Q57) against the naive first-crossing count (8,679), and whether the strict state calls hold up on the Good 2017 data. **No field moves in this task.** Fidelity (`unverifiable`) and internal do not move.

## Deliverable
One pre-registration, committed before any computation or scoring:
- if the test needs computation: a script `research/checks/e6_external.py` per the `design-check` skill (docstring with quotes and ids, Day-side, critic-side and audit predictions, exhaustive bands, the external verdict each band licenses, launch and collect commands; smoke test on na-workhorse only if the run is not trivial);
- if it needs none: a criterion-only file `research/checks/results/R4-E6-external-criterion.md` in the form of `0fd4581` (A2e-fidelity criterion).

**Feasibility gate first.** The Good 2017 files are held (`builder:sources/raw/l6-good2017-data-2026-10-11/`, sha256 in `results/raw/l6_data.sha256`, found by EVOA-58; read only, check the hashes). Write one paragraph in the pre-registration on what they allow: can the strict definition in Z23105291 be applied to them as written, or does it need a choice the text does not fix? If no test that could put E6 external in more than one band is possible from held material, **stop**: commit only a 10-line note `research/checks/results/R4-E6-external-feasibility.md` that names the missing input, and report it.

Each registered band must be reachable by a stated result (ST-05, MA-24). Both sides must be able to lose: a band where the strict count is reproduced from the held data (Day side) and one where it is not, or depends on an unstated choice (critic side).

## Allowed paths
- `research/checks/e6_external.py` (new) OR `research/checks/results/R4-E6-external-criterion.md` (new) OR `research/checks/results/R4-E6-external-feasibility.md` (new)
- `research/checks/results/raw/e6_external*` (smoke output only, if a script is used)

Read anything; grep big files by id. Do not edit claim files, `R4-E5E6.md`, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `gap-blockers.yaml`, ledgers, argmap, `DECISIONS.md` or the board.

## Skill
`design-check`. Compute only on na-workhorse (AGENTS.md "How to run"); never commit from the host.

## Budget
At most 3 commits. No main run in this task. No fetches (the corpus is frozen; a missing input is a stop). Fix passes left: 2 of 2.

## Stop when
- the pre-registration is committed and pushed to `research`; OR
- the feasibility gate fails (feasibility note committed, row goes to `outside`/`owner`); OR
- the work needs a fetch, a new quote, a path outside the list, or a rule change.

## Not in scope
E6 internal and fidelity; E5 (closed); E7 and A2; re-scoring R4-E5E6; running the check; the close-batch for E5; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: E6`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; the feasibility paragraph in short form; the bands and the verdict each licenses; which result would put each side in its band; cost from the smoke (if any); next step (run, or row to `outside`/`owner` with the missing input named).
