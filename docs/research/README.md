# Research: The Mathematical Case Against Evolution (Vox Day) and Its Critics

This is a neutral, two-sided audit of the mathematical claims in Vox Day's *Probability Zero* / MITTENS corpus and in the critiques written against it. The output is a sourced map of every claim, a numerical check of each equation, and a list of variables for a user-controllable simulator to be built later.

## Rules
1. **Three verdicts per claim:**
   - **(a) Internal validity:** does the conclusion follow from the author's own assumptions?
   - **(b) Model fidelity:** does the cited theory or paper actually say that?
   - **(c) External validity:** are the assumptions biologically realistic?
2. **Both sides get equal scrutiny.** Arithmetic, sources and assumptions are audited for critics and allies just as for Day. Valid points from either side are recorded as prominently as errors.
3. **Verbatim quotes only.** Each quote needs a locator (URL plus paragraph, page or equation) and a source date or version. A claim known only through an opponent's quotation is tagged `secondhand`.
4. **Pre-register predictions.** Before a check runs, its claim file states what each side's model predicts.
5. **Numeric provenance.** Every number comes from `parameters.yaml`, from a cited quote, or is marked `derived:` with its formula.
6. **No question-begging.**
   - Forward simulations decide disputes about equilibrium. The coalescent (msprime) is used only for baselines.
   - Scaling (shrinking N and raising μ with θ held fixed) is validated before it is relied on.
7. **No full texts in git.** `sources/raw/` is gitignored. The repo commits links, archive URLs, short quotes and sha256 hashes.

## Layout
| Path | Contents |
|---|---|
| `glossary.md` | Pinned definitions. Most disputes here turn on definitions. |
| `parameters.yaml` | Numeric inputs, per side and per source version |
| `hierarchy.yaml`, `hierarchy/*.md` | The claim tree, as machine-readable YAML and as per-branch Mermaid diagrams |
| `claims/<ID>-<slug>.md` | One file per claim (see `claims/_TEMPLATE.md`) |
| `sources/bibliography.md` | Every source, with its access status |
| `opponents/<name>.md` | Each critic or ally, with their arguments mapped to claim IDs |
| `ledgers/` | Citation fidelity, side-by-side balance, contradictions, version drift |
| `../../research/checks/` | Throwaway verification code and `REVIEW.md` |

## Status
| Stage | Status |
|---|---|
| R0 Scaffold | done |
| R1 Corpus harvest | **done** 2026-10-07: Day (154 posts, 32 Zenodo files, 75 quotes), literature (37 sources, 75+ quotes), critics/allies (48 rows, 132 quotes, 23 profiles) |
| R2 Claim extraction | **done** 2026-10-07: 193 claims (day 107, critic 46, ally 16, literature 24); lint clean |
| R3 Hierarchy | generated from claims (`hierarchy.yaml`, `hierarchy/branch-*.md`); 30 load-bearing nodes |
| R4 Math resolution | in progress: B0, B0.4, B1, B1b, B2a, B3, F1 done + reviewed (reviews #1–#3); B1c, B4a, B3b/B3c, C1, C1b, H, H2-hard, C2, F2, A-sim done + reviewed (review #4, 2026-10-08; 40 claim files updated). Remaining: E checks, G1/G3 (specific-vs-any), D sims, C1b call-depth follow-up, H at realistic human R with hard-selected load (plus T50 CIs), Yoo μ rescaling |
| R5 Synthesis | — |

## Running checks
```
python3 -m venv research/.venv && research/.venv/bin/pip install -r research/requirements.txt
research/.venv/bin/python -I research/checks/<file>.py
```
