---
id: D9a
title: "Dawkins's Weasel actually demonstrates the opposite of its purpose, since its 50-generation estimate is off by four orders of magnitude"
side: day
branch: D
parent: D9
edges: [{type: depends-on, target: D9},{type: supports, target: D}]  # D9a -> D was typed attacks; as D9 (target = Dawkins's Weasel, no node). Judgement: read as support for D (2026-10-08)
load_bearing: false  # illustrative
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur      # the published Weasel is a truncation-selection algorithm; the 540,000 figure is for a different system (a population with constant s); a Weasel with Day's own 12 offspring and 5% mutation (exploratory run) completes in ~1,760 generations, not 540,000
  fidelity: n/a      # Day's inference, not a source quote
  external: contested   # the "known target" objection (also Day's) cuts the other way; R4 D1: known-target walks are Weasel-like and uninformative on this
---

## Statement (verbatim)
> "So Dawkins’s little program which was meant to demonstrate the viability of evolution by natural selection actually demonstrates the precise opposite, since his estimate of 50 generations was off by four orders of magnitude, or about 11,000x."

> "Although, obviously, it doesn’t make sense, since as the usual critique correctly points out, the target phrase is known from the start, which is not the case in the evolutionary context."

Source: [Probability Weasel](https://voxday.net/2026/09/12/probability-weasel/), 2026-09-12, voxday.net, paras 12 and 7.

## Formal statement
Claim: T_Weasel(Dawkins parameters) = 50 generations; T_real(population-genetic model, s = 0.001) = 540,000; hence Weasel is 'off' by 10^4. The comparison treats the Weasel's per-generation selection (pick the best of N offspring; truncation selection, effective advantage of the best offspring over the mean is large) as an advantage s that applies to every individual of a standing population of 10,000. Those are different systems; the Weasel 'estimate' of 50 is a runtime of an algorithm, not an estimate of anything biological, and Dawkins's own description of the algorithm is the first quotation in Day's post.

## Assumptions
- Stated: the 5% is a mutation probability, not a selection advantage (Day says so), and the relevant s is ~0.001.
- Implicit: Weasel-as-published is meant to model a real species.

## Responses
- Against: (a) T(original Weasel, N = 100, P = 0.05) is itself ~50-80 generations (exploratory: mean 78, median 73, p5-p95 49-121; Day's 'about 50' is within a factor 1.6 and Dawkins's published runs vary), so the original estimate is right for the algorithm. (b) With Day's own 12 offspring, same algorithm: mean 1,763, median 1,302 (p5-p95 387-4,761), i.e. 1,300-1,800 generations, not 540,000. (c) Dembski (ally) agrees the Weasel's fitness function is chosen (D13).
- In support: the Weasel's known target is a real disanalogy (Day, Dembski).
- Weaknesses: the 'precise opposite' does not follow from the figures. Day makes the 'target known' objection himself two paragraphs earlier, i.e. he treats the Weasel as non-representative, then uses it to claim evolution's numbers are off.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Dawkins 1986 (via approxion.com) | quoted in Day's post | secondhand |

## Pre-registered prediction
Written before the algorithm runs. Under Day: T(N=12, P=0.05, truncation) is much larger than 50 and scales as 540,000/50 = 10^4. Under the opposing model: T scales weakly with N (log N) and is 10^2-10^3. Result that would change a verdict: T(N=12, P=5%) >= 10^5 (not observed).

## Check
R4 D1 (research/checks/results/R4-D1-spike.md, review #11, 2026-10-09): the RNA walks are known-target and Weasel-like; they carry no weight on this claim.

Exploratory scratch run (python3 -I, numpy, seed 20261007/8, not committed): Weasel with 28 letters, alphabet 27, 400 replicates each: N = 100, P = 0.05: mean 78.3 (elitist and always-different-letter variants 78-79); N = 12, P = 0.05: mean 1,763 (300 replicates); N = 100, P = 0.01: mean 140. Not reproducing 50 (Day) is a 1.6x difference. Ranks of the claim: arithmetic of the 'four orders' holds only for the non-Weasel system.

## Simulator variables implied
Selection scheme (truncation vs proportional); offspring number; per-letter mutation probability P; alphabet; target-known flag.
