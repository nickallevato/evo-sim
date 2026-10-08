---
id: G2g
title: "Day (Appendix A, quoted in his blog): the Bernoulli Barrier rules out parallel fixation, therefore fixation must be sequential, and sequential gives 180 against 205 million"
side: day
branch: G
parent: G
edges: [{type: supports, target: A}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: non-sequitur
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> Therefore fixation must be sequential. And sequential fixation is empirically falsified: the fastest rate ever measured in any organism, applied to the most generous generation count, yields 180 fixations where 205 million are required.

Source: [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (key B2026-10-01-they-never-stop-lying), blog, 2026-10-01, ¶24 (Day quotes a passage he says is from Appendix A and "different, non-MITTENS math"). The book text itself was not checked.

> Now, perhaps I could have worded it better, but the statement is nevertheless correct because the all-cause rate is obviously faster than a sequential rate.

Source: [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (key B2026-10-01-they-never-stop-lying), blog, 2026-10-01, ¶25.

## Formal statement
Logical form quoted by Day: (Bernoulli Barrier: p^n ≈ 10^−34,000,000, so parallel fixation is impossible) ∧ (Averaging Problem: polygenic rescue impossible) ⟹ fixation sequential ⟹ N_fix = 252,000/1,400 = 180 versus 205e6. `derived:` 252,000/1,400 = 180 ✓ (the 1,400 is the book's G_f; 3.0 uses 1,322, i.e. 190.6). The p^n in the quoted passage is for n = 2e7 (Ga); the requirement in the same sentence is 205 million: different n.
In ¶25 Day states the 180 is based on a rate (all-cause) that is "obviously faster than a sequential rate", i.e. the 180 is not a purely sequential calculation; ¶22: "MITTENS … specifically includes and incorporates parallel fixation, with my subsequent disproofs of parallel fixation." In ¶4: "serial fixation with sweeps and ancestral drift are about all that is left AFTER the math eliminates various mechanisms".

## Assumptions
- Stated: BB is correct; parallel fixation is impossible in real species (¶22: "That’s not how real-world species work"); the LTEE rate includes parallelism because it is an average over 12 populations running in parallel.
- Implicit: the BB conclusion and the aggregate G_f can both be used: the first removes parallelism from humans, the second keeps it in the LTEE rate applied to humans. If parallelism is ruled out for humans, then applying a rate that includes parallel overlap to humans overstates what humans can do (a point in Day's favour for the shortfall) but also means G_f is not the serial rate (a point against his statement that the rate "is sequential").

## Responses
- Against: Hancock, Myers (G2, G2e): the argument rests on a serial premise. Camestros (G2d). The fidelity gap in BB (G, Gc).
- In support: Day's own caveats: ¶25 "the all-cause rate is obviously faster than a sequential rate"; ¶22 distinguishes MITTENS from the "subsequent disproofs of parallel fixation".
- Weaknesses in the responses: the critics quote the Appendix A passage as evidence of seriality; Day replies that it is non-MITTENS math. Both can be right: the book's chain of argument is serial, and the 3.0 math is aggregate. The internal verdict (non-sequitur) concerns the chain as quoted: from BB (which has its own issues, G) to sequential, then to 180 using a rate that Day says includes parallelism. Not independently checked against the book.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No prediction; consistency analysis only.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- Mode switch in the simulator: "parallel allowed" vs "forced sequential".
