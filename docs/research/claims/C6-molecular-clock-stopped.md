---
id: C6
title: "Ancient DNA falsifies the constant-rate clock: 99.8% of fixation events fall before 7,000 BP; the clock predicts ~630 fixations in 350 generations and 21 are seen"
side: day
branch: C
parent: C
edges: [{type: supports, target: C}, {type: supports, target: B4}]
load_bearing: false  # Earlier (Feb 2026) aDNA paper whose counts differ from the later Z23046531; used to support recalibration (B4). ROOT does not depend on it.
sourcing: firsthand
status: extracted
verdicts:
  internal: arithmetic-error
  fidelity: n/a
  external: pending
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
Script: shared with C1 (`research/checks/c1_ascertainment_sim.py`, planned). · Result: not run · Review: pending

## Simulator variables implied
Number of neutral sites, panel fraction, window length, sample-size per bin, definition of fixation (sample versus population).
