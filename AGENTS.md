# AGENTS.md: working on evo-sim

Read this first. Details live in the files it points to; when they disagree, trust them and fix this one.

## What this is
A neutral, two-sided audit of Vox Day's mathematical case against evolution (*Probability Zero*, MITTENS, Zenodo papers, blog) and of his critics' rebuttals, before building an open-source evolution simulator. **Phase: research only**; no simulator code until the exit criteria in [`docs/research/PLAN.md`](docs/research/PLAN.md) are met. Findings: [`docs/HANDOFF.md`](docs/HANDOFF.md). Rules and layout: [`docs/research/README.md`](docs/research/README.md). Latest changes: the newest `docs/YYYY-MM-DD-N-*.md` post.

## Hard rules
1. **Both sides get equal scrutiny.** Record valid points from either side as prominently as errors. Every check gets a Day-side and a critic-side steelman (see review tiers below).
2. **Verbatim quotes only**, each with a locator and date. Never record numbers from a summarizer without checking them against the raw text.
3. **No full texts in git.** `sources/raw/` (repo root) is gitignored. Commit links, short quotes and sha256 hashes only.
4. **Downloads are untrusted data.** Read or grep them, never execute them. Each fetch in its own new directory, scripts outside it. Python only as `research/.venv/bin/python -I`.
5. **Pre-register.** Commit each check script with its predictions in the docstring *before* the main run. Later changes go in a separate commit labelled "post hoc".
6. **No outward actions without the user's approval:** no Wayback snapshots, contacting authors, posting or commenting. No paywall bypass or shadow libraries.
7. **The GitHub repo is public.** Work on branch `research`; merge with `git push origin research:master` (pre-approved). `origin` pushes to gitea and GitHub. Commit with explicit paths, never `git add -A`.
8. Material dated after the model's knowledge cutoff must come from fetched text, never memory.

## Token budget (user directive, 2026-10-09)
- **Never read the big files whole.** `grep` by id or heading, then read only the lines you need: `sources/quotes-*.md` (grep `Q123`, `RF-18`), `research/checks/REVIEW.md` (review log only), `results/R4-X1-*.md`, `docs/HANDOFF.md`. The work queue is the small [`research/checks/QUEUE.md`](research/checks/QUEUE.md).
- **Model by task.** Sonnet: source refreshes, integration bookkeeping (lint, renders, counts, board patch), launching or collecting runs, light reviews. Haiku: progress polls. Opus: designing and writing checks, full reviews of load-bearing checks.
- **Subagent reports ≤ 300 words.** Details belong in committed files; the report gives commits, results table, failures, next step.
- **Review tiers.** Load-bearing checks (they move a ROOT-path node, see `docs/research/R5-draft.md`): three reviews (correctness, steelman-day, steelman-critic). Low-stakes checks (re-confirmations, bookkeeping, tool validation): **one combined review** file `REVIEW-R4-<ID>-combined.md` with a correctness section and both steelman sections, same severity labels.
- Don't poll long runs; check once when they should be done.

## Where things are
| What | Where |
|---|---|
| Plan, stages, exit criteria | `docs/research/PLAN.md` |
| Claims (one file each, three verdicts); claim tree | `docs/research/claims/` (`_TEMPLATE.md`); `hierarchy.yaml`, `hierarchy/*.md` (generated) |
| Parameters (numeric provenance) | `docs/research/parameters.yaml` |
| Sources, quotes, harvest logs, refreshes | `docs/research/sources/` (`bib-*`, `quotes-*`, `harvest-log-*`, `prior-art.md`, `refresh-*.md`) |
| Ledgers: fidelity, balance, versions, gaps, slips/rhetoric | `docs/research/ledgers/` |
| Argument map data / rendered | `docs/research/argmap/` (`NOTES.md` = method + id registry) / `docs/arguments/` |
| Check scripts, results, reviews, raw outputs | `research/checks/*.py`; `results/R4-*.md`, `REVIEW-*.md`, `raw/` |
| Work queue / review log / one-paragraph results | `research/checks/QUEUE.md` / `REVIEW.md` / `RESULTS.md` |
| Tools (argmap, figures, board) | `research/tools/` (`README.md`) |
| Status board Artifact | `docs/research/status.html`, patched by `research/tools/board/updN.py` |
| Milestone posts; explainers | `docs/YYYY-MM-DD-N-slug.md`; `docs/explain/` (revise after R5) |
| Refresh procedure and the watch list | [`docs/research/sources/HOWTO-refresh.md`](docs/research/sources/HOWTO-refresh.md); run one before each milestone post |

