"""E4 -- relictation: exact Markov chains for Day & Athos's Cannings "jackpot" model (Z23188201).

THROWAWAY research check.  Run:  research/.venv/bin/python -I research/checks/e4_relictation_chain.py
(exact linear algebra; one seeded MC cross-check; raw output -> research/checks/results/raw/e4_relictation_chain.out)

CLAIMS (verbatim; sources/raw/day/zenodo-23188201.txt, untrusted local copy, read only):
  Abstract: "The fixation probability p = 1/(2N) is protected by the martingale property and holds exactly regardless
    of offspring distribution." / "When that compression fails and a single family can replace more than ~10% of the
    population, the formula t = 4Ne breaks in quantifiable ways. Below 10% replacement, the formula holds to within the
    few-percent finite-size offset of the Wright-Fisher chain itself" / "From 15% to 85% replacement ... actual fixation
    times exceed 4Ne by up to 7-25% at 2N = 20-50, an excess that keeps growing with population size."
  s2 model: "in each generation, with probability p_jackpot, one randomly chosen individual survives and its offspring
    replace a specified fraction f of the population, that is, round(f . 2N) of the other gene copies. The remaining
    copies reproduce deterministically (each contributing one offspring), and in a generation without a jackpot nothing
    changes. Ne is the variance effective size, computed from the one-generation variance of the frequency change."
    "At jackpot probability 0.1 ... The ratio does not depend on the jackpot probability, which only rescales time. The
    98% row is complete replacement at all three sizes: the family replaces all 2N - 1 other copies."
  s2 table t/4Ne at 2N = 20/30/50: 5% .950/.983/.993; 10% .968/.999/1.033; 20% 1.003/1.048/1.100; 30% 1.035/1.091/
    1.160; 50% 1.071/1.146/1.239; 60% 1.068/1.148/1.249; 80% .976/1.060/1.173; 90% .950/.966/1.023; 98% .5/.5/.5.
    WF chain "0.932, 0.952, and 0.970"; "the Moran model gives exactly 1 - 1/(2N)".
  s2: "at 50% replacement the ratio reaches 1.36 at 2N = 100 and 1.74 at 2N = 800, about 0.125 per doubling" / "at 10%
    replacement the ratio is 1.033 at 2N = 50 but 1.179 at 2N = 800, while for a fixed family of six it returns toward
    the drift baseline as the population grows (1.045 at 2N = 60, 1.013 at 2N = 480)."
  s3: "In eigenvalue terms, the slowest-decaying mode is untouched: its rate is exactly 1/(2Ne) ... At 50% replacement
    the decay rates stand in the ratio 1 : 2 : 2.7 : 3.2 : 3.4 rather than the diffusion's 1 : 3 : 6 : 10 : 15"
    (thresholds "computed at 2N = 30 with jackpot probability 0.1").
  s1: "A family of 6 offspring in a population of 20 is a 30% replacement event."

WHAT IS WHAT.  Arithmetic/theorem: P_fix = i/2N (martingale; any neutral exchangeable model).  Model result: the
  t/4Ne table and its N-dependence (exact chain; reproducible).  Interpretive/empirical: that the haploid chain with
  replacement fraction f represents "a family of size fN in a population of N" diploids; that vertebrate bottlenecks
  sit in that regime; Viluma 2022 (not tested here).

METHOD.  Haploid 2N copies.  Jackpot (prob pj): parent copy uniform; m = min(round(f 2N), 2N-1) others, uniform without
  replacement, take the parent's type.  If parent is A (prob i/2N): i -> i + HG(2N-1, 2N-i, m); else i -> i - HG(2N-1,
  i, m).  P_fix by linear solve; t = [(I-P_TT)^-1 u](1)/u(1) (Doob h-transform, identical to Day's (I-Q)g = 1).
  Ne_var = x(1-x)/(2 Var(dx)) computed from the matrix at every interior i.  Baselines: WF and Moran exact chains.
  Extra model (NOT Day's): diploid pair-family -- two random parent individuals, K offspring individuals replace K of
  the other N-2 individuals; parental copies HG-sampled (random pairing of copies into individuals each generation,
  an assumption); offspring A count Bin(K, a1/2) + Bin(K, a2/2).  Family share F = K/N.

PRE-REGISTERED PREDICTIONS (written before any run of this script; no timing run preceded them):
  P1 baselines: exact WF t/4N = 0.932/0.952/0.970 at 2N = 20/30/50 (Day's numbers reproduce, +/-0.001); Moran exactly
     1 - 1/(2N); P_fix(1) = 1/(2N) to <= 1e-12 in every chain (martingale; Day's claim holds trivially).
  P2 Day's table reproduces within +/-0.002 in every cell under one of the two rounding conventions (Python round /
     half-up); ratio independent of pj to machine precision.
  P3 Ne_var in the jackpot chain is constant in i and equals 1/(2c), c = pj m(m+1)/(2N(2N-1)) (= coalescent Ne); at
     fixed f it saturates at ~1/(2 pj f^2) as 2N grows (20 at f = 0.5, pj = 0.1): Ne does NOT grow with N.
  P4 at fixed f the ratio keeps growing roughly linearly in log(2N), slope per doubling ~ f^2 ln2 / (2(-ln(1-f)))
     (0.125 at f = 0.5, 0.033 at f = 0.1, 0.017 at f = 0.05) within +/-30% for 2N >= 200 (heuristic: Dirac-Lambda
     coalescent needs ~ln(2N)/(-ln(1-f)) events while 4Ne -> 2/(pj f^2) is N-free).  Day's 1.36 (2N=100) and 1.74
     (2N=800) at f=0.5 and 1.179 (2N=800, f=0.1) reproduce within +/-0.01.  The claim file's "opposing" pre-registration
     (ratio converges to a constant 1.2-1.3 at fixed f) is predicted to FAIL; the claim file's Day-side prediction
     (>= 1.3 at 2N = 100-200) to HOLD.
  P5 at fixed family size m = 6 the ratio returns to the WF/Kingman value as 2N grows (Day's 1.045 at 60, 1.013 at 480
     reproduce); Kingman is recovered whenever m/2N -> 0 (Moehle-Sagitov condition).
  P6 the replacement fraction f* at which the excess over the WF chain reaches +5% is NOT a fixed ~10%: it falls with
     2N (predicted f* ~ 8-12% at 2N = 50, ~3-5% at 2N = 800), so "below 10% the formula holds" is true only at 2N <= ~50.
  P7 eigen decay rates at f = 0.5, 2N = 30: leading rate = c exactly; ratios ~1 : 2 : 2.7 : 3.2 : 3.4 (+/-0.1).
  P8 diploid pair-family model at family share F gives a much smaller excess than the haploid chain at f = F (each
     parental gene copy reaches only ~F/4 of the copies); at 2N <= 50 its peak excess over WF is < 8%, and it matches
     the haploid chain at an f between F/4 and F/2.  I.e. "a family of 6 in 20 is a 30% replacement event" maps to a
     per-copy replacement of ~7.5-15% in the chain's own units.
"""
import os
import time
import json
from math import floor, log

