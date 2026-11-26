# owner-D41-analyst-3: review of KITTENS (RE-2) (item 3 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 3 (owner approved the series "in this order"). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 3. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Source
- **RE-2:** Sparky_6_4 (self-disclosed AI-assisted, "Clauwd Meowgorithm"), "KITTENS: rebuttal to Vox Day's MITTENS 3.0", r/DebateEvolution post 1wxgsjm, 2026-10-04 (a twin post 1wxgamf has the same title), `bib-critics.md` row RE-2 (sha256 `46dfb6b8…` for `arctic-tree-1wxgsjm.json`). Quotes on file: RE-08..RE-11 (`quotes-critics.md`). The post self-discloses AI use and from-memory citations: say so on the page, and treat each uncited input under rule F.
- **Comments:** the replies in the 1wxgsjm thread, including any by Day or by defenders of MITTENS, are in scope where they contain maths or answer the post.
- **Held copy:** none. The original `sources/raw/critics/` copy is gone. Make one read-only fetch (Arctic Shift, PullPush fallback; see `docs/research/sources/HOWTO-refresh.md` §6) of the post and its comment tree into a new directory `sources/raw/kittens-re2-2026-11-26/`, record sha256s. A hash difference from the bib row is expected (different API wrapper); the test is that every quote on file (RE-08..RE-11) is an exact substring of the fetched text. If any quote is missing, or the fetch fails on every endpoint, report and stop.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/kittens-re2.md` with skill `deref-source`: each statement verbatim with locator → argument steps → `M-` objects. **Reuse first:** M-006 (LTEE ceiling, 93,659 supply ratio), M-007 (supply arithmetic and the KITTENS decomposition 93,659 × 11.714 = 1,097,143 against 1,075,000), M-008 (achievable 17.9e6 against 17.5e6), the claim files A5b (KITTENS decomposition, with the audit's sublinear-scaling sensitivity from Day's mutator data A5d), A5c (neutral supply 9.7M) and A2e. Only maths not in the library becomes a new object (next free id after M-915) with a record `records/M-NNN.py` + `.json` asserting every number the page states.
2. **Review page** `docs/reviews/2026-11-26-sparky-kittens-mittens-3.md` (actual date if later) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides), what fails, slips (R1 with the check shown), logic (N/U, hidden premises; the linear-scaling assumption KITTENS itself states at RE-09 is the obvious one), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; same standard for MITTENS lines quoted and for commenters), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line. Link the McCarthy item-1 and item-2 pages where a point was already settled there rather than repeating it.
3. **One link** in `docs/index.html`: one `<li>` after the McCarthy item-2 entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-sparky-kittens-mittens-3.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/kittens-re2.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (one line: new fetch hash). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or a quote on file is not in the text (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
The other Reddit threads (RE-1, item 9); claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hashes and whether quotes match; new object ids with record sha256s; objects reused; R1 results for any slips; claim-file candidates; lint and record-run output; next step.
