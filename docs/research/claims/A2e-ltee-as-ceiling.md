---
id: A2e
title: "The LTEE rate is an empirical ceiling on what evolution can accomplish, so the human shortfall is a lower bound"
side: day
branch: A
parent: A
edges: [{type: supports, target: A}, {type: depends-on, target: A2}]
load_bearing: true   # If the LTEE rate is not a ceiling for humans, the shortfall in A has no basis and ROOT loses its selection-rate branch.
sourcing: firsthand
status: checked
verdicts:
  internal: non-sequitur
  fidelity: pending
  external: contested
---

## Statement (verbatim)
> Whatever number the LTEE produces, it is the empirical ceiling on what evolution can accomplish when every tool in its kit is deployed simultaneously under ideal conditions.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.2.

> The LTEE rate is therefore not an estimate for complex organisms. It is an unattainable ceiling, the absolute best-case scenario, the performance of a Formula One car used to benchmark a horse-drawn cart.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.4.

## Formal statement
Claim: rate_human <= rate_LTEE = 1/G_f (per generation), with no scaling. Equivalent form: `ltee.gens_per_fixation` is a lower bound on human G_f.

Check against the paper's own numbers (`derived:`):
- Mutation supply per genome per generation: LTEE 4.1e-4 (s4.3); human 38.4 = 3.2e9 x 1.2e-8 (s6.4). Ratio 93,659 (python3 -I). The same paragraph that calls the LTEE the ceiling lists "an effectively unlimited mutation supply" among its advantages (p.4), which these two figures do not support.
- Mutator populations in the same experiment run 8.5x–17x faster than the ceiling (A2d), so the ceiling is exceeded inside the LTEE.
- Day's own conclusion that a 100x mutation increase gives only 8.5x–17x (A5d) is evidence for sublinear but non-zero response to supply; it does not show response is zero.

## Assumptions
- Stated: the LTEE has larger Ne, shorter generation, stronger selection, no mate-finding cost, no recombination overhead, and effectively unlimited mutation supply (p.4).
- Implicit: that "no recombination overhead" is an advantage rather than a handicap (clonal interference, A5f); that per-generation fixation rate is bounded by the highest value in one experimental system.

## Responses
- Against: Hössjer scales by mutation rate and genome length and finds a ~2x residual (A5a); the KITTENS authors find parity (A5b); Camestros (CA-08): "if humans reproduced in the way e.coli reproduce then maybe humans would never have evolved"; r/DebateEvolution (RE-07): the LTEE is largely nonrecombining, one clone, one environment (A5f). Gariépy (GA-01, secondhand): fixation rate in single-celled organisms is not equal to that in mammals because of sex and population-size variability.
- In support: Hössjer (HO-06) agrees with the conclusion after adjustment; American Hypnotist (AH-01) asserts the simple-organism rate must be faster than complex organisms (no calculation); Duffy (DU-06) says mammal fixation "way slower" (no numbers).
- Weaknesses in the responses: critics' linear scaling is an illustration (RE-09); Hössjer's Haldane step to restore the gap is asserted not computed (HO-03); the ally statements AH-01, DU-06 give no numbers; Day's ceiling claim is an extrapolation from one system.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon et al. 2016 | six hypermutable populations carried 96.5% of the point mutations; neutral mutations accumulate at constant rate in non-mutators | verified |
| Good et al. 2017 | many beneficial variants compete simultaneously; trajectories inconsistent with periodic selection | verified (main text) |

## Pre-registered prediction
No check has run (queued as A-sim in the file for A). 
- Under the claimant's model: adaptive fixation rate per generation saturates at about the LTEE value regardless of mutation supply and recombination.
- Under the opposing model: with recombination, rate grows with supply until Hill-Robertson/depletion limits, so the human rate exceeds the LTEE rate at 94,000x supply.
- Result that would change a verdict: a forward simulation in which fixation rate per generation, at fixed s and N, rises by more than an order of magnitude when supply rises by 1e4–1e5 with recombination on.

## Check
Script: none yet. Internal verdict is from the paper's own tables (above). Review: pending.

## Simulator variables implied
- Supply (U per genome), recombination rate, population size, s distribution; output fixations per generation compared to 1/G_f.
