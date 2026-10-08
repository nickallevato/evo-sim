---
id: A2d
title: "Day's G_f is an average, not the fastest fixation rate that could be claimed"
side: critic
branch: A
parent: A2
edges: [{type: attacks, target: A2e}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> If the figure is an average then it includes some mutations that fixed quicker and so is not the fastest fixed mutation rate.

Source: [Camestros Felapton, Reading Vox Day 2026 [5]](https://camestrosfelapton.wordpress.com/2026/01/29/reading-vox-day-so-you-dont-have-to-2026-5/), 2026-01-29, para 9 (CA-11).

> He is correct that when he calculated the number it was an average. It isn’t intended to be a time for an individual chromosome.

Source: same post, para 9 (CA-10; a concession to Day on G1).

> 180 total fixed mutations is all there's time for using the fastest rate of mutational fixation ever observed in any organism

Source: [Gutsick Gibbon, Will Duffy livestream](https://www.youtube.com/live/6jXiwrcC5PQ), 2026-09-22, t=00:29:42 (DU-02; Duffy presenting MITTENS; auto-caption).

## Formal statement
Claim: G_f = 1,322 is a mean over populations and over mutations (fast and slow); Day (via Duffy) calls it "the fastest rate … ever observed in any organism".

Check against Day's own 3.0 tables (Z23003785 s5.1, s7.2): point-mutator populations are 43 to 183 generations per fixation (Ara-4: 43; Ara-3: 183; the IS-element mutator Ara+1 is 452; mean over seven 104.7) and the metagenomic mutator average at 60K is 78. 1,322/78 = 16.9, 893/104.7 = 8.5. So the LTEE itself contains rates 8.5x–17x faster than the headline; the non-mutator average is not the fastest observed rate even in the LTEE. Day treats the mutator rates as inapplicable to humans (s6; A5d).

## Assumptions
- Stated by the critic: "average" and "fastest" are different quantities.
- Implicit: that Day uses "fastest" in the statistical sense; Day uses it as "fastest in the applicable class of organism" (non-mutator).

## Responses
- Against (Day): G_f is meant to be a throughput average (blog 2026-01-27: "25 mutations … fixed in parallel"); an average is the right quantity to multiply by time.
- In support (critic): Day's own 3.0 table.
- Weaknesses in the responses: Camestros's CA-07 asserts Day "has not shown" the rate is fast, without computing an alternative; the claim "fastest observed in any organism" is a claim about all organisms; the repo does not test it.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Prediction (critic): published fixation rates for faster-evolving non-mutator systems (e.g. viral or yeast experimental evolution) exceed 1/1,322 per generation. Not tested here (outside repo sources).

## Check
No script. Review: pending.

## Simulator variables implied
- Rate presets for non-mutator and mutator classes.
