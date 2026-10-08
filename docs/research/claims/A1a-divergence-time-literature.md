---
id: A1a
title: "Independent dating of the human-chimp split: 5.5–6.3 My (Yoo), at least 7–8 My (Langergraber), about 6 My (Scally)"
side: literature
branch: A
parent: A1
edges: [{type: supports, target: A1}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: partial
  external: supported
---

## Statement (verbatim)
> Our analyses dated the human-chimpanzee split between 5.5 and 6.3 million years ago (Ma; minimum to maximum estimate of divergence)

Source: Yoo et al. 2025 (key Yoo2025), main text, "Divergence and selection".

> We date the human-chimpanzee split to at least 7-8 million years and the population split between Neanderthals and modern humans to 400,000-800,000 y ago.

Source: Langergraber et al. 2012 (key Langergraber2012), Abstract.

> We propose a synthesis of genetic and fossil evidence consistent with placing the human-chimpanzee and human-chimpanzee-gorilla speciation events at approximately 6 and 10 million years ago (Mya).

Source: Scally et al. 2012 (key Scally2012), Abstract.

## Formal statement
Literature values for `divergence.t_div_years`: yoo_2025 [5.5e6, 6.3e6] (verified), langergraber_2012 ">=7e6-8e6" (verified), Scally ~6e6. Day 2026 uses 6.3e6 (the Yoo maximum); Day's earlier papers cite Langergraber for 6–7 My.

## Assumptions
- Stated by the papers: each uses its own calibration. Langergraber states independence from fossil calibration.
- Implicit: molecular dates depend on mutation-rate calibration, which Hössjer (HO-05) and McCarthy (MC-12) say is partly neutral-theory based (branch B4, circularity).

## Responses
- Against (Day side): the molecular-clock recalibration claims (B4) put the CHLCA at 200–580 kya, 68 kya, or 250 kya–1.3 Mya (see A1c).
- In support: Hössjer and McCarthy both treat the date as circular in the sense that it uses a neutral rate (B4); this affects Day's use of the date and the critics' use of neutral rates symmetrically.
- Weaknesses in the responses: neither HO-05 nor MC-12 gives a citation; the ledger notes pedigree rates are independent of divergence data.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo2025 | 5.5–6.3 My | verified-accurate |
| Langergraber2012 | ">=7–8 My", independent of fossil calibration | verified; Day's use as 6–7 My is a misread |
| Scally2012 | about 6 My | verified (abstract) |

## Pre-registered prediction
No check needed; descriptive.
- Prediction: a sensitivity of the shortfall to t_div in [5.5, 8] My changes the shortfall by a factor <= 1.5 (derived: 8/5.5 = 1.45).

## Check
No script. Review: pending.

## Simulator variables implied
- Preset list of t_div values with citation keys.
