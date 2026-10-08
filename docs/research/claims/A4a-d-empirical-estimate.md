---
id: A4a
title: "d ≈ 0.45 ± 0.08 estimated from ancient-DNA time series at three loci (loci differ between two papers)"
side: day
branch: A
parent: A4
edges: [{type: depends-on, target: A4}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # arithmetic reproduces from Day's s priors; d not identifiable apart from s, onset, T, dominance
  fidelity: unverifiable
  external: "contested"   # not identifiable (C2d)
---

## Statement (verbatim)
> Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2.

Source: [Zenodo 18165980](https://zenodo.org/records/18165980) (key Z18165980), pub. 2025-12-28, ¶69 (Methods).

> Day and Athos (2025a) estimated d empirically from ancient DNA time series, finding d ≈ 0.45 from three independent loci (LCT, SLC45A2, TYR).

Source: [Zenodo 18166234](https://zenodo.org/records/18166234) (key Z18166234), pub. 2025-12-24 (modified 2026-01-06), ¶5.

## Formal statement
d = 0.45 ± 0.08 (`selection.turnover_d`). Two papers published four days apart give the same value from different locus sets: {LCT, SLC24A5, HERC2} (Z18165980) and {LCT, SLC45A2, TYR} (Z18166234). The record cannot say whether one is a typo or whether both sets give 0.45 (versions ledger).

## Assumptions
- Stated: aDNA allele-frequency time series (Mathieson et al. 2015 panel).
- Implicit: d is estimated by comparing observed frequency change with a predicted discrete-generation change, so it requires a known s per locus; the s values are not given in the quotes.

## Responses
- Against: Mathieson 2015 states the SLC24A5 rise "mostly" reflects migration, not selection, so SLC24A5 cannot supply a selection-based d. The main text of Mathieson gives no s values.
- In support: none in corpus.
- Weaknesses in the responses: the critics have not recomputed d. Day has not reconciled the two locus lists.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Mathieson et al. 2015 | "The strongest signal of selection is at the SNP (rs4988235) responsible for lactase persistence in Europe"; SLC24A5 "was mostly due to migration" | verified; no s values in main text or ED legends: **unverified** for Day's use |

## Pre-registered prediction
Not run. Prediction (claimant): recomputing d from the Mathieson 2015 or AADR data at LCT gives 0.45 ± 0.1. Prediction (opposing): the estimate depends on the assumed s and on migration, with a range spanning 0.2–1.

## Check
No script. Review: pending.

R4 C2d (research/checks/results/R4-H-C2.md, `c2_ratio_nonident.py`): three trajectories, four unknowns: an exact fit exists for every d. Day's own published s ranges (LCT .04-.10, SLC45A2 .04-.05, TYR .02-.04) give d in [0.481, 0.568]; scaling the ranges by 0.75 / 1.25 moves it to [0.638, 0.756] / [0.387, 0.456]. The 0.45 comes from priors on s, not from the trajectories. Equivalent alternatives: onset 2,100-3,100 y later, generation length 51-66 y, or dominance (LCT dominant needs d = 0.745). Critic-side note: at d = 1 the required s (LCT 0.024) is below the published ranges, an anomaly the critics have not explained. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- None directly.
