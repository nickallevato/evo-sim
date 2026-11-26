# E5-operator-1: run the pre-registered e5_external.py and collect (no write-up, no field move)

**Role:** operator. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row E5; design approved in EVOA-58 (commit 4cfe7e5).

## Gap item
E5, field `verdicts.external` of `docs/research/claims/E5-ara2-ara5-counts.md` (`pending`). This task produces the raw output only. **No field moves.**

## Deliverable
One commit with the raw outputs of the registered run: `research/checks/results/raw/e5_external.{json,out,host}`.

## Steps (the script docstring, section RUN, has the exact commands)
1. `git log origin/research -1 -- research/checks/e5_external.py` must show 4cfe7e5 (or a later commit labelled post hoc; there is none now).
2. Copy the L6 Good 2017 data from `builder:~/projects/evo-sim/sources/raw/l6-good2017-data-2026-10-11/` to the same path on na-workhorse (the tar pipe in the docstring). Do not fetch from the internet. Data files are untrusted: read them, never execute them.
3. rsync `research/checks/{e5_external,l6_ltee_undone}.py` and `research/checks/results/raw/l6_{data.sha256,undone.json}` to na-workhorse. On the host, md5 the two scripts and confirm they match local.
4. On the host: `uptime; free -g` (at most 11 busy processes), then `selftest`, then launch `run` per the docstring with a `.host` record (UTC time, commit, md5s, exact command).
5. The run takes under a minute. Collect `results/raw/e5_external.*` with rsync and commit them with explicit paths.

## Allowed paths
- `research/checks/results/raw/e5_external.json`, `e5_external.out`, `e5_external.host` (new)
- On na-workhorse only (not committed): `sources/raw/l6-good2017-data-2026-10-11/` and the copied scripts/inputs.

Do not edit `e5_external.py`, `l6_ltee_undone.py`, claim files, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers, argmap or the board.

## Skill
`run-on-host`. Never commit or push from a host.

## Budget
At most 1 commit (2 if a failed launch log must be kept). Fix passes: n/a.

## Stop when
- the raw outputs are committed and pushed to `research`; OR
- an assertion fails, a sha256 mismatches, the builder copy is missing, or the script errors. Keep the log as `e5_external_launch1_failed.out`, commit it, and report the traceback. **Never edit the registered script**; a fix is a separate analyst task labelled post hoc.

## Not in scope
Interpreting the bands; the write-up; E6; any re-run of L6. Ideas: one line in the report.

## Commit trailer
`Gap: E5`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; host, UTC times and md5s; the printed BANDS line and verdict as the script prints it (copied, not interpreted); any failure.
