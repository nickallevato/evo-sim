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
  internal: holds   # R4 F3a: (2/s) ln(2N_e) = 19,807 at s = 0.001, N_e = 1e4; "faster than 4N_e" holds for N_e >= 4,559. At Day's human N_e = 3,300 (Z18525547) it would be slower, but that input is not used in this passage (two texts mixed): noted, not carried into the verdict
  fidelity: misread   # re-confirmed from the raw text: Zeng's ~0.001 is a mean |s| for trait variants under negative selection (Z3); no measured beneficial mean. Fidelity concerns the label; whether the magnitude is a fair stand-in is the R1 question (undetermined)
  external: contested   # R1 materiality undetermined: latency moves > 25% for s outside 0.0008-0.00133, but no sourced human beneficial mean s is in the repo (R4 F3a). The steady-state rate does not depend on latency (F1)
---

## Statement (verbatim)
> at s = 0.001 (the empirical mean for beneficial mutations in humans from Zeng et al. 2021)

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶15 of extracted text

> We detect widespread signatures of negative selection in the genetic architecture across 155 complex traits with a predicted mean selection coefficient of ~0.001

Source: [Zeng et al. 2021, Widespread signatures of natural selection across human complex traits and functional genomic categories, Nat Commun 12:1164](https://www.nature.com/articles/s41467-021-21446-3), 2021, Results, evolutionary inference


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
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
Script: `research/checks/f3a_zeng_s_small_checks.py` (R4 F3a; pre-registered f9c8ed9). Related: B0.4 in F3.

R4 F3a (`research/checks/results/R4-F3a.md`; pre-registered f9c8ed9, post hoc e9d2284 control-character strip; combined review #36, 0 MAJOR 6 MINOR; fix pass 30bc620): P1 failed as pre-registered on a PDF extraction artefact (a \x02 before the italic s in Zeng's sentence Z4; the quote is verbatim once stripped; the strip is global and Day's text matched exactly in both runs). P2-P6 hold: six Zeng sentences give a numeric s, none a beneficial mean (only two carry an explicit negative-selection flag in the sentence; the rest rely on the paper's framing; the scan has a `pos and not neg` blind spot, and the review's grep of eight positive/beneficial mentions found none with a measured value; a full read of Methods and Supplement remains open). The B0.4 asymptote is 8,532 and Day overstates it 2.32x. Critic side: the attribution is a misread and the sign matters (|s| under purifying selection); at Day's own N_e = 3,300 the formula is slower than 4N_e. Day side: the arithmetic is exact, 0.001 is a defensible order-of-magnitude scale for trait-affecting variants, and even the category means (0.0005-0.0010) keep the 'faster' sentence true, marginally at 0.0005. The misread does not touch MITTENS's throughput figure. Verdicts: internal pending -> holds; fidelity misread and external contested confirmed.

## Simulator variables implied
- s (distribution)
- sign convention
