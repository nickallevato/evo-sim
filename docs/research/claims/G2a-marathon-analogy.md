---
id: G2a
title: "Marathon analogy: 60,000 runners x 4 h = 240,000 h only if run serially; mutation and fixation run in parallel"
side: critic
branch: G
parent: G2
edges: [{type: attacks, target: G2g}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: partial
  external: n/a
---

## Statement (verbatim)
> Of course you say that's not possible, they run parallel. Well, the same goes with mutation and fixation.

Source: [Jan Ghijselen, "Will Duffy's math on Gutsick Gibbon's channel."](https://www.youtube.com/watch?v=nTVRiEcswI8), 2026-09-28, t=00:03:52 (DZ-01; auto-caption).

Day's transcription of the argument: [Math Teacher Can’t Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (blog, 2026-09-30), ¶6: "It would mean that if you have the Marathon of New York with 60,000 participants and an average length of 4 hours per marathon. If you would follow this reasoning, it would take on average 240,000 hours for the marathon to end."

## Formal statement
60,000 x 4 h = 240,000 h = 10,000 days = 27.4 years (python3 -I; DeDzjang says "27 years"). Reconciles. The serial division is wrong for parallel events; the analogy applies to any calculation of the form (time)/(latency).

## Assumptions
- Stated: events overlap in time.
- Implicit: the criticised calculation divides time by latency.

## Responses
- Against (Day): [Math Teacher Can’t Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (blog, 2026-09-30) ¶7: "The math is not wrong because parallel fixation is clearly and specifically included in the calculation." (i.e., Day's G_f is not a latency).
- In support: Day's s8.2 and A5e calculations that do use fixation time as an interval (G2 responses).
- Weaknesses in the responses: DeDzjang himself says in comments that he is "not schooled on this subject" and that "he rejects parallel fixation on shaky grounds" (said of Day); the analogy is valid logic but its application to G_f as defined is exactly what G1 disputes. He says a fuller treatment needs stochastics but gives none.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Linked result: F1 (research/checks/RESULTS.md, seed 31, N = 1000, s = 0.01, U_b = 0.01, independent loci, no interference, no cost): predicted steady-state rate 0.3960 per generation, simulated 0.3972 ± 0.0018; t_fix = 847 generations but G_f = 1/rate = 3 generations; in-transit count ≈ 336, computed from Little's law (not measured). Review #3 caveats: the regime is unrealistic (20 new beneficial mutations per generation), so pipelining is shown to be possible, not feasible; feasibility is the F2/H question.

## Check
Link: `research/checks/RESULTS.md` F1; arithmetic audit (python3 -I, scratch).

## Simulator variables implied
- None beyond G2.
