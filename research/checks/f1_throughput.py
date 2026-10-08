"""Check F1 (THROWAWAY): latency is not throughput (Mansfield's 'truck' / pipelining argument).

PRE-REGISTERED PREDICTIONS (2026-10-07), independent loci (no interference):
  P1 Steady-state substitution rate of beneficial mutations = 2N*U_b*u(s) (Kimura u), independent of
     the fixation latency t_fix.
  P2 Little's law: mean number of eventually-fixing alleles in transit = rate * mean t_fix, so
     G_f = 1/rate can be far smaller than t_fix (many fixations in flight at once).
  Limit of this check: no linkage/interference — that is F2 (Day's strongest version, review D4).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # allow `python -I`

import numpy as np
from wf import substitutions_demog, kimura_u, diffusion_cond_fix_time

rng = np.random.default_rng(31)
N, s, Ub = 1000, 0.01, 0.01
T, reps = 20000, 8
rate_pred = 2 * N * Ub * kimura_u(N, s)
lat = diffusion_cond_fix_time(N, s)
runs = np.array([substitutions_demog(lambda g: N, Ub, T, rng, s=s, burn_in=5000, N_burn=N) for _ in range(reps)])
rate = runs.sum(axis=1) / T
print(f"N={N} s={s} U_b={Ub}: predicted rate 2N*U_b*u={rate_pred:.4f}/gen; sim={rate.mean():.4f} ± {rate.std(ddof=1)/np.sqrt(reps):.4f}")
print(f"latency t_fix={lat:.0f} gens; G_f=1/rate={1/rate.mean():.0f} gens; Little's law in-transit fixers ≈ {rate.mean()*lat:.1f}")
print(f"Serial reading (one at a time) would give {T/lat:.1f} fixations in T={T}; observed {runs.sum(axis=1).mean():.1f}")
