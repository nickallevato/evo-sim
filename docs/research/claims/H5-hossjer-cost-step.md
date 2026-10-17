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
  external: "contested"   # R4 H8 kscale64 (15e4941, post hoc; K = 64,000, 60/60 jobs): 'slower than 1/300' stays conditional on K (tested to 64,000) and on the survival horizon; K1' miss (0.0863), K2' indeterminate (D = 30 interval 348 at 10k, bracket 294-368 straddles 300; 490 at 20k), K3' hit (0.567), K4' hit / marginal miss; no K trend; verdict unchanged. Earlier: R4 H8 kscale16 (409378f, post hoc): any 'slower than 1/300' reading is conditional on K (tested to 16,000); K1 miss, K2 indeterminate (D = 30 interval point 546, bracket 473-631), K3 miss, K4 hit; verdict unchanged. Earlier: R4 H8: Hossjer's conditional is confirmed (0.0351 per generation payable under hard selection from R about 2-2.7 at in-model D; under soft selection at every R, conditional on purely relative fitness); human-lineage R unsourced (R5 draft V17). Earlier: depends on H. R4 H3: the conditional is mechanically supported (shared budget); 15,800/450k payable at R ~2-3 under hard adaptive + soft load; cost step still uncomputed by Hössjer | R4 HF (2026-10-13): as H (h-scope, Day-1 clause, latency vs throughput); conditional on h and R, external stays contested.
verdict_scope:
  external: "'slower than 1/300' stays conditional on K (tested to 64,000) and on the survival horizon"
---

## Statement (verbatim)
> "Vox Day convincingly argues that if many nucleotides at which fixation takes place have a selective advantage (so that natural selection acts on all these mutations) there is a reproductive cost of having many fixations going on in parallel."

Source: Hössjer, [MITTENS - Convincing Arguments Against Neo-Darwinism](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), PDF attached to Dembski's post, 2026-09-14, p.3 (§2).

> "it implies that the number of fixations with a selective advantage along the supposed human lineage is far less than what equation (4) predicts, perhaps more in line with equation (3)."

Source: same, p.3 (HO-03 in `sources/quotes-critics.md`).

> "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli."

Source: same, p.3 (HO-06).


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
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

