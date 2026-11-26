# owner-D41-analyst-5: review of Bowers, "A Critical Review of Probability Zero", with Day's reply (JB-1) (item 5 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 5 (owner approved the series "in this order"). Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 5. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Source
- **JB-1:** Joe Bowers, "A Critical Review of Probability Zero", known only through Day's repost with his point-by-point reply, voxday.net, 2026-03-04, `bib-critics.md` row JB-1 (sha256 `f7bb3f68…` for `vd-bowers-repost.html`). Day says the original title was "Ignorant and Unscientific Drivel". Quotes on file: BO-01..BO-04 (`quotes-critics.md`). Both sides are in one source: Bowers's seven points (secondhand) and Day's replies (firsthand).
- **Secondhand text (rule U, inverted):** Bowers's words reach us only through Day. Score them as reposted, mark each `secondhand`, and do not score Day's repost as a misquote unless the original is found and differs.
- **Original:** make at most one search pass (two or three queries) for Bowers's original review. If found, fetch it read-only into the same new directory and compare it with the repost: say whether the repost is complete and verbatim, and list any differences. If not found, say so in one line; the bib row already records the earlier failed search.
- **Held copy:** none on disk. Make one read-only fetch of the repost URL (the page, and its comments only if Day's reply continues there) into a new directory `sources/raw/jb-1-2026-11-26/`, record sha256s. A hash difference from the bib row is acceptable (site chrome changes); the test is that every quote on file (BO-01..BO-04) is an exact substring of the fetched text. If a quote is missing or the fetch fails, report and stop.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/bowers-jb1.md` with skill `deref-source`: each statement verbatim with locator (Bowers's seven points and Day's reply to each) → argument steps → `M-` objects. **Reuse first:** the branch-F and branch-G maps already hold BO-01 (F4, M-113), BO-03 (F4a, M-605) and BO-02 (G2f, M-706 / M-704); specific-vs-any is settled in G3 and the McCarthy item-1 page; fixation rate vs latency is M-115; the 4Nₑ lag is M-914. Link settled points, don't repeat them. Only maths not in the library becomes a new object (next free id after M-917) with a record `records/M-NNN.py` + `.json` asserting every number the page states. Bowers's points contain no numbers (BO-04 note), so a new object may not be needed; don't create one for its own sake.
2. **Review page** `docs/reviews/2026-11-26-joe-bowers-critical-review.md` (actual date if later) from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds (entries for both sides; Bowers and Day's reply are judged by the same standard), what fails, slips (R1 with the check shown), logic (N/U, hidden premises; in particular whether Day's "probability vs rate" reply answers the point Bowers made, F4a), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; Day's "Not a single calculation" (BO-04) and his retitling get the same treatment as Bowers's lines), verdict table with readings (RD), labelled informal and not entered in any claim file, Day-side and critic-side steelman of equal depth, bottom line.
3. **One link** in `docs/index.html`: one `<li>` after the Nesslig20 entry, same pattern.

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/<date>-joe-bowers-critical-review.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/bowers-jb1.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/sources/bib-critics.md` (one line: new fetch hash, original found or not), `docs/research/math/people.yaml` (one entry for Bowers if missing). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers (or, if the page has fewer, every number) recomputed independently, three quotes re-read against the fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or a quote on file is not in the text (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
Other Day posts about Bowers; the general literature on fixation probability beyond what F4 already holds; claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hashes and whether quotes match; original found or not (and repost fidelity if found); new object ids with record sha256s, or "none"; objects reused; R1 results for any slips; secondhand calls; claim-file candidates; lint and record-run output; next step.
