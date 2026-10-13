# R4 HF: H follow-ups (soft-selection rate limit, truncation and synergistic epistasis, T50/lam50 intervals, GAP-05)

**Status: three reviews done (baa7595: 0 BLOCKER, 10 MAJOR); fix pass written (see "Review resolution" at the end, which supersedes the body where they differ); post hoc run `hf_posthoc.py` stage `ph` (pre-registered 5c30ed9) launched, results pending.** Load-bearing tier (HF moves the H ROOT-path node). Not integrated.

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
| U_d | S1 substitutions per lineage | S1 log-fitness decline (sum 2s) over 252,000 gens | S1 substitutions per generation | S2 net | S3 net decline |
|---|---|---|---|---|---|
| 0.3 | 16,800 | 0.25 | 0.067 | ~0 (< 1e-18) | 0.24 |
| 1 | 55,900 | 0.82 | 0.22 | ~0 | 0.80 |
| 3 | 168,000 | **2.47** | 0.67 | ~0 | **2.39** |

- Sensitivity: Ne = 2e4 roughly halves the decline (U_d = 3: 1.09 S1, 1.01 S3). Shape 0.1 gives 2.54 / 2.44; shape 0.3 gives 1.77 / 1.73 (U_d = 3, Ne = 1e4). Everything scales linearly in U_d.
- S0 (selection off): harmful substitutions per generation = 0.75 × U_total = 28.8 at U_total = 38.4 (parameters.yaml). Day's 7.6 implies U_total = 10.1. With selection on (S1), the rate is 0.67 per generation at U_d = 3, i.e. **43x lower than S0** (11x lower than Day's 7.6) **[fix pass (C3): 43x = 9.6x from the 75%-harmful premise x 4.5x from selection; the decline ratio, selection off vs on at U_d = 3, is about 1.8e4]**. The per-generation log-fitness decline under S1 is about 1e-5, not the order-0.1-per-generation decline needed for collapse in 9 generations.
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
- **Day's 9-generation collapse needs selection switched off for every harmful mutation.** With Kimura fixation over Boyko's DFE, the harmful substitution rate is 43x lower than the selection-off rate **[fix pass (C3): 9.6x of that is the input premise, 4.5x is selection; the decline ratio is about 1.8e4; (Day-3) this scores the second horn of Day's dilemma only]**. The per-generation decline is about 1e-5 in log fitness, so nothing collapses in 9 generations, or in 225 years. Day's statement scores against its own hypothesis (drift with selection "switched off by hypothesis"). That is a premise no critic holds: the neutral theory he is answering keeps purifying selection on constrained sites (Kimura's nearly neutral theory; Charlesworth 2013).
- **[Fix pass (Critic-3): S3 is "the upper-end scenario computed"; see Review resolution.]** **But the slow decline is real in this model and is not small over 252,000 generations.** Starting from an optimum, or from equilibrium at the larger ancestral Ne (S3, the standard demographic picture of an Ne decline), the cumulative log-fitness decline is about 0.8-2.5 (U_d 1-3), i.e. absolute fitness falls 2.2- to 12-fold. That is the GAP-05 "upper-end scenario", now computed. It supports the premise of Hössjer's HO-11 (fitness declines over time) at the upper end of U_d. It does not support "quite rapidly dies": the rate is about 1e-5 per generation, and it is open to compensation that this model omits.
- **The critics' standard resolution holds only at equilibrium.** At the mutation-selection-drift equilibrium for the current Ne, the net decline is zero (S2). S3 shows that an Ne decline from about 2e5 to 1e4 puts the population out of equilibrium for far longer than 252,000 generations (per-site relaxation ~1/mu), so S2's zero needs a reason the population was already at its current-Ne equilibrium. The model also omits compensatory mutations at other sites, beneficial substitutions (A2e-alpha: 1,000-3,600 coding adaptive substitutions per lineage on the critic-side estimates), soft selection (Charlesworth 2013), and epistasis. Each of these would offset some of the decline; none is quantified here.

## HF-a: soft-selection rate limit (complete)
**Targets:** H (Day, Z18168236 Abstract) "one beneficial substitution per 300 generations"; H8 (Day, Z19984826 s3.3.1) "None of them raises smax above order unity, and the reason is the same in all three cases." (RH tag: dialectic.) Critic-side mechanism: Wallace's soft selection, Nunney, Maynard Smith truncation. Raw: `raw/hf_analyse.out` (1,720 rows). K = 1000 and s = 0.01 unless stated. Hard caps (H8 lam50, 10k): 0.00368 / 0.0363 / 0.0606 at R = 1.111 / 2 / 3.

**Results on the pre-registered success rule** (lam_max = largest lam with >= 50% success at 20k; "1.6+" = success at the top of the grid, censored).

| Mode | R = 1.05 | R = 1.111 | R = 1.5 | R = 2 | R = 3 |
|---|---|---|---|---|---|
| softJ (h = 0) lam_max | none (< 0.0351) | 0.8 **[>= 0.8, max_open-censored at 1.6]** | 1.6+ | 1.6+ | 1.6+ |
| trunc lam_max | 0.8 **[>= 0.8, max_open-censored at 1.6]** | 1.6+ | 1.6+ | 1.6+ | 1.6+ |
| softWF (R-free) lam_max | | 1.6+ (all R) | | | |
| mix h = 0.1 lam50 10k (x hard cap) **[fix pass: log-midpoints of a 4/4 and a 0/4 grid point; report the brackets]** | | 0.0064 (1.7x); bracket 0.0037-0.0111 (1.0-3.0x) | | 0.141 (3.9x); bracket 0.1-0.2 (2.76-5.5x) | 0.283 (4.7x); bracket 0.2-0.4 (3.3-6.6x) |
| mix h = 0.3 lam50 10k (x hard cap) **[fix pass: floor tie / small-nopen noise; indeterminate]** | | 0.0037 (2/4 tie at the grid floor) | | no crossing (noise at nopen 4-6); lam_max 0.0351 (1.0x) | 0.0705 (1.2x) |
| mix h = 1 (validation) lam50 10k | | 0.00368 (H8 0.00368) | | 0.0360 (H8 0.0363) | |
| K = 4000 softJ / trunc lam_max | | 0.4 **[>= 0.4, max_open-censored at 1.6; no 0.8 point]** / 1.6+ | | 1.6+ / 1.6+ | |
| weak s = 0.002 softJ / trunc lam_max | | none / 0.4+ | | none / 0.4+ | |
| weak s = 0.002 hard lam50 (10k and 20k) | | > 0.0077 (no crossing) | | > 0.050 (no crossing) | |

**What the failures are (post hoc descriptive reading of the same rows; changes no pre-registered score).**
- *Extinction only, mix cells.* At low lam, mix cells hold few open loci (nopen ~5-60), and the steady-state rule (`nopen_q4/nopen_q1 <= 1.15`) fails on noise there: one h = 0.3, R = 2 rep has a ratio of 2.52 at nopen ~6. These runs are alive and keep pace (k/lam ~1). Reading extinction alone, the boundary lies between the last all-alive lam and the first all-extinct lam:
  - h = 0.1: R = 1.111 0.0111-0.0351 (3.0-9.5x the hard cap) **[withdrawn in the fix pass (C1): at 0.0111 the runs are alive but not keeping pace (k/lam 0.79-0.92, N/K 0.85-0.92); the limit is about 0.011-0.013, 3-3.5x]**; R = 2 0.1-0.2 (2.8-5.5x); R = 3 0.2-0.4 (3.3-6.6x).
  - h = 0.3: R = 1.111 0.0037-0.0111 (1.0-3.0x); R = 2 0.0351-0.1 (1.0-2.8x); R = 3 about 0.1 (2/4 extinct; 1.7x).
  - The pre-registered mean-field rule (extinction when h lam D_soft > ln R, with D_soft from the softJ rows) predicts 0.0052 / 0.0157 at R = 1.111 and 0.096 / 0.29 at R = 2 (h = 0.3 / 0.1). That is inside the observed brackets at R = 1.111 and R = 2 (h = 0.3) and up to ~2x above them at R >= 2 for h = 0.1, and at R = 3.
- *softJ at R = 1.05, and weak-s softJ.* None of these runs went extinct or hit max_open below lam = 0.8. They fail the k/lam >= 0.9 rule with a ratio that is **flat in lam**: 0.79-0.84 at R = 1.05 for every lam from 0.0351 to 0.4; 0.46-0.55 for weak s at R = 1.111; 0.77-0.85 for weak s at R = 2. A real rate ceiling would make k/lam fall as lam rises. A flat ratio is what an unfilled sweep pipeline gives: the implied sweep time (nopen/k) is ~7,500 generations at R = 1.05 and ~19,000 for weak s at R = 1.111, both longer than the 5,000-generation burn-in (the R = 1.111 s = 0.01 cells, ~4,500 generations, pass). So these "failures" are probably a window artefact, not a limit. The rule is applied as pre-registered; a longer burn-in run would settle it (proposed, not run). The same caveat covers K = 4000 softJ at R = 1.111 (k/lam 0.87-0.95, borderline).
- *Weak-s hard at 40k (the recorded 40k checkpoint, not used by `analyse`).* At R = 1.111 all 6 reps survive at lam 0.0049 and 2/6 at 0.0061 and at 0.0077, so lam50(40k) is ~0.005-0.006 (1.4-1.7x the s = 0.01 cap). At R = 2, 5/6 survive at the top (0.050), so the result is still censored. D_obs, the cost per substitution, is ~15-17 at both s (Haldane's s-independence of the cost holds), but the sustainable load lam x D is ~1.5x higher at weak s.

**Scoring.**
| ID | Prediction | Result | Score |
|---|---|---|---|
| DA1 (Day) | mix h = 0.1 and 0.3 lam50 within 2x of the hard cap at R = 1.111 (<= 0.0074) and R = 2 (<= 0.073) | h = 0.3: 0.0037; R = 2 lam_max 0.0351 (extinction bracket 0.035-0.1). h = 0.1: 0.0064 at R = 1.111 (extinction-only 0.011-0.035); **0.141 at R = 2** | **Fails** (h = 0.1 at R = 2 is 3.9x the cap). Holds for h = 0.3. **Fix pass (C1, Day-4): fails robustly at h = 0.1, R = 2, lam 0.1 (2.76x; 4/4 sustained on the strict rule); h = 0.3 "holds" rests on a floor tie and noise (within 1-3x). DA1 is an audit gloss, not a Day statement.** |
| DA2 (Day) | K = 4000 lam_max <= K = 1000 lam_max | softJ 0.4 vs 0.8 (R = 1.111); 1.6+ vs 1.6+ elsewhere | **Fix pass (C2): unscorable** (max_open censoring: both R = 1.111 values are set by the 5,000-locus cap; the rest are grid-top censored). Post hoc stage C pending. |
| CA1 (critic) | softJ and trunc sustain >= 0.1 at every R >= 1.111 and >= 0.4 at R >= 2 | softJ >= 0.8, trunc >= 1.6 at every R >= 1.111 | **Holds** (240-480x Haldane's 1/300) |
| CA2 (critic) | mix h = 0.1 lam50 >= 3x the hard cap at R <= 2 | 1.7x (R = 1.111), 3.9x (R = 2) (both log-midpoints) | **Fix pass (C1): R = 1.111 fails (limit about 3x, marginal); R = 2 indeterminate (bracket 2.76-5.5x).** The extinction-only reading is withdrawn. Post hoc stage M pending. |
| PA1 | softJ lam_max: R = 1.05 0.1-0.4; R = 1.111 0.2-0.8; R >= 2 >= 0.4. trunc >= softJ. softWF <= 0.4, maxrel at limit < 2 | R = 1.05: none on the rule (pipeline caveat); 0.8; 1.6+. trunc >= softJ at every R. **softWF sustains 1.6+** (maxrel 1.74 at 1.6) | **Partly holds**: R = 1.111 and R >= 2 hold, trunc >= softJ holds; R = 1.05 fails; softWF fails (it is faster than predicted) |
| PA2 | h = 0.3 R = 1.111 [0.004, 0.012]; h = 0.1 R = 1.111 [0.008, 0.035]; R = 2: h = 0.3 [0.04, 0.12], h = 0.1 [0.07, 0.3] | 0.0037; 0.0064; no crossing (extinction 0.035-0.1); 0.141 | **1 of 4 holds** (h = 0.1, R = 2); 2 just below their bands; 1 unscorable on the rule. The extinction-only brackets overlap all four bands. **Fix pass (C1): the two h = 0.3 rows are indeterminate (floor tie / noise).** |
| PA3 | mix h = 1 within 25% of H8 (0.00368, 0.0363) | 0.00368, 0.0360 (< 1%) | **Holds** (engine validated) |
| PA4 | K = 4000 within one lam step of K = 1000 | 0.4 vs 0.8; others censored equal | **Fix pass (C2): unscorable** (max_open censoring). Post hoc stage C pending. |
| PA5 | weak s: hard lam50 x D_obs within 25% of s = 0.01; softJ lam_max at R = 2 0.1-0.2 | hard: no crossing at 10k/20k (> 2.1x / > 1.4x cap); 40k read ~1.5x. softJ: fails at every lam (pipeline caveat) | **Fails** (weak-s hard sustains more than the s = 0.01 cap; D_obs itself is s-independent) |

**Interpretation.**
- **[Fix pass: superseded by Review resolution C1, C4, Day-1, Critic-1. Soft modes cannot go extinct in this model; h = 0.3 is within 1-3x, h = 0.1 about 3-5.5x.]** **The hard cap is specific to hard selection, and it comes back quickly as hardness rises.** With purely relative (soft) selection or truncation, a K = 1000 population sustains 0.8-1.6+ substitutions per generation at every R >= 1.111, i.e. >= 217x the H8 hard cap and >= 240x Haldane's 1/300. The R-free Wright-Fisher version (softWF) does too. With 30% of the selection hard (h = 0.3), the limit is within 1.0-1.7x the hard cap on the pre-registered rule (<= 3x reading extinction only). With 10% hard (h = 0.1), it is 1.7-4.7x (2.8-9.5x reading extinction only). The mean-field rule h lam D_soft ~ ln R captures this within about 2x.
- So whether a Haldane-type limit binds depends on how hard human selection is. The hardness h is not sourced for humans; it is the new key unsourced parameter, next to R (V17).
- Day's s3.3.1 is literally true of s_max: truncation's s_max is R by construction, and soft selection's maxrel is 1.1-2.2 here **[fix pass (C9): softWF's realised maxrel is 1.09-1.75; for softJ the realised differential is <= R]**. **As a rate claim it is false for soft selection and truncation** **[fix pass (Day-1, Day-2): in-model, for purely relative fitness and for noise-free genotype truncation]**. It is close to true for selection that is >= ~30% hard.

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
- **[Fix pass (Day-2, C2): scope is noise-free genotype truncation; R = 1.05 is >= 249x Term 3 (max_open-censored), not 353x; phenotypic truncation is post hoc stage N, pending.]** **Truncation is a real reduction in the cost, and Term 3 is not a bound across mechanisms.** Day's "order unity" holds for s_max but does not cap the rate: with s_max = R <= 3, truncation sustains >= 22-353x Term 3. This is the pre-registered "PB1/CB1 holding" branch.
- **Quadratic synergy against an absolute optimum, under hard selection, does not help** **[fix pass (Critic-2): scope narrowed; "the critic-side synergy mechanism fails" withdrawn]**. In this model it lowers the hard-selection rate by up to ~2x, and the pre-registered mean-field gain was wrong in sign. It is not a test of synergy acting through the variance of counts under relative fitness, which is the critics' mechanism.
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
*Pre-review text; corrected items are listed in the Review resolution (C1, C3, Day-1, Day-4, Day-5, Critic-1, Critic-3, Critic-5).*

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

**Verdict implications (pre-review; superseded by "Provisional verdicts" in the Review resolution)**
- **H** (1/300): the external verdict stays contested. Its scope is now explicit: it holds for hard or >= ~30%-hard selection and fails for soft selection and truncation.
- **H8:** the s3.3.1 verbatim holds as stated (s_max). As a rate bound, Term 3 is contradicted for truncation and soft selection and supported for quadratic synergy and partly-hard selection.
- **H5** (Hössjer): conditional on h, the same as H.

**HF-c:** see the HF-c section (Day's 1/300 is conservative at D = 30 at every K; soft T50 > hard T50 in 43/47 pairs).

**HF-d (GAP-05)**
- **Day side:** The slow decline is real in a standard Kimura-flux model. At the upper-end deleterious input with an Ne decline it is 2.4 log units over 252,000 generations, which is more than R = 3 could absorb if nothing offsets it. No critic has answered this with numbers (GAP-05 S21), and the "equilibrium" answer needs the population to have been at its current-Ne equilibrium.
- **Critic side:** Day's "collapse in 9 generations" comes only from switching selection off for harmful mutations. With selection on, the harmful substitution rate is 43x lower and the decline is about 1e-5 per generation. Compensatory and beneficial substitutions, soft selection and epistasis are all omitted here, and each would lower the net decline.
- **Both:** GAP-05 turns on the initial condition and on U_d (0.3-3 moves the decline 10-fold), not on the arithmetic.
- **Supplementary note (2026-10-11, R4 GAP05; supplements, does not replace, the HF rows):** on a sourced coding DFE (Kim, Huber & Lohmueller 2017) the coding-only decline is 0.29-0.43 at N_e 1e4 on the pre-registered base (mu = 1.2e-8, T = 252,000) and about 0.8-1.1 on a divergence-calibrated base (post hoc), against HF's 0.82 at U_d = 1. Not like for like: a different s-distribution, and the coding 0.33 per genome per generation is a nonsynonymous mutation rate including neutral and nearly neutral classes, not a deleterious rate. The noncoding row stays unsourced.

## Review resolution (fix pass, 2026-10-11)
Reviews (baa7595): `REVIEW-R4-HF-correctness.md` (C), `-steelman-day.md` (Day), `-steelman-critic.md` (Critic); 0 BLOCKER, 10 MAJOR. Items that need new data go to the post hoc run **`hf_posthoc.py` stage `ph`** (pre-registered, labelled post hoc, 5c30ed9; 410 jobs; stages L long burn, C cap release, M mix boundary, N noisy truncation; predictions in its docstring). They are marked **pending post hoc run `ph`**. No pre-registered score is changed by the fix pass except where a review showed the reported value was a censoring point or a midpoint (C1, C2); those rows now say so in place.

### MAJOR
- **C1 (mix midpoints; extinction-only reading). Resolved in text; final boundary pending post hoc run `ph` (stage M).** The mix lam50 values were log-midpoints between a 4/4 and a 0/4 grid point (0.0064 = sqrt(0.0037 x 0.0111), etc.). Brackets: h = 0.1: 1.0-3.0x (R = 1.111), **2.76-5.5x (R = 2)**, 3.3-6.6x (R = 3). Rescored: **CA2 fails at R = 1.111 (limit about 3x, marginal) and is indeterminate at R = 2** (3x = 0.109 lies inside 0.1-0.2). **DA1 fails robustly** at h = 0.1, R = 2, lam 0.1 (2.76x the cap; 4/4 sustained on the strict rule, k/lam 0.94-1.01). PA2's h = 0.3 rows are **indeterminate** (2/4 floor tie at R = 1.111; small-nopen noise at R = 2). **Withdrawn:** "3.0-9.5x" and "holds at both R on the extinction-only reading". At h = 0.1, R = 1.111, lam 0.0111 the runs are alive but not keeping pace (k/lam 0.79-0.92 with nopen about 57, N/K 0.85-0.92, h La 0.087-0.093 against ln R 0.105), and at 0.0351 all four are extinct by generation 2,670; the limit there is about 0.011-0.013 (3-3.5x). h = 0.3 is "within 1-3x the hard cap" (grid- and noise-limited), not "1.0-1.7x".
- **C2 (max_open censoring). Resolved in text; cap release pending post hoc run `ph` (stage C).** In every soft/trunc cell nopen is about lam x tau with tau nearly flat in lam, so the lam_max values below the grid top are set by max_open = 5,000. Restated: softJ R = 1.111 **>= 0.8 (censored at 1.6)**; K = 4000 softJ R = 1.111 **>= 0.4 (censored)**; trunc R = 1.05 **>= 0.8 (>= 249x Term 3; "353x" withdrawn)**. **DA2 and PA4 are unscorable** (they compared two censoring points), not "holds".
- **C3 (the 43x). Resolved.** S0 = 0.75 x U_total (38.4) = 28.8 per generation. With the same harmful input (U_d = 3) and selection off, the rate is 3.0, so **selection alone lowers the substitution count 4.5x (3 / 0.665); the remaining 9.6x comes from Day's 75%-of-all-mutations premise** against the 8%-constrained input (against Day's 7.6: 2.5x input, 4.5x selection). The operative comparison is the decline (post hoc, descriptive): selection off at U_d = 3 gives about 3 x 0.058 = 0.17 log units per generation, against S1's 9.8e-6, **a ratio of about 1.8e4**. PD4 and the critic-side ">10x" are scored as pre-registered and unchanged.
- **C4 (two soft-selection results). Resolved.** H-C2 (latency for a fixed target with finite supply M = 2Ku; the soft cull loses rare mutants) and HF-a (throughput on a treadmill that re-seeds every lost copy, so supply never limits) answer different questions. **Soft selection is slower per locus (H-C2; softJ tau about 4,300 generations at R = 1.111) but does not cap the number of concurrent sweeps (HF-a).** HF-c's "soft T50 > hard T50 in 43/47 pairs" is a latency result and stands; HF-a's ">= 217x the hard cap" is a throughput result, conditional on Day-1. Integration must carry "latency vs throughput" into the H verdict text (ROOT row 4, F1); neither result may be cited alone for "soft selection and the cost".
- **Day-1 (soft arms cannot fail for population reasons; cost uncharged). Resolved in text.** In softJ the population is always culled back to K from R N >= K, and in softWF N = K by definition, so extinction is impossible in both; the only failures are a growing backlog or the max_open cap, and the treadmill re-seeds every lost copy (it completes near-neutral substitutions too). **The cost per substitution is not reduced, only not charged:** softWF D_obs is 16.2-16.8 at every lam (cell means; 16.1-16.9 per rep), the same as the hard arm's about 16 (a Day-side observation: Haldane's cost per substitution survives). At lam = 1.6 softWF's mean log-viability relative to the optimum genotype is about -27 (1.6 x 16.8); a hard-accounting population would need R of about e^27. Every soft result is now stated with its condition: **"with purely relative fitness (soft selection) the population cannot go extinct in this model, and the rate is limited only by sweep latency and the locus cap."**
- **Day-2 (truncation is noise-free genotype truncation). Resolved in scope; phenotypic arm pending post hoc run `ph` (stage N).** Every truncation statement is scoped to **noise-free truncation on the exact count of ancestral copies** (s does not enter it, C8). Crow & Kimura 1979 (PA-15): "Whether nature ranks and truncates, or approximates this behavior, is an empirical question, yet to be answered." The H8 implication becomes "Term 3 contradicted in-model for noise-free genotype truncation; untested for phenotypic truncation" until stage N (genotypic share 1, 0.5, 0.1) is scored. Stage N also has N = K always, so it measures sweep speed, not load (Day-1 applies).
- **Day-3 (HF-d tests only horn two). Resolved.** Added targets (same post, the paragraph after the 7.6 sentence; RH tag dialectic): "Either selection is operating—in which case the reproductive ceiling applies and parallel fixation fails—or selection is not operating, in which case harmful mutations accumulate, the genome degenerates, and the species goes extinct. You cannot turn selection off for neutral mutations while keeping it on for harmful ones." Under rule C the 9-generation figure is the second horn of a stated dilemma (a reductio conditional on "switched off by hypothesis"), and it **holds internally on that premise**. S1 (selection on for harmful mutations, drift for neutral ones) escapes horn 2 **at the cost of horn 1: purging U_d = 3 under hard multiplicative selection is the H7 load problem** (mean fitness about e^-3; H7 found about 18 offspring per female at U = 2.2; Lesecque et al. 2012, PA-16, "≥ 88% reproductive failure" in the absolute model), which turns on hardness exactly as HF-a does. HF-d does not test horn 1. The crux sentence is scored below (contradicted externally by per-mutation fixation; S1 computes that case).
- **Critic-1 (h = 0.3 numbers are floor ties and noise). Resolved in text; pending post hoc run `ph` (stage M).** Everywhere: "within 1-3x the hard cap at h = 0.3 (grid- and noise-limited)", with the h = 0.1 limit (about 3-5.5x) beside it; "1.0x" as a point value is dropped. The mix "10k" column counts any failure up to 20k (C6), which favours Day's side by up to about 20%; stage M scores at 20k against both the 10k and the 20k H8 caps.
- **Critic-2 (synergy anchored to an absolute optimum). Resolved in scope; no new arm in `ph`.** CB2 stays "fails" as pre-registered. The interpretation is scoped to "quadratic synergy against an absolute optimum under hard selection"; "the critic-side synergy mechanism fails" is deleted (done in place). b A^2 grows with the square of the number of open loci before any variance among individuals (persisting reps at R = 2 hold nopen 14.6-27.9 at b = 0 against 3.5-5.2 at b = 4e-3). A synergy arm under relative fitness (mix h in {0.3, 1} with b > 0, or b on the deviation of A from the population mean) is **an open follow-up, not run**.
- **Critic-3 (S3 stacks upper-end inputs). Resolved.** S3's 2.39 is **"the upper-end scenario computed"** (GAP-05's words): U_d = 3 (an extrapolation), Ne = 1e4 for all 252,000 generations, a step down from 2.06e5 at t = 0, and exact back mutation as the only return route. With Ne = 2e4 it is 1.01 (< ln 3); with U_d = 1 it is 0.80. Comparing a log decline relative to the optimum genotype with ln R treats all of it as lost absolute fitness, i.e. the hard-selection reading; **if load is absorbed as soft selection, it is not a demographic decline (cf. HF-a, Day-1)**. The Day-side credit "more than R = 3 could absorb" now carries both conditions.

### MINOR and NOTE
- **C5. Resolved; burn-in part pending post hoc run `ph` (stage L).** softJ s = 0.01, R = 1.111 success on the rule: 1/4, 3/4, 4/4, 3/4, >= 2/4 at lam 0.0351, 0.1, 0.2, 0.4, 0.8 (lam50 NaN: the lowest point fails; q4/q1 1.07-1.28, k/lam 0.89-0.97 in every cell). The earlier "the R = 1.111 s = 0.01 cells pass" is withdrawn.
- **C6. Disclosed.** For steady-rule modes `success()` (8bd9d29) counts a 10k success only if the run never failed over the whole 20k run, so the mix 10k and 20k columns are identical. Against H8's 20k caps (0.0035 / 0.030 / 0.056) the midpoints are 1.8x / 4.7x / 5.1x, against 1.7x / 3.9x / 4.7x at 10k. The bias is <= ~20% and favours Day's side.
- **C7. Resolved.** PA3's "< 1%" is grid identity (both lam50 values are the x = 0.6 grid point with a 3/6 tie). Restated: "same grid bracket; 9% at 20k (0.00318 vs 0.0035)". PA3 holds within its 25%.
- **C8. Resolved.** trunc is s-independent (it keeps the K juveniles with the fewest ancestral copies), so the weak-s trunc rows are replicates of the s = 0.01 rows (nopen 159 vs 160; 2 vs 2), not a weak-selection test.
- **C9. Resolved** (in place): cite softWF realised maxrel 1.09-1.75 only; for softJ, "realised differential <= R".
- **C10. Resolved.** Weak-s hard: the fair comparison is 40k against 40k, H8 s = 0.01 lam50(40k) = 0.00265 against weak 0.0049-0.0061, i.e. **1.9-2.3x** (not 1.4-1.7x against the 10k cap). The 20k "no crossing" is a tie at 3/6 at both 0.0061 and 0.0077. PA5 fails either way.
- **C11. Resolved.** (a) Day/ally row restated: "Holds at U_d = 3 for Ne = 1e4 at every shape, and for shape 0.1 at Ne = 2e4 (1.19); fails at U_d <= 1; the Ne = 2e4, shape 0.184 failure is by a hair (1.09 vs ln 3 = 1.0986)". (b) The column is renamed "S1 substitutions per generation" (in place).
- **C12 / PD5 (validation z = -3.1). Closed.** The correctness reviewer reran the per-site WF validation with a fresh seed and 5x the replicates (2,000,000 new mutations per point, na-workhorse, 2026-10-11, scratch script, not committed): 2Ns = -2: z +0.38; -1: +0.44; **-0.5: 2.815e-4 vs 2.911e-4, z -0.79**; **0: 5.135e-4 vs 5.000e-4, z +0.85**; +1: +0.54. Every point passes, including the neutral point, which only an implementation error could bias. **PD5 still fails as pre-registered (one point at z = -3.10 in the original run); the estimator item is closed as sampling noise.** A committed post hoc validation run is optional and not scheduled.
- **C13. Noted.** S2's zero net decline is exact by construction (the per-site two-state equilibrium has zero net flux); PD2 checks the code, not the population.
- **C14. Disclosed.** No smoke output was kept, so the smoke run's time cannot be shown. It is treated as plumbing only; the pre-registration commit 8bd9d29 (18:51:02) precedes the main launch (18:51:16). `hf_posthoc.py` keeps its smoke output (`raw/hf_ph_smoke*.out`, after 5c30ed9).
- **C, flagged burn-in artefact.** Agreed: CA1 and the H/H8 verdicts are unaffected; the artefact decides PA1 at R = 1.05, PA5 (softJ part) and K = 4000 softJ at R = 1.111. Stage L (80k generations, 40k burn, max_open 20,000) decides them; **pending post hoc run `ph`**.
- **Day-4. Resolved.** DA1 is labelled "audit gloss (not a Day statement)"; its failure scores against no Day statement (rule S). Both halves get equal weight in the verdict scope: "near the hard cap for h >= 0.3; a few-fold above it at h = 0.1; uncapped only at h = 0". Neither side has a human hardness figure.
- **Day-5. Resolved.** Day-side list now includes PC3: at Haldane's R = 1.111 and D = 30 the 95% interval lies wholly above 300 at every K tested (K = 1,000: 419-568; 16,000: 342-720; 64,000: 326-768), so "approximately one per 300 generations" is conservative there under hard selection, and PC3's critic-side prediction failed. Carry into the H claim file (with Critic-6's R-scope).
- **Critic-4. Resolved (definition).** h is "the share of the log-load expressed as density-independent survival at a fixed R" in the mix model, which has no density compensation (J = R N even when N < K). It is not Wallace's field parameter and has no field estimator. A density-compensating arm (fecundity rising as N falls below K) would raise the partly-hard limits; not run.
- **Critic-5. Resolved.** Added: even where the rule records failure, the realised rate in every soft and truncation cell without a backlog is >= 0.46 lam, i.e. >= 0.016 per generation at lam = 0.0351 (about 5x 1/300) and >= 0.18 at lam = 0.4 (about 55x); at R >= 1.111, s = 0.01 every cell keeps k/lam >= 0.89. The artefact decides only Day-side or audit bands.
- **Critic-6. Resolved.** PC3 is stated "at R = 1.111" only (R is unsourced, V17). Same table, K = 1,000, D = 30 interval: 213-349 at R = 1.2, 174-263 at R = 1.3, 93-115 at R = 1.5, 50-69 at R = 2.
- **Critic-7 / Day-6. Noted** (latency vs throughput is C4; synergy credit to Day stays, scoped by Critic-2).
- **R4-X1 RH (C).** "kills off the entire proto-human race thousands of times faster" (same post) is rhetoric (hyperbole) like "closes it with a corpse"; log in `ledgers/slips.md` at integration, not scored.

### Pending post hoc run `ph` (what each stage decides)
*Scored 2026-10-13: see "Post hoc run `ph`" at the end of this file. Every "pending post hoc run `ph`" above is closed there.*

| Stage | Decides | Review items |
|---|---|---|
| L (long burn) | PA1 at R = 1.05, PA5 softJ, K = 4000 softJ at R = 1.111: fill lag or rate limit | C5, C (burn-in), Critic-5 |
| C (cap release, max_open 20,000) | whether softJ R = 1.111 (K = 1000, 4000), softJ R = 1.05 and trunc R = 1.05 sustain 0.8 / 1.6; whether DA2 / PA4 become scorable | C2 |
| M (mix boundary, 8 reps, 40k) | the h = 0.1 and h = 0.3 boundaries at R = 1.111 and 2 (CA2 at R = 2; DA1/PA2 at grid resolution); the h-scope sentence of H/H8/H5 | C1, Critic-1, Day-4 |
| N (noisy truncation, genotypic share 1 / 0.5 / 0.1) | whether "Term 3 contradicted in-model" extends from noise-free to phenotypic truncation | Day-2 |

### Provisional verdicts (rule R4-X1; for integration after the post hoc run; nothing in the claim files is changed yet)
*The bracket figures in the H and H8 items below are replaced by the stage M and N numbers in "Post hoc run `ph`" (section "Verdict text after `ph`"). No verdict value changes.*

- **H (Day, 1/300).** Fidelity and internal unchanged (HF re-tests the external premise only). **External: contested**, with the h-scope: "the cap binds for hard selection and stays within about 1-3x of it at h = 0.3; at h = 0.1 the limit is about 3-5.5x; with purely relative fitness (no extinction possible in-model) or noise-free truncation there is no cap in-model". Never "fails for soft selection" without "conditional on purely relative fitness". h is the audit's parameter, not an author's input, so rule F does not apply; the verdict stays contested because h, like R (V17), has no source. Day-side addition: at R = 1.111, hard selection, the 1/300 is conservative at 95% at every K tested (PC3). The stage M numbers will replace the bracket figures.
- **H8 (Day, Z19984826).** s3.3.1 "None of them raises smax above order unity": **internal holds** (literal s_max; trunc s_max = R; softWF realised maxrel <= 1.75). **Term 3 as a rate bound across mechanisms: external contested**; contradicted in-model for purely relative fitness and noise-free genotype truncation; supported for hard selection, h >= 0.3, and quadratic synergy against an absolute optimum. These counterexamples rest on modelling choices Day does not share, so this is an external disagreement, not rule N. Phenotypic truncation: pending stage N.
- **H5 (Hössjer).** Same as H: **conditional on h and R; external contested**.
- **Drift Deathmarch (Day, blog 2026-01-11).** The 9-generation figure: **internal holds** as the second horn of a stated dilemma, conditional on its premise (rule C). "Standard estimates for the damage caused by each mutation" is uncited: **fidelity unverifiable** (rule F). The 7.6 vs 28.8 difference runs in the direction that strengthens Day's horn: slip ledger, not an error against him (R1). The crux "You cannot turn selection off for neutral mutations while keeping it on for harmful ones": **external contradicted** by standard per-mutation fixation (Kimura u(s); S1 computes exactly that case). The dilemma's remaining force is horn 1 (purging load under hard selection, H7), which HF-d does not test. "Thousands of times faster": rhetoric, slip ledger.
- **HO-11 (Hössjer, p.6).** "the overall fitness of the population declines over time": **external contested** (supported only at the upper-end U_d = 3 with Ne = 1e4, from the optimum or after an Ne decline, and only under the hard-selection reading of the decline). "and the population eventually (and quite rapidly) dies": **external contradicted** in this model (about 1e-5 log units per generation).

## Post hoc run `ph` (scored 2026-10-13)

**Status of this section.** Post hoc. `hf_posthoc.py` was written after the three HF reviews and committed with its predictions before any run (5c30ed9). Its docstring says of itself that every prediction was made after `raw/hf_main.jsonl` had been seen, so nothing here can rescue or sink a pre-registered HF score. It closes the items the reviews left open. One combined light review is owed before integration (low-stakes tier: the run re-measures reviewed items).

**Run.** 83 cells, 410 jobs, 454.8 CPU-h, peak worker RSS 385 MB. Two hosts and three shard files (`raw/hf_ph_wh.jsonl`, `raw/hf_ph_bd.jsonl`, `raw/hf_ph_all.jsonl`); na-workhorse rebooted on 2026-10-12 and its shard was relaunched (history and md5s in `raw/hf_ph.host`). Merge: 410 unique of 410 expected, missing 0, extra 0; **209 jobs were run on two hosts, 0 mismatches** on every field but run time and memory. Merged rows `raw/hf_ph.jsonl`; tables `raw/hf_ph_analyse.out`. Engine identity was checked before the run (`smoke`: 4 `hf_main` jobs rerun with their original seeds).

Rules are the ones fixed in the docstring: HF's rule (no failure, k/lam >= 0.9, nopen q4/q1 <= 1.15) and, beside it, the reviews' stricter rule (k/lam >= 0.95, q4/q1 <= 1.10). tau = nopen / k.

### Stage L: long burn-in (softJ, 80,000 generations, 40,000 burn)

| Series | lam 0.0351 / 0.1 / 0.2 / 0.4: k/lam | HF rule | strict rule | tau (generations) |
|---|---|---|---|---|
| s = 0.01, R = 1.05, K = 1000 | 0.973 / 0.993 / 0.997 / 1.001 | 4/4 each | 4/4 each | 7,041 / 7,023 / 7,129 / 7,385 |
| s = 0.01, R = 1.111, K = 1000 | 1.011 / 0.983 / 1.002 / 0.995 | 4/4 each | 4/4, 3/4, 4/4, 4/4 | 4,329 / 4,405 / 4,424 / 4,508 |
| s = 0.01, R = 1.111, K = 4000 | 0.989 / 1.004 / 0.999 / 1.004 | 4/4 each | 3/4, 4/4, 4/4, 4/4 | 5,411 / 5,549 / 5,597 / 5,693 |
| s = 0.002, R = 1.111, K = 1000 | 0.991 / 0.988 / 0.978 / 0.987 | 4/4 each | 4/4 each | 16,072 / 15,817 / 16,015 / 15,877 |
| s = 0.002, R = 2, K = 1000 | 1.010 / 1.015 / 0.996 / 1.005 | 4/4 each | 4/4 each | 7,413 / 7,404 / 7,433 / 7,432 |

| Prediction | Result |
|---|---|
| Critic side: every L cell passes HF's rule at every lam | **Hit** (80 of 80 runs) |
| Day side: in at least one series k/lam falls with lam, below 0.9 at 0.4 with no backlog | **Miss** (k/lam at 0.4 is 0.987 to 1.005) |
| Audit PL1: k/lam >= 0.95 and q4/q1 <= 1.10 in every cell | **Hit** on cell means (lowest k/lam 0.973, highest q4/q1 1.05); 2 of 80 single runs miss the strict rule |
| Audit PL1, tau values: about 7,500 / 4,300 / 6,000 / 20,000 / 9,000 | First three within 10%; the two weak-s values are 18-21% below the prediction (15,900 and 7,420) |
| Audit PL2: tau flat in lam within 25% | **Hit** (largest spread 5%) |

The flat-k/lam softJ "failures" of the main run at R = 1.05, at K = 4000 and at weak s were a fill lag: the pipeline had not filled when the 5,000-generation burn ended. With a 40,000-generation burn they are gone. Recorded for Day's side: in the three s = 0.01 series tau rises by 4-5% over an 11-fold range of lam, and tau is about 25% longer at K = 4000 than at K = 1000. Sweeps take longer when more are concurrent and when the population is larger; neither lowers throughput in this range.

### Stage C: cap release (max_open 20,000; the main-stage window: 20,000 generations, 5,000 burn)

| Cell | lam | HF rule | k/lam | q4/q1 | nopen | backlog failures |
|---|---|---|---|---|---|---|
| softJ K = 1000, R = 1.05 | 0.8 | 0/4 | 0.784 | 1.40 | 5,275 | 0 |
| | 1.6 | 0/4 | 0.746 | 1.49 | 11,098 | 0 |
| softJ K = 1000, R = 1.111 | 0.8 | 3/4 | 0.931 | 1.13 | 3,588 | 0 |
| | 1.6 | 0/4 | 0.916 | 1.16 | 7,570 | 0 |
| softJ K = 4000, R = 1.111 | 0.8 | 0/3 | 0.894 | 1.17 | 4,524 | 0 |
| | 1.6 | 0/3 | 0.871 | 1.22 | 9,586 | 0 |
| trunc K = 1000, R = 1.05 | 1.6 | 0/4 | 0.935 | 1.21 | 5,578 | 0 |

| Prediction | Result |
|---|---|
| Audit PC-1 (a): no C cell backlogs at max_open 20,000; nopen <= 12,000 | **Hit** (0 of 26 runs; largest nopen 11,178) |
| Audit PC-1 (b): softJ R = 1.111 and trunc R = 1.05 sustain 1.6 on HF's rule | **Miss** (0/4 and 0/4; both fail on q4/q1, 1.16 and 1.21: the open count is still rising at 20,000 generations) |
| Audit PC-1 (c): softJ K = 4000 k/lam 0.88-0.93, a coin-flip on the rule, no backlog | Partly: 0.894 at 0.8 is inside, 0.871 at 1.6 is just below; 0/3 and 0/3 on the rule, not a coin-flip; no backlog |
| Audit PC-1 (d): softJ R = 1.05 fails the rule on the fill lag (k/lam about 0.8), no backlog | **Hit** (0.78 and 0.75) |
| Day side, DA2 restated: K = 4000 sustains less than K = 1000 at R = 1.111, not explained by the fill lag | **Undecided.** At lam 0.8 K = 1000 passes 3/4 and K = 4000 passes 0/3, so the first half is met. The second half is not settled: k/lam falls with lam at both K (0.931 to 0.916; 0.894 to 0.871), tau exceeds the 5,000-generation burn in three of the four cells, and the long-burn series above show no K deficit up to lam 0.4 |
| Critic side: no K effect beyond the lag | **Undecided**, for the same reason |

What stage C settles: the main run's failures at nopen near 5,000 were the cap (with the cap at 20,000 the mean open count is 3,600 to 11,200 and no run fails on it). What it does not settle: whether lam 0.8 and 1.6 are sustained in the steady sense, because a 20,000-generation run with a 5,000-generation burn is too short when tau is 3,700 to 9,300 and the open count is still rising. The audit predicted that two of these cells would pass the rule and they did not. A long-burn run at lam 0.8 and 1.6 would decide it and has not been run. In every C run the realised rate over the window is at least 0.62 substitutions per generation (lowest cell mean 0.63).

**DA2 and PA4 by the letter.** With the cap released the two can be scored at this horizon: softJ lam_max at R = 1.111 is 0.8 at K = 1000 and 0.4 at K = 4000 (4/4 at 0.4 in stage L; 0/3 at 0.8 here). DA2 ("K = 4000 lam_max <= K = 1000 lam_max") **holds by the letter**; PA4 ("within one lam step") **holds**. The cause of the one-step difference is the undecided item above, so neither is evidence for or against a K effect on the limit.

### Stage M: mix boundary (s = 0.01, K = 1000, 8 runs per lam, 40,000 generations)

| h | R | lam50 at 20k (bracket) | x H8 hard cap at 10k / at 20k | lam50 at 40k | Runs passing the 20k rule, by lam |
|---|---|---|---|---|---|
| 0.1 | 1.111 | 0.0130 (0.0130, 0.0157) | 3.53 / 3.71 | 0.0130 | 7, 5, 4, 4, 2 of 8 at 0.0074, 0.0094, 0.0111, 0.0130, 0.0157 |
| 0.1 | 2 | 0.128 (0.119, 0.141) | 3.53 / 4.27 | 0.1295 | 8, 7, 0, 0, 0 at 0.1, 0.119, 0.141, 0.168, 0.2 |
| 0.3 | 1.111 | 0.00575 (0.0049, 0.0064) | 1.56 / 1.64 | 0.0056 | 5, 7, 2, 1, 0 at 0.0037, 0.0049, 0.0064, 0.0084, 0.0111 |
| 0.3 | 2 | 0.0479 (0.0454, 0.0592) | 1.32 / 1.60 | 0.0518 | 7, 5, 0, 0, 0 at 0.0351, 0.0454, 0.0592, 0.0768, 0.1 |

| Prediction | Result |
|---|---|
| Day side (DA1 restated): h = 0.3 lam50(20k) <= 2x the 10k hard cap at both R | **Hit** (1.56x and 1.32x; the upper ends of the brackets are 1.74x and 1.63x) |
| Day side: h = 0.1 lam50(20k) < 3x the cap at R = 1.111 (< 0.0110) | **Miss** (0.0130, 3.53x) |
| Critic side (CA2 restated): h = 0.1 lam50(20k) >= 3x the cap at R = 1.111 and at R = 2 | **Hit** at both (0.0130 >= 0.0110; 0.128 >= 0.109) |
| Audit PM1 [0.0094, 0.0135], PM2 [0.12, 0.18], PM3 [0.0045, 0.0090], PM4 [0.045, 0.090] | **Hit**, all four (PM1 and PM4 near an edge) |
| Audit PM5: the mean-field limit within 2x of lam50(20k) in all four | **Miss**: 1.21x and 0.90x at R = 1.111, but 2.27x and 2.005x at R = 2 (the mean field overstates the limit there; the miss rests on the 2.27, the 2.005 being inside the rounding of a two-digit prediction) |
| Audit PM6: lam50(40k) <= lam50(20k) in all four | **Miss** in two (h = 0.1, R = 2: 0.1295 against 0.128; h = 0.3, R = 2: 0.0518 against 0.0479). The brackets are the same at 20k and 40k in all four series; survival only falls, but more surviving runs meet the rate criterion over the longer window |

Limits of this stage, stated for both sides. At h = 0.1, R = 1.111 the boundary is wide at eight runs: the passing share is 5/8 at 2.55x the cap and 4/8 at both 3.0x and 3.5x, so the critic-side hit and the Day-side miss there both rest on a share at the 50% line (4 of 8 has a 95% interval of about 16-84%). At R = 2 the boundary is sharp (7/8 at 0.119, 0/8 at 0.141) and the same conclusion does not depend on a tie. h is the audit's parameter (the share of the log-load expressed as density-independent survival at fixed R, with no density compensation); it has no field estimator and no author's value.

### Stage N: truncation on a noisy phenotype (K = 1000, 80,000 generations, 40,000 burn; g = genotypic share of the variance of the truncation variable)

| R | g | HF rule at lam 0.0351 ... 1.6 | lam_max | x Term 3 | nopen at 1.6 | tau at 0.0351 / 1.6 |
|---|---|---|---|---|---|---|
| 1.111 | 1 | 4/4 at every lam | 1.6+ | >= 231 | 2,179 | 94 / 1,360 |
| 1.111 | 0.5 | 4/4 except 3/4 at 0.1 | 1.6+ | >= 231 | 3,565 | 110 / 2,227 |
| 1.111 | 0.1 | 4/4 at every lam | 1.6+ | >= 231 | 11,754 | 296 / 7,374 |
| 2 | 1 | 4/4 at every lam | 1.6+ | >= 35 | 195 | 15 / 122 |
| 2 | 0.5 | 4/4 at every lam | 1.6+ | >= 35 | 305 | 17 / 191 |
| 2 | 0.1 | 4/4 at every lam | 1.6+ | >= 35 | 1,114 | 31 / 696 |

| Prediction | Result |
|---|---|
| Day side (steelman-day #2; DB1 for phenotypic truncation): at g = 0.1 lam_max <= 1.25x Term 3 | **Miss** (1.6 sustained 4/4 at both R; 1.6 is the grid top) |
| Critic side: at g = 0.1 lam_max >= 5x Term 3 at both R | **Hit** |
| Audit PN1: g = 1 reproduces HF trunc (lam_max 1.6+; nopen within 25% of `hf_main`) | **Hit** (R = 1.111: 3, 13, 43, 158, 593, 2,179 against 3, 13, 43, 160, 579, 2,162; R = 2: 1, 2, 5, 14, 52, 195 against 1, 2, 4, 14, 51, 194, the 5 against 4 being a rounding of small counts) |
| Audit PN2: R = 2, lam_max 1.6+ at g = 0.5 and 0.1 | **Hit** |
| Audit PN3: R = 1.111, lam_max 1.6+ at g = 0.5; at g = 0.1 lam_max 0.8 with 1.6 failing by backlog | **Miss** on the second half: 1.6 is sustained at g = 0.1 with nopen 11,754, about half the 21,760 the audit's mean field predicted (the open count grows about 5.4-fold from g = 1 to g = 0.1, not 10-fold) |
| Audit PN4: tau(g = 0.1) / tau(g = 1) in [3, 20] at every sustained lam | **Miss** at one point (R = 2, lam 0.0351: 2.07); 3.01 to 6.2 at the other eleven |

Standing condition, from the docstring and from review item Day-1: truncation in this model keeps N = K in every generation at every g. It cannot go extinct, so stage N measures sweep speed and backlog and charges no demographic cost. The result says that adding phenotypic noise down to a genotypic share of 0.1 does not bring the truncation rate near Term 3; it does not say a real population could pay for it.

**Correction to the fix pass (C2).** "tau nearly flat in lam" is true of softJ (stage L, within 5%) and false of truncation: at g = 1, R = 1.111, tau rises from 94 to 1,360 generations between lam 0.0351 and 1.6, and the open count grows roughly as lam squared (as the stage N mean field in the docstring has it). The C2 sentence is restricted to softJ.

### Review items closed by `ph`

| Item | Closed as |
|---|---|
| C1 (mix midpoints) | Stage M boundaries replace the midpoints and the earlier brackets: h = 0.1 about 3.5x the 10k hard cap at both R (brackets 3.5-4.3x and 3.3-3.9x); h = 0.3 about 1.6x and 1.3x (brackets 1.3-1.7x and 1.25-1.6x). CA2 holds at both R (at R = 1.111 on a 4-of-8 share); the audit gloss DA1 holds at h = 0.3 and fails at h = 0.1; PA2's h = 0.3 rows are no longer indeterminate (0.00575 in [0.004, 0.012]; 0.0479 in [0.04, 0.12], scored here at 20k, post hoc) |
| C2 (max_open censoring) | The cap was the cause of the main run's failures near nopen 5,000 (no backlog in 26 runs at 20,000). Restated: softJ R = 1.111, K = 1000 sustains 0.8 on the rule (3/4); 1.6 is not shown at this horizon (0/4, k/lam 0.916, still filling). softJ K = 4000 sustains 0.4 (stage L); 0.8 and 1.6 not shown at this horizon. trunc R = 1.05: >= 0.8 stands; 1.6 not shown at this horizon (k/lam 0.935). DA2 and PA4 hold by the letter; their cause is undecided |
| C5; C, flagged burn-in artefact; Critic-5 | Fill lag, confirmed (stage L: 80 of 80 runs pass HF's rule). PA1 at R = 1.05 holds at the top of its band (0.4 sustained; 0.8 not shown at the short horizon). PA5's softJ part fails upward (weak-s softJ sustains 0.4, the top of the L grid, at R = 2; predicted 0.1-0.2). K = 4000 softJ at R = 1.111 passes to 0.4 |
| Critic-1 (h = 0.3 numbers were floor ties and noise) | Replaced by eight-run boundaries with brackets (stage M). "Within 1-3x" becomes "about 1.3-1.6x (brackets 1.25-1.74x)" |
| Day-2 (truncation was noise-free genotype truncation) | Extended to phenotypic truncation with genotypic share 1, 0.5 and 0.1 (stage N), under the standing condition N = K |
| Day-4 (weight of both halves) | Unchanged in substance, numbers updated: "near the hard cap for h >= 0.3 (about 1.3-1.6x); a few-fold above it at h = 0.1 (about 3.5x); uncapped in-model only at h = 0" |

### Verdict text after `ph` (proposals for integration; no verdict value changes)

- **H (Day, 1/300). External: contested**, with the h-scope now: "the cap binds for hard selection; at h = 0.3 the sustainable rate is about 1.3-1.6x the hard cap (R = 1.111 and 2, K = 1000, s = 0.01; brackets 1.25-1.74x); at h = 0.1 about 3.5x (brackets 3.3-4.3x); with purely relative fitness, or truncation that holds N = K, there is no cap in-model". The rest of the provisional H text stands (h and R unsourced; PC3 at R = 1.111; latency against throughput, C4).
- **H8 (Day, Z19984826).** s3.3.1 on s_max: internal holds, unchanged. Term 3 as a rate bound across mechanisms: **external contested**, unchanged. The sentence "Phenotypic truncation: pending stage N" becomes: "contradicted in-model for truncation on a phenotype with a genotypic share of the truncation variable down to 0.1 (K = 1000, R = 1.111 and 2, lam to 1.6), under the condition that truncation holds N = K and cannot go extinct; supported for hard selection and for h >= 0.3".
- **H5 (Hössjer).** As H.
- Drift Deathmarch and HO-11: not touched by `ph`.

### Who this helps (`ph` only)

- **Day side.** A modest hard component restores a limit near Haldane's: at h = 0.3 the sustainable rate is within 1.3-1.6x of the hard cap at both R, on eight runs per point (DA1 restated holds there). The cost per substitution is still not reduced in any soft or truncation arm, only not charged (Day-1 stands; stage N cannot go extinct by construction). Sweep residence time grows with the number of concurrent sweeps and with K. Two audit predictions that favoured the critic-side reading missed (PC-1 (b): 1.6 not sustained on the rule at the 20k horizon; PM5: the mean field overstates the limit at R = 2).
- **Critic side.** The softJ "failures" Day's side could have cited were a fill lag (80 of 80 long-burn runs pass). Ten per cent hardness leaves about 3.5x the hard cap at both R (CA2 restated holds). Truncation keeps its rate when the phenotype is mostly noise (genotypic share 0.1: 1.6 per generation sustained at both R, against a Day-side prediction of failure at 0.0351 and an audit prediction of a backlog at 1.6, both missed).
- **Both.** The answer still turns on h and R, which no source fixes. Nothing in `ph` moves a verdict value; it replaces brackets with measured boundaries and removes one artefact.

### Open after `ph` (none run)

1. A long-burn run of softJ and trunc at lam 0.8 and 1.6 (K = 1000 and 4000), to decide the DA2 item and whether 1.6 is sustained.
2. More runs at h = 0.1, R = 1.111 between 0.0094 and 0.0157 (the 4-of-8 tie).
3. A synergy arm under relative fitness (Critic-2), a density-compensating mix arm (Critic-4), and a sourced h for humans (queue item L2).

### Review resolution for `ph` (fix pass, 2026-10-13)

Review: `REVIEW-R4-HF-ph-combined.md` (e1d0ad0; 0 BLOCKER, 2 MAJOR, 9 MINOR, 8 NOTE). The reviewer found every table number equal to `raw/hf_ph_analyse.out`, the per-run counts equal to `raw/hf_ph.jsonl`, and no hit or miss call wrong. Number corrections were made in place above (C1, C5, C6, C7); wording corrections are stated here and **override the text above where they differ**. One new computation, on the traces already recorded, is labelled post hoc.

**MAJOR**

- **D1 (the h = 0.1, R = 1.111 boundary rests on a 4-of-8 tie, and survival is still falling). Accepted.** The registered estimator takes the last lam with a passing share of at least 50%, which gives 0.0130 (3.53x). The share is 5/8 at 0.0094, 4/8 at 0.0111 and 4/8 at 0.0130, so a strict "more than half" reading gives 0.0094 (2.55x), and under it CA2 misses and the Day-side prediction hits at R = 1.111. Runs alive at 0.0130 are 7, 6 and 4 of 8 at 10k, 20k and 40k. Both calls at R = 1.111 are therefore **marginal**: scored as registered (CA2 hit, Day side miss), and reported as depending on the tie convention. At R = 2 the boundary is sharp and the calls stand. Everywhere above and in the verdict text, "about 3.5x at both R" is replaced by **"about 2.6-3.5x at R = 1.111 (marginal, eight runs) and about 3.5x at R = 2 (sharp)"**.
- **D2 (the proposed H text dropped the Day-1 clause). Accepted.** "There is no cap in-model" is replaced, in H and in H8, by the sentence the first fix pass made mandatory: **"with purely relative fitness, or truncation that holds N = K, the population cannot go extinct in this model, and the rate is limited only by sweep latency and the open-locus cap"**, with the measured figures beside it: residence time 4,300 to 9,300 generations for softJ, and 3,600 to 11,800 loci open at once at lam 0.8 to 1.6.

**MINOR**

- **C1. Fixed in place.** The PN4 miss rests on one point (2.07); the value at lam 0.1 is 3.01, inside the band.
- **C2 (the cap was the cause of the failure label only). Accepted.** With the cap at 20,000 no run fails on it, but no lam_max moved: softJ R = 1.111, K = 1000 stays at 0.8 and trunc R = 1.05 stays at 0.8 on the rule. softJ at lam 1.6 fails the rule narrowly (q4/q1 1.151 to 1.167 against 1.15). The closure row should read "the cap produced the failure label; the rule outcome is unchanged at this horizon".
- **C3 (PA4 scored on softJ only). Accepted.** No K = 4000 truncation cell is in `ph`. The truncation half of PA4 is carried from the main run (1.6+ at both K).
- **C4 (verdict words reused for sub-scopes). Accepted.** In the H8 sentence, "contradicted in-model for" and "supported for" become "does not hold in-model for" and "holds in-model for", so that the claim-file word `contested` is the only verdict word.
- **D3 (restated DA2 scored more strictly than the letter of DA2 and PA4). Accepted in part.** The registered discriminator, "k/lam falling with lam", is met at K = 4000 and also at K = 1000, so it cannot separate a K effect from the lag; "undecided" was the right call on the registered test. The trace analysis below now speaks to it.
- **D4 (Term 3 at h = 0.3 not reported). Accepted; added to the Day side.** Against Term 3 (0.00693 at R = 1.111, 0.0456 at R = 2) the h = 0.3 boundary is 0.83x and 1.05x: **Term 3 holds as a rate bound in-model when 30% of selection is hard.** At h = 0.1 the boundary is 1.9x and 2.8x Term 3.
- **K1 (the headline ratio was the smallest available). Accepted.** h = 0.3: 1.3-1.6x against the 10k cap (the registered comparison), 1.6x at both R like for like (20k boundary against the 20k cap), up to 1.7x at 40k. The headline becomes **"about 1.3-1.7x"**. h = 0.1: 3.5x against the 10k cap, 3.7-4.3x against the 20k cap.
- **K2 (the traces can test convergence without a new run). Done, below.**
- **K3 ("near Haldane's" is true only at R = 1.111). Accepted.** The statement is "within about 1.3-1.7x of the H8 hard cap at the same R". That cap is near 1/300 only at R = 1.111 (the h = 0.3 boundary is about 1.7x 1/300 there); at R = 2 the hard cap is itself about 11x 1/300 and the h = 0.3 boundary about 14x. R is unsourced (V17).

**NOTE items carried into the text.** D5: the 10k cap is the comparison that gives the smaller multiples; it was the registered one. D6: in stage N the measured cost per substitution rises with noise (D at lam 1.6, R = 1.111: 18.3 at g = 1, 31.1 at g = 0.5, 114.7 at g = 0.1, against about 16 under hard selection); truncation on a noisy phenotype sustains the rate by not charging a cost that grows about six-fold, which strengthens the standing condition. K4: at g = 0.1, R = 1.111, lam 1.6 the open count is 11,754 against a cap of 20,000, so a genotypic share below 0.1 would probably hit the cap; "down to 0.1" is the limit of what was tested. K5: the 20k rule is noisy at small open counts and biases lam50(20k) low, toward Day's side (h = 0.3, R = 2, lam 0.0454: 8 of 8 alive throughout, 5 of 8 on the 20k rule, 8 of 8 on the 40k rule).

**Post hoc, descriptive (K2, D3): the late window of the stage C runs.** From the traces in `raw/hf_ph.jsonl` (every 250 generations), cell means over runs; no new simulation.

| Cell | lam | k/lam over the last 5,000 generations | change in open count over the last 2,500 | open count at the end | lam x tau from stage L at lam 0.4 |
|---|---|---|---|---|---|
| softJ K = 1000, R = 1.05 | 0.8 | 0.931 | +2.1% | 6,037 | 5,908 |
| | 1.6 | 0.896 | +2.4% | 13,081 | 11,816 |
| softJ K = 1000, R = 1.111 | 0.8 | 0.990 | +0.4% | 3,748 | 3,606 |
| | 1.6 | 0.981 | +0.6% | 7,985 | 7,213 |
| softJ K = 4000, R = 1.111 | 0.8 | 0.991 | +0.3% | 4,737 | 4,554 |
| | 1.6 | 0.981 | -0.1% | 10,260 | 9,109 |
| trunc K = 1000, R = 1.05 | 1.6 | 0.986 | +1.8% | 6,052 | n/a |

Reading. At R = 1.111 the runs have nearly converged by generation 20,000: the rate over the last quarter is 98-99% of the supply and the open count has stopped rising. K = 4000 and K = 1000 are then the same to the third decimal (0.991 against 0.990; 0.981 against 0.981). On this evidence **the one-step difference in lam_max between K = 4000 and K = 1000 is the fill lag, and there is no K effect on the sustained rate up to lam 1.6**; the critic-side prediction for stage C is supported and restated DA2 is not, both post hoc and descriptive, with DA2 and PA4 still holding by the letter of their registered wording. At R = 1.05 the runs have not converged (0.90-0.93, open count still rising 2% per 2,500 generations), so 0.8 and 1.6 remain not shown there. Recorded for Day's side: the open count at the end exceeds lam x tau from the low-lam long-burn series by 4-13%, so residence time keeps rising with the number of concurrent sweeps; the latency limit is real and grows with lam.

**Verdict text after the fix pass (replaces "Verdict text after `ph`" where they differ; no verdict value changes).**

- **H (Day, 1/300). External: contested.** h-scope: "the cap binds for hard selection; at h = 0.3 the sustainable rate is about 1.3-1.7x the H8 hard cap at the same R (and within about 1.05x of Term 3); at h = 0.1 it is about 2.6-3.5x at R = 1.111 (marginal) and about 3.5x at R = 2; with purely relative fitness, or truncation that holds N = K, the population cannot go extinct in this model, and the rate is limited only by sweep latency and the open-locus cap". h and R have no source.
- **H8 (Day, Z19984826).** s3.3.1 on s_max: internal holds. Term 3 as a rate bound across mechanisms: **external contested**; it holds in-model for hard selection and at h = 0.3, and does not hold in-model at h = 0.1 (about 1.9-2.8x), for purely relative fitness, or for truncation on a phenotype with genotypic share down to 0.1, the last two under the condition that the population cannot go extinct and the cost per substitution is not charged (and under noisy truncation rises about six-fold).
- **H5 (Hössjer).** As H.
