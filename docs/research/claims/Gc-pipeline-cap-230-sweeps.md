---
id: Gc
title: "The active zone limits the pipeline to about 230 simultaneous sweeps, so about 157,000 fixations can occur in 300,000 generations"
side: day
branch: G
parent: G
edges: [{type: depends-on, target: G}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: non-sequitur   # no derivation given; 230 equals 157,000 x t_transit/T, so the 'match' is circular if fitted; near-candidates: additive halving 200, s6.1 ceiling 100-200
  fidelity: n/a
  external: "contested"   # falsifier not met in tested regime; ~230 concurrent sweeps persist under hard selection for R >= 5; R4 GAP-04 (post hoc): as a cap, 230 has no support in interference theory (W&B soft-selection ceiling at R/2 is 7.7-8.3e3 at s = 0.01, reached only at very large supply); as a number, 230 matches the concurrency implied by K_a ~ 1e5 (s = 0.01), 1e4 (s = 0.001) or Day's own 200,000 (349 at s = 0.01); human scale untested
---

## Statement (verbatim)
> the "active zone" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of approximately 230 simultaneous sweeps.

Source: [The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07), ¶6 (abstract).

> Working backward from the constraint, the active zone can sustain approximately 200–300 simultaneous sweeps before the Bernoulli Barrier compresses variance below the threshold required for effective selection.

Source: [The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07), ¶111 (s7.8).

> Maximum fixations ≈ (300,000 / 440) × 230 ≈ 157,000 This appears to match the requirement for human-chimpanzee divergence.

Source: [The Bernoulli Barrier, Zenodo 18167588](https://zenodo.org/records/18167588) (key Z18167588), pub. 2026-01-04 (modified 2026-01-07), ¶63 (s7.8).

## Formal statement
t_transit = (2/s)·ln 9 = 200 x 2.197 = 439.4 ≈ 440 generations (s = 0.01, 0.1 < p < 0.9); fixations ≤ (T/t_transit)·C with C = 230, T = 300,000.
`derived:` (python3 -I) 300,000/440 = 681.8; x 230 = 156,818 ≈ 157,000 (reconciles). The cap C is not derived: "working backward from the constraint" gives "200–300"; the cap that makes the product equal the paper's own n = 157,000 is 230, which is the same number that is then said to "appear to match the requirement". The requirement used elsewhere in the corpus is 20M (Z18165980) or 205M (Z23003785): 20e6/157,000 = 127; 205e6/157,000 = 1,306. The paper's own criterion (available additive differential 2z·√(n/4)·s ≥ required n·s, with z = 3.72 for N = 10,000) gives n ≤ z² = 13.8, not 230 (derived by this audit; applies the paper's s3 comparison to n loci). The paper's separate "reproductive ceiling" (s6.1: Σs ≤ 1.0–2.0) gives 100–200 loci at s = 0.01, which is closer to 230 but is a different constraint (branch H).

## Assumptions
- Stated: the constraint acts on loci with 0.1 < p < 0.9; each locus spends t_transit there; pipeline runs full and continuously (s7.9 says this is idealised).
- Implicit: the same threshold applies at every n; s = 0.01 uniform; free recombination.

## Responses
- Against: none in corpus directly. Hancock's statement (GG-13, G2c) is about a strictly serial model, not this one.
- In support: none; the paper itself flags (s7.9) that the idealised 157,000 cannot be achieved because of the drift input constraint.
- Weaknesses in the responses: no critic has asked for the derivation of 230. The conclusion that 157,000 "match[es]" the requirement is at odds with the MITTENS requirement of 20M–205M, which makes the pipeline cap about 127x–1,300x too small by the paper's own numbers (so the Barrier would be a stronger constraint than the text says, not a weaker one).

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
See G (G-sim). Prediction specific to this claim: the simulated fixation rate as a function of simultaneously active loci saturates; the saturation level is the quantity C. Under the paper's own s3 criterion C ≈ 14. Under critics: no saturation below the reproductive-capacity limit.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 F2 + H2 (research/checks/results/R4-F2-A.md, research/checks/results/R4-H2-hard.md): the Gc falsifier (P_fix < 50% of 2s at ~230 active loci, soft, free recombination) is not met in the tested regime (R_int 0.975 at 272). Under hard selection with free recombination, ~255 simultaneous open loci persist at R >= 10 (s = 0.01); at R = 2, 90 persisted and 167 did not, so ~230 concurrent sweeps persist for R >= 5. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

R4 G1 (research/checks/results/R4-G1.md): multiplicative fitness, soft selection, free recombination, N = 1000: no cap at 230. Additive-exclusive convention: 0.85x at 230 concurrent. Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

R4 GAP-04 (research/checks/results/R4-GAPS-04-07-02.md): POST HOC (`gap04_posthoc_concurrency.py`, `gap0x_posthoc_review.py`). Concurrent active-zone sweeps n_mid = Lambda * ln(81)/s (Day's own 440 at s = 0.01). At W&B's R/2 asymptote (R = 35-37.9 M) the ceiling is 7.7-8.3e3 (s = 0.01) to 7.7-8.3e4 (s = 0.001), up to 2x with interference slowing (W&B Fig. 5 conditions extrapolated); it is reached only at a beneficial supply of order U_tot. At GAP-01 rates (K_a 1e3-1e6) n_mid is 1.7-1,744 at s = 0.01; Day's 200,000 gives 349. Day's separate s6.1 reproductive ceiling (sum of s <= 1-2), untested here, would bind at K_a ~ 6e4-1.2e5 on the active zone alone. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

## Simulator variables implied
- Pipeline capacity C as a measured output of G-sim; t_transit.
