# Milestone 2: First checks and three rounds of review
*2026-10-07 · stage: R4 begins · commits `3d888e9`, `36a7ff9`, `c8aaed3`, `63ac339`*

These checks ran *before* the corpus harvest finished, so their framing relied on quotes from the pass-1 survey. Milestone 3 shows how the verbatim text later changed that framing. This post states each check as it was reviewed at the time and notes where later material bears on it.

## Textbook baselines (B0): all pass
Before testing anyone's claim, the simulation code had to reproduce standard results:

| Check | Simulated | Target |
|---|---|---|
| Neutral fixation probability | 0.00989 and 0.00246 | 1/2N: 0.01 and 0.0025 |
| Conditional fixation time | ≈ 3.9N–4.0N | diffusion value |
| Kimura's u(s, N) | matches | within 1.2 standard errors |
| Neutral substitution rate at equilibrium | k = U | at N = 50 and N = 200 |

If these had failed, nothing downstream would mean anything.

## Fixation time of a beneficial mutant (B0.4)
- Day uses (2/s)·ln(2N), which gives 19,807 generations at N = 10⁴ and s = 0.001.
- The simulation and the diffusion integral give **8,480**.
- The approximation Day uses is a standard deterministic one, but it overstates the time to fixation, conditioned on fixing, by about 2.3×.
- **Scope note:** this is a *latency*, the time one allele takes to fix. Whether latency limits throughput is a separate question.

## The "empty pipe" (B1)
Day's "Intrinsic Irrelevance" paper writes the expected number of fixations as E[F(T)] = μL∫F_X, which tends to μL(T − 4Nₑ).

| Start state | Result |
|---|---|
| Empty: no standing variation | The simulation matches Day's formula at every T. **Internal: holds.** |
| Mutation–drift equilibrium | The simulation gives μLT, with no deficit. |

The review insisted on two caveats:
- The empty-start match holds by construction.
- An empty pipe means zero heterozygosity, which contradicts observed human diversity. So the empty start is a counterfactual boundary case.

The open question became which start state applies.

## N vs Nₑ (B3)
In an exchangeable population model, lowering Nₑ (by raising the variance in offspring number from 1 to 10.7):
- left the fixation probability at 1/2N;
- scaled the fixation time with Nₑ (t_fix/Nₑ ≈ 4.0 throughout).

**Result:** Day is right that Nₑ sets the timescale, and wrong that it sets the probability. The review noted that in this model class the result is a theorem, since allele frequency is a martingale. That made Day's strongest form of the claim the obvious next test: overlapping generations plus fluctuating N, the Balloux–Lehmann setting. That test (B3b) waited until Milestone 5.

## Size changes (B1b)
The Day-side steelman pointed out that Day's real claim concerns *changes* in population size, not the two extreme start states. The check started from equilibrium:
- **Expansions:** a transient deficit, which is Day's direction.
- **Contractions:** a transient excess.
- **Bottlenecks:** roughly zero net effect.

The net effect is bounded by 4ΔN/T, and an analytic cross-check matched (1.267 vs 1.259; 0.733 vs 0.733). Review #3 removed an early "credit to Day": the mechanism is standard theory, and its sign is wrong for contractions. It also pointed out that pairwise *divergence* is a different observable from fixed substitutions. Both points forced checks B1c and B4a.

## Hard Limits tail (B2a)
Exact Wright–Fisher chains, with no randomness, show that Day's exponent −π²Nₑ/G is the correct leading-order tail. An empirical prefactor of about 50·(G/N)^−1.5 sits in front of it.
- Whether Day's number over- or understates depends on whether it is conditional on fixation. The pass-1 quote did not settle which.
- A fairness note was added: Day presents the formula as "of order", and judging its prefactor is harsher than that framing warrants.
- **Relevance:** the result is a per-allele latency tail, not a throughput bound.

## Latency vs throughput (F1)
- **Setting:** independent loci with no interference.
- **Result:** the substitution rate is 0.397 per generation (predicted 0.396), while a single fixation takes 847 generations.
- **Conclusion:** dividing time by latency does not bound throughput.
- **Review #3 caveats:** this shows pipelining is *possible*, not *feasible* at realistic parameters. Attributing the "serial" reading to anyone needs a quote. Day explicitly describes the LTEE figure as a throughput.

## What the reviews changed
| Review | What it found | Result |
|---|---|---|
| #1: two-sided steelman | Five new Day-side tests and six critic-side gaps | Created B1b, B2a, B3b, B4a, C1, F1 and F2 |
| #2: correctness | No simulation bugs. One blocker (an import under `python -I`), one major (a flat-4N baseline target) and several minors | All fixed |
| #3: correctness + steelman | Wording and framing problems | Fixed, including overcrediting Day on B1b and the B2a limit order |

## Reading this in hindsight
Two things learned in Milestone 3 change how these results read:
1. Kimura 1962 and Kimura & Ohta 1969 were checked from PDFs. Both state 1/2N for the neutral fixation probability. Day's own record shows a concession on k = μ on 2026-08-27.
2. Day wrote on 2026-10-01 that the ancestral pipe was "full, but much shorter". That moves the dispute from "empty vs full" to "how full, and of what size", which B1c and B4a then tested.