import numpy as np
from scipy.linalg import lu_factor, lu_solve, eigvals
from scipy.stats import binom, hypergeom

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
SEED_ROOT = 20261008
PJ = 0.1  # Day's jackpot probability


def m_of(f, n2, rule):
    x = f * n2
    m = round(x) if rule == "py" else floor(x + 0.5 + 1e-12)
    return int(min(max(m, 0), n2 - 1))


def jackpot_matrix(n2, m, pj=PJ):
    P = np.zeros((n2 + 1, n2 + 1))
    for i in range(n2 + 1):
        P[i, i] += 1 - pj
        if i == 0 or i == n2:
            P[i, i] += pj
            continue
        X = np.arange(0, m + 1)
        px = hypergeom.pmf(X, n2 - 1, n2 - i, m)  # parent A: non-A copies replaced
        ok = px > 0
        np.add.at(P[i], i + X[ok], pj * (i / n2) * px[ok])
        py = hypergeom.pmf(X, n2 - 1, i, m)  # parent a: A copies replaced
        ok = py > 0
        np.add.at(P[i], i - X[ok], pj * ((n2 - i) / n2) * py[ok])
    return P


def wf_matrix(n2):
    i = np.arange(n2 + 1)
    return binom.pmf(i[None, :], n2, i[:, None] / n2)


def moran_matrix(n2):
    """One birth-death step; time unit = 1 step (n2 steps = 1 generation)."""
    P = np.zeros((n2 + 1, n2 + 1))
    for i in range(n2 + 1):
        a = (i / n2) * ((n2 - i) / n2)
        if 0 < i < n2:
            P[i, i + 1] = a
            P[i, i - 1] = a
        P[i, i] = 1 - (2 * a if 0 < i < n2 else 0)
    return P


