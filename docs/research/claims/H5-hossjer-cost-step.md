---
id: H5
title: "Hössjer: after scaling by mutation rate and genome length the gap is ~2x, but Haldane's cost of parallel selected fixations keeps the selected count near 15,800, so the MITTENS conclusion stands"
side: ally
branch: H
parent: H
edges: [{type: supports, target: H}, {type: revises, target: A5}]
load_bearing: true  # The ally's route to keeping the conclusion after conceding most of the LTEE-scaling objection (A5). The cost step carries the conclusion and is asserted, not computed.
sourcing: firsthand
status: reviewed
verdicts:
  internal: "non-sequitur"   # the 15,800 is a rate scaling, not a cost computation (10.5x Haldane's 1,500)
  fidelity: pending
  external: "contested"   # depends on H. R4 H3: the conditional is mechanically supported (shared budget); 15,800/450k payable at R ~2-3 under hard adaptive + soft load; cost step still uncomputed by Hössjer
---

## Statement (verbatim)
> "Vox Day convincingly argues that if many nucleotides at which fixation takes place have a selective advantage (so that natural selection acts on all these mutations) there is a reproductive cost of having many fixations going on in parallel."

Source: Hössjer, [MITTENS - Convincing Arguments Against Neo-Darwinism](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), PDF attached to Dembski's post, 2026-09-14, p.3 (§2).

> "it implies that the number of fixations with a selective advantage along the supposed human lineage is far less than what equation (4) predicts, perhaps more in line with equation (3)."

Source: same, p.3 (HO-03 in `sources/quotes-critics.md`).

> "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli."

Source: same, p.3 (HO-06).

## Formal statement
Hössjer's chain (p.2-3): F_max = (t_div x d)/(g_len x G_f) = 9e6 x 0.45/(20 x 1,600) = 127 (eq. 2.2); mutation-rate adjustment x (1.25e-8/1e-10) = 15,800 (eq. 2.3, his "equation (3)"); genome-length adjustment x (3e9/4.6e6) = 10 million (eq. 2.4, his "equation (4)"); then "the number of fixations with a selective advantage ... is far less than ... equation (4) predicts, perhaps more in line with equation (3)".

derived (R2 recompute):
- 9e6 x 0.45/(20 x 1,600) = 126.6 (holds); 127 x 125 = 15,875 (his 15,800; holds within rounding); 15,800 x 3e9/4.6e6 = 10.3 million (holds). His neutral count with d in the rate: 3e9 x 0.45 x 1.25e-8 x 450,000 = 7.59 million (holds; HO-04). Without d the same expression is 3e9 x 1.25e-8 x 450,000 = 16.9 million (balance ledger: "16.9M vs 20M").
- His cost step is not computed. The Haldane limit applied to the same window gives 450,000/300 = 1,500 selected fixations (675 with d = 0.45; Z18168236's 487 uses 325,000 generations). His "perhaps more in line with equation (3)" figure, 15,800, is 10.5 times Haldane's own number (1,500), so it sits above both cost-based figures in Day's corpus (487 from Haldane + d, H; about 6,690 from Term 3, H1) and has no derivation.
- Gaps (corrected 2026-10-08; this line earlier read "The 2.2x gap ... arises from d inside the neutral rate"). Neutral, eq. 3.1: 20M/7.59M = 2.63. Rate scaling, eq. 2.4 (his "only by a factor of 2"): 20M/10.30M = 1.94. Neither is 2.2. The 2.2 is d's factor (1/0.45 = 2.22). Without d the neutral count is 16.9M (1.19× short) and the scaled bound is 22.9M (1.14× above 20M).

## Assumptions
- Stated: parallel fixation between loci in both calculations; independence of loci; "Haldane's cost restrictions for parallel fixations" apply only to selected fixations (his footnote 7); a cost argument "is an instance of Haldane's dilemma".
- Implicit: that most differences along the human lineage are selected (otherwise eq. (3.1) neutral count applies, which he computes as 7.6M); that Haldane's cost holds under the relevant selection regime (H2, H7); his own view: "I rather advocate uncommon descent between the two species" (HO-10), i.e. the conclusion is not common-descent-impossible for him but that Neo-Darwinism cannot do it.

## Responses
- Against: Nunney 2003 (H2) and Keightley 2012 (H7) for the hard-selection premise. McCarthy's A5 line (genome size and mutation rate) is conceded by Hössjer; a critic (Hancock GG-02) objects that the MITTENS arithmetic is off by a factor of two (both lineages).
- In support: Day's Z18168236 (H).
- Weaknesses in the responses: no critic engaged Hössjer's cost step; it contains no computation; his post is dated after Day's 2026-05-07 retraction (H1), which narrows the cost-bound to selected substitutions, and Hössjer applies it to selected ones only.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1957 | cited as footnote 3 | primary not retrieved; see H |
| Wright 1938 (rate d mu with overlapping generations: footnote 6) | not retrieved | unverified |
| Kimura 1968 | footnote 4 | not retrieved (abstract only in the repo) |

## Pre-registered prediction
- Under the claimant's model (Hössjer): the selected-fixation count along the human lineage after the Haldane cost is of the order 1e4, between 1,500 and 15,800 (his "perhaps").
- Under the opposing model: the cost step gives 1,500 (or 675 with d), well below 15,800, if hard selection holds with s_max = 0.1; under soft selection or M above 1/2 the limit is higher (H2).
- Result that would change a verdict: the H simulation, run with Hössjer's inputs (t_div = 450,000 generations, m = 0.10), giving a number between 1,500 and 15,800 or outside.

## Check
R4 H (research/checks/results/R4-H-C2.md): Hössjer's 15,800 is 10.5x Haldane's own 1,500 over 450,000 generations (675 with d); it comes from a mutation-rate scaling, not a cost computation, so the cost step is unsupported by the Haldane arithmetic. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: `research/checks/h_cost_of_selection.py` (planned, H). · Result: not run · Review: pending

R4 H3 (research/checks/results/R4-H3-human.md): Hössjer's conditional (if many fixations were selected, a parallel reproductive cost applies) is mechanically confirmed: concurrent sweeps share one budget (D1a). His 15,800 over 450,000 generations (0.035 per generation) is payable at R ~ 2-3 (D = 20; R ~ 3 with long-run phi) under hard adaptive selection with a soft load. It is close to GAP-01's coding-only maximum (1.2e4), so it is compatible with a coding-only reading. 'Perhaps' is a hedge, not a target, and the cost step remains asserted rather than computed. Review: `research/checks/REVIEW.md` (review #7, 2026-10-09).

## Simulator variables implied
Fraction of lineage fixations that are selected, selective mortality budget, d, L, mu ratio.
