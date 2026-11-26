# X-MATHMAP-operator-3: source map for branch D claim files (maps only)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHMAP (owner request 2026-11-01, 31e5d25); `docs/research/math/README.md` (schema); `docs/research/math/REMAINING.md` P1. Form: `docs/research/math/sources/branch-C.md` (X-MATHMAP-operator-2, 3e9be4e, lead-approved).

## Gap item
X-MATHMAP, branch D (third of B, C, D, E, F, G, H, ROOT). Done for D when every branch-D node is `used_by` at least one object: the **41** files `docs/research/claims/D*.md` **except `DN*.md`** (DN1-DN6 hang under ROOT-FM and go with the ROOT batch). No verdict, status or claim field moves.

## Deliverable
One branch backfill, with the `deref-source` skill including its merge step:
- `docs/research/math/sources/branch-D.md`: the source map, same header as branch C (`| Locator | Speaker | Quote | RH | Steps | Objects | Existing node | Arithmetic |`). One or more rows per D node. The locator is the claim file plus its quote number, and the Q id where one exists (grep `sources/quotes-*.md` by id; don't read them whole).
- New objects appended to `docs/research/math/objects.yaml`, ids **M-401 to M-499 only**. Reuse an existing M-1xx, M-2xx or M-3xx object, and add the D node to its `used_by` where it asks the same maths question. Don't renumber or reword existing objects beyond `used_by`.
- Merge pass inside branch D: fewer than 0.7 new objects per D node (at most 28).
- **Carry-over fix from the branch C review:** in `branch-C.md`, row `C2c q1`, change "settled: non-sequitur (R4 X1)" to "settled: non-sequitur (R4 C2c)". That one edit only.

## Allowed paths
- `docs/research/math/sources/branch-D.md` (new)
- `docs/research/math/objects.yaml` (append M-4xx; `used_by` additions on existing objects)
- `docs/research/math/sources/branch-C.md` (the one carry-over edit above)

Read anything; grep big files by id. Don't edit claim files, `hierarchy*`, `parameters.yaml`, pilots, `branch-B.md`, `people.yaml` (if a speaker alias is missing, use the claim file's name and list it in the report), QUEUE, REVIEW, RESULTS, `gap-blockers.yaml`, ledgers, argmap, or the board.

## Skill
`deref-source`. No computation beyond recomputing quoted arithmetic (local, seconds). No host, no fetch (O-7). Many D quotes are historical (Wistar 1966, Eden, Ulam, Fisher, Wright) and relayed by Day or Rosenhouse: record the relay as the speaker the claim file names, and keep the original author in the Steps cell.

## Candidate flags
Before writing a `candidate:` flag, read the claim file's `internal:` verdict comment and its R4 paragraphs. If the point is already settled there, write "settled: <verdict> (<R4 id>)", using the R4 id that the claim file itself gives (the branch C slip was a wrong id). Report only flags that are new.

## Budget
At most 3 commits. Fix passes left: 2 of 2. The lead does the review: `research/tools/math_map.py --lint` at 0 errors, under 0.7 objects per D node, every quote verbatim in its claim file, and a seeded 8-object spot check against the claim files. No other review.

## Stop when
- all files are committed and pushed, `math_map.py --lint` shows 0 errors, and every D node is covered; OR
- a quote can't be found verbatim in its claim file (list it; don't paraphrase); OR
- the work needs a path outside the list, a fetch or a rule change.

## Not in scope
Branches other than D (including DN1-DN6); merging the A and vid02 pilots; resolving objects (records/); verdicts; tooling fixes (a failing `math_map.py` is an `upkeep` stop: report it). Ideas: one line in the report.

## Commit trailer
`Gap: X-MATHMAP`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`; `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commits; D nodes covered / 41; new objects (count and ratio), reused ids; `math_map.py --lint` output; carry-over fix done; new `candidate:` flags (one line each); quotes not found; next step.
