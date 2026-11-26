# X-MATHMAP-operator-8: source map for ROOT and DN claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-H.md` (X-MATHMAP-operator-7, 9415cab, lead-approved), with the lessons below.

## Gap item
X-MATHMAP, branch ROOT (eighth and last branch, after B to H). It is done for ROOT when every one of these **17** nodes is in the `used_by` of at least one object: ROOT, ROOT-B, ROOT-COV, ROOT-DE, ROOT-EP, ROOT-FM, ROOT-H, ROOT-K, ROOT-M, ROOT-PG, ROOT-T (files `docs/research/claims/ROOT*.md`) and DN1-DN6 (files `DN*.md`, children of ROOT-FM). Use the `id:` field of each file, not the file name. No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-ROOT.md`: the source map, with the same header, preamble style and columns as branch H. Write one or more rows per node. The locator is the claim file plus its quote number (count the blockquotes in the Statement section), and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read those files whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-901 to M-999 only**. Reuse an existing M-1xx..M-8xx object before you create one. ROOT restates the whole case (time, supply, Haldane, dN/dS), so most rows should reuse objects. Don't renumber or reword existing objects beyond `used_by`.
- Endorsements and appeals to authority (e.g. ROOT-T, ROOT-EP, ROOT-PG) are mapped as the RH tag in the claim file says. Where a quote is rhetoric, map it to an object with `resolution: rhetoric` (math README, Rules); create at most one such object for the branch.
- Merge pass inside ROOT: fewer than 0.7 new objects per node (**at most 11**).
- Where an object's statement quotes a spread or range, it must say which sources the figure covers.

## Lessons from E to H (do these)
1. Wrap each quote once, in straight double quotes `"..."`.
2. Every `used_by` you add must have at least one row in `branch-ROOT.md` that names that object.
3. **Both directions:** every object a row names must list that row's node in `used_by`.
4. Name quantities exactly as the claim file does. Where two claim files give different figures for one quantity, quote both and name both files (H5 says Term 3 gives about 6,690; H1 and H8 say about 6,650).
5. Run the verbatim check and `math_map.py --lint` **before** `git commit`, as separate commands. Commit only after both pass.
6. A `candidate:` flag is new only if the claim file does not already state it. If the file states part of it, say which part is new.

## Allowed paths
- `docs/research/math/sources/branch-ROOT.md` (new)
- `docs/research/math/objects.yaml` (append M-9xx; `used_by` additions on existing objects)

You can read any file. Grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, other `sources/branch-*.md`, `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap or the board.

## Skill
`deref-source`. Do no computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7).

## Candidate flags
Before you write a `candidate:` flag, read the `internal:` verdict comment in the claim file and its R4 paragraphs. If the point is already settled there, write "settled: <verdict> (<R4 id>)", with the R4 id that the claim file gives. If the file gives none, write "claim file". Report only flags that are new.

## Budget
At most 2 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, fewer than 0.7 new objects per node, every quote verbatim in its claim file, `used_by` and rows consistent in both directions, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, `math_map.py --lint` shows 0 errors, and all 17 nodes are covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Other branches; merging the A and vid02 pilots (next task); resolving objects (records/); verdicts; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it); fixes carried from earlier branches (X-MATHRESOLVE); pre-existing `used_by` entries with no citing row. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Use explicit paths, never `git add -A`. Run `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; ROOT nodes covered / 17; new objects (count and ratio) and reused ids; `math_map.py --lint` output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
