# Brief: publish the EVOA-102 review of Paul's "rate equations" post (operator-1)

Owner request, EVOA-102 comment 2a0f690e (2026-11-26): "get it publishjed to the github site or whatever". No D- id; this is a one-off owner request, not an exit-gap item.

**Gap item:** none (owner request). No claim, verdict or status field moves.

**Deliverable:** one new page, `docs/reviews/2026-11-26-paul-rimmer-rate-equations.md`, holding the EVOA-102 `review` document (revision `9e88e413-4299-42e9-90ef-73d75f249a7a`, `GET /api/issues/0da1bb7a-b2da-4902-9cdb-35c50fde02ba/documents/review`), plus one link to it from `docs/index.html`, published to `master`.
- Copy the document body as is. Add only, at the top under the title, one note: "Lead review written at the owner's request (EVOA-102). Not an audit check: no claim file, verdict or count changed. Scope: the owner asked for the errors from Day's side; §5 gives the critic-side steelman at equal depth (hard rule 1)."
- Keep the source line (URL, date, sha256). The local path `sources/raw/...` stays as text only; commit nothing from `sources/raw/`.
- `docs/` has `.nojekyll`, so Pages does not render `.md`. Link the way `index.html` links HANDOFF.md: `https://github.com/nickallevato/evo-sim/blob/master/docs/reviews/2026-11-26-paul-rimmer-rate-equations.md`. Add one `<li>` after the Math ledger item: link text "Review: Paul's \"rate equations\" post (2026-11-26)", span "Where the maths in an argument against MITTENS holds and where it fails, with both sides' cases."

**Allowed paths:** `docs/reviews/2026-11-26-paul-rimmer-rate-equations.md` (new), `docs/index.html`. Nothing else.

**Skill:** none needed; plain edit, commit, push.

**Budget:** 1 commit (2 at most if a fix is needed). No fix passes.

**Stop when:** the commit is on `research` and on `master` (`git push origin research` then `git push origin research:master`), and
- `https://github.com/nickallevato/evo-sim/blob/master/docs/reviews/2026-11-26-paul-rimmer-rate-equations.md` returns 200, and
- `https://nickallevato.github.io/evo-sim/` shows the new link (Pages can take a few minutes; check once after ~3 min, then report).
Also stop if the document fetch fails or the body differs from the named revision (report it, don't rewrite the review), or if the work would touch any other path.

**Not in scope:** harvest-log entries, quotes files, source maps, people pages (generated; do not edit), argmap, board, milestone post, claim files. Ideas go in one line in the report.

**Commit:** explicit paths only, never `git add -A`. Message body cites the owner comment id above. Trailer `Gap: owner` plus the attribution lines your issue gives you.

**Report (≤ 150 words):** commit hash, `git show --stat`, the two URL checks with status codes.
