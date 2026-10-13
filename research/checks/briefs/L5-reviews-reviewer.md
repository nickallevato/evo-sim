# Brief L5-reviews (reviewer): the two reviews L5 is missing under the new tier rule

Lead: Big Sim. Written 2026-10-13, before the tasks were created (MA-21).
Skill to load: `.claude/skills/review-check/SKILL.md`.
Authority: owner decision **D-23** of 2026-10-13, verbatim: "Three reviews" — a check that
is not marked load-bearing but whose registration carries a verdict-field flip, or whose
node is a listed feeder of a load-bearing node, gets three reviews. That supersedes D-16,
which had lowered L5's tier to one combined review after registration.

## Standing of this task

L5's pre-registered docstring asked for three reviews. On 2026-10-11 the tier was lowered
to one (D-16); the one that was done found 7 MAJOR and the C-external flip was withheld.
The owner's answer of 2026-10-13 restores three for exactly this case. **The lead reads
that as giving L5 its two missing reviews before the withheld flip can be integrated. The
owner was not asked that sub-question and may overrule it**; if he does, these two tasks
are dropped and nothing else changes.

## The two reviews

| # | Review | File |
|---|---|---|
| 1 | steelman-day | `REVIEW-R4-L5-steelman-day.md` |
| 2 | steelman-critic | `REVIEW-R4-L5-steelman-critic.md` |

The correctness review exists (the one with 7 MAJOR). Read it; do not redo it. Your job is
the side you are given, argued as hard as it can be argued honestly, on the write-up as it
now stands after its fix pass.

The live question behind both: the registered arithmetic excludes a Day-side outcome at
s ≤ 0.01 and allows one at s ≥ 0.03, and the C external `contested` → `contradicted` flip
was withheld on rule RD (an extended reading cannot set the field). Day side: is the
withheld flip rightly withheld, and is the s range the registration used fair to him?
Critic side: does the evidence carry the flip under the as-written reading, and was
withholding it over-cautious?

## Rules

- You write **only your own review file**. No claim file, no ledger, no `QUEUE.md`.
- BLOCKER / MAJOR / MINOR, each with file and line.
- First line says which side you are steelmanning.
- Conflicts between the two steelmen are ruled by **the lead** (D-24), who writes the
  ruling into the brief before any fix pass. Make your case; do not split the difference.
- One agent at a time (D-22): these two run one after another, not together.
- Report ≤ 300 words.

## After both

The flip stays withheld until the lead has ruled on the two steelmen and a fix pass has
answered every MAJOR and MINOR. Integration is a separate task.
