---
name: review-correctness
description: Correctness review of an evo-sim check write-up: recompute numbers from raw outputs, check every hit/miss call and verdict move against the registration. Run as the reviewer agent.
---
# Correctness review

You write one review file, `research/checks/results/REVIEW-R4-<ID>-correctness.md`, and edit nothing else.

Recompute; do not trust. Check every number against the raw json, every hit or miss against the exact registered wording, every post hoc label, the run-integrity facts (hashes, commit order against the host record) and whether each proposed verdict move is exactly what the registration licenses. Read the code path behind any surprising number before accepting the write-up's explanation of it. Findings are numbered and labelled BLOCKER / MAJOR / MINOR / NOTE, each with evidence and an exact fix. Close with counts and a list of wrong numbers (old -> right). You were not told what the lead suspects; if your brief lists suspicions, treat them as a starting list, not the scope.
