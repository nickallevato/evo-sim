"""H3 post-processing (POST HOC: written after seeing stage A/V output; reads raw files only, runs no simulation).
Computes lam50 (interpolated 50%-persistence rate) per (stage, linkage, load, U, K, s, M, R), the fluctuation factor
phi = lam50 / lam*, and the human-scale extrapolation K_max = phi * T * (ln R - U_hard) / D for D in {10, 20, 30}.
Run: research/.venv/bin/python -I research/checks/h3_tables.py  > research/checks/results/raw/h3_tables.out
"""
import os
import json
import math
import collections

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw")


def wilson(k, n, z=1.96):
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, c - h), min(1.0, c + h)


def lam50(pts):
    """pts: sorted list of (lam, persist). First downward crossing of 0.5, linear in lam. Returns (lam50, lo, hi)
    where lo/hi are the bracketing lam values."""
    for (l1, p1), (l2, p2) in zip(pts, pts[1:]):
        if p1 >= 0.5 > p2:
            return l1 + (l2 - l1) * (p1 - 0.5) / (p1 - p2), l1, l2
    if pts and pts[0][1] < 0.5:
        return float("nan"), 0.0, pts[0][0]
    return float("nan"), pts[-1][0] if pts else float("nan"), float("inf")


def main():
    groups = collections.defaultdict(list)
    for st in ("V", "A", "B", "C", "S"):
        p = os.path.join(RAW, f"h3_{st}_summary.json")
        if not os.path.exists(p):
            continue
        for r in json.load(open(p)):
            key = (st, r["linkage"], r["load"], r["U"], r["K"], r["s"], r["M_sup"], r["R"])
            groups[key].append(r)
    rows = []
    print("stage link load U K s M R | lam50 [bracket] lam* phi=lam50/lam* | lam50 x 300 | points (lam:persist)")
    for key in sorted(groups, key=lambda k: tuple(str(x) for x in k)):
        rs = sorted(groups[key], key=lambda r: r["lam"])
        pts = [(r["lam"], r["persist"]) for r in rs]
        l50, lo, hi = lam50(pts)
        ls = rs[0]["lam_star"]
        if key[6] is not None:          # finite supply: lam* uses D + 1/M
            ls = math.log(key[7]) / (2 * math.log(2 * key[4]) + 1 / key[6])
        phi = l50 / ls if ls > 0 and not math.isnan(l50) else float("nan")
        rows.append(dict(stage=key[0], linkage=key[1], load=key[2], U=key[3], K=key[4], s=key[5], M=key[6], R=key[7],
                         lam50=l50, lo=lo, hi=hi, lam_star=ls, phi=phi))
        ptxt = " ".join(f"{l:.4f}:{p:.2f}" for l, p in pts)
        print(f"{key[0]} {key[1]:5s} {key[2]:4s} {key[3]:4} {key[4]:5} {key[5]:5} {str(key[6]):4s} R={key[7]:<5} | "
              f"{l50:.5f} [{lo:.5f},{hi:.5f}] {ls:.5f} phi={phi:.2f} | {l50*300:.2f} | {ptxt}")
    json.dump(rows, open(os.path.join(RAW, "h3_tables.json"), "w"), indent=1)

    # pooled phi (stage A, free + map36 pooled per R) and human extrapolation
    print("\nPooled stage-A persistence (free + map36, 16 reps per lam point where both exist) and phi:")
    pooled = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
    for key, rs in groups.items():
        if key[0] != "A":
            continue
        for r in rs:
            a = pooled[key[7]][round(r["lam"], 6)]
            a[0] += round(r["persist"] * r["reps"])
            a[1] += r["reps"]
    phis = {}
    for R in sorted(pooled):
        pts = sorted((l, k / n) for l, (k, n) in pooled[R].items())
        l50, lo, hi = lam50(pts)
        ls = math.log(R) / (2 * math.log(2000))
        phis[R] = l50 / ls
        ci = " ".join(f"{l:.4f}:{k}/{n}[{wilson(k, n)[0]:.2f},{wilson(k, n)[1]:.2f}]" for l, (k, n) in sorted(pooled[R].items()))
        print(f"  R={R:<5} lam50={l50:.5f} (bracket {lo:.5f}-{hi:.5f}) lam*={ls:.5f} phi={phis[R]:.2f}  lam50/(1/300)={l50*300:.2f}")
        print(f"      {ci}")
    print("\nHuman-scale extrapolation (soft load; D = 2 ln 2N validated by stage V; phi from K = 1000, 10,000-gen window):")
    print("  K_max = phi(R) * T * ln R / D   [mean-field phi=1 in brackets]")
    ext = []
    for T in (146250, 252000, 450000):
        for R in sorted(phis):
            cells = []
            for D in (10, 20, 30):
                km = phis[R] * T * math.log(R) / D
                k1 = T * math.log(R) / D
                ext.append(dict(T=T, R=R, D=D, phi=phis[R], K_max=km, K_max_meanfield=k1))
                cells.append(f"D={D}: {km:7.0f} [{k1:7.0f}]")
            print(f"  T={T} R={R:<5} " + "  ".join(cells))
    json.dump(dict(phi=phis, extrap=ext), open(os.path.join(RAW, "h3_extrap.json"), "w"), indent=1)


