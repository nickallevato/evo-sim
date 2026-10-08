---
id: E8
title: "Tenaillon 2016: six LTEE populations carried 96.5% of point mutations through hypermutable phenotypes; non-mutators show mostly beneficial fixations and a constant neutral clock"
side: literature
branch: E
parent: E
edges: [{type: supports, target: E}, {type: supports, target: E1}]
load_bearing: false  # Source for the mutator count and for the all-cause versus beneficial split. Supplies premises to E, E1, E7.
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: n/a   # this file records the source itself; Day's use is judged in E (E8) and E6 (E9)
  external: pending
---

## Statement (verbatim)
> "six populations (Ara-1, Ara-2, Ara-3, Ara-4, Ara+3 and Ara+6) had 96.5% of the point mutations, having evolved hypermutable phenotypes"

Source: Tenaillon et al. 2016, [Tempo and mode of genome evolution in a 50,000-generation experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC4988878/), Nature 536:165, Results, "Genome evolution" (quote in `sources/quotes-literature.md`).

> "The populations that retained the ancestral mutation rate support a model where most fixed mutations are beneficial, the fraction of beneficial mutations declines as fitness rises, and neutral mutations accumulate at a constant rate."

Source: Tenaillon 2016, Abstract.

## Formal statement
Mutator share: six populations, 96.5% of point mutations; the remaining 3.5% sits in the other populations (derived: 100 - 96.5; the number of populations sequenced is not in the quoted passage). Day's use: Z23020792 Abstract (six mutators: four mutS/mutL, two mutT); Z23003785 and Z23105291 count seven mutators (adding Ara+1, an IS-element mutator).
Parameter link: proposed `ltee.mutator_populations` (6 per Tenaillon 2016 at 50,000 generations; 7 per Wielgoss 2013 / Consuegra 2021 used in Z23105291 for 60,000 generations).

## Assumptions
- Stated (by the paper): point mutations in sequenced clones at 50,000 generations; populations classified by the evolved hypermutable phenotype.
- Implicit (in Day's use): the six-versus-seven classification differences are time-dependent (Ara+1's IS-element phenotype, antimutator evolution in some lineages; Z23105291 acknowledges the binary classification "is a simplification").

## Responses
- Against: none.
- In support: Day Z23020792 (six, with the mismatch-repair / oxidative-repair split, which the quoted passage does not contain).
- Weaknesses in the responses: Day's three papers use two different counts (six, seven) without reconciling them.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon 2016 (the work itself) | quotes above | verified (fidelity ledger: "Tenaillon 2016 ... verified") |

## Pre-registered prediction
- Under the literature: six mutators at 50,000 generations, 96.5% of point mutations; non-mutators show constant neutral accumulation and a declining beneficial fraction.
- Under Day's use: consistent with the six; seven at 60,000 generations with Ara+1.
- Result that would change a verdict: a gene-level table (mutS/mutL/mutT) from the Tenaillon SI contradicting the 4 + 2 split in Z23020792.

## Check
Script: none (literature lookup). · Result: not run · Review: pending

## Simulator variables implied
Mutator count and timing, mutation-rate multiplier per population, neutral fraction.
