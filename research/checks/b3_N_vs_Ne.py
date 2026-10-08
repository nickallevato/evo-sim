"""Check B3/B7 (THROWAWAY): does neutral fixation probability / substitution rate depend on Ne or N?

Claim B3 (Day, Zenodo 18429937/19984826, pass-1 wording; verbatim pending R1p2):
  neutral fixation probability = 1/(2Ne), hence k = mu * N/Ne (supply uses census N).
Counter-claim B7: fixation probability = initial frequency 1/(2N) (martingale), hence k = mu;
  Ne governs the *time* to fixation, not the probability.

Model: exchangeable Cannings model, M = 2N gene copies, Dirichlet(alpha) family weights; small
alpha => high offspring variance => Ne << N.

PRE-REGISTERED PREDICTIONS (2026-10-07):
  P1 P_fix = 1/M for every alpha (to 3 SE). Day's model predicts 1/(2Ne) = sigma^2/M.
  P2 Conditional mean t_fix scales with Ne (~ 4Ne, Ne ≈ N/sigma^2), NOT with census N.
     (i.e. Day is right that Ne sets the timescale.)
  P3 Consequently k = U for every alpha.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # allow `python -I`

import numpy as np
from wf import cannings_single_locus

rng = np.random.default_rng(13)
M = 400  # N = 200 diploids
reps = 1_000_000
print(f"M={M} copies (N={M//2}); reps={reps}")
print(f"{'alpha':>6} {'sigma2':>7} {'Ne≈N/s2':>8} | {'P_fix sim':>12} {'1/M':>8} {'Day 1/2Ne':>10} | {'t_fix/Ne':>8} {'t_fix/N':>8}")
for alpha in (1e6, 4.0, 1.0, 0.25, 0.1):
    sigma2 = (M * (1 + alpha)) / (1 + M * alpha) * (1 - 1 / M)   # Beta-binomial variance for one copy
    Ne = (M / 2) / sigma2
    fixed, t = cannings_single_locus(M, alpha, reps, rng)
    p = fixed.mean(); se = np.sqrt(p * (1 - p) / reps)
    tf = t[fixed].mean(); tfse = t[fixed].std() / np.sqrt(fixed.sum())
    print(f"{alpha:>6g} {sigma2:>7.2f} {Ne:>8.1f} | {p:.5f}±{se:.5f} {1/M:>8.5f} {1/(2*Ne):>10.5f} z={(p-1/M)/se:+.2f} | {tf/Ne:>5.2f}±{tfse/Ne:.2f} {tf/(M/2):>8.2f}")
