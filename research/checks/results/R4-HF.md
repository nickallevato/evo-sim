# R4 HF: H follow-ups (soft-selection rate limit, truncation and synergistic epistasis, T50/lam50 intervals, GAP-05)

**Status: run in parts, written up in parts; awaiting reviews.** Load-bearing tier: three reviews (correctness, steelman-day, steelman-critic). Not integrated. Parts HF-a and HF-b (`main`) and HF-c (`ci`) are filled in when collected (see QUEUE item 8 for the collect steps); HF-d (GAP-05) is complete.

## Files
- Script `research/checks/hf_followups.py`, pre-registered at **8bd9d29** (the docstring holds the predictions). The smoke run (6 tiny cells) was used for plumbing only.
- Runs on na-workhorse:
  - `main`: 1,720 jobs, 10 workers, launched 2026-10-10 18:51 -06:00. Host record `raw/hf_main.host`.
  - `gap05` then `ci`: 1 process, launched 18:53. Host record `raw/hf_gap05_ci.host`.
- Raw: `raw/hf_main.jsonl`/`.out`, `raw/hf_ci.jsonl`/`.out`, `raw/hf_gap05.out`/`.json`.
- Engine: H8's `run()` generalised (modes `mix` with hardness h, `trunc`, synergistic term b). The `mix h = 1` cells validate it against H8 (PA3).
- DFE: there is no sourced human beneficial DFE (refresh-2026-10-10b s3). HF keeps s = 0.01 per copy (2Ns = 20, "strong") and adds a weak s = 0.002 bracket, following Uricchio 2019's weak/strong split (abstract: "72% of which is contributed by weakly adaptive variants"). This is a bracket, not a DFE.

## HF-d: GAP-05, slightly deleterious fixations on the human lineage (complete)
**Targets (verbatim; RH tag dialectic unless stated).**
- Day, "The Drift Deathmarch" (blog 2026-01-11): "At observed mutation rates and population sizes, the drift model fixes roughly 7.6 harmful mutations per actual generation. Using standard estimates for the damage caused by each mutation, collapse occurs in 9 generations—about 225 years." The same post's "The Drift Deathmarch closes it with a corpse" is rhetoric (device: vivid image; dialectical core = the 9-generation arithmetic) and is not scored.
- Hössjer, HO-11, p.6: "so that the overall fitness of the population declines over time and the population eventually (and quite rapidly) dies."

**Method.** Kimura flux of new deleterious mutations, integrated over Boyko 2008's gamma DFE:
- DFE: shape 0.184 (Kim 2017 quoting Boyko), mean |s| 0.029 (Boyko: "−0.029 for the gamma"), heterozygote effect s, homozygote 2s (Boyko's convention).
- U_d (new deleterious mutations per haploid genome per generation) ∈ {0.3, 1, 3}. U_d = 3 is GAP-05's upper end: 8% constrained × 3.1e9 × 1.2e-8, with Boyko's nonsynonymous DFE applied to all constrained sites (an extrapolation).
- Ne ∈ {1e4, 2e4}; T = 252,000 generations.
- Exact back mutation only, at mu/3.
- Scenarios:
  - S1: start at the optimum.
  - S2: start at the mutation-selection-drift equilibrium at the same Ne.
  - S3: equilibrium at Ne_anc = 2.06e5 (Yoo HCB, rescaled per GAP-06), then Ne for T.
  - S0: Day's selection-off hypothesis.

Sanity check: the fitted gamma puts **28.0%** of mutations at |s| < 1e-4, which matches Boyko's verbatim "tightly clustered around 28%".

**Results (primary row: shape 0.184, Ne = 1e4).**
| U_d | S1 substitutions per lineage | S1 log-fitness decline (sum 2s) over 252,000 gens | S1 per generation | S2 net | S3 net decline |
|---|---|---|---|---|---|
| 0.3 | 16,800 | 0.25 | 0.067 | ~0 (< 1e-18) | 0.24 |
| 1 | 55,900 | 0.82 | 0.22 | ~0 | 0.80 |
| 3 | 168,000 | **2.47** | 0.67 | ~0 | **2.39** |

- Sensitivity: Ne = 2e4 roughly halves the decline (U_d = 3: 1.09 S1, 1.01 S3). Shape 0.1 gives 2.54 / 2.44; shape 0.3 gives 1.77 / 1.73 (U_d = 3, Ne = 1e4). Everything scales linearly in U_d.
- S0 (selection off): harmful substitutions per generation = 0.75 × U_total = 28.8 at U_total = 38.4 (parameters.yaml). Day's 7.6 implies U_total = 10.1. With selection on (S1), the rate is 0.67 per generation at U_d = 3, i.e. **43x lower than S0** (11x lower than Day's 7.6). The per-generation log-fitness decline under S1 is about 1e-5, not the order-0.1-per-generation decline needed for collapse in 9 generations.
- Validation (per-site WF, N = 1000, 400,000 new mutations per 2Ns): **6 of 7 points pass** the pre-registered 99% band. 2Ns = -0.5 fails: simulated 2.08e-4 against Kimura 2.91e-4 (z = -3.10). The neutral point is low too (4.10e-4 against 5.00e-4, z = -2.55, inside the band). Two low z-values are more than chance would usually give; a possible estimator issue is open (reviewer item; a larger post hoc validation is proposed, not run).

