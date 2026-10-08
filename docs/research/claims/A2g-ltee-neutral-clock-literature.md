---
id: A2g
title: "LTEE non-mutators accumulate mutations clock-like; neutral mutations at a constant rate; most fixed mutations beneficial"
side: literature
branch: A
parent: A2
edges: [{type: supports, target: A2}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> The populations that retained the ancestral mutation rate support a model where most fixed mutations are beneficial, the fraction of beneficial mutations declines as fitness rises, and neutral mutations accumulate at a constant rate.

Source: Tenaillon et al. 2016 (key Tenaillon2016), Abstract.

> Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations.

Source: Barrick et al. 2009 (key Barrick2009), Abstract (Europe PMC; full text paywalled).

> The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4), but there is a marked deficit of fixations in others (e.g. Ara-6).

Source: Good et al. 2017 (key Good2017), Results.

## Formal statement
Descriptive. Relevant to `ltee.gens_per_fixation` (the rate is steady for non-mutators) and to the critics' use of k = μ for LTEE neutral accumulation.

## Assumptions
- Stated: observed in the LTEE.
- Implicit: the LTEE environment and clonal structure.

## Responses
- Against: critics (A5f) say clonal interference and absence of recombination make the LTEE rate depressed relative to a recombining genome. Day (Z23003785 s8.2) says neutral fixation by drift is "off" at Ne ≈ 3e7 and that the 20 neutral fixations were all hitchhikers.
- In support: Day cites the steadiness for a stable G_f; critics cite it for neutral clock-like change.
- Weaknesses: abstracts only for Barrick; Good 2017 SI not retrieved.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon2016 | above | verified |
| Barrick2009 | above | verified (abstract) |
| Good2017 | above | verified (main text); ≥95% unverified |

## Pre-registered prediction
No prediction; descriptive.

## Check
No script.

## Simulator variables implied
- Preset: LTEE non-mutator trajectory shape (nearly linear accumulation).
