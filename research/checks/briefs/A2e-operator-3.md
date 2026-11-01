# A2e-operator-3: integrate R4-A2e-fidelity (field move: fidelity pending → unverifiable)

**Role:** operator. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e; `R4-A2e-fidelity.md` (criterion 0fd4581, write-up 0f8f64a, fix pass 1 da89938, lead-approved EVOA-16); combined review `REVIEW-R4-A2e-fidelity-combined.md` (61fc014); lead ruling on conflict 1 in `A2e-analyst-4.md`.

## Gap item
A2e, field `verdicts.fidelity` of `docs/research/claims/A2e-ltee-as-ceiling.md`: `pending` → `unverifiable`, exactly as section 4's comment text gives it. **The issue carries an owner approval stage; the field move is final only when the owner approves.** Internal and external do not move.

## Deliverable
One integration per the `integrate-check` skill, applying `R4-A2e-fidelity.md` section 4 (comment text) and section 8 and nothing more:
1. Quotes: Open 3 asks for the s1/s2 Day sentences the integration cites (l.62-149 of the held `main.txt`, sha256 `0287f54b…`), into `quotes-day.md` with the next Q ids, verbatim, locator and date. Only those you cite; not found exactly: don't add, report.
2. `research/checks/REVIEW.md`: one entry for the combined review (61fc014), with counts (0 BLOCKER, 2 MAJOR, 10 MINOR) and the fix pass (da89938).
3. `RESULTS.md` (one paragraph, both sides, from section 5); `QUEUE.md` (A2e-fidelity DONE, 2026-11-01; open: U3-U5 and U6 fetches, Open 3/4); `docs/research/ROADMAP.md`, the matching row if one exists (do not add one).
4. Claim file: replace `fidelity: pending` with the section 4 comment text; an "R4 A2e-fidelity" paragraph crediting both sides. A2e is `SCOPED` (MINOR-3): no `reading-dependent:` comment, not counted as reading-dependent. Per review NOTE-9: mark that the claim table's "verified" rows are quote checks, not scored Day uses, and give "Fidelity n/a unchanged" (l.77) its lost scope (from `R4-A2e-alpha.md` l.125); mark, don't delete.
5. `docs/research/ledgers/fidelity.md`: the A2e rows (U6 `unverifiable`; U3-U5 not held), in the ledger's existing form.
6. Argmap: `chk:A2e-fidelity`, `rev:R4-A2e-fidelity-combined` in `NOTES.md`; defeaters only as the write-up licenses; lineage node.
7. Gates and counts as in the skill (lint `--write-hierarchy`, `argmap_check.py` 0/0, `argmap_render.py`, counts in `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`, `readme_figs.py`, revert SVGs whose only diff is random ids).

While editing the write-up's text into shared files, drop the duplicated "No held use is misread or partial" in section 5's first Day bullet (do not edit the write-up itself).

## Allowed paths
- `research/checks/REVIEW.md`, `RESULTS.md`, `QUEUE.md`, `PREREG-STATUS.md`
- `docs/research/ROADMAP.md`, `docs/research/sources/quotes-day.md`, `docs/research/ledgers/fidelity.md`
- `docs/research/claims/A2e-ltee-as-ceiling.md`, `hierarchy.yaml`, `hierarchy/*.md` (as regenerated)
- `docs/research/argmap/NOTES.md`, `defeaters.yaml`, `lineage.yaml`
- `docs/arguments/`, `README.md`, `docs/HANDOFF.md`, the README figures `readme_figs.py` writes

Read anything. Do not edit `R4-A2e-fidelity.md`, any review file, `gap-blockers.yaml`, `DECISIONS.md`, `parameters.yaml`, `criticality/` or the board.

## Skill
`integrate-check`. Local lint/render tools only; no host work, no fetch.

## Budget
At most 3 commits. No fix passes apply.

## Stop when
- the integration is committed and pushed to `research`, lint and argmap_check at 0/0; OR
- a step needs a field move other than A2e fidelity, a fetch, or a path outside the list (report; don't work around it); OR
- a gate fails for a reason outside A2e (report as a possible `upkeep` item).

## Not in scope
A2e external (waits on the owner with B and O-17) and internal; the `fidelity.md` l.37 Good 2017 "SI not retrieved" row (review NOTE-3: report it in one line, don't edit); rule F changes; the board, a milestone post, `git push origin research:master`. Ideas: one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`.

## Report (≤ 300 words, as the issue comment)
Commits; shared files changed; counts before and after; every verdict field whose value or governing reading changed (expected: A2e fidelity only); new Q, REVIEW, defeater and lineage ids; anything you stopped on; next step.
