---
id: A2h
title: "Day's s6.4 supermutator arithmetic is a tenfold slip: 3.2e9 x 1.2e-8 x 100 = 3,840, not 38,400"
side: critic
branch: A
parent: A5d
edges: [{type: attacks, target: A5d}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: n/a
---

## Statement (verbatim)
> Section 6.4 also makes a tenfold arithmetic mistake: 3.2 billion × 1.2 × 10⁻⁸ × 100 is 3,840 mutations per haploid genome, not 38,400.

Source: [r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (RE-02).

> A 100-fold increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100).

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.11 (s6.4). Locator: line "increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation".

## Formal statement
3.2e9 x 1.2e-8 = 38.4; x 100 = 3,840. `derived:` the paper's 38,400 is 10x too large. Its next step, "10% deleterious fraction … 3,840 deleterious mutations", is 10% of the erroneous 38,400; the correct figure is 384. Its fitness figure (0.999)^3,840 ≈ 0.02 becomes (0.999)^384 ≈ 0.68; (0.99)^3,840 ≈ 1e-17 becomes (0.99)^384 ≈ 0.021 (recomputed: 0.999^384 = 0.681, 0.99^384 = 0.0211). The same product at 1x gives 38.4 mutations per haploid genome per generation, the number used in A5b.

## Assumptions
- Stated: arithmetic with Day's own inputs (the critic and the paper use the same product).
- Implicit: the 10% deleterious fraction is Day's; the critic does not dispute it.

## Responses
- Against: none in corpus; Day has not been recorded answering this point.
- In support: the arithmetic is verified here.
- Weaknesses in the response: the slip affects the argument of s6.4 that a mutator allele in a sexual organism is immediately selected against, whose conclusion (a 100x mutator in a sexual organism is strongly deleterious) would still hold at 384 deleterious mutations (fitness 0.021 at s = 0.01). Whether 3.0 contains other uses of 38,400 was not searched.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Arithmetic; no pre-registration needed.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- None.
