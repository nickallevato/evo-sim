# R4 HF: H follow-ups (soft-selection rate limit, truncation and synergistic epistasis, T50/lam50 intervals, GAP-05)

**Status: all four parts run and written up; awaiting three reviews (Opus): correctness, steelman-day, steelman-critic.** Load-bearing tier (HF moves the H ROOT-path node). Not integrated.

## Files
- Script `research/checks/hf_followups.py`, pre-registered at **8bd9d29** (the docstring holds the predictions). The smoke run (6 tiny cells) was used for plumbing only.
- Runs on na-workhorse:
  - `main`: 1,720 jobs, 10 workers, launched 2026-10-10 18:51 -06:00, dearest-first. Host record `raw/hf_main.host`. **Post hoc (orchestration only), disclosed:** on 2026-10-11 the remaining jobs were split with a second host, builder (Ryzen 7 3700X, 7 workers, `HF_REVERSE=1` cheapest-first, commit 7632b57; `HF_ROTATE` from da6f8ac was added for a possible third host and not used for any row here). Builder started from a 316-row copy of workhorse's file and passed a 5/5 pre-launch reproduction check. Both hosts were killed once the union covered all 1,720 jobs, so some jobs ran on both and 8 ran on workhorse only. Host record `raw/hf_main_builder.host`. Seeds are per (cell, rep), so neither the split nor the job order can change any row.
  - **Cross-host reproducibility check (post hoc):** `research/checks/hf_merge_hosts.py` merged the two files on (cell, rep). **696 jobs ran independently on both hosts; all 696 agree on every field except `sec` (0 mismatches).** The 316 seed-copy rows are byte-identical (they are copies, not a test). Union: **1,720 unique jobs** (316 seed + 696 both + 8 workhorse-only + 700 builder-only).
  - `gap05` then `ci`: 1 process, launched 18:53. Host record `raw/hf_gap05_ci.host`.
- Raw: `raw/hf_main.jsonl` (merged), `raw/hf_main_workhorse.jsonl`/`.out`, `raw/hf_main_builder.jsonl`/`.out`, `raw/hf_analyse.out` (the `analyse main` tables, run on na-workhorse), `raw/hf_ci.jsonl`/`.out`, `raw/hf_gap05.out`/`.json`.
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

## HF-a: soft-selection rate limit (complete)
**Targets:** H (Day, Z18168236 Abstract) "one beneficial substitution per 300 generations"; H8 (Day, Z19984826 s3.3.1) "None of them raises smax above order unity, and the reason is the same in all three cases." (RH tag: dialectic.) Critic-side mechanism: Wallace's soft selection, Nunney, Maynard Smith truncation. Raw: `raw/hf_analyse.out` (1,720 rows). K = 1000 and s = 0.01 unless stated. Hard caps (H8 lam50, 10k): 0.00368 / 0.0363 / 0.0606 at R = 1.111 / 2 / 3.

**Results on the pre-registered success rule** (lam_max = largest lam with >= 50% success at 20k; "1.6+" = success at the top of the grid, censored).

| Mode | R = 1.05 | R = 1.111 | R = 1.5 | R = 2 | R = 3 |
|---|---|---|---|---|---|
| softJ (h = 0) lam_max | none (< 0.0351) | 0.8 | 1.6+ | 1.6+ | 1.6+ |
| trunc lam_max | 0.8 | 1.6+ | 1.6+ | 1.6+ | 1.6+ |
| softWF (R-free) lam_max | | 1.6+ (all R) | | | |
| mix h = 0.1 lam50 10k (x hard cap) | | 0.0064 (1.7x) | | 0.141 (3.9x) | 0.283 (4.7x) |
| mix h = 0.3 lam50 10k (x hard cap) | | 0.0037 (1.0x) | | no crossing; lam_max 0.0351 (1.0x) | 0.0705 (1.2x) |
| mix h = 1 (validation) lam50 10k | | 0.00368 (H8 0.00368) | | 0.0360 (H8 0.0363) | |
| K = 4000 softJ / trunc lam_max | | 0.4 / 1.6+ | | 1.6+ / 1.6+ | |
| weak s = 0.002 softJ / trunc lam_max | | none / 0.4+ | | none / 0.4+ | |
| weak s = 0.002 hard lam50 (10k and 20k) | | > 0.0077 (no crossing) | | > 0.050 (no crossing) | |

