---
id: F1
title: "Mansfield: time to fix one allele is not important; the time between successive fixations is (latency is not throughput)"
side: critic
branch: F
parent: F
edges: [{type: attacks, target: F}, {type: attacks, target: B2d}]
load_bearing: true  # if latency bounded throughput, Day's serial reading would hold; F1 says it does not
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important.

Source: [Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbR9n0iZNuQ (Mansfield; truck analogy NY–LA follows)

> Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time.

Source: [McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 22 (McCarthy)

## Formal statement
Little's law: in-flight count = arrival rate × latency; throughput = arrivals × P_fix independent of latency. For independent loci, rate = 2N·U_b·u(s) (Kimura 1962) and G_f = 1/rate.
RESULTS F1 (N = 1000, s = 0.01, U_b = 0.01): predicted 0.3960 per generation; simulated 0.3972 ± 0.0018; t_fix = 847 generations but G_f = 3; in-transit ≈ 336 (computed as rate × latency, **not measured**).

## Assumptions
- Stated: Many alleles in transit at once (truck analogy).
- Implicit: Independent loci, no interference, no cost of selection (RESULTS caveats).

## Responses
- Against: Day (F1a): his throughput number already includes parallelism; feasibility is limited by cost/interference (F2).
- In support: RESULTS F1.
- Weaknesses in the responses: RESULTS caveat: the parameters (20 new beneficial mutations per generation, 0.4 substitutions per generation) are far above any realistic regime and avoid selective load by construction, so pipelining is shown possible, not feasible. Mansfield's comment was made before Day's reply, and quotes Day only via a paste.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | u(s) formula used for the rate | accurate |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS F1; the check has run).
- Under the claimant's model: (Mansfield) Steady-state rate = 2N·U_b·u(s), independent of latency.
- Under the opposing model: (Day, weak form) Count ≤ window / latency.
- Result that would change a verdict: In-transit count measured directly (TODO); F2 for interference.

## Check
Script: `research/checks/f1_throughput.py` (seed 31) · Result: rate confirmed (0.3972 ± 0.0018 vs 0.3960); spacing vs latency 3 vs 847 generations; in-transit count is Little's law, not measured. Verdict: as logic, dividing elapsed time by latency is not a throughput bound; feasibility is untested (F2). Review #3 caveats (unrealistic regime; serial reading must be tied to a quote → F1a). Review: `research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`

R4 F1b (research/checks/results/R4-F1b.md; review #16, combined, 2026-10-09): the open item is closed. In-transit count measured directly (infinite-sites WF, N = 1000, s = 0.01, independent loci): 333.3 +- 0.9, 17.07 +- 0.18, 0.984 +- 0.022 against theory 335.5, 16.8, 1.01; Poisson dispersion (variance/mean 0.95-1.00); the weak form (count <= window / latency) is violated 333x and 17x in the first two regimes and is an equality at the serial boundary. Feasibility (interference, cost, human supply) is untouched, so verdicts stay holds / n/a / contested.

## Simulator variables implied
- number of independent loci
- U_b
- s
- latency/in-transit display (measure, not compute)
