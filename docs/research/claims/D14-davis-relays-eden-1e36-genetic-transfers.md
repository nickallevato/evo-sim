---
id: D14
title: "Rebekah Davis (relaying Eden): about 10^36 genetic transfers would be needed to form one ordered pair of genes"
side: ally
branch: D
parent: D
edges: [{type: supports, target: D}]
load_bearing: false  # not a premise of ROOT
sourcing: secondhand
status: extracted
verdicts:
  internal: holds      # 1/(1e-15 x 1e-21) = 1e36; population needed 1e36/(1e12 x 1e-6) = 1e30; reproduces from Eden's printed inputs
  fidelity: accurate      # Eden p.9 prints "1036 genetic transfers" (= 10^36)
  external: contested      # Eden calls it a "very rough estimate" built on unsourced probabilities; a different mechanism (transposition of operon genes) from point-mutation evolution
---

## Statement (verbatim)
> "it would take about 10 to the 36th power of genetic transmissions to do that."

Source: Rebekah Davis (Examining Origins), [Can Evolutionists Finally Face the Math? Challenge Issued!](https://www.youtube.com/watch?v=jDxFtCOGZ3A), 2026-09-23, t=00:12:05 (quotes-critics RD-03). `secondhand`: she relays Eden.

Primary text:

> "Then to achieve a single ordered pair of genes on these assumptions would require something like 1036 genetic transfers."

Source: Eden, Wistar p.9 ('1036' = 10^36).

## Formal statement
Eden's chain (p.9): a transposition of chromosomal material 'should occur in an unselected environment with a frequency of 10^-15 for each sequential pair of genetic transfers'; a specific transposition has probability 10^-21 (uniform chain segmenting); so a single ordered gene pair needs 1/(10^-15 * 10^-21) = 10^36 genetic transfers. E. coli: 10^12 two-hour periods since life began, 10^-6 of the population mating at any instant, so the required population is 10^36/(10^12 * 10^-6) = 10^30 cells (Eden: 'about 10^13 tons or a layer ... two centimeters thick'). All reproduce arithmetically.

## Assumptions
- Stated (Eden): 'a very rough estimate'; unselected environment; uniform chain segmenting.
- Implicit: no selection for intermediate rearrangements; transposition frequency 10^-15 and 10^-21 are unsourced.

## Responses
- Against: Eden's own caveat ('a discovery of a new transposition mechanism can make such speculations an exercise in futility', p.9); selection on operon organisation, recombination, horizontal transfer.
- In support: Davis (relay); Day (D).
- Weaknesses: Davis says she has not read the book (RD-01) and relays Duffy's presentation; the claim is Eden's and concerns bacterial operon organisation, not human-chimpanzee divergence.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.9 (Eden) | quoted above | accurate |

## Pre-registered prediction
Written before the arithmetic. Under Eden: 10^36 and 10^30. Standard arithmetic reproduces both. Result that would change a verdict: none; the input probabilities are what is uncertain.

## Check
`python3 -I -c "print(1/(1e-15*1e-21), 1e36/(1e12*1e-6))"` -> 1e36, 1e30. Reconciles.

## Simulator variables implied
Transposition/rearrangement frequency; population size; number of mating periods.
