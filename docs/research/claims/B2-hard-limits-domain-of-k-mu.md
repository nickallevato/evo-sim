---
id: B2
title: "Hard Limits: drift cannot complete fixations above a census ceiling; the domain of k = mu is empty for large vertebrates"
side: day
branch: B
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: B2a}, {type: depends-on, target: B2b}, {type: depends-on, target: B2c}]
load_bearing: true  # with B1 it is the other route by which the neutral escape is closed; if both fail ROOT as worded fails
sourcing: firsthand
status: reviewed
verdicts:
  internal: pending
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> Checking them yields a hard ceiling on population size, X = (Vₖ + 2)·G/16 — reproductive variance and lineage generations alone, with no mutation rate, no coalescent quantity, and no fitted constant.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)

> The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)

## Formal statement
Summary (the pieces are B2a, B2b, B2c, B2d): 4Nₑ < G ⇒ N < X = (Vₖ+2)G/16; above X, P(τ ≤ G | fixation) ~ exp(−π²Nₑ/G).

The paper contains no reference list in the harvested copy (balance ledger), and cites Kimura & Ohta 1969, Wright, Hill 1972 and Maruyama 1970/74 in the text only. `parameters.yaml` has no entries for Vₖ or census N; propose `new: population.Vk_human = 5` (HL Table 1) and `new: population.census_human = 8.2e9` (HL Table 1).

## Assumptions
- Stated: k = μ is accepted ("this paper accepts it throughout"); the mean fixation time 4Nₑ is the transit time; Nₑ is the variance effective size; Wright's Nₑ = (4N−2)/(Vₖ+2).
- Implicit: A mean time (4Nₑ) is a deadline unless the tail is quantified (addressed by B2a); the lineage window G is the relevant window (but the paper's 78-million exponent uses a 400-generation window, B2c); the pipe is empty at the start of the window (B1c/B1d).

## Responses
- Against: "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield; replying to a Day blog sentence about drift at large N, not to HL))
  RESULTS B2a: the exponent is a per-allele latency tail, not a throughput bound.
- In support: RESULTS B2a: the exponent −π² is the correct leading-order short-time asymptotic. Day's own simulation reproduces the mean time (391 vs 400).
- Weaknesses in the responses: Mansfield's comment predates HL and is aimed at a different statement. Day's abstract summary "about ten thousand" is not what the paper's table gives (35,000–114,000, B2b). The two sides have not met on the fill-state question (B1c).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | "takes about 4Ne generations until it spreads to the whole population" (p.766) | accurate |
| Maruyama 1970/1974 (cited by HL, third objection) | not retrieved (abstract only for 1970) | unverified |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: k(T) = μF(T) with F exponentially small for T ≪ 4Nₑ.
- Under the opposing model: For a population at equilibrium the flux is μ regardless of transit time (B1, B1b).
- Result that would change a verdict: See B2a (exponent), B2b (ceiling inputs), B1c (fill state).

## Check
See child claims. Script: `research/checks/b2a_hard_limits_chain.py`, `research/checks/b2a_scaling.py` · Result: see B2a. Review: `research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`

## Simulator variables implied
- Vₖ
- G (lineage generations)
- census N and Nₑ definition (variance/coalescent)
- window T
- fill state
