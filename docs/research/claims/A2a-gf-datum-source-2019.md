---
id: A2a
title: "The 1,600 datum: 25 fixed mutations in ~40,000 LTEE generations (cited to Nature 2009, later to Good 2017)"
side: day
branch: A
parent: A2
edges: [{type: depends-on, target: A2}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: unverifiable
  external: pending
---

## Statement (verbatim)
> Source: Sequencing of 19 whole genomes detected 25 mutations that were fixed in the 40,000 generations of the experiment. NATURE, 2009

Source: [Maximal Mutations](https://voxday.net/2019/02/07/maximal-mutations/) (key B2019-02-07), blog, 2019-02-07, ¶9.

> Sequencing detected 25 mutations that were fixed over approximately 40,000 bacterial generations, yielding an average of 1,600 generations per fixed mutation.

Source: [Zenodo 18168236](https://zenodo.org/records/18168236) (key Z18168236), 2026-01-05, ¶29. This paper cites Good et al. 2017.

## Formal statement
G_f = 40,000 / 25 = 1,600  (`ltee.gens_per_fixation.day_2019`). `derived:` 40,000/25 = 1,600 exactly.

Citation drift: 2019 post "NATURE, 2009"; 2025 papers "Good et al. 2017" (60,000 generations); Z18168236 also says "reported in Nature in 2017". Barrick et al. 2009 (Nature) reports genomes at 20,000 generations (abstract in repo). Camestros (CA-06) reads the same literature as 35 mutations by 15,000 generations, i.e. 15,000/35 = 429 generations per fixed mutation (his source text prints 1500, a typo; he hedges that he may be misreading).

## Assumptions
- Stated: 25 fixed mutations, 40,000 generations.
- Implicit: the datum is from a non-mutator line (the 2019 text says "19 whole genomes"; which lines is not stated in the quote).

## Responses
- Against: Camestros (CA-06) obtains 429 from the same literature, an order of magnitude faster than 1,600 (as a question, not an assertion).
- In support: Day later replaced this datum with his own re-analysis (A2, A2b).
- Weaknesses: the repo has abstract-level access to Barrick 2009 only, so neither the 25/40,000 nor the 35/15,000 reading is checked against the paper. Camestros's own quote contains an arithmetic typo (1500 for 15,000).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Barrick et al. 2009 | "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations." | verified (abstract). The 40,000 generation horizon is not in the abstract. |
| Good et al. 2017 | trajectories to 60,000 generations | unverified for 25/40,000 |

## Pre-registered prediction
Not a testable prediction; a retrieval task. Prediction: the Barrick 2009 full text gives a per-lineage fixation count that, divided into 20,000 generations, is within a factor of 4 of 429–1,600; if it gives 429 (Camestros), the original G_f was 3.7x too slow for early generations.

## Check
Arithmetic only. Review: pending. Pending task: obtain Barrick 2009 full text (paywalled).

## Simulator variables implied
- LTEE windows (20k, 40k, 50k, 60k) as presets.
