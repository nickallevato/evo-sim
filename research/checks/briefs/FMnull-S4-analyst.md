# Brief FMnull-S4 (analyst): criterion S4 and the Poisson re-estimate

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

## Goal

Finish the two pieces `R4-FMnull.md` registered or named and did not run:

1. **Criterion S4 — tree-incongruent sharing above the ILS rate.** S4 was registered and
   never run. Either run it or **drop it with a stated reason written into the results
   file**; an unrun registered criterion is a pre-registration defect, and the criticality
   layer will score it as one either way. Say which you did and why, in the registration
   language.
2. **The Poisson GLM re-estimate of the covariate-adjusted index.** Needed only if S1's
   covariate clause is to be used. It needs `fm_bins.npz`, which lives on `na-workhorse`.
   If you conclude the covariate clause is not going to be used, say so and skip it —
   explicitly, not silently.

Both are **post hoc** relative to the original FMnull registration. Label them so, in the
docstring and in the write-up, and commit the script before the run (rule 5).

## What the lead has already seen

- `research/checks/results/R4-FMnull.md` (integrated 2026-10-13, reviews #76-#79, fix pass
  `2802425`): Day's "> 80 times more variable" is true at W ≥ 1 Mb in every lineage and
  never outside the neutral band where true (index / N_hi 0.11-0.91); little power below a
  dominant block mechanism. **No verdict value moved**: FM3 external `supported` as a
  description and non-discriminating; FM10 internal `pending` (owner decision); no defeater
  against FM10 licensed.
- The ILS sigma upper edge (0.30-0.54) is one of the write-up's **unsourced brackets**. S4
  is a test against the ILS rate, so it stands or falls on that bracket: source it or carry
  it as a declared range across the whole result, and register the band before you look.
- Two items the integration left for the lead, **not yours**: the criticality-layer record
  beside ST-10, and the DECISIONS.md proposal for a fair Day-side criterion (K12).

## Review tier

**Load-bearing: three reviews** (correctness, steelman-day, steelman-critic). FMnull feeds
**FM3** and **FM10**, both marked `load_bearing: true` in `docs/research/hierarchy.yaml`,
and S4 is the criterion most able to move FM10's internal verdict off `pending`. Register
in advance, exhaustively, which S4 outcomes would license a defeater against FM10 and which
would not — the previous round's S2 criterion defect (write-up C8, D10: a margin symmetric
about the stacked upper corner, taken on the value) is the failure mode to avoid.

## Files you may write

- `research/checks/fmnull_s4.py` (or similarly named; pre-registered, committed before the
  run, predictions and bands in the docstring)
- `research/checks/results/R4-FMnull.md` — **new sections only**, appended, labelled post
  hoc; do not rewrite the scored sections
- `research/checks/results/raw/` outputs and the `.host` record

Not yours: claim files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers, the argmap data,
`DECISIONS.md`, the criticality folder.

## Constraints

- `AGENTS.md` hard rules and token budget. Read `R4-FMnull.md` by heading, never whole.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16 02:00-08:00 -06:00.** Nothing
  launches there before the `ph2` collect task is done. Design, pre-register and smoke-test
  locally (one process, under 500 MB, under a minute); the run is a separate later task.
  When it does run: at most 11 busy processes across all agents, RAM under ~12 GB, check
  `uptime` first, launch with `< /dev/null`, record hostname and md5s in `raw/<x>.host`.
- Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits (the pre-registration commit first); the registered bands for S4 and which FM10
moves each would license; whether the Poisson re-estimate is in scope and why; failures;
next step.
