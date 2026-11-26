# E5-analyst-1: design and pre-register one check on E5 external (no run, no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row E5; `research/checks/results/R4-E5E6.md` l.28-29 (what R4-E5E6 settles and does not settle); D-40 (one combined review follows the write-up, not this design).

## Gap item
E5, field `verdicts.external` of `docs/research/claims/E5-ara2-ara5-counts.md` (`pending`). The claim to test: the -906 (Ara-2) and 0 (Ara+5 at 60K) cells of MITTENS 3.0 (Z23003785 §4.1, §5.1-5.2) are estimator artefacts, not biology. **No field moves in this task.**

## Deliverable
One pre-registration, committed before any computation or scoring:
- if the test needs computation: a script `research/checks/e5_external.py` per the `design-check` skill (docstring with quotes and ids, Day-side, critic-side and audit predictions, exhaustive bands, the external verdict each band licenses, launch and collect commands; smoke test on na-workhorse only if the run is not trivial);
- if it needs none (a reading of held texts against a fixed criterion): a criterion-only file `research/checks/results/R4-E5-external-criterion.md` in the form of `0fd4581` (A2e-fidelity criterion).

**Feasibility gate first.** R4-E5E6 says the clone-pair correction formula is not in the extracted text. Grep the held texts (Z23003785, Z23105291, Good 2017; `sources/raw/`, read only) for the formula or enough inputs to rebuild it (the 4.2% sharing rate, clone counts, the snapshot rule). Write one paragraph in the pre-registration on what the held material allows. If no test that could put E5 external in more than one band is possible from held material, **stop**: commit nothing but a 10-line note `research/checks/results/R4-E5-external-feasibility.md` that names the missing input (Day's formula or code, or a fetch) and report it.

Each registered band must be reachable by a stated result (ST-05, MA-24). Both sides must be able to lose: a band where the -906 is reproduced from a stated biological reading (Day side) and one where it follows from the estimator alone (critic side).

## Allowed paths
- `research/checks/e5_external.py` (new) OR `research/checks/results/R4-E5-external-criterion.md` (new) OR `research/checks/results/R4-E5-external-feasibility.md` (new)
- `research/checks/results/raw/e5_external*` (smoke output only, if a script is used)

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
E5 internal and fidelity; E6 (its own row); E7 and A2; re-scoring R4-E5E6; running the check; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: E5`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; the feasibility paragraph in short form; the bands and the verdict each licenses; which result would put each side in its band; cost from the smoke (if any); next step (run, or row to `outside`/`owner` with the missing input named).
