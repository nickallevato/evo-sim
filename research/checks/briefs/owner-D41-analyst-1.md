# owner-D41-analyst-1: review of McCarthy MC-1 + MC-1c (item 1 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document, §3 row 1 and §7. Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 1. No claim verdict, status field, claim-tree edge, ledger or count moves. Anything that would change a claim file goes in the report as a candidate.

## Sources
- **MC-1:** McCarthy, "Why 'Probability Zero' is Wrong About Evolution" (free repost, 2026-09-11), `bib-critics.md` row MC-1 (URL, sha256 `d7d808a3…`).
- **MC-1c:** McCarthy's own replies in that post's comment thread (2026-09-11 to 2026-09-25), `bib-critics.md` row MC-1c; quotes RF-1..RF-17 in `quotes-critics.md` (RF-6 is comment id 340149310).
- The original 2026-10-07/09 raw copies are **not held** locally. Make one read-only fetch (Substack public API for the post and its comments) into a new directory `sources/raw/mccarthy-mc1-2026-11-26/`. Record the new sha256. If the post body's hash differs from the bib row, diff the text: if only metadata differs, say so; if the text differs, report it and quote the current text. Every quote on the page is checked against this fetch.

## Deliverable
At most 3 commits:
1. **Source map** `docs/research/math/sources/mccarthy-mc1.md` with skill `deref-source`: each statement verbatim with locator → argument steps → `M-` objects. **Reuse first.** The library already covers much of this: P = p^n / Darwillion (objects.yaml ~l.1023), specific-vs-any (~l.1041), expected neutral fixations incl. McCarthy 450e9/20,000 (~l.436), human G_f vs the LTEE 1,600 (~l.604, ~l.922). Known content: the Darwillion (1/20,000)^20M, the GF = 1,600 LTEE transfer, the 4Nₑ lag calculation, 1,400 generations per fixation, and the RF-6 slip (400 billion × 1/20,000 written as 35 million; it is 20 million). Only maths not in the library becomes a new object with a record `records/M-NNN.py` + `.json` asserting every number the page states. Add McCarthy to `people.yaml` only if absent.
2. **Review page** `docs/reviews/2026-11-26-dennis-mccarthy-probability-zero-wrong.md` from `docs/reviews/_TEMPLATE.md`, **neutral** (D-41): what holds, what fails, slips (R1: RF-6 is a ledger-level slip unless correcting it moves his stated conclusion by >25 %; show the check), logic (N/U, hidden premises), rhetoric (RH: device, audience, function, dialectical core, better answer at the move; the same standard for Day's replies in the thread), verdict table with readings (RD), Day-side and critic-side steelman of equal depth, bottom line.
3. **One link** in `docs/index.html`: one `<li>` after the Paul review item, same pattern (GitHub blob URL on `master`; `docs/` has `.nojekyll`).

Before committing, run every new record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/2026-11-26-dennis-mccarthy-probability-zero-wrong.md` (new), `docs/index.html` (one `<li>`), `docs/research/math/sources/mccarthy-mc1.md` (new), `docs/research/math/objects.yaml` (new objects; `sources:` back-references on reused objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/math/people.yaml` (one entry, only if absent), `docs/research/sources/bib-critics.md` (one line: new fetch hash). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed independently, three quotes re-read against the new fetch, `git show --stat` inside the list. Then the lead publishes under D-41 (`git push origin research:master`).

## Stop when
All three parts are committed and pushed to `research`; OR the fetch fails or the text differs from the quotes on file (report, don't work around it); OR the work would touch a path outside the list, a claim file, a ledger or a verdict.

## Not in scope
MC-2 ("Vox Day Responds") and its thread except where a MC-1c reply quotes it; paywalled MC-5/MC-6; claim files; `slips.md`; argmap; board; tooling; new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; fetch hash and whether it matches the bib row; new object ids with record sha256s; objects reused; the RF-6 R1 result; any claim-file candidates; lint and record-run output; next step.
