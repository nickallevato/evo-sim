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
  fidelity: accurate   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: contested
---

## Statement (verbatim)
> or about 9.7 million over its proposed 252,000 generations.

Source: [r/DebateEvolution, Dumb-and-Dumber, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, post 1wss2wj (Dumb-and-Dumber)

> It needs the elapsed time to be long compared with the fixation time.

Source: [r/DebateEvolution, justatest90, comment pcug1j0 under "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/new_antievolution_paper_today_from_vox_day/pcug1j0/), 2026-09-29 (RE-16; attribution corrected 2026-10-09, R4 X1 rule rev 2 section 8: justatest90, not the OP)

> The gap is under a factor of two (much of which is solved with the CHLCA point above), not a factor of 91,600.

Source: [r/DebateEvolution, justatest90, comment pcug1j0 under "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/new_antievolution_paper_today_from_vox_day/pcug1j0/), 2026-09-29 (RE-17)

> Further, at the point of divergence from CHLCA, the ancestral population was already in process of fixing or eliminating mutations.

Source: [r/DebateEvolution, justatest90, comment pcug1j0 under "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/new_antievolution_paper_today_from_vox_day/pcug1j0/), 2026-09-29 (RE-18; the commenter's full-pipe premise)

## Formal statement
Derived: 3.2e9 × 1.2e-8 = 38.4 per generation; × 252,000 = 9.68M ✓ (single lineage). The OP (Dumb-and-Dumber) gives 9.7M as "an illustration, not a prediction"; justatest90's comment pcug1j0 states the SNV-only requirement of 17.5M and that "The gap is under a factor of two": 17.5/9.68 = 1.81 (derived). The comment also takes the neutral fixation time as 4Nₑ ("40,000–132,000 generations") and notes 252,000 is well above it — the B1a subtraction would give (252,000 − 40,000) × 38.4 = 8.14M or (252,000 − 132,000) × 38.4 = 4.6M (derived).

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

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / accurate. ATTRIBUTION: the 9.7M quote is the OP (Dumb-and-Dumber, 'illustration, not a prediction', N4); 'It needs the elapsed time ...' and 'gap under a factor of two' are justatest90, comment pcug1j0. N1: on that commenter's stated full-pipe premise the lag is absent and the conclusion follows; inputs match Day's s6, s4.3 Charitable reading tried: tried the full-pipe premise stated by the commenter (pcug1j0); the OP's 9.7M is an illustration.

## Simulator variables implied
- L haploid
- μ
- T
