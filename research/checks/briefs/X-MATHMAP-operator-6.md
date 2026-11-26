# X-MATHMAP-operator-6: source map for branch G claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-F.md` (X-MATHMAP-operator-5, 34e3c5a, lead-approved), with the lessons below.

## Gap item
X-MATHMAP, branch G (sixth of B, C, D, E, F, G, H, ROOT). Done for G when every branch-G node is `used_by` at least one object: the **26** files `docs/research/claims/G-*.md`, `G[1-6]*.md` and `G[a-e]-*.md` (G, G1, G1a, G1b, G1c, G2, G2a-G2h, G3, G3a, G3b, G4, G4b, G5, G6, Ga, Gb, Gc, Gd, Ge). `GAP-*` files are not G nodes. No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-G.md`: the source map, same header and preamble style as branch F (`| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`). One or more rows per G node. The locator is the claim file plus its quote number (count the blockquotes in the Statement section), and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read them whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-701 to M-799 only**. Three G nodes already appear in `used_by` (G1, G1c on M-101; G2h on M-106: grep `used_by:.*G`); map their quotes to those objects where they ask the same maths question, and still write the rows. Reuse any existing M-1xx..M-6xx object before creating one; branch G overlaps F heavily (rate vs latency M-115, parallel capacity / 230 cap M-604, sweep latency M-601, throughput ceiling M-106, average rate M-101). Don't renumber or reword existing objects beyond `used_by`.
- Merge pass inside branch G: fewer than 0.7 new objects per G node (**at most 18**).
- Where an object's statement quotes a spread or range, it must say which sources the figure covers.

## Lessons from E and F (do these)
1. Wrap each quote in single straight double quotes `"..."`.
2. Every `used_by` you add must have at least one row in `branch-G.md` that names that object.
3. Name quantities exactly as the claim file does.
4. Run the verbatim check and `math_map.py --lint` **before** `git commit`, as separate commands; commit only after both pass (F ran the commit in the same command as a failing check).
5. A `candidate:` flag is new only if the claim file does not already state it; if the file states part of it (e.g. F3 line 34 had the 0.01-0.99 window), say which part is new.

## Allowed paths
- `docs/research/math/sources/branch-G.md` (new)
- `docs/research/math/objects.yaml` (append M-7xx; `used_by` additions on existing objects)

Read anything; grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, other `sources/branch-*.md`, `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap, or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7).

## Candidate flags
Before writing a `candidate:` flag, read the claim file's `internal:` verdict comment and its R4 paragraphs. If the point is already settled there, write "settled: <verdict> (<R4 id>)", using the R4 id that the claim file itself gives; where the file gives none, write "claim file". Report only flags that are new.

## Budget
At most 2 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, under 0.7 objects per G node, every quote verbatim in its claim file, every added `used_by` cited by a row, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, `math_map.py --lint` shows 0 errors, and every G node is covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Branches other than G; merging the A and vid02 pilots; resolving objects (records/); verdicts; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it); earlier branches' carried fixes (X-MATHRESOLVE); pre-existing `used_by` entries with no citing row. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; G nodes covered / 26; new objects (count and ratio), reused ids; `math_map.py --lint` output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
