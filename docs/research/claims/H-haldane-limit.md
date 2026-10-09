---
id: H
title: "Haldane's cost of selection caps mammals at about one beneficial substitution per 300 generations; with d = 0.45 and 325,000 generations, 487 fixations (shortfall 41,068-fold)"
side: day
branch: H
parent: ROOT
edges: [{type: supports, target: ROOT}, {type: depends-on, target: C2}, {type: depends-on, target: H9}, {type: attacks, target: G2}]  # was attacks G1 (Day's own claim). Z18168236 s2.3 answers the generic parallel-fixation objection; judgement (2026-10-08): G2 is the corpus's main critic statement of it
load_bearing: true  # This is the only argument in the corpus that does not rely on the LTEE rate: it bounds *selected* substitutions from first principles. If it fails, ROOT rests on A (LTEE scaling) and B. It was narrowed by the 2026-05-07 retraction (H1) and Hössjer (ally) leans on it (H5) to keep a conclusion after conceding most of A5.
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # arithmetic 300, 487, 41,068
  fidelity: partial   # the 300-generation figure is reported accurately by Nunney 2003 (primary Haldane 1957 not retrieved); the d extension, parallel-budget claim and the Kimura & Ohta recombination citation are Day's
  external: "contested"   # cap is ln R/D, so 10% is not general; Haldane regime (R ~1.1, D ~20-30) untested; soft selection did not remove cost; human M, R undetermined; H1 scope applies to the 20M comparison
---

## Statement (verbatim)
> "Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes on a population."

