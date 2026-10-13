---
name: close-batch
description: Close an evo-sim batch after its checks are integrated: source refresh, criticality pass, milestone post, bookkeeping, board patch and republish, merge to master.
---
# Close a batch

Order matters; steps 1 and 2 can run in parallel.

1. **Source refresh** (`operator` + skill `source-refresh`): `docs/research/sources/HOWTO-refresh.md`; output `refresh-YYYY-MM-DD.md`. If a critic or author reply exists and is unread, the post must say so.
2. **Criticality pass** (`reviewer` at effort xhigh + skill `criticality-pass`, a fresh instance that did none of the batch's work): `docs/research/criticality/README.md`, "Standing procedure". Tell it the process facts as well as the artefacts, including your own shortcuts.
3. **Bookkeeping** (`operator`): the pass's integrator fixes; queue the refresh follow-ups; ROADMAP statuses; board patch `research/tools/board/upd<N+1>.py` (runs from `docs/research/`, asserts its anchors, parses counts from the files of record).
4. **Milestone post** (`analyst` + skill `milestone-post`), in parallel with 3: new `docs/YYYY-MM-DD-N-slug.md` plus update notes on older posts. Afterwards correct its "Next" list for anything step 3 already did.
5. **Republish the board**: the `republish-board` skill.
6. `git push origin research` and `git push origin research:master` (pre-approved). Rule or vocabulary changes proposed by the pass are never applied here; they wait for the owner under the freeze procedure.
7. Tell the owner: what changed, every verdict field that moved, the audit's own errors, open owner decisions (new `O-` ids), what is still running and when it is due.
