# Brief L5-C1a (analyst): the random-SNP comparator for C1a's sign

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

## Goal

Settle the sign of the ascertainment effect that **C1a** asserts, which L5 left untested.

C1a is Day's reply to C1: *"panel ascertainment bias would favor detecting recent
fixations, not obscure them."* The test is a **random-SNP comparator**: against a matched
set of sites drawn without the 1240k panel's present-day-variable ascertainment, does the
expected count of detectable recent fixations go **up** (Day) or **down** (the critics) in
the ascertained panel, at the same s and the same horizon?

Register the comparator's construction in advance: how sites are drawn, how the SFS and
coverage are matched, and the numeric band that counts as each side's hit. The sign is the
result; the magnitude is secondary and should be reported with an interval.

Also open from L5 and in scope if the design reaches them: the size of the Z50 / Z10
understatement at s ≥ 0.05; sweep independence at F = 15,556. **Not in scope**: which of
B10 / Z50 / Z10 is Day's primary statistic (the L5 band does not depend on it, and it is an
outside-input question).

## What the lead has already seen

- `research/checks/results/R4-L5.md` (pre-registered `0e6da82`; run on na-workhorse;
  reviewed #80 combined `d7f70ec`; fix pass `0b0431c` with post hoc `l5_posthoc_v3.py`
  `c9f3d69`; integrated 2026-10-13). Band **CRITIC**: the zero carries no information at
  s ≤ 1e-2 (the registered scope, Q44's 1e-3 included); descriptively the same at s = 0.02;
  at s ≥ 0.05 the panel registers hundreds to thousands of events where mainstream expects
  about zero.
- **No verdict value moved.** C external stays `contested` (reading-dependent, Readings
  R-a..R-e; the registered field flip was withheld), C1 `supported`, **C1a `contested`**.
  The audit's own figures "5.7" (C) and "4.8" (C1) are annotated; slip S-L5-1.
- L5's review tier was set by the owner (2026-10-11) to **one combined review**, overriding
  the three stated in the `l5_adna_power.py` docstring; the script is never edited, so the
  tier lives in `QUEUE.md`. The same reasoning applies to this follow-up — see below.
- D3 is only a partial sensitivity, and the mainstream s mapping is assumed. If your
  comparator depends on either, declare it as a bracket.

## Review tier

**Low-stakes: one combined review**, `REVIEW-R4-L5-C1a-combined.md` (correctness plus both
steelman sections). C, C1 and C1a are not marked `load_bearing: true` in
`docs/research/hierarchy.yaml`.

**Escalation clause, stated in advance:** C1a's sign is the pivot of the C branch. If your
result would move **C1a off `contested`**, or would license the C external field flip that
L5 deliberately withheld, this becomes load-bearing and takes **three reviews**. Report it;
do not apply the move.

## Files you may write

- `research/checks/l5_c1a_randsnp.py` (pre-registered, committed before the run; comparator
  construction, both sides' predictions and bands in the docstring)
- `research/checks/results/R4-L5-C1a.md`
- `research/checks/results/raw/` outputs and the `.host` record

Not yours: `R4-L5.md`'s scored sections, claim files, `QUEUE.md`, `REVIEW.md`,
`RESULTS.md`, ledgers, the argmap data.

## Constraints

- `AGENTS.md` hard rules and token budget. Read `R4-L5.md` by heading, never whole.
- Reuse the L5 machinery rather than rebuilding it; if you change a parameter L5 fixed, say
  which and why, and show the L5 numbers reproduce before the comparator is added.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16.** Nothing launches there
  before the `ph2` collect task is done. Design, pre-register and smoke-test locally (one
  process, under 500 MB, under a minute); the run is a separate later task. At launch: at
  most 11 busy processes across all agents, RAM under ~12 GB, `uptime` first, `< /dev/null`,
  md5s in `raw/<x>.host`. Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits (pre-registration first); the comparator's construction in three sentences; a
results table (each registered prediction, Day-side and critic-side, hit or miss) with the
sign and its interval; whether the escalation clause fired; failures; next step.
