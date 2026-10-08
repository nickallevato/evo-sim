---
id: A1
title: "Generations available since the split: about 252,000 (6.3 My at 25 y)"
side: day
branch: A
parent: A
edges: [{type: depends-on, target: A1a}, {type: depends-on, target: A1b}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.11 (s7.1).

## Formal statement
N_gen = t_div_years / generation_time_years = 6.3e6 / 25 = 252,000   (`divergence.t_div_years.day_2026_mittens3`, `generation_time_years.day_2026`, `generations_available.day_2026`)

`derived:` version history of the same quantity:

| Version | t_div | g_len | N_gen | Note |
|---|---|---|---|---|
| 2019 | 9.0e6 | 20 | 450,000 | B2019-02-07 |
| 2025 | 6–7e6 (6.5e6) | 20 | 300,000–350,000 (325,000) | Z18165980, Q12 |
| 2025 effective | — | — | 325,000 x 0.45 = 146,250 | with d (A4) |
| 2026 3.0 | 6.3e6 | 25 | 252,000 | Z23003785 |
| alt. | 6.3e6 | 32.5 | 193,846 | parameters.yaml `day_alt` (B2025-01-18, not re-verified here) |

All arithmetic reconciles. Range over the sources: 169,231 (5.5 My, 32.5 y) to 450,000 (9 My, 20 y), a factor of 2.7.

## Assumptions
- Stated: 6.3 My divergence time and 25 y generation length.
- Implicit: constant generation length over the whole lineage; t_div applies to the whole genome (population split later than the species split by an ancestral-coalescence term, which would add mutational time, not remove it; see A1a).

## Responses
- Against: none engaged the 252,000 figure as an error. Keruru and Hössjer use 300,000 and 450,000 in their own recalculations (KR-08, HO-04), i.e. more generations, not fewer.
- In support: Duffy and DeDzjang both recompute 6.3e6/25 = 252,000 (DZ-02).
- Weaknesses in the responses: Day's own later statement (2026-05-07) moves the CHLCA to 250 kya–1.3 Mya, which is incompatible with 6.3 My; see A1c. Day's 2019 value (9 My, 20 y) is not a "generous" choice relative to the current 6.3 My, since it gives 1.8x more generations.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo et al. 2025 | "Our analyses dated the human-chimpanzee split between 5.5 and 6.3 million years ago" | verified-accurate (see ledger) |
| Langergraber et al. 2012 | "We date the human-chimpanzee split to at least 7-8 million years" | verified-misread when cited for 6–7 My |

## Pre-registered prediction
No check yet. The result is arithmetic and is already recorded above.
- Under the claimant's model: 252,000 generations.
- Under the opposing model: 220,000–450,000 depending on source; conclusions insensitive to the factor of 2.7.
- Result that would change a verdict: a sourced g_len for the ancestral hominin lineage substantially above 32.5 y.

## Check
Arithmetic audit (python3 -I, scratch): all rows reconcile. Review: pending.

## Simulator variables implied
- `t_div_years` (5.5e6 to 9e6), `generation_time_years` (20 to 32.5), derived `N_gen`.
