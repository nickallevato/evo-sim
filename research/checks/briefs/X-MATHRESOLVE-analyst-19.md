# X-MATHRESOLVE-analyst-19: claim-file pass part 2 (M-008 and M-905 findings)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE, `next` step (1); map-fix part 2 done (EVOA-97, 1442eef, lead-approved); `docs/research/math/README.md` ("Records").

## Gap item
X-MATHRESOLVE, claim-file part 2. It carries the M-008 and M-905 findings, now in `objects.yaml` (1442eef), into the claim files that print the same numbers. No verdict value, status field or claim-tree edge moves.

## Deliverable
One commit. Each correction gets a dated `<!-- X-MATHRESOLVE 2026-11-26: was ..., M-NNN record -->` comment, or, inside a YAML verdict comment, an appended `X-MATHRESOLVE 2026-11-26 (M-NNN record): ...` clause. Leave the verdict value as it is.
1. `claims/A3b-snv-only-concession.md` l.14 (external comment): "17.5M is 83% of measured events per lineage (21.05M, hg38 vs panTro6)". Add that it is 72% on the T2T count (24.14 M, GAP-07t). Cite M-008. Take the 24.14 M and the 72% from the M-008 record or R4 GAP-07t, not from memory.
2. `claims/DN3-consortium-gene-set-artefact.md` l.12 (internal comment, "6,946 = 34%") and l.13 (fidelity comment): say that 20,400 − 13,454 = 6,946 is Day's set against CSAC's, and is not CSAC's exclusion: CSAC's curation removed 2,591 of its own 16,045 genes (16.2%). Cite M-905. If l.13 already says this in substance, add only the 2,591 and 16.2% figures.
3. `claims/DN1-dnds-080-on-20400-genes.md`, near l.26-33 (Day's 71.6% / 28.4% / 0.71): add one line. At the correct site ratio N/S 3.34, Day's 71.6% gives (71.6/28.4)/3.34 = 0.755, not 0.71; the implied N/S is 3.55. Cite M-905. Put it in the derivation or the R4 text, not in a verdict field.
4. `claims/A3-required-fixations-2019-2025.md` l.13: check only. It already flags the 40M "single-nucleotide variants" label (Q12). Add the M-008 citation only if no record is cited there. List the result.

Before committing, run every record (`for f in docs/research/math/records/M-*.py; do research/.venv/bin/python -I "$f" || echo FAIL $f; done`), then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass. If a record quotes a line you changed and fails, undo that change and list it. Don't edit the record.

## Allowed paths
- `docs/research/claims/A3b-snv-only-concession.md`, `DN3-consortium-gene-set-artefact.md`, `DN1-dnds-080-on-20400-genes.md`, `A3-required-fixations-2019-2025.md` (text and comments only; no verdict value, status or edge fields)

Read anything. Don't edit objects.yaml, records, source maps, results files, parameters.yaml, hierarchy*, gap-blockers.yaml, ledgers, QUEUE/REVIEW/RESULTS, argmap or the board.

## Skill
`fix-pass` (correction comments, no verdict moves). No host, no fetch (O-7). Grep big files by id; don't read them whole.

## Budget
At most 1 commit. Fix passes left: 2 of 2. Lead review: both lints at 0 errors, all records pass, `git show --stat` inside the list, and a seeded spot check of 2 corrections. No other review (D-40).

## Stop when
- all 4 items are done or listed as "no change" or skipped (with the reason), committed and pushed; OR
- a correction would move a verdict value, or needs a judgment that the M-008 or M-905 record does not settle. List it; don't guess.

## Not in scope
Other claim files with the same numbers (list them with file:line). Also out of scope: the rhetoric objects M-221 and M-908 (next task), the open M-117 assumption, C2d's 'holds', tooling and new rules. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Use explicit paths, never `git add -A`. Run `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; items done / 4, with file:line; no-change or skipped items with the reason; records run (pass count); lint output; other claim-file lines with the same numbers; next step.
