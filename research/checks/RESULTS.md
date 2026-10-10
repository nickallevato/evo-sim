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

**Regime limits:** per-bin genotyped fraction 1.0 or 0.3. Real old-bin call depth is far lower. (Corrected by C1c, 2026-10-09: measured mean depth is 49 / 62 / 282 chromosomes per site in the three oldest bins, so sparse calls are not the cause; C6 was then decided on C1d.) The reviewer's 1-replicate direction test (coverage 0.3 → 0.01: S21 6,537 → 1,204; 121 if all bins are required) moves toward Day's profile but inflates the eligible count to 72–138k.

**Verdict:** not reproducible from the published procedure; cannot adjudicate. The C6 external verdict is `untestable` pending a call-depth model. (Superseded 2026-10-09 by C1c and C1d: C6 external `contradicted` as stated.)

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

## GAP-07b — Direct count of human–chimp divergence events from a whole-genome alignment · `gap07b_alignment_count.py` (deterministic; pre-registered 3c847b8), post hoc `gap07b_posthoc_{blocks,polarize,ladder}.py` (c1727f0), `gap07b_posthoc_review.py` (3798b92), `gap07b_posthoc_review2.py` (fbbc580) · claims A3, A3a, A3b, A3c, A3d, A3x · full write-up `results/R4-GAP07b-alignment.md`

**Data.** UCSC hg38 vs panTro6 net, chain and axtNet, and hg38 vs gorGor6 axtNet as outgroup (md5s match UCSC). Primary chromosomes only. **Not T2T**: every ratio is for this pair of assemblies, which counts both lineages plus ancestral and within-species polymorphism.

**Measured (pre-registered main run).**
- 37.77M SNVs (Ts/Tv 2.05; divergence 1.35%); 4.30M indel events (chain gaps inside the net; 40.8% 1 bp, 48.4% 2–10 bp, 0.54% > 1 kb, largest 25.2 Mb); total 42.10M events, **21.05M per lineage**.
- SNV lineage split (gorilla outgroup, 95% polarizable): 48.6% human-derived. The indel split is consistent with 50/50 for events <= 50 bp only.
- Bases outside every aligned block: 261 Mb (201 Mb without hg38 centromere models); with aligned nested sequence 521 Mb.

**Ratio.** Day's 205M per lineage = **9.7× the measured events** (pre-registered quantity). Bracket about **7–14×** (all rows post hoc): Day-favourable 7.2–9.5 (non-aligned bases as 171/32-bp repeat units, indel slippage ×2–×3, non-T2T undercount); critic-favourable 10.1–13.4 (human lineage alone, top-level fills, <2%-divergent records, CSAC's 14–22% polymorphic share). Repeat masking gives 22–24×, a unique-sequence bound. **Events are not fixations, and events are not selected**: the ratio is the unit mismatch only.

**For Day.** His SNV-only 17.5M is 83% of measured events per lineage and brackets the polymorphism-corrected fixed events (16.4–18.1M); his SNV-only shortfall rises on the measured count (99,100–110,400 at G_f 1,322). The bp magnitude of non-1:1 sequence is the same order as 410M. His first-edition "40 million" was an events figure (42.1M measured). His stated position (04-28 ¶19; 05-13 ¶4–6) is a weighting claim with a range; as a weight, 205M needs ~3,250 SNV-equivalents per event above 50 bp (untested; his own G_f counts events). The k = μ rate route undershoots the measurement ~2× (the clock question, B4a / GAP-06).

**For the critics.** The unit argument (A3x) holds by direct count. Observation-based critic estimates land within 7–19% (McCarthy 22.5M, Mansfield 25M per lineage; Nesslig20 and Hancock ~38M total, −10% of events). CSAC's "5M indels" is a two-lineage total (4.30M measured).

**Errors recorded, both sides.** CSAC's ambiguous "in each species"; the audit's own 22.5M per-lineage upper bound (retired); A3x's 1,140 six-ape inversions (453 nested inversion fills >= 10 kb in the human–chimp net); the first-published 523M row double-counted 2.75M SNVs; critic slips RF-6, MF-03, PS-01, GG-11.

