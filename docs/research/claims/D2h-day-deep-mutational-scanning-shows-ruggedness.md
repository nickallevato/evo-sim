---
id: D2h
title: "Deep mutational scanning shows single-residue changes mostly reduce or destroy function; the landscape is rugged, which confirms Eden"
side: day
branch: D
parent: D2
edges: [{type: supports, target: D},{type: attacks, target: D1a}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # no data or citation offered
  fidelity: unverifiable      # no study cited; the claim concerns "most proteins" as a class
  external: contested      # requires harvest of DMS literature (not in corpus)
---

## Statement (verbatim)
> "The most relevant empirical work, deep mutational scanning studies, actually shows the opposite of what Rosenhouse implies. Single-residue changes to most proteins tend to reduce or destroy function. The fitness landscape is rugged, not smooth. Eden’s 1966 concerns about the rarity of functional proteins in sequence space have been confirmed by subsequent experimental work, not refuted by it."

Source: [The Best They've Got II](https://voxday.net/2026/10/06/the-best-theyve-got-ii/), 2026-10-06, voxday.net, para 5. No citation in the post (Day uses the same standard against Rosenhouse in the previous paragraph).

## Formal statement
Claim: for typical proteins, the share of single-substitution mutants with reduced/destroyed function is large (the DFE is shifted toward deleterious) and the landscape (functional sequences) is non-connected. Parameters: `p_del` = fraction of single substitutions that substantially reduce function; `K` or a pair-correlation of effects. Day gives neither.

## Assumptions
- Stated: DMS studies exist and support ruggedness.
- Implicit: 'reduce or destroy' is equivalent to 'rugged'. Reduction is not destruction; ruggedness needs local optima that block ascent, not mean deleterious effect. Most random mutations being deleterious is compatible with smooth landscapes (Fisher's geometric model) and with selection finding the rare beneficial ones.

## Responses
- Against: Rosenhouse (D1a) says the opposite and also gives no citation. Wistar-era data (Lewontin) point the other way (D2b).
- In support: Wald (D2c). Axe 2004 (D10) measured low prevalence for one fold under a hydropathic-signature restriction, not DMS.
- Weaknesses: symmetrical lack of citations on both sides; the corpus has no DMS source. The quoted sentence is a general factual claim about the field.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Deep mutational scanning literature | not in corpus; no study cited by Day | unverifiable |

## Pre-registered prediction
Written before any check. Under Day: a harvest of DMS datasets shows median single-substitution fitness effects strongly deleterious for most positions and landscape-wide epistasis that creates local optima. Under the opposing model: most positions tolerate several substitutions, deleterious effects are typically mild, and high-fitness sequences form connected networks (percolating neutral networks). Result that would change a verdict: harvested p_del and epistasis distributions; the NK-reachability module (D, S2) mapped to measured K.

## Check
Specification only (separate later module). Harvest list: classic DMS sets with published per-position tolerance fractions (beta-lactamase TEM-1, GFP, ubiquitin, Gb1, hemoglobin variants); compute p_del and pairwise epistasis; feed into S2.

## Simulator variables implied
p_del; epistasis structure; connectivity of high-fitness sequences.
