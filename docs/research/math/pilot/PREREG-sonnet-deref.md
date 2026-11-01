# Pilot: can a Sonnet 5.5 agent de-reference sources into the math map?

Registered 2026-10-31, **before** either agent was spawned. The agents do not see this file. Post hoc changes go in a separate section below.

## Test V: video window
- **Source:** Gutsick Gibbon live session, "Teaching Famous Creationist Will Duffy Evolutionary Theory (LIVE) Human Evolution #3", uploaded 2026-10-30, https://www.youtube.com/watch?v=l_dIj1GTc0Q. Window 00:31:24 to 00:59:35: Will Duffy's critique of the critics' videos, then Erica's reply. Auto-generated captions, held at `sources/raw/vid02-l_dIj1GTc0Q-2026-10-31/` (gitignored). sha256 of the vtt is `28f5c6d1befd692ae3b4ec856850293e834081264655377204f713a4d5934070`, of the transcript `ac73e51ed3d81a10c44172c6602443daf0412f5b65ee227811d310cd86ca850d`.
- **Answer key** (lead's reading, written before the agent ran):

| # | Locator | Object | Existing node | Expected flag |
|---|---|---|---|---|
| K1 | 00:33:49-00:35:12 | d (selective turnover) vs N_e / Moran handling of overlapping generations | A4, A4e | model-choice; both positions |
| K2 | 00:37:58 | 252,000 x 0.8 = 201,600, where A4 records d = 0.45 (which gives 113,400) | A4, A1 | candidate: d value mismatch / edition |
| K3 | 00:35:32-00:37:15 | 76.8 is diploid; Porubsky 2025's 152 includes SVs, so it can't back a SNV-only count; haploid 38.4 | A3 (and the mutation-rate parameter) | parameter lookup |
| K4 | 00:38:18-00:38:39 | 2 x 38.4 x 201,600 x 35M / 3.2B = 169,344 (reproduces) but applies the observed divergence fraction to expected substitutions | A3 / B | candidate: double counting (non-sequitur) |
| K5 | 00:39:00-00:41:05 | MITTENS is a rate, not a latency; does F_max imply serial fixation? | A, F1a | inference; derivation |
| K6 | 00:42:07, 00:51:36 | "waiting time" vs "fixation problem" | — | rhetoric / terminology |
| K7 | 00:43:29, 00:52:39 | LTEE clonal start, so the rate does not transfer (Duffy concedes) | A2e | both sides credited |
| K8 | 00:44:31 | Lynch: prokaryotes adapt more efficiently, so LTEE is an upper bound | A2e | quote check + direction |
| K9 (minor) | 00:32:25 | the critics used a first-edition ePub; second edition corrected | versions ledger | fidelity / edition |
| K10 (minor) | 00:50:56, 00:53:00 | the standard popgen models fit real populations; pedigree DNM rates don't match Day's maths | B / A3 | empirical; critic side |

**Scoring:**
- **Recall:** K1-K8, each hit or miss, where a hit means the same object linked to the right node or noted as new. Pass at 6 or more of 8; strong at 8 of 8 including both candidate flags K2 and K4.
- **Quote fidelity:** every quote must grep-match the transcript after whitespace normalisation. Pass at 100%; each miss is recorded.
- **Arithmetic:** 169,344 and 201,600 are reproduced.
- **Balance:** both positions are filled, and Duffy's valid points (K3, K7) and the critics' valid points (K7, K10) are recorded.
- **Precision:** objects that are spurious or out of window are counted.
- **Cost:** tokens and wall time as reported.

## Test A: backfill of branch A claim files
- **Source:** the 43 claim files `docs/research/claims/A*.md` (209 KB), branch A (the MITTENS formula and its inputs).
- No answer key. Scored on:
  - **Mechanics:** `math_map.py --lint` passes with 0 errors on the agent's file.
  - **Dedup ratio:** objects per claim. A useful map is under 0.7; 1.0 means no dedup.
  - **Correctness:** the lead checks a seeded random sample of 8 objects against the claim files (seed `20261031`, sampled with Python `random.Random(20261031).sample(sorted_ids, 8)`). For each, is the formula or parameter stated correctly, are `used_by` and `resolved_by` correct, and are both positions fair? Pass at 7 or more of 8.
  - **Resolved status:** objects already settled by an R4 check are marked `resolved` with the file named.
  - **Cost:** tokens and wall time as reported.

## What the result decides
If both pass, the team uses Sonnet with `deref-source` for the backfill of the remaining branches, with an Opus spot check on a sample per branch. If either fails, the failure modes go into the skill and the test is rerun once, or Opus does the mapping.
