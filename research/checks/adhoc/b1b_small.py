"""Check B1b (THROWAWAY): neutral substitution rate under size changes, from an EQUILIBRIUM start.

Steelman of Day (review D1): "k=μ holds only after a population has held one size for the roughly
4Ne generations a neutral allele needs to drift" (Zenodo 22129121 abstract, per fetcher).

PRE-REGISTERED PREDICTIONS (2026-10-07):
  Standard theory: long-run mean k = U for any size history, but transients occur:
   - contraction/bottleneck: temporary EXCESS (standing variants fix fast in the small population);
   - expansion: temporary DEFICIT lasting ~4N_new gens (pipeline lengthens), cumulative deficit
     on the order of U * (mean fixation-time increase) — i.e. Day's mechanism is real for expansions.
  Day: deficit whenever N has not been constant for ~4Ne gens.
  What would change verdicts: a persistent deficit (not transient) under any schedule, or a
  deficit under contraction.
Scale: N in units of N0=500; time in units of 4*N0. U=0.2.
"""
import os, sys
sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')  # allow `python -I`

import numpy as np
from wf import substitutions_demog

rng = np.random.default_rng(21)
N0, U = 500, 0.2
T = 12 * N0                    # 3 x 4N0
win = N0                       # window = N0 gens
reps = 4
scen = {
    "constant N0":               (lambda g: N0, N0),
    "bottleneck N0->N0/10 (N0/2 gens)->N0": (lambda g: N0 // 10 if g < N0 // 2 else N0, N0),
    "contraction N0->N0/5":      (lambda g: N0 // 5, N0),
    "expansion N0/5->N0":        (lambda g: N0, N0 // 5),
    "expansion N0/5->5N0":       (lambda g: 5 * N0, N0 // 5),
    "founder N0->10 (20 gens)->N0": (lambda g: 10 if g < 20 else N0, N0),
}
print(f"N0={N0}, U={U}, window={win} gens, T={T} (=3*4N0), reps={reps}. Entries = window k / U (1.00 = k=μ)")
hdr = " ".join(f"{(i+1)*win:>6}" for i in range(T // win))
print(f"{'scenario':<38} {hdr} | cum/UT")
for name, (Nf, Nb) in scen.items():
    runs = np.array([substitutions_demog(Nf, U, T, rng, burn_in=10 * Nb, N_burn=Nb) for _ in range(reps)])
    w = runs.reshape(reps, T // win, win).sum(axis=2).mean(axis=0) / (U * win)
    cum = runs.sum(axis=1).mean() / (U * T)
    print(f"{name:<38} " + " ".join(f"{x:>6.2f}" for x in w) + f" | {cum:.3f}")
