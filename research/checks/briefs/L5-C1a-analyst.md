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

## Lead ruling LC-R1..LC-R5 (Big Sim, 2026-10-14; written before the main run)

The registration (`l5_c1a_randsnp.py` s5, commit `1c6e983`) left one question to the lead:
L-R8 made reading (i) governing for the *"not obscure"* clause but did not rule **which
comparator governs the "favor detecting" clause**. Ruling it now, with no result in hand, is
the only time it can be ruled without fitting it to the sign. D-24.

**LC-R1. Within reading (iv), the governing comparator is R, the unascertained SNP panel.**
Not (ii) random base pairs, not (iii) whole-genome data. Day's subject is *"such bias"* — a
selection criterion — and the counterfactual to a criterion is the same object with the
criterion removed and everything else held: same site count, map density, coverage model,
samples. That is R by construction (s2). Reading (ii) confounds the ascertainment with
*being an SNP panel at all*, which Day does not assert and no critic disputes.
*Day-side counter, recorded:* the claim file's registered wording is "a random **site**
sample", which reads toward (ii) — but that wording is the audit's own paraphrase, and an
audit-written gloss may not fix the baseline against the author. The check prints the (ii)
cross-check `rho_R0` anyway, so the Day-side number exists either way.

**LC-R2. The clause splits, and the "strengthens" inference goes with "favor".** L-R8 stands:
(i) governs *"not obscure"*. The *"favor detecting"* clause and the sentence it feeds — *"The
absence of recent fixations despite this bias strengthens our conclusion"* — take the
comparative reading, i.e. (iv) under LC-R1. Reason: that inference has no force on the
absolute reading. A bias that merely fails to obscure adds nothing to a null result; only a
bias that inflates the expected count relative to an unbiased design makes an observed zero
*stronger* evidence. Rule C cuts this way, not against it: the comparative reading is the one
on which Day's paragraph is a real argument rather than a truism.

**LC-R3. A CRITIC band does not by itself take C1a off `contested`.** This overrides the s5
proposal "C1a external contested -> contradicted (scoped)". Under rule RD, a result that
contradicts the *"favor"* clause while (i) still carries Day's sign for *"not obscure"* leaves
the statement **reading-dependent**: the field stays `contested`, and the Readings table
carries (i) supported / (ii) supported / (iii) wrong / (iv) contradicted, with the comment
naming the clause split and the scope (selection-driven completions, Day's zero-reported
statistic, actual panel design). The *"strengthens"* inference is separately recorded as
unsupported under LC-R2. A DAY band is a different matter: it aligns (i), (ii) and (iv), and
a `contested -> supported` move is then on the table for the operator and the lead.

**LC-R4. Escalation is retained on DAY *or* CRITIC, whether or not the field value moves.**
LC-R3 would otherwise switch the escalation clause off for CRITIC by a side effect of my own
ruling, which is not a reason to review a pivot result less. Either band changes the Readings
table of the C branch's pivot: **three reviews** (correctness, steelman-Day, steelman-critic,
separate agents, MA-21/O-26), unless the band is SENSITIVE under s5 (a)-(e), in which case it
moves nothing and the combined review stands.

**LC-R5. What would overturn LC-R1/LC-R2.** A located Day source that states the baseline
explicitly; an owner decision; or a reviewer showing that the *"despite this bias"* sentence
does not do inferential work in s9.4 of Z18525185 — the fresh reviewer is asked to attack
LC-R2 first, then LC-R1.

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
