---
id: E7
title: "A 100-fold higher mutation rate raises LTEE fixation throughput only 8.5-17-fold (mean 12.75), so fixation is bottlenecked by sweep dynamics, not mutation supply"
side: day
branch: E
parent: E
edges: [{type: supports, target: E}, {type: supports, target: A2}]
load_bearing: false  # Used to rebut "hypermutation rescues the rate" (the most aggressive rescue per Z23003785 §5). A2's non-mutator G_f is unaffected by it.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> "a 100-fold increase in mutation rate produces only an average 12.75-fold increase in fixation rate (in the range 8–17×, depending on the exact measurement window and counting methodology)"

Source: [Punctuated Equilibrium and the Hypermutation Hazard](https://zenodo.org/records/23020792), Z23020792, 2026-09-28, §2.1.

> "The headline result: a 100-fold increase in mutation rate produces only an approximately 8.5-fold increase in fixation throughput by clone-pair analysis at 50K (from 893 gen/fix to 104.7 gen/fix), or a 17-fold increase by metagenomics at 60K (from 1,322 gen/fix to 78 gen/fix)."

Source: [MITTENS 3.0](https://zenodo.org/records/23003785), Z23003785, 2026-09-28, §5.1.

> "Fixation is bottlenecked not by mutation supply but by sweep dynamics: beneficial mutations compete with each other for fixation (clonal interference), and elevated mutation rates exacerbate this interference rather than overcoming it."

Source: Z23020792, §2.1.

## Formal statement
Ratio R = G_f(non-mutator) / G_f(mutator). Clone-pair: 893 / 104.7 = 8.53 (50K). Metagenomic: 1,322 / 78 = 16.9 (60K). Mean of the two = 12.74 (paper 12.75; holds). "100-fold" is the mutation-rate ratio for the point-mutator populations; Ara+1 is an IS-element mutator "~5×" (Z23003785 §5.1 table).

derived (R2 recompute):
- Clone-pair mean 104.7 uses all seven mutators including Ara-2 = -906: 477.6/pop. Excluding Ara-2: 708.2/pop, 70.6 gen/fix, R = 12.6. The negative value lowers the mutator average and therefore lowers R; excluding it raises R from 8.5 to 12.6 (E5).
- Strict whole-population counts (Z23105291 Table 1): mutators 5,307 over 424,500 population-generations (0.01250/gen; 80 gen/fix); non-mutators 189 over 298,500 (0.000633/gen; 1,579 gen/fix). R = 19.7. Excluding Ara-2 (94): 22.6.
- Three counting rules therefore give R of 8.5, 16.9 and 19.7 (the last uses the lineage-aware counts that the same authors later call the count of record).
- If throughput scaled linearly with supply, R would be near 100 for the five ~100x populations; the observed R of 8-23 is sublinear in each rule.

## Assumptions
- Stated: mutator classification by Wielgoss 2013 and Consuegra 2021 (Z23105291); strong selection; asexual.
- Implicit: that supply is the only difference between mutator and non-mutator populations (mutators also accumulate deleterious load, Couce 2017; mutation-rate changes occur at different generations, Z23105291 notes non-stationary rates); that the observed sublinearity carries over to sexual vertebrates (the paper's own §5 caveat is that recombination changes clonal interference).

## Responses
- Against: the A5 critics point to the difference between the non-recombining LTEE bacteria and sexual vertebrates (Reddit RE-07: "largely nonrecombining bacteria descended from one clone"; Gariepy GA-01: sexual reproduction; McCarthy MC-07: the rate depends on "its genome size, mutation rate, etc."), so a bacterial sublinearity does not transfer. Hössjer (allied) accepts the scaling by mutation rate and genome length as a first-order adjustment (HO-01, HO-02).
- In support: Good 2017 reports multiple beneficial variants "simultaneously competing for dominance in each population" and says the trajectories are "inconsistent with a 'periodic selection' model".
- Weaknesses in the responses: critics did not quantify sublinearity; Hössjer's linear scaling in L and μ is not tested against it.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good 2017 | "molecular evolution continues to be characterized by signatures of rapid adaptation, with multiple beneficial variants simultaneously competing for dominance in each population" | accurate for competition between variants |
| Tenaillon 2016 | six populations "had 96.5% of the point mutations, having evolved hypermutable phenotypes" | accurate; see E8 |
| Couce 2017 | "Mutator genomes decay, despite sustained fitness gains" (title per Day) | not retrieved |

## Pre-registered prediction
- Under the claimant's model: in a forward simulation of an asexual population with competing beneficial mutations, fixation rate scales sublinearly in mutation rate (R well below the rate ratio) once U_b N s exceeds the clonal-interference threshold.
- Under the opposing model: with free recombination (sexual), R approaches the rate ratio up to the cost-of-selection and drift limits; the LTEE sublinearity does not carry over.
- Result that would change a verdict: a forward simulation with N, s and U_b scanned (asexual, then recombining) showing R vs rate ratio; plus agreement or disagreement of the simulated asexual R with the LTEE values (8.5-23).

## Check
Script: none yet (spec: `research/checks/e7_mutator_scaling.py`, planned; F2 interference sim with recombination parameter). · Result: not run · Review: pending

## Simulator variables implied
Mutation-rate multiplier, recombination rate, N, s distribution, counting rule.