R4 H8 (research/checks/results/R4-H8.md; fix pass 6d1359e; reviews #29-#31): the conditional behind Hössjer's "far less than what equation (4) predicts" is confirmed in Haldane's own regime. Hard selection sustains 0.0351 per generation from R between 2 and 2.7 at the in-model D (the same R found by R4 H3), with the whole excess spent on adaptive substitution; soft selection sustains it at every R tested, provided fitness is purely relative. The run confirms the conditional; it does not refute it. The cost step is still uncomputed by Hössjer (internal `non-sequitur` unchanged), and whether the human lineage had that R is unsourced on both sides (external `contested` unchanged). The K = 16,000 run proposed in R4-H8 section 8.2 awaits approval.
R4 H8 kscale16 (post hoc, 409378f; `results/R4-H8.md` section 9; 60/60 jobs, na-workhorse): at K = 16,000 the pre-registered K1 (lam50 x D 0.072-0.078) missed (0.0549), K2 (D = 30 interval) is indeterminate (point 546, bracket 473-631 straddles 480), K3 missed on the point (0.571 vs 0.59-0.61), K4 hit (D 22.8, 21.4). 'Slower than 1/300' stays conditional on K (tested to 16,000): it is not removed and not K-stable. Critic side: the finite-size explanation (interval falling toward 285-340) is not supported at K <= 16,000. Day side: 'up to 10-25% shorter' is not supported either, and his verbatim upper bound is unaffected. Verdicts unchanged. The optional K = 64,000 stage is not approved.

R4 H8 kscale64 (post hoc, 15e4941; `results/R4-H8.md` sections 10 and 10.1; 60/60 jobs, 7,720 s, na-workhorse; combined review #49 at b30137d; fix pass 4442c99): at K = 64,000 K1' (lam50 x D 0.050-0.068) missed above (0.0863; lam50 0.003492, D 24.71, phi 0.82), K2' (D = 30 interval) is indeterminate (10k point 348, bracket 294-368 straddles 300; the same runs give 490 at the 20k horizon, which would read keep), K3' hit (R = 2: 0.567), K4' hit at R = 1.111 (24.71) and a marginal miss at R = 2 (23.87). The 10k point estimates 566 / 484 / 441 / 546 / 348 at K = 500 / 1000 / 4000 / 16,000 / 64,000 are not monotone, so no K trend is established; the horizon matters as much as K. R = 2 is about 5.7x faster than 1/300 at every K tested. Day side: his verbatim upper bound is unaffected under R1 (every point is above 225; only the bracket edge, 294, is below 300). Critic side: the finite-size reading predicts the low 10k point, but 20k gives 490. 'Slower than 1/300 at D = 30, R = 1.111' stays conditional on K (to 64,000) and on the survival horizon.

R4 GAP05 (research/checks/results/R4-GAP05.md; pre-registered, combined review `REVIEW-R4-GAP05-combined.md`, fix pass 5601687; integrated 2026-10-11): numeric anchor for the HO-11 / Drift Deathmarch premise. On a sourced coding DFE (Kim, Huber & Lohmueller 2017 Table 3; Boyko 2008 row), the coding-only drift account fixes about 15,000-21,000 slightly deleterious nonsynonymous mutations per lineage (9,000-26,000 across rows, N_e, mu), 17-30% of the neutral-equivalent base, with log-fitness decline 0.29-0.43 (pre-registered base mu = 1.2e-8, T = 252,000, N_e 1e4) and about 0.8-1.1 on a divergence-calibrated base (post hoc, k = 2.2-2.4; ln 3 = 1.10). Day's premise (hominids fixed many slightly deleterious variants) is supported; a collapse is not (no row beyond ln 3 on the pre-registered base; compensation and the noncoding class are unsourced). No verdict change.

R4 HF (research/checks/results/R4-HF.md; reviews #66-#69; integrated 2026-10-13): Hossjer's conditional (a parallel reproductive cost applies if many fixations were selected) inherits H's scope. Day side: the hard cap reproduces (PA3, within 4-16% of H8); at R = 1.111 and D = 30 the 95% interval lies wholly above 300 at every K tested (K = 1,000: 419-568; 16,000: 342-720; 64,000: 326-768), so 1/300 is conservative under hard selection (PC3; R-scope per Critic-6: 213-349 at R = 1.2, 50-69 at R = 2); with 30% hard selection the rate is within about 1.3-1.7x the hard cap, and Term 3 holds in-model at h = 0.3; quadratic synergy against an absolute optimum lowers the rate; the cost per substitution is not reduced in any soft or truncation arm, only not charged (softWF D 16.2-16.8 against about 16 hard; mean log-viability about -27 at lam 1.6); s3.3.1 is literally true of s_max. Critic side: soft selection and noise-free or noisy truncation (genotypic share down to 0.1) sustain >= 0.8-1.6 substitutions per generation at R >= 1.111, >= 217x the hard cap, so Term 3 is not a bound across mechanisms; 10% hardness leaves about 2.6-3.5x the hard cap; the softJ failures were a fill lag (80 of 80 long-burn runs pass) and no K effect on the sustained rate up to lam 1.6 (post hoc trace analysis); weak selection sustains more than strong under hard selection (PA5). Both: the answer turns on the unsourced h and R. Caveats: HF-d's 9-generation figure is the second horn of Day's stated dilemma (see ledgers/slips.md and R4-HF.md) and the S3 2.39 is the upper-end scenario only. HO-11 (no claim file; see ROOT row 4 and the R4 GAP05 paragraph): 'the overall fitness of the population declines over time' external contested (supported only at upper-end U_d = 3, Ne = 1e4, under the hard-selection reading); 'and the population eventually (and quite rapidly) dies' proposed contradicted in-model (about 1e-5 log units per generation); not applied here, awaiting a claim file. No verdict value change.

R4 L2 (research/checks/results/R4-L2.md; registered ade0542; reviews #87-#89; fix-passed 2026-10-14; integrated 2026-10-14; no verdict value moves, external stays `contested`): Sourced proxies for h in humans (L2; route (a) under the audit's mapping A1, route (b) under M-b1; neither mapping recovers h when applied to the HF mix model): route (a), population regulation in nine European countries 1470-1870, [0.125, 0.256]; route (b), viability share of Crow's index in ten pre-transition records, [0.284, 0.641]; the routes do not overlap, which may reflect that they measure different quantities. Governing hull [0.125, 0.641], band MH, no value move. For H5: in-model a reproductive cost of parallel fixations exists at every h > 0; it is uncapped only at h = 0. Credit to Day: on the registered readings no eligible record on either route gives a proxy below 0.1 (reading-dependent: it fails if route (a) takes the authors' second baseline), and the same source also reaches high estimates (country points, median about 0.70-0.74). Credit to the critics: no sourced support for the strong Day-side proxy B-HH; the audit's prior 0.1-0.3 is met by route (a) and missed on the high side by route (b); both mappings are unvalidated (tool validation queued). R stays unsourced (V17); h stays a declared bracket.

## Simulator variables implied
Fraction of lineage fixations that are selected, selective mortality budget, d, L, mu ratio.
