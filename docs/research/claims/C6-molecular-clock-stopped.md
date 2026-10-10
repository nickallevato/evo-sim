---
id: C6
title: "Ancient DNA falsifies the constant-rate clock: 99.8% of fixation events fall before 7,000 BP; the clock predicts ~630 fixations in 350 generations and 21 are seen"
side: day
branch: C
parent: C
edges: [{type: supports, target: C}, {type: supports, target: B4}]
load_bearing: false  # Earlier (Feb 2026) aDNA paper whose counts differ from the later Z23046531; used to support recalibration (B4). ROOT does not depend on it.
sourcing: firsthand
status: reviewed
verdicts:
  internal: non-sequitur   # R4 X1 rule rev 2 (was arithmetic-error): N3 on his own basis: 630 is for 1.5e8 genome-wide sites, 21 is among 1,233,013 panel SNPs; scaling by his own panel size gives 5.2, which flips the comparison (>25%): not an arithmetic-error but a conclusion that ...
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: contradicted   # as stated, under his described method on real AADR genotypes (C1d): 3.6-5k post-6000 events vs 21; 132 configurations plus his documented two-period pipeline, which reproduces sample and SNP count but not counts, 3.6x. Best Day reading: underspecified (no damage/quality/coverage rule); damage is not the missing piece (library test). Reopens as contested if he documents a pipeline
---

## Statement (verbatim)
> "Instead, we observe that 99.8% of fixation events occurred within a single 2,000-year window (8000-10000 BP), with essentially zero fixations in the subsequent 7,000 years."

