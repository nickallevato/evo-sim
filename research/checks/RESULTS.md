# Check Results Log (THROWAWAY research checks)

Each entry lists: the script, its seed, what was predicted before the run, what came out, and the review status. A result counts only after it passes review (see `REVIEW.md`).

Run any script with:
```
research/.venv/bin/python -I research/checks/<script>.py
```
Each script adds its own directory to `sys.path`, so `-I` works from any directory. (Fixed after review #2.)

## B0 — Textbook baselines · `baseline_textbook.py` (seed 20261007) · ALL PASS
| Check | Simulated | Target | z |
|---|---|---|---|
| B0.1 neutral P_fix, N=50 | 0.009893 | 0.01 | −0.69 |
| B0.1 neutral P_fix, N=200 | 0.00246 | 0.0025 | −0.51 |
| B0.2 conditional mean t_fix / N, N=50 | 3.908 | 3.980 (diffusion at p=1/2N; exact chain 3.935) | −2.15 |
| B0.2 conditional mean t_fix / N, N=200 | 4.006 | 3.995 | +0.16 |
| SD of t_fix / N | 2.105, 2.108 | ≈2.15 (diffusion) | — |
| B0.3 Kimura u, N=100, s=0.01 | 0.019995 | 0.020171 | −0.56 |
| B0.3 Kimura u, N=500, s=0.01 | 0.019745 | 0.019801 | −0.18 |
| B0.3 Kimura u, N=1000, s=0.005 | 0.010225 | 0.009950 | +1.22 |
| B0.5 neutral k at equilibrium, N=50 | 0.05018 | U=0.05 | +0.13 |
| B0.5 neutral k at equilibrium, N=200 | 0.04964 | U=0.05 | −0.64 |

**Notes**
- Review #2 corrected the B0.2 target from a flat 4N to the diffusion value at p=1/(2N). Against the exact chain (3.935N) the N=50 z is about −0.8. Resolved.
- B0.5 holds at both N values, consistent with k = U for any N.

## B0.4 / F — Fixation time of a beneficial mutant · `beneficial_fix_time.py` (seed 7)
**Prediction:** simulated t_fix ≈ the Kimura–Ohta diffusion integral (tolerance 5%), and Day's (2/s)ln(2N) overshoots both.

**Result:** confirmed. Simulation and diffusion agree within the 5% tolerance (SE ≈ 0.4–0.7%; review #2 also checked against the exact chain). (2/s)ln(2N) overshoots by 1.6–2.2× across the tested range.

*Correction (review #2):* the stochastic asymptote is (2/s)(ln(**4**Ns)+γ), not ln(2Ns). The column below uses the corrected form.

| N | s | 2Ns | sim | diffusion | (2/s)ln2N | (2/s)(ln4Ns+γ) |
|---|---|---|---|---|---|---|
| 500 | 0.01 | 10 | 698±3 | 703 | 1382 | 715 |
| 1000 | 0.005 | 10 | 1405±9 | 1407 | 3040 | 1429 |
| 2500 | 0.01 | 50 | 1043±6 | 1033 | 1703 | 1036 |
| 5000 | 0.01 | 100 | 1177±7 | 1173 | 1842 | 1175 |
| **10⁴ (Day's)** | **0.001** | **20** | — | **8,480** | **19,807** | 8,532 |

**Interpretation**
- **Fidelity:** (2/s)ln(2N) is a standard deterministic sweep-time approximation, so Day uses it legitimately. It does, however, overstate the mean time of an allele *conditioned on fixing* by about 2.3× at his parameters.
- **Scope:** this number is a *latency*, the time for one allele to fix. Whether latency limits *throughput*, the number of fixations per unit time, is a separate question; see B1 and F1.
- **Input dispute:** separately, Day's s = 0.001 comes from Zeng 2021. Per the pass-1 fidelity ledger that paper estimates negative selection, not beneficial effects. Pending verbatim check.

## B1 — Empty vs full "pipeline" · `b1_start_state.py` (seed 11)
**Setup:** N=100, U=0.5 per generation, 60 replicates, T up to 20N.

**Predictions**
- **P1:** with an empty start, the simulation matches U∫F_X, which is Day's formula, approaching U(T−4N).
- **P2:** with an equilibrium start, the simulation matches U·T.

**Result:** both predictions confirmed at every T.

| T | U·T | Day: U∫F_X | Empty start (sim) | Equilibrium start (sim) |
|---|---|---|---|---|
| 200 | 100 | 2.6 | 2.8 ± 0.2 | 99.3 ± 1.5 |
| 400 | 200 | 41.6 | 41.3 ± 0.8 | 198.5 ± 2.0 |
| 1000 | 500 | 304.5 | 304.4 ± 1.8 | 501.0 ± 3.3 |
| 2000 | 1000 | 802.7 | 802.5 ± 3.4 | 1005.1 ± 4.3 |

**Interpretation**
- *Review #2 note:* the empty-start simulation is Poisson thinning of independent trajectories, so it matches U∫F by construction. It verifies the code, not anything deep about Day's claim. The two vacuous grid points (T ≤ 100) were removed, and burn-in was raised to 20N.
- **Internal validity of Day's E[F(T)]: HOLDS** as mathematics. For an empty starting population his formula is exact.
- **Caveat:** an empty pipeline means zero standing heterozygosity. That contradicts observed human diversity, so the empty start is a *counterfactual boundary case*, not a realistic scenario. This framing came from steelman review C1.
- **The key question is external:** was the ancestral population's pipeline empty or full at the split? The standard view is that it was full, because the ancestor was a long-standing population.
- **Day's strongest remaining argument** would be that demographic change partially emptied the pipeline. → New sub-check **B1b**: test bottleneck and expansion histories.

## B3 — N vs Nₑ · `b3_N_vs_Ne.py` (seed 13)
**Setup:** exchangeable Cannings model, M=400 gene copies, 10⁶ replicates. Nₑ is lowered by raising the variance in offspring number.

**Predictions**
- **P1:** P_fix = 1/M for every Nₑ.
- **P2:** t_fix scales with Nₑ.

**Result:** both predictions confirmed.

| Variance σ² | Nₑ | P_fix (sim) | 1/(2N) | Day: 1/(2Nₑ) | t_fix / Nₑ |
|---|---|---|---|---|---|
| 1.00 | 200 | 0.00250 | 0.00250 | 0.00249 | 3.98 |
| 1.25 | 160 | 0.00252 (z=+0.50) | 0.00250 | 0.00312 | 3.95±0.04 |
| 1.99 | 100 | 0.00257 (z=+1.34) | 0.00250 | 0.00498 | 3.97±0.04 |
| 4.94 | 40 | 0.00248 | 0.00250 | 0.01235 | 4.01 |
| 10.70 | 19 | 0.00257 | 0.00250 | 0.02676 | 4.07 |

**Interpretation**
- **Day is right on time:** Nₑ sets the *timescale* of fixation.
- *Review #2 note:* in this model P_fix = 1/M is a theorem (allele frequency is a martingale), so the simulation verifies the code and illustrates the theorem.
- **Day is wrong on probability (provisional, pending verbatim quotes and B3b):** in an exchangeable model, Nₑ does not set the fixation *probability*. So k = μN/Nₑ fails *in this model class*.

**Open fairness sub-check B3b.** Day's k = 0.743μ invokes Balloux & Lehmann 2012: fluctuating N combined with overlapping generations. That is a non-exchangeable, time-varying setting, where the neutral rate *can* differ from μ per generation. B3b must test that setting before B3 receives a final verdict.

## B2a — Hard Limits tail exp(−π²Nₑ/G) · `b2a_hard_limits_chain.py` (exact WF Markov chain, no randomness)
**Prediction:** Day's exponent is the correct leading-order short-time asymptotic. From the arcsine transform y=arccos(1−2p) (variance 1/(2N) per generation, path length π), (G/N)·ln F_cond → −π².

**Result.** The exponent is **consistent with −π²**. Review #3 took the right limit order: N → ∞ at fixed r = G/N first, then r → 0. Values of r·ln F_cond at N = 100 / 400 / 1600:

| r = G/N | N = 100 | N = 400 | N = 1600 | limit |
|---|---|---|---|---|
| 0.25 | −7.75 | −8.19 | −8.33 | ≈ −8.4 |
| 0.5 | −7.03 | −7.31 | −7.40 | ≈ −7.45 |
| 1 | −5.78 | −5.94 | −5.99 | ≈ −6.0 |

- **Fit:** ln F_cond ≈ −π²/r + 1.5·ln(1/r) + 3.9, i.e. a power-law prefactor of about 50·r^−1.5. Empirical fit, not derived analytically. Reproduced in-repo by `b2a_scaling.py` (N=1600 row: −8.33 / −7.40 / −5.99 vs fit −8.37 / −7.40 / −5.97).
- **Small-N rows:** the earlier G/N = 0.05 rows at small N (G = 10 generations) are dominated by discreteness and are disregarded.

**Numerical use depends on which probability Day means. The verbatim definition is UNVERIFIED (fetcher quote only).**
- *Reading 1: conditional on eventual fixation.* exp(−π²N/G) *understates* the true probability:

  | G/N | Exact (N=200) | Day | Exact / Day |
  |---|---|---|---|
  | 4 (his threshold) | 0.61 | 0.085 | 7× |
  | 1 | 2.8e−3 | 5.2e−5 | 54× |
  | 0.25 | 1.2e−14 | 7.2e−18 | 1.6e3× |

- *Reading 2: unconditional, per new mutation (= F_cond / 2N).* At G = 4N and N = 200: 0.61/400 = 1.5e−3, which is *smaller* than Day's 0.085. Under this reading Day overstates the probability at moderate G.
- **Fairness note:** Day presents it as an "of order" leading exponent. Judging it on prefactor accuracy, especially at G = 4Nₑ where e^(−π²/4) is not small, is harsher than its asymptotic framing warrants.

**Verdicts (provisional)**
- **Internal (exponent): HOLDS.**
- **Numerical:** depends on the reading; resolve from the verbatim text in R1p2.
- **Relevance:** whichever reading applies, it is a per-allele *latency* tail. The expected number of substitutions across all mutations is U∫F, which equals U·T at equilibrium (B1).

## F1 — Latency vs throughput · `f1_throughput.py` (seed 31)
**Setup:** N=1000, s=0.01, U_b=0.01. Independent loci, no interference, no cost of selection.

**Prediction:** the steady-state rate equals 2N·U_b·u(s), independent of latency.

**Result:**
- **Rate: confirmed.** Predicted 0.3960 per generation; simulated 0.3972 ± 0.0018.
- **Spacing vs latency:** t_fix = 847 generations, but G_f = 1/rate = 3 generations.
- **In-transit count, *computed, not measured*:** rate × t_fix ≈ 336 fixers. This is Little's law used as an identity; `track_transit` is unused. Measuring it directly is a TODO.

**Verdict.** As logic, dividing elapsed time by fixation latency is **not** a throughput bound. Without interference, many fixations are in flight at once, which is the critics' pipelining point.

**Caveats (review #3)**
- **Unrealistic regime.** The parameters (20 new beneficial mutations per generation, 0.4 substitutions per generation) are far above any realistic regime, and they dodge selective load and cost by construction. **This shows pipelining is *possible*, not that it is *feasible* at realistic parameters.** Feasibility is Day's actual argument, tested in F2 (interference) and H (cost of selection).
- **Strawman risk.** "Serial reading = T / latency" must be tied to a specific quote, from Day or from a critic's rendering of him, before it is attributed to anyone. Day explicitly says his LTEE G_f is a throughput measurement (blog 2026-10-01, per fetcher).

## B1b — Size changes from an equilibrium start · `b1b_demography.py` (seed 21; 7 min)
**Setup:** N0=500, U=0.2, 24 replicates, T = 3×4N0. Each value is window k / U.

**Predictions:**
- **Standard theory:** contraction gives a transient *excess*; expansion gives a transient *deficit* of about 4N_new generations; the long-run mean is k = U.
- **Day:** a deficit whenever N has not been constant for about 4Nₑ.

| Scenario | First window | Recovered by (approx., by eye from means) | Cumulative / U·T | Analytic 1 − 4ΔN/T |
|---|---|---|---|---|
| constant | 1.00 | — | 0.996 | 1 |
| bottleneck N0→N0/10 (N0/2 gens)→N0 | 3.82 | ~4–5 N0 | 0.999 | ≈1 (net ΔN=0) |
| contraction N0→N0/5 | 3.79 | ~1.5 N0 | 1.259 | 1.267 |
| expansion N0/5→N0 | 0.19 | ~5–6 N0 | 0.733 | 0.733 |
| expansion N0/5→5N0 | 0.03 | not within 12 N0 | 0.085 | (bound 4ΔN = 9.6 N0 > T; deficit saturates) |
| founder N0→10 (20 gens)→N0 | 2.69 | ~4–5 N0 | 0.996 | ≈1 |

**Analytic cross-check (review #3).** The cumulative excess or deficit ≈ U·4ΔN, independent of the simulation. Contraction predicts 1.267 (sim 1.259); expansion predicts 0.733 (sim 0.733).

**Interpretation**
- **Day's claim as stated is half right.**
  - *Right for expansions:* the substitution rate does lag below μ for about 4N_new generations.
  - *Wrong in sign for contractions and bottlenecks:* those produce an excess, or a net of about zero.
  - The mechanism is **standard theory**: the transient lag of the substitution rate after a size change. The pre-registration predicted it. It is not a novel result of Day's.
- **Observable caveat.** These are within-lineage *fixed substitutions*. The human–chimp *pairwise sequence divergence* is the mutations accumulated along both branches since coalescence (≈ 2μT + ancestral θ). That quantity does **not** depend on fixation latency or demography. A B1b deficit applies to fixed-difference counts only, not to raw divergence. Check **B4a** must do this accounting before B1b is applied to the human–chimp case.
- **Scale.** The net effect is bounded by 4ΔN/T. At human–chimp scales (T ≈ 250k generations, ancestral Nₑ possibly 5×10⁴–10⁵), the transient regime is *not* negligible a priori. That makes **B1c** load-bearing.
- **Open (B1c).** Use sourced Nₑ trajectories (PSMC/MSMC/ILS estimates), lineage by lineage, to determine which direction applied. Human history includes both an ancestral size change and recent growth. Nothing about direction is asserted here until B1c is sourced.

---
# R4 batch (2026-10-08) — B1c, B4a, B3b/B3c, C1, C1b, H, H2-hard, C2, F2, A-sim
Full write-ups (post-review numbers) are in `results/R4-*.md`; review #4 is summarised in `REVIEW.md`. Pre-registered predictions are in each script docstring. All numbers below are final, after review corrections.

## B1c — Sourced Nₑ histories · `b1c_ne_history.py` (seed 20261008; 150 reps; burn-in 20 N_sim) · claims B1c, B1, B1d, B5, B6
**Setup:** ancestral population at equilibrium (Yoo 2025 Nₑ,anc = 1.98e5 HCB or 1.32e5 HCG), then step histories to sourced modern Nₑ (Prado-Martinez 2013 Table 1: humans 13.1–16.2k, common chimp 30.9–61.8k, bonobo 11.9–23.8k; textbook 1e4; Takahata-like two-step). Window T = 252,000 generations. Scaling validated (N_anc_sim 500/1000/2000 agree within SE; constant controls 1.000).

**Result:** every step history gives an *excess*, K/UT = 1.9–4.0 (H1 at HCB 3.986 vs analytic 1+4ΔN/T = 3.984). The new-mutation component is 0.84 at Nₑ = 1e4, which equals Day's (T−4Nₑ)/T.

**Regime limits:** this is the B1b telescoping identity applied to step histories, not an independent empirical result. Yoo's Nₑ is a lifetime average. No PSMC trajectory was extracted (Table S5 not retrieved). K counts alleles that fix in both lineages, so it is not a difference count. Unlinked neutral sites only.

**Verdict:** the empty-start premise is contradicted, and Day withdrew it (B1d). Day's post-split formula is confirmed for new mutations.

## B4a — Two-lineage divergence · `b4a_two_lineage_ils.py` (seed 20261009; burn-in 20 N_sim) · claims B4a, B6, B6a, B6b, B5c, B5e
**Result:** d − 2μT = θ_anc within ~0.3% in every row, and msprime agrees. At T = 252k and μ = 1.2e-8:
- HCB node (1.98e5): d = 1.55–1.56%, about 25% above the observed 1.23%.
- Nₑ,anc = 1e4: d = 0.65%, about half the observed value (Day-side point).
- CSAC's 14–22% polymorphic share corresponds to the poly-but-diff column: 22–25% in config B (human 1e4 / chimp 4.6e4). No tension.
- Day's 2μ(T−4Nₑ) = 0.51% is below the simulated fixed differences (0.56–1.46%).

**Regime limits:** a 3-parameter fit (μ, T, Nₑ,anc). Yoo's own μ is not recorded, so the Nₑ,anc rescaling is open. ILS discordance and an outgroup were not run.

**Verdict:** the formula holds. The external fit is contested.

**Critic-side correction (Hancock B5c / Nesslig20 B5e):** on an SNV basis, 2 × 252,000 × 38.4 = 19.4M, which equals 2μT. So the observed ~35M ≈ 19M post-split + ~15M ancestral, and the "38M matches 35–40M" claims double-count. Hancock's retained 76 is an SV-inclusive event count. Nesslig20's basis is unstated.

## B3b / B3c — Balloux & Lehmann; RRME 0.743 · `b3b_overlap_fluctuation.py` (seeds 20261008+, 16 reps) · claims B3b, B3c, B3
**Result:**
- B&L eq. (3) was reproduced in 9 scenarios (all |z| < 1.6). Fluctuation without overlap gives k = μ.
- At human-like parameters (analytic eq. 3): symmetric cycles give −0.3% to −2%; one-way growth raises the arrival rate of eventual fixers by 1.38× (transient). The contrived range is 0.59–1.70.
- RRME's 0.743 depends on the window (0.868 at 2 cohorts → limit 0.598).
- A mutant born in cohort i fixes with probability 1/N_i (P_fix·M_i = 0.973–1.018), not 1/(2N_t). The opposite sign to B&L.

**Regime limits:** haploid model, uniform survival, no senescence. The per-generation-time normalisation is open (0.81–1.11; Lehmann 2014 not retrieved).

**Verdict:**
- B3b: the effect is real and supported qualitatively (credit to Day). Its size at human scale cannot give 0.743 or 32.3.
- B3c: mechanism falsified; 0.743 is a window artefact.

## C1 — 1240k ascertainment · `c1_ascertainment_sim.py` (exact chain; seed 20261009 for MC) · claims C, C1, C1a, C6
**Result** (Nₑ = 1e4, 280 generations):
- Expected events: from <50%, ~0; from 50–90%, 0.04 (v62) / 0.11 (v66). New-in-window fixations: 5e-151 per site.
- Sample-level newly-100% counts: 13.8k (D2) and 18.2k (D3) vs 17,806 observed (v62). v66 (3,469) is 3.8× below, unexplained.
- C1a's sign is right for the 10–90% bands (1.2–3.4× enrichment) but wrong for the ≥90% bands (5–30× suppression).
- The observed 1 and 3 completions exceed expectation at Nₑ = 1e4 (P = 2e-4) and match it at Nₑ ≈ 7k.

**Regime limits:** a single closed population, no admixture, assumed split time. The statistic is Z23046531's, **not** the 21-count (see C1b).

**Verdict:** C: the test does not discriminate. C1: supported. C1a: right in sign for its bands, immaterial.

## C1b — Day's binned 21-count · `c1b_day_binned_statistic.py` (SeedSequence 20261010; 20 reps × 13 configs × 16 readings) · claim C6
**Result:** the literal procedure gives 1.2e3–1.7e4 post-7000 BP events under neutral (Nₑ 7e3–2e4) and under Day's d = 0.45 model, against 21 observed. The model also misses Day's own bin profile: 7000–8000 BP ≈1,350 vs 4,497 observed; pre-7000 share 38–60% vs 99.86%. Admixture pulses change S by <15%.

**Regime limits:** per-bin genotyped fraction 1.0 or 0.3. Real old-bin call depth is far lower. The reviewer's 1-replicate direction test (coverage 0.3 → 0.01: S21 6,537 → 1,204; 121 if all bins are required) moves toward Day's profile but inflates the eligible count to 72–138k.

**Verdict:** not reproducible from the published procedure; cannot adjudicate. The C6 external verdict is `untestable` pending a call-depth model.

## H — Cost of selection · `h_cost_of_selection.py` (20261008), `h_nunney_gauss.py` (20261010), `h_nunney_gauss_lowR.py` (20261020+), `h_keightley_load.py` (20261009) · claims H, H1, H2, H5, H7, H8
**Results:**
- **Arithmetic:** 300 = 30/0.10, 487 and 41,068 all hold.
- **D values:** diploid D = 2 ln(1/p0) gives 92–278 generations for standing variation and ≈200 for a new mutation.
- **Term 3:** 0.0256/gen (1 per 39). Its same-basis ratio to Haldane + d is **17.1** (the earlier 7.7 was withdrawn).
- **Hössjer:** his 15,800 is 10.5× Haldane's own 1,500. It comes from rate scaling, not cost.
- **Nunney reconstruction** (EXPLORATORY: adjusted twice after seeing results; mutation timing fixed):
  - The M-dependence is reproduced.
  - The absolute values are not: R = 10 comes out 2–12× low; R = 2.2, M = 0.1 gives 170 vs ~300.
  - **Soft T50 exceeds hard T50 at equal supply in both models**, so "soft selection removes the cost" is not reproduced.
- **Keightley (U = 2.2):** hard selection needs ≥2e^U ≈ 18 offspring per female (extinct at Fmax ≤ 20; persists at 30 and 60). Soft selection persists throughout.

**Regime limits:** K = 500, 8–10 reps, no CI on T50, N/K not in the success criterion. Siler life tables were used.

**Verdict:**
- H: arithmetic holds; external contested.
- H1: supported (scope).
- H2: contested.
- H5: non-sequitur (cost step).
- H7: supported.
- H8: arithmetic holds.

## H2-hard — Hard-selection multilocus treadmill · `h2_hard_selection_multilocus.py` (seed 20261030) · claims H, Gc, H7, F2
**Setup:** haploid-equivalent, free recombination, imposed demand λ, ceiling fecundity f = min(R, K/N).

**Results:**
- Wherever the population persists, k = λ (R_int 0.9–1.1), up to ~260 open loci (λ = 0.4/gen, 120× 1/300).
- Selective deaths reach 46–86% in persisting populations.
- Extinction occurs when λD (+U) > ln R, with D ≈ ln M + 1 (7.0 vs 6.9).
- The flip lies 9–100× above 1/300 for R ≥ 1.3 (factor-2 brackets).

**Regime limits:**
- The tested grid has R ≥ 1.3 and haploid D ≈ 7. **Haldane's own regime (R ≈ 1.1, diploid D ≈ 20–30 → ≈1/300) is untested.**
- Ceiling regulation assumes compensatory fecundity.
- No linkage; λ is imposed.
- The pre-registration was edited after the V1 run.

**Verdict:** 10% is not a general bound; the cap is ln R / D. The literal 1/300 is *not supported* in the tested range, but it is not falsified. Extrapolated (not simulated): U = 2.2 hard load with R ≈ 10 brings the cap down to ≈1/300.

## C2 — Turnover coefficient d · `c2_overlap_vs_standard.py` (20261011), `c2_ratio_nonident.py` · claims C2, C2a, C2c, C2d, A4, A4a
**Results:**
- d = mean cumulative hazard at the age of mothers (0.789 vs 0.784).
- d·s is exact for hazard-scale s (V1, within 1.5%): a point for Day. For per-generation s the factor is 1 (V3/V4/V5 ratio 1.000).
- Day's formula gives d = −ln L for discrete generations.
- C2c's ratio is invariant for random locus pairs (an identity).
- d is not identifiable: Day's own s priors give d ∈ [0.481, 0.568].
- Table 1 is not reproduced with a Siler stand-in; the Coale-Demeny tables were not retrieved.

**Verdict:**
- A4 / C2a: hold for hazard-scale s.
- C2: non-sequitur as a fitted correction.
- C2c: contradicted.
- Externals contested, because which s scale the papers use was not retrieved.

## F2 / A-sim — Multi-locus interference; LTEE scaling · `f2_multilocus.py` (4242, crc32 seeds), `f2_fwdpy11.py` (777), `a_ltee_scaling.py` (20261008, crc32) · claims F2, F, G, Gc, A, A2, A2e, A5b, A5d, A5f
**Results** (soft selection, N = 1000, s = 0.01):
- Clonal R_int falls 0.645 → 0.088 over 2N·U_b 0.1 → 32.
- A 0.1 M map gives 0.204; one 1.5 M group gives 0.572.
- Free recombination gives 0.975 ± 0.005 at 272 active loci, linear in supply. fwdpy11 agrees.

**A-sim results** (LTEE, Nₑ = 3.3e7 **unsourced**):
- G_f ≈ 1,300 is reproducible, but U_b is underdetermined over 3 orders of magnitude.
- The asexual supply exponent is a = 0.23–0.34 per 100×.
- The free-recombination factor of 1.5–172× is an **extrapolation**.

**Regime limits:** ≤272 active loci, 2N·U_b ≤ 32, single s, soft selection, 4 reps. Human-scale active loci (~1e4–1e5) are untested.

**Verdict:**
- F2 / G / Gc: Day's cap is not reproduced in the tested regime; external contested.
- A5f: direction supported.
- A5b: linear only under free recombination.
- A5d: sublinear (asexual) confirmed.

## E — Founder hypermutation hazard; relictation · `e_founder_hazard.py`, `e4_relictation_chain.py` (exact chains; MC `SeedSequence([20261008, cfg])`) · claims E, E3, E4 · full write-up `results/R4-E.md`
**E / E3, founder hazard (N = 100, G = 50 unless stated):**
- The headline size reproduces; the route to it does not:
  - Day's P(≥2 carriers) is 0.0509, not 0.06, so his own product gives 2.00%.
  - 68% of the hazard comes from founders carrying a single copy.
  - His 39% conditional is a with-replacement Hardy–Weinberg artefact: exact 22.8% under drift, 15.9% with selection.
- **Day's model as written in the text** (selection on realized genotypes): 2.75% (second-seed MC 2.750 ± 0.037%), outside the claim file's pre-registered 2.33 ± 0.15% band. This is the falsifier firing.
- **With selection on HW-expected genotypes** (a textbook mean-field formulation): reproduces his Tables 2–5 within MC error. Exceptions: Table 2 N=500 at −4.2 SE and Table 3 N=500 at −3.1 SE. Table 8 is reproduced by neither formulation.
- **Population-level effect** (post hoc): depends on N and on the threshold. At N = 100, a mean-fitness dip below 0.99 / 0.98 / 0.97 / 0.95 is 1.15× / 6.4× / 31× / 619× rarer than ≥1 affected birth. At N = 20–30 the gap is 1–5×, because one affected birth is itself a 3–5% dip. Each hit averages about 2.5 affected births.
- **Isolate growth** (post hoc) raises the hazard from 2.75% to 9.0%.
- **6/12 LTEE mutators** confirmed in Tenaillon 2016 and Good 2017. Tenaillon reports a 7th, transposon-driven mutator.

**E4, relictation:** Day's mathematics reproduces exactly.
- His table matches to ≤ 0.0004; P_fix = 1/(2N) to 1e-13; large-N values 1.363 / 1.737 / 1.179 match.
- Growth with N needs family size ∝ N (the sweepstakes regime). For a fixed family size the excess shrinks (1.0445 → 1.0045).
- E4 changes the fixation time, never P_fix or k. It is the known multiple-merger result.
- The 10% threshold depends on N: 15% at 2N = 20, 2.5% at 2N = 1,600.
- One diploid two-parent construction (biased low) gives +2.9% where Day's one-copy chain gives +17.4%.
- keruru built the same chain on 2026-08-26.

**Predictions:** E P2, P5 and P6-split failed, as did E4 P8 equivalence and the claim file's opposing 1.2–1.3 convergence. The rest held.

**Reviews:** correctness, Day-side and critic-side steelman (`results/REVIEW-R4-E-*.md`); every MAJOR resolved in the fix pass.

**Verdict:**
- E: holds approximately; fidelity accurate; the bridge from per-event risk to a speciation hazard is untested, and Day defers it himself.
- E3: reproduces only under the mean-field formulation; "independently sufficient" and "minefields" overreach.
- E4: holds / accurate / external contested.

## G1 — Bernoulli Barrier: specific vs any outcome · `g1_specific_vs_any.py` (SeedSequence), post hoc `g1b_review_runs.py` · claims G, Ga, Gb, Gc, Gd, G1, G2*, G3*, G4* · full write-up `results/R4-G1.md`
**Arithmetic.** Every power reproduces: 0.02^(2×10⁷) = 10^−33,979,400; 0.5^157,000 = 10^−47,262; Darwillion 10^−86,020,600.
- 14.7 is 14.74 (additive) or 14.67 (log-fitness). Under the log reading, 107 is a valid ratio. The label "(1.01)^1474 ≈ 14.7×" is false as written (that power is 2.34×10⁶).
- ~230 sweeps is numerically identical to 157,000 × t_transit / T. No derivation is given.

**What each number prices.**
- 0.02^n (Ga) and the Darwillion price a *pre-specified list* of arisings. 0.5^157,000 (Gb) prices one genotype, which Day's own s7.10 says is not needed.
- p^n doesn't depend on timing, so it cannot force sequential fixation.
- Day's Gd (157,000 / 0.02 = 7.85M arisings) is itself an "any n of M" calculation.
- On the "specific" reading Day is right, even allowing recurrent mutation.

**The middle case:** functional but interchangeable, with n_f required changes each met by any of m alternatives.
- P(all achieved) jumps from ~0 to ~1 as λ = −m·ln(1−q) crosses 12.3–17.2. The 5–95% band is 4.07 wide.
- It applies only to the adaptive subset; neutral differences have no required function.
- m and the adaptive n_f are not established in the corpus. Branch D's estimates don't convert to per-site m.
- At n_f = 2×10⁷ and s = 0.001, the genome cannot supply enough alternatives for the flip (Day-favourable bound).

**Simulations** (soft selection; post-hoc parts labelled):
- **Free recombination:** joint fixation = 1.03 ± 0.02 × p², and the count is Poisson-like.
- **Linkage:** 0.84 at 0.05 M and 0.65 at 0.005 M (the pre-registered 1 M map was too loose to show it). Clonal: 0.
- **Multiplicative fitness** (Day's stated model): no cap near 230; 814 concurrent sweeps at 98% of the single-locus rate.
- **Additive fitness:** the dilution depends on an unstated convention.
  - If fixed alleles count: driven by total alleles carried, so a sequential chain is diluted more (0.40× vs 0.54× at 1,000).
  - If only segregating alleles count: concurrency-specific (0.85× at 230, 0.60× at 1,000).
  - Normalised effects: no dilution.
- **Reproductive excess:** best/mean ≈ 340 (N_eff ≈ 333) with 157,000 loci all at p = 0.5. It is ≈ 1.3 at Day's own 230-locus standing crop and 2.1 at s = 0.001.
- **Per-locus P_fix:** falls ~14% when var(ln w) is O(1).

**Predictions:** two failed. Linked-map interference did not show at 1 M, and effective parents came out at 355–432 against a predicted ~205. P6 failed as pre-registered and holds only in the post-hoc E2 run.

**Scope:** this does not test Day's current throughput argument (2026-09-30 / 10-01: parallel fixation is already inside G_f; the Barrier is moot in MITTENS 3.0).

**Reviews:** correctness, Day-side and critic-side steelman (`results/REVIEW-R4-G1-*.md`). The two steelmen's conflicts (additive dilution, reproductive excess) were settled by post-hoc runs.

**Verdict:**
- Ga and Gb: the arithmetic holds, but the event priced is not the one required. "Forces sequential" is a non-sequitur.
- G3b is an incomplete dilemma: the middle case is missing. Its "neutral ≠ functional" half is valid.
- Gc: no derivation.
- G2 / G2e / G2f hold against the serial p^n chain only, not against arithmetic built on the LTEE rate (G1).

## GAP-04 / GAP-07 / GAP-02 — Finite-map limit; indel/SV event counts; sweep detection window · `gap04_weissman_barton.py`, `gap07_event_counts.py`, `gap02_sweep_window.py` (deterministic; pre-registered at b812741), post hoc `gap04_posthoc_concurrency.py`, `gap0x_posthoc_review.py` · claims F2, A, A2e, Gc, A3, A3a, A3b, A3x, H, A6, A6a, ROOT-M · full write-up `results/R4-GAPS-04-07-02.md`
**Disclosure.** All 20 F2 cells were known before registration, so GAP-04 P1–P3 and P5 test formula forms and tolerances on known data. GAP-02's predictions are arithmetic consequences of its model. The only later change to a committed script is a cosmetic print-label fix in `gap04_weissman_barton.py`.

**GAP-04, Weissman & Barton 2012** (PLoS Genet 8:e1002740; equations read from the PDF):
- The cap is a bracket, not one number:
  - R/4 for an exponential DFE (Eq. 13);
  - R/2 for fixed s (Eq. 7);
  - simulations up to ~3R at Λ₀/R = 10³.
  - None depends on N or s. The brief's "R × log factor" is only a heuristic bound on growth above R/2.
- **F2 fit:**
  - 1.5 M map: Eq. 7 agrees within ~6–10% (c = 1.79 ± 0.03 vs 2).
  - Free recombination: Eq. 1 within 1.4 SE.
  - 0.1 M map: the form fails (observed rate 2.6 × R/2).
  - Clonal runs are out of domain.
- **Day's stated model** (MITTENS 3.0 §4.3/§8.2: every fixation sweep-carried). 17.5–20M per lineage is:
  - 3.3–4.5× over R/2 and 6.5–9.1× over R/4 (R = 35–38 M);
  - 0.54–0.76 of the simulated maximum, reachable only with a beneficial supply of order 1% to several hundred % of all new mutations (Fig. 4 read at s = 0.05; N_e- and s-dependent).
- **Critics' model:**
  - the asymptotes bind only above a 13–14% (R/4) or 25–27% (R/2) adaptive share;
  - interference costs ≤ 4.3% at K_a ≤ 10⁵ and 17–31% at 10⁶;
  - Day's own 99%-neutral 200,000 is 22–31× below R/2.
  - This is the interference leg only; the H2-hard cap (1,200–8,700) is exceeded by K_a ≥ 10⁴.
- **Magnitude:** R/2 per lineage is 1,800–25,000× MITTENS' achievable count.
- **Post hoc, concurrency:** the R/2 ceiling is 7.7–8.3×10³ concurrent active-zone sweeps at s = 0.01. At GAP-01 rates it is 1.7–1,744.

**GAP-07, event counts (k = μ):**
- Events per lineage, by route:
  - rate × time: 9.6–10.4M;
  - clock-free calibrated: 18.2–19.7M;
  - CSAC-observed basis: 20.0M (22.5M upper bound).
- 205M is ≈ 9–11× these; ≥ 8× at observation-consistent grid points; 5.3× at the extreme corner.
- CSAC's 5M indel events are a two-lineage total.
- SV base pairs under k = μ (0.35–0.92 Gb) match SDR base pairs only in order of magnitude; SDRs are mostly satellite and heterochromatin.
- A repeat-unit reading gives 21–30M at Yoo's satellite units.
- G_f counts events, so a base-pair numerator is a unit mismatch.

**GAP-02, detection window:**
- Expected detectable completed sweeps are power-1 upper bounds.
  - Day's stated 3,200 sweeps over 325,000 generations: ≈ 98 in the sourced ~10,000-generation window (Hernandez 2011).
  - Top of his own range (32,000; N_e 33,000): ~1,000–3,250.
- The cited scans are threshold-limited top-1% lists of mostly incomplete sweeps.
- Hernandez's trough test supports rarity of classic sweeps (< 10% of human-specific amino-acid substitutions strongly favoured).
- Bonobos: 326,000 selective sweeps would leave ~1.4–1.6×10⁵ detectable against Yoo's 30.

**Predictions:**
- GAP-04 P1 **failed** (strict 0.03 tolerance: 0.046 at one low-supply free cell, 1.4 SE). P2, P3, P5, P6, P7 and P8 held (P8's falsifier was set at the favourable N_e). P4 was not a test.
- GAP-07 P1–P5 held. P3's base-pair band is non-discriminating.
- GAP-02 P1–P6 held as arithmetic. P1's falsifier could not fail. P3's stated consequence ("tension with scans") is withdrawn.

**Reviews:** correctness (0 BLOCKER, 6 MAJOR, 11 MINOR), Day-side steelman (7 MAJOR, 7 MINOR) and critic-side steelman (7 MAJOR, 6 MINOR), in `results/REVIEW-R4-GAPS-*.md`. Every MAJOR was resolved in the fix pass. The main changes:
- a bracket in place of a single cap, with Day's model stated as his;
- "supply-infeasible" withdrawn;
- concurrency presented as a ceiling;
- the indel "undercount" and the "few large events" reading withdrawn;
- E_detect stated as an upper bound and scan lists marked illustrative;
- Day's full block and N_e ranges added.

The first pass's "gaps.md 4–16% should read 4–19%" was retracted (a different loss definition).

**Verdict:**
- **F2, A, A2e, Gc:** unchanged cells, new comments (two models; bracket; Gc "as a cap" vs "as a number").
- **A3x:** supported.
- **A3a:** external contested; "contradicted as an event count" is the alternative reading.
- **A3 and A3b:** magnitudes corroborated.
- **New claims:**
  - A6 (Z18452504 §4.3(4)): pending / partial / contested.
  - A6a (Z18441321 §3.1, bonobos): holds / n/a / supported, as against selective fixations.

## H3 — Cost of selection at human scale · `h3_human_scale.py` (pre-registered 0061b28), post hoc `h3_posthoc.py`, `h3_tables.py` (70d83cc, 872d8b1), `h3_fixpass.py` (e48a5af, 3688bcb; stages L/H/M/W/X on na-workhorse) · claims H, H1, H2, H5, H6, H7, H8, ROOT-M · full write-up `results/R4-H3-human.md`
**Model:** a hard-selection treadmill, where the environment makes the ancestral allele costly. Costs are log-additive across loci, with ceiling regulation, K = 1000 (4000 and 10⁴ for the load runs) and a 36.8 M map. Sustainable adaptive rate = φ·(ln R − U_hard)/D, where D ≈ 2 ln 2N (validated against K) and φ ≤ 1 is the shortfall from load fluctuations.

**Results (every one conditional):**
- **Shared budget (Day's structure, D1a): held.** Concurrent sweeps share one budget, and parallelism does not raise the total beyond it. The 10% is Haldane's assumed parameter (R ≈ 1.1); under ceiling regulation the budget is ln R.
- **R = 1.1:**
  - 10k-window λ50 = 0.00340 [0.00300, 0.00379] (≈ 1/300; circular in R by construction; needs a soft deleterious load);
  - fails over 40k;
  - long-run φ_252k = 0.30, i.e. ≈ 1/530–1/1,050 at D = 15–30 (s = 0.01). At s = 0.003 it is ≈ 1/230–1/460.
- **Long-run φ_252k** (s = 0.01): 0.30 / 0.57 / 0.59 / 0.73 at R = 1.1 / 1.5 / 2 / 3. At s = 0.003: 0.69 (R = 1.1), 0.94 (R = 2). At s = 0.001 the long run is unresolved.
- **Minimum R for K_a adaptive substitutions in 252,000 generations** (hard adaptive / soft load, D = 20, long-run φ): 1.22 (10³), 2.98 (10⁴), 5.4×10⁴ (10⁵), none (10⁶). With a whole-genome hard load (U = 2.2), multiply by ≈ 9. D = 5 (intermediate-frequency standing variation): 1.07 / 1.45 / 15 / 6.7×10¹¹.
- **Finite supply:** D ≈ 15 + 1/M at M ≤ 0.03 (39–163). At M = 0.01 even R = 2 sustains only ≈ 1/430.
- **Hard load:** U = 2.2 is incompatible with R ≤ 9 (analytic). R = 20 persists at K ≥ 4000, so the K = 1000 extinction was an artefact.
- **GAP-01 targets:**
  - Coding-only K_a (1.3×10³–1.2×10⁴) is payable at R ≈ 1.2–3.
  - a_nc ≈ 0.1% (2×10⁴) needs R ≈ 3–9.
  - a_nc ≥ 1% is unpayable at R ≤ 3–4 (the anchor range) for D ≥ 5.
  - The flip (a_nc ≈ 0.01–0.6%) is below the resolution of any α estimate, so it is **undetermined**.
- **Day's 17.5M–205M:** unpayable under any cost model, which is uninformative about A/B (branch B decides that).
- **Not modelled:** soft selection on the adaptive loci, absolute-fitness gain, truncation/synergistic epistasis.

**Predictions:**
- Held: S1, S2 (well-sampled cells), S7 (except 2Ns = 100, −23%), D1a, P-V.
- S3 is a marginal miss at R = 1.5.
- The λ50 parts of S4 could not be resolved; p_fix on the 36.8 M map failed marginally.
- S5 failed or was untestable at R = 1.5.
- S6 failed at M ≥ 0.1 and approximately held at M ≤ 0.03 (post hoc).
- D2 held in the 10k window if R = 2 is intended.
- D3 is cut to R ≤ 9.

**Reviews:** correctness (0 BLOCKER, 4 MAJOR, 11 MINOR), Day-side steelman (7 MAJOR, 5 MINOR) and critic-side steelman (6 MAJOR, 8 MINOR), in `results/REVIEW-R4-H3-*.md`. Every MAJOR was resolved in the fix pass:
- long-window runs;
- the low-M and hard-load-K runs;
- D1 split;
- R anchors;
- conditional verdicts;
- the "not modelled" table;
- credits (Hancock ×4, Nesslig20 → Matheson, keruru KR-09).

**Verdict:** every cell is unchanged, and the comments now state the condition.
- **H:** holds / partial / contested.
- **H1:** holds / n/a / supported, scoped to Term 3.
- **H2:** n/a / accurate / contested.
- **H5:** non-sequitur / pending / contested; the conditional is mechanically supported.
- **H6:** holds / partial / supported.
- **H7:** n/a / n/a / supported; these are bounding cases.
- **H8:** holds / pending / contested.
- **ROOT-M row 1:** pending / n/a / pending, now carrying its conditions.
