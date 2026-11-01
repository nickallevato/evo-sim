---
name: check-lifecycle
description: Take one evo-sim check from a finished run to a reviewed, fix-passed write-up using the analyst and reviewer agents and the write-up, review and fix-pass skills. Use after raw outputs are collected and committed.
---
# From raw outputs to a fix-passed write-up

Three agents exist (`.claude/agents/`): `analyst` (Opus), `reviewer` (Opus), `operator` (Sonnet). Each brief names the skill the agent must load. None of the steps below touches a shared file, so they can overlap with other checks' agents.

## Steps
1. **Write-up** (`analyst` + skill `write-up-check`): `research/checks/results/R4-<ID>.md`. Give it the script path and registration commit, any pre-run note, the raw output paths and the claim files. Tell it which numbers you have already seen and that it must verify them.
2. **Review** (`reviewer`, a fresh instance): always ONE combined file `REVIEW-R4-<ID>-combined.md` (D-40): a correctness section (skill `review-correctness`), then a Day-side and a critic-side section (skill `review-steelman`, both sides in the same file, equal depth). No three-review tier. Math-map work, lookups, arithmetic: seeded spot check by the lead, no review.
3. **Rulings.** Where the steelmen conflict, rule each conflict in writing before the fix pass, and put the rulings in the fix-pass brief so they end up quoted in the write-up. Defaults that held up on 2026-10-13:
   - registered wording stays registered; new findings go in separate sentences labelled post hoc;
   - the audit's own missed predictions and bugs go under "Both / the audit's own errors", never as credit to a side;
   - record every plausible reading with its verdict (rule RD); never ask the owner to pick;
   - a candidate cause the audit located but cannot tie to the author's unseen pipeline is "a candidate error class with a real-data instance";
   - a registered verdict flip is withheld if a reading is unresolved or the test could not have come out the other way; say so and why.
4. **Fix pass** (`analyst` + skill `fix-pass`): answers every MAJOR and MINOR by id; post hoc scripts committed before they run.
5. Hand over to the `integrate-check` skill.

## Briefs
Save each agent brief as `research/checks/briefs/<ID>-<role>.md` and commit it before spawning (MA-21: briefs were not in git and could not be audited). A brief states the goal, the files, what the lead has already seen, the constraints (which files may be touched, explicit git paths, no push to master) and the report format (at most 300 words). Do not list your own suspicions for a reviewer beyond pointing at the write-up's "looked wrong" list.

## What to check when a report comes back
- The commit exists and touched only the allowed files (`git show --stat`).
- Any claim that surprises you: open the file and look before repeating it to the owner.
- Reports are the agent's words, not the owner's approval.
