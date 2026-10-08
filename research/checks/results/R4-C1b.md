# R4 C1b: Day's actual time-binned statistic (Z18525185: 22,428 "fixations", 21 after 7000 BP)

Script: `research/checks/c1b_day_binned_statistic.py` (run `research/.venv/bin/python -I ... 20`; 20 reps x 13 configs x 16 readings; 1291 s, 3 workers; seeds SeedSequence([20261010, config, rep])). Not committed. Pre-registered predictions are in the docstring and were written before the run (only an output-discarded timing test preceded it).

## Procedure as simulated (quotes in docstring, Z18525185 s3.2-s3.4, s4.1, s4.4)
Unscaled neutral Wright-Fisher, 2Ne chromosomes, constant Ne in {7e3, 1e4, 2e4}; panel = present-day-ascertained (start-of-window minority-frequency density 1.86 per unit q from the earlier D2 chain, flat to 18% down to q=1e-3; 1.14M panel sites; q<=10% simulated); 11 bins with Day's n and midpoint dates (10000+ at 10,500 BP, assumed); per-bin genotyped ~Bin(n, cov), chromosomes = k x genotyped; fixed bin = sample 100%. Readings: eligibility E1 (modern 100% and pooled 6000-8000 BP <100%, s3.3) or E2 (modern 100% and some older bin <100%); dating T1 (start of unbroken 100% run to present) or T2 (oldest bin ever 100%, gaps allowed: "oldest time bin in which the allele appeared fixed"); k = 1 or 2; cov = 1.0 or 0.3. Generation 20 y (Appendix A, 350 gens) with a 25 y sensitivity. "Day" model = same process with drift clock x 0.45 (158 effective generations). Admixture: one pulse (m = 0.1 or 0.3 at 7,500 or 5,500 BP) from an independently drifted source (scenario only).

## Results (E2-T2 and E1-T2 give identical post-7000 counts; S21 = 0-6000 BP, S23 = 6000 BP and younger; observed 21 and 23)
| Config | S21, k1 cov1 | S21, k2 cov0.3 | eligible (obs 22,428) |
|---|---|---|---|
| neutral Ne=7000 | 17,198 [16.9k,17.5k] | 14,254 | 35,357 |
| neutral Ne=10000 | 10,959 [10.8k,11.1k] | 8,855 | 25,200 |
| neutral Ne=20000 | 4,222 | 3,397 | 13,338 |
| Day d=.45 Ne=7000 / 1e4 / 2e4 | 6,023 / 3,630 / 1,414 | 4,820 / 2,942 / 1,250 | 16,743 / 12,206 / 7,283 |
| neutral Ne=1e4, 25 y/gen | 8,099 | 6,520 | 20,371 |
| admixture pulses (4 scenarios, Ne=1e4) | 9,556-10,831 | 7,756-8,785 | 22.5-24.5k |
Every cell: 0 of 20 reps (and Poisson P < 1e-300) at or below 21 or 23. The 16 readings give S21 from 1,250 (Day, Ne=2e4) to 20,142 (neutral Ne=7e3); none is near 21. K=5% truncation changes S by ~7%.

Bin profile (E2-T2-k1-cov1, neutral Ne=1e4): 3,907 / 7,409 / 1,347 / then ~1,200-1,900 in each younger bin including 1,878 in 0-500 BP. Observed: 3,038 / 8,741 / 4,497 / 2 / 9 / 7 / 2 / 1 / 0 / 0 / 2. The model reproduces the two oldest bins (and total eligible 13-35k vs 22,428) but not the 7000-8000 bin and, decisively, not the 99.86% pre-7000 share (model 38-60% pre-7000 at best). T1 dating puts 2,000-3,000 events in 0-500 BP (obs 2) and has no pre-7000 events at all under E1.

## Power and identifiability
- Within a model the statistic is precise (sd ~1-2%): AUC neutral(1e4) vs Day(1e4) = 1.00. But the model-dependence is far larger: Day(d=.45) at Ne=1e4 (3,630) lies between neutral Ne=1e4 (10,959) and 2e4 (4,222); d is not separable from Ne (time-rescaling), as pre-registered (P5).
- Against the observed 21-23, discrimination is nil in the sense that matters: BOTH neutral (any Ne 7e3-2e4) and Day's d=0.45 model predict 1.2e3-1.7e4, i.e. 60-800x the observed value. Within this model the statistic as literally defined does not favour Day's model over neutral; since the model also misses Day's own bin profile, this says the 21 is not reproducible, not that either model is rejected.
- Admixture (m up to 0.3) changes S by <15%; it cannot produce 21.

