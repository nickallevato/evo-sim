---
id: H2
title: "Nunney 2003: the cost of selection is substantially less than Haldane's for M > 1/2 and is eliminated by soft selection, but rises sharply for M < 1/2 and Haldane's 300 binds at M = 0.1"
side: literature
branch: H
parent: H
edges: [{type: attacks, target: H}, {type: supports, target: H}]
load_bearing: true  # The only H-branch rebuttal in the corpus (balance ledger) and also the source that confirms Haldane's 300. Whether H survives depends on the human value of M and on hard versus soft selection.
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a
  fidelity: accurate
  external: "contested"   # M-dependence reproduced both ways (R4 H3: D ~6.5 at M = 1 up to 99-163 at M = 0.01, ~15 + 1/M at low M); absolute T and soft-selection elimination not reproduced in R4-H-C2; human M unsourced
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
R4 H Model 1/2 (research/checks/results/R4-H-C2.md; EXPLORATORY reconstruction, Nunney's Eq. 3 and 5 lost in extraction, adjusted twice after seeing results): the qualitative M-dependence is reproduced (T50 rises as M falls, more steeply for n = 7). Absolute values are not (R = 10 is 2-12x below Nunney; R = 2.2, M = 0.1 hard gives 170 vs ~300). Soft selection did not reduce the cost at equal mutation supply (soft T50 1.5-3.5x hard). Human M is undetermined. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: `research/checks/h_cost_of_selection.py` (planned; spec in H). · Result: not run · Review: pending

R4 H3 (research/checks/results/R4-H3-human.md, stages C and M): the M-dependence is reproduced in both directions. D_eff ~ 6.5 (M = 1), 10.5 (0.3), 17-22 (0.1), 39-52 (0.03), 99-163 (0.01), i.e. ~15 + 1/M at low M. The pre-registered D + 1/M form failed at M >= 0.1 and approximately held at M <= 0.03. At M = 0.01 even R = 2 sustains only ~1/430. M >= 1 needs about 4e3 target sites per locus (derived:). Human M is unsourced. Review: `research/checks/REVIEW.md` (review #7, 2026-10-09).

## Simulator variables implied
K, u (per-locus beneficial mutation rate), M = 2Ku, R (net reproductive rate), n loci, hard versus soft switch, density dependence.
