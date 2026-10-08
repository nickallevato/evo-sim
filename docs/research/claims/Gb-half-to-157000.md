---
id: Gb
title: "P(all beneficial) = 0.5^157,000 = 10^−47,262 and the population size required to find one such individual"
side: day
branch: G
parent: G
edges: [{type: depends-on, target: G}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> P(all beneficial) = (0.5)¹⁵⁷'⁰⁰⁰ = 10⁻⁴⁷'²⁶²

Source: [The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07), ¶45 (s4.1). The apostrophes are the thousands separators in the source.

## Formal statement
log10(0.5^157,000) = 157,000 x (−0.30103) = −47,261.7 → 10^−47,262 (reconciles). N_required = 10^47,262 individuals (s4.2).
Relevance: the probability that an individual carries all 157,000 beneficial alleles when each is at p = 0.5. The paper also says (s7.10) "Each locus … experiences its selection coefficient s and responds accordingly. The Bernoulli Barrier does not deny this." so the existence of an all-beneficial genotype is not needed for per-locus sweeps; the number illustrates the compression of variance (s4) rather than a requirement.

## Assumptions
- Stated: p = 0.5 at every locus; independence; n = 157,000.
- Implicit: all loci are simultaneously intermediate (not so, s7.8); the extreme genotype is the target.

## Responses
- Against: critics did not engage this number. The specific-vs-any objection (G3) applies in the same way: the probability that a *particular* genotype exists is not the probability that selection acts.
- In support: Day (blog 2026-10-01 ¶26) maintains correctness.
- Weaknesses in the responses: no critic has addressed s7.10 (per-locus response); Day's s7.10 qualifies the use of this number.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Arithmetic only.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- None directly.
