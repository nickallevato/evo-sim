# Brief B1e-Q2 (analyst): B1e's second Statement quote and the Kimura (1955) link

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md` (one skill; design and pre-register,
then the write-up is a later task in the same lifecycle).

## Goal

Close the two gaps the B2f integration left open on `docs/research/claims/B1e-chalub-2022-reading.md`
(its "Fields set by this integration" paragraph names both):

1. **The 1/(2N) quote.** The second Statement quote is the 2026-08-23 blog sentence,
   "Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model.
   It is not a result produced by the mathematics."
   (voxday.net/2026/08/23/chalub-and-the-kimura-cancellation/, ¶5 of extracted text).
   B2f did not examine it. Score it: is 1/(2N) an input Chalub assumes, a consequence of
   the diffusion limit he derives, or a boundary/initial condition? Fidelity against
   Chalub 2022 verbatim, internal against Day's own derivation.
2. **Is Chalub's Gegenbauer expansion the Kimura (1955) series?** This decides how far the
   credit B2f gave Day for the derivation route reaches. If it is the same series under a
   change of variables, the route is standard and old; if it is a distinct solution, the
   relay is a fair description of a 2022 result. Settle it from the two papers'
   mathematics, not from either author's description of the other.

## What the lead has already seen

- B2f (`research/checks/results/R4-B2f.md`, integrated `de3c1a2`, review #82) found the
  exponent exact in the short-time limit and the described route real apart from the word
  "eigenvalue"; as an equality the form is low by (4πNₑ/T)^1.5 e^(T/16Nₑ).
- B1e's current fields: internal `holds`, fidelity `partial`, external `contested`, all
  reading-dependent (rule RD). Quotes Q286, Q288 and the ledger rows are already in
  `quotes-day.md`; the blog quote in the Statement block has no Q id yet — assign one.
- The Zenodo file was replaced on 2026-10-13; the first Statement sentence is superseded.
  The blog quote is not affected by that replacement.
- Chalub 2022 verbatim rows are already in the claim file's source table (lines 55-57).

## Review tier

**Low-stakes: one combined review**, `REVIEW-R4-B1e-Q2-combined.md`, with a correctness
section and both steelman sections. B1e is not load-bearing.

**Escalation clause, stated in advance** (it is the claim file's own condition): this check
becomes load-bearing and needs **two further reviews** (three in total) if your result
would change a verdict value or a defeater on **B1, B1a, B2 or B**, if Reading B is adopted
as field-setting on B1e, or if Day is found to have derived a number from F(T). If you
reach any of those, stop, write what you have, and report it to the lead; do not apply the
move yourself.

## Files you may write

- `research/checks/<id>.py` only if a computation is needed (it probably is not; this is a
  mathematics-and-text check). If you write one, pre-register it per the skill.
- `research/checks/results/R4-B1e-Q2.md`
- `research/checks/briefs/` — nothing; the brief is the lead's.

Not yours in this task: claim files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers,
quotes files, the argmap data. Integration is a separate task.

## Constraints

- `AGENTS.md` hard rules and token budget apply. Verbatim quotes with locator and date
  (rule 2). No full texts in git (rule 3). No outward actions (rule 6).
- Chalub 2022 and Kimura 1955: use the held copies under `sources/raw/` if present; read or
  grep, never execute. No paywall bypass, no shadow libraries. If Kimura (1955) is not
  obtainable within the rules, say so and score the link `unverifiable` rather than
  guessing.
- No computation on this workstation beyond a trivial check (one process, under 500 MB,
  under a minute). `na-workhorse` is busy with `ph2` until 2026-10-16: launch nothing there.
- Rules S, C and RD in `R4-X1-verdict-rule.md` govern the scoring; record every plausible
  reading with its verdict.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits; a results table (each registered prediction, Day-side and critic-side, hit or
miss); the proposed verdict for each of the two questions and whether the escalation clause
fired; failures; next step.
