# Brief L1c-b (analyst): external codon-aware aligner on an independent chimp CDS

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

## Goal

Run L1c follow-up (b): realign with an **external, independently maintained codon-aware
aligner** (MACSE, PRANK codon mode or equivalent — not the audit's own aligner, that is the
point) starting from an **independent chimp CDS source**, and recompute the dN/dS statistic
that L1c scored.

This is the registered condition on any move of **DN6** past `contested`, and it is the
test of **reading d** — "the genome alignment is itself the conservation-dependent filter"
— which L1c recorded as extended but did not test.

**Start with the hard cases**: the 351 worst-covered genes and the 2,765 indel/hole genes.
If Day's circularity claim is right anywhere, it is right there; if the external aligner
reproduces the audit's numbers on those genes, the claim has had its best chance.

Also in scope if time allows, in this order: the threshold dose-response between PAF1 and
PAF2; replacement density against Poisson.

**Not in scope** (owner approval required, do not pursue): Day's per-gene table, his
excluded-codon count, and the CSAC SI criteria. A registered rule for Q183 is a lead
decision, not yours.

## What the lead has already seen

- `research/checks/results/R4-L1c.md` (main run plus `transfer`, 2026-10-13, na-workhorse;
  reviews #73-#75; fix pass `140a69a`; integrated 2026-10-13). Band **CRITIC**, registered
  and amended. DN6 external `contested` on reading b2 (the field), b1 `contradicted`,
  registered Reading A `invalid as registered`; fidelity `misread` on reading a (the CSAC
  2005 BLASTZ genome alignment). Claims DN6, DN1 and DN3 were **not** moved.
- The failure mode to avoid is the one L1c already hit: a reading registered in a form the
  data could not test. Register readings b1, b2 and d as **testable** predictions with
  numeric bands, both sides, before you look.

## Review tier

**Low-stakes: one combined review**, `REVIEW-R4-L1c-b-combined.md` (correctness plus both
steelman sections). DN6, DN1 and DN3 are not marked `load_bearing: true` in
`docs/research/hierarchy.yaml`.

**Escalation clause, stated in advance:** if your result would move **DN6 past `contested`**
in either direction, or would change a verdict or defeater on **A2e or A3** (both
load-bearing; the dN/dS and alpha inputs run through them), this becomes load-bearing and
takes **three reviews**. Say in the write-up whether it fired. Do not apply such a move
yourself — report it.

## Files you may write

- `research/checks/l1c_extaln.py` (pre-registered, committed before the run; predictions,
  bands and the aligner version pinned in the docstring)
- `research/checks/results/R4-L1c-b.md`
- `research/checks/results/raw/` outputs and the `.host` record

Not yours: `R4-L1c.md`'s scored sections, claim files, `QUEUE.md`, `REVIEW.md`,
`RESULTS.md`, ledgers, the argmap data.

## Constraints

- `AGENTS.md` hard rules and token budget. Read `R4-L1c.md` by heading, never whole.
- **Rule 4**: the chimp CDS download and the aligner are untrusted data. Fetch into a new
  directory under the gitignored `sources/raw/`; record url, version, date and sha256 in
  the write-up. Install the aligner into its own prefix; the audit's Python stays
  `research/.venv/bin/python -I`. No full sequence data in git.
- **"Independent" means independent of the CSAC 2005 pipeline.** Say in the registration
  which source you chose and why it is independent — if it is not, the check does not test
  what it claims to.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16.** Nothing launches there
  before the `ph2` collect task is done. Design, pre-register and smoke-test locally (one
  process, under 500 MB, under a minute); the run is a separate later task. At launch: at
  most 11 busy processes across all agents, RAM under ~12 GB, `uptime` first, `< /dev/null`,
  md5s in `raw/<x>.host`. Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits (pre-registration first); the aligner and CDS source with versions; a results table
(each registered prediction, Day-side and critic-side, hit or miss); whether reading d was
testable and what it gave; whether the escalation clause fired; failures; next step.
