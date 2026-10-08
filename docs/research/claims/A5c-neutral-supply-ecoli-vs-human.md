---
id: A5c
title: "Hancock: on neutral supply alone E. coli expects ~4e-5 fixations per generation (22,000 gens per fixation) and humans dozens per generation"
side: critic
branch: A
parent: A5
edges: [{type: attacks, target: A2e}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> you only expect four e to the neg5 mutations to fix per generation.

Source: [Gutsick Gibbon and Zach Hancock video](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:53:50 (GG-07; auto-caption).

> under neutrality, it should take like 22,000 generations to fix one mutation.

Source: same video, t=01:54:12 (GG-08).

## Formal statement
E. coli neutral rate = μ_E · L_E: with μ = 1e-11 per site (Hancock) and L = 4.6e6, 4.6e-5 per generation → 1/4.6e-5 = 21,739 generations per fixation (reproduces "22,000"). With the measured 8.9e-11 (McCarthy via Wielgoss 2011): 4.1e-4 per generation → 2,439 generations per fixation.
`derived:` (python3 -I) The MITTENS 3.0 s4.3 text itself uses the neutral identity for the LTEE: "expected number of neutral hitchhikers is μ_genome × G" = 4.1e-4 x 50,000 = 20.5 (Z23003785 p.7). The same formula for humans: 38.4 x 252,000 = 9.68e6 neutral substitutions per lineage over 252,000 generations, the figure KITTENS also reports (9.7M). Against R_SNV = 17.5M: 0.55 (factor 1.8). Day contests k = μ for humans (B3, B5).

## Assumptions
- Stated: neutral substitutions occur at the mutation rate per genome per generation (k = μ).
- Implicit: all mutations are neutral for the neutral estimate (an upper bound on the neutral share); the human rate 1e-8 per site per generation is per haploid genome.

## Responses
- Against (Day): 3.0 s8.2 argues the drift channel is "off" in the LTEE (Ne ≈ 3e7) and that k = μ holds in the LTEE through hitchhiking; in humans Ne = 10,000–33,000 gives 4–13 neutral fixations over 252,000 generations (serial division of time by fixation time, G2); k ≠ μ in humans (B3).
- In support: Day's own s4.3 hitchhiker formula; Tenaillon 2016 constant-rate accumulation.
- Weaknesses in the responses: Hancock's 1e-11 is below the measured 8.9e-11 (balance ledger); his "back of the napkin" calculation (GG-16) has no confidence interval; Day's 4–13 neutral fixations over 252,000 generations is a serial calculation (252,000/66,000 = 3.8, 252,000/20,000 = 12.6).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon 2016 | neutral mutations accumulate at a constant rate in non-mutators | verified |
| Kimura 1962 / Kimura & Ohta 1969 | neutral fixation probability 1/2N; time 4Ne | verified (see B-claims) |

## Pre-registered prediction
Covered by B-branch checks (B0.5: neutral k = U at equilibrium; B1/B1b). Result from RESULTS.md B0.5: simulated neutral k 0.05018 (N=50) and 0.04964 (N=200) vs U = 0.05 (z = +0.13, −0.64), i.e. k = U for any N at equilibrium. B1b: expansion produces a transient deficit of about 4N_new generations (cumulative 0.733 of U·T at N0/5→N0); contraction an excess.

## Check
Link: `research/checks/RESULTS.md` B0.5, B1, B1b. Arithmetic audit (python3 -I, scratch).

## Simulator variables implied
- Mutation rate, genome length, N, demographic history (B1b), neutral fraction.
