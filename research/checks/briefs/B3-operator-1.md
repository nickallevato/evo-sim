# B3-operator-1: integrate R4-B3-internal (no field move; comment and Readings table only)

**Role:** operator. **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row B3; write-up `research/checks/results/R4-B3-internal.md` (26dabc8, fix pass 1 4360f38, lead-approved EVOA-56); combined review `REVIEW-R4-B3-internal-combined.md` (38e19ef, EVOA-55); lead ruling in `briefs/B3-analyst-2.md` (177c68f).

## Gap item
B3, field `verdicts.internal` of `docs/research/claims/B3-k-neq-mu-values-umbrella.md` (l.12). **The value stays `pending`.** Only its comment changes. Fidelity and external do not move.

## Deliverable
One integration per the `integrate-check` skill, applying the write-up's §5 and its "Review resolution (fix pass 1)" and nothing more:
1. No new quotes (§5 cites existing Q-ids only). Do not file the unquoted Z18429937 sentence (Open 3); report it in one line.
2. `research/checks/REVIEW.md`: one entry for the combined review (38e19ef), with its severity counts as the review file gives them, and the fix pass (4360f38).
3. `RESULTS.md` (one paragraph, both sides, from §4); `QUEUE.md` (B3-internal DONE 2026-11-26, value `pending`; open: the umbrella aggregation rule, owner); `docs/research/ROADMAP.md`, the matching row only if one exists (do not add one).
4. Claim file: replace the l.12 comment with §5's comment text, value unchanged. Add an "R4 B3-internal" paragraph crediting both sides, with §5's Readings table. **No `reading-dependent:` prefix; B3 is not counted as reading-dependent and is not scoped (§3, §5 "Counts").** In the l.72 paragraph, mark (don't delete) "(rule C, not scored)" with a dated note: the ground is N2b own-text scope (X1 l.63) plus rule C (review C-3).
5. Argmap: `chk:B3-internal` and `rev:R4-B3-internal-combined` in `NOTES.md`; defeaters only as the write-up licenses (none is required); lineage node.
6. Gates and counts as in the skill (lint `--write-hierarchy`, `argmap_check.py` 0/0, `argmap_render.py`, counts in `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`, `readme_figs.py`, revert SVGs whose only diff is random ids). Counts should not change (no field moves).

## Allowed paths
- `research/checks/REVIEW.md`, `RESULTS.md`, `QUEUE.md`
- `docs/research/ROADMAP.md`
- `docs/research/claims/B3-k-neq-mu-values-umbrella.md`, `hierarchy.yaml`, `hierarchy/*.md` (as regenerated)
- `docs/research/argmap/NOTES.md`, `defeaters.yaml`, `lineage.yaml`
- `docs/arguments/`, `README.md`, `docs/HANDOFF.md`, the README figures `readme_figs.py` writes

Read anything (grep big files by id). Do not edit `R4-B3-internal.md`, any review file, other claim files, `gap-blockers.yaml`, `DECISIONS.md`, ledgers, `criticality/` or the board.

## Skill
`integrate-check`. Local lint/render tools only; no host work, no fetch.

## Budget
At most 3 commits. No fix passes apply.

## Stop when
- the integration is committed and pushed to `research`, lint and argmap_check at 0/0; OR
- a step needs a field move, a fetch, a new quote, or a path outside the list (report; don't work around it); OR
- a gate fails for a reason outside B3 (report as a possible `upkeep` item).

## Not in scope
Any verdict value; B3 fidelity and external; the umbrella aggregation rule (owner); re-scoring B3a-B3m; the board, a milestone post, `git push origin research:master`. Ideas: one line in the report.

## Commit trailer
`Gap: B3`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`.

## Report (≤ 300 words, as the issue comment)
Commits; shared files changed; counts before and after (expected unchanged); every verdict field whose value or governing reading changed (expected: none); new REVIEW, defeater and lineage ids; anything you stopped on; next step (row B3 to `owner` for the aggregation rule).
