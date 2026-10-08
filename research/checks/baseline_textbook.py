"""Textbook baselines (THROWAWAY). Must pass before any claim-specific check counts.

PRE-REGISTERED PREDICTIONS (written before first run, 2026-10-07):
  B0.1 Neutral fixation probability of a new mutant = 1/(2N).
  B0.2 Mean time to fixation, conditional on fixation, ~= 4N gens; SD ~= 2.15N (Kimura & Ohta 1969).
  B0.3 Fixation probability with genic s: (1-e^{-2s})/(1-e^{-4Ns}) (Kimura 1962).
  B0.4 Conditional fixation time for beneficial allele (exploratory, two candidate formulas):
         Day's form (2/s)ln(2N)  [deterministic logistic, 1/(2N) -> 1-1/(2N)]
         stochastic form (2/s)(ln(2Ns) + 0.5772)   [for 2Ns >> 1]
       Prediction: simulation is closer to the stochastic form.
  B0.5 Neutral substitution rate at equilibrium k = U (per-genome neutral rate), independent of N.
Pass tolerance: within 3 standard errors (B0.1–B0.3, B0.5); B0.4 reported only.
"""
import sys
import numpy as np
from wf import kimura_u, single_locus, neutral_substitutions

rng = np.random.default_rng(20261007)
ok = True


def check(name, est, se, target):
    global ok
    z = (est - target) / se if se > 0 else float("inf")
    passed = abs(z) < 3
    ok &= passed
    print(f"{'PASS' if passed else 'FAIL'} {name}: est={est:.5g} ± {se:.2g}  target={target:.5g}  z={z:+.2f}")


# B0.1 / B0.2
for N in (50, 200):
    reps = 400_000
    fixed, t = single_locus(N, 0.0, reps, rng)
    p = fixed.mean()
    check(f"B0.1 P_fix neutral N={N}", p, np.sqrt(p * (1 - p) / reps), 1 / (2 * N))
    tf = t[fixed]
    check(f"B0.2 mean t_fix neutral N={N} (in units of N)", tf.mean() / N, tf.std() / N / np.sqrt(len(tf)), 4.0)
    print(f"     SD t_fix / N = {tf.std() / N:.3f} (Kimura–Ohta ~2.15); n_fixed={len(tf)}")

# B0.3 / B0.4
for N, s in ((100, 0.01), (500, 0.01), (1000, 0.005)):
    reps = 200_000
    fixed, t = single_locus(N, s, reps, rng)
    p = fixed.mean()
    check(f"B0.3 P_fix N={N} s={s}", p, np.sqrt(p * (1 - p) / reps), kimura_u(N, s))
    tf = t[fixed]
    day = 2 / s * np.log(2 * N)
    sto = 2 / s * (np.log(2 * N * s) + 0.5772)
    print(f"INFO B0.4 N={N} s={s} 2Ns={2*N*s:g}: sim mean t_fix={tf.mean():.0f} ± {tf.std()/np.sqrt(len(tf)):.0f}; "
          f"(2/s)ln(2N)={day:.0f}; (2/s)(ln(2Ns)+γ)={sto:.0f}")

# B0.5 neutral k = U at equilibrium, two N values, same U
U = 0.05
for N in (50, 200):
    T = 40 * N
    reps = 20
    rates = [neutral_substitutions(N, U, T, rng, start="equilibrium")[-1] / T for _ in range(reps)]
    rates = np.array(rates)
    check(f"B0.5 k at equilibrium N={N} (U={U})", rates.mean(), rates.std(ddof=1) / np.sqrt(reps), U)

print("ALL BASELINES PASS" if ok else "BASELINE FAILURE")
sys.exit(0 if ok else 1)
