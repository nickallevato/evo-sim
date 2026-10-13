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
- In `docs/research/hierarchy.yaml`: **D10**, **D11**, **D12** and **D** itself are all
  `load_bearing: false`; D11 and D12 attack D10, D10 supports D, and D is a branch root
  under ROOT. **C1d is a check id, not a claim id** (corrected by the lead 2026-10-13): the
  original C1d scored C6, C7, C, C5a, C5b, B2e and C4 (`RESULTS.md` section C1d,
  `results/R4-C1d.md`); none of those is marked `load_bearing: true` either.
- The D branch is where the audit most risks scoring a rhetorical point as a mathematical
  one. Rule **RH** applies: tag each quoted statement `dialectic` or `rhetoric` first;
  rhetoric is not literal-fact-checked and moves no verdict.

## Review tier

**Lead ruling, 2026-10-13 (supersedes the tier paragraph this brief carried when it was
first committed at 817d049).** The original paragraph set "low-stakes: one combined review"
per part on the test "none of these nodes is marked `load_bearing: true`". That is the
**D-16** test, and **D-23** (owner, 2026-10-13, "Three reviews") supersedes it: three
reviews are due where a check's registration carries a verdict-field flip, **or its node is
a listed feeder of a load-bearing node** (`R5-draft.md` section 1.3), even where
`hierarchy.yaml` does not mark it `load_bearing`. Both parts hit that clause:

- **Part A — three reviews.** `R5-draft.md` 1.3 lists the row **"C / C6 / C1c (aDNA '21')"**
  as a feeder on a ROOT path. The C1d follow-ups test that same node. Files:
  `REVIEW-R4-C1d-fu-correctness.md`, `-steelman-day.md`, `-steelman-critic.md`, run one
  after another under the cap of one agent.
- **Part B — tier decided at registration, default three.** `R5-draft.md` 1.3 lists the row
  **"D (sequence space)"**. D10-D12 are not themselves rows, so the trigger is the other
  D-23 limb: **if the registration carries any verdict-field flip** on D10, D11, D12 or D,
  Part B takes three reviews (`REVIEW-R4-D-fu-correctness.md`, `-steelman-day.md`,
  `-steelman-critic.md`). Only if the registration carries no verdict-field flip and touches
  no verdict or defeater on D does Part B fall back to the single combined
  `REVIEW-R4-D-fu-combined.md`. **State which, in the registration docstring, before the
  run** — the tier is fixed in advance, never after the numbers are seen.

**Escalation clause, unchanged:** if either part would change a verdict or defeater on **D**
itself (a branch root feeding ROOT) or on **C2 / C2a** (both load-bearing), that part is
load-bearing and takes three reviews. Report it; do not apply the move.

This is a tier change, so standing procedure item 3 (a criticality pass) applies to it, as
it did to D-23 itself; the lead carries that, not the analyst.

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
