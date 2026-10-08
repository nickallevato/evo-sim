---
id: A2f
title: "Natural-selection-only LTEE rates: 4,615 (blog) vs ~1,408 (Zenodo 3.0) vs ~24,500 \"serial\" (blog)"
side: day
branch: A
parent: A2
edges: [{type: revises, target: A2}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> The real, updated 60-generation LTTE numbers are: 4,615 generations per beneficial fixation (natural selection) 1,322 generations per all-cause fixation (natural selection + neutral theory + everything else)

Source: [The Temperature Rises](https://voxday.net/2026/09/27/the-temperature-rises/) (key B2026-09-27), blog, 2026-09-27, ¶13. The text prints "LTTE" and "60-generation" as written.

> UPDATE: The SERIAL natural selection rate for the LTEE at 60k generations is ~24,500 generations per fixation.

Source: [Math Teacher Can't Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (key B2026-09-30), blog, 2026-09-30, ¶23.

## Formal statement
Three different "natural-selection-only" numbers in the Day corpus:
- 4,615 gens/beneficial fixation (blogs 2026-09-27, 09-28, 09-30): `derived:` 60,000/4,615 = 13.0 beneficial fixations per 60,000 generations.
- ~1,408 gens/beneficial fixation (Z23003785 s4.3): 56.0 clone-pair fixations − 20.5 neutral hitchhikers (4.1e-4 x 50,000) = 35.5; 50,000/35.5 = 1,408 (reconciles).
- ~24,500 "serial" (blog 09-30): `derived:` 60,000/24,500 = 2.4 sequential events per 60,000 gens. Compare Ara+2 alone: 14 sequential events in 60,000 gens (G1a) = 4,286 gens/event.

13.0 beneficial fixations (4,615) is not derivable from the s4.3 inputs (35.5 beneficial). No derivation of 4,615 or 24,500 appears in the corpus (the blog says "I'll want to dig in a little deeper to be certain of that").

## Assumptions
- Stated: a natural-selection-only rate separates sweeps from hitchhikers and drift.
- Implicit: all hitchhikers are neutral and all sweeps are beneficial; the quantity differs between sources.

## Responses
- Against: none in corpus.
- In support: none; these are Day's statements about his own numbers.
- Weaknesses: the numbers are mutually inconsistent as stated and none carries a derivation; Day marks the 24,500 as provisional. MITTENS 3.0 itself says the total throughput (1,322), not the beneficial-only rate, is what MITTENS measures (s4.3).

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Prediction: a recount using the ≥95% and lineage-aware rules (A2b) yields a beneficial-only G_f of ~1,400–1,700 (s4.3 style), not 4,615. Result that would change the verdict: a published derivation of 4,615.

## Check
Arithmetic only. Review: pending.

## Simulator variables implied
- Separate counters for sweep drivers, hitchhikers and drift fixations in the simulator output.
