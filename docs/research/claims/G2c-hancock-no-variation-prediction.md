---
id: G2c
title: "Hancock: a strictly serial model predicts almost no genetic variation among individuals, unlike observed polymorphism"
side: critic
branch: G
parent: G2
edges: [{type: attacks, target: G2}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> there would basically be no genetic variation amongst individuals except for the mutation that's increasing in frequency

Source: [Gutsick Gibbon and Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution"](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:33:59 (GG-13; auto-caption). Same passage (t=01:37:07): the model "makes a specific prediction about levels of polymorphism in the natural world, about the shape of the site frequency spectrum" which "doesn't bear out".

## Formal statement
Prediction of a strictly serial sweep model for segregating variation, as stated by Hancock. Not formalised. A formulation would require the sweep rate r (per generation per genome), sweep duration, and recombination: under free recombination, neutral diversity at unlinked sites is set by mutation-drift balance θ = 4Neμ and is reduced by sweeps only at linked sites. That expectation is a standard-theory statement, not tested in the repo.

## Assumptions
- Stated: one rising allele at a time.
- Implicit: that variation is generated only by the rising allele (neglects standing neutral variation) and that Day's model is strictly serial, which Day denies (G1, Gc: 230 simultaneous sweeps).

## Responses
- Against (Day): his models are not strictly serial (Gc, G1); the Bernoulli paper itself models ~230 simultaneous sweeps.
- In support: Z23003785 s8.2: neutral drift is "off" and hitchhiking carries neutrals, which would reduce variation; no polymorphism data are shown by Day.
- Weaknesses in the responses: no polymorphism data are in the repo; the claim is the speaker's experience ("as someone that has measured a lot of sight frequency spectrums" (auto-caption spelling)), not a calculation; Day's models differ from the strict serial case Hancock describes.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Proposed check G2c-sim (not run): forward simulation with sweep rate 1/1,322 per genome per generation (LTEE-rate) and free recombination; measure neutral heterozygosity at unlinked sites vs θ.
- Under Hancock: diversity near zero only if sweeps are strictly one at a time with genome-wide linkage; under free recombination expect θ.
- Under Day: nothing predicted.
- Result that would change a verdict: heterozygosity <10% of θ under free recombination at the stated sweep rate.

## Check
Script: none yet. Review: pending.

## Simulator variables implied
- Neutral diversity output; sweep rate; recombination.
