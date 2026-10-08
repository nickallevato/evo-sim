"""Check H2 (THROWAWAY): Nunney-2003-style Gaussian-optimum model; does the M-dependence appear?
Seed: SeedSequence(20261010). Run: research/.venv/bin/python -I research/checks/h_nunney_gauss.py

PRE-REGISTERED PREDICTION (claim H2, written before running this variant, after seeing that the constant-s
treadmill in h_cost_of_selection.py gave only a gradual M-dependence):
 Nunney (quoted): "For M > 1/2, the cost of natural selection is substantially less than Haldane's estimate;
 however, when M < 1/2, the cost (and particularly the fixed cost) increases in an accelerating fashion as M is
 lowered."  "a simulated population with M = 10 can tolerate environmental change that requires allelic
 substitution at 7 loci ... every 40 generations. With M = 1, ... a single trait ... could still undergo allelic
 turnover every 20 generations."  "K = 10,000 ... M = 0.1 ... extinct if ... faster than about every 300 generations".
 Prediction for this reconstruction (K=500, R=10, hard): n=1 interval ~20 at M=1, ~10-20 at M=10; n=7 ~40 at M=10,
 ~55-60 at M=1; interval rises sharply (>~70) at M<=0.25 and ~300 at M=0.1. A reconstruction that gets M=0.1 right
 only within a factor ~3 counts as a qualitative reproduction. SOFT regime (not in Nunney's simulation): predict
 smaller or equal T_min only when R is ample.
 Not expected to match: absolute values (his Eq.3/5 reconstructed; his persistence rule is 'no extinction in 20 runs
 incl. 1.02C,1.05C,1.10C' vs mine 8 runs).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import wf_hc as h

GRID = [6, 8, 10, 13, 16, 20, 25, 32, 40, 50, 64, 80, 100, 130, 170, 220, 300, 400, 550, 750, 1000]

def cond(a):
    K, n, R, M, reg, seed = a
    rng = np.random.default_rng(np.random.SeedSequence(seed))
    u = M / (2 * K)
    fr, streak = [], 0
    for T in GRID:
        ok = 0
        for _ in range(10):
            o = h.gauss_run(K, n, T, R, u, reg, 5 if T < 300 else 4, rng)
            ok += (not o["extinct"]) and (o["dev2"] < 0.5)
        fr.append(ok / 10)
        streak = streak + 1 if ok >= 9 else 0
        if streak >= 2: break
    T50 = np.nan
    for i, f in enumerate(fr):
        if f >= 0.5:
            if i == 0: T50 = GRID[0]
            else:
                t0, t1 = GRID[i - 1], GRID[i]
                T50 = float(np.exp(np.log(t0) + (0.5 - fr[i - 1]) / (f - fr[i - 1]) * (np.log(t1) - np.log(t0))))
            break
    return (K, n, R, M, reg, T50)

if __name__ == "__main__":
    base = 20261010
    conds = []
    i = 0
    for reg in ("hard", "soft"):
        for n in (1, 7):
            for M in (0.1, 0.25, 0.5, 1.0, 10.0):
                i += 1
                conds.append((500, n, 10, M, reg, base + i))
    for reg in ("hard", "soft"):
        for R in (2.2, 3, 5, 40):
            i += 1
            conds.append((500, 1, R, 1.0, reg, base + i))
    with Pool(3) as p:
        res = p.map(cond, conds, chunksize=1)
    print("K=500; success = no extinction AND adult mean squared deviation < 0.5 (10 reps/T); T50 = 50% crossing")
    print("Nunney reference (R=10): M=10 n=7 ~40; M=1 n=1 ~20, n=7 ~ 3x slower than M=10; M=0.25 ~70 (n=1); M=0.1 ~300 (K=1e4)")
    for K, n, R, M, reg, T50 in res:
        print(f" {reg:4s} n={n} R={R:<4} M={M:<5} T50={T50:7.1f}  rate n/T50={n/T50:.4f}/gen")
