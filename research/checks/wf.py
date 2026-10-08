"""Minimal Wright-Fisher primitives for research checks (THROWAWAY, non-product).

Conventions (see docs/research/glossary.md):
  N  = diploid census size; M = 2N gene copies.
  s  = per-copy (genic) selection coefficient: an allele copy has fitness 1+s.
       Diffusion fixation probability for a new mutant: (1-exp(-2s))/(1-exp(-4Ns)).
  Loci are independent (no linkage) unless stated; this is exact for the expected
  neutral substitution count, not for its variance.
"""
import numpy as np


def kimura_u(N, s, p=None):
    """Kimura (1962) fixation probability, genic selection, Ne = N."""
    if p is None:
        p = 1.0 / (2 * N)
    if s == 0:
        return p
    return (1 - np.exp(-4 * N * s * p)) / (1 - np.exp(-4 * N * s))


def single_locus(N, s, reps, rng, max_gens=10**7):
    """Run `reps` independent new-mutant trajectories (start at 1 copy) to absorption.

    Returns (fixed: bool array, t_abs: int array of absorption generation).
    """
    M = 2 * N
    k = np.ones(reps, dtype=np.int64)
    t = np.zeros(reps, dtype=np.int64)
    alive = np.ones(reps, dtype=bool)
    gen = 0
    while alive.any():
        gen += 1
        if gen > max_gens:
            raise RuntimeError("max_gens exceeded")
        idx = np.flatnonzero(alive)
        p = k[idx] / M
        if s:
            p = p * (1 + s) / (1 + s * p)
        k[idx] = rng.binomial(M, p)
        done = (k[idx] == 0) | (k[idx] == M)
        t[idx[done]] = gen
        alive[idx[done]] = False
    return k == M, t


def neutral_substitutions(N, U, T, rng, start="empty", burn_in=None):
    """Infinite-sites neutral WF, unlinked sites.

    U = genome-wide neutral mutation rate per gamete per generation, so 2N*U new
    mutations enter per generation. Returns cumulative fixation counts per generation
    (length T), counted from the start of the observation window.

    start='empty'      : no segregating variation at t=0 (Day's 'empty pipeline').
    start='equilibrium': run `burn_in` generations first (default 10N) so the
                         ancestral population is at mutation-drift balance.
    """
    M = 2 * N
    counts = np.empty(0, dtype=np.int64)

    def step(counts):
        new = rng.poisson(M * U)
        counts = np.concatenate([counts, np.ones(new, dtype=np.int64)])
        counts = rng.binomial(M, counts / M)
        fixed = int((counts == M).sum())
        counts = counts[(counts > 0) & (counts < M)]
        return counts, fixed

    if start == "equilibrium":
        for _ in range(burn_in if burn_in is not None else 10 * N):
            counts, _ = step(counts)
    elif start != "empty":
        raise ValueError(start)

    cum = np.empty(T, dtype=np.int64)
    total = 0
    for g in range(T):
        counts, f = step(counts)
        total += f
        cum[g] = total
    return cum


def diffusion_cond_fix_time(N, s, p=None):
    """Kimura & Ohta (1969) mean time to fixation conditional on fixation (diffusion), genic s.

    Written in a numerically stable form: the factor exp(Sx) in psi(x) is folded into (1-u(x)).
    """
    from scipy.integrate import quad
    if p is None:
        p = 1.0 / (2 * N)
    if s == 0:
        return -4 * N * (1 - p) * np.log(1 - p) / p
    S = 4 * N * s
    den = -np.expm1(-S)                      # 1 - e^{-S}
    intG = den / S                           # int_0^1 e^{-Sy} dy
    u = lambda x: -np.expm1(-S * x) / den
    one_minus_u_times_eSx = lambda x: -np.expm1(-S * (1 - x)) / den
    pref = lambda x: 4 * N * intG / (x * (1 - x))   # 2*intG/V(x) with V = x(1-x)/(2N)
    a = quad(lambda x: pref(x) * u(x) * one_minus_u_times_eSx(x), p, 1, limit=500,
             points=[min(0.5, 10 / S)])[0]
    b = quad(lambda x: pref(x) * np.exp(S * x) * u(x) ** 2, 0, p, limit=200)[0]
    up = u(p)
    return a + (1 - up) / up * b


def cannings_single_locus(M, alpha, reps, rng, max_gens=10**7):
    """Neutral exchangeable (Cannings) model with M gene copies and Dirichlet(alpha) family weights.

    Offspring-number variance per copy ~ (1+alpha)/alpha for large M (alpha -> inf recovers WF).
    Focal allele count update is exactly BetaBinomial(M, k*alpha, (M-k)*alpha).
    Returns (fixed, t_abs) for new mutants starting at 1 copy.
    """
    k = np.ones(reps, dtype=np.int64)
    t = np.zeros(reps, dtype=np.int64)
    alive = np.ones(reps, dtype=bool)
    gen = 0
    while alive.any():
        gen += 1
        if gen > max_gens:
            raise RuntimeError("max_gens exceeded")
        idx = np.flatnonzero(alive)
        kk = k[idx]
        w = rng.beta(kk * alpha, (M - kk) * alpha)
        k[idx] = rng.binomial(M, w)
        done = (k[idx] == 0) | (k[idx] == M)
        t[idx[done]] = gen
        alive[idx[done]] = False
    return k == M, t


def substitutions_demog(N_of_g, U, T, rng, s=0.0, burn_in=0, N_burn=None, track_transit=False):
    """Infinite-sites, unlinked sites, genic s (same s for all new mutations), size schedule N_of_g(g).

    Burn-in runs `burn_in` gens at constant N_burn (equilibrium start if burn_in >~ 10*N_burn).
    At each generation: mutate (Poisson(2N*U) new single copies), then WF-sample at the new size
    (binomial(2N_new, p'), p' from previous frequencies), count fixations.
    Returns per-generation fixation counts (length T) and, if track_transit, the per-generation
    number of segregating alleles that will eventually fix (known post hoc via ids).
    """
    counts = np.empty(0, dtype=np.int64)
    M_prev = 2 * (N_burn if N_burn is not None else N_of_g(0))

    def step(counts, M_prev, M):
        new = rng.poisson(M_prev * U)
        counts = np.concatenate([counts, np.ones(new, dtype=np.int64)])
        p = counts / M_prev
        if s:
            p = p * (1 + s) / (1 + s * p)
        counts = rng.binomial(M, p)
        fixed = int((counts == M).sum())
        return counts[(counts > 0) & (counts < M)], fixed

    for _ in range(burn_in):
        counts, _ = step(counts, M_prev, M_prev)
    fix = np.empty(T, dtype=np.int64)
    for g in range(T):
        M = 2 * N_of_g(g)
        counts, fix[g] = step(counts, M_prev, M)
        M_prev = M
    return fix
