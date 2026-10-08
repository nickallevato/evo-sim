---
id: A4
title: "The Selective Turnover Coefficient d (about 0.45) reduces effective generations for selection"
side: day
branch: A
parent: A
edges: [{type: supports, target: A}, {type: depends-on, target: A4a}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model)

Source: [Zenodo 18166234](https://zenodo.org/records/18166234) (key Z18166234), pub. 2025-12-24 (modified 2026-01-06), ¶33 (s2.3).

> d = T × d_continuous = T × [∫ μ(x) × l(x) × v(x) dx / ∫ l(x) × v(x) dx]

Source: [Zenodo 18166234](https://zenodo.org/records/18166234) (key Z18166234), pub. 2025-12-24 (modified 2026-01-06), ¶51 (s3.3). μ(x) = −d[ln l(x)]/dx is the mortality force.

## Formal statement
effective generations = N_gen x d, with d = `selection.turnover_d` = 0.45.   F_max = (t_div x d)/(g_len x G_f).
`derived:` 325,000 x 0.45 = 146,250; 450,000 x 0.45 = 202,500 (the "202,500 generations" Tree of Woe interview figure, TW-01); T x mean mortality force is dimensionless (T in years, μ in 1/y), so the integral form is dimensionally consistent. Day (Q&A 2026-01-19, ¶16): "If l(x) and v(x) were constants, they'd cancel and you'd get d = T × ∫μ(x)dx. But they're not constants, they're age-dependent functions".

## Assumptions
- Stated: overlapping generations make the effective rate of allele-frequency change per nominal generation lower by d.
- Implicit: the nominal generation length used for N_gen equals the T in the definition; d is constant over the 6.3 My lineage; d is a pure multiplier on G_f, independent of s.

## Responses
- Against: Camestros (A4b): d is undefined in the introduction (later corrected: Ch.13, App. A) and would have changed during human history.
- In support: Hössjer reproduces 127 with d = 0.45 (HO-01) and applies d inside a neutral-rate calculation (A5a); Duffy presents the overlapping-generations correction (A4c).
- Weaknesses in the responses: Hössjer's use of d in the neutral rate is outside the definition above (d is defined for allele frequency change under selection); Day's MITTENS 3.0 dropped d (A4d), so the 3.0 numbers do not depend on it.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No check has run. Proposed check A4-sim: age-structured Moran or Leslie-matrix model with a human life table (Coale-Demeny West, as cited by Day), allele with fixed s; compare allele-frequency change per mean generation time T with a discrete-generation Wright-Fisher at the same s.
- Under the claimant's model: ratio of per-generation frequency change ≈ 0.45.
- Under the opposing model: the ratio is ≈ 1 when T is the mean age of parents (a generation is defined by turnover), so d ≈ 0.45 reflects a definition of T, not a slowdown.
- Result that would change a verdict: a ratio between 0.3 and 0.6 with T = mean age of reproduction.

## Check
Script: none yet. Review: pending.

## Simulator variables implied
- Life table (l(x), v(x) or fertility m(x)), generation time T; output d; toggle d on/off in F_max.