**Scorecard.** Held: indel total (3.5–6.5M), CSAC 5M a total, total events (33–45M), per lineage (16–23M), L3 bp/event 7–18 under all four filters, nested inversions 200–1,500. Missed: SNV total (37.8M vs 27–35M), raw gap bp, 2–10 bp share, > 1 kb count, repeat-masking sensitivity, unaligned shares (P8). The pre-registered indel polarization was asymmetric (33% human as run; a method artefact).

**Open.** GAP-07c (polymorphic share from population frequencies) and a T2T re-run (CHM13/hs1 vs mPanTro3). Reviews: `results/REVIEW-R4-GAP07b-*.md`; resolution in the write-up §14; `REVIEW.md` review #8.

## C1c — Day's aDNA 21 with real AADR call depth and an ancestry-replacement model · `c1c_call_depth_replacement.py` (pre-registered b128110), post hoc `c1c_posthoc_mindepth.py` (ee0b725), `c1c_posthoc_variant_gate.py` (9045329), `c1c_posthoc2_fixpass.py` (d2fe788) · claims C6, C, C1, C4, C5, C5b, C7 · full write-up `results/R4-C1c.md`

**Model.** Exact frequency-level Wright-Fisher, one pooled European population per bin, Anatolian and steppe pulses (R0 none to R3 strong), real per-bin call depth from the AADR v62.0.p1 anno (mean 49 / 62 / 282 chromosomes per site in the three oldest bins), Day's E1 eligibility and T2 dating; 44 base scenarios, 4 replicates.

**Result.** No cell reproduces Day's eligible count (22,428), profile, tracked fraction (0.727) and start table together. Post-6000 count S21: 1.5k–3.9k at constant N_e 1e4 (70–190x Day's 21); about 21 only at closed N_e ~1e5–3e5 or growth/step schedules to 1e5–1e6 (15–67); replacement raises it at high N_e (to ~40x, R3). Day's d = 0.45 gives 739. S21 / eligible is the density-robust number (Day 0.129%; error-free cells 0.5–27%). Matched capture (tracked 0.72–0.74) changes S21 by at most ~1.6x; the earlier "thousands" came from a design flaw (modern bin given capture heterogeneity) and is withdrawn.

**Reading.** Model-conditional and conditional on the Holocene N_e trajectory, which is not sourced in the repo (retrieval in progress): a deficit against neutral at N_e <= ~5e4 or strong replacement (Day); neutral-compatible at closed N_e >= ~1e5 or growth (critics). The 21-class events start at >= 95%, so the intermediate-start claim (C) is untouched. Reviews: `results/REVIEW-R4-C1c-*.md`; `REVIEW.md` review #9.

## C1d — Day's aDNA statistics on the real AADR genotypes; keruru's temporal N_e · `c1d_aadr_real.py` (pre-registered c0a4071), post hoc `c1d_posthoc.py` (814f5da, 982366c), `c1d_verify.py` (d308586), `c1d_posthoc2.py` (c09b957), `c1d_posthoc3_keruru.py` (5f0ba57), `c1d_posthoc4_tp.py` (3f70039), `c1d_figure.py` (6f43473) · claims C6, C7, C, C5a, C5b, B2e, C4 · full write-up `results/R4-C1d.md`

**Data.** AADR v62.0.p1 and v66.p1 1240K genotypes (TGENO), md5-verified, downloaded and processed on na-workhorse only. Day's European sample rebuilt (8,808 vs his 8,738).

**Day's 11-bin statistic.** Literal reading (E1, T2): 62,757 eligible / 4,957 events dated 5000–6000 BP or younger (v62), 48,888 / 3,649 (v66), against 22,428 / 21; 84% of the 4,957 in 0–500 BP. 132 grid cells do not close the gap. Start table reproduces to 0.4 points on v62 (credit to Day). 97.7% of the post-6000 events are transitions; a library-type test with matched random controls shows the excess is not specific to damage-prone libraries (so not damage); transversions alone give 36–44 on autosomes (0.57% per eligible allele vs Day's 0.094%; neutral comparison open).

**Day's two-period pipeline (Z23046531).** Sample (1,377 / 683 vs 1,372 / 680) and SNP count (1,143,870 vs 1,143,671) reproduce; completions from MAF >= 10% reproduce in kind (2 and 0 vs 1 and 3); the event total does not (63,631 vs 17,814, 3.6x). No code was found (Zenodo, GitHub, OSF, the saved blog corpus); the promise is in Z23046531 and may mean on request.

