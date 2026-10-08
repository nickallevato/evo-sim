---
id: B1b
title: "k = mu holds only after one size is held for ~4Ne generations (size-change transients)"
side: day
branch: B
parent: B1
edges: [{type: supports, target: B1}, {type: depends-on, target: B1c}]
load_bearing: false  # the direction (deficit vs excess) is empirical (B1c); the mechanism is standard theory
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> it holds only after a population has held one size for the roughly 4N ₑ generations a neutral allele needs to drift from a single copy to fixation.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)

> Interrupt that condition and the far end delivers whatever the near end was feeding it 4Nₑ generations back, not what it is feeding it now.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Transit Time

## Formal statement
After a step change in size, the per-window substitution rate k_w/μ departs from 1 for ≈ 4N_new generations; the cumulative excess or deficit ≈ μL·4ΔN (expansion: deficit; contraction/bottleneck: excess), long-run mean = μ.

Day's claim, read narrowly (a statement about transients), is the standard result. Read broadly (a deficit whenever N has not been constant for about 4Nₑ generations) it holds only for expansions (RESULTS B1b).

## Assumptions
- Stated: Population size history determines the fill state of the pipeline.
- Implicit: The relevant history is a monotone expansion; the pipeline emptied by past events is not refilled by contractions.

## Responses
- Against: RESULTS B1b: contractions give an excess, bottlenecks and founder events net ≈ 0; no critic in the corpus engaged this directly.
- In support: Expansion lag confirmed: cumulative/UT 0.733 for N0/5→N0 (analytic 0.733).
- Weaknesses in the responses: Only a within-lineage fixation count is tested; the human–chimp observable is pairwise divergence (B4a).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: (RESULTS B1b) Deficit whenever N has not been constant for ≈4Nₑ.
- Under the opposing model: (RESULTS B1b) Contraction gives a transient excess, expansion a transient deficit of about 4N_new generations; long-run k = U.
- Result that would change a verdict: Sourced history (B1c) showing contraction or constancy over the 252,000-generation window.

## Check
Script: `research/checks/b1b_demography.py` (seed 21) · Result: N0=500, U=0.2, 24 replicates, T = 3×4N0. Cumulative/U·T: constant 0.996; contraction N0→N0/5 1.259 (analytic 1.267); expansion N0/5→N0 0.733 (analytic 0.733); expansion N0/5→5N0 0.085 (saturating); bottleneck 0.999; founder 0.996. Verdict: half right (right for expansions, wrong in sign for contractions); mechanism is standard theory. Review: `research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`

## Simulator variables implied
- Nₑ(t) piecewise schedule
- scenario presets: bottleneck, expansion, contraction, founder
- window length in units of 4Nₑ