Source: [The Recalibration of the Molecular Clock](https://zenodo.org/records/18525185), Z18525185, 2026-02-08, Abstract.

> "The molecular clock predicts approximately 630 fixations per 350 generations (based on k = μ for neutral sites; see Appendix A)."

Source: same, §5.3.

> "This confirms that essentially all "fixations" were completion events for alleles already near fixation—not new substitutions traversing the frequency spectrum."

Source: same, §4.3.

> "E[total fixations] = 1.8 × 350 ≈ 630"

Source: same, Appendix A (with "For 150 million neutral sites: E[fixations per generation] = 1.2 × 10⁻⁸ × 1.5 × 10⁸ = 1.8").

## Formal statement
Observed (paper §1.3, §4.1): fixations from polymorphic states, 22,428 alleles total; timing tracked for 16,299; by bin: 10000+ BP 3,038 (18.6%); 8000-10000 BP 8,741 (53.6%); 7000-8000 BP 4,497 (27.6%); 6000-7000 BP 2; 5000-6000 BP 9; 4000-5000 BP 7; 3000-4000 BP 2; 2000-3000 BP 1; 1000-2000 BP 0; 500-1000 BP 0; 0-500 BP 2. Post-7000 BP total 21. Prediction: E = mu x G_sites x gens, with mu = 1.2e-8 (`mutation.mu_per_site_per_gen.pedigree_human`) and G_sites = 1.5e8 neutral sites.

derived (R2 recompute):
- 1.2e-8 x 1.5e8 x 350 = 630 (holds).
- The abstract's headline "99.8% within a single 2,000-year window (8000-10000 BP)" is not what Table 4.1 shows. That window holds 8,741/16,299 = 53.6%. The 99.8% figure is the share before 7,000 BP across three bins: (3,038 + 8,741 + 4,497)/16,299 = 99.86%. Result: arithmetic-error in the abstract's description (the table itself is internally consistent).
- Five different "fold" figures appear: 400-fold (abstract, §4.2; 70%/0.2% = 350), about 1,700x (§5.3, 133/0.078), 1,000x (§5.4: 20,000,000/19,500 = 1,026; 21/7,000 x 6,500,000 = 19,500, holds), 30x (Appendix A: 630/21), and a statistical p < 0.0001.
- Denominator mismatch: the 630 expectation is for 150M neutral sites genome-wide; the 21 observed are among the 1,233,013 panel SNPs. Scaled to the panel, 630 x 1,233,013/150,000,000 = 5.2 (derived). On that scaling the 21 observed is above, not below, the expectation. The comparison of 630 with 21 in §5.3 and the "p << 0.0001" in §9.5 therefore do not follow. Even the scaled figure presupposes that panel sites can register new neutral substitutions, which C1 disputes.
- 16,000 fixations in about 120 generations (10000-7000 BP) = 133 per generation (holds); the paper concludes this "suggest[s] a non-clock process" and §4.3/§5.2 itself attributes it to alleles "already near fixation" and to population replacement.

## Assumptions
- Stated: continuity (European samples only); a "fixation" is an allele polymorphic in an earlier bin and at 100% in a later bin.
- Implicit: sample-based 100% equals population fixation (bins as small as n = 129 at 8000-10000 BP); bins are samples of one continuous population (the paper's own §5.1 says Anatolian farmers replaced indigenous hunter-gatherers); panel sites measure substitution (C1); the neutral-site count 150M is the correct denominator for a 1.23M-site panel.

## Responses
- Against: C1 (ascertainment), C5 (neutral expectation), and the repo's denominator point above. No critic engaged the paper directly.
- In support: Day's C1a defence.
- Weaknesses in the responses: C1a does not address the denominator or the near-fixation admission in §4.3.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1968 / textbook k = mu | "Calculating the rate of evolution in terms of nucleotide substitutions seems to give a value so high that many of the mutations involved must be neutral ones." (abstract) | accurate for k = mu as a neutral-rate claim; the identity is a long-run substitution rate per lineage, not a rate per 7,000-year window of one panel |
| Zuckerkandl & Pauling (clock) | not quoted | unverified |

## Pre-registered prediction
- Under the claimant's model: the 22,428 "fixed" alleles are mostly completions; post-7000 BP completions from polymorphic states are far fewer than the neutral expectation.
- Under the opposing model: completions of near-fixed alleles are sampling and replacement artefacts, and the number of neutral new-mutation substitutions on a 1.23M-site panel in 350 generations is of order 5 or fewer, with most mutations not on the panel.
- Result that would change a verdict: the C1 simulation giving an expected panel-registered count that is (a) well above 21 (supports Day's deficit) or (b) at or below 21 (removes the deficit).

## Check
R4 C1c + C1d (research/checks/results/R4-C1c.md; research/checks/results/R4-C1d.md; reviews #9-#10, 2026-10-09). C1c (model with real AADR v62.0.p1 call depth and an ancestry-replacement Wright-Fisher model, 44 scenarios): no cell reproduces Day's eligible count, profile, tracked fraction and start table together; the model count after 6000 BP is 1.5k-3.9k at constant N_e 1e4 (70-190x the 21) and reaches ~21 only at closed-population N_e ~1e5-3e5 or growth/step schedules to 1e5-1e6; Day's own d = 0.45 gives 739. C1d (Day's statistic on the real v62.0.p1 and v66.p1 1240K genotypes, E1 eligibility, T2 dating, his European sample): 62,757 eligible / 4,957 events dated 5000-6000 BP or younger (v62) and 48,888 / 3,649 (v66), against 22,428 / 21; 84% of the 4,957 sit in the 0-500 BP bin; 132 grid cells and his documented two-period pipeline (Z23046531: sample and SNP count reproduced to 0.4% and 0.02%, events 63,631 vs 17,814) do not close the gap; library type and damage rate do not explain the transition excess; transversions alone give 36-44 (autosomes). Credit to Day: the start-frequency table reproduces to 0.4 points on v62 and his §4.3 near-fixation description is right in kind (98.8%). No code was found on Zenodo, GitHub or OSF; the scripts promise is in Z23046531, not Z18525185. Verdict: external `contradicted` for the statistic as described; best Day reading "underspecified"; reopens as `contested` if a pipeline is documented.

R4 C1 + C1b (research/checks/results/R4-B3b-C1.md, research/checks/results/R4-C1b.md, `c1b_day_binned_statistic.py`, 20 reps x 13 configs x 16 readings): the 630 arithmetic (150M x 1.2e-8 x 350) is correct, but the denominator is wrong for a polymorphism-ascertained panel (neither 630 nor the uniform rescaling 5.2 is the right comparator). C1b simulated Day's binned first-passage statistic literally: every reading gives 1.2e3-1.7e4 post-7000 BP events for both neutral (Ne 7e3-2e4) and Day's d = 0.45 model, against 21 observed; but the model also misses Day's own bin profile (7000-8000 BP ~1,350 vs 4,497; pre-7000 share 38-60% vs 99.86%). Verdict: not reproducible from the published procedure; cannot adjudicate. Neither "neutral predicts ~0" (Day side) nor "does not rescue Day" / "deficit vs neutral" (earlier audit wording) is supported. (Superseded by C1c: measured mean depth is 49 / 62 / 282 chromosomes per site in the three oldest bins, so sparse calls are not the cause, and ancestry replacement widens rather than closes the gap.) Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: shared with C1 (`research/checks/c1_ascertainment_sim.py`, planned). · Result: not run · Review: pending

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is non-sequitur / unverifiable. N3 on his own basis: 630 is for 1.5e8 genome-wide sites, 21 is among 1,233,013 panel SNPs; scaling by his own panel size gives 5.2, which flips the comparison (>25%): not an arithmetic-error but a conclusion that does not follow. Abstract's 99.8% in one window vs 53.6% (it is 99.86% over three bins: charity) -> ledger. 1.5e8 sites uncited (F) Charitable reading tried: tried 99.8% as the pre-7,000 BP share over three bins: 99.86% reproduces (abstract slip -> ledger); the 630 vs 21 denominator has no charitable reading.

R4 RG-01 retrieval (docs/research/sources/holocene-ne.md, 2026-10-09): under the flatter published trajectories (Gazave, Coventry, Gravel, temporal F) C1c's model gives about 900-3,900 neutral events against Day's 21; under a Nelson-type trajectory about 32-35. The literature does not decide between them; C1e (the C1c model on each published trajectory) is queued. C6's external verdict (contradicted as stated, on C1d) does not depend on this.

R4 C1e (research/checks/results/R4-C1e.md; review #18, 2026-10-09): model-side, three of four published Holocene N_e fits (Gravel, Gazave, Coventry) leave 21 a 25-161x deficit versus the neutral expectation (25 y generation clock matched, post hoc rerun; the first 20 y run gave 35-246x); the Nelson 2012 trajectory (1.7%/gen) reaches S21 = 31 (R0) / 50 (R2), 1.5-2.4x of 21, but its tracked total (1.1k) is 7% of Day's 16.3k. External stays contradicted (as stated, on the real AADR genotypes, C1d); C1c's reading that 21 is neutral-compatible needs a Nelson-type growth.

## Simulator variables implied
Number of neutral sites, panel fraction, window length, sample-size per bin, definition of fixation (sample versus population).
