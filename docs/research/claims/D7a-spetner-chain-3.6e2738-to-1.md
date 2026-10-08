---
id: D7a
title: "The odds against 500 sequential specific mutations each with probability 1/300,000 are about 3.6 x 10^2738 to 1"
side: day
branch: D
parent: D
edges: [{type: depends-on, target: D7},{type: supports, target: D}]
load_bearing: false  # not a premise of ROOT; Day endorses it as one of many "correct" challenges but calls his own Impossibility of Mutational Fixation argument better because it leaves "no room ... for epicycles"
sourcing: secondhand
status: extracted
verdicts:
  internal: holds      # arithmetic reproduces: (3e5)^500 = 10^2738.56 = 3.64e2738; reciprocal 2.75e-2739 (Day prints 2.7)
  fidelity: unverifiable      # Spetner (Not By Chance) and darwinsmaths.com not retrieved; 1/600 and "500 steps" have no source here
  external: contested      # single-specific-path model; the same post disowns it in the next paragraph
---

## Statement (verbatim)
> "The chance that a specific change to a specific nucleotide will occur during a step is thus 1/600, and the odds that it will also take over the population is 1/500. The total odds are thus 1/600 * 1/500 or 1/300,000. This needs to happen 500 times in a row (the number of steps required to arrive at a new species). We thus need to multiply 1/300,000 by itself 500 times. The odds against this happening are approximately 3.6 x 102738 to 1, or viewed the other way round, the chance of this happening is 2.7 x 10-2739."

Source: [Every Critique is Correct](https://voxday.net/2024/04/25/every-critique-is-correct/), 2024-04-25, voxday.net, para 3. OCR/extraction note: superscripts are flattened in the extracted text ('102738' = 10^2738, '10-2739' = 10^-2739). `secondhand` (the argument is Spetner's, via darwinsmaths.com).

> "Of course, one cannot simply assume that only one mutation is available at every step."

> "All of them can be safely assumed to be valid."

> "The thing to keep in mind is that all of them are correct."

Source: same post, paras 4, 1, 9.

## Formal statement
Model: a specific path of n = 500 steps; at each step a specific nucleotide change must (i) occur, with probability a = 1/600, and (ii) fix, with probability b = 1/500 (2s, D7). Per-step success p1 = a*b = 1/300,000. All steps independent. P(path) = p1^n = (1/300000)^500. Recomputed: log10 = -500*log10(3e5) = -2738.56, so P = 2.75e-2739 and odds against = 3.64e2738 to 1 (Day: 3.6 x 10^2738 'to 1' and 2.7 x 10^-2739; the 2.7 vs 2.75 is a rounding/truncation difference of 2%). Reconciles.

## Assumptions
- Stated: one specific nucleotide per step; 500 steps for a new species; independence; 'Nobody knows' how many positive mutations are available, so Spetner turns the question around (D7b).
- Implicit: 'step' is not defined (generation? fixation event?); 1/600 has no stated referent; the 500 is unsourced; the product treats the path as pre-specified (the specific-vs-any issue G3).

## Responses
- Against: Camestros and McCarthy on specific-vs-any (G3); Day's own paragraph 'one cannot simply assume that only one mutation is available'. Ulam (D4a, p.21) called the chain argument 'naive'.
- In support: Day: 'all of them are correct'. Ulam wrote the same multiplicative form in the opening of his talk (D4a) before saying it was not the problem.
- Weaknesses: the arithmetic is right, and it is a statement about one specified path. Day's text does not claim it as the probability of evolution; the next two paragraphs reframe it as a requirement on the number of available mutations (D7b). Calling it 'correct' while not using it as the main case is consistent.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Spetner, Not By Chance (1997) | not retrieved | unverifiable |
| Fisher 1930 / Haldane 1927 | see D7 | partial |

## Pre-registered prediction
Written before the computation. Prediction (Day): 3.6e2738. Standard arithmetic: 10^(500*log10(3e5)). Result that would change a verdict: |log10 - 2738.56| > 0.05.

## Check
`python3 -I -c "import math;L=500*math.log10(300000);print(L, 10**(L%1), 10**(1-L%1))"` -> 2738.5606, 3.636, 2.750. Reconciles (Day: 3.6, 2.7).

## Simulator variables implied
Path length n; per-step probability a*b; specific-site vs any-site switch; number of beneficial mutations per step.
