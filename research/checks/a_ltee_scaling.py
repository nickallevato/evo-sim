"""A-sim / LTEE scaling (A, A2, A2e, A5b, A5d, A5f, E7). THROWAWAY check.

Run: research/.venv/bin/python -I research/checks/a_ltee_scaling.py   (seed 20261008; ~15-25 min, 11 cores)

PRE-REGISTERED PREDICTIONS (from docs/research/claims/A-mittens-formula.md, A2e, A5b, A5d, A5f, E7; written before the run):
 Day (A2e/A5d): fixation rate saturates near the LTEE value 1/G_f (G_f 1,322-1,587) regardless of supply and
   recombination; response to 100x supply is sublinear (8.5-17x, strict 19.7x -> exponent a = 0.47-0.64) because
   fixation is "bottlenecked by the dynamics of sweeps", not supply. Day's side expects a ~ 0.5 in BOTH asexual and
   recombining populations.
 Critics (A5b, KITTENS): rate linear in supply (a = 1); with free recombination a -> 1 at low supply and falls <1
   only at high supply; recombining populations exceed the LTEE rate at 94,000x supply.
 This audit's third possibility (A5b): sublinear a = 0.5-0.6, 80-450x gap remains.
 Additional pre-registration (mine, written before running; theory: Gerrish-Lenski 1998 / Desai-Fisher 2007, from memory):
   (1) In an ASEXUAL population with LTEE-scale Ne (3.3e7, assumption: not in parameters.yaml, unverified; sensitivity
       1e7-1e8 reported) and single s, the fixation rate saturates logarithmically in beneficial supply, so the local
       exponent a = dln k/dln U_b is < 1 and declines with U_b; a 100x supply increase gives a ratio in the 2-6x range
       for fixed-s (a ~ 0.3-0.4), i.e. BELOW Day's 8.5-17x (because Day's mutators also have a DFE and
       diminishing-returns structure that this one-parameter model lacks).
   (2) Sublinearity is a property of linkage, not of 'evolution': the same parameters with free recombination should
       give k ~ independent-sites 2N*U_b*u(s) (exponent ~1) until the active zone is very crowded (F2).
   (3) Standard scaling (M/c, c*s, c*U) leaves k/c invariant (validated here before use, E4).
 Falsifiers: a asexual local exponent >= 0.9 at LTEE-like parameters would favour KITTENS' linear illustration for
 the asexual case; k_free/k_clonal <= 1.2 at LTEE-calibrated parameters would support 'LTEE ceiling is not
 asexual-specific'.
Method: haploid-equivalent WF, M = 2N copies, genic selection exp(s*k), k = number of beneficial mutations.
 For a clonal population with one s, the exact multinomial class-count process over k ('fitness classes') is the same
 stochastic model as wf_f2.sim(mode='clonal') (validated below) and costs O(#classes) per generation, so it reaches
 Ne = 3.3e7. Fixation rate = d<k>/dt (every fixation adds one mutation to everyone; long-run identity).
"""
import os, sys, time, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import wf_f2 as w
from wf import kimura_u

SEED = 20261008


def class_rate(M, U, s, T, burn, rng, nblocks=5):
    """Clonal fixed-s: returns (rate, se_blocks, mean_classes). Rate = d<k>/dt over [burn, burn+T]."""
    n = np.zeros(8, dtype=np.int64); n[0] = M
    off = 0.0            # mutation count of class index 0
    marks = []
    ncls = 0.0
    nrec = 0
    checkpoints = {burn + int(T * i / nblocks) for i in range(nblocks + 1)}
    for g in range(burn + T + 1):
        if n[-1] > 0:
            n = np.append(n, 0)
        idx = np.arange(len(n))
        mean = (n * idx).sum() / M
        if g in checkpoints and g >= burn:
            marks.append(off + mean)
        if g == burn + T:
            break
        wgt = n * np.exp(s * (idx - mean))
        stay = wgt * (1 - U)
        flow = np.zeros_like(stay); flow[1:] = wgt[:-1] * U
        p = stay + flow
        p = p / p.sum()
        n = rng.multinomial(M, p)
        nz = np.flatnonzero(n)
        lo = nz[0]
        if lo > 0:
            n = n[lo:]; off += lo
        if g >= burn and g % 100 == 0:
            ncls += (n > 0).sum(); nrec += 1
    marks = np.array(marks)
    d = np.diff(marks) / (T / nblocks)
    return d.mean(), d.std(ddof=1) / np.sqrt(len(d)), ncls / max(nrec, 1)