**keruru (B2e, C5b).** His temporal N_e replicates within 1–8% (7,812 / 9,672 vs 8,139 / 9,835); his pseudo-haploid sampling term is half the standard one (corrected 9.7k / 10.5k; a slip-ledger item). The estimate is a lower bound on a drift N_e. Against Wright's formula: 5.9x at census 1e5, 59x at 1e6, 591x at 1e7 (break-even ~17k); composition explains 6–17% of the F. "Three orders" is not established at the unsourced 1e7; a >= 6x gap survives at any census >= 1e5. Day's N_e near 2 is excluded.

**Verdicts.** C6 external **contradicted** as stated (best Day reading "underspecified"; reopens as contested if a pipeline is documented); C7 external **contradicted** for "no allele-frequency movement" (drift attribution open); C5b holds (slip ledger) / supported; B2e contested. Reviews: `results/REVIEW-R4-C1d-*.md`; `REVIEW.md` review #10.

## D1 — Sequence-space spike: alternatives per needed change · `d1_sequence_space_spike.py` (pre-registered d72c733; ViennaRNA 2.7.2), post hoc `d1_posthoc_refine.py` (88dda5a), `d1_posthoc_gb1_snv.py`, `d1_aggregate.py`, fix-pass scripts (40d9261, e92de84) · claims D, D1a, D1b, D1d, D2c, D2h, D2i, D3, D4, D9a, D10–D12, G3b · full write-up `results/R4-D1-spike.md`

**What it measures.** G1's open number: interchangeable alternatives per needed change, against the flip λ_50 = 7–17 (λ = 0.48 m at s = 0.01, linear in s). Stand-ins: RNA folding (ViennaRNA) and 114 non-stability ProteinGym DMS sets plus the complete GB1 four-site landscape. Shown along an axis of readings (H1 Day's specific horn, H2 tolerated "neutral noise", H3 the middle case, H4 any-n-of-M).

**Result.** Exact RNA structure: m given a route 2.3 (m_all 0.05; far from S1 1.5; tRNA 1.5): λ ~1, below the flip even at s = 0.05. Within 2 bp: 3.4. Pre-registered same-shape class: 28 (a fired trigger; dominated by helix loss); without helix loss 11.8 at L >= 76. DMS: tolerated substitutions per codon 5.1 of 6.6 (H2); beneficial-proxy per codon 0.21 (λ 0.10); gene-level beneficial pool median 51 (0–1,760; 17% none), shared: P(success) 0.999 for 10 needed changes, 0.074 for 25, 4e-20 for 50 at s = 0.01. Any-n-of-M: within-gene beneficial fraction (3.6%, upper bound) 82–1,600x G1's requirement for n <= 2e5, 8–16x for n = 2e7 at p = 0.02.

**For Day.** Exact-outcome λ ~1; GB1 95% nonfunctional, 67–158 SNV-level local maxima, 30–51% reach of the best variant; "reduce or destroy" passes as worded (61% of datasets); a short locus cannot drift its way to a one-step route (36–80 neutral steps needed vs 0.03–0.06 available). **For the critics.** 71% of singles keep half of WT-like function; "destroy" alone is a minority (majority in 2% of datasets); GB1 is one connected component and 98.5% of functional variants have an uphill SNV neighbour; RNA neutral networks ~1e33. **Untouched:** per-sequence prevalence (D10–D12), cross-family connectivity, regulatory waiting times (D15).

**Verdicts.** D1d external **supported** (existence part); D2h contested (partial support as worded); others unchanged with comments; G3b's open item replaced by measured numbers. Reviews: `results/REVIEW-R4-D1-*.md`; `REVIEW.md` review #11.

## X1 — Arithmetic and internal-validity audit of every numeric critic and ally claim; one verdict rule for both sides · `x1_critic_arithmetic.py` (pre-registered fa0bc9b), post hoc `x1_posthoc_wf_convergence.py`, `x1_posthoc_missing_rows.py`, `x1_fix_posthoc.py` (77b9790), `x1_rescore.py` (11744e6, 32e2a75, f9e8291, 6eea84e, 849ec9c), `x1_rule2_posthoc.py` (4318f16) · all critic and ally numeric claims, and every Day node with an error or n/a-fidelity verdict · write-ups `results/R4-X1-critic-arithmetic.md`, `R4-X1-verdict-rule.md` (rev 2), `R4-X1-rescore.md`