Source: [Independent Confirmation of Haldane's Limit](https://zenodo.org/records/18168236), Z18168236, 2026-01-05 (record modified 2026-01-07), Abstract, ¶8 of docx text extraction (Q47).

> "Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations"

Source: Z18168236, §4.2, line 48 of the text extraction (Q48 in `sources/quotes-day.md` lists ¶41; the extraction has no blank lines, so the count here is 48).

> "This objection misunderstands Haldane's argument. The 10% selective mortality is a total budget for the population, not a per-locus allocation."

Source: Z18168236, §2.3 (the parallel-fixation reply).

> "If that cohort represents only 45% of the population-generation product, then selection operates at only 45% of the rate Haldane assumed."

Source: Z18168236, §4.2.

## Formal statement
Haldane: cost per substitution C = 30 N selective deaths (diploid, single new copy); sustainable selective mortality m = 0.10 N per generation; minimum interval = C/(m N) = 30/0.10 = 300 generations. Parallel loci share the budget: sum of s_i <= s_max (Z18168236 §2.3).
Day's extension: effective generations G_eff = G x d = 325,000 x 0.45 = 146,250 (`generations_available.day_2025_effective`), achievable = G_eff/300.

derived (R2 recompute):
- 30/0.10 = 300 (holds); 146,250/300 = 487.5 (the paper truncates to 487; holds); 20,000,000/487 = 41,068 (the paper's 41,068x; holds); 91 -> 487: 487/91 = 5.35 and 1,600/300 = 5.33 (paper's "5.3 ... 5.4"; holds).
- Same arithmetic without d: 325,000/300 = 1,083; at 450,000 generations (2019): 1,500; at 252,000 (MITTENS 3.0): 840. Required 17.5M (SNV-only, `shortfall`) gives 20,833-fold; 205M gives 244,048-fold (derived).
- 2019 blog (Q49): 9,000,000 y/25 y/300 = 1,200 (table "Maximum fixed mutations: 1,200"; holds), with a separate x1.4 bp factor stated in the post.
- Parameter link: `haldane.gens_per_substitution` = 300 (verified only via Nunney 2003).
- Scope: the quantity bounded is adaptive (selected) substitutions. The argument compares it with the whole 20M differences; the 2026-05-07 retraction (H1) concedes that this class of bound "is a constraint on selectively driven substitutions alone, not on total substitutions" for the related Term 3. Applying d to a death-budget argument is an additional step (the budget is per generation of deaths; d rescales time).

## Assumptions
- Stated: hard selection (selective deaths add to other mortality); about 10% of mortality can be selective; independent loci (cost additive).
- Implicit: that most of the 20M differences are adaptive (otherwise the bound does not apply to them); that the cost per substitution is 30 N at all s (Haldane's approximation for a single new copy); that the 10% budget holds for human ancestors; that d (C2) multiplies a cost-based limit.

## Responses
- Against: Nunney 2003 (H2): cost "substantially less" for M > 1/2 and soft selection "eliminates" it, but at M = 0.1 a population dies if substitutions come faster than about every 300 generations (supports Haldane's number in that regime); Keightley 2012 (H7): the deleterious analogue cannot be hard selection in humans; Kimura's neutral theory (neutral substitutions pay no cost). Nesslig20 (H6) accepts the limit for selection and points out it does not apply to drift. Hössjer (H5) accepts the cost argument for selected changes.
- In support: Hössjer (ally) writes that Day "convincingly argues" the cost point; Nunney 2003 reports the 300 figure correctly.
- Weaknesses in the responses: no critic in the corpus engaged Nunney 2003 (balance ledger); Nunney's M > 1/2 condition has not been assessed for ancestral humans (K, u); the repo has no check yet.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1957 (via Nunney 2003) | "Based on mutation-selection balance and 10% selective mortality, he suggested that the limit to adaptive evolution was about one allelic substitution per 300 generations." | accurate via Nunney only; primary text not retrieved |
| Kimura & Ohta 1969 | recombination: word occurs 0 times | misread (H9) |
| Good 2017 (25 fixations, ~40,000 generations; Day cites "Nature 2017") | not located as such in the quoted passages | the 2019 post cites "NATURE, 2009" (Q02, Q64) |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: a Nunney-type simulation (carrying capacity K, net reproductive rate R, juvenile survival density-independent, selection among juveniles) with human-like parameters finds a minimum interval between substitutions of about 300 generations (or a few hundred), with parallel loci costing additively.
- Under the opposing model (Nunney 2003, Wallace): for M = 2Ku above 1/2 the minimum interval is far below 300 (Nunney: 7 loci per 40 generations at M = 10; one locus per 20 generations at M = 1); under soft selection there is no cost; at M of order 0.1 the limit is near 300 (Nunney's own K = 10,000, u = 5e-6 example).
- Result that would change a verdict: the human value of M. If M for the ancestral population (K near 1e4-1e5, with u the per-locus beneficial-mutation rate) lies well below 0.5, Haldane's 300 binds under hard selection (supports H); if above 1, it does not; and under soft selection it does not bind at any M. A direct question for R4 is whether the selection regime for human adaptation is hard or soft (Keightley 2012 says soft/relative fitness operates for the deleterious load).

## Check
R4 H (`h_cost_of_selection.py`, `h_nunney_gauss*.py`, `h_keightley_load.py`; research/checks/results/R4-H-C2.md) and H2 hard multilocus (research/checks/results/R4-H2-hard.md). Arithmetic holds (300 = 30/0.10; 487 = 146,250/300; 41,068). D = 30 is Haldane's input: diploid D = 2 ln(1/p0) gives 92-278 generations for standing variation (p0 1e-2 to 1e-6) and ~200 for a new mutation (p0 = 1/2N, D ~ 20), so 300 is the same order as the new-mutation case (Day-side point). Under hard selection the cap is ln R / D, so 10% is not a general bound; at R >= 1.3, haploid D ~ 7 the flip lies 9-100x above 1/300 (bracket). Haldane's own regime (R ~ 1.1, diploid D ~ 20-30 = ~1/300) was not tested, so the literal 1/300 is untested, not falsified. In the Nunney reconstruction soft selection did NOT remove the cost (soft T50 > hard T50 at equal supply, both models): the critics' stock reply is not reproduced (credit to Day). Human M and R are undetermined by the repo. The comparison with the 20M total falls under the scope argument Day conceded for Term 3 (H1). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none yet (spec: `research/checks/h_cost_of_selection.py`, planned). Spec: reproduce Nunney's (2003) model: K in {500, 5,000, 50,000}, M = 2Ku in {0.05, 0.1, 0.25, 1, 10}, net reproductive rate R, n loci selected at once; measure the minimum substitution interval (generations per locus) compatible with persistence under (a) hard selection (juvenile survival independent of density) and (b) soft selection (density-dependent). Targets: hard, M = 0.1, K = 10,000: about 300 per substitution; hard, M = 10: 7 loci per 40 generations; hard, M = 1: 1 locus per 20 generations; soft: no cost. Then apply d as a time rescaling to the result and compare with 487. · Result: not run · Review: pending

R4 GAP-02 (research/checks/results/R4-GAPS-04-07-02.md): Hernandez et al. 2011 (Science 331:920, main text) bounds strongly favoured classic sweeps at < 10% of human-specific amino-acid substitutions (no excess diversity trough vs synonymous), < 1.3-3e3 per lineage on a constant-rate extrapolation, while stating that 10-15% (possibly up to 40%) of amino-acid differences were adaptive: most adaptation was weak or soft. Consistent with alpha-scale K_a, which the cost question (H, H2-hard) still has to price. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

## Simulator variables implied
Selective mortality budget m, cost per substitution (30 N), hard versus soft selection, M = 2Ku, K, R, number of loci selected at once, d.
