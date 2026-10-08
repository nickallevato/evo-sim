"""Check B2a (THROWAWAY): exact Wright-Fisher Markov chain vs Day's Hard Limits tail exp(-pi^2 Ne/G).

Claim B2 (Zenodo 22129121 abstract, per fetcher): probability of neutral fixation within G
generations is "exponentially small, of order exp(-pi^2 Ne/G)" when 4Ne > G.

PRE-REGISTERED PREDICTION (2026-10-07): arcsine transform y = arccos(1-2x) gives constant variance
1/(2N)/gen and path length pi, so the short-time (Varadhan) asymptotic is ln P ~ -pi^2 N/G:
(G/N)·ln F_cond(G) -> -pi^2 as G/N -> 0. Day's EXPONENT correct as a leading-order asymptotic;
the prefactor is sub-exponential.
Relevance caveat (pre-stated): per-allele probability; expected substitutions across all mutations
= U*int F (B1), so B2 bounds latency, not throughput.
"""
import numpy as np
from scipy.stats import binom

for N in (50, 100, 200):
    M = 2 * N
    states = np.arange(M + 1)
    P = binom.pmf(states[None, :], M, states[:, None] / M)
    v = np.zeros(M + 1); v[1] = 1.0
    G_max = 6 * N
    F = np.empty(G_max)
    for g in range(G_max):
        v = v @ P
        F[g] = v[M]
    for _ in range(40 * N):
        v = v @ P
    u = v[M]
    Fc = F / u
    print(f"N={N}: exact P_fix={u:.6f} (1/2N={1/M:.6f})")
    for r in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0):
        g = int(round(r * N))
        if g >= 1 and Fc[g - 1] > 0:
            print(f"   G/N={r:<5} F_cond={Fc[g-1]:.3e}  (G/N)ln F={r*np.log(Fc[g-1]):+7.3f} [-pi^2=-9.870]  Day exp(-pi^2 N/G)={np.exp(-np.pi**2/r):.3e}  ratio exact/Day={Fc[g-1]/np.exp(-np.pi**2/r):.2e}")
