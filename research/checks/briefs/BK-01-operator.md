# Brief BK-01 (operator): bookkeeping pass and board patch `upd22`

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/republish-board/SKILL.md`, with the bookkeeping part of
`.claude/skills/integrate-check/SKILL.md` for the count refresh.

## Goal

Make the public numbers agree with the files of record. No verdict value moves in this task.
If anything you find would move a verdict, stop and report it; it is not yours to apply.

## What the lead has already seen

Three specific disagreements, found on 2026-10-13 at commit `9806966`. Treat them as a
starting list, not the scope — recount from the files of record and patch whatever else
disagrees.

1. **`research/tools/readme_figs.py` line 130**: the verdict tallies behind `verdicts.svg`
   are hardcoded from a `lint_research.py` run on 2026-10-09 at 217 claims. There are now
   234 files in `docs/research/claims/`. The figure is therefore stale.
2. **The reading-dependent total disagrees between two public files**:
   `docs/HANDOFF.md` (lines 91 and 62 area) says 7 claims and *10* reading-dependent
   verdicts counting the 3 RH tags; `docs/arguments/README.md` line 105 says *9* with the
   3 RH tags. One of them is wrong. Settle it from the claim files themselves, not from
   either prose summary, and make both read the same.
3. **Board patch `upd22.py`**: `upd21.py` carried the 2026-10-13 batch (HF `ph`, L1b, L1c,
   FMnull, L5) and criticality pass vii, but its header does not mention **Q93close** or
   **B2f**, which were integrated the same day (defeaters d470-d475). Check whether the
   board reflects them; `upd21` set `233 claim files` and there are now 234. Write
   `research/tools/board/upd22.py` in the style of `upd21.py` — every step asserts its
   anchor so it cannot apply twice, and it starts with `assert 'upd22' not in s` — for
   whatever is genuinely out of date, then republish the status Artifact to the same file
   and the same URL.

## Files you may write

- `research/tools/readme_figs.py` (the hardcoded tally block only)
- the regenerated figures under the paths `readme_figs.py` writes
- `research/tools/board/upd22.py` and `docs/research/status.html`
- `docs/HANDOFF.md` and `docs/arguments/README.md`, counts and the reading-dependent
  sentence only
- `README.md` counts, if they are stale too

Nothing else. Do not touch claim files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers,
quotes files, the argmap data or any registered check script.

## Constraints

- `AGENTS.md` hard rules and token budget apply. Grep by id or heading; never read
  `HANDOFF.md`, the quotes files or `REVIEW.md` whole.
- Counts come from the files of record, recomputed, never from a prose summary:
  `research/tools/lint_research.py --write-hierarchy` (verdicts, claims),
  `research/tools/argmap_check.py` (defeaters, lineage), `PREREG-STATUS.md`,
  `ROADMAP.md`.
- No computation on this workstation beyond the linters and renderers themselves (one
  process, under 500 MB, under a minute). `na-workhorse` is busy with run `ph2` until
  2026-10-16 — do not launch anything there.
- After `readme_figs.py`, `git checkout` any SVG whose only change is a random id.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push. Push `origin research` only; do
  **not** push `research:master` in this task.
- You are the only agent on the shared files while this runs.

## Report format (at most 300 words)

Commits; a table of each number you changed, with its old value, new value and the file of
record you took it from; failures; next step.
