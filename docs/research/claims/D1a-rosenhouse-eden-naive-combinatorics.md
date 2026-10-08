---
id: D1a
title: "Rosenhouse p.124: molecular biologists learned the geometry of protein space and it makes Eden's combinatorial calculations look hopelessly naive"
side: critic
branch: D
parent: D1
edges: [{type: attacks, target: D3},{type: attacks, target: D}]
load_bearing: false  # D is not required for ROOT
sourcing: secondhand
status: extracted
verdicts:
  internal: pending      # no argument visible in the quoted paragraph
  fidelity: unverifiable      # book not accessed; quote is Day's transcription
  external: contested      # contradictory literature estimates and Day's unsourced DMS claim (D2h)
---

## Statement (verbatim)
> "Molecular biology and computer science were both in a very rudimentary state when the conference was held in 1966. Both ﬁelds have blossomed spectacularly in the ensuing decades, with results that have not been kind to the perspectives of Eden and Schützenberger. Molecular biologists have learned a lot about the geometrical structure of protein space, and their results make Eden’s simplistic combinatorial calculations look hopelessly naive.”"

Source: Rosenhouse, *The Failures of Mathematical Anti-Evolutionism*, Cambridge UP 2022, p.124, as transcribed by Day in [The Best They've Got II](https://voxday.net/2026/10/06/the-best-theyve-got-ii/), 2026-10-06, voxday.net, para 3. `secondhand` (Day's transcription, with 'ﬁ' ligatures as printed). Not independently verified against the book.

## Formal statement
A is-a claim: 'the geometrical structure of protein space (known since 1966) makes Eden's 20^250-vs-10^52 comparison irrelevant'. Equivalent to asserting that the topological hypothesis (Eden's second horn, D3b) is true.

## Assumptions
- Stated: molecular biologists 'have learned a lot about the geometrical structure of protein space'.
- Implicit: that structure is path-connected for functional proteins; the results exist and are in ch.6 (promised 'We will discuss this work in Chapter 6', D1c).

## Responses
- Against: Day (D2): no citations, no quantification in the paragraph, 'either those results exist or they do not'; Day's DMS counter-claim is itself unsourced (D2h). Axe 2004 (D10) is consistent with Eden's concern for a particular fold.
- In support: Taylor 2001 and Keefe & Szostak 2001 show functional proteins exist in random libraries at measurable frequency (D11, D12), but both also say single-step random search is infeasible for enzymes (Taylor) and neither measures connectivity.
- Weaknesses: the paragraph is a pointer to ch.6; judging it requires ch.6.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Taylor 2001 | 'a library of ~10^24 members would have been needed to obtain AroQ mutases' if every position were randomized | accurate; shows low density, not connectivity |

## Pre-registered prediction
Written before any check. Under the claimant (Rosenhouse): published measurements of protein-space geometry (e.g. neutral-network sizes, fraction of functional single mutants) show connectivity sufficient for selection. Under the opposing model: measured fractions of functional single mutants are low and decline with distance. Result that would change a verdict: a named study with a measured fraction of functional single-substitution neighbors (D2h).

## Check
No check possible until ch.6 or the cited studies are obtained. Action: harvest ch.6 and DMS literature (neither in corpus).

## Simulator variables implied
Fraction of functional single-substitution neighbors; neutral network size; distance-decay of function.
