---
id: G4b
title: "Day: McCarthy's use of a 40,000-generation fixation time increases the Darwillion by a factor of 25"
side: day
branch: G
parent: G4
edges: [{type: attacks, target: G3}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> In other words, he actually INCREASED the size of the Darwillion by a factor of 25. I was using a time-to-fixation number of 1,600. He’s proposing that increasing that 1,600 to 40,000 is somehow going to reduce the improbability, which obviously is not the case.

Source: [An Inspiring Critique](https://voxday.net/2026/01/27/an-inspiring-critique/) (key B2026-01-27-an-inspiring-critique), blog, 2026-01-27, ¶15.

## Formal statement
40,000/1,600 = 25 (python3 -I). The Darwillion as rendered by McCarthy, (1/20,000)^(2e7), contains no time-to-fixation input; the formula connecting a fixation time to the Darwillion is not in the harvested text. If the Darwillion is multiplied by 25, log10 changes by 1.4 out of 86,020,600; if the exponent were multiplied by 25, log10 would change 25-fold. The text does not say which. Pending the book.

## Assumptions
- Stated: fixation takes time; the neutral time 4Ne ≈ 40,000 generations (Q&A) is 25x Day's 1,600.
- Implicit: a formula linking fixation time to the Darwillion exists.

## Responses
- Against: none in corpus engaged this reply.
- In support: none.
- Weaknesses: unclear what is multiplied by 25; also 1,600 (a throughput inverse, A2) is compared with 40,000 (a latency), the throughput/latency mix flagged in G2d.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Not testable until the formula is available.

## Check
No script.

## Simulator variables implied
- None.