def rate_task(a):
    tag, M, U, s, T, burn, rep = a
    rng = np.random.default_rng(np.random.SeedSequence([SEED, zlib.crc32(tag.encode()) % 100003, rep]))
    r, se, nc = class_rate(M, U, s, T, burn, rng)
    return tag, rep, r, se, nc


def pooled(rs):
    r = np.array([x[2] for x in rs]); se = np.array([x[3] for x in rs])
    m = r.mean()
    sem = max(r.std(ddof=1) / np.sqrt(len(r)) if len(r) > 1 else 0, np.sqrt((se ** 2).sum()) / len(r))
    return m, sem


def run_tasks(pool, tasks):
    out = pool.map(rate_task, tasks, chunksize=1)
    d = {}
    for o in out:
        d.setdefault(o[0], []).append(o)
    return {k: pooled(v) for k, v in d.items()}


def calib_task(a):
    s, G = a
    Ne = 3.3e7
    lo, hi = 1e-10, 1e-6
    for it in range(7):
        mid = np.sqrt(lo * hi)
        ks = [class_rate(int(Ne), mid, s, 150000, 60000, np.random.default_rng(np.random.SeedSequence([SEED, 5, it, r])))[0] for r in range(2)]
        if np.mean(ks) < 1.0 / G: lo = mid
        else: hi = mid
    return np.sqrt(lo * hi)


def ind_task(a):
    M, MU, s, rep = a
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 7, int(MU * 10), rep]))
    return MU, w.sim(M, MU / M, s, 'clonal', 20000, 3000, rng)['rate']


