---
id: B5f
title: "r/DebateEvolution: 38.4 × 252,000 = ~9.7 million expected neutral substitutions on the human lineage vs 17.5 million required"
side: critic
branch: B
parent: B5
edges: [{type: attacks, target: B1}, {type: attacks, target: B3a}]
load_bearing: false  # illustration; the gap to the SNV-only requirement is under a factor of two
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> or about 9.7 million over its proposed 252,000 generations.

Source: [r/DebateEvolution, Dumb-and-Dumber, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (Dumb-and-Dumber)

> It needs the elapsed time to be long compared with the fixation time.

Source: [r/DebateEvolution, Dumb-and-Dumber, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (Dumb-and-Dumber)

## Formal statement
Derived: 3.2e9 × 1.2e-8 = 38.4 per generation; × 252,000 = 9.68M ✓ (single lineage). The same post states the SNV-only requirement of 17.5M and that "The gap is under a factor of two": 17.5/9.68 = 1.81 (derived). It also takes the neutral fixation time as 4Nₑ ("40,000–132,000 generations") and notes 252,000 is well above it — the B1a subtraction would give (252,000 − 40,000) × 38.4 = 8.14M or (252,000 − 132,000) × 38.4 = 4.6M (derived).

## Assumptions
- Stated: Haploid 3.2 Gb, μ = 1.2e-8, 252,000 generations; Day's Z23003785 uses the same formula for the LTEE hitchhikers (§4.3).
- Implicit: All sites neutral; full pipe.

## Responses
- Against: n/a
- In support: B5c/B5e after haploid correction (19.4M and 18.9M for two lineages, ≈ 9.7M per lineage).
- Weaknesses in the responses: The post is KITTENS-adjacent reddit commentary (AI-assisted per related posts); the 17.5M comparator includes polymorphism and ignores the ancestral term.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: ~9.7M per lineage; gap < 2×.
- Under the opposing model: (Day) 7.56M (IR) with a 15.9% empty-pipe loss; gap to 17.5M ≈ 2.6×.
- Result that would change a verdict: B4a (ancestral term) closes the gap if Nₑ,anc is ~10⁵.

## Check
Script: none (arithmetic).

## Simulator variables implied
- L haploid
- μ
- T
