"""Two-lineage / sourced-demography extensions to wf.py (THROWAWAY, non-product). wf.py is untouched.

Infinite-sites, unlinked sites, neutral. U = genome-wide mutation rate per gamete per generation.
Scaling rule (E4): N_sim = N/f, T_sim = T/f, U_sim = U*f, so N*U, T*U and T/N are invariant (theta fixed).
Everything reported is a ratio to U*T or a per-site value converted with mu*f/U_sim.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np


def burn_in(N, U, gens, rng):
    """Equilibrium ancestral state: counts (out of 2N) of segregating alleles; fixed/lost removed."""
    M = 2 * N
    c = np.empty(0, dtype=np.int64)
    for _ in range(gens):
        new = rng.poisson(M * U)
        if new:
            c = np.concatenate([c, np.ones(new, dtype=np.int64)])
        c = rng.binomial(M, c / M)
        c = c[(c > 0) & (c < M)]
    return c


def schedule(pieces, f, T_real):
    """pieces: [(start_gen_real, Ne_real), ...] sorted. Returns int array N_sim[g] for g in 0..T_sim-1."""
    T_sim = int(round(T_real / f))
    g_real = (np.arange(T_sim) + 0.5) * f
    starts = np.array([p[0] for p in pieces])
    nes = np.array([p[1] for p in pieces], dtype=float)
    idx = np.searchsorted(starts, g_real, side="right") - 1
    return np.maximum(2, np.rint(nes[idx] / f)).astype(np.int64)


def evolve(pre_counts, M0, N_arr, U, rng, checkpoints=()):
    """Evolve one lineage from a split. pre_counts = ancestral segregating alleles (counts of M0).
    N_arr[g] = diploid size in generation g. checkpoints = generations (1-based, <= len(N_arr)) to snapshot.
    Returns dict gen -> snapshot (always includes final)."""
    n_pre = len(pre_counts)
    ids = np.arange(n_pre)
    cur = pre_counts.astype(np.int64).copy()
    absorbed = np.full(n_pre, np.nan)       # final freq (0 or 1) of absorbed pre-split alleles
    post = np.empty(0, dtype=np.int64)
    post_fixed = 0
    pre_fixed = 0
    M_prev = M0
    T = len(N_arr)
    cps = set(checkpoints) | {T}
    snaps = {}
    for g in range(1, T + 1):
        M = 2 * int(N_arr[g - 1])
        new = rng.poisson(M_prev * U)
        if new:
            post = np.concatenate([post, np.ones(new, dtype=np.int64)])
        if cur.size:
            cur = rng.binomial(M, cur / M_prev)
        if post.size:
            post = rng.binomial(M, post / M_prev)
        m = (cur == 0) | (cur == M)
        if m.any():
            fx = cur[m] == M
            absorbed[ids[m]] = fx
            pre_fixed += int(fx.sum())
            cur = cur[~m]
            ids = ids[~m]
        fxp = post == M
        post_fixed += int(fxp.sum())
        post = post[(post > 0) & (post < M)]
        M_prev = M
        if g in cps:
            freq = absorbed.copy()
            freq[ids] = cur / M_prev
            snaps[g] = dict(pre_freq=freq, pre_fixed=pre_fixed, post_fixed=post_fixed,
                            post_seg_sum=float((post / M_prev).sum()), n_post_seg=int(post.size))
    return snaps


def pair_stats(sH, sC):
    """Expected pairwise differences between one random haplotype from each lineage, and fixed-difference
    count, from snapshots of the two lineages (infinite sites). Returns dict of counts (sim units)."""
    fH, fC = sH["pre_freq"], sC["pre_freq"]
    d_pre = float((fH * (1 - fC) + fC * (1 - fH)).sum())
    fixdiff_pre = float((((fH == 1) & (fC == 0)) | ((fH == 0) & (fC == 1))).sum())
    d_post = sH["post_seg_sum"] + sC["post_seg_sum"] + sH["post_fixed"] + sC["post_fixed"]
    fixdiff_post = sH["post_fixed"] + sC["post_fixed"]
    d = d_pre + d_post
    fixdiff = fixdiff_pre + fixdiff_post
    return dict(d=d, fixdiff=fixdiff, polydiff=d - fixdiff, d_pre=d_pre, fixdiff_pre=fixdiff_pre,
                fixdiff_post=fixdiff_post)
