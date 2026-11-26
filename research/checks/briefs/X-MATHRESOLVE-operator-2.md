# X-MATHRESOLVE-operator-2: one parameters.yaml pass (Day's d = 0.80, N_e 33,000, g = 29; day_alt 32.5)

**Role:** operator (Sonnet). **Written by:** lead, 2026-11-26. **Authority:** `docs/research/gap-blockers.yaml`, row X-MATHRESOLVE, `next` step (1); records M-114, M-110, M-002 (`docs/research/math/records/`). The claim-file pass is done (EVOA-92, c19d409).

## Gap item
X-MATHRESOLVE, parameters part. No verdict, status or claim-tree field moves. No existing parameters.yaml value changes.

Four items, each a provenance lookup in held text (`sources/raw/`, gitignored; grep, never execute):
1. **d = 0.80.** Add a key under `selection:` (e.g. `turnover_d_day_2025_10: {value: 0.80, ...}`) next to `turnover_d` (0.45). Find the held post that states 0.80 (source maps evo005, evo006, evo009 use it; evo009@L54 states only the d = 1 count). `source:` is the post's bibliography key; add a `locator:` and the verbatim phrase in `note:`.
2. **N_e 33,000.** Add a key under `population:` for Day's 33,000 with two locators: evo007@L32 (called a human parameter) and Z18525547 (where 33,000 is the chimpanzee N_e and human N_e is 3,300; see claim files B3, B4 and M-114). Say both in `note:`; do not pick one.
3. **g = 29.** Add a key under `generation_time_years:` for evo007@L32's "generation time ≈ 29 years" with that locator. Note that M-114 found no other held Day source for 29.
4. **day_alt 32.5 (B2025-01-18).** Grep the held B2025-01-18 text for 32.5. If found verbatim, add `locator:` and the phrase. If not, leave `verified: false` and add `note: "no verbatim quote in held text (M-002)"`.

For every new key: `verified: true` only when you have grepped the verbatim phrase in held text and give its locator; otherwise `verified: false` and say why in `note:`. Use bibliography keys that already exist (`docs/research/sources/bib-*`); if a post has none, use the source map's file id (e.g. `evo007`) and say so in the report.

## Deliverable
One commit changing `docs/research/parameters.yaml` only. Before committing, run as separate commands, all must pass: every record (`for f in docs/research/math/records/M-*.py; do research/.venv/bin/python -I "$f" || echo FAIL $f; done`), `research/tools/math_map.py --lint`, `research/checks/lint_research.py`. `git status` must show no other changed file after the record run.

## Allowed paths
- `docs/research/parameters.yaml`

Read anything. Don't edit records, objects.yaml, source maps, claim files, results, gap-blockers.yaml, ledgers, QUEUE/REVIEW/RESULTS, argmap or the board.

## Skill
`deref-source` (locate verbatim text in held sources, with locator). No host, no fetch (O-7).

## Budget
1 commit (2 at most). Fix passes left: 2 of 2. Lead review: lints 0 errors, all records pass, `git show --stat` is parameters.yaml only, spot check of each new key's locator against held text. No other review (D-40).

## Stop when
- the four items are done, committed and pushed; OR
- a value is not in held text: key it `verified: false` with the reason, don't infer it; OR
- a record or lint fails because of the new keys, or a fix needs a path outside the list: stop and report.

## Not in scope
P3 compute; changing any existing value or `verified` flag; the "Ideas (not queued)" lines (ltee.mutator_populations etc.); records; tooling; people.yaml.

## Commit trailer
`Gap: X-MATHRESOLVE`, then the attribution lines your issue gives you, in one trailer block. Explicit paths, never `git add -A`. `git pull --rebase origin research` before `git push origin research`. Don't push to `master`.

## Report (≤ 300 words, as the issue comment)
Commit; each new key with value, source, locator, verified flag; item 4 outcome; records run (pass count); lint output; anything stopped on.
