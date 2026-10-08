---
id: G2b
title: "Duffy: 180 total fixed mutations is all there is time for (252,000 generations / 1,400 per fixation)"
side: ally
branch: G
parent: A
edges: [{type: supports, target: A}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: contested
---

## Statement (verbatim)
> 180 total fixed mutations is all there's time for using the fastest rate of mutational fixation ever observed in any organism

Source: [Gutsick Gibbon, Will Duffy livestream, Human Evolution #2](https://www.youtube.com/live/6jXiwrcC5PQ), 2026-09-22, t=00:29:42 (DU-02; auto-caption).

> The length of a generation for humans is 25 years times 1,000 400

Source: [Jan Ghijselen video](https://www.youtube.com/watch?v=nTVRiEcswI8), 2026-09-28, t=00:00:44 (DZ-02; auto-caption). The arithmetic he restates: 6.3e6/25 = 252,000; /1,400 = 180.

## Formal statement
252,000/1,400 = 180 exactly (python3 -I). 1,400 is the book's G_f (Z23003785 s3.3; the 3.0 paper replaces it with 1,322 → 190.6). Table s7.2 row "Book's original (1,400)": 180 achievable, shortfall 205e6/180 = 1,138,889 (paper: 1,139,000×; reconciles).
"Fastest rate … observed in any organism": see A2d; the LTEE point-mutator populations run faster (43–183 gens/fixation).

## Assumptions
- Stated: the book's G_f and generation count.
- Implicit: d = 1 in this worked arithmetic (balance note: Duffy presents the overlapping-generations point as a separate flaw).

## Responses
- Against: Hancock (A3d, factor of two); the "fastest observed" wording (A2d); G2a (serial division).
- In support: the arithmetic is verified by an opposing critic (DeDzjang, DZ-02).
- Weaknesses in the responses: Duffy says he is "not a mathematician" and "not certain he’s right" (DU-04); the 180 figure uses a G_f that Day has since replaced.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Arithmetic only.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- Preset: "book 2026-01" (1,400, 252,000).
