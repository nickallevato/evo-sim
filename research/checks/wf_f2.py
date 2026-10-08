"""Multi-locus beneficial-mutation Wright-Fisher helpers for F2 / A-sim (THROWAWAY, non-product).
Does not modify wf.py.

Model (haploid-equivalent bookkeeping, see glossary): M = 2N gene copies; every copy carries a set of
beneficial mutations (infinite sites). Genic fitness exp(sum s_i), which for additive h=0.5 diploid
selection with per-copy s is the same single-locus dynamics (u = (1-e^{-2s})/(1-e^{-2Ms}), identical to
wf.kimura_u(N, s)). U = beneficial mutations per gene copy per generation (U_b).
Modes of reproduction:
  'clonal' : offspring copies one parent (asexual)
  'free'   : each site independently from either of two parents (r=1/2 between all sites)
  float R  : R = genome map length in Morgans; Poisson(R) uniform crossovers between two parents
Soft selection: fixed M, parents drawn proportional to fitness.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from wf import kimura_u  # noqa: E402


def sim(M, U, s, mode, T, burn, rng, dfe_mean=None, s_max=None, record_every=50):
    """Run one replicate. Returns dict(fix_per_gen, n_mid, n_seg, T_obs, n_fix).

    s: fixed selection coefficient per new mutation, unless dfe_mean is given (exponential DFE with that
       mean, truncated at s_max if given).
    """
    cap = 256
    G = np.zeros((cap, M), dtype=np.uint8)
    sv = np.zeros(cap)
    pos = np.zeros(cap)
    K = 0
    lf = np.zeros(M)                       # log fitness per copy (relative)
    n_fix = 0
    mid_acc = 0.0
    seg_acc = 0.0
    rec_n = 0
    for g in range(burn + T):
        # --- selection + reproduction
        w = np.exp(lf - lf.max())
        cw = np.cumsum(w)
        cw /= cw[-1]
        a = np.searchsorted(cw, rng.random(M))
        a[a >= M] = M - 1
        if K > 0:
            if mode == 'clonal':
                G[:K, :] = np.take(G[:K, :], a, axis=1)
                lf = lf[a]
            else:
                b = np.searchsorted(cw, rng.random(M))
                b[b >= M] = M - 1
                Ga = np.take(G[:K, :], a, axis=1)
                Gb = np.take(G[:K, :], b, axis=1)
                if mode == 'free':
                    mask = rng.random((K, M), dtype=np.float32) < 0.5
                else:
                    R = float(mode)
                    nb = rng.poisson(R, M)
                    tot = int(nb.sum())
                    if tot == 0:
                        mask = np.zeros((K, M), dtype=bool)
                    else:
                        idx = np.repeat(np.arange(M), nb)
                        x = rng.random(tot)
                        order = np.argsort(pos[:K])
                        sp = pos[:K][order]
                        rk = np.searchsorted(sp, x)             # first sorted column with pos > x
                        D = np.zeros((K + 1, M), dtype=np.int16)
                        np.add.at(D, (rk, idx), 1)
                        cnt_sorted = np.cumsum(D, axis=0)[:K]
                        inv = np.empty(K, dtype=np.int64)
                        inv[order] = np.arange(K)
                        mask = (cnt_sorted[inv] & 1).astype(bool)   # odd #breaks before column -> from b
                G[:K, :] = np.where(mask, Gb, Ga)
                lf = sv[:K] @ G[:K, :]
        else:
            lf = np.zeros(M)
        # --- mutation
        nm = rng.poisson(M * U)
        if nm:
            if K + nm > cap:
                newcap = max(cap * 2, K + nm + 64)
                G2 = np.zeros((newcap, M), dtype=np.uint8); G2[:K] = G[:K]; G = G2
                sv2 = np.zeros(newcap); sv2[:K] = sv[:K]; sv = sv2
                p2 = np.zeros(newcap); p2[:K] = pos[:K]; pos = p2
                cap = newcap
            who = rng.integers(0, M, nm)
            if dfe_mean is None:
                svals = np.full(nm, s)
            else:
                svals = rng.exponential(dfe_mean, nm)
                if s_max is not None:
                    svals = np.minimum(svals, s_max)
            for j in range(nm):
                G[K + j, :] = 0
                G[K + j, who[j]] = 1
            sv[K:K + nm] = svals
            pos[K:K + nm] = rng.random(nm)
            np.add.at(lf, who, svals)
            K += nm
        # --- bookkeeping
        if K:
            cnt = G[:K, :].sum(axis=1, dtype=np.int64)
            fixed = cnt == M
            lost = cnt == 0
            if g >= burn:
                n_fix += int(fixed.sum())
            keep = ~(fixed | lost)
            if not keep.all():
                kk = int(keep.sum())
                G[:kk] = G[:K][keep]
                sv[:kk] = sv[:K][keep]
                pos[:kk] = pos[:K][keep]
                cnt = cnt[keep]
                K = kk
            if g >= burn and (g - burn) % record_every == 0:
                f = cnt / M
                mid_acc += float(((f > 0.1) & (f < 0.9)).sum())
                seg_acc += K
                rec_n += 1
        elif g >= burn and (g - burn) % record_every == 0:
            rec_n += 1
    return dict(n_fix=n_fix, T_obs=T, rate=n_fix / T, n_mid=mid_acc / max(rec_n, 1),
                n_seg=seg_acc / max(rec_n, 1))


def indep_rate(M, U, s):
    """Independent-sites prediction 2N*U_b*u(s) = M*U*u."""
    return M * U * kimura_u(M // 2, s)


def desai_fisher_k(M, U, s):
    """Desai & Fisher (2007) successional-mutations speed v = s^2 (2 ln(Ms) - ln(s/U)) / ln^2(s/U)
    (formula recalled from memory, regime Ms>>1, U<<s; NOT verified against the paper); k = v/s."""
    L = np.log(s / U)
    v = s * s * (2 * np.log(M * s) - L) / (L * L)
    return v / s


def mean_se(x):
    x = np.asarray(x, float)
    return x.mean(), (x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float('nan'))