**Why.** The R5 draft's balance audit found 22 of 112 Day nodes with internal error verdicts against 0 of 51 critic nodes, and only one check aimed at a critic claim. PLAN item 10 (arithmetic audit of both sides) had never been run for the critics.

**What it did.** Recomputed all 45 numeric critic and ally claims from their own stated inputs (34 clean, 9 with a flagged basis or input, 2 not reproduced in the first pass); wrote one verdict rule (materiality R1 with a symmetric slip test on the author's own stated conclusion and a 25% line; R1c no input-looseness rescue for steep outputs; scope S; self-correction SC; non-sequitur N; fidelity F; unidentified authors U; charity C); re-scored both sides under it. A blind audit of the rule's application agreed on 90% of Day calls and 100% of critic error / no-error calls, found clauses that bit one side harder, and led to rev 2.

**Result (rev 2).** Error verdicts, Day vs critics: 13/81 vs 1/20 (numeric by the author's quoted text, p = 0.29); 16/82 vs 1/31 (formal-statement numeric, p = 0.038); 18/114 vs 1/51 (all files, p = 0.008). Per 10k quoted words: 22.7 vs 10.0. Sensitivity: with the three critic tie-breaks (C5, A3d, B5f) flipped, 16/82 vs 4/31, p = 0.58; at a 10% materiality line 18/82 vs 2/31, p = 0.059. **Reading:** Day's errors are robust to reading (most fail against his own table, equation or text); the audit cannot claim critics err less per argument (critic claims are shorter, and the critic zero or near-zero rests on tie-break clauses).

**For Day.** Three earlier error verdicts withdrawn under one rule: A3a (charity: 35M + 1,140 + 2 x 187M = 409.0M, 0.24% from 410M), G (label slip; the stated 107 survives at 106.5), F (it double-counted F1a's step); A5e and G1a move to the slip ledger. Critic slips recorded: Hancock's 38M match does not follow on his own event basis (B5c, +46%); keruru's 4e-35 is about 10 orders above the exact value at his stated Nₑ; Hancock's E. coli rate is 8.9x below the measured rate; McCarthy mixes 25 y and 20 y generations (ledger).

**For the critics.** The exact identities (k = μ; P_fix = 1/(2N) using the census count) and Mansfield's "1 per generation", McCarthy's 22.5M, Matev's variance figures and a Reddit commenter's 3,840 correction all reproduce; keruru's values reproduce at his own measured Nₑ; Day's s6.4 38,400 slip gets its own Day node (A5h, arithmetic-error). The audit's own C5 figure (1.2e-46) was 41x low and is corrected.

**Verdicts.** See `R4-X1-rescore.md` (both sides, one row per node). Reviews: `results/REVIEW-R4-X1-{correctness,steelman-day,steelman-critic,rule-audit}.md` (review #12).

## GAP-07c — Share of human–chimp divergent sites still polymorphic in humans · `gap07c_polymorphic_share.py` (pre-registered 078850b), post hoc `gap07c_posthoc_toplevel.py`, `gap07c_posthoc_review.py` (ae42a91); runs on na-workhorse · claims A3, A3b, A3c, A3x · full write-up `results/R4-GAP07c.md`

**What it measures.** At GAP-07b's divergent sites, whether the chimp-matching allele is still segregating in humans (1000 Genomes phase 3 on GRCh38; NYGC 30x cross-check on chr21+22, same people, independent pipeline).

**Result.** 15.6% of human-derived divergent SNVs are polymorphic at >= 1% (14.8–16.7% per chromosome), consistent with the human half of CSAC's 14–22%. Human-lineage indels 7.4–8.7% (9.5–10.5% in mask); SVs >= 50 bp 6.8% net (n = 450; short-read, lower bound). The chimp side is not measured. Fixed events per lineage: 17.2–17.9M, so Day's 205M is 10.6–12.6x fixed events (human lineage alone 11.9); combined with GAP-07b, about **8–13x**.

**For Day.** 84.4% of human-derived differences are fixed; large variants are mostly fixed (consistent with his post-divergence remark, Q100); his own remarks on ancestral polymorphism (Q37; 04-28 ¶24) are now credited.

**For the critics.** Polymorphism is real and of CSAC's size; the unit mismatch (about 10x) is untouched. Day's 17.5M, like for like, is 9.8% above the measured fixed SNVs and 2.2% below all fixed events (two offsetting errors); his SNV-only shortfall falls about 9%.

**Verdicts.** A3 contested, A3b supported, A3c supported (status reviewed), A3x supported; comments updated. Reviews: `results/REVIEW-R4-GAP07c-{correctness,steelman}.md` (review #13).

## P1: machine-checked derivations (2026-10-09)
Pre-registered c17b44a; run on na-workhorse (34 s). All 17 identity groups (k = mu, P_fix = i/M, exchangeable low-N_e P_fix = 1/M, empty-start deficit mu E[tau], Kimura/Moran, diffusion and exact fixation times, Haldane's D) and 33 Day-arithmetic rows came out as pre-registered; Q03 (table 125 vs 281.25), Q19 (8 vs 9.13) and Q30 (printed-input rounding) are slips/discrepancies. **For Day:** 30/33 rows hold, the empty-start formula and the -pi^2 N_e/G exponent are exact at the level proved. **For the critics:** k = mu and P_fix = 1/(2N) are exact and independent of N_e (exchangeable models); D is not a constant. **Verdicts:** none changed (re-confirmation); scope limits in the Review resolution. Review: `results/REVIEW-R4-P1-combined.md` (0 MAJOR, 5 MINOR, 6 NOTE).

## B5b: Mansfield's supply with a sourced neutral fraction (2026-10-09)
Pre-registered b707415; arithmetic, na-workhorse. All predictions met. The identity is exact; at 2% the supply is 44x (450k generations) to 69x (252k) short; with f = 0.918 (Rands 2014 complement, an upper bound) and 100 per zygote it is 20.7M over 450,000 generations (20M covered by 3%) but 11.6M over 252,000 (0.66x of 17.5M); with 76.8 per zygote 0.79x and 0.51x. Combined review #15: 0 MAJOR, 5 MINOR. No verdict change. `results/R4-B5b.md`.

## F1b: in-transit fixation count measured (2026-10-09)
Pre-registered fb6aac2; na-workhorse. All predictions met (cell A not fully blind). In transit: 333.3, 17.07, 0.984 against theory 335.5, 16.8, 1.01; Poisson dispersion 0.95-1.00; weak form violated 333x and 17x, an equality at the serial boundary. Review #16: 1 MAJOR (Little's law on the same sample is an identity; wording), 1 MINOR header. F1 open item closed; verdicts unchanged; F1b external -> supported (independent loci). `results/R4-F1b.md`.

## C1e: C1c model on published Holocene N_e trajectories (2026-10-09)
Pre-registered 2c245ec; na-workhorse, 3 replicates. P1-P4, P5 central, P6 met; P5 sensitivity clauses (1.2%, 2.3%) and P7 (R2 within 2x of R0) missed. R0 S21 (Day 21): Gravel 1,127; Gazave 5,164; Coventry 5,102; Nelson 42 (R2 51); controls reproduce C1c. Review #18: 1 MAJOR (25 y vs 20 y generation mismatch, S21 high by 1.4-1.7x; bracketed, not rerun), 5 MINOR. No verdict change. `results/R4-C1e.md`. POST HOC RERUN (review MAJOR-1; script 1c7e463; 25 y clock matched to every source; 6 replicates): R0 S21 Gravel 710 (34x), Gazave 3,387 (161x), Coventry 3,279 (156x), Nelson 31 (1.5x; R2 50); all pre-registered predictions met; conclusions unchanged (see R4-C1e.md).

## G2c / B6c: standing neutral variation under parallel sweep models (2026-10-09)
Pre-registered 1ffd053; na-workhorse. Hn ratio to control 0.97-1.03 at sweep rate 1/1,322 and 1.00-1.01 at about 146 concurrent sweeps; falsifier (< 0.10) did not fire. Missed: A rep1 concurrency (0.5), B concurrency 146 vs [150, 300] (realised fixation rate 1.55x intended, unexplained). Review #17: 1 MAJOR (that account), 5 MINOR. G2c and B6c external pending -> supported as a conditional. `results/R4-G2c.md`.