## Adjudication of the C1/C6 dispute
- Critic ("observed 1 and 3 exceed neutral, P~2e-4"): concerns Z23046531's 50-90% statistic, not this one; not tested here. 
- Day-side ("neutral also predicts ~0, no power"): not supported within this model, where the literal procedure gives thousands, not ~0; but see the next bullet (the model is not a valid null for the published table).
- Correctness review ("does not rescue Day" unsupported): confirmed unsupported as phrased. The model also fails to reproduce Day's own table (7000-8000 BP bin ~1,350 vs 4,497 observed; 38-60% pre-7000 vs 99.86% observed), so it is not a valid null for his statistic, and no deficit or excess relative to neutral can be inferred from it (review REVIEW-R4-new, MAJOR). Verdict: **not reproducible from the published procedure; cannot adjudicate.**
- What this does and does not show: pre-registered P1 (T1 inconsistent with profile) and P3 (observed in the lower tail, P<0.01) hold. P2's magnitude was WRONG (predicted central ~500, range 30-3,000; found ~1e4): the prediction underestimated drift completions of near-fixed alleles. P4 (S rises with Ne) is WRONG: S falls with Ne (17.2k, 11.0k, 4.2k). P5 holds; P6 holds.
- Therefore the 21 cannot be read as an empirical rate measurement for either side: the published number is not reproducible from the published procedure. Candidate unmodelled causes (not tested): the 27% "insufficient coverage" drop with an unstated threshold, a differently implemented fixation/dating rule (e.g. requiring polymorphism in the oldest-dated bin, or population-level pooling of bins), different eligible sets, or an implementation error. The paper's own pre-7000 counts (16,276) likewise fail to match the 7000-8000 bin (4,497 vs ~1,350).

## Likely cause of the mismatch: per-site call depth (hypothesis, not tested at scale)
The script genotypes a fraction 1.0 or 0.3 of each bin (>= 39 chromosomes even in the 129-individual bin). Real 1240k pseudo-haploid data in old bins give only a handful of calls per site, so "100%" is trivially met there, and T2 ("oldest bin in which the allele appeared fixed") then piles events into old bins. "Tracked" also requires data in every bin (the 27% drop). Reviewer's cheap test (neutral Ne=1e4, k=1, E2-T2, **1 replicate; direction only**, scratchpad script, not committed): S21 = 6,537 / 4,180 / 1,583 / 1,204 at per-site coverage 0.3 / 0.1 / 0.03 / 0.01, and 121 at coverage 0.01 when data in all bins is required; the profile shifts toward the 10000+ bin (63,750). The direction moves S21 and the profile toward Day's table, but eligible rises to 72-138k against 22,428, so this is not a reproduction. Ancestry structure (the 10000+ bin is Mesolithic; Day's own s5.2 invokes replacement) is the second unmodelled factor. Neither is a code bug. Follow-up queued: a per-site, per-bin call-depth model with real AADR bin coverage plus a replacement model.

## Caveats
Single closed panmictic population, constant Ne, unlinked sites, no genotype error, no population structure/replacement (Anatolian/steppe turnover modelled only as one-pulse scenarios); panel start density borrowed from the scaled chain (Ne=1e4) for all Ne and flat below q=1e-3 by assumption; the 10000+ bin date is assumed; missingness model crude; the 27% untracked drop not modelled; q>10% starts omitted (<1%); scenario admixture is not data. Replicate count 20 limits tail estimates but the gap is orders of magnitude.

## Suggested verdict edits (for the claim files)
- C6 external: the "630 vs 21" comparison is invalid (denominator). The 21 is not reproducible from the stated method in this model (which also misses Day's own bin profile); neither "neutral predicts ~0" nor "does not rescue Day" nor "deficit vs neutral" is supportable. Mark: not reproducible; cannot adjudicate (`untestable` pending the call-depth follow-up).
- C1/C: unchanged for Z23046531's two-period statistic; separate this from the Z18525185 statistic.

## Review corrections applied (REVIEW-R4-new)
1. MAJOR: "massive deficit vs neutral" and "sign of the claim stands" removed; verdict is "not reproducible; cannot adjudicate".
2. Per-site call-depth hypothesis added with the reviewer's 1-replicate numbers, labelled direction only.
3. Code checks (bin order, T1/T2, S21/S23 indices, single T per site): no bug found.
