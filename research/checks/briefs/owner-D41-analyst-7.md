# owner-D41-analyst-7: review of Gutsick Gibbon with Zach Hancock (GG-1), window 1: the MITTENS maths segment (item 7 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 7 ("split into time windows, one review per window"; owner approved the series "in this order"). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 7, window 1. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Source
- **GG-1:** Gutsick Gibbon (Erika) with Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution", YouTube, 2026-10-03, 3:30:28, https://www.youtube.com/watch?v=_Vu0ZVVjwHc, `bib-critics.md` row GG-1 (sha256 `c1adc852…`).
- **This window: t=01:28:00 to 02:05:00**, the maths segment named in the bib row. Quotes on file in it: GG-01..GG-13, GG-24, GG-25 (`quotes-critics.md`, grep the ids). Already mapped in part in `docs/research/math/sources/branch-A.md`, `branch-G.md`, `kittens-re2.md`, `nesslig20-ps1.md` and claim files A3x, A5c, B5c, G2c (Hancock's 76.8 per generation, bp vs events, no-variation prediction). Link those, don't redo them. The other windows (00:00 to 01:28, 02:05 to end) are later items; touch them only to cite a locator.
- **Relay (rule U):** the segment answers Will Duffy's presentation of MITTENS 2.x (252,000 generations, 1,400 per fixation, 205M), not Day directly. Check each attacked line against Day's own text (`quotes-day.md`, the library's MITTENS sources). Where Duffy's relay and Day differ, the critique lands on the relay, and the page says so. The JG-1 review (`docs/reviews/2026-11-26-jan-ghijselen-duffy-math.md`) left open whether Duffy presented the Appendix A serial chain; answer it from this window if the captions show it, otherwise say "not shown in the captions".
- **Whiteboard:** the bib row says the whiteboard is not captured by the captions. Score only what is spoken. Where a number is written but not said, say so; don't reconstruct it.
- **Held copy:** none on disk. Make one read-only fetch with the pinned `research/.venv/bin/yt-dlp` (no video download: `--skip-download --write-auto-subs --sub-langs en --write-info-json`; no comments) into a new directory `sources/raw/gg-1-2026-11-26/`, record sha256s. Auto-captions can differ from the filed copy; the test is that the window's quotes on file are present (allowing caption chunk boundaries; quote the fetched wording and note any difference). If the fetch fails or a quote is missing, report and stop.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/gutsick-gibbon-gg1-w1.md` with skill `deref-source`: each maths statement in the window verbatim with `t=` locator → argument steps → `M-` objects. **Reuse first** (serial vs aggregate M-706/M-918, latency vs rate M-115, 4Nₑ lag M-914, 180 arithmetic M-711/M-110, bp vs events M-917, LTEE transfer M-007 and M-916). Only maths not in the library becomes a new object (next free id after M-918) with a record `records/M-NNN.py` + `.json` asserting every number the page states. Don't create an object for its own sake.
2. **Review page** `docs/reviews/2026-11-26-gutsick-gibbon-hancock-w1-maths.md` (actual date if later) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides), what fails, slips (R1 with the check shown; caption garbles are transcription, not the speaker's slip), logic (N/U), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; the title's "AI-Generated" is tagged, not fact-checked), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line. Say on the page that it covers one window of a 3.5 h video.
3. **One link** in `docs/index.html`: one `<li>` after the Ghijselen entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-gutsick-gibbon-hancock-w1-maths.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/gutsick-gibbon-gg1-w1.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (one line: new fetch hashes), `docs/research/math/people.yaml` (entries for Hancock / Gutsick Gibbon if missing). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or a quote on file is not in the captions (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
Other windows of GG-1; GG-4 and other videos; claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hashes and whether quotes match; relay calls (rule U), including whether Duffy presented the serial chain; new object ids with record sha256s, or "none"; objects reused; R1 results for any slips; claim-file candidates; lint and record-run output; next step.