def logit_lam50():
    """Review fix m1 (post hoc): binomial logistic fit of persistence on ln(lam) over the pooled stage-A points
    (free + map36), per R.  lam50 = exp(-a/b); 95% CI by profile likelihood on ln lam50 (overdispersion ignored)."""
    import numpy as np
    from scipy.optimize import minimize
    from scipy.stats import chi2
    pooled = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
    for st in ("A",):
        for r in json.load(open(os.path.join(RAW, f"h3_{st}_summary.json"))):
            a = pooled[r["R"]][round(r["lam"], 7)]
            a[0] += round(r["persist"] * r["reps"])
            a[1] += r["reps"]
    out = {}
    print("\nLogistic fit (pooled stage A; persistence ~ logit(b (ln lam - ln lam50))), 95% profile CI:")
    for R in sorted(pooled):
        pts = sorted(pooled[R].items())
        x = np.array([math.log(l) for l, _ in pts])
        k = np.array([v[0] for _, v in pts], float)
        n = np.array([v[1] for _, v in pts], float)

        def nll(m, b):
            z = b * (x - m)
            p = 1 / (1 + np.exp(z))          # persistence falls with lam (b > 0)
            p = np.clip(p, 1e-12, 1 - 1e-12)
            return -float(np.sum(k * np.log(p) + (n - k) * np.log(1 - p)))
        best = minimize(lambda v: nll(v[0], math.exp(v[1])), [float(np.median(x)), 1.0], method="Nelder-Mead",
                        options=dict(xatol=1e-6, fatol=1e-8, maxiter=5000))
        m0, b0 = best.x[0], math.exp(best.x[1])
        L0 = best.fun
        crit = chi2.ppf(0.95, 1) / 2

        def prof(m):
            return minimize(lambda v: nll(m, math.exp(v[0])), [math.log(b0)], method="Nelder-Mead").fun - L0
        grid = np.linspace(m0 - 1.0, m0 + 1.0, 801)
        ok = [g for g in grid if prof(g) <= crit]
        lo, hi = math.exp(min(ok)), math.exp(max(ok))
        out[R] = dict(lam50=math.exp(m0), lo=lo, hi=hi, slope=b0)
        print(f"  R={R:<5} lam50(10k) = {math.exp(m0):.5f}  95% CI [{lo:.5f}, {hi:.5f}]  x300 = {300*math.exp(m0):.2f} "
              f"[{300*lo:.2f}, {300*hi:.2f}]  phi = {math.exp(m0)/(math.log(R)/(2*math.log(2000))):.3f}")
    json.dump(out, open(os.path.join(RAW, "h3_logit_lam50.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
    logit_lam50()
