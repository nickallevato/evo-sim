# X-MATHMAP-operator-1: source map for branch B claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1; pilot `docs/research/math/pilot/RESULT-sonnet-deref.md` (form of `pilot/A/sources/branch-A.md`).

## Gap item
X-MATHMAP, branch B (first of B, C, D, E, F, G, H, ROOT). Done for B when every `docs/research/claims/B*.md` node (51 files) is `used_by` at least one object. No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-B.md`: the source map, with the exact header the skill gives (`| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`). One or more rows per B node. The locator is the claim file plus its quote number, and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read them whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-201 to M-299 only** (M-001+ belong to the unmerged pilots, M-101+ to the digests). Reuse an existing M-1xx object, and add the B node to its `used_by` where it asks the same maths question. Don't renumber or reword existing objects beyond `used_by`.
- Merge pass inside branch B: fewer than 0.7 new objects per B node (at most 35).

## Allowed paths
- `docs/research/math/sources/branch-B.md` (new)
- `docs/research/math/objects.yaml` (append M-2xx; `used_by` additions on existing objects)

Read anything; grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap, or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7).

## Budget
At most 3 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, under 0.7 objects per B node, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- both files are committed and pushed, `math_map.py --lint` shows 0 errors, and every B node is covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Branches other than B; merging the A and vid02 pilots; resolving objects (records/); verdicts; `candidate:` flags beyond one line each; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it). Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; B nodes covered / 51; new objects (count and ratio), reused M-1xx ids; `math_map.py --lint` output; `candidate:` arithmetic flags (one line each); quotes not found; next step.