def diploid_pair_matrix(N, K, pj=PJ, parents_die=False):
    """parents_die=False: parents survive, K offspring replace K of the other N-2 individuals.
    parents_die=True (post-hoc variant): the K offspring replace both parents plus K-2 of the other N-2 (K >= 2)."""
    n2 = 2 * N
    P = np.zeros((n2 + 1, n2 + 1))
    for i in range(n2 + 1):
        P[i, i] += 1 - pj
        if i == 0 or i == n2:
            P[i, i] += pj
            continue
        row = np.zeros(n2 + 1)
        for a in range(0, 5):
            pa = hypergeom.pmf(a, n2, i, 4)
            if pa <= 0:
                continue
            for a1 in range(0, 3):
                pa1 = hypergeom.pmf(a1, 4, a, 2)
                if pa1 <= 0:
                    continue
                a2 = a - a1
                o = np.convolve(binom.pmf(np.arange(K + 1), K, a1 / 2), binom.pmf(np.arange(K + 1), K, a2 / 2))
                if parents_die:
                    r0 = hypergeom.pmf(np.arange(2 * K - 3), n2 - 4, i - a, 2 * K - 4)
                    r = np.zeros(2 * K + 1)
                    r[a:a + len(r0)] = r0  # removed = a parental A copies + others
                else:
                    r = hypergeom.pmf(np.arange(2 * K + 1), n2 - 4, i - a, 2 * K)
                d = np.convolve(o, r[::-1])  # index t -> o - r = t - 2K
                idx = i + np.arange(len(d)) - 2 * K
                ok = (d > 0) & (idx >= 0) & (idx <= n2)
                np.add.at(row, idx[ok], pa * pa1 * d[ok])
        P[i] += pj * row
    return P


def analyse(P, time_unit=1.0):
    n2 = P.shape[0] - 1
    T = slice(1, n2)
    A = np.eye(n2 - 1) - P[T, T]
    lu = lu_factor(A)
    u = lu_solve(lu, P[T, n2])
    w = lu_solve(lu, u)
    tbar = w[0] / u[0] * time_unit
    i = np.arange(1, n2)
    di = np.arange(n2 + 1)[None, :] - i[:, None]
    mean = (P[T] * di).sum(1)
    var = (P[T] * di ** 2).sum(1) - mean ** 2
    x = i / n2
    ne = x * (1 - x) / (2 * var / n2 ** 2)
    return dict(pfix_err=float(np.max(np.abs(u - i / n2))), u1=float(u[0]), tbar=float(tbar),
                ne_min=float(ne.min()), ne_max=float(ne.max()), drift_max=float(np.abs(mean).max()))


def ratio(P, time_unit=1.0, ne_scale=1.0):
    a = analyse(P, time_unit)
    ne = a["ne_min"] * ne_scale
    return a["tbar"] / (4 * ne), a


def mc_check(n2, m, pj, reps, seed_key):
    """Independent copy-level simulation of the jackpot process from one A copy; mean time | fixation."""
    rng = np.random.default_rng(np.random.SeedSequence([SEED_ROOT, *seed_key]))
    pop = np.zeros((reps, n2), bool)
    pop[:, 0] = True
    t = np.zeros(reps)
    done = np.zeros(reps, bool)
    fixed = np.zeros(reps, bool)
    gen = 0
    while not done.all():
        gen += 1
        live = np.nonzero(~done)[0]
        t[live] = gen
        jp = live[rng.random(live.size) < pj]
        if jp.size:
            parent = rng.integers(0, n2, jp.size)
            keys = rng.random((jp.size, n2))
            keys[np.arange(jp.size), parent] = 2.0  # exclude parent
            repl = np.argsort(keys, axis=1)[:, :m]
            ptype = pop[jp, parent]
            rows = np.repeat(jp, m)
            pop[rows, repl.ravel()] = np.repeat(ptype, m)
        cnt = pop[live].sum(1)
        newly_lost = live[cnt == 0]
        newly_fix = live[cnt == n2]
        done[newly_lost] = True
        done[newly_fix] = True
        fixed[newly_fix] = True
    tf = t[fixed]
    return fixed.mean(), tf.mean(), tf.std(ddof=1) / np.sqrt(tf.size), int(tf.size)


