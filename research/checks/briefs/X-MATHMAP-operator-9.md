# X-MATHMAP-operator-9: source map for branch A claim files, from the A pilot (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1; `docs/research/math/pilot/RESULT-sonnet-deref.md` (what the A pilot got wrong). Form: `docs/research/math/sources/branch-ROOT.md` (X-MATHMAP-operator-8, c92999b, lead-approved).

## Gap item
X-MATHMAP, branch A. It is done for A when every one of the **43** nodes with a file `docs/research/claims/A*.md` is in the `used_by` of at least one object (use each file's `id:` field). 31 are uncovered now; the 12 already covered (A1, A2d, A2e, A3b, A3c, A3x, A4, A4a, A4c, A4e, A4f, A4g) still get rows. No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-A.md` (new): same header, preamble style and columns as branch ROOT. One or more rows per node; locator = claim file plus quote number (count the blockquotes in the Statement section), and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read those files whole). Real steps (P, I, C, implicit) per quote, not generic ones.
- New objects appended to `docs/research/math/objects.yaml`, ids **M-001 to M-099 only**. Reuse an existing M-1xx..M-9xx object before you create one.
- **The pilot is a draft input, not a source.** `pilot/A/objects.yaml` (42 objects) and `pilot/A/sources/branch-A.md` failed on merging (0.98 objects per node) and step depth. Use them to find the maths questions, then merge: fewer than 0.7 new objects per node (**at most 30**). The pilot's ids M-001..M-042 are not kept: number fresh from M-001, and say in the preamble which pilot ids each new object absorbs.
- Every new object has `status: open`. Do not carry the pilot's `resolved` / `resolved_by` (settling objects is X-MATHRESOLVE); where the pilot named a result file, you may name it in `positions` as a pointer.
- Where an object's statement quotes a spread or range, say which sources it covers.

## Lessons from B to ROOT (do these)
1. Wrap each quote once, in straight double quotes `"..."`.
2. Every `used_by` you add must have at least one row in `branch-A.md` that names that object.
3. **Both directions:** every object a row names must list that row's node in `used_by`.
4. Name quantities as the claim file does; where two files give different figures for one quantity, quote both and name both files.
5. Run the verbatim check and `math_map.py --lint` **before** `git commit`, as separate commands. Commit only after both pass.
6. A `candidate:` flag is new only if the claim file doesn't already state it. Read the `internal:` verdict comment and R4 paragraphs first; if settled there, write "settled: <verdict> (<R4 id>)", or "claim file" if it gives no id.
7. RH tags follow the claim files; at most one `resolution: rhetoric` object for the branch (reuse M-221 or M-908 first).

## Allowed paths
- `docs/research/math/sources/branch-A.md` (new)
- `docs/research/math/objects.yaml` (append M-0xx; `used_by` additions on existing objects)

You can read any file. Don't edit the pilot files, claim files, `hierarchy*`, `parameters.yaml`, other `sources/branch-*.md`, `people.yaml` (list missing speakers in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds), with every factor the speaker uses (state the formula before you flag). No host, no fetch (O-7).

## Budget
At most 2 commits. Fix passes left: 2 of 2. Lead review: `math_map.py --lint` at 0 errors, fewer than 0.7 new objects per node, every quote verbatim in its claim file, `used_by` and rows consistent in both directions, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, lint shows 0 errors and all 43 nodes are covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
The vid02 pilot and the six FM children of ROOT-FM (FM3, FM4, FM5, FM7, FM8b, FM10): the next task. Resolving objects; verdicts; tooling (a failing `math_map.py` is an `upkeep` stop: report it); fixes to earlier branches (X-MATHRESOLVE). Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; A nodes covered / 43; new objects (count, ratio, pilot ids absorbed) and reused ids; lint output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
