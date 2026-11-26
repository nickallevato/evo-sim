# X-MATHMAP-operator-10: source map for the six FM children of ROOT-FM (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-ROOT.md` (X-MATHMAP-operator-8, c92999b) and `branch-A.md` (X-MATHMAP-operator-9, a4b2a83), both lead-approved.

## Gap item
X-MATHMAP, last part. After branch A, the only claim-tree nodes in no object's `used_by` are **FM3, FM4, FM5, FM7, FM8b, FM10** (files `docs/research/claims/FM{3,4,5,7,8b,10}-*.md`; use each file's `id:` field). When all six are covered, every node is covered and X-MATHMAP's done condition is met. No verdict, status or claim field moves.

## Deliverable
One backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-FM.md` (new): same header, preamble style and columns as branch ROOT. One or more rows per node; locator = claim file plus quote number (count the blockquotes in the Statement section), and the Q id where one exists (grep `sources/quotes-*.md` by id; ROOT-FM q1-q4 already cite Q164-Q166 and Q168). Real steps (P, I, C, implicit) per quote.
- `docs/research/math/objects.yaml`: reuse first. M-902 (overdispersion), M-903 (one mesa against two ceilings) and M-904 (sigillation) already state FM3, FM5 and FM7 maths from the ROOT-FM quotes; add the FM nodes to their `used_by`. New objects, if any, take ids **M-911 to M-999 only**, `status: open`, and are fewer than 0.7 per node (**at most 4**). Don't reword existing objects beyond `used_by`.
- Where an object's statement quotes a spread or range, say which sources it covers.

## Lessons (do these)
1. Wrap each quote once, in straight double quotes `"..."`.
2. Every `used_by` you add must have at least one row in `branch-FM.md` that names that object.
3. **Both directions:** every object a row names must list that row's node in `used_by`.
4. Name quantities as the claim file does; where FM and ROOT-FM files give different figures for one quantity, quote both and name both files.
5. Run the verbatim check and `math_map.py --lint` **before** `git commit`, as separate commands. Commit only after both pass.
6. A `candidate:` flag is new only if the claim file doesn't already state it. Read the `internal:` verdict comment and R4 paragraphs first; if settled there, write "settled: <verdict> (<R4 id>)", or "claim file" if it gives no id. FM10's internal waits on Day releasing his method: say so; don't flag it.
7. RH tags follow the claim files; reuse M-221 or M-908 for rhetoric, create none.

## Allowed paths
- `docs/research/math/sources/branch-FM.md` (new)
- `docs/research/math/objects.yaml` (append M-911..M-999; `used_by` additions on existing objects)

You can read any file. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, other `sources/*.md` (including `branch-ROOT.md`), `people.yaml` (list missing speakers in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds), stating the formula first. No host, no fetch (O-7).

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `math_map.py --lint` at 0 errors, fewer than 0.7 new objects per node, every quote verbatim in its claim file, `used_by` and rows consistent in both directions, every claim node covered, and a seeded spot check of every object the map names (up to 8) against the claim files. No other review.

## Stop when
- all files are committed and pushed, lint shows 0 errors and all six nodes are covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
The vid02 pilot merge: its held captions are on neither the workstation nor na-workhorse, so its quotes can't be checked without a re-fetch (owner, O-7). Resolving objects (X-MATHRESOLVE); verdicts; tooling (a failing `math_map.py` is an `upkeep` stop: report it); fixes to earlier branches. Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; FM nodes covered / 6; new objects (count, ratio) and reused ids; lint output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