def main():
    t0 = time.time()
    out = {}
    pr = print
    sizes = (20, 30, 50)
    fs = (0.05, 0.10, 0.20, 0.30, 0.50, 0.60, 0.80, 0.90, 0.98)
    day = {0.05: (.950, .983, .993), 0.10: (.968, .999, 1.033), 0.20: (1.003, 1.048, 1.100),
           0.30: (1.035, 1.091, 1.160), 0.50: (1.071, 1.146, 1.239), 0.60: (1.068, 1.148, 1.249),
           0.80: (.976, 1.060, 1.173), 0.90: (.950, .966, 1.023), 0.98: (.5, .5, .5)}

    pr("=== P1 baselines ===")
    wf_ratio = {}
    for n2 in (20, 30, 50, 60, 100, 200, 400, 480, 800, 1600, 3200):
        r, a = ratio(wf_matrix(n2))
        wf_ratio[n2] = r
        p = 1 / n2
        diff = -(1 / p) * 2 * n2 * (1 - p) * np.log(1 - p)  # diffusion t from p, 4N = 2*n2
        if n2 <= 100 or n2 == 3200:
            pr(f"WF 2N={n2:5d}: t/4N = {a['tbar']/(2*n2):.4f} (Ne_var {a['ne_min']:.3f}-{a['ne_max']:.3f} vs N={n2//2}); "
               f"diffusion t/4N {diff/(2*n2):.4f}; |u - i/2N| max {a['pfix_err']:.1e}")
    for n2 in sizes:
        a = analyse(moran_matrix(n2), time_unit=1 / n2)
        pr(f"Moran 2N={n2}: t/4Ne = {a['tbar']/(4*a['ne_min']/n2):.5f} (1-1/2N = {1-1/n2:.5f}); "
           f"Ne_var (per step) const? {a['ne_min']:.4f}-{a['ne_max']:.4f}; pfix err {a['pfix_err']:.1e}")
    out["wf_ratio"] = wf_ratio

    pr("\n=== P2 Day's table (pj = 0.1), two rounding conventions ===")
    maxdev = {"py": 0, "hu": 0}
    rows = {}
    for f in fs:
        line = f"f={f:4.2f}:"
        for rule in ("py", "hu"):
            vals = []
            for k, n2 in enumerate(sizes):
                m = m_of(f, n2, rule)
                r, a = ratio(jackpot_matrix(n2, m))
                vals.append((m, r, a["pfix_err"]))
                maxdev[rule] = max(maxdev[rule], abs(r - day[f][k]))
            rows[(f, rule)] = vals
            line += f"  [{rule}] " + " ".join(f"m={m:2d}:{r:.3f}" for m, r, _ in vals)
        line += f"   Day {day[f]}"
        pr(line)
    pr(f"max |dev| vs Day: python-round {maxdev['py']:.4f}; half-up {maxdev['hu']:.4f}")
    pr(f"max pfix error over the table: {max(v[2] for vals in rows.values() for v in vals):.1e}")
    pr("excess over WF chain at same 2N (ratio/WF - 1), python-round:")
    for f in fs:
        pr(f"  f={f:4.2f}: " + "  ".join(f"{rows[(f,'py')][k][1]/wf_ratio[n2]-1:+.3f}" for k, n2 in enumerate(sizes)))
    for pj in (0.01, 0.33, 1.0):
        r, _ = ratio(jackpot_matrix(30, 15, pj))
        pr(f"pj={pj}: 2N=30 f=0.5 ratio {r:.6f}")
    out["day_table"] = {f"{f}_{rule}": v for (f, rule), v in rows.items()}

    pr("\n=== P3 Ne vs c and vs N (pj = 0.1) ===")
    for f in (0.1, 0.5):
        for n2 in (20, 50, 200, 800, 3200):
            m = m_of(f, n2, "py")
            a = analyse(jackpot_matrix(n2, m))
            c = PJ * m * (m + 1) / (n2 * (n2 - 1))
            pr(f"f={f} 2N={n2:5d} m={m:4d}: Ne_var {a['ne_min']:.4f}-{a['ne_max']:.4f}; 1/(2c) = {1/(2*c):.4f}; "
               f"1/(2 pj f^2) = {1/(2*PJ*f*f):.2f}; census N = {n2//2}")

    pr("\n=== P4 growth with 2N at fixed f ===")
    grid = (50, 100, 200, 400, 800, 1600, 3200)
    growth = {}
    for f in (0.05, 0.10, 0.20, 0.50):
        vals = []
        for n2 in grid:
            r, a = ratio(jackpot_matrix(n2, m_of(f, n2, "py")))
            vals.append(r)
        growth[f] = vals
        slopes = np.diff(vals)
        pred = f * f * log(2) / (2 * -log(1 - f))
        pr(f"f={f:4.2f}: " + " ".join(f"{n2}:{v:.3f}" for n2, v in zip(grid, vals)))
        pr(f"        per-doubling increments " + " ".join(f"{s:.4f}" for s in slopes) + f"   heuristic {pred:.4f}")
        pr(f"        vs WF chain: " + " ".join(f"{v/wf_ratio[n2]:.3f}" for n2, v in zip(grid, vals)))
    out["growth"] = {str(k): v for k, v in growth.items()}
    pr("Day: f=0.5 1.36 @100, 1.74 @800; f=0.1 1.179 @800")

    pr("\n=== P5 fixed family size (m = 6 replaced copies) ===")
    for n2 in (20, 30, 60, 120, 240, 480, 960, 1920):
        r, _ = ratio(jackpot_matrix(n2, 6))
        pr(f"2N={n2:5d} (f={6/n2:.4f}): ratio {r:.4f}; WF {ratio(wf_matrix(n2))[0] if n2 not in wf_ratio else wf_ratio[n2]:.4f}")
    pr("Day: 1.045 @60, 1.013 @480")

    pr("\n=== P6 threshold f* where ratio/WF >= 1.05 and where ratio >= 1.05 (scan over integer m) ===")
    for n2 in (20, 30, 50, 100, 200, 400, 800, 1600):
        fstar_rel = fstar_abs = None
        ms = range(1, n2) if n2 <= 200 else sorted(set(np.unique(np.round(np.geomspace(1, n2 - 1, 60)).astype(int))))
        for m in ms:
            r, _ = ratio(jackpot_matrix(n2, m))
            if fstar_rel is None and r / wf_ratio.get(n2, ratio(wf_matrix(n2))[0]) >= 1.05:
                fstar_rel = m / n2
            if fstar_abs is None and r >= 1.05:
                fstar_abs = m / n2
            if fstar_rel is not None and fstar_abs is not None:
                break
        pr(f"2N={n2:5d}: f*(+5% over WF chain) = {fstar_rel}; f*(ratio >= 1.05) = {fstar_abs}")

    pr("\n=== P7 eigen decay rates (2N = 30, pj = 0.1) ===")
    for lab, P in (("jackpot f=0.5", jackpot_matrix(30, 15)), ("jackpot f=0.1", jackpot_matrix(30, 3)),
                   ("WF", wf_matrix(30))):
        ev = np.sort(np.real(eigvals(P[1:30, 1:30])))[::-1]
        rates = 1 - ev
        pr(f"{lab:14s}: leading rate {rates[0]:.6f}; ratios " + " : ".join(f"{x/rates[0]:.2f}" for x in rates[:6]))
    pr(f"c(f=0.5, 2N=30) = {PJ*15*16/(30*29):.6f}; WF 1/(2N) = {1/30:.6f}")

    pr("\n=== P8 diploid pair-family model vs haploid chain at the same family share ===")
    for N in (10, 15, 25):
        n2 = 2 * N
        pr(f"2N={n2} (N={N} individuals); WF ratio {wf_ratio[n2]:.3f}")
        hap_cache = {m: ratio(jackpot_matrix(n2, m))[0] for m in range(1, n2)}
        for K in sorted(set([max(1, round(F * N)) for F in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)])):
            if K > N - 2:
                continue
            rd, ad = ratio(diploid_pair_matrix(N, K))
            rh = hap_cache[min(2 * K, n2 - 1)]
            # haploid f giving the same ratio on the rising branch
            feq = None
            for m in range(1, n2):
                if hap_cache[m] >= rd:
                    feq = m / n2
                    break
            pr(f"   K={K:2d} (F={K/N:.2f}): diploid ratio {rd:.4f} (excess vs WF {rd/wf_ratio[n2]-1:+.3f}, Ne {ad['ne_min']:.2f}, "
               f"pfix err {ad['pfix_err']:.0e}) | haploid f=F: {rh:.4f} ({rh/wf_ratio[n2]-1:+.3f}) | "
               f"haploid f with same ratio (rising branch) ~ {feq}")

    pr("\n=== MC cross-check of the matrix (copy-level simulation; SeedSequence([20261008, 1])) ===")
    pf, mt, se, nf = mc_check(30, 15, PJ, 200_000, (1,))
    a = analyse(jackpot_matrix(30, 15))
    pr(f"2N=30 f=0.5 pj=0.1: MC P_fix {pf:.5f} (1/30 = {1/30:.5f}); MC t|fix {mt:.2f} +/- {se:.2f} (n={nf}); "
       f"exact {a['tbar']:.2f}")

    pr(f"\nwall time {time.time() - t0:.1f} s")
    with open(os.path.join(RAW, "e4_relictation_chain.json"), "w") as fh:
        json.dump(out, fh, default=float)


