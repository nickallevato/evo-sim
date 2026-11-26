# owner-D41-analyst-8: review of Gutsick Gibbon with Zach Hancock (GG-1), window 2: t=00:00 to 01:28 (item 7 of the D-41 series, second window)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 7 ("split into time windows, one review per window"; owner approved the series "in this order"). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 7, window 2. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Source
- **GG-1:** Gutsick Gibbon (Erika) with Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution", YouTube, 2026-10-03, 3:30:28, https://www.youtube.com/watch?v=_Vu0ZVVjwHc, `bib-critics.md` row GG-1 (sha256 `c1adc852…`).
- **This window: t=00:00:00 to 01:28:00**, everything before the maths segment. Quotes on file in it: GG-14, 15, 17-23, 32-36, 39-48 (`quotes-critics.md`, grep the ids). Window 1 (01:28 to 02:05) is done: map `docs/research/math/sources/gutsick-gibbon-gg1-w1.md`, review `docs/reviews/2026-11-26-gutsick-gibbon-hancock-w1-maths.md`, record M-919. Link them; don't redo them. Window 3 (02:05 to end) is a later item; touch it only to cite a locator.
- **Expect less maths than window 1.** Map only statements with a number, a formula, or a quantitative claim about MITTENS, *Probability Zero* or Day's sources. If the window has no maths beyond what the library holds, say so: no new object is the right result. Non-numeric arguments (credentials, AI authorship, publishing, the book's citations) go in the logic and rhetoric sections only where they bear on the MITTENS case; otherwise one line each.
- **Relay (rule U):** where the speakers attack Day through Duffy's slides or anyone else's relay, check the line against Day's own text (`quotes-day.md`, the library's MITTENS sources) and say on which text the critique lands. Where they quote Day directly, check the quote.
- **Whiteboard / screen:** score only what is spoken. Where a number is shown but not said, say so; don't reconstruct it.
- **Held copy:** reuse `sources/raw/gg-1-2026-11-26/` from window 1 (sha256s in the window-1 map, line 3). Re-hash before use; if a hash differs, report and stop. No new fetch. Auto-caption wording may differ from the quotes on file; the test is that each window quote is present (allowing chunk boundaries and `[hh:mm:ss]` markers in `transcript.txt`); quote the fetched wording and note any difference. If a quote on file is missing, report and stop.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/gutsick-gibbon-gg1-w2.md` with skill `deref-source`: each maths statement in the window verbatim with `t=` locator → argument steps → `M-` objects. **Reuse first** (window 1's M-919 and the objects it reuses: M-001, M-007, M-012, M-115, M-209, M-212, M-213, M-706, M-711, M-713, M-914, M-916, M-917, M-918). Only maths not in the library becomes a new object (next free id after M-919) with a record `records/M-NNN.py` + `.json` asserting every number the page states. Don't create an object for its own sake.
2. **Review page** `docs/reviews/<date>-gutsick-gibbon-hancock-w2-opening.md` (actual date) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides), what fails, slips (R1 with the check shown; caption garbles are transcription, not the speaker's slip), logic (N/U), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; the title's "AI-Generated" is tagged, not fact-checked), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line. Say on the page that it covers one window of a 3.5 h video and link the window-1 page.
3. **One link** in `docs/index.html`: one `<li>` after the GG-1 window 1 entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-gutsick-gibbon-hancock-w2-opening.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/gutsick-gibbon-gg1-w2.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (GG-1 row only, if a note is needed), `docs/research/math/people.yaml` (entries for Hancock / Gutsick Gibbon if missing). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR a held-copy hash differs or a quote on file is not in the captions (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
Windows 1 and 3 of GG-1; GG-4 and other videos; claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; held-copy hashes and whether quotes match; relay calls (rule U); new object ids with record sha256s, or "none"; objects reused; R1 results for any slips; claim-file candidates; lint and record-run output; next step.
