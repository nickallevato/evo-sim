---
id: A2i
title: "Matev: an LTEE generations-per-fixation figure is not a 'generous' bound for humans, because bacteria are fast per year (short generations), not per generation"
side: critic
branch: A
parent: A2e
edges: [{type: attacks, target: A2e}]
load_bearing: false  # restates the A2e weakness as a units argument; ROOT unaffected beyond A2e
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # X = A x B: a high per-year rate 1/X1 that comes from a short generation time B1 says nothing about A1 vs A2
  fidelity: pending   # Matev attributes to a 2022 Day post the view that time, not generations, is what counts; that post is not in the corpus
  external: pending   # whether human generations per fixation can be below the LTEE value is the A2 scaling question (A-sim, GAP-04); A2e is already internal non-sequitur
---

## Statement (verbatim)
> "The reasoning is that 1/X1 is high (due to 1/B1 being high), so it very generous for the estimation of X2 to use the A1 value as an estimate for A2 even though A1 isn't why 1/X1 is high."

Source: [Matev, comment on McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds/comment/340270022), 2026-09-18, comment id 340270022 (RF-4). Matev is a commenter (Substack @ns670106) with no publication of his own found.

## Formal statement
Years per fixation X = A x B, with A = generations per fixation and B = years per generation (subscript 1 = E. coli LTEE, 2 = humans). The LTEE's high fixation rate per year (1/X1) comes from its short generation time (B1 of hours), not from a low A1. Using A1 (1,322-1,587 generations per fixation) for A2 is "generous" only if A2 >= A1 is shown; the per-year speed of bacteria does not show it.

## Assumptions
- Stated: the "fastest rate ever measured" premise (Q91: "the fastest empirical rate ever measured in any organism") refers to a per-time speed.
- Implicit: what bounds A2 depends on N, mu, L, recombination and the DFE, not on B.

## Responses
- Against: none located. Day's 2nd-edition abstract (Q91) keeps "1,400 generations per fixation (the fastest empirical rate ever measured in any organism)".
- In support: R4 GAP-04 (finite-map cap R/2-R/4 independent of N and s; LTEE outside its domain) and the A-sim / F2 results in A2e; RF-9 (The Deuce, an ally) reads the LTEE figure as a ceiling under maximal selection, which is the premise this attacks.
- Weaknesses in the responses: Matev gives no number for A2; the point is structural.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Day blog post (2022) cited by Matev | not located in the corpus | unverified |

## Pre-registered prediction
Not run. No check is proposed beyond A2e / GAP-04.

## Check
None (structural point; recorded from the 2026-10-09 corpus refresh, `docs/research/sources/refresh-2026-10-09.md` C-4).

## Simulator variables implied
Generation time (years) as a separate input from generations per fixation; report rates per generation and per year.
