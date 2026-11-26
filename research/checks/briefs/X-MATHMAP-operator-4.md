# X-MATHMAP-operator-4: source map for branch E claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-D.md` (X-MATHMAP-operator-3, 778f205, lead-approved).

## Gap item
X-MATHMAP, branch E (fourth of B, C, D, E, F, G, H, ROOT). Done for E when every branch-E node is `used_by` at least one object: the **11** files `docs/research/claims/E*.md` (E, E1-E10). No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-E.md`: the source map, same header and preamble style as branch D (`| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`). One or more rows per E node. The locator is the claim file plus its quote number (count the blockquotes in the Statement section, as branch D does), and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read them whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-501 to M-599 only**. Reuse an existing M-1xx..M-4xx object, and add the E node to its `used_by`, where it asks the same maths question (LTEE rates and counts may already exist under A, B or C objects: grep `objects.yaml` for LTEE, Barrick, Tenaillon, Good, mutator first). Don't renumber or reword existing objects beyond `used_by`.
- Merge pass inside branch E: fewer than 0.7 new objects per E node (**at most 7**).
- Where a claim file records that no verbatim statement was located (E1 says so), map the statements the file does hold (literature or Day text) and say so in the row; don't invent a speaker.
- Where an object's statement quotes a spread or range, it must say which sources the figure covers (branch D lesson: M-403's "53 orders" is Axe vs Taylor only).

## Allowed paths
- `docs/research/math/sources/branch-E.md` (new)
- `docs/research/math/objects.yaml` (append M-5xx; `used_by` additions on existing objects)

Read anything; grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, other `sources/branch-*.md`, `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap, or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7).

## Candidate flags
Before writing a `candidate:` flag, read the claim file's `internal:` verdict comment and its R4 paragraphs (E3, E5, E6, E7 carry check results). If the point is already settled there, write "settled: <verdict> (<R4 id>)", using the R4 id that the claim file itself gives; where the file gives none, write "claim file". Report only flags that are new.

## Budget
At most 2 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, under 0.7 objects per E node, every quote verbatim in its claim file, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, `math_map.py --lint` shows 0 errors, and every E node is covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Branches other than E; merging the A and vid02 pilots; resolving objects (records/); verdicts; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it); the M-403 range wording (carried to X-MATHRESOLVE). Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; E nodes covered / 11; new objects (count and ratio), reused ids; `math_map.py --lint` output; new `candidate:` flags (one line each); quotes not found; speakers missing from `people.yaml`; next step.
