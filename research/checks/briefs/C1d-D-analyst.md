# Brief C1d-D (analyst): the C1d follow-ups and the D follow-ups

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

This is **one queue item with two parts** (`QUEUE.md` items 5 and 6). Do part A first,
commit it, then part B. Both are small follow-ups to checks already written up; neither is
a new branch.

## Part A — C1d follow-ups

1. A **transversion-restricted, SFS-matched neutral model**: redo the C1d comparison on
   transversions only, with the site-frequency spectrum matched, so the transition/
   transversion asymmetry cannot carry the result.
2. **What the transition excess is**: name and quantify it — CpG deamination, ascertainment,
   damage in ancient DNA, or a residual. "An excess exists" is not an answer; the audit
   needs its size with an interval and its most likely cause, or an explicit
   `unverifiable`.

## Part B — D follow-ups (D10-D12)

1. **ProteinGym multi-mutant decay**: how fitness/function falls with the number of
   mutations, from the public ProteinGym assays.
2. **A noise null for the beneficial proxy**: what fraction of the "beneficial" calls the
   measurement noise alone produces. Register the null before you look.
3. **Per-sequence prevalence** across D10 (Axe, 1 in 10^77), D11 (Taylor, ~10^24 library)
   and D12 (Keefe & Szostak, 4 of 6×10^12): put the three on one common per-sequence basis
   so they can be compared at all. Much of the apparent disagreement between them is a
   units difference; say how much of it is, and how much is real.

## What the lead has already seen

- `QUEUE.md` items 5 and 6 are the full text of both follow-up lists; nothing else is
  registered for them.
- In `docs/research/hierarchy.yaml`: **D10** and **D12** are `load_bearing: false`; D11
  attacks D10 and supports D; D is a branch root under ROOT. C1d sits in the C branch under
  C1.
- The D branch is where the audit most risks scoring a rhetorical point as a mathematical
  one. Rule **RH** applies: tag each quoted statement `dialectic` or `rhetoric` first;
  rhetoric is not literal-fact-checked and moves no verdict.

## Review tier

**Low-stakes: one combined review** for each part — `REVIEW-R4-C1d-fu-combined.md` and
`REVIEW-R4-D-fu-combined.md` (correctness plus both steelman sections in each). None of
C1d, D10, D11 or D12 is marked `load_bearing: true`.

**Escalation clause, stated in advance:** if either part would change a verdict or defeater
on **D** itself (a branch root feeding ROOT) or on **C2 / C2a** (both load-bearing), that
part becomes load-bearing and takes **three reviews**. Report it; do not apply the move.

## Files you may write

- `research/checks/c1d_tv.py` and `research/checks/d_followups.py` (pre-registered,
  committed before their runs, predictions and bands in the docstrings)
- `research/checks/results/R4-C1d-fu.md` and `research/checks/results/R4-D-fu.md`
- `research/checks/results/raw/` outputs and the `.host` records

Not yours: existing scored write-ups, claim files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`,
ledgers, the argmap data.

## Constraints

- `AGENTS.md` hard rules and token budget.
- **Rule 4**: ProteinGym and any sequence data are untrusted downloads — own new directory
  under the gitignored `sources/raw/`, read or grep, never execute, sha256 and access date
  recorded. **Rule 3**: no bulk data in git.
- Every number from a paper gets a verbatim quote with a locator and a date (rule 2). The
  Axe, Taylor and Keefe & Szostak figures are relayed in several places in the corpus;
  check each against the raw text, not against the audit's own earlier summary of it.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16.** Nothing launches there
  before the `ph2` collect task is done. Design, pre-register and smoke-test locally (one
  process, under 500 MB, under a minute); runs are separate later tasks. At launch: at most
  11 busy processes across all agents, RAM under ~12 GB, `uptime` first, `< /dev/null`,
  md5s in `raw/<x>.host`. Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words, covering both parts)

Commits (each pre-registration first); one results table per part (each registered
prediction, Day-side and critic-side, hit or miss); the size and named cause of the
transition excess; the three D figures on their common per-sequence basis; whether either
escalation clause fired; failures; next step.
