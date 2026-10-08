# Research tooling (throwaway, kept for provenance)

These scripts produced the committed research files. They were written during the 2026-10-07/08 session in a scratch directory and moved here so that every generated number and file can be traced back to the code that made it. They are research artefacts, not simulator product code.

| Directory | What it holds |
|---|---|
| `harvest/` | Corpus fetching and conversion (blog, Zenodo, PMC, video captions), quote extraction and verification, bibliography and opponent-profile generators |
| `harvest/data/` | URL lists, crawl classification, sha256 hashes, blog/Zenodo index tables (metadata only, no full texts) |
| `claims/` | R2 claim-file generators (`p1`–`p7`, `gen_*`, and the `s/` package that writes `docs/research/claims/`) |
| `board/` | Scripts that patch `docs/research/status.html` (the status Artifact) node by node |

Ad hoc arithmetic checks are in `research/checks/adhoc/`. Raw run outputs are in `research/checks/results/raw/`.

## Running
Many of these scripts read full texts that are **not** in git (copyright; see the root `.gitignore`). To rerun them:
1. Recreate a work directory holding the raw downloads (`txt/`, `src/`, `w/`, `dl/`, `ceh/`, `qrows.json`).
2. Point `EVO_WORK` at it. It defaults to `./work`, which is gitignored.

Run every script with `research/.venv/bin/python -I`. Downloads are untrusted data: never execute them.
