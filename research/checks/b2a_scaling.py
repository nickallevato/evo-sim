"""B2a follow-up (THROWAWAY): N-convergence of r*ln F_cond(G=rN) at fixed r, exact WF chain.
Reproduces review #3's table. Prediction (from review #3): limits ≈ -8.4 (r=.25), -7.45 (r=.5), -6.0 (r=1),
consistent with ln F ≈ -pi^2/r + 1.5 ln(1/r) + 3.9.
"""
import numpy as np
from scipy.stats import binom

rs = (0.25, 0.5, 1.0)
print(f"{'N':>6} " + " ".join(f"{'r='+str(r):>9}" for r in rs) + "   fit -pi^2/r+1.5ln(1/r)+3.9 → r*lnF")
for N in (100, 400, 1600):
    M = 2 * N
    st = np.arange(M + 1)
    P = binom.pmf(st[None, :], M, st[:, None] / M)
    v = np.zeros(M + 1); v[1] = 1.0
    out = {}
    for g in range(1, N + 1):
        v = v @ P
        for r in rs:
            if g == int(r * N):
                out[r] = r * np.log(v[M] * M)   # F_cond = F / (1/2N)
    fit = " ".join(f"{r*(-np.pi**2/r + 1.5*np.log(1/r) + 3.9):>7.2f}" for r in rs)
    print(f"{N:>6} " + " ".join(f"{out[r]:>9.3f}" for r in rs) + f"   {fit}")
