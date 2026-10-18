# Research tooling (throwaway, kept for provenance)

These scripts produced the committed research files. They were written during the 2026-10-07/08 session in a scratch directory and moved here so that every generated number and file can be traced back to the code that made it. They are research artefacts, not simulator product code.

| Directory | What it holds |
|---|---|
| `harvest/` | Corpus fetching and conversion (blog, Zenodo, PMC, video captions), quote extraction and verification, bibliography and opponent-profile generators |
| `harvest/data/` | URL lists, crawl classification, sha256 hashes, blog/Zenodo index tables (metadata only, no full texts) |
| `claims/` | R2 claim-file generators (`p1`–`p7`, `gen_*`, and the `s/` package that writes `docs/research/claims/`) |
| `board/` | Scripts that patch `docs/research/status.html` node by node. `board/scope_guard.py` is the publication gate, not a patcher: it exits 1 where the page states a scoped verdict with no scope, or states a value the audit has pulled back to `pending`, and prints REVIEW lines where the page paraphrases a scope instead of quoting the ruled line (B-R21, re-cut by B-R28). Run it before every publication |
| `argmap_check.py` | Checks `docs/research/argmap/` (verbatim lineage quotes, registered ids, dates, standard-form targets, mechanical `counter` lists, coverage of hierarchy attack edges) |
| `argmap_render.py` | Draws `docs/img/argmap/genealogy.svg` and writes `docs/arguments/defeaters.md` (objection graph per branch, grounded semantics read three ways) |
| `prereg_status.py` | Writes `research/checks/PREREG-STATUS.md` from `git log` and the local `origin/research` reflog (descriptive; reads history only) |
| `method_audit_stats.py` | Read-only counts over the claim files used in `docs/research/criticality/METHOD-AUDIT-proposals.md` (holds on unchecked files, seeded sample of `contested`) |
| `grade_certainty.py` | Read-only: the seeded, stratified sample of external verdicts rated in `docs/research/criticality/grade-certainty-2026-10-12.md`, and (`count`) a recomputation of every certainty in its table from the code column, with the aggregates |
| `readme_figs.py`, `eli_figs.py` | README and explainer figures, from committed check outputs only |

Ad hoc arithmetic checks are in `research/checks/adhoc/`. Raw run outputs are in `research/checks/results/raw/`.

## Running
Many of these scripts read full texts that are **not** in git (copyright; see the root `.gitignore`). To rerun them:
1. Recreate a work directory holding the raw downloads (`txt/`, `src/`, `w/`, `dl/`, `ceh/`, `qrows.json`).
2. Point `EVO_WORK` at it. It defaults to `./work`, which is gitignored.

Run every script with `research/.venv/bin/python -I`. Downloads are untrusted data: never execute them.
