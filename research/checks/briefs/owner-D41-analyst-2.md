# owner-D41-analyst-2: review of McCarthy MC-2 + MC-2c (item 2 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 2 and §8 (revision 4, accepted 2026-11-26). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 2. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Sources
- **MC-2:** McCarthy, "Vox Day Responds" (free repost, 2026-09-17; paid original 2026-02-03 is MC-2p, preview only, out of scope), `bib-critics.md` row MC-2 (URL, sha256 `78bf1ace…`). Quotes on file: MC-08, MC-09, MC-10 (`quotes-critics.md` §MC2).
- **MC-2c:** McCarthy's own replies in that post's comment thread, `bib-critics.md` row "MC-1c, MC-2c"; RF-6 (comment 340149310) and the Matev comments MV (345248135, 340270022) sit in this thread.
- **Held copy:** item 1 already fetched the MC-2 thread read-only: `sources/raw/mccarthy-mc1-2026-11-26/comments-vdr.json` (sha256 `4bdd3432…`) and `comments-vdr.txt`. Reuse it; check its hash first. The MC-2 **post body** is not held: make one read-only fetch (Substack public API) into a new directory `sources/raw/mccarthy-mc2-2026-11-26/`, record its sha256, and handle a hash difference from the bib row as item 1 did (if every quote on file is an exact substring and `updated_at` predates 2026-10-07, say the difference is metadata; if any quote is missing, report and stop). Every quote on the page is checked against these copies.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/mccarthy-mc2.md` with skill `deref-source`: each statement verbatim with locator → argument steps → `M-` objects. **Reuse first:** M-914 and `mccarthy-mc1.md` (4Nₑ lag, RF-6/RF-7), M-007 (E. coli/human genome and supply ratios; check whether it covers the 410 Mb figure), the expected-neutral-fixations object (~l.436), specific-vs-any (~l.1044). In scope: Day's 4Nₑ time-component reply (quoted secondhand by McCarthy, so rule U: score McCarthy's relay, not Day), the time-adjusted 360,000 − 40,000 generations (MC-09), the 410 Mb figure, MC-10's 3 % deleterious against Day's "3x more harmful than neutral", and MC-08's concurrent fixation. Only maths not in the library becomes a new object (next id after M-914) with a record `records/M-NNN.py` + `.json` asserting every number the page states. Look up a source for the 3 % and the 3:1 ratio only if one is cited in the text; otherwise mark both uncited (rule F) and say neither side supplies one.
2. **Review page** `docs/reviews/2026-11-26-dennis-mccarthy-vox-day-responds.md` (use the actual date if later) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides), what fails, slips (R1 with the check shown), logic (N/U, hidden premises), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; same standard for Day's quoted lines and for commenters McCarthy answers), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line. Link the item-1 page where a point was already settled there rather than repeating it.
3. **One link** in `docs/index.html`: one `<li>` after the McCarthy item-1 entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-dennis-mccarthy-vox-day-responds.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/mccarthy-mc2.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (one line: new fetch hash). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or a quote on file is not in the text (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
Speciation, fossil and biogeography sections (no maths); MC-2p and paywalled MC-5/MC-6; claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hashes and whether they match; new object ids with record sha256s; objects reused; R1 results for any slips; claim-file candidates; lint and record-run output; next step.
