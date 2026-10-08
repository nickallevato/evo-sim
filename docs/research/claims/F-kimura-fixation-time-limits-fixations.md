---
id: F
title: "Kimura's fixation-time equations (4Ne neutral; (2/s) ln 2Ne beneficial) limit how many fixations can complete; 1/(2N) says nothing about when"
side: day
branch: F
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: F1}, {type: depends-on, target: F3}]
load_bearing: true  # F is the conceptual bridge from per-allele fixation time to a cap on the count; if latency does not bound throughput (F1), only the fill-state argument (B1/B2) remains
sourcing: firsthand
status: reviewed
verdicts:
  internal: pending
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> The Kimura equation Brian should have used is Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶6 of extracted text

> k = μ gives the output rate once the process is running. t̄ = 4Nₑ gives the startup cost before any output appears.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §2 The Missing Equation

> It contains no time variable. It says nothing about when.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶6 of extracted text. on 1/2N

## Formal statement
Glossary sense: throughput k = substitutions per generation; latency t_fix = generations per allele. Day's position, in its strongest form (Education blog; IR §2): latency is the "startup cost" (fill time), and the count over a window is rate × (window − startup) (B1). Weaker form (Q&A, F1a): window ÷ latency bounds the count.
Sub-claims: F1 (critic: latency ≠ throughput), F1a (Day's reply and his own serial use), F1b (McCarthy, parallel), F2 (interference/feasibility check), F3 (beneficial time formula), F3a (s = 0.001), F4/F4a (Bowers 2s and Day's reply), F5 (Kimura & Ohta SD), F6 (relictation).

## Assumptions
- Stated: Kimura's own framework supplies the time equations.
- Implicit: The (2/s)ln(2Nₑ) formula is Kimura's (the Zenodo calculator cites Charlesworth 1994; not found in Kimura & Ohta 1969 or Kimura 1962); fill-state is empty (B1c).

## Responses
- Against: "The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbR9n0iZNuQ (Mansfield))
- In support: Day: the Hard Limits paper treats the 4Nₑ transit as the length of the pipe (B2).
- Weaknesses in the responses: Mansfield's comment predates Day's reply and answers a different sentence; Day's reply in turn depends on the fill state, which neither side has sourced (B1c).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | 4Nₑ (Eq. 15); no (2/s)ln(2Nₑ) formula | accurate for 4Nₑ; not found for the beneficial formula (it is attributed to Charlesworth 1994 in Z19984826) |
| Kimura 1962 | U = 1/2N, ≈2s | accurate (B7a) |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Latency enters the count only through the fill state.
- Under the opposing model: Latency does not bound throughput; the count is rate × window once the pipeline is full.
- Result that would change a verdict: B1c, F2.

## Check
See F1 (done), F2 (proposed), F3 (done: `research/checks/beneficial_fix_time.py` (seed 7)).

## Simulator variables implied
- latency model per allele
- throughput mode (parallel | serial)
- fill state
