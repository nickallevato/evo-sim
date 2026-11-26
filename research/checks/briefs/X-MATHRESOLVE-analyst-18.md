# X-MATHRESOLVE-analyst-18: map-fix part 2 (simulation statuses, stale fields, data-check findings)

**Role:** analyst (Opus). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE, `next` (data-check part 2 done: EVOA-96, ba8b38d, lead-approved; lead call on M-301/505/506/604 under the P3 manifest entry); `docs/research/math/compute-manifest.md` (db4e99d); `docs/research/math/README.md` (schema, "Records").

## Gap item
X-MATHRESOLVE, map-fix part 2. The 5 open `simulation` objects move to `blocked`. Stale fields and the findings of data-check parts 1 and 2 are written into `objects.yaml`. No claim verdict moves, and no record is written or edited.

## Deliverable
One commit that edits `objects.yaml` (and a source map row only where an item below names one):
1. **M-301, M-506, M-604:** `status: blocked`, `blocked_on: "after: X-VARLIST (R5 sensitivity table); not run, because no open field on a load-bearing node moves (compute-manifest.md §<n>)"`. For M-604, add that F2 is already set (`contested`). Take the § numbers from the manifest.
2. **M-505:** `status: blocked`. Reuse M-710's `blocked_on` wording for the M-503/E6 inputs (no second request). Add the X-VARLIST residual as in item 1.
3. **M-405:** `resolution: data-check`, `status: blocked`, `blocked_on: "outside: ..."` using the manifest's §4 and row wording (no held landscape at Eden's scale; the viability leg is in R4-D1-spike.md). Remove its `compute` field only if `math_map.py --lint` requires it.
4. **Stale fields** (manifest §3, §6 and l.96-100; gap row): M-301 `compute.est_cpu_h` 0 to 12 (the script's estimate, `measured: false`); M-413 `compute` as the manifest says; M-505 critic: "planned, not run" becomes ran in R4-F2-A (cite its number); M-501 critic: "consequence ... open" becomes what R4-E's threshold sweep settles. Use only the R4 text, and quote its section.
5. **M-008 statement or positions** (part 1's findings): Q12 labels 40e6 "single-nucleotide variants", but the 20e6 needs CSAC's 35e6 SNV + 5e6 indel. The paper's "2,407 achievable" implies G_f 104.7, not 105. A3b's "83% of events" is 72% on T2T (GAP-07t). Also fix the matching `branch-A.md` row if it repeats the error.
6. **M-905 statement** (part 2's findings): CSAC removed 2,591 of 16,045 genes, so the 6,946 is Day's-set arithmetic and not CSAC's exclusion. Day's 71.6% at N/S 3.34 gives 0.755, not 0.71. Take both numbers from `records/M-905.json`, not from memory. Fix the `branch-ROOT.md` DN1 q4 row only if it states either one wrongly.

Records quote `objects.yaml` and the source maps verbatim. Before committing, run every record (`for f in docs/research/math/records/M-*.py; do research/.venv/bin/python -I "$f" || echo FAIL $f; done`) and `math_map.py --lint`, as separate commands. If a fix breaks a record, undo that fix and list it in the report. Don't edit the record.

## Allowed paths
- `docs/research/math/objects.yaml`: only M-008, M-301, M-405, M-413, M-501, M-505, M-506, M-604 and M-905 (statement, positions, resolution, status, blocked_on, compute)
- `docs/research/math/sources/branch-A.md` and `branch-ROOT.md`: only the rows that items 5 and 6 name

You can read any file. Don't edit records, claim files, `parameters.yaml`, `compute-manifest.md`, `gap-blockers.yaml`, ledgers, QUEUE/REVIEW/RESULTS, argmap or the board.

## Skill
`deref-source` (merge-step rules: one wrap per quote). No host, no fetch (O-7). Grep big files by id; don't read them whole.

## Budget
At most 1 commit. Fix passes left: 2 of 2. Lead review: both linters at 0 errors, all records pass, `git show --stat` inside the list, and a seeded spot check of 3 items. No other review (D-40).

## Stop when
- all 6 items are done or listed as skipped (with the reason), committed and pushed; OR
- a fix needs a path outside the list, a fetch, or a judgment that the R4 text, the manifest or the record does not settle (list it; don't guess).

## Not in scope
Claim files that carry the same wrong numbers (DN3's 6,946, A3b's 83%, Q12's label): list them with file:line for a later claim-file pass. Also out of scope: the rhetoric objects M-221 and M-908, the open M-117 assumption (Matthews' "slideshow"), tooling and new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Use explicit paths, never `git add -A`. Run `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; items done / 6; skipped items with the reason; records run (pass count); lint output; claim-file lines for the later pass; next step.
