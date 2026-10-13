# Brief L2 (analyst): a sourced hardness h for humans

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md`.

**This is the highest-value item in the batch.** The cost-of-selection answer turns on the
hardness parameter h, and h is currently **unsourced** — the audit has been reporting
results across a range it chose rather than one the data sets. Whoever picks h picks the
answer, which is exactly the move the audit exists to catch, on either side. Treat the
sourcing standard as the deliverable, not the number.

## Goal

Produce a **sourced interval for h in humans**, with its provenance, to place against the
thresholds in `research/checks/results/R4-HF.md`. Two independent routes, both named in
`QUEUE.md` item L2:

- **(a) Density-dependence of survival and fertility in historical cohorts.** h is the
  degree to which selection is soft (density- or rank-dependent, deaths substitute for one
  another) rather than hard (independent, deaths add). Historical demographic series with
  density variation identify it.
- **(b) Viability vs fertility decomposition of lifetime reproductive success**, on the
  Stearns 2010 and Byars 2010 designs.

Run both. If they disagree, **report the disagreement as the result** — do not average
them, and do not pick the one that favours either side. An honest interval that is too wide
to discriminate is a finding; the audit says so and h stays a declared bracket.

Write down, before you look at any number: the mapping from each published statistic to h
(this is the step where the result is really decided), and both sides' predicted bands.

## What the lead has already seen

- `research/checks/results/R4-HF.md` (main 1,720 jobs, `ci`, `gap05`, post hoc `ph`;
  reviews #66-#68 plus combined #69; fix pass `c2ac2c3`; integrated 2026-10-13). No verdict
  value changed: **H, H8, H5 external all stay `contested`**; the h-scope text, the Day-1
  clause and the latency-vs-throughput distinction were carried into H, H8 and H5.
- `QUEUE.md` L2 expects h in the region of **0.1 to 0.3**. That is the audit's prior, not a
  target. If the data put h outside it, say so plainly.
- HF open item (2) is a 4-of-8 tie at h = 0.1, R = 1.111 between 0.0094 and 0.0157 — i.e.
  the thresholds are genuinely close to the expected range of h, which is why this check
  can move verdicts.
- `research/checks/results/R4-HF.md` open item (6): no sourced human beneficial DFE or M
  exists (refresh 10b s3). Do not substitute one; if h's interpretation needs it, declare
  it as a bracket.
- `docs/research/parameters.yaml` is where a sourced parameter's provenance belongs — but
  writing to it is an **integration** step, not yours in this task.

## Review tier

**Load-bearing: three reviews** (correctness, steelman-day, steelman-critic).
H, H1, H5 and H8 are all marked `load_bearing: true` in `docs/research/hierarchy.yaml`, and
h is the parameter their external verdicts turn on. A sourced h that lands on one side of
the R4-HF thresholds moves them; register in advance, exhaustively, which intervals for h
license which verdict move on H, H5 and H8, and which license none.

## Files you may write

- `research/checks/l2_hardness.py` (pre-registered, committed before any run; the
  statistic-to-h mapping, both sides' predictions and the exhaustive band-to-verdict table
  in the docstring)
- `research/checks/results/R4-L2.md`
- `docs/research/sources/bib-lit.md` and `docs/research/sources/quotes-lit.md` — appended
  rows for the demographic sources only
- `research/checks/results/raw/` outputs and the `.host` record

Not yours: `parameters.yaml`, claim files, `R4-HF.md`, `QUEUE.md`, `REVIEW.md`,
`RESULTS.md`, ledgers, the argmap data.

## Constraints

- `AGENTS.md` hard rules and token budget. Read `R4-HF.md` by heading, never whole.
- **Rule 2**: every number from Stearns, Byars or a demographic database gets a verbatim
  quote with a locator and a date, checked against the raw text, never from a summarizer.
- **Rule 6**: no paywall bypass, no shadow libraries, no contacting authors. If a paper is
  paywalled, add it to the owner's list in the refresh file and carry the gap openly rather
  than filling it from memory.
- **Rule 4**: data downloads into their own new directory under the gitignored
  `sources/raw/`; read or grep, never execute; sha256 and access date recorded.
- **`na-workhorse` is busy with `ph2` until about 2026-10-16.** Nothing launches there
  before the `ph2` collect task is done. Design, pre-register and smoke-test locally (one
  process, under 500 MB, under a minute); the run is a separate later task. At launch: at
  most 11 busy processes across all agents, RAM under ~12 GB, `uptime` first, `< /dev/null`,
  md5s in `raw/<x>.host`. Never commit or push from workhorse.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Report format (at most 300 words)

Commits (pre-registration first); the h interval from route (a) and from route (b), each
with its source and its mapping in one line; whether they agree; the band-to-verdict table
and which row the result lands in for H, H5 and H8; what stayed unsourced; failures; next
step.
