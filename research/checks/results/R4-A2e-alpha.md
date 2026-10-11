# R4 A2e-alpha: published human adaptive-substitution estimates against the A2e flip (~191 per lineage)

**Status: run, written up; awaiting reviews.** Load-bearing tier: three reviews (correctness, steelman-day, steelman-critic). Not integrated.

## Files
- Script `research/checks/a2e_alpha_map.py`, pre-registered at **49824e0** (docstring = predictions); run locally once after the commit (arithmetic and quote verification only, < 1 s). Nothing post hoc.
- Raw output `research/checks/results/raw/a2e_alpha.out`. Sources: `docs/research/sources/refresh-2026-10-10b.md` s1; local texts under `sources/raw/refresh-2026-10-10b/` (gitignored), sha256 printed in the raw output. All 13 quotes verified as substrings of the local raw text.
- Target: A2e (`docs/research/claims/A2e-ltee-as-ceiling.md`), the per-generation adaptive-only flip from R4-A2e Flag 1 / PH8. RH tag: the scored statement ("The objection implicitly claims that humans can fix mutations faster per generation than bacteria under ideal conditions", Z23003785 s8.6 p.15; "unattainable ceiling, the absolute best-case scenario") is dialectic. Nothing rhetorical is scored here.

## What was done
R4-A2e found that, per generation and adaptive-only, A2e is equivalent to "the human lineage fixed at most about 191 adaptive substitutions since the CHLCA" (252,000 / 1,322). The refresh fetched the published alpha (adaptive fraction) estimates. This check multiplies each alpha by a nonsynonymous-substitution count for the human lineage and reads off which side of the threshold it lands on. Two thresholds: **G1** = 252,000 / 1,322 = **190.6** (Day's MITTENS 3.0) and **G2** = 252,000 / 1,587 = **158.8** (2nd edition). Day's adaptive-only reading (1,408 → 179.0) and Yoo's generation count (257,143 → 194.5) are printed as well.

Denominators (all are counts over a gene set, so lower bounds on the whole-exome count):
- N1, Gayà-Vidal human branch: 2 × 9,785 = 19,570. The "2" is rounded in the text, so 14,678-24,463 is also shown.
- N2, Boyko 22,180 / 2 = 11,090 per lineage. This assumes an even split between the lineages.
- N3, N2 / 0.61 = 18,180. This scales to all autosomal RefSeq gene bases (derived).

## Results
| estimate (access) | adaptive substitutions per lineage | × G1 threshold | side (G1 and G2) |
|---|---|---|---|
| Gayà-Vidal 2014, alpha ≈ 0.2% on the human branch (full text) | 29-49 | 0.15-0.26 | **Day (A2e holds)** |
| Boyko 2008, 10-20% of human-chimp differences (full text) | 1,109-3,636 | 5.8-19.1 | **critic (A2e flips)** |
| Boyko 2008, 9.3% gamma-model deficit, the lower end (full text) | 1,031-1,691 | 5.4-8.9 | critic |
| Uricchio 2019, alpha = 0.135 (**abstract only**) | 1,497-3,303 | 7.9-17.3 | critic |
| Uricchio, strongly adaptive share only, 0.135 × 0.28 (abstract only; derived) | 419-925 | 2.2-4.9 | critic |
| Eyre-Walker & Keightley 2009, "little evidence" read as 0-5% (**abstract only**; the 0-5% reading is the audit's) | 0-1,223 | 0-6.4 | straddles |
| Eyre-Walker & Keightley 2009, "as high as 40%" (abstract only; a conditional upper bound) | 4,436-9,785 | 23-51 | critic |
| Gayà-Vidal, "at least 40%" in accelerated genes | not mapped (that gene set's Dn was not extracted) | n/a | n/a |

alpha\* (the alpha at which the count equals the threshold) is **0.65%-1.75%** across denominators and bases (G1: 0.78-1.75%; G2: 0.65-1.43%).

## Scoring of the pre-registered predictions
| ID | Prediction | Result | Score |
|---|---|---|---|
| Day side | the best human estimates put the lineage at or below ~191 | Gayà-Vidal: 29-49. EK "little evidence" straddles the threshold. Galtier, "with the notable exception of primates", gives no count | **Holds for Gayà-Vidal only** |
| Critic side | Boyko and Uricchio give ≥ 1,000, i.e. > 5x the threshold, on every denominator and on both bases | Boyko 1,031-3,636 (5.4-19x); Uricchio 1,497-3,303 (7.9-17x) | **Holds** (Uricchio is abstract only) |
| Q1 | alpha\* between 0.8% and 1.8% | 0.65-1.75% | **Partly fails**: below 0.8% for N1-high and for N1/N3 on G2 |
| Q2 | GV 20-60; BO 10-20% → 1,100-3,700; UR → 1,500-2,700 | GV 29-49 (hit). BO 1,109-3,636 (hit). UR 1,497-3,303 (miss at both ends: 1,497 marginally low, 3,303 high; the range was set without the N1-high denominator) | **GV and BO hit; UR misses** |
| Q3 | estimates on **both sides by more than 10x each way**, so external stays contested with a named disagreement | Both sides: yes. By > 10x each way: **no**. The Day-side estimate is 4-7x below the threshold; the critic-side estimates are 5-19x above | **Qualitative part holds; the "> 10x each way" part fails** |

## Interpretation
- **The threshold sits inside the published range.** One full-text estimate (Gayà-Vidal) is on Day's side by 4-7x. Two (Boyko, full text; Uricchio, abstract) are on the critics' side by 5-19x. The flip is not a matter of denominators: alpha\* is about 1% on every reading, and the estimates sit at 0.2% versus 9-20%.
- **The two sides of the disagreement are not symmetric** (stated in advance). Coding-only counts are lower bounds on all adaptive substitutions, because regulatory and non-coding adaptation is not counted in any comparable human-lineage form (refresh s1). So a coding count above the threshold is enough for the flip if it is correct. A coding count below the threshold is not enough for Day: it would also need non-coding adaptive substitutions to number at most ~150.
- **Why the estimates differ.**
  - Gayà-Vidal's 0.2% uses SNPs at DAF ≥ 60% on the human branch. The authors say estimates in their DAF classes are affected by slightly deleterious polymorphism.
  - Boyko's 10-20% comes from a model-fit deficit (observed 22,180 versus 20,113 expected under the gamma DFE) and depends on how the beneficial DFE is modelled.
  - Eyre-Walker and Keightley's 40% is conditional on a decline in Ne.
  - This check does not decide between them. They are different estimators applied to different data.
- **Verdict relevance (proposed, for reviewers):** A2e external stays **contested**. The open item "literature not fetched" (R4-A2e, follow-up 1) becomes "the literature disagrees by about 100-fold (0.2% versus 9-20%), and the threshold (~1%) lies between the two". Rule R1: no verdict moves.

## Who this helps
- **Day side:**
  - The one full-text estimate made on the human branch itself puts adaptive substitutions at about 30-50, well under 191.
  - Galtier ("notable exception of primates") and Eyre-Walker & Keightley ("little evidence" against macaque) point the same way.
  - The critic-side numbers rest on one full-text model fit (Boyko) and one abstract (Uricchio). The beneficial DFE is not inferred in either (refresh s3).
- **Critic side:**
  - Two independent methods put coding-only adaptive substitutions at 1,000-3,600 per lineage, 5-19x above the flip.
  - These are lower bounds: non-coding adaptation and the genes outside the sampled sets are not counted.
  - Even the strongly adaptive share alone (28% of Uricchio's alpha) exceeds 191 on every denominator.
- **Both:** The A2e question is now empirical and narrow. Is the human-lineage alpha nearer 0.2% or 10%? The threshold is about 1%, so each side needs the other's estimate to be wrong by about 5-fold or more.

## Caveats for the reviewers
- Two of the four quantitative sources are abstract only (Uricchio, Eyre-Walker & Keightley), and EK's "little evidence" was turned into 0-5% by the audit.
- The even split of Boyko's 22,180 between the lineages is an assumption. The 0.61 scale-up assumes uniform density across genes.
- alpha is the share of nonsynonymous substitutions fixed by positive selection. That includes weakly beneficial changes (72% of Uricchio's alpha). Day's 1,322-generation ceiling is a count of beneficial fixations of any effect size, so the two definitions match only roughly.
- Gayà-Vidal's "at least 40%" in accelerated genes is not mapped. Its Dn could on its own put a lower bound above 191; this was not checked.
