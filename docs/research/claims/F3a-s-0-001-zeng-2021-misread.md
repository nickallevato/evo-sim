---
id: F3a
title: "s = 0.001 \"the empirical mean for beneficial mutations in humans from Zeng et al. 2021\""
side: day
branch: F
parent: F3
edges: [{type: supports, target: F3}]
load_bearing: true  # the input that sets the 19,800 latency; halving or doubling s doubles or halves it
sourcing: firsthand
status: reviewed
verdicts:
  internal: pending
  fidelity: misread
  external: contested
---

## Statement (verbatim)
> at s = 0.001 (the empirical mean for beneficial mutations in humans from Zeng et al. 2021)

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶15 of extracted text

> We detect widespread signatures of negative selection in the genetic architecture across 155 complex traits with a predicted mean selection coefficient of ~0.001

Source: [Zeng et al. 2021, Widespread signatures of natural selection across human complex traits and functional genomic categories, Nat Commun 12:1164](https://www.nature.com/articles/s41467-021-21446-3), 2021, Results, evolutionary inference

## Formal statement
Parameter key: `selection.s_zeng_2021` = 0.001, sign negative, positive selection appears only as a simulation sensitivity scenario and Day uses the value as beneficial (parameters.yaml note, verified). Zeng: "Since we only detected signatures of negative selection in real traits, our evolutionary simulations focused on the models of negative selection." Latency scales as 1/s (F3): derived t(s = 0.01, N = 10⁴) = 1,981 vs 19,807 at s = 0.001 for the deterministic formula.

## Assumptions
- Stated: s = 0.001 is the mean for beneficial mutations in humans.
- Implicit: A mean over trait-affecting variants under negative selection is a proxy for the beneficial coefficient.

## Responses
- Against: Fidelity ledger: verified-misread.
- In support: None found; Z18166426 uses s_eff.
- Weaknesses in the responses: Neither side has a human beneficial-s distribution; Zeng itself says about 1% of the genome are mutational targets with mean 0.001, which does not inform sweep speed of rare beneficial alleles.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Zeng 2021 | "about 1% of human genome sequence are mutational targets with a mean selection coefficient of ~0.001" | verified-misread when used for beneficial mutations |
| Zeng 2021 | "Since we only detected signatures of negative selection in real traits, our evolutionary simulations focused on the models of negative selection." | nuance: positive selection only a sensitivity scenario |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: s_ben = 0.001.
- Under the opposing model: s is an unmeasured distribution; sweep latency spans 10²–10⁴ generations.
- Result that would change a verdict: A sourced human beneficial-s distribution.

## Check
Script: none. Related: B0.4 in F3.

## Simulator variables implied
- s (distribution)
- sign convention
