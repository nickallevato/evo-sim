# A2e-operator-1: host provenance of L3's hand-patched `sites.vcf.gz` (correctness MINOR-1)

**Role:** operator. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e; correctness review of L3 (`REVIEW-R4-L3-correctness.md`, 8432a1c, MINOR-1); `R4-L3.md` section 9 item 1 and section 10 item 2 (fix pass 1, e5e1a7d).

## Gap item
A2e. No field moves in this task: the run stands (MINOR-1 ruling). This closes the provenance gap before L3 is integrated.

## Deliverable
An appended section `--- provenance (A2e-operator-1, 2026-11-01) ---` at the end of `research/checks/results/raw/l3_amk.host`, recording from what is on `na-workhorse` under `~/projects/evo-sim/sources/raw/l3-data-2026-10-19/` (and any sibling fetch directory the earlier records name):
1. A directory listing (`ls -la`, including `parts/`) of the fetch directory or directories.
2. `sha256sum` of every copy of `sites.vcf.gz` present: the patched file in use (must equal 381d2ece…7b7f2), the 10-18 copy and the 10-19 copy if they still exist, and `sites_bad_3windows.vcf.gz.discard`. Say plainly which are missing.
3. `sha256sum` of each `parts/curl*.err`, plus their contents verbatim if together under 60 lines; otherwise their `tail -n 5` each.
4. The four bad-window offsets (three in the 10-19 copy, one in the 10-18 copy) and the 500 B patch window, from those files or by `cmp -l` between the copies if both exist (count of differing bytes and first/last offset per window, no more). If the offsets cannot be recovered, say so.
5. What "server refetch x3 identical" compared, if the evidence shows it; otherwise "not recorded".
6. One line each: the two fetches share one directory (yes/no, as found); no provider checksum is held (do not fetch one).

## Allowed paths
- `research/checks/results/raw/l3_amk.host` (append only; do not change existing lines)

Read anything you need; write nothing else in git. On the host, read and hash only: no deletes, moves, re-patches or fetches.

## Skill
`run-on-host` (its ssh pitfalls and "never commit or push from a host"). Hashing is the only computation; one at a time, check `uptime` first.

## Budget
At most 1 commit. No fix passes apply.

## Stop when
- the section is committed and pushed to `research`; OR
- the host is unreachable or the fetch directory is gone (report it; do not reconstruct from memory); OR
- the patched file's sha256 does not equal 381d2ece…7b7f2 (report both values; stop, don't choose); OR
- the work would need a fetch or a path outside the list.

## Not in scope
Integration of L3, the AA README quote (needs a fetch), editing `R4-L3.md` or `gap-blockers.yaml`, rerunning L3, cleaning up the host. Ideas: one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit path; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; a table of items 1-6 → recorded / missing; any hash mismatch with both values; next step (integrate L3).
