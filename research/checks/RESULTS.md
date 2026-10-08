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

- **Fit:** ln F_cond ≈ −π²/r + 1.5·ln(1/r) + 3.9, i.e. a power-law prefactor of about 50·r^−1.5. This is the reviewer's empirical fit from 3 points, not derived analytically.
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