def main():
    t0 = time.time()
    pool = Pool(int(os.environ.get("NPROC", "3")))
    print("## 0. Validation: class process vs individual-based wf_f2 (clonal, M=2000, s=0.01)")
    ind = pool.map(ind_task, [(2000, MU, 0.01, r) for MU in (0.5, 2, 8) for r in range(4)])
    tasks = [("val%g" % MU, 2000, MU / 2000, 0.01, 40000, 3000, r) for MU in (0.5, 2, 8) for r in range(4)]
    cl = run_tasks(pool, tasks)
    print("| 2N*U_b | individual-based rate (SE) | class process rate (SE) | indep. 2NUu | z |")
    print("|---|---|---|---|---|")
    for MU in (0.5, 2, 8):
        v = [x[1] for x in ind if x[0] == MU]
        m, se = w.mean_se(v)
        c, cse = cl["val%g" % MU]
        print("| %g | %.4g (%.2g) | %.4g (%.2g) | %.4g | %.2f |" % (
            MU, m, se, c, cse, w.indep_rate(2000, MU / 2000, 0.01), (m - c) / np.hypot(se, cse)))

    print("\n## 1. Scaling validation (E4): (M, s, U) -> (M/c, c*s, c*U); prediction k/c invariant")
    tasks = []
    for MU in (2, 20):
        for c in (1, 2, 4, 8):
            M = 128000 // c; s = 0.00125 * c; U = MU / M
            T = int(2e5 / c) ; burn = int(6e4 / c)
            for r in range(3):
                tasks.append(("sc%g_%d" % (MU, c), M, U, s, T, burn, r))
    sc = run_tasks(pool, tasks)
    print("| M*U | c | M | s | k (per gen) | k/c (SE) | indep/c |")
    print("|---|---|---|---|---|---|---|")
    for MU in (2, 20):
        for c in (1, 2, 4, 8):
            M = 128000 // c; s = 0.00125 * c
            m, se = sc["sc%g_%d" % (MU, c)]
            print("| %g | %d | %d | %.5f | %.4g | %.4g (%.2g) | %.4g |" % (MU, c, M, s, m, m / c, se / c, w.indep_rate(M, MU / M, s) / c))

    print("\n## 2. LTEE calibration: Ne = 3.3e7 (assumption), find U_b with k = 1/1322 (and 1/1587), asexual")
    Ne = 3.3e7
    res = {}
    combos = [(0.003, 1322), (0.01, 1322), (0.03, 1322), (0.01, 1587)]
    for (s, G), U in zip(combos, pool.map(calib_task, combos)):
        res[(s, G)] = U
        print("s=%g target G_f=%d -> U_b=%.3g per genome per gen" % (s, G, U), flush=True)
    print("(U_b as fraction of the LTEE total supply 4.1e-4: " + ", ".join("s=%g: %.2g" % (s, res[(s, 1322)] / 4.1e-4) for s in (0.003, 0.01, 0.03)) + ")")

    print("\n## 3. Supply response at LTEE M, asexual vs independent-sites (EXTRAPOLATION: assumes R_int=1 for free recombination, beyond F2 tested range)")
    print("| s | U_b mult | 2N*U_b | clonal k | SE | G_f clonal | indep k0 | G_f indep | k0/k (interference factor) | local exponent to next row |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    summary = {}
    for s in (0.003, 0.01, 0.03):
        U0 = res[(s, 1322)]
        mults = [1, 3, 10, 30, 100, 1000, 10000, 94000]
        tasks = []
        for mm in mults:
            T = int(max(1e5, min(8e5, 150 / max(1e-4, 1 / 1322 * mm ** 0.5)))) if mm <= 100 else 40000
            for r in range(4):
                tasks.append(("sup%g_%g" % (s, mm), Ne, U0 * mm, s, T, 60000 if mm <= 100 else 30000, r))
        sr = run_tasks(pool, tasks)
        ks = [sr["sup%g_%g" % (s, mm)] for mm in mults]
        for i, mm in enumerate(mults):
            k, se = ks[i]
            k0 = w.indep_rate(int(Ne), U0 * mm, s)
            ex = (np.log(ks[i + 1][0] / k) / np.log(mults[i + 1] / mm)) if i + 1 < len(mults) else float('nan')
            print("| %g | %g | %.3g | %.4g | %.2g | %.0f | %.4g | %.0f | %.1f | %s |" % (
                s, mm, Ne * U0 * mm, k, se, 1 / k, k0, 1 / k0, k0 / k, "%.2f" % ex if ex == ex else ""), flush=True)
        summary[s] = (mults, ks)
        k1 = ks[0][0]; k100 = ks[mults.index(100)][0]
        print("  -> s=%g: 100x supply -> %.2fx (a = %.2f); 94,000x -> %.0fx (a = %.2f); Day 8.5-17x (a 0.47-0.61), strict 19.7x (a 0.65); linear = 100x / 94,000x" % (
            s, k100 / k1, np.log(k100 / k1) / np.log(100), ks[-1][0] / k1, np.log(ks[-1][0] / k1) / np.log(94000)), flush=True)

    print("\n## 4. Sensitivity to Ne (s=0.01, U_b fixed at the Ne=3.3e7 calibration): k vs M")
    U0 = res[(0.01, 1322)]
    tasks = [("ne%g" % M, M, U0, 0.01, 400000, 60000, r) for M in (1e6, 3.3e6, 1e7, 3.3e7, 1e8) for r in range(4)]
    ne = run_tasks(pool, tasks)
    for M in (1e6, 3.3e6, 1e7, 3.3e7, 1e8):
        m, se = ne["ne%g" % M]
        print("M=%g: k=%.4g (SE %.2g), G_f=%.0f" % (M, m, se, 1 / m if m > 0 else float('inf')))
    print("\nelapsed %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
