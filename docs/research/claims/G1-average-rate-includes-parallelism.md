---
id: G1
title: "An average rate is indifferent to parallel versus sequential timing; the LTEE G_f already includes parallel fixation"
side: day
branch: G
parent: A
edges: [{type: supports, target: A}, {type: depends-on, target: A2}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> The 1,322 gen/fix rate is not a sequential rate that needs to be divided by a parallelism factor. It is the total throughput, the net output after parallel fixation, clonal interference, sweep displacement, and every other concurrent dynamic has played out.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.13 (s8.1).

> If you drove ten miles and it took you an hour, then it makes no difference if you were driving sixty miles an hour part of the time or you were stopped part of the time, or even if you turned around and drove back home to pick up something you forgot.

Source: [Snikker-Snak](https://voxday.net/2026/10/01/snikker-snak/) (key B2026-10-01-snikker-snak), blog, 2026-10-01, ¶9. Day is defending a quoted commenter: "When dealing with average rates, it really doesn't matter if particular fixations happen parallel or in sequence."

## Formal statement
G_f = (generations in window)/(fixations in window) = T_obs / n_obs, an inverse throughput. F_max = T/(g_len·G_f) uses only the ratio; overlaps in time do not enter. This is true for any measured average rate over a window (`glossary.md`: G_f read as a latency is the confusion; G_f as throughput is the stated definition).

`derived:` (python3 -I) How "parallel" is the LTEE count? Z23105291: 5,496 whole-population fixations in 723,000 population-generations: 723,000/12 = 60,250 gens per population. Pooling all twelve populations gives 723,000/5,496 = 131.6 population-generations per fixation, a different quantity from the per-population G_f = 60,000/45.4 = 1,322 applied to one lineage. Averaging per-population rates over twelve independent populations does not add parallelism within one lineage; only overlap of sweeps inside a population counts. Day's argument in [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (blog, 2026-10-01) ¶22 ("the math is an average of 12 different populations … built into the structure since it utilizes 12 completely separate populations all running simultaneously in parallel. That’s not how real-world species work.") concedes this about real species.

## Assumptions
- Stated: G_f is measured, aggregate, post-parallelism, post-interference.
- Implicit: the degree of parallelism available in the measured system (within-population overlap of sweeps) equals that available to the target system; the rate is transferred unscaled (A2e, A5). The counting rule matters (A2b).

## Responses
- Against: Hancock (G2) and Myers, Bowers, Dumb-and-Dumber (RE-01) read the formula as sequential; Camestros (G2d) says "Generations per fixation" reads like one at a time. Day's own blog (Appendix A passage, G2g) says "Therefore fixation must be sequential" and applies 180 = 252,000/1,400.
- In support: Camestros concedes the figure is an average (G1c); Samson (G1b); Duffy (DU-03): "the number he's using in the math is already parallel fixation."; the F1 result shows that an observed throughput is not a latency division.
- Weaknesses in the responses: the critics' strongest version is not that the average is miscomputed but that it is applied to a system with a different capacity for parallelism (A5f). Day's own blog reports zero parallel fixation events inside Ara+2 over 60,000 generations (G1a), while s8.1 describes "overlapping sweeps at dozens of loci": the two descriptions are not reconciled. Day's s8.2 and Appendix D use the interval form (time/fixation-time) for drift and for the human-derived rate (A5e).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017 | "multiple beneficial variants simultaneously competing for dominance in each population" | verified (abstract); supports within-population overlap |
| Good et al. 2017 | trajectories "inconsistent with a “periodic selection” model in which individual driver mutations fix in a sequence of discrete selective sweeps" | verified |

## Pre-registered prediction
Linked result: F1 (research/checks/RESULTS.md, seed 31, N = 1000, s = 0.01, U_b = 0.01, independent loci, no interference, no cost): predicted steady-state rate 0.3960 per generation, simulated 0.3972 ± 0.0018; t_fix = 847 generations but G_f = 1/rate = 3 generations; in-transit count ≈ 336, computed from Little's law (not measured). Review #3 caveats: the regime is unrealistic (20 new beneficial mutations per generation), so pipelining is shown to be possible, not feasible; feasibility is the F2/H question.
- Under Day: G_f is a throughput; transfer is a separate question (A5). Under critics: any serial reading is a latency division (G2), which F1 shows is not a throughput bound. Both sides agree on the logic of averages; the verdict turns on A5f.

## Check
Link: `research/checks/RESULTS.md` F1. Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- Output separation: per-generation fixation rate (throughput) vs per-allele fixation time (latency); in-transit count measured directly (TODO in F1).
