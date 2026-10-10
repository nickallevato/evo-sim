---
id: B5b
title: "Mansfield: if 2% of ~100 de novo mutations are neutral, there is on average 1 neutral fixation per generation"
side: critic
branch: B
parent: B5
edges: [{type: attacks, target: B1}, {type: attacks, target: B3a}]
load_bearing: false  # an illustration; by itself it falls ~44× short of 20M, so it does not close the gap alone
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> If even just 2 of these 100 are neutral - which is certainly way under the actual proportion - then in a population of size N there are about 2*N new neutral alleles introduced each generation.

Source: [Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07; terminus ante quem 2026-10-01: Day quotes this comment in "The Education of a Population Geneticist", ¶12 (added 2026-10-08), comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield)

> So, the expectation is that there will be on average 1 neutral fixation every generation if just 2% of new mutations are neutral.

Source: [Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07; terminus ante quem 2026-10-01: Day quotes this comment in "The Education of a Population Geneticist", ¶12 (added 2026-10-08), same comment

## Formal statement
2 neutral per zygote × N zygotes = 2N neutral alleles; × 1/(2N) = 1 fixation per generation ✓ (derived). Over 450,000 generations 450,000 fixations, over 252,000 generations 252,000; against 20M that is 44.4× short, against 17.5M (SNV) 69.4× short (derived). With a neutral fraction f of 100 mutations: 50 f per generation; 20M in 450,000 generations needs f = 0.89; 17.5M in 252,000 needs f = 1.39 (>1: impossible at 100 per zygote).

## Assumptions
- Stated: 2% of ~100 de novo mutations are neutral; N zygotes per generation.
- Implicit: "way under the actual proportion" (Mansfield; no figure); a full pipe (B1c); the 20M requirement is per lineage.

## Responses
- Against: Day (EDU 2026-10-01): same identity, but the pipe is not full (B1c); N/Nₑ not used by Mansfield.
- In support: Hössjer's 7.6M and Hancock's 19.4M give the same order when all sites are counted (B5c, B5h).
- Weaknesses in the responses: The illustration is under by a factor ~44 and the comment states the proportion qualitatively; Mansfield quotes Day only via a commenter's paste (secondhand per ledger).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: 1 neutral fixation per generation (at 2%).
- Under the opposing model: (Day) k = μ requires a full pipe.
- Result that would change a verdict: Mansfield or others supplying the actual neutral fraction (e.g., ~0.9+ of non-coding sites).

## Check
Script: none (arithmetic). See B5.

R4 B5b (research/checks/results/R4-B5b.md; review #15, combined, 2026-10-09): the identity (1 neutral fixation per generation at 2 neutral per zygote) is exact; at 2% it is 44x (450k generations) to 69x (252k) short of 20M / 17.5M. With the sourced complement of Rands 2014 (f = 0.918, an upper bound on the neutral share) and 100 mutations per zygote, supply is 20.7M over 450,000 generations (covers the 2019 count by 3%) but 11.6M over 252,000 (0.66x of 17.5M); with Kong's 76.8 per zygote it is 15.9M and 8.9M (0.79x, 0.51x) even at f = 0.918. Needed f: 0.889 (20M) and 1.389 (17.5M). Verdicts unchanged: holds / n/a / contested.

## Simulator variables implied
- neutral fraction
- new mutations per zygote