**Scoring.**
| ID | Prediction | Result | Score |
|---|---|---|---|
| Day/ally side | S1 decline over 252,000 gens > ln 3 = 1.1 (more than Day's upper R absorbs) | 2.47 at U_d = 3; 0.82 at U_d = 1; 1.09 at U_d = 3, Ne = 2e4 | **Holds only at the GAP-05 upper-end U_d = 3 with Ne = 1e4**; fails at U_d <= 1 or Ne = 2e4 |
| Critic side | S2 net ~ 0; S0 vs S1 > 10x | S2 < 1e-18; S0/S1 = 43x (11x against Day's 7.6) | **Holds** |
| PD1 | S1 substitutions 3e4-3e5; decline 0.3-5 (U_d = 3) | 1.68e5; 2.47 | **Holds** |
| PD2 | S2 abs net < 0.01 | ~0 | **Holds** |
| PD3 | S3 net decline 0.1-2 | 2.39 (U_d = 3, Ne = 1e4); 0.80 (U_d = 1) | **Fails at the primary row** (above the band) |
| PD4 | S1 rate <= 1/10 of S0 at U_d = 3 | 0.67 vs 28.8 (1/43) | **Holds** |
| PD5 | validation passes at every 2Ns | 6/7 | **Fails at one point** (2Ns = -0.5) |

**Interpretation (conditional on the DFE extrapolation and on exact back mutation as the only return route).**
- **Day's 9-generation collapse needs selection switched off for every harmful mutation.** With Kimura fixation over Boyko's DFE, the harmful substitution rate is 43x lower than the selection-off rate. The per-generation decline is about 1e-5 in log fitness, so nothing collapses in 9 generations, or in 225 years. Day's statement scores against its own hypothesis (drift with selection "switched off by hypothesis"). That is a premise no critic holds: the neutral theory he is answering keeps purifying selection on constrained sites (Kimura's nearly neutral theory; Charlesworth 2013).
- **But the slow decline is real in this model and is not small over 252,000 generations.** Starting from an optimum, or from equilibrium at the larger ancestral Ne (S3, the standard demographic picture of an Ne decline), the cumulative log-fitness decline is about 0.8-2.5 (U_d 1-3), i.e. absolute fitness falls 2.2- to 12-fold. That is the GAP-05 "upper-end scenario", now computed. It supports the premise of Hössjer's HO-11 (fitness declines over time) at the upper end of U_d. It does not support "quite rapidly dies": the rate is about 1e-5 per generation, and it is open to compensation that this model omits.
- **The critics' standard resolution holds only at equilibrium.** At the mutation-selection-drift equilibrium for the current Ne, the net decline is zero (S2). S3 shows that an Ne decline from about 2e5 to 1e4 puts the population out of equilibrium for far longer than 252,000 generations (per-site relaxation ~1/mu), so S2's zero needs a reason the population was already at its current-Ne equilibrium. The model also omits compensatory mutations at other sites, beneficial substitutions (A2e-alpha: 1,000-3,600 coding adaptive substitutions per lineage on the critic-side estimates), soft selection (Charlesworth 2013), and epistasis. Each of these would offset some of the decline; none is quantified here.

## HF-a: soft-selection rate limit (pending collection)
(Filled from `hf_analyse.out`: lam50 / lam_max per R for softJ, trunc, softWF, mix h = 0.1 / 0.3; validation h = 1 vs H8; K = 4000; weak s.)

## HF-b: truncation and synergistic epistasis vs Term 3 (pending collection)

## HF-c: intervals on H-C2 T50 and H8 lam50 (complete)
**Method:**
- The 96 H-C2 conditions were rerun with their original seeds (`ci` stage, 1 worker, 2,013 s).
- At each grid point, p_T was drawn from Beta(k + 0.5, n - k + 0.5) (Jeffreys) and T50 was recomputed with the original first-crossing rule (10,000 draws). The 95% interval is the 2.5 and 97.5 percentiles.
- The same was done for H8 lam50 per R. For the D = 30 interval, D_obs was also bootstrapped over persisting reps.
- Raw: `raw/hf_ci.out`.

**Results.**
- **PC1 (reproduction): all 96 rerun T50 values equal the published values exactly** (60/60 treadmill, 36/36 Gaussian; matched against `raw/h_cost_of_selection.out`, `h_nunney_gauss.out`, `h_nunney_gauss_lowR.out`). **Holds.**
- **PC2:** The median 95% interval is -13% / +13% around T50. The range is -55% to +97%, widest at grid edges and low M. **Soft T50 > hard T50 with non-overlapping intervals in 43 of 47 matched pairs.**
  - The pre-registered width (+-20-40%) is **partly missed**: intervals are usually narrower, a few are wider.
  - "Non-overlapping in at least half" **holds**.
  - H-C2's "soft selection did not remove or reduce the cost (soft T50 > hard T50 throughout)" therefore stands at 95% in 43/47 pairs. The four overlapping pairs are the R = 10, M = 10 Gaussian pair (6.0 vs 6.5, grid floor), R-scan s = .03 at R = 3 and 5 (marginal), and one Gaussian low-M pair.
- **PC3 (H8, the 1/300 question), R = 1.111, interval at D = 30, 10k window:**

| K | point | 95% interval |
|---|---|---|
| 1,000 | 484 | **419-568** |
| 500 | 561 | 396-990 |
| 4,000 | 439 | 389-851 |
| 16,000 | 546 | **342-720** |
| 64,000 | 348 | **326-768** |

  - 20k window: K = 1,000 509 (440-763); K = 16,000 631 (535-762); K = 64,000 490 (406-809).
  - Every 95% interval lies wholly above 300. The prediction "lower end in [300, 420]" holds at K = 1,000 (419) and at K = 16,000 / 64,000 (342 / 326). Of the two sides: **"Day side: wholly >= 300" holds at every K tested**, and **"Critic side: reaches <= 300" fails** at every K.
  - For R4-H8's rule K2/K2' (<= 300 remove, >= 480 keep, between = conditional on K): the K = 64,000 interval (326-768) excludes the remove zone at 95% but straddles 480. So "slower than 1/300" stays **conditional on K**, but "about equal to or faster than 1/300 at D = 30" is now excluded at 95% at every K tested (Day's verbatim upper bound is conservative there).
  - R = 2: 52 (50-69) at K = 1,000 and 53 (50-61) at K = 64,000: about 4.3-6x Haldane's rate at every K.
- **Caveat:** the Beta draws treat grid points as independent and ignore the fact that the grid was stopped early (H-C2 stops after two >= 87.5% points). A wider grid could add crossings that are currently censored (censored share <= 2% everywhere).

## Who this helps (GAP-05 part; the rest follows the runs)
- **Day side:** The slow decline is real in a standard Kimura-flux model. At the upper-end deleterious input with an Ne decline it is 2.4 log units over 252,000 generations, which is more than R = 3 could absorb if nothing offsets it. No critic has answered this with numbers (GAP-05 S21), and the "equilibrium" answer needs the population to have been at its current-Ne equilibrium.
- **Critic side:** Day's "collapse in 9 generations" comes only from switching selection off for harmful mutations. With selection on, the harmful substitution rate is 43x lower and the decline is about 1e-5 per generation. Compensatory and beneficial substitutions, soft selection and epistasis are all omitted here, and each would lower the net decline.
- **Both:** GAP-05 turns on the initial condition and on U_d (0.3-3 moves the decline 10-fold), not on the arithmetic.
