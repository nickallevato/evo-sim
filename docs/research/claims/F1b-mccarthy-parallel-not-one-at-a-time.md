---
id: F1b
title: "McCarthy: mutations do not increase in frequency one at a time; the expected count has no queue"
side: critic
branch: F
parent: F1
edges: [{type: attacks, target: F}]
load_bearing: false  # same logical point as F1, embedded in McCarthy's time-adjusted calculation (B5a)
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: supported   # R4 F1b: in-transit overlap measured (independent loci, no interference; beneficial s = 0.01 only); feasibility at human scale untouched (F2, H)
---

## Statement (verbatim)
> Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time.

Source: [McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 22

## Formal statement
McCarthy's time-adjusted count: (450,000 − 50,000) × 50 = 20M (B5a). Day's reply (R2) restates it and answers with the Bernoulli Barrier (branch G) and the N/Nₑ correction (B3e, retracted B3g).

## Assumptions
- Stated: Fixations overlap in time.
- Implicit: Independent loci.

## Responses
- Against: Day (G): the probability that millions of in-transit mutations all complete is astronomically small (Bernoulli Barrier; not assessed here).
- In support: RESULTS F1.
- Weaknesses in the responses: Day's argument that "expected value is the average over infinite trials" confuses the expected count with the requirement; for 20M fixations, the Poisson sd is ≈ 4.5 thousand (derived), so the count is concentrated (branch G).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Overlap is routine.
- Under the opposing model: (Day) overlap capped by selection cost/variance (G, H).
- Result that would change a verdict: F2.

## Check
Script: `research/checks/f1_throughput.py`.

R4 F1b (research/checks/results/R4-F1b.md; review #16, combined, 2026-10-09): measured overlap in three regimes (333, 17 and 1.0 alleles in transit; overlap in 26% of generations even at the serial boundary). External contested -> supported for independent loci with no interference or cost, genic beneficial alleles only; neutral alleles are argued, not simulated.

## Simulator variables implied
- parallel width