**What the failures are (post hoc descriptive reading of the same rows; changes no pre-registered score).**
- *Extinction only, mix cells.* At low lam, mix cells hold few open loci (nopen ~5-60), and the steady-state rule (`nopen_q4/nopen_q1 <= 1.15`) fails on noise there: one h = 0.3, R = 2 rep has a ratio of 2.52 at nopen ~6. These runs are alive and keep pace (k/lam ~1). Reading extinction alone, the boundary lies between the last all-alive lam and the first all-extinct lam:
  - h = 0.1: R = 1.111 0.0111-0.0351 (3.0-9.5x the hard cap); R = 2 0.1-0.2 (2.8-5.5x); R = 3 0.2-0.4 (3.3-6.6x).
  - h = 0.3: R = 1.111 0.0037-0.0111 (1.0-3.0x); R = 2 0.0351-0.1 (1.0-2.8x); R = 3 about 0.1 (2/4 extinct; 1.7x).
  - The pre-registered mean-field rule (extinction when h lam D_soft > ln R, with D_soft from the softJ rows) predicts 0.0052 / 0.0157 at R = 1.111 and 0.096 / 0.29 at R = 2 (h = 0.3 / 0.1). That is inside the observed brackets at R = 1.111 and R = 2 (h = 0.3) and up to ~2x above them at R >= 2 for h = 0.1, and at R = 3.
