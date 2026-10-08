---
id: B3c
title: "Real Rate of Molecular Evolution: k = mu × (sum N_i^2 / sum N_i) / N_t = 0.743 mu"
side: day
branch: B
parent: B3
edges: [{type: supports, target: B3}, {type: depends-on, target: B3b}]
load_bearing: false  # feeds the molecular-clock direction claim (dates older) that conflicts with B4
sourcing: firsthand
status: reviewed
verdicts:
  internal: "non-sequitur"   # arithmetic holds; fixation probability taken as 1/(2N_t), simulation gives 1/N at birth
  fidelity: "misread"   # B&L sign opposite
  external: "contradicted"   # 0.743 is a window artefact (0.60-0.87, limit 0.598)
---

## Statement (verbatim)
> k = μ × 6.091/8.2 = 0.743μ (3)

Source: [Z18525262, The Real Rate of Molecular Evolution (Day & Athos)](https://zenodo.org/records/18525262), Zenodo 2026-02-08 (v2; v1 Z18517618 2026-02-07 is byte-identical), ¶58 of extracted text

> k_{i} = M_{i} × 1/(2N_{t}) = 2N_{i}μ × 1/(2N_{t}) = μN_{i}/N_{t}

Source: [Z18525262, The Real Rate of Molecular Evolution (Day & Athos)](https://zenodo.org/records/18525262), Zenodo 2026-02-08 (v2; v1 Z18517618 2026-02-07 is byte-identical), ¶21 of extracted text. Eq. (1)

> The 25.7% shortfall is not an approximation error or a boundary effect; it is the mathematical consequence of computing k from real population sizes rather than assuming constant N.

Source: [Z18525262, The Real Rate of Molecular Evolution (Day & Athos)](https://zenodo.org/records/18525262), Zenodo 2026-02-08 (v2; v1 Z18517618 2026-02-07 is byte-identical), ¶59 of extracted text

## Formal statement
k_t = (μ/N_t) · ΣN_i²/ΣN_i over contributing cohorts i; cohorts 1950–2025 at 25-year spacing: N = 2.5, 4.0, 6.1, 8.2 (billions); μ = 1.2e-8 (Kong 2012; `mutation.mu_per_site_per_gen.pedigree_human`).

**Arithmetic audit (derived, python3 -I):** ΣN² = 6.25 + 16.00 + 37.21 + 67.24 = 126.70 ✓; ΣN = 20.8 ✓; 126.70/20.8 = 6.0913; /8.2 = 0.7428 ✓. Column k_i/μ = 0.305, 0.488, 0.744, 1.000 ✓.
**Sensitivity (derived):** holding the paper's growth ratio (8.2/2.5)^(1/3) = 1.485 per cohort and extending the window: k/μ = 0.87 (2 cohorts), 0.78 (3), 0.72 (4), 0.65 (6), 0.61 (10), 0.60 (20). The number 0.743 is a property of the four-cohort window chosen, not of the population.
**Direction:** the paper states that divergence times "are longer than reported" (k < μ); Z18525547 (same week) concludes dates are 15–150× shorter (k > μ). Both can be true only for different N-histories; the corpus applies each to the same human lineage.

## Assumptions
- Stated: A mutation arising in cohort i exists as "one copy among 2N_{t} gene copies" in the current population, so its fixation probability is 1/(2N_t).
- Implicit: Copy number of a new mutant does not grow with the population (in a growing Wright–Fisher population the mean offspring number exceeds 1, so the expected frequency of a neutral lineage stays 1/(2N_i)); census N_i of 25-year cohorts is the relevant N; Day describes the RRME as applying to overlapping generations while tabulating discrete 25-year cohorts.

## Responses
- Against: Ledger: Balloux & Lehmann (verified-partial) have the effect only for overlap plus fluctuation; no 0.743 in their paper. Hössjer and McCarthy use k = μ.
- In support: Day: independent route to the B&L conclusion; arithmetic reproduces.
- Weaknesses in the responses: B&L-style effects are a different mechanism from the cohort-dilution bookkeeping above; the corpus has no independent test of RRME (B3b would give one). Day's Z18637333 repeats 0.743 without new derivation.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Balloux & Lehmann 2012 | no 0.743; k = μ(1 − s) for constant survival s | verified-partial |
| Kong 2012 | "with an average father's age of 29.7, the average de novo mutation rate is 1.20×10-8 per nucleotide per generation" | verified (μ input) |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: k/μ = 0.743 for the human population in 2025.
- Under the opposing model: A neutral lineage in a growing Wright–Fisher population has P_fix = 1/(2N_i), so the long-run rate stays μ; any transient is a lag (B1b), not a rate change.
- Result that would change a verdict: B3b scenario (i): simulated k/μ ≠ 1 for non-overlapping growth would support RRME.

## Check
Script: proposed `research/checks/b3b_overlap_fluctuation.py`; arithmetic audit above computed with python3 -I. Related done check: B1b (growth gives a transient deficit that recovers).

R4 B3c (research/checks/results/R4-B3b-C1.md): arithmetic 0.7428 reproduces, but the value depends on the window (2 cohorts 0.868 ... 20+ cohorts 0.598). Mechanism test: a mutant born in cohort i fixes with probability 1/N_i (P_fix*M_i = 0.973-1.018; with overlap 1.034 +/- 0.026) against the 1/(2N_t) the derivation needs (0.305). Day's "RRME confirms B&L" has the opposite sign (B&L realistic growth: +38%; RRME: -26%). The 1/(2N_t) step is the audit's reconstruction of eq. 1 and 3, to be confirmed. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- cohort N series
- window length
- calendar generations vs average-generation-time units
