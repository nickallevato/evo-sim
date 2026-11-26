# owner-D41-analyst-6: review of Ghijselen, "Will Duffy's math on Gutsick Gibbon's channel." (JG-1) (item 6 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 6 (owner approved the series "in this order"). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 6. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Source
- **JG-1:** Jan Ghijselen (@DeDzjang), "Will Duffy's math on Gutsick Gibbon's channel.", YouTube, 2026-09-28, 4:53, https://www.youtube.com/watch?v=nTVRiEcswI8, `bib-critics.md` row JG-1 (sha256 `2a3cd824…`). Quotes on file: DZ-01..DZ-03 (`quotes-critics.md`, YT-nTVRiEcswI8 section). Already mapped in `docs/research/math/sources/branch-G.md` (G2a q1, G2b q2 → M-115, M-706, M-711, M-110).
- **Relay (rule U):** the video answers Will Duffy's presentation of MITTENS (252,000 / 1,400 = 180), not Day directly. Check each attacked line against Day's own text (`quotes-day.md`, the MITTENS sources already in the library); where Duffy's relay and Day differ, the critique lands on the relay, and the page says so.
- **Held copy:** none on disk. Make one read-only fetch with the pinned `research/.venv/bin/yt-dlp` (no video download: `--skip-download --write-auto-subs --sub-langs en --write-info-json`; comments only if needed for the author's own replies, capped) into a new directory `sources/raw/jg-1-2026-11-26/`, record sha256s. Auto-captions can differ from the filed copy (HOWTO-refresh, "Pin the harvest tool"); the test is that DZ-01..DZ-03 are present in the captions (allowing the caption chunk boundaries; quote the fetched wording and note any difference). If the fetch fails or a quote is missing, report and stop.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/ghijselen-jg1.md` with skill `deref-source`: each statement verbatim with `t=` locator → argument steps → `M-` objects. **Reuse first:** serial vs aggregate is M-706 (with G2a), fixation latency vs rate M-115, the 4Nₑ lag M-914, the 180 arithmetic M-711 / M-110. Link settled points, don't repeat them. Only maths not in the library becomes a new object (next free id after M-917) with a record `records/M-NNN.py` + `.json` asserting every number the page states (e.g. the marathon figures, 60,000 × 4 h = 240,000 h ≈ 27.4 years, if not already asserted). Don't create an object for its own sake.
2. **Review page** `docs/reviews/2026-11-26-jan-ghijselen-duffy-math.md` (actual date if later) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides), what fails, slips (R1 with the check shown; auto-caption garbles such as "times 1,000 400" are transcription, not the speaker's slip), logic (N/U; in particular whether the marathon analogy fits the G_f = T_obs / n_obs aggregate rate or only a serial reading, M-706, and whether Day's own text uses the serial reading), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; the "math teacher" credential DZ-03 is tagged, not fact-checked), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line.
3. **One link** in `docs/index.html`: one `<li>` after the Bowers entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-jan-ghijselen-duffy-math.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/ghijselen-jg1.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (one line: new fetch hashes), `docs/research/math/people.yaml` (one entry for Ghijselen if missing). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers (or, if the page has fewer, every number) recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or a quote on file is not in the captions (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
Other Ghijselen videos; Duffy's original presentation beyond what the video shows (GG-1 is item 7); claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hashes and whether quotes match; relay calls (rule U); new object ids with record sha256s, or "none"; objects reused; R1 results for any slips; claim-file candidates; lint and record-run output; next step.
