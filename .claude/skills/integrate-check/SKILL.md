---
name: integrate-check
description: Integrate one reviewed, fix-passed evo-sim check into the shared files (step 6 of the lifecycle). One agent at a time; run as the operator agent.
---
# Integrate a check (one agent at a time on shared files)

Spec: the write-up's final "Review resolution" section and its proposed verdict comments. Apply exactly that. Copy the form of the latest integration (grep the previous check's id in each target file).

0. **Quotes first.** Passages the write-up lists "for integration to file" go into `docs/research/sources/quotes-*.md` with the next Q ids, verbatim from the held raw text under `sources/raw/` (gitignored), with locator and date. Not found exactly: do not add; cite nothing that depends on it; report.
1. `research/checks/REVIEW.md`: one entry per review (next `#NN`).
2. `research/checks/RESULTS.md`: one paragraph, both sides.
3. `research/checks/QUEUE.md`: DONE with date, plus what stays open. `docs/research/ROADMAP.md`: the matching A row to `done`.
4. Claim files: verdict comments and an "R4 <ID>" paragraph crediting both sides. Reading-dependent verdicts get the `reading-dependent:` comment and a Readings table; the field takes the reading under which the quoted statement is most defensible. Superseded sentences are marked, not deleted. Corrected audit figures keep their text and gain a dated correction, logged in `ledgers/slips.md`.
5. Argmap (`docs/research/argmap/`): `chk:<ID>` and review ids in `NOTES.md`; defeaters in `defeaters.yaml` (next `dNNN`, both sides where warranted, none the write-up does not license); lineage node; mini-form in `standard-forms.md` if a claim was created.
6. `research/.venv/bin/python -I research/checks/lint_research.py --write-hierarchy`; `research/tools/argmap_check.py`; `research/tools/argmap_render.py`; refresh counts in `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`; `research/tools/readme_figs.py`, then `git checkout` SVGs whose only change is random ids. Lint and argmap_check must end at 0 errors, 0 warnings.
7. Regenerate `research/checks/PREREG-STATUS.md` (`research/tools/prereg_status.py`) if a new script ran.
8. Commit with explicit paths; `git pull --rebase origin research`; `git push origin research`.

Report every verdict field whose value or governing reading changed. Do not write a milestone post, patch the board, or edit `DECISIONS.md` or `criticality/`.

Known stale spots to fix when you pass them: `readme_figs.py` hardcodes the 2026-10-09 tallies (`verdicts.svg`); the reading-dependent total differs between `docs/HANDOFF.md` and `docs/arguments/README.md`.

## Conduct
You are the only agent on the shared files while you run.

Apply exactly what the fix-passed write-up proposes and nothing more. File quotes first, verbatim from the held raw text; if a passage is not found exactly, do not add it and cite nothing that depends on it. Never change a verdict value the write-up does not propose; list every field whose value or governing reading changed in your report. Finish with lint and argmap_check at 0 errors and 0 warnings. No milestone post, board patch, criticality or DECISIONS edits.
