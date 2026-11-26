# X-MATHMAP-operator-5: source map for branch F claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-E.md` (X-MATHMAP-operator-4, 2fdf415, lead-approved), with the three fixes under "Lessons from E".

## Gap item
X-MATHMAP, branch F (fifth of B, C, D, E, F, G, H, ROOT). Done for F when every branch-F node is `used_by` at least one object: the **12** files `docs/research/claims/F-*.md` and `F[1-6]*.md` (F, F1, F1a, F1b, F1c, F2, F3, F3a, F4, F4a, F5, F6). The `FM*` files are under `ROOT-FM` and are **not** in this task (they go with ROOT). No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-F.md`: the source map, same header and preamble style as branch E (`| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`). One or more rows per F node. The locator is the claim file plus its quote number (count the blockquotes in the Statement section), and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read them whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-601 to M-699 only**. Seven F nodes already appear in `used_by` (F, F1, F1a, F1c, F3, F4, F6: grep `used_by:.*F`); map their quotes to those objects where they ask the same maths question, and still write the rows. Reuse any existing M-1xx..M-5xx object (fixation time 4Ne and (2/s) ln(2Ne), P_fix = 2s, relictation M-507, rate vs latency M-115, s_min M-506) before creating one. Don't renumber or reword existing objects beyond `used_by`.
- Merge pass inside branch F: fewer than 0.7 new objects per F node (**at most 8**).
- Where an object's statement quotes a spread or range, it must say which sources the figure covers.

## Lessons from E (do these)
1. Wrap each quote in single straight double quotes `"..."`, as branches B-D do (E had `""...""`).
2. Every `used_by` you add must have at least one row in `branch-F.md` that names that object (E added E2 to M-115 with no row citing it).
3. Name quantities exactly as the claim file does (E's M-501 wrote "q = 1/280 per diploid" where the file has carrier frequency 1/280, q = 0.0018).

## Allowed paths
- `docs/research/math/sources/branch-F.md` (new)
- `docs/research/math/objects.yaml` (append M-6xx; `used_by` additions on existing objects)

Read anything; grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, other `sources/branch-*.md` (don't fix branch-E's quote marks either; that goes to X-MATHRESOLVE), `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap, or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7).

## Candidate flags
Before writing a `candidate:` flag, read the claim file's `internal:` verdict comment and its R4 paragraphs. If the point is already settled there, write "settled: <verdict> (<R4 id>)", using the R4 id that the claim file itself gives; where the file gives none, write "claim file". Report only flags that are new.

## Budget
At most 2 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, under 0.7 objects per F node, every quote verbatim in its claim file, every added `used_by` cited by a row, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, `math_map.py --lint` shows 0 errors, and every F node is covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Branches other than F (FM* included); merging the A and vid02 pilots; resolving objects (records/); verdicts; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it); the M-403 range wording and the branch-E fixes (carried to X-MATHRESOLVE). Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; F nodes covered / 12; new objects (count and ratio), reused ids; `math_map.py --lint` output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
