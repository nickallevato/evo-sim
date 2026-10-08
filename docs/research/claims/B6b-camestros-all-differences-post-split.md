---
id: B6b
title: "Camestros: Day treats ALL human-chimp genetic differences as mutations that occurred after the split"
side: critic
branch: B
parent: B6
edges: [{type: attacks, target: B6a}]
load_bearing: false  # first-edition critique; quantified here only through CSAC's 14–22%
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: accurate
  external: "supported"   # qualitatively (B4a)
---

## Statement (verbatim)
> So Day is treating ALL the genetic differences between chimps and humans as mutations that initially only occurred after the point of divergence of the two species.

Source: [Camestros Felapton, "Reading Vox Day So You Don't Have To 2026 [2]" (post and comments)](https://camestrosfelapton.wordpress.com/2026/01/25/reading-vox-day-so-you-dont-have-to-2026-2/), 2026-01-24/25, para 46 (Camestros; first edition)

> it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000 mutations to become fixed in the chimpanzee population

Source: [Day, "Maximal Mutations" (blog)](https://voxday.net/2019/02/07/maximal-mutations/), 2019-02-07, ¶26 of extracted text. Day, first-edition basis (Q05 in the harvest)

## Formal statement
Day 2019 (second quote above) splits the whole 30M between lineages as post-split fixations. Quantification (derived): if polymorphism is 14–22% of observed SNV divergence (CSAC), the fixed fraction is 0.78–0.86; 35M × (0.78–0.86) = 27.3–30.1M fixed SNVs, 13.7–15.1M per lineage vs 17.5M used in Z23003785 (derived).

## Assumptions
- Stated: Day counts all differences as post-split fixations.
- Implicit: The 40M/35M count is of fixed differences.

## Responses
- Against: Day (B6a).
- In support: CSAC text.
- Weaknesses in the responses: Camestros reviewed the first edition only and writes "ALL" without a figure; the second edition and Z23003785 use SNV 35M with apportioning (17.5M) and do not subtract polymorphism.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Chimpanzee Sequencing and Analysis Consortium 2005 | "we estimate that polymorphism accounts for 14-22% of the observed divergence rate" | verified |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Some of the counted differences predate the split.
- Under the opposing model: (Day) rounding error (B6a).
- Result that would change a verdict: B4a.

## Check
Script: proposed B4a.

R4 B4a (research/checks/results/R4-B1c-B4a.md): qualitatively vindicated: ancestral alleles also sort into fixed differences (Day's 2mu(T-4Ne) = 0.51% is below the simulated fixed differences 0.56-1.46%), and raw d is not reduced by the empty-pipe term. Critic-side caveat: 2muT alone already supplies ~19M of the differences, so the point is accounting, not a gap filled only by ancestry. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- polymorphic fraction of divergence
