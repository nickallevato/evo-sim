---
id: ROOT-K
title: "Steve Keen: the Blind Watchmaker hypothesis fails because of time; the required time exceeds the age of the Universe"
side: ally
branch: ROOT
parent: ROOT
edges: [{type: supports, target: ROOT}]
load_bearing: false  # an endorsement; ROOT does not depend on Keen
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # Keen gives no equations; his figure depends on ROOT/A inputs
  fidelity: partial      # endorses The Frozen Gene, not the MITTENS papers; scope differs
  external: contested      # checked arithmetic only reaches the claim if the bacterial rate is a fixed ceiling
---

## Statement (verbatim)
> "The reason it fails, as Vox Day and Claude Athos show in this book, is time."

Source: Steve Keen, [Natura Facit Saltum](https://profstevekeen.substack.com/p/natura-facit-saltum) (preface to The Frozen Gene), 2026-02-03, para 7 (quotes-critics KE-01).

> "is orders of magnitude greater than the age of the Universe, let alone the age of the Earth."

Source: same, para 7 (KE-05). The sentence's subject is truncated in the extracted quote; the full sentence is in the source.

## Formal statement
Keen's claim: `T_required >> T_universe`. Under MITTENS 3.0 numbers: `T_required = T_div * shortfall = 6.3e6 y * 1.075e6 = 6.77e12 y` (derived; parameters.yaml `divergence.t_div_years.day_2026_mittens3`, `shortfall.mittens3_full`); `6.77e12 / 1.38e10 = 491` universe-ages. Recomputed. 'Orders of magnitude greater' holds (2.7 orders) only if the shortfall is read as a time multiplier at a fixed per-fixation rate. For the older 220,000x shortfall: 6.3e6 * 2.2e5 = 1.4e12 y (100 universe-ages).

## Assumptions
- Stated: the Frozen Gene's statistical implications of the 'Blind Watchmaker' hypothesis.
- Implicit: a Lamarckian/quantum mechanism (McFadden 2001; Schwartz 2000, per the note in quotes-critics) is the preferred alternative; the preface has no equations. Keen's references to 'time' rely on the book, not the preface.

## Responses
- Against: the A5/A3x/B7 findings on inputs undermine the 491-universe-ages figure at its source (205M counts bp of SVs; Kimura 1962 gives 1/2N).
- In support: none beyond Day's papers.
- Weaknesses: Keen's endorsement is of The Frozen Gene; it is not evidence about Probability Zero's calculations. Credentials (economics PhD, evolutionary programming) self-described.

## Primary literature
| Cited work | What it actually says | Fidelity |
|---|---|---|
| McFadden 2001; Schwartz 2000 | not retrieved | unverified |

## Pre-registered prediction
Written before the (arithmetic-only) check. Under the claimant: 6.3e6*1.075e6/1.38e10 >> 1. Under the opposing model: the shortfall figure is a bound on a fixed-ceiling rate model only; with validated scaling (A5) and SNV-only counts (A3x) the time multiplier falls to ~10-10^2, i.e. well below universe-ages. A verdict changes if the A-branch checks establish the SNV-only, scaled shortfall.

## Check
`python3 -I -c "print(6.3e6*1.075e6, 6.3e6*1.075e6/1.38e10)"` -> 6.7725e12, 490.8. Reconciles with the note in quotes-critics (KE-05).

## Simulator variables implied
T_div, shortfall factor (A), age of Universe as comparator; no simulator variables of its own.
