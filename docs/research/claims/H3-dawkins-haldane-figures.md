---
id: H3
title: "Dawkins's 11,739 (dominant) / 321,444 (recessive) generations to reach half frequency, doubled to 642,888, are 87,916,307 times too slow for 20 million sites"
side: day
branch: H
parent: H
edges: [{type: supports, target: H}, {type: depends-on, target: G1}]
load_bearing: false  # Rhetorical illustration. The figures are Dawkins's (after Haldane), not Day's derivation, and the multiplication is serial.
sourcing: secondhand
status: extracted
verdicts:
  internal: pending
  fidelity: unverifiable
  external: pending
---

## Statement (verbatim)
Dawkins as posted by Day (`secondhand`: The Genetic Book of the Dead, 2024, not retrieved):
> "His answer was a mere 11,739 generations if the gene is dominant, 321,444 generations if it is recessive."

Source: Day, [88 Million x](https://voxday.net/2026/01/08/88-million-x/), B2026-01-08-88-million-x, posted 2026-01-08, ¶4 of extracted text (Q50). The passage describes a hypothetical selection pressure "for every 1,000 individuals with the mutation who survive, 999 individuals without the mutation will survive" and asks "how long will it take for such a new mutation to spread through half the population".

Day's use:
> "Dawkins somehow imagines that even 642,888 generations for one single base pair is more than enough time for evolution to take place. He’s off by a mere factor of 4.4 x 20 million, or 87,916,307x."

Source: same post, ¶6 (Q51).

> "Based on my necessary Bio-Cycle correction to the bacteria-based Kimura fixation model, that leaves 146,250 generations to fixate all of those base pairs."

Source: same post, ¶3.

## Formal statement
Dawkins/Haldane: time to reach 50% for a new mutation with s about 0.001 (999 survive per 1,000): 11,739 generations (dominant) and 321,444 (recessive). Day: t_site = 2 x 321,444 = 642,888; compare with G_eff = 146,250; ratio 4.396; multiply by n = 20,000,000.

derived (R2): 2 x 321,444 = 642,888 (holds); 642,888/146,250 = 4.3958 (Day: "4.4"); x 20,000,000 = 87,916,307.7 (Day: 87,916,307, truncated; holds as arithmetic). The step from "half the population" to 642,888 as a fixation time is a doubling Day does not explain (11,739 x 2 = 23,478 for the dominant case, not mentioned). The recessive/dominant choice drives the answer by a factor 27 (321,444/11,739 = 27.4).
Link: parameters.yaml `haldane.dawkins_figures` = [11739, 321444] (verified as Dawkins's numbers quoted by Day). The comparison treats 20,000,000 substitutions as sequential: 20M x t_site against G_eff. Day's own G1 position is that an empirical G_f includes parallelism; a single-allele time to half frequency does not.

## Assumptions
- Stated: a selection coefficient so weak as to "seem trivial" (about 0.001, not given numerically in the quote); recessive case.
- Implicit: that the human-chimp fixations are all of this weak size and recessive; that fixations occur one after another (serial); that the time to half-frequency equals half the time to fixation, so doubling gives a fixation time; that Dawkins's initial frequency (not stated in the quote) applies.

## Responses
- Against: none located in the critic corpus (not engaged). The serial reading is the target of the G2 critics (Myers PZ-01, Hancock GG-01, Ghijselen DZ-01) for the main MITTENS argument.
- In support: none.
- Weaknesses in the responses: not engaged.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1927 (the origin of the figures per Dawkins) | not retrieved | unverified |
| Dawkins 2024, The Genetic Book of the Dead | quoted only through Day's post | unverifiable (book not retrieved) |

## Pre-registered prediction
- Under the claimant's model: time to 50% for s = 0.001 with a recessive allele is of order 3e5 generations from a single copy; 20M independent such substitutions in series cannot fit.
- Under the opposing model: the figure depends on the start frequency and dominance; deterministic recessive timing from 1/(2N) with N near 1e4 is dominated by the early rare phase; parallel fixation across the genome removes the serial multiplication; and nearly all fixed differences are neutral, with fixation times of order 4Ne and a different set of numbers.
- Result that would change a verdict: a deterministic recursion (dominance h = 0 and 1, s = 0.001, p0 = 1/(2N) for N in {1e3, 1e4, 1e5}) that reproduces 11,739 and 321,444 for some (N, convention); then the inputs of the figures are identified and the factor 87.9M can be checked for its serial assumption.

## Check
Script: none yet (spec: `research/checks/h3_dawkins_figures.py`, planned; two-line deterministic recursion for dominant/recessive selection to 50%). · Result: not run · Review: pending

## Simulator variables implied
Dominance h, s, p0, target frequency (50% versus 100%), number of loci, serial versus parallel.