def time_moments(P):
    """Mean and SD of the fixation time from one copy, conditional on fixation (h-transform, exact)."""
    n2 = P.shape[0] - 1
    T = slice(1, n2)
    u = np.arange(1, n2) / n2
    Q = P[T, T] * u[None, :] / u[:, None]
    A = np.eye(n2 - 1) - Q
    lu = lu_factor(A)
    g1 = lu_solve(lu, np.ones(n2 - 1))
    g2 = lu_solve(lu, np.ones(n2 - 1) + 2 * Q @ g1)
    return g1[0], np.sqrt(g2[0] - g1[0] ** 2)


def supplement():
    """POST HOC (review fix pass, REVIEW-R4-E-*): exact f* by bisection; Day's literal diploid case (20 individuals,
    family of 6); parents-die diploid variant; SD of the conditional fixation time.  NOT pre-registered.
    Run with argument 'supp'."""
    t0 = time.time()
    pr = print
    pr("=== S1 exact threshold f* (smallest integer m with ratio/WF >= 1.05; bisection on the rising branch) ===")
    for n2 in (200, 400, 800, 1600):
        wf = ratio(wf_matrix(n2))[0]
        lo, hi = 1, n2 // 4
        while lo < hi:
            mid = (lo + hi) // 2
            if ratio(jackpot_matrix(n2, mid))[0] / wf >= 1.05:
                hi = mid
            else:
                lo = mid + 1
        pr(f"2N={n2}: m*={lo}, f*={lo/n2:.4f}")
    pr("=== S2 Day's literal example: 20 individuals (2N = 40), family of 6 (F = 0.30) ===")
    wf40 = ratio(wf_matrix(40))[0]
    hap = ratio(jackpot_matrix(40, 12))[0]
    for pdie in (False, True):
        rd, ad = ratio(diploid_pair_matrix(20, 6, parents_die=pdie))
        pr(f"parents_die={pdie}: diploid ratio {rd:.4f} (excess vs WF {rd/wf40-1:+.4f}; pfix err {ad['pfix_err']:.0e})")
    pr(f"WF 2N=40 {wf40:.4f}; haploid chain f=0.30 (m=12): {hap:.4f} ({hap/wf40-1:+.4f})")
    pr("=== S3 parents-die variant across F (2N = 30, 50) ===")
    for N in (15, 25):
        n2 = 2 * N
        wf = ratio(wf_matrix(n2))[0]
        for F in (0.2, 0.3, 0.4, 0.5, 0.6, 0.8):
            K = max(2, round(F * N))
            if K > N - 2:
                continue
            ra = ratio(diploid_pair_matrix(N, K))[0]
            rb = ratio(diploid_pair_matrix(N, K, parents_die=True))[0]
            pr(f"2N={n2} K={K} F={K/N:.2f}: parents survive {ra/wf-1:+.4f}; parents die {rb/wf-1:+.4f} (excess vs WF)")
    pr("=== S4 spread of the conditional fixation time (SD/mean), pj = 0.1 ===")
    for n2 in (20, 30, 50):
        mw, sw = time_moments(wf_matrix(n2))
        line = f"2N={n2}: WF mean {mw:.2f} SD {sw:.2f} (CV {sw/mw:.3f})"
        for f in (0.1, 0.5):
            m, sd = time_moments(jackpot_matrix(n2, m_of(f, n2, "py")))
            line += f" | f={f}: mean {m:.2f} SD {sd:.2f} (CV {sd/m:.3f})"
        pr(line)
    pr(f"wall time {time.time() - t0:.1f} s")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "supp":
        supplement()
    else:
        main()
