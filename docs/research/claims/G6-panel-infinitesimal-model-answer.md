---
id: G6
title: "Gutsick Gibbon panel: the standard population-genetics answer to the Bernoulli Barrier is the infinitesimal model (variance in fitness is maintained under many small-effect mutations)"
side: critic
branch: G
parent: G
edges: [{type: attacks, target: G}]
load_bearing: false  # branch G is a listed feeder (R5-draft 1.3), but this node carries no verdict and moves nothing
sourcing: firsthand
status: extracted
verdicts:
  internal: pending   # created at integration of R4 VID-01-score (2026-10-14); not yet scored. The write-up grades the answer "on point" (top of the band) to GGR-19 but notes it gives no derivation and never touches the CV-to-variance substitution; that grade is not a verdict.
  fidelity: n/a
  external: pending   # no external verdict proposed; G's own external is `contested`, and the answer adds no derivation (R4 VID-01-score Q3)
---

## Statement (verbatim)
> "So like the interpretation that I got is there's many many mutations of which many have very small effect and so the variance of fitness is small. Um this is literally called the infinite decimal model. It's the fundamental model of quantitative genetics."

Source: Gutsick Gibbon (Erika) with Zach Hancock and panel, "Six Scientists Roast One Racist Loser (Heartwarming) (Four Hours) (Hopecore)", YouTube `AqC1ZM4icms`, posted 2026-10-13, auto-generated captions (ASR), t=02:14:07, quote GGR-44 (`sources/quotes-critics.md`); speaker unnamed (`panel`). "infinite decimal model" is the ASR rendering of *infinitesimal model* (Fisher 1918). Introduced in the same unbroken turn at t=02:13:47 (GGR-43): "I'll give the like uh again I'll give the pop gen answer to go back to Bernoli's law if you want to know how it is that variance and fitness can be maintained even if you have very very uh for one like low fitness impacts of each individual mutation."

Target: the Bernoulli Barrier paper (Z18167588), claim G, as relayed in GGR-19 (a Reddit formulation read aloud; the Reddit original is unlocated, so branch G is scored against a relay, rule U).

RH tag: dialectic (the panel's own label: "the pop gen answer"; a named standard model offered as an answer to a stated premise; no rhetorical device scored).

## Formal statement
Not formalised here. The claim, as the audit reads it: for many loci each of small effect, the infinitesimal model (Fisher 1918) is the standard framework in which additive genetic variance in fitness is maintained and selection responds to it, so the Barrier's inference "CV(K) falls with n, hence the response to selection falls" does not describe the standard regime. The audit has **not** checked whether the infinitesimal model answers the coefficient-of-variation step; GGR-44's note records the same.

## Assumptions
- Stated: many mutations, each of small effect (GGR-44).
- Implicit: that the Barrier's quantity of interest is the variance in fitness (the quantity Fisher's theorem uses), not the CV of the beneficial-allele count. G5 makes the allele-count side of the same point (Var(K) = n/4 rises with n).

## Responses
- Against: none located from Day. (MITTENS 3.0 omits the Barrier, claim Ge, so this answer is addressed to the January 2026 paper, not to 3.0.)
- In support: G5 (the allele-count side of the same defect); R4 G1 (no ~230 sweep cap under multiplicative fitness, soft selection, free recombination); R4 VID-01-score Q3, which grades GGR-43/GGR-44 "on point" at the top of that band, and as a different angle from G5, not a weaker restatement of it.
- Weaknesses in the responses: no derivation is given; the same unbroken turn's second point (GGR-27..GGR-29, dN/dS and heterozygosity varying across the genome) is graded "adjacent". The speaker says the interpretation is "what Erica read", i.e. of the relayed Reddit text.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Fisher 1918 (infinitesimal model) | not retrieved | unverified |

## Pre-registered prediction
Not applicable (node created at integration; no check run on it).

## Check
`research/checks/results/R4-VID-01-score.md`, Q3 and Open item 2. Created by the integration of R4 VID-01-score, 2026-10-14. Verdicts `pending`; scoring it is a separate task.

## Simulator variables implied
Genetic architecture option: many small-effect loci with additive variance in (log) fitness (infinitesimal regime) versus few large-effect loci.
