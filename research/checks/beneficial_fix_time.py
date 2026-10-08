"""B0.4 follow-up (THROWAWAY): conditional fixation time of a new beneficial mutant.
Compares WF simulation, the Kimura–Ohta diffusion integral, Day's (2/s)ln(2N)
(deterministic logistic sweep time), and the stochastic approximation (2/s)(ln(4Ns)+γ).
PRE-REGISTERED: sim ≈ diffusion integral (within ~5%); (2/s)ln(2N) exceeds both by a factor
that shrinks only slowly as 2Ns grows.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # allow `python -I`

import numpy as np
from wf import single_locus, diffusion_cond_fix_time
rng = np.random.default_rng(7)
print(f"{'N':>6} {'s':>6} {'2Ns':>6} {'sim':>8} {'diffusion':>10} {'(2/s)ln2N':>10} {'stoch':>8} {'ratio Day/sim':>13}")
for N, s, reps in ((500, 0.01, 200_000), (1000, 0.005, 200_000), (2500, 0.01, 60_000), (5000, 0.01, 40_000)):
    fixed, t = single_locus(N, s, reps, rng)
    tf = t[fixed]
    d = diffusion_cond_fix_time(N, s)
    day = 2 / s * np.log(2 * N)
    sto = 2 / s * (np.log(4 * N * s) + 0.5772)
    print(f"{N:>6} {s:>6} {2*N*s:>6g} {tf.mean():>5.0f}±{tf.std()/np.sqrt(len(tf)):<3.0f} {d:>10.0f} {day:>10.0f} {sto:>8.0f} {day/tf.mean():>13.2f}")
# Day's human parameters (no sim; diffusion only): Ne=1e4, s=0.001
N, s = 10_000, 0.001
print(f"Day's parameters Ne=1e4 s=0.001: diffusion={diffusion_cond_fix_time(N, s):.0f}, (2/s)ln(2N)={2/s*np.log(2*N):.0f}, stoch={2/s*(np.log(4*N*s)+0.5772):.0f}")
