---
id: A5d
title: "Hypermutators: a 100x mutation rate gives only 8.5x–17x faster fixation, so fixation is not bottlenecked by mutation supply"
side: day
branch: A
parent: A5
edges: [{type: attacks, target: A5b}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: non-sequitur
  fidelity: n/a
  external: "contested"   # sublinear confirmed for asexual; not for free recombination in F2's tested regime
---

## Statement (verbatim)
> Supermutation does not scale linearly with mutation rate. It cannot, because fixation is not bottlenecked by mutation supply. It is bottlenecked by the dynamics of sweeps:

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.8 (s5.1). The headline result is "a 100-fold increase in mutation rate produces only an approximately 8.5-fold increase in fixation throughput by clone-pair analysis at 50K (from 893 gen/fix to 104.7 gen/fix), or a 17-fold increase by metagenomics at 60K (from 1,322 gen/fix to 78 gen/fix)".

## Formal statement
response f = G_f(non-mutator)/G_f(mutator): 893/104.7 = 8.53 (clone-pair); 1,322/78 = 16.95 (metagenomic); 1,322/105 = 12.6 (the 105 used in s7.3). Exponent a = ln f/ln 100 = 0.47 (clone-pair), 0.61 (metagenomic). `derived:` (python3 -I) a < 1 (sublinear) is supported by the paper's own table; a = 0 (no dependence on supply) is not: f > 8 for 100x supply. Also: Ara-2 (−906) is a failure mode (A2c); the mutator average row ("Average (all 7)": 477.6 fixations, 104.7 gen/fix) includes it.
A related s5.3 table shows mutator advantage rising from 7.6x at 10K to ~20x at 40–50K and 16.9x at 60K (non-mutator: 794 → 1,322).

## Assumptions
- Stated: sweep dynamics, clonal interference, and finite carrying capacity of the selective environment bottleneck fixation; "More mutations … produce more competition between mutations, most of which cancel each other out."
- Implicit: the mutator populations' response (asexual, deleterious load) generalises to the response of a recombining genome to a 94,000x supply increase.

## Responses
- Against: the response is positive and large (8.5x–17x); "not bottlenecked by mutation supply" does not follow from a positive sublinear response. A2h: the paper's s6.4 supermutator arithmetic contains a tenfold slip. Recombination (A5f) is a mechanism by which supply-limited and interference-limited regimes differ.
- In support: the KITTENS author flags linear scaling as an illustration (RE-09), consistent with sublinearity; Day's s6 argues a mutator allele in a sexual organism cannot hitchhike with its beneficial products.
- Weaknesses in the responses: the critics (A5b) do not use Day's exponent; Day does not apply his own exponent to a 94,000x supply difference (which gives 206–1,136x, A5b), so the data are consistent with both a large and a small gap.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon et al. 2016 | "six populations (…) had 96.5% of the point mutations, having evolved hypermutable phenotypes" | verified |

## Pre-registered prediction
Pre-registered in A (A-sim): measured exponent a of fixation rate versus supply in a simulated asexual vs recombining population.
- Under Day: a ≈ 0.5 in both; supply-limited regime never reached.
- Under critics: a → 1 in the recombining case at low supply, falling below 1 only at high supply.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 A-sim (research/checks/results/R4-F2-A.md): sublinear response confirmed for an asexual genome (simulated 100x supply gives 2.9-4.8x, a = 0.23-0.34, more sublinear than Day's 0.47-0.61; the model lacks a DFE, so the exponent comparison is qualitative). Day's mechanism (sweep dynamics) is right for linked loci; for unlinked loci F2 gives a = 1.00 in its tested range. Credit to Day: sublinearity is real. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- Fixation rate vs supply curve for asexual vs recombining populations (output of A-sim).
