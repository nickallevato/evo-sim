---
id: A1b
title: "Generation length: chimpanzee about 24–25 y; Day uses 20 y (2019) and 25 y (2026)"
side: literature
branch: A
parent: A1
edges: [{type: supports, target: A1}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> The average generation time for the former communities was 24.9, whereas it was 24.3 for the latter.

Source: Langergraber et al. 2012 (key Langergraber2012), Results (chimpanzee generation time). The two groups are chimpanzee communities with and without high infection-induced mortality.

Day, secondhand within his own Q&A, uses another figure: "T = 22 years (generation, Gurven & Kaplan 2007)" ([Probability Zero Q&A](https://voxday.net/2026/01/19/probability-zero-qa/), 2026-01-19, ¶5).

## Formal statement
`generation_time_years`: day_2019 = 20, day_2026 = 25, day_alt = 32.5, Q&A = 22; Langergraber: 24.3–24.9 (chimpanzee). `derived:` 6.3e6/24.9 = 253,012; 6.3e6/20 = 315,000; 6.3e6/32.5 = 193,846.

## Assumptions
- Stated: generation length averaged over the lineage.
- Implicit: the same g_len for the human and chimp branches and for the ancestor.

## Responses
- Against: none in corpus.
- In support: the 25 y value agrees with the chimpanzee measurement (24.3–24.9).
- Weaknesses: only chimpanzee data in the repo; no sourced figure for the human lineage or ancestors, and Day's 32.5 y alternative is unquoted here.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Langergraber2012 | 24.9 / 24.3 y for chimpanzee communities | verified |

## Pre-registered prediction
No check needed. Prediction: no plausible g_len moves N_gen outside 190,000–320,000 (derived).

## Check
No script.

## Simulator variables implied
- `generation_time_years` input.
