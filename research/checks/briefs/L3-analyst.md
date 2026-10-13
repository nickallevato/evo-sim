# Brief L3 (analyst): alpha from MK with demographic correction

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

## Goal

Reproduce a **bias-corrected human-chimp alpha** on public polymorphism data, using the
asymptotic MK method (Messer and Petrov 2013), and place it against **alpha\* ≈ 1%** — the
threshold the A2e argument turns on.

The point of the asymptotic form is that it corrects for slightly deleterious polymorphism
and for demography, which is where the standard MK estimate is known to be biased. Report
the standard MK value and the asymptotic value side by side, with their confidence
intervals, so the size of the correction is visible rather than buried.

Register in advance: the polymorphism dataset and frequency cutoffs, the divergence set,
the fit form, and both sides' predicted bands for alpha.

## What the lead has already seen

- `research/checks/results/R4-A2e-alpha.md` (reviews #53-#55; fix pass `e7ecda6`;
  integrated 2026-10-10, **load-bearing tier**). Bias-corrected alpha estimates — Boyko
  9.3%, Uricchio abstract, Eyre-Walker & Keightley conditional 40% — are all above
  alpha\* ≈ 1% (lowest compounded Day-charitable row 299 vs 191). Gayà-Vidal's 0.2% is an
  **MK null, not a count**; its accelerated genes straddle 191 (228, 112-323; 67-136
  corrected). A2e external stays `contested`, leaning `contradicted`.
- **The Uricchio 2019 blocker is cleared.** `QUEUE.md` L3 says it "needs Uricchio 2019 full
  text (owner)"; that text was obtained, reviewed (#64) and integrated on 2026-10-11, and
  the owner accepted the two-reading scoping (A2e external `contradicted` scoped to the
  any-effect-size per-generation count; strong-only / fitness-weighted stays `contested`).
  **L3 is not blocked.** Your result must respect that scoping: say which of the two
  readings your alpha speaks to, because an alpha estimate that answers the strong-only
  reading and one that answers the any-effect-size reading move different fields.
- `QUEUE.md` also proposes **RG-03**, a non-coding human-lineage adaptive-substitution
  source. Out of scope here; note it if your data bear on it.
- Day's position is that K is not derivable from first principles (Z23020792); the critics'
  is "most differences are neutral", with no number. Both sides therefore gain from a
  sourced alpha, and both can lose. Write the "Who this helps" section accordingly.

## Review tier

**Load-bearing: three reviews** (correctness, steelman-day, steelman-critic).
**A2e** is marked `load_bearing: true` in `docs/research/hierarchy.yaml`, and this check can
move its external verdict from `contested, leaning contradicted` to `contradicted` — or
pull it back. Register in advance, exhaustively, which alpha intervals license which move
on A2e (and on A and F2 if they propagate), and which license none.

## Files you may write

- `research/checks/l3_amk.py` (pre-registered, committed before any run; dataset, cutoffs,
  fit form, both sides' predictions and the exhaustive band-to-verdict table in the
  docstring)
- `research/checks/results/R4-L3.md`
- `docs/research/sources/bib-lit.md` and `docs/research/sources/quotes-lit.md` — appended
  rows for the polymorphism and method sources only
- `research/checks/results/raw/` outputs and the `.host` record

Not yours: `R4-A2e-alpha.md`, claim files, `parameters.yaml`, `QUEUE.md`, `REVIEW.md`,
`RESULTS.md`, ledgers, the argmap data.

## Constraints

- `AGENTS.md` hard rules and token budget. Read `R4-A2e-alpha.md` by heading, never whole.
- **Rule 2**: every published number you compare against gets a verbatim quote with a
  locator and a date, checked against the raw text. The Boyko, Uricchio, Eyre-Walker &
  Keightley and Gayà-Vidal figures are already quoted in the audit — reuse those Q ids
  rather than re-quoting from memory, and verify any new one.
- **Rule 6**: no paywall bypass, no shadow libraries. Public polymorphism data only
  (1000 Genomes, gnomAD under its terms, or equivalent); record the exact release.
- **Rule 4**: downloads into their own new directory under the gitignored `sources/raw/`;
  read or grep, never execute; sha256 and access date recorded. No bulk VCF in git.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16.** Nothing launches there
  before the `ph2` collect task is done. Design, pre-register and smoke-test locally (one
  process, under 500 MB, under a minute); the run is a separate later task. At launch: at
  most 11 busy processes across all agents, RAM under ~12 GB, `uptime` first, `< /dev/null`,
  md5s in `raw/<x>.host`. Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits (pre-registration first); standard MK and asymptotic MK alpha with intervals and
the size of the correction; which Uricchio reading your alpha speaks to; the band-to-verdict
table and which row the result lands in for A2e; failures; next step.
