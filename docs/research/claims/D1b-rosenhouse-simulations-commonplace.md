---
id: D1b
title: "Rosenhouse p.124: Schützenberger's arguments about computer simulation have not held up; simulations of evolution are commonplace"
side: critic
branch: D
parent: D1
edges: [{type: attacks, target: D5}]
load_bearing: false  # D is not required for ROOT
sourcing: secondhand
status: extracted
verdicts:
  internal: pending      # one-sentence assertion
  fidelity: unverifiable      # book not accessed
  external: contested   # Day's reply (D2i) turns on designed fitness functions; R4 D1: RNA walks are known-target (D2i); on the measured GB1 landscape random-uphill walks end at a mean of 5.9x WT and at the best variant only 5.8% of the time: navigable, not trapped, not finding the top
---

## Statement (verbatim)
> "Schützenberger’s arguments about computer simulations have likewise not held up, and computer simulations of the evolutionary process are now commonplace."

Source: Rosenhouse 2022, p.124 (Assertion 2), via [The Best They've Got II](https://voxday.net/2026/10/06/the-best-theyve-got-ii/), 2026-10-06, voxday.net, para 6. `secondhand`.

## Formal statement
Existence of working evolutionary computations is offered as evidence against the 'gap' between program space and function space (D5).

## Assumptions
- Stated: simulations are commonplace.
- Implicit: simulations model the biological mapping from sequence to fitness, not merely a programmer-defined one.

## Responses
- Against: Day (D2i): every evolutionary algorithm has a programmer-designed fitness function, the very mapping Schützenberger said biology lacks.
- In support: Wright's 1250-question analogy (D6) and Weasel-type demonstrations show cumulative selection works given a fitness signal.
- Weaknesses: both sides agree on the logic: algorithm success shows what selection can do when a fitness mapping exists; it cannot by itself show biology supplies the mapping. Day's reply is therefore valid against a reading of Rosenhouse as an existence proof and does not address a reading as a plausibility argument.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Schützenberger (Wistar p.75) | 'without some built-in matching, nothing interesting can occur' (artificial-intelligence experience) | accurate |

## Pre-registered prediction
Written before any check. Under the claimant (Rosenhouse): evolutionary computations with biologically derived fitness (e.g. protein-folding or measured-fitness landscapes) succeed. Under the opposing model: success occurs only where the designer builds in matching; with measured biological landscapes success rate falls with ruggedness. Result that would change a verdict: success of selection on an empirical, designer-independent landscape (DMS-derived).

## Check
R4 D1 (research/checks/results/R4-D1-spike.md, review #11, 2026-10-09): RNA adaptive walks toward a known target never got trapped (known-target, as D2i objects). On the measured GB1 landscape random-uphill walks from functional starts end at a mean 5.9x WT; 5.8% reach the global maximum (1.1% from WT).

Specification: NK / DMS-derived landscapes in D, step S2 and S3. No script.

## Simulator variables implied
Fitness-function provenance (designed vs measured); landscape source.
