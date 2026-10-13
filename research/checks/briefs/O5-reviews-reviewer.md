# Brief O5-reviews (reviewer): the six reviews that bring B internal and A2e external back

Lead: Big Sim. Written 2026-10-13, before the tasks were created (MA-21).
Skill to load: `.claude/skills/review-check/SKILL.md`.
Authority: owner decision **D-21** of 2026-10-13: "Put them back to `pending` until three
reviews are done".

## What is being reviewed

Both fields are `pending` as of the O5-revert pass. Three reviews each, six in all, each
its own task, each its own file. Under the cap of one agent (D-22) they run **one after
another**, not in parallel.

| # | Target | Review | File |
|---|---|---|---|
| 1 | B internal | correctness | `REVIEW-R4-B-internal-correctness-2.md` |
| 2 | B internal | steelman-day | `REVIEW-R4-B-internal-steelman-day.md` |
| 3 | B internal | steelman-critic | `REVIEW-R4-B-internal-steelman-critic.md` |
| 4 | A2e external | correctness | `REVIEW-R4-A2e-external-correctness-2.md` |
| 5 | A2e external | steelman-day | `REVIEW-R4-A2e-external-steelman-day.md` |
| 6 | A2e external | steelman-critic | `REVIEW-R4-A2e-external-steelman-critic.md` |

The question in each case is **not** "is the superseded value correct?" but the tier
question the single review never answered: does the evidence on record carry the field to
that value, under rule C (most charitable defensible reading), rule RD (every plausible
reading recorded) and the scoping the file states?

- **B internal** was `non-sequitur` on the N2b argument within Hard Limits, with reading F
  (flux fill 0.697) recorded alongside as `holds`, scoped to the B2 statement. The 2026-02
  blog quote predates Hard Limits by seven months and is not answerable to it.
- **A2e external** was `contradicted`, scoped to the per-generation count of adaptive
  coding fixations of any effect size on model-inferred alpha, resting on Uricchio 2019's
  lower 95% HPD with a 25% charity haircut. The strong-only and fitness-weighted readings
  stayed `contested`. Note that the scoping itself was accepted by the owner in D-12; the
  scoping is not reopened, only whether the evidence carries the value inside it.

## Rules for the reviewer

- You write **only your own review file**. You do not touch the claim file, the ledgers or
  `QUEUE.md`. You do not set a verdict; you say what the evidence carries.
- Severity labels as standing: BLOCKER / MAJOR / MINOR, each with the file and line it
  attaches to.
- A steelman review argues **one side as hard as it can be argued honestly**, and says so
  in its first line. Do not hedge to the middle.
- Where the Day-side and critic-side steelman conflict, **the lead rules** (owner,
  2026-10-13, D-24) and writes the ruling into the brief before the fix pass. Your job is
  to make your side's best case, not to pre-settle the conflict.
- You are a fresh instance with no memory of the authoring run. Do not go looking for the
  other reviews of the same field; if you have already written one of the six, say so.
- Token budget: grep by id, never read the big files whole. Report ≤ 300 words.

## What the lead already suspects

Stated here deliberately, because O-26's sub-question on whether briefs may name the
lead's suspicions is **still open** and until it is answered the standing practice is to
name them in the brief where they exist, so that they are on record rather than steering
the review silently:

- For A2e: the 25% charity haircut on N2 and the choice of the lower HPD rather than the
  point estimate are the two steps a Day-side steelman should attack hardest.
- For B: whether the 2026-02 blog sentence and the Hard Limits abstract sentence can carry
  one internal field at all, or whether the field is being set by the one of the two that
  suits the result.

## Deliverable per task

One review file, committed, named above. Then stop. The fix pass and any move off
`pending` are separate tasks and need all three reviews of that field in hand.
