# owner-D41-analyst-0: review template + EVOA-102 repair (item 0 of the D-41 series)

**Role:** analyst. **Written by:** lead, 2026-11-26. **Authority:** owner decision D-41 (`docs/research/DECISIONS.md`); plan in EVOA-104's `plan` document. Off-gap, owner-approved.

## Gap item
`owner` (D-41), item 0. No claim verdict, status field, claim-tree edge or count moves.

## Deliverable
At most 3 commits:
1. **Template** `docs/reviews/_TEMPLATE.md` (≤ 80 lines): the EVOA-102 sections, made **neutral** per D-41 Q2: source pin (URL, date, words, sha256 of the held fetch) · the argument, verbatim with locators · the maths located and rebuilt (table: step | equation | inputs | library object or "new M-NNN" | check) · what holds · what fails (errors; non-sequiturs and hidden premises, rules N/U) · slips (R1/SC, ledger level) · rhetoric (rule RH: device, audience, function, dialectical core, a better answer aimed at the move, never at the person; the same standard for Day) · verdict table with readings (RD) · Day-side steelman and critic-side steelman of equal depth · bottom line. Header line: "Not an audit check; no claim file, verdict or count changed."
2. **Source map** `docs/research/math/sources/paul-rimmer-2026-11-08.md` with skill `deref-source`, from the held fetch `sources/raw/paulnottheapostle-2026-11-26/` (read only; don't refetch). Reuse objects first. New maths (at least the JC69 divergence that gives 6.05 My, and the bacteria-at-100-My figure) becomes new `M-` objects in `objects.yaml` with records `records/M-NNN.py` + `.json` asserting every number the review states. Add Paul to `people.yaml` and a `bib-critics.md` entry with the sha256.
3. **Lookup:** human pairwise nucleotide diversity "about 0.1 %" (review §3 E2, l.58). One read-only fetch of an open primary source, in a new directory under `sources/raw/`; one verbatim quote with locator in `bib-literature.md` and a new key in `parameters.yaml`. If no open source gives it, drop the number from the page instead.
4. **Repair the page** `docs/reviews/2026-11-26-paul-rimmer-rate-equations.md`: cite the new objects/records in its §2 table, replace the l.58 caveat with the lookup (or drop it), and add one line under the header: "Written before D-41; Day-side framing at the owner's request (EVOA-102). Later reviews are neutral." Change no finding. If a recomputed number differs from the page, correct it in place and list it.

Before committing, run every record, then `research/tools/math_map.py --lint`, then `research/checks/lint_research.py`, as separate commands. All must pass.

## Allowed paths
`docs/reviews/_TEMPLATE.md`, `docs/reviews/2026-11-26-paul-rimmer-rate-equations.md`, `docs/research/math/sources/paul-rimmer-2026-11-08.md`, `docs/research/math/objects.yaml` (new objects only), `docs/research/math/records/M-NNN.{py,json}` (new only), `docs/research/math/people.yaml` (one entry), `docs/research/sources/bib-critics.md`, `docs/research/sources/bib-literature.md` (one entry each), `docs/research/parameters.yaml` (one new key). Raw fetches stay in gitignored `sources/raw/`.

## Skill
`deref-source` for the map; records per `docs/research/math/README.md` "Records". No host (records run locally in seconds; if one doesn't, stop and report).

## Budget
At most 3 commits. Lead review = the seeded spot check (D-40): three numbers recomputed from records, three quotes re-read against the raw text, `git show --stat` inside the list. Then the lead publishes under D-41.

## Stop when
All four parts are committed and pushed; OR an input is missing (report, don't work around it); OR the work would touch a path outside the list, edit a claim file, ledger or verdict.

## Not in scope
Items 1–10, other sources, claim files, ledgers (`slips.md`), argmap, board, index.html, tooling, new rules. Ideas: one line in the report.

## Commit trailer
`Gap: owner` with "D-41" in the body, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; new object ids with record sha256s; objects reused; lookup value, source and locator (or "dropped"); any number corrected on the page; lint and record-run output; next step.
