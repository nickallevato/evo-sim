---
id: A4d
title: "MITTENS 3.0 drops d and uses 252,000 nominal generations"
side: day
branch: A
parent: A4
edges: [{type: revises, target: A4}, {type: supersedes, target: A}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> Applied to human-chimpanzee divergence (205 million required fixations on the human lineage across 252,000 available generations), the shortfall is 1,075,000-fold for non-mutators and 104,873-fold across all twelve populations including hypermutators.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.1 (abstract). The 3.0 text has no d term (searched "turnover" and "d =").

## Formal statement
F_max(3.0) = 252,000 / 1,322 = 190.6, with no d. `derived:` had d = 0.45 been applied: 252,000 x 0.45 = 113,400; /1,322 = 85.8; shortfall 205e6/85.8 = 2.39e6 (2.2x larger than 1.075e6). Dropping d is therefore conservative with respect to the claim. The versions ledger notes d = 0.45 in both Zenodo papers of Dec 2025 computed on different loci (A4a).

## Assumptions
- Stated: none (d is not mentioned).
- Implicit: nominal generations are the right unit; or the d correction is subsumed into the empirical G_f (the LTEE is asexual and discrete).

## Responses
- Against: Hössjer (HO-01, HO-04) still uses d = 0.45 in his reproduction (published 2026-09-14, before 3.0).
- In support: Camestros's objection to d (A4b) no longer applies to the 3.0 numbers.
- Weaknesses in the responses: the 3.0 paper offers no reason for dropping d; the later "Appendix D" human-derived rate (A5e) cites the "Bio-Cycle correction for overlapping generations", so the correction is still invoked in 3.0 elsewhere.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Arithmetic only (above).

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- d toggle (already specified in A4).
