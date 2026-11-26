# F1a-analyst-2: design and pre-register one check on F1a external (no run, no field move)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row F1a; claim file `docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md` ("Pre-registered prediction", "Result that would change a verdict"); `results/R4-F1a.md` with fix pass 4971d70 (an engine consistency check, not independent evidence); D-40 (one combined review follows the write-up, not this design).

## Gap item
F1a, field `verdicts.external` (`pending`). The claim to test, as quoted in the claim file: the LTEE 1,322 gen/fix is a total throughput measurement, and the human 19,800 "generations per fixation" (a latency, F3) used as a divisor shows humans are slower than E. coli. **No field moves in this task.** Internal (`non-sequitur`) and fidelity (`n/a`) do not move.

## Deliverable
One pre-registration, committed before any computation or scoring:
- if the test needs computation: a script `research/checks/f1a_external.py` per the `design-check` skill (docstring with quotes and Q ids, Day-side, critic-side and audit predictions, exhaustive bands, the external verdict each band licenses, launch and collect commands; smoke test on na-workhorse only if the run is not trivial);
- if it needs none (the deciding evidence is already held: Good 2017 quote, R4-F2-A, R4-GAPS-04-07-02, R4-F1b): a criterion-only file `research/checks/results/R4-F1a-external-criterion.md` in the form of `0fd4581` (A2e-fidelity criterion), fixing which held result puts F1a external in which band, before anyone reads them for scoring.

**Reuse gate first.** Write one paragraph on what existing checks already settle for this field (F2 and GAP-04 bound interference at human R; R4-F1a's count is fixed by supply; F1b measures overlap). Do not recompute settled maths. If a new run would only repeat them, use the criterion-only form. If no test from held material could put F1a external in more than one band, **stop**: commit a 10-line note `research/checks/results/R4-F1a-external-feasibility.md` naming the missing input, and report it.

Each registered band must be reachable by a stated result (ST-05, MA-24); a band reached by construction (as in R4-F1a) does not count. Both sides must be able to lose: a band where human-scale spacing is near 19,800 (e.g. interference pushes effective width near 1: Day side) and one where it is well below (critic side), plus any `untestable` region.

## Allowed paths
- `research/checks/f1a_external.py` (new) OR `research/checks/results/R4-F1a-external-criterion.md` (new) OR `research/checks/results/R4-F1a-external-feasibility.md` (new)
- `research/checks/results/raw/f1a_external*` (smoke output only, if a script is used)

Read anything; grep big files by id. Do not edit claim files, `R4-F1a.md`, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, `gap-blockers.yaml`, ledgers, argmap, `DECISIONS.md` or the board.

## Skill
`design-check`. Compute only on na-workhorse (AGENTS.md "How to run"); never commit from the host.

## Budget
At most 3 commits. No main run in this task. No fetches (corpus frozen, O-7; a missing input is a stop). Fix passes left: 2 of 2.

## Stop when
- the pre-registration is committed and pushed to `research`; OR
- the reuse/feasibility gate fails (feasibility note committed; row goes to `outside`/`owner`); OR
- the work needs a fetch, a new quote, a path outside the list, or a rule change.

## Not in scope
F1a internal and fidelity; F1, F1b, F2 fields; rewording "All predictions met" (ROADMAP B36); the misplaced #24 sentence in the claim file (next integration); running the check; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: F1a`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; the reuse/feasibility paragraph in short form; form chosen (script or criterion); the bands and the verdict each licenses; which result would put each side in its band; cost from the smoke (if any); next step.
