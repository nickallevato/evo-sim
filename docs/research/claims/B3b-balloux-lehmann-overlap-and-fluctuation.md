---
id: B3b
title: "Balloux & Lehmann 2012: k depends on N under overlapping generations plus fluctuating demography"
side: day
branch: B
parent: B3
edges: [{type: supports, target: B3}, {type: depends-on, target: B3c}]
load_bearing: false  # the only B3 leg with literature support; but magnitude (0.743, 32.3) is not from the paper
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # B&L effect reproduced
  fidelity: partial
  external: "supported"   # qualitatively (k != mu with overlap + fluctuation); human-scale size -2% to +38%, sign upward; cannot give 0.743 or 32.3
---

## Statement (verbatim)
> Balloux and Lehmann (2012) demonstrated that under the joint conditions of fluctuating demography and overlapping generations, conditions which are satisfied by every natural population of interest, k ≠ μ.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §6 The Irrelevance

> we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations

Source: [Balloux & Lehmann 2012, Substitution rates at neutral genes depend on population size under fluctuating demography and overlapping generations, Evolution 66:605-611](https://serval.unil.ch/notice/serval:BIB_2B87D605B70D), 2012, Abstract

> population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations

Source: [Balloux & Lehmann 2012, Substitution rates at neutral genes depend on population size under fluctuating demography and overlapping generations, Evolution 66:605-611](https://serval.unil.ch/notice/serval:BIB_2B87D605B70D), 2012, Results, "Overlapping generations without fluctuating demography"

## Formal statement
Literature: B&L give k = μ(1 − s) for constant survival s (overlap alone, per time step; see quote below) and N-dependence only when overlap and fluctuation co-occur. Neither "0.743" nor "32.3" appears in the text.
Parameters: none in parameters.yaml; propose `new: demography.survival_s`, `new: demography.N_cycle`.

**Proposed check B3b (not yet run; pre-registered here):**
- Model: age-structured (Moran-type) population, survival s ∈ {0, 0.5, 0.9}, N(t) either constant, cyclic between N₁ and N₂ with period P, or monotone growth by a factor 3.3 over 3 generations (the RRME example), neutral alleles with infinite-sites mutation; run until the long-run substitution count is stable; report substitutions per time step, per average generation time, and per newborn.
- Predictions: (i) s = 0, any N(t): k = μ per generation (B&L, quoted); (ii) s > 0, N constant: k = μ(1 − s) per time step and k = μ per average generation time (Lehmann 2014 as paraphrased in Z18525262; that paper not retrieved); (iii) s > 0 with fluctuating N: k departs from (ii) by an amount set by the N(t) statistics (B&L). RRME predicts k/μ = 0.74 for non-overlapping growth, so (i) is a direct test of B3c.
- Would change the verdict: finding (i) violated (k ≠ μ for non-overlapping fluctuating N) supports Day; finding (iii) with a departure ≤ a few percent for human-like parameters means the effect cannot produce factors of 0.74 or 32.3.

## Assumptions
- Stated: Overlapping generations and fluctuating N are "satisfied by every natural population of interest".
- Implicit: The B&L effect is large enough for humans to matter; the unit of time is calendar generations (Lehmann 2014 argues that in average-generation-time units k = μ).

## Responses
- Against: Ledger: under non-overlapping generations fluctuations "do not affect substitution rates at neutral loci"; Lehmann (2014) as paraphrased by Day himself restores k = μ in average generation-time units.
- In support: B&L abstract confirms the existence of the effect.
- Weaknesses in the responses: Day's own text calls Lehmann's redefinition "mathematically legitimate but biologically circular" without testing it; the corpus contains no independent simulation of B&L.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Balloux & Lehmann 2012 | "introducing overlapping generations reduces the substitution rate as fewer age class one individuals are produced per generation and therefore mutants." | verified-partial |
| Balloux & Lehmann 2012 | "One of the central results of the Neutral Theory of evolution ... states that the rate k of allele substitution (rate of evolution) at neutral loci is unaffected by fluctuations in population size and is simply equal to the mutation rate." | the standard result B&L qualify |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: k/μ departs from 1 with a magnitude set by the demographic history.
- Under the opposing model: k = μ for non-overlapping generations; modest departure for overlap plus fluctuation; no departure of order 0.74 or 32 for humans.
- Result that would change a verdict: See Formal statement (check B3b).

## Check
R4 B3b (`b3b_overlap_fluctuation.py`, 16 reps; research/checks/results/R4-B3b-C1.md): B&L 2012 eq. (3) reproduced by independent individual-based simulation in 9 scenarios (all |z| < 1.6); fluctuation without overlap gives k = mu exactly. At human-like parameters (exact eq. 3, s = 0.96/yr): symmetric cycles -0.3% to -2%; one-way growth raises the arrival rate of eventual fixers by 1.38x (transient); contrived two-state range 0.59-1.70, with k < mu only for an unrealistic survival ordering. Credit to Day: the effect exists and Kimura's k = mu is not exact with overlap (critics' blanket k = mu is a discrete-generation result). Against Day: the realistic sign is upward and the size cannot give 0.743 or 32.3. Open: per-generation-time normalisation (0.81-1.11 under strong fluctuation; Lehmann 2014 not retrieved). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: proposed `research/checks/b3b_overlap_fluctuation.py` (not yet written) · Result: none. Queued in REVIEW.md "Queue".

## Simulator variables implied
- survival s / age structure
- N(t) schedule
- time unit for k
