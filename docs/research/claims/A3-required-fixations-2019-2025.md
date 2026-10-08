---
id: A3
title: "Required fixations: 30M (2019) then 20M on the human lineage (2025)"
side: day
branch: A
parent: A
edges: [{type: supports, target: A}, {type: depends-on, target: A3c}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000 mutations to become fixed in the chimpanzee population

Source: [Maximal Mutations](https://voxday.net/2019/02/07/maximal-mutations/) (key B2019-02-07), blog, 2019-02-07, ¶26.

> Genetic divergence: ~40 million single-nucleotide variants; ~20 million fixations required on human lineage. Time available: 6–7 million years at 20 years/generation = 300,000–350,000 nominal generations.

Source: [MITTENS 2025, Zenodo 18165980](https://zenodo.org/records/18165980) (key Z18165980), pub. 2025-12-28 (modified 2026-01-06), ¶34.

## Formal statement
R_2019 = 15e6 per lineage (30e6 total); R_2025 = 40e6 / 2 = 20e6 per lineage   (`divergence.required_fixations.day_2019`, `.day_2025`)

`derived:` 35e6 SNV + 5e6 indel events (CSAC 2005) = 40e6 events, /2 = 20e6 (reconciles). Correcting for polymorphism: CSAC fixed fraction 0.0106/0.0123 = 0.862; 35e6 x 0.862 = 30.2e6 fixed SNV differences, /2 = 15.1e6 per lineage (python3 -I). That is close to the 2019 figure of 15e6, although the 2019 post does not give this derivation.

## Assumptions
- Stated: the SNV and indel differences in one human and one chimp genome are the substitutions to be explained; symmetric split between lineages.
- Implicit: polymorphic sites are fixed differences (CSAC says 14–22% of the divergence is polymorphism, A3c); every SNV or indel event is a separate fixation (true for SNV; for indels the CSAC count is events).

## Responses
- Against: Hancock (GG-02) says a factor-of-two issue exists (A3d, where it is assessed); Mansfield (MF-06) says "around 25 million give or take" is the number he has seen (uncited; consistent with this claim, not a disagreement).
- In support: Mansfield's 25 million is the same order as 20M.
- Weaknesses: the 2019 "30,000,000" is used with 450,000 generations and 281/562/125 achievable (A-file): the three achievable numbers do not reconcile with each other.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Chimpanzee Sequencing and Analysis Consortium 2005 | "constituting approximately thirty-five million single-nucleotide changes, five million insertion/deletion events, and various chromosomal rearrangements" | verified-partial (one genome per species; includes polymorphism; see A3c) |

## Pre-registered prediction
Not a simulation target. Prediction (claimant): R_2025 = 20M. Prediction (critic): fixed differences are 14–22% fewer, so R = 15–17M per lineage (derived: 35e6 x 0.78–0.86 / 2 = 13.7–15.1M for SNV only). A change in R by 1.3x has no effect on a shortfall of 1e5.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- `required_fixations` per lineage with a polymorphism-correction toggle (fixed fraction 0.78–0.86).