- *softJ at R = 1.05, and weak-s softJ.* None of these runs went extinct or hit max_open below lam = 0.8. They fail the k/lam >= 0.9 rule with a ratio that is **flat in lam**: 0.79-0.84 at R = 1.05 for every lam from 0.0351 to 0.4; 0.46-0.55 for weak s at R = 1.111; 0.77-0.85 for weak s at R = 2. A real rate ceiling would make k/lam fall as lam rises. A flat ratio is what an unfilled sweep pipeline gives: the implied sweep time (nopen/k) is ~7,500 generations at R = 1.05 and ~19,000 for weak s at R = 1.111, both longer than the 5,000-generation burn-in (the R = 1.111 s = 0.01 cells, ~4,500 generations, pass). So these "failures" are probably a window artefact, not a limit. The rule is applied as pre-registered; a longer burn-in run would settle it (proposed, not run). The same caveat covers K = 4000 softJ at R = 1.111 (k/lam 0.87-0.95, borderline).
- *Weak-s hard at 40k (the recorded 40k checkpoint, not used by `analyse`).* At R = 1.111 all 6 reps survive at lam 0.0049 and 2/6 at 0.0061 and at 0.0077, so lam50(40k) is ~0.005-0.006 (1.4-1.7x the s = 0.01 cap). At R = 2, 5/6 survive at the top (0.050), so the result is still censored. D_obs, the cost per substitution, is ~15-17 at both s (Haldane's s-independence of the cost holds), but the sustainable load lam x D is ~1.5x higher at weak s.

**Scoring.**
| ID | Prediction | Result | Score |
|---|---|---|---|
| DA1 (Day) | mix h = 0.1 and 0.3 lam50 within 2x of the hard cap at R = 1.111 (<= 0.0074) and R = 2 (<= 0.073) | h = 0.3: 0.0037; R = 2 lam_max 0.0351 (extinction bracket 0.035-0.1). h = 0.1: 0.0064 at R = 1.111 (extinction-only 0.011-0.035); **0.141 at R = 2** | **Fails** (h = 0.1 at R = 2 is 3.9x the cap). Holds for h = 0.3. |
| DA2 (Day) | K = 4000 lam_max <= K = 1000 lam_max | softJ 0.4 vs 0.8 (R = 1.111); 1.6+ vs 1.6+ elsewhere | **Holds, but uninformative**: 3 of 4 pairs are censored at the grid top, and the K = 4000 grid has no 0.8 point |
| CA1 (critic) | softJ and trunc sustain >= 0.1 at every R >= 1.111 and >= 0.4 at R >= 2 | softJ >= 0.8, trunc >= 1.6 at every R >= 1.111 | **Holds** (240-480x Haldane's 1/300) |
| CA2 (critic) | mix h = 0.1 lam50 >= 3x the hard cap at R <= 2 | 1.7x (R = 1.111), 3.9x (R = 2); extinction-only 3.0-9.5x at R = 1.111 | **Fails on the pre-registered rule at R = 1.111**; holds at R = 2. Holds at both R on the extinction-only reading (post hoc). |
| PA1 | softJ lam_max: R = 1.05 0.1-0.4; R = 1.111 0.2-0.8; R >= 2 >= 0.4. trunc >= softJ. softWF <= 0.4, maxrel at limit < 2 | R = 1.05: none on the rule (pipeline caveat); 0.8; 1.6+. trunc >= softJ at every R. **softWF sustains 1.6+** (maxrel 1.74 at 1.6) | **Partly holds**: R = 1.111 and R >= 2 hold, trunc >= softJ holds; R = 1.05 fails; softWF fails (it is faster than predicted) |
| PA2 | h = 0.3 R = 1.111 [0.004, 0.012]; h = 0.1 R = 1.111 [0.008, 0.035]; R = 2: h = 0.3 [0.04, 0.12], h = 0.1 [0.07, 0.3] | 0.0037; 0.0064; no crossing (extinction 0.035-0.1); 0.141 | **1 of 4 holds** (h = 0.1, R = 2); 2 just below their bands; 1 unscorable on the rule. The extinction-only brackets overlap all four bands. |
| PA3 | mix h = 1 within 25% of H8 (0.00368, 0.0363) | 0.00368, 0.0360 (< 1%) | **Holds** (engine validated) |
| PA4 | K = 4000 within one lam step of K = 1000 | 0.4 vs 0.8; others censored equal | **Holds** (grid-limited) |
| PA5 | weak s: hard lam50 x D_obs within 25% of s = 0.01; softJ lam_max at R = 2 0.1-0.2 | hard: no crossing at 10k/20k (> 2.1x / > 1.4x cap); 40k read ~1.5x. softJ: fails at every lam (pipeline caveat) | **Fails** (weak-s hard sustains more than the s = 0.01 cap; D_obs itself is s-independent) |

**Interpretation.**
- **The hard cap is specific to hard selection, and it comes back quickly as hardness rises.** With purely relative (soft) selection or truncation, a K = 1000 population sustains 0.8-1.6+ substitutions per generation at every R >= 1.111, i.e. >= 217x the H8 hard cap and >= 240x Haldane's 1/300. The R-free Wright-Fisher version (softWF) does too. With 30% of the selection hard (h = 0.3), the limit is within 1.0-1.7x the hard cap on the pre-registered rule (<= 3x reading extinction only). With 10% hard (h = 0.1), it is 1.7-4.7x (2.8-9.5x reading extinction only). The mean-field rule h lam D_soft ~ ln R captures this within about 2x.
- So whether a Haldane-type limit binds depends on how hard human selection is. The hardness h is not sourced for humans; it is the new key unsourced parameter, next to R (V17).
- Day's s3.3.1 is literally true of s_max: truncation's s_max is R by construction, and soft selection's maxrel is 1.1-2.2 here. **As a rate claim it is false for soft selection and truncation.** It is close to true for selection that is >= ~30% hard.

## HF-b: truncation and synergistic epistasis vs Term 3 (complete)
**Targets:** H8 Term 3 (Day, Z19984826 s4.3, at simulation scale lam_T3(R) = ln R / (2 ln 2K) = 0.0069 / 0.0456 / 0.0723 at R = 1.111 / 2 / 3, K = 1000); H8 s3.3.1 (above); H7 (Keightley 2012, Abstract) "could be tolerated if selection acts on relative fitness differences between individuals or if there is synergistic epistasis." That quote is about deleterious load; HF applies the mechanism to adaptive cost, as pre-registered.

**Results.**
- **Truncation:** lam_max >= 1.6 at every R >= 1.111 (0.8 at R = 1.05), i.e. **>= 22x / 35x / 231x Term 3** at R = 3 / 2 / 1.111 (353x at R = 1.05). All except R = 1.05 are censored at the grid top. The cost per substitution D_obs (in w units) is 0.1-30 in sustained cells, against ~16 under hard selection.
- **Synergy** (hard, w = exp(-s A - b A^2), 10 reps per point): lam50 (10k) and the gain lam50(b)/lam50(0):

| b | R = 1.111 | R = 2 | R = 3 |
|---|---|---|---|
| 0 (fresh-seed H8 replicate) | 0.00350 | 0.0347 | 0.0705 |
| 2.5e-4 | 0.00424 (1.21; 20k 0.92) | 0.0355 (1.02) | 0.0611 (0.87) |
| 1e-3 | 0.00318 (0.91) | 0.0297 (0.86) | 0.0511 (0.72) |
| 4e-3 | 0.00184 (0.52; 20k < 0.0018) | 0.0209 (0.60) | 0.0383 (0.54) |

  - The b = 0 replicate matches H8 (0.00368 / 0.0363 / 0.0606) within 4-16%.
  - D_obs falls with b as predicted (~16 to ~10 at b = 4e-3), but the sustainable rate falls too. Extinctions over the whole synergy grid rise with b: 167, 175, 199, 231 of 270 runs.
  - The mean load at lam50 (lam x D) at R = 2 falls from ~0.54 (b = 0) to ~0.21 (b = 4e-3), both below ln 2 = 0.69. So the extra extinctions are not driven by the mean load. A fluctuation mechanism (the quadratic term amplifying upward swings in A) is a candidate; it is not tested here (reviewer item).

**Scoring.**
| ID | Prediction | Result | Score |
|---|---|---|---|
| DB1 (Day) | trunc lam_max and syn lam50 <= 1.25 x Term 3 (0.0087 / 0.057 / 0.090) | trunc >= 1.6 (>= 22-231x Term 3); syn <= 0.0042 / 0.0355 / 0.061 | **Fails for truncation; holds for synergy** |
| s3.3.1 verbatim | truncation s_max order unity | s_max = R <= 3 by construction | **Holds trivially** |
| CB1 (critic) | trunc >= 5x Term 3 at every R | >= 22x | **Holds** |
| CB2 (critic) | synergy raises lam50 >= 1.5x at b = 4e-3 | 0.52-0.60 (it lowers it) | **Fails** |
| PB1 | trunc lam_max >= 10x Term 3 at R = 1.111 (>= 0.1) | >= 1.6 | **Holds** |
| PB2 | gain in [1.0, 1.3] / [1.1, 1.6] / [1.2, 2.0] at b = 2.5e-4 / 1e-3 / 4e-3; never > 2.2; D_obs falls by the same factor | 0.87-1.21 / 0.72-0.91 / 0.52-0.60; max 1.21; D_obs falls but lam50 does not rise | **Fails** (only b = 2.5e-4 at R = 1.111 and 2 is in band; "never > 2.2" holds) |

**Interpretation.**
- **Truncation is a real reduction in the cost, and Term 3 is not a bound across mechanisms.** Day's "order unity" holds for s_max but does not cap the rate: with s_max = R <= 3, truncation sustains >= 22-353x Term 3. This is the pre-registered "PB1/CB1 holding" branch.
- **Quadratic synergy on the adaptive cost does not help.** In this model it lowers the hard-selection rate by up to ~2x. On this point Day's side holds: the critic-side synergy mechanism (H7, applied to adaptive cost) fails, and the pre-registered mean-field gain was wrong in sign.
- This says nothing about synergy on deleterious load, which is what Keightley's quote is about (H7 is not re-scored here).

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

## Who this helps
**HF-a / HF-b (soft limit, truncation, synergy)**
- **Day side:**
  - The hard cap reproduces exactly (PA3; the b = 0 replicates are within 4-16% of H8).
  - Modest hardness brings it back. With 30% of selection hard, the sustainable rate is within 1.0-1.7x the hard cap at R = 1.111-3 (DA1 holds at h = 0.3). If human selection is substantially hard, Haldane's limit (and Hössjer's H5 use of it) stands at the hard-cap level.
  - Quadratic synergistic epistasis, a critic-side escape (H7 mechanism), lowers the rate rather than raising it (CB2 fails, DB1 holds for synergy).
  - Day's s3.3.1 is literally true of s_max.
- **Critic side:**
  - Soft selection and truncation sustain >= 0.8-1.6 substitutions per generation at every R >= 1.111 (CA1, CB1, PB1 hold). That is >= 217x the hard cap and >= 22-353x Term 3, so Term 3 is not a bound across mechanisms, and s3.3.1 fails as a rate claim.
  - Even 10% hardness leaves 1.7-4.7x the hard cap on the pre-registered rule (2.8-9.5x reading extinction only).
  - Weak selection (s = 0.002) sustains more than strong selection under hard selection, not less (PA5 fails toward the critics).
- **Both:** the outcome turns on the unsourced hardness h (and on R), not on the arithmetic. Several pre-registered numeric bands missed (PA1 partly, PA2, PA5, PB2), so both sides' mean-field intuitions were off in places. The softJ failures at R = 1.05 and at weak s look like a burn-in artefact (flat k/lam), which is unresolved.

**Verdict implications (for the integration pass after reviews; nothing changed yet)**
- **H** (1/300): the external verdict stays contested. Its scope is now explicit: it holds for hard or >= ~30%-hard selection and fails for soft selection and truncation.
- **H8:** the s3.3.1 verbatim holds as stated (s_max). As a rate bound, Term 3 is contradicted for truncation and soft selection and supported for quadratic synergy and partly-hard selection.
- **H5** (Hössjer): conditional on h, the same as H.

**HF-c:** see the HF-c section (Day's 1/300 is conservative at D = 30 at every K; soft T50 > hard T50 in 43/47 pairs).

**HF-d (GAP-05)**
- **Day side:** The slow decline is real in a standard Kimura-flux model. At the upper-end deleterious input with an Ne decline it is 2.4 log units over 252,000 generations, which is more than R = 3 could absorb if nothing offsets it. No critic has answered this with numbers (GAP-05 S21), and the "equilibrium" answer needs the population to have been at its current-Ne equilibrium.
- **Critic side:** Day's "collapse in 9 generations" comes only from switching selection off for harmful mutations. With selection on, the harmful substitution rate is 43x lower and the decline is about 1e-5 per generation. Compensatory and beneficial substitutions, soft selection and epistasis are all omitted here, and each would lower the net decline.
- **Both:** GAP-05 turns on the initial condition and on U_d (0.3-3 moves the decline 10-fold), not on the arithmetic.
