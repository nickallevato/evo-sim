---
id: ROOT
title: "No evolutionary mechanism can produce the observed human-chimpanzee divergence in the available time"
side: day
branch: ROOT
parent: null
edges: [{type: depends-on, target: A},{type: depends-on, target: B},{type: depends-on, target: C},{type: depends-on, target: D},{type: depends-on, target: E},{type: depends-on, target: F},{type: depends-on, target: G},{type: depends-on, target: H},{type: depends-on, target: ROOT-M}]
load_bearing: true  # this is the root claim; it fails if its universal quantifier fails for any mechanism (see ROOT-M)
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # branches A-H and ROOT-M must be resolved first
  fidelity: n/a      # aggregate claim; fidelity is audited per branch
  external: pending      # depends on A-H
---

## Statement (verbatim)
> "my own demonstration of the mathematical impossibility of evolution by natural selection, selective sweeps, neutral sweeps, genetic drift, ILS, biased gene conversion, and every other imagined mechanism"

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, voxday.net, para 3 of extracted text. Day's own summary of his scope: eight named mechanism classes plus an unnamed remainder.

> "Alternative mechanisms—incomplete lineage sorting, soft sweeps, standing variation, hitchhiking—do not rescue the model. Each alternative, when subjected to quantitative analysis, fails to close gaps of 3-5 orders of magnitude. The fixed differences exist. They must be accounted for. The proposed mechanisms cannot account for them in the available time."

Source: [The Universal Failure of Fixation: MITTENS Applied Across the Tree of Life](https://zenodo.org/records/18452504) (Z18452504), 2026-02-02 (v1), Sections 4.3-4.4 / Conclusion, extracted-text lines 320 and 349

> "The post-Darwinian polythesis fails comprehensively under the most favorable experimental conditions ever constructed."

Source: [MITTENS 3.0: The Mathematical Impossibility of the Post-Darwinian Polythesis](https://zenodo.org/records/23003785) (Z23003785), published 2026-09-28, record modified 2026-10-04 (content drift not yet diffed, see ledgers/versions.md), Abstract, p.1.

> "evolution by natural selection not only never happened, but was never even possible"

Source: [Every Critique is Correct](https://voxday.net/2024/04/25/every-critique-is-correct/), 2024-04-25, para 10 (earlier, stronger-worded form: 'never happened' as well as 'never possible').

## Formal statement
ROOT as an implication:
- For every mechanism M in a set S = {natural selection (hard and soft sweeps), parallel fixation, neutral drift, neutral sweeps, hitchhiking, ILS, biased gene conversion, relictation-type bottleneck drift, recombination, hypermutation, ... and "every other imagined mechanism"}:
  `F_M(T) < F_req`, where F_M(T) is the number of lineage-specific fixations (or equivalent) mechanism M can deliver in T generations and F_req is the number required by the observed divergence.
- Day's operational form (MITTENS 3.0): `F_max = T_gen / G_f` with `T_gen = 252,000` (parameters.yaml `generations_available.day_2026`), `F_req = 2.05e8` (`required_fixations.day_2026`), `G_f = 1,322` (`ltee.gens_per_fixation.day_mittens3_nonmutator`); shortfall `F_req / F_max = 2.05e8 / (252000/1322) = 1.075e6` (derived, reproduces the stated 1,075,000 to 3 sig figs: 2.05e8/190.62 = 1.0754e6).
- The universal quantifier ("every other imagined mechanism") is the part that needs an argument per mechanism; see ROOT-M.

## Assumptions
- Stated: (i) the divergence is the 205M (2026) or 20M (2025) fixations; (ii) T = 252,000 or 202,500 or 146,250 generations (versions drift, see ledgers/versions.md); (iii) the LTEE throughput of 1,322 gens/fixation is an upper bound on any mechanism ("the fastest fixation rate ever observed in any organism under any conditions"); (iv) the LTEE includes "almost every way evolution can theoretically take place" (blog 2026-09-30).
- Implicit: the fixation of an allele is the unit of work (not haplotype blocks, not polymorphism sorting); a bacterial asexual aggregate bounds a sexual vertebrate; ancestral Ne and the starting pipeline state do not matter; dates of divergence are independent of the neutral-clock mechanism being tested.
- Implicit: absence of a computed argument for a mechanism is treated by Day as non-rescue (burden of the alternative; Z18452504: "they gesture at alternative mechanisms without demonstrating that any alternative can accomplish the required work").

## Responses
- Against (as of R2): No critic in the corpus addresses ROOT as a whole; critics attack the supporting branches (A5 scaling, B1/B3/B5 neutral theory, F1 latency vs throughput, G serial vs parallel, C1 ascertainment). See hierarchy.yaml for the edges. A5, B3, B7 and A3x have verified fidelity problems on the Day side (ledgers/fidelity.md); the ally Hossjer re-derives a ~2x (not 10^6x) gap after scaling (HO-01, HO-02, claim ROOT-H).
- In support: allies endorse the conclusion (ROOT-K, ROOT-T, ROOT-H, ROOT-DE) but contribute no independent calculation, with the partial exception of Hossjer's scaling.
- Weaknesses in the responses: "no critic addressed ROOT as a whole" is a statement about our corpus (23 opponent profiles); the Gutsick Gibbon / Hancock 3.5 h response (2026-10-03) was transcribed but only parts mapped. Day's characterisation of the critics' answer as "qualitative" ("The response ... was not a quantitative rebuttal", MITTENS 3.0 section 1) is contradicted by at least KITTENS, Hancock, Mansfield and Nesslig20, who give numbers (balance ledger); equally, several critics' numbers are off (balance ledger).

## Primary literature
| Cited work | What it actually says | Fidelity |
|---|---|---|
| See branch files A-H | ROOT cites no literature of its own | n/a |
| Kimura 1962; Kimura & Ohta 1969; Zeng 2021; Yoo 2025; Langergraber 2012 (inputs to A, B) | see ledgers/fidelity.md | misread/partial/not-found (as recorded there) |

## Pre-registered prediction
Written before any ROOT-level check (ROOT has no check of its own; it is the conjunction of A-H plus ROOT-M).
- Under the claimant's model: every branch check with defensible parameters returns a shortfall of at least ~10^2 for every mechanism in ROOT-M; no mechanism in ROOT-M has an unaddressed quantitative route.
- Under the opposing model: at least one of (A5 scaling, B1/B3 equilibrium state, F1/G pipelining, C1 ascertainment) removes most of the shortfall, so that the required fixations are within ~1-2 orders of magnitude of achievable; the mechanisms are not individually excluded.
- Result that would change a verdict: ROOT is **refuted** if any single mechanism class in ROOT-M is shown (by forward simulation under parameters.yaml values and Day's own T, with scaling validated) to deliver the required F_req within T; ROOT is **supported** only if all of A (after scaling), B and G survive the R4 checks and every row of ROOT-M carries a computed exclusion. Rows tagged "asserted, not computed" cannot count as support.

## Check
No ROOT-level script. Component checks: B0, B0.4, B1, B1b, B2a, B3, F1 (done); A, C, E, G, H (queued); Branch D (this module): arithmetic only so far, simulations specified in D, D2h, D9, D4. Arithmetic here: `python3 -I -c "print(2.05e8/(252000/1322))"` -> 1.0754e6 (reconciles with the stated 1,075,000).

## Simulator variables implied
T_gen (generations available), F_req (required fixations: SNV-only vs bp), G_f or a mechanistic fixation process, mechanism switches (selection, drift, linkage/hitchhiking, recombination, bottleneck family replacement, mutation supply), population structure, demographic history, scaling parameters.