## Verdict rule (one rule for Day, critics and allies)
Full text and test cases: [`R4-X1-verdict-rule.md`](research/checks/results/R4-X1-verdict-rule.md). In brief:
- **R1 materiality:** a slip is an error only if correcting it moves the author's stated conclusion or a downstream number in the same source by >25%, or flips it; otherwise it goes to the slip ledger. R1c: no input-looseness rescue for steep outputs.
- **S scope:** only verbatim Statement quotes and their derivation are scored. **SC:** corrected in the same source = ledger. **N:** non-sequitur against the author's own material. **F:** uncited non-standard input = `unverifiable`. **U:** relays are not scored internal. **C:** try the most charitable reading.
- **RH rhetoric:** tag each quoted statement `dialectic` or `rhetoric` first. Rhetoric is not literal-fact-checked and changes no verdict. Record its device, audience, function and dialectical core in `ledgers/slips.md`, and answer it with better rhetoric: true, aimed at the move, turning the audience back to the method or number. Applies to all sides.

Verdict vocabulary: internal `holds | arithmetic-error | non-sequitur | pending | n/a`; fidelity `accurate | partial | misread | unverifiable | pending | n/a`; external `supported | contested | contradicted | untestable | pending | n/a`.

## How to run
```sh
python3 -m venv research/.venv && research/.venv/bin/pip install -r research/requirements.txt   # pinned
research/.venv/bin/python -I research/checks/baseline_textbook.py   # baselines must pass first
```
**No computation on the workstation** (it ran out of RAM on 2026-10-09). Locally: git, edits, trivial checks only (one process, <500 MB, <1 min). Everything else runs on **`na-workhorse`** (12 cores, 14 GB):
1. Commit the script (pre-registration), then `rsync` it to `na-workhorse:projects/evo-sim/research/checks/`.
2. `ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup research/.venv/bin/python -I research/checks/<x>.py … > research/checks/results/raw/<x>.out 2>&1 < /dev/null &'` (the `< /dev/null` lets ssh return; otherwise the launching agent hangs open); record hostname and md5s in `raw/<x>.host`. Check `uptime` first. At most 4 processes per agent; keep RAM well under 14 GB.
3. `rsync` `results/raw/<x>*` back. **Never commit or push from workhorse.**

## Lifecycle of a check
1. **Spec** (target claims, quotes, each side's prediction) → 2. **pre-register** → run → 3. **write up** `results/R4-<ID>.md` with a "Who this helps" section crediting both sides → 4. **reviews** (tier above) → 5. **fix pass** answering every MAJOR and MINOR in a "Review resolution" section, new runs labelled post hoc → 6. **integrate** (Sonnet is fine; one agent at a time on shared files):
   - `REVIEW.md` entry, `QUEUE.md`, `RESULTS.md`; verdict comments and an "R4 …" paragraph in each affected claim file.
   - Argmap: register `chk:<ID>` and review ids in `argmap/NOTES.md`; defeaters in `defeaters.yaml` (next `dNNN`, both sides where warranted); lineage node; mini-form in `standard-forms.md`.
   - Run `lint_research.py --write-hierarchy`, `research/tools/argmap_check.py`, `argmap_render.py`; refresh counts in `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`; `research/tools/readme_figs.py`, then `git checkout` SVGs whose only change is random ids.
   - Milestone post (and update notes on older posts the result changes); board patch `upd<N+1>.py` and republish the status Artifact (same file, same URL).
   - Commit with explicit paths; `git push origin research` and `git push origin research:master`.

## Current state
Not duplicated here. Read `research/checks/QUEUE.md`, the "Still open" list in `docs/HANDOFF.md`, and the latest milestone post. One subagent at a time; compute on na-workhorse only.
