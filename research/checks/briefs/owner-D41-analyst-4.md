# owner-D41-analyst-4: review of Nesslig20, "Response to Will Duffy, Part I" (PS-1) (item 4 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 4 (owner approved the series "in this order"). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 4. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Source
- **PS-1:** Nesslig20, "Response to Will Duffy / PART I - Population Genetics", Peaceful Science topic 18094, 2026-10-05, `bib-critics.md` row PS-1 (sha256 `9912398e…` for `ps-topic-18094.json`; OP + 4 replies). Quotes on file: PS-01..PS-05 (`quotes-critics.md`). PS-05 relays Martin Neukamm: credit it to him.
- **Rule U:** the post answers Will Duffy's presentation of MITTENS 2.x, not Day directly. Where it attacks a Duffy statement, say whether Day's own text makes the same claim (cite the Day quote) or not. A Duffy statement Day never made is not scored against Day, and a non-sequitur against Duffy alone is not a point against MITTENS.
- **Replies:** the four replies in the topic are in scope where they contain maths or answer the post.
- **Held copy:** none on disk. Make one read-only fetch of `https://discourse.peacefulscience.org/t/18094.json` (and `/posts.json?post_ids[]=…` if the stream is truncated) into a new directory `sources/raw/ps-18094-2026-11-26/`, record sha256s. A hash difference from the bib row is acceptable if the post was not edited; the test is that every quote on file (PS-01..PS-05) is an exact substring of the fetched text. If the post shows an edit after 2026-10-05, record the version and note it on the page. If a quote is missing or the fetch fails, report and stop.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/nesslig20-ps1.md` with skill `deref-source`: each statement verbatim with locator → argument steps → `M-` objects. **Reuse first:** the branch-B and branch-H maps already hold PS-01, PS-02 and PS-04 (claim files B5e, H6; objects M-801 and those listed in `branch-B.md` rows B5e q1/q2), the 4Nₑ lag M-914, the neutral-count and 3:1 neutral-share work in M-915, A3x / GAP-07b for the indel size spectrum (PS-03, PS-05). Settled points in the McCarthy item-1 and item-2 pages are linked, not repeated. Only maths not in the library becomes a new object (next free id after M-916) with a record `records/M-NNN.py` + `.json` asserting every number the page states.
2. **Review page** `docs/reviews/2026-11-26-nesslig20-response-to-duffy-part-1.md` (actual date if later) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides), what fails, slips (R1 with the check shown; the known one is PS-01: 75 is a de novo count per diploid offspring, stated as per haploid genome, so check what it does to the 37.8 million of PS-02 and whether that crosses 25 %), logic (N/U, hidden premises), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; same standard for the Duffy/Day lines quoted and for repliers), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line.
3. **One link** in `docs/index.html`: one `<li>` after the KITTENS entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-nesslig20-response-to-duffy-part-1.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/nesslig20-ps1.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (one line: new fetch hash). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or a quote on file is not in the text (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
Part II or other Nesslig20 posts (PS-2 is not MITTENS maths); Duffy's presentation itself beyond the lines the post quotes; claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hashes and whether quotes match; new object ids with record sha256s; objects reused; R1 results for any slips; rule-U calls (which attacked lines are Day's own); claim-file candidates; lint and record-run output; next step.
