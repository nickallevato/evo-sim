# X-MATHMAP-operator-7: source map for branch H claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-G.md` (X-MATHMAP-operator-6, 03a0726, lead-approved), with the lessons below.

## Gap item
X-MATHMAP, branch H (seventh of B, C, D, E, F, G, H, ROOT). Done for H when every branch-H node is `used_by` at least one object: the **12** files `docs/research/claims/H-*.md` and `H[0-9]*.md` (H, H1, H2, H2a, H3, H4, H5, H6, H7, H8, H9, H10). No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-H.md`: the source map, same header and preamble style as branch G (`| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`). One or more rows per H node. The locator is the claim file plus its quote number (count the blockquotes in the Statement section), and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read them whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-801 to M-899 only**. H10 already appears in `used_by` (M-120, M-121: grep `used_by:.*H`); map its quotes to those objects where they ask the same maths question, and still write the rows. Reuse any existing M-1xx..M-7xx object before creating one (e.g. Kimura fixation probability, neutral fixation time 4Ne, average rate M-101). Don't renumber or reword existing objects beyond `used_by`.
- Merge pass inside branch H: fewer than 0.7 new objects per H node (**at most 8**).
- Where an object's statement quotes a spread or range, it must say which sources the figure covers.

## Lessons from E, F and G (do these)
1. Wrap each quote in single straight double quotes `"..."`.
2. Every `used_by` you add must have at least one row in `branch-H.md` that names that object.
3. **Both directions:** every object a row names must list that row's node in `used_by` (G missed Gd on M-604).
4. Name quantities exactly as the claim file does.
5. Run the verbatim check and `math_map.py --lint` **before** `git commit`, as separate commands; commit only after both pass.
6. A `candidate:` flag is new only if the claim file does not already state it; if the file states part of it, say which part is new.

## Allowed paths
- `docs/research/math/sources/branch-H.md` (new)
- `docs/research/math/objects.yaml` (append M-8xx; `used_by` additions on existing objects)

Read anything; grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, other `sources/branch-*.md`, `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap, or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7).

## Candidate flags
Before writing a `candidate:` flag, read the claim file's `internal:` verdict comment and its R4 paragraphs. If the point is already settled there, write "settled: <verdict> (<R4 id>)", using the R4 id that the claim file itself gives; where the file gives none, write "claim file". Report only flags that are new.

## Budget
At most 2 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, under 0.7 objects per H node, every quote verbatim in its claim file, `used_by` and rows consistent in both directions, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, `math_map.py --lint` shows 0 errors, and every H node is covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Branches other than H; ROOT and DN1-DN6 (next task); merging the A and vid02 pilots; resolving objects (records/); verdicts; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it); earlier branches' carried fixes (X-MATHRESOLVE); pre-existing `used_by` entries with no citing row. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; H nodes covered / 12; new objects (count and ratio), reused ids; `math_map.py --lint` output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
