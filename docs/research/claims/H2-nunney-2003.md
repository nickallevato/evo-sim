---
id: H2
title: "Nunney 2003: the cost of selection is substantially less than Haldane's for M > 1/2 and is eliminated by soft selection, but rises sharply for M < 1/2 and Haldane's 300 binds at M = 0.1"
side: literature
branch: H
parent: H
edges: [{type: attacks, target: H}, {type: supports, target: H}]
load_bearing: true  # The only H-branch rebuttal in the corpus (balance ledger) and also the source that confirms Haldane's 300. Whether H survives depends on the human value of M and on hard versus soft selection.
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: accurate
  external: pending
---

## Statement (verbatim)
> "For M > 1/2, the cost of natural selection is substantially less than Haldane's estimate; however, when M < 1/2, the cost (and particularly the fixed cost) increases in an accelerating fashion as M is lowered."

Source: Nunney L. 2003, [The cost of natural selection revisited](http://www.sekj.org/PDF/anz40-free/anz40-185.pdf), Ann. Zool. Fennici 40:185-194, Abstract (read from an existing Internet Archive capture, per bib-literature.md; the abstract quote is in `sources/quotes-literature.md`). The apostrophe in "Haldane's" is a modifier letter in the PDF text.

> "Based on mutation-selection balance and 10% selective mortality, he suggested that the limit to adaptive evolution was about one allelic substitution per 300 generations."

Source: Nunney 2003, Abstract.

> "As a result, soft selection inevitably reduces or eliminates the cost of substitution. However, given directional environmental change, it is likely that hard selection will dominate the adaptive process"

Source: Nunney 2003, Introduction.

> "This relatively large population will become extinct if the environmental change requires allelic substitution faster than about every 300 generations"

Source: Nunney 2003, Discussion (example with K = 10,000, u = 5 × 10⁻⁶ per gamete, M = 0.1).

> "Unfortunately, soft selection is only important when natural selection is driven by intraspecific competition."

Source: Nunney 2003, Discussion.

## Formal statement
M = 2Ku: the number of new mutations per generation, with K carrying capacity and u mutation rate (Nunney's definition, "approximated by M = 2Ku"). Cost C = C_0(M) + n C_1(M) for n loci selected simultaneously (fixed cost plus per-locus cost); the fixed cost reflects genetic deaths during the stochastic phase when the beneficial allele is rare.
Reported results (Discussion): M = 10 tolerates substitutions at 7 loci every 40 generations; M = 1 a single locus every 20 generations; K = 10,000, u = 5e-6 gives M = 0.1 and extinction when substitutions come faster than about every 300 generations; K = 5,000 about every 700 generations.

derived (R2): M = 2 x 10,000 x 5e-6 = 0.1 (holds); the K needed for M = 1/2 at u = 5e-6 is 0.5/(2 x 5e-6) = 50,000 (matches the abstract's "must be 50 000 for M = 1/2"; holds).
Parameter link: `haldane.gens_per_substitution` = 300 (verified via Nunney); proposed `cost.M` = 2Ku.

## Assumptions
- Stated: hard selection in the simulations ("The simulation model was a model of hard selection"; juvenile survival independent of density); density-dependent regulation allows mortality to shift from random to selective.
- Implicit (for use against H): that the human ancestral M is above 1/2, and that human adaptation is closer to soft selection. The paper's own caveat is that interspecific competition, predation and abiotic factors "are unlikely to result in soft selection".

## Responses
- Against: Day's Z19984826 §3.3.1 argues that truncation, soft and multiplicative moves "are mechanisms for redistributing a fixed reproductive budget, not mechanisms for inflating it" and that none raises s_max above order unity (H8); this does not engage Nunney's simulation. Z18168236 §6.2 dismisses soft selection and truncation as "verbal rather than mathematical" (H), which does not describe Nunney's simulation.
- In support: Day's H cites the 300 figure; Nunney confirms it for M = 0.1.
- Weaknesses in the responses: no critic in the corpus engaged Nunney (balance ledger); Day does not cite it; the value of u for beneficial mutations in humans is not in the repo.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1957 | (via Nunney) "a typical allelic substitution required about 30N genetic deaths. However, he believed that, in general, only about 10% of the overall mortality would be related to genotype, leading to a total mortality of 300N per substitution." | accurate secondary report |
| Wallace 1970, 1975 (soft selection) | cited by Nunney; primary not retrieved | unverified |
| Kimura 1968 | "If correct, this result has far-reaching consequences, both for the interpretation of molecular data (Kimura 1968) and for expectations regarding the survival of populations exposed to long-term environmental change." | accurate (Nunney's own sentence) |

## Pre-registered prediction
- Under the literature (Nunney): the cost depends on M; hard selection at M > 1/2 allows far shorter intervals than 300; soft selection removes the cost.
- Under Day (H): the interval is 300 (with d: 300/d in nominal generations) independent of M; soft/truncation moves redistribute but do not raise s_max.
- Result that would change a verdict: the check in H reproducing Nunney's M-dependence (supports H2) or not; and the human M value from independent sources (K ancestral near 1e4-1e5; u beneficial per locus). The fixed-cost mechanism ("time to escape drift") suggests a link to the cost rising as M falls; the simulation should check it.

## Check
Script: `research/checks/h_cost_of_selection.py` (planned; spec in H). · Result: not run · Review: pending

## Simulator variables implied
K, u (per-locus beneficial mutation rate), M = 2Ku, R (net reproductive rate), n loci, hard versus soft switch, density dependence.
