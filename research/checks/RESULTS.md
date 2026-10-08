# Check Results Log (THROWAWAY research checks)

Each entry lists: the script, its seed, what was predicted before the run, what came out, and the review status. A result counts only after it passes review (see `REVIEW.md`).

Run any script with:
```
research/.venv/bin/python -I research/checks/<script>.py
```
Run it from inside `research/checks/`, because the scripts import `wf.py` from there.

## B0 — Textbook baselines · `baseline_textbook.py` (seed 20261007) · ALL PASS
| Check | Simulated | Target | z |
|---|---|---|---|
| B0.1 neutral P_fix, N=50 | 0.009893 | 0.01 | −0.69 |
| B0.1 neutral P_fix, N=200 | 0.00246 | 0.0025 | −0.51 |
| B0.2 conditional mean t_fix / N, N=50 | 3.908 | 4 | −2.75 |
| B0.2 conditional mean t_fix / N, N=200 | 4.006 | 4 | +0.08 |
| SD of t_fix / N | 2.105, 2.108 | ≈2.15 (diffusion) | — |
| B0.3 Kimura u, N=100, s=0.01 | 0.019995 | 0.020171 | −0.56 |
| B0.3 Kimura u, N=500, s=0.01 | 0.019745 | 0.019801 | −0.18 |
| B0.3 Kimura u, N=1000, s=0.005 | 0.010225 | 0.009950 | +1.22 |
| B0.5 neutral k at equilibrium, N=50 | 0.05018 | U=0.05 | +0.13 |
| B0.5 neutral k at equilibrium, N=200 | 0.04964 | U=0.05 | −0.64 |

**Notes**
- The N=50 fixation-time z of −2.75 is consistent with known small-N discreteness corrections to the diffusion approximation. To follow up, check it against an exact Markov chain (rule E4).
- B0.5 holds at both N values, consistent with k = U for any N.

## B0.4 / F — Fixation time of a beneficial mutant · `beneficial_fix_time.py` (seed 7)
**Prediction:** simulated t_fix ≈ the Kimura–Ohta diffusion integral, and Day's (2/s)ln(2N) overshoots both.

**Result:** confirmed. Simulation and diffusion agree within 1%. (2/s)ln(2N) overshoots by 1.6–2.2× across the tested range.

| N | s | 2Ns | sim | diffusion | (2/s)ln2N | (2/s)(ln2Ns+γ) |
|---|---|---|---|---|---|---|
| 500 | 0.01 | 10 | 698 | 703 | 1382 | 576 |
| 1000 | 0.005 | 10 | 1405 | 1407 | 3040 | 1152 |
| 2500 | 0.01 | 50 | 1043 | 1033 | 1703 | 898 |
| 5000 | 0.01 | 100 | 1177 | 1173 | 1842 | 1036 |
| **10⁴ (Day's)** | **0.001** | **20** | — | **8,480** | **19,807** | 7,146 |

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
- **Internal validity of Day's E[F(T)]: HOLDS.** For an empty starting population his formula is exact.
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
| 1.99 | 100 | 0.00257 | 0.00250 | 0.00498 | 3.97 |
| 4.94 | 40 | 0.00248 | 0.00250 | 0.01235 | 4.01 |
| 10.70 | 19 | 0.00257 | 0.00250 | 0.02676 | 4.07 |

**Interpretation**
- **Day is right on time:** Nₑ sets the *timescale* of fixation.
- **Day is wrong on probability:** in an exchangeable model, Nₑ does not set the fixation *probability*. So k = μN/Nₑ fails *in this model class*.

**Open fairness sub-check B3b.** Day's k = 0.743μ invokes Balloux & Lehmann 2012: fluctuating N combined with overlapping generations. That is a non-exchangeable, time-varying setting, where the neutral rate *can* differ from μ per generation. B3b must test that setting before B3 receives a final verdict.
