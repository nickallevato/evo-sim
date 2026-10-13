---
name: republish-board
description: Republish the evo-sim status board Artifact in place at its existing URL after a board patch. Use after research/tools/board/updN.py has been run and committed.
---
# Republish the status board (same file, same URL)

The board is `docs/research/status.html`, published privately as the Artifact "Probability Zero Audit": https://claude.ai/artifact/AsRA58LU6Uw174xPcUsdHL. The owner wants the same Artifact updated every time; never create a second one, never use `force`.

1. Confirm nothing published would be lost: the live page should equal the last committed version of the file before the new patch. `Artifact action=read url=<URL>` saves the live source locally; `diff <(tail -n +2 <saved copy>) <(git show <commit before patch>:docs/research/status.html)` should show only the hosting wrapper's closing lines.
2. The Artifact tool refuses to publish until every line of the saved live copy has been Read. That is about 50,000 tokens (two lines are long base64 data URIs). **Delegate it to a fresh `operator` agent** with these instructions: read the artifact; Read the saved copy completely in chunks of about 60 lines (limit 1 for any oversize line); Read `docs/research/status.html` completely; check it holds no credentials or private data; publish with `file_path`, `url` and a short `label`, passing no `icon`, `title`, `capabilities` or `force`; on refusal do what the refusal says and retry at most twice; report the version string.
3. The page stays private. Sharing is the owner's action.
4. Ask the publishing agent to list any stale numbers it noticed on the page; fix them in the next `updN.py`, not by hand.
