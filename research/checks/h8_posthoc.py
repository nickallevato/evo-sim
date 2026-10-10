"""H8/H5 post hoc analysis -- post hoc, after reviews 2935b8f.

Answers the three reviews of R4-H8 (REVIEW-R4-H8-{correctness,steelman-day,steelman-critic}.md).  Reads only the
existing raw file results/raw/h8_main.jsonl (745 rows); runs no simulation.  Trivial size (one process, < 1 s).
Nothing here was pre-registered; every number it prints is labelled post hoc in R4-H8.md section 8.

Estimators are copied verbatim (logic) from h8_haldane_regime.py at af09e77 (lam50: first crossing from >= 0.5 to
< 0.5, log-linear interpolation; D_obs: median over persisting reps of cells with x <= 0.8).  "Pre-registered
cells" are cell index < 107 (the acd3a9e grid: 72 hard + 16 Kscale + 15 softJ + 4 softWF); 107-142 are the
appended post hoc cells (af09e77).

Prints:
  A. hard K = 1000, per R, all rows vs pre-registered cells only: D_obs (n), lam50 + bracket per window,
     D = 30 and D = 20 intervals, and the mean-field (phi = 1) interval D / ln R.
  B. Kscale lam50 * D_obs per K (both cell sets) and the P1 slope dD/dlnK.
  C. bracket-implied ranges for the near-threshold scores (PD1 40k, PC2 R = 2, P3 10k, P6 d = 0.45 40k, Term 3
     at R = e).
  D. min persisting-rep k/lam over sustained cells, with post hoc flag.
  E. open-locus counts and implied sum of per-locus selection coefficients (nopen * s to nopen * 2s) next to
     maxrel and Crow's I, in hard, softJ and softWF cells.
  F. softJ per-generation log load k * D_obs and the implied mean viability relative to the optimum.
"""
import collections
import json
import math
import os
import sys

import numpy as np

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw", "h8_main.jsonl")
NPRE = 107
S = 0.01
CHECKS = (10000, 20000, 40000)
HOSSJER = 15800 / 450000


def Dref(K):
    return 2 * math.log(2 * K) + 2


def lam50(pts):
    if not pts:
        return float("nan"), (float("nan"), float("nan")), "none"
    if pts[0][1] < 0.5:
        return float("nan"), (0.0, pts[0][0]), f"< {pts[0][0]:.4g}"
    for (l1, f1), (l2, f2) in zip(pts, pts[1:]):
        if f1 >= 0.5 > f2:
            u = (f1 - 0.5) / (f1 - f2)
            return math.exp(math.log(l1) + u * (math.log(l2) - math.log(l1))), (l1, l2), f"[{l1:.4g}, {l2:.4g}]"
    return float("nan"), (pts[-1][0], float("inf")), f"> {pts[-1][0]:.4g}"


def groups(rows):
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["arm"], r["K"], round(r["lam"], 8), None if r["R"] != r["R"] else round(r["R"], 6), r["label"])].append(r)
    return g


def est(g, arm, K, R):
    cells = sorted([(k[2], v) for k, v in g.items() if k[0] == arm and k[1] == K and k[3] == R])
    lnR = math.log(R)
    Ds = [r["D"] for lam, v in cells for r in v
          if lam <= 0.8 * lnR / Dref(K) * 1.0001 and r["fail"] is None and r["D"] == r["D"]]
    Dm = float(np.median(Ds)) if Ds else float("nan")
    out = {}
    for T in CHECKS:
        pts = []
        for lam, v in cells:
            vv = [r for r in v if str(T) in r["alive"]]
            if vv:
                pts.append((lam, sum(r["alive"][str(T)] for r in vv) / len(vv)))
        if pts:
            out[T] = lam50(pts)
    return Dm, len(Ds), out


def iv(l, D, Dt):
    return 1.0 / (l * D / Dt) if l and l == l and D == D and l != float("inf") else float("nan")


def main():
    rows = [json.loads(l) for l in open(RAW)]
    pre = [r for r in rows if r["cell"] < NPRE]
    print(f"rows {len(rows)}; pre-registered-cell rows {len(pre)}; appended {len(rows) - len(pre)}")
    sets = (("all", groups(rows)), ("pre", groups(pre)))
    Rs = sorted({k[3] for k in sets[0][1] if k[0] == "hard"})

    print("\n## A. hard K = 1000: all rows vs pre-registered cells only")
    print("| R | set | D_obs (n) | T | lam50 | bracket | D=30 interval [bracket] | D=20 | mean-field 30/lnR |")
    print("|---|---|---|---|---|---|---|---|---|")
    A = {}
    for R in Rs:
        for name, g in sets:
            Dm, n, out = est(g, "hard", 1000, R)
            for T in CHECKS:
                if T not in out:
                    continue
                l, (lo, hi), br = out[T]
                A[(R, name, T)] = (l, lo, hi, Dm)
                print(f"| {R:.3f} | {name} | {Dm:.2f} ({n}) | {T} | {l:.4g} | {br} | {iv(l, Dm, 30):.0f} "
                      f"[{iv(hi, Dm, 30):.0f}, {iv(lo, Dm, 30):.0f}] | {iv(l, Dm, 20):.0f} | {30 / math.log(R):.0f} |")

    print("\n## B. Kscale lam50 * D_obs (both sets) and P1 slope")
    for name, g in sets:
        for R in (round(1 / 0.9, 6), 2.0):
            line, Dk = [], {}
            for K in (500, 1000, 4000):
                arm = "hard" if K == 1000 else "Kscale"
                Dm, n, out = est(g, arm, K, R)
                Dk[K] = Dm
                line.append(f"K={K}: D={Dm:.2f}(n={n}) " +
                            " ".join(f"{T // 1000}k:{out[T][0] * Dm:.4f}" for T in (10000, 20000) if T in out))
            sl = (Dk[4000] - Dk[500]) / math.log(8) if Dk[500] == Dk[500] else float("nan")
            print(f"{name} R={R:.3f}: " + " | ".join(line) + f" | slope {sl:.2f}")

    print("\n## C. near-threshold scores, bracket-implied ranges (all rows)")
    R11, R2, Re, R3 = round(1 / 0.9, 6), 2.0, round(math.e, 6), 3.0
    l, lo, hi, D = A[(R11, "all", 40000)]
    print(f"PD1 40k: interval {iv(l, D, 30):.0f}, bracket [{iv(hi, D, 30):.0f}, {iv(lo, D, 30):.0f}] vs cut 600")
    for T in CHECKS:
        l, lo, hi, D = A[(R2, "all", T)]
        print(f"PC2 R=2 {T // 1000}k: rescaled multiple of 1/300 = {l * D / 30 * 300:.2f}x "
              f"[{lo * D / 30 * 300:.2f}, {hi * D / 30 * 300:.2f}] vs 6x; in-model {l * 300:.1f}x "
              f"[{lo * 300:.1f}, {hi * 300:.1f}] vs 10x")
    l, lo, hi, D = A[(R11, "all", 10000)]
    print(f"P3 R=1.111 10k: interval {iv(l, D, 30):.0f} [{iv(hi, D, 30):.0f}, {iv(lo, D, 30):.0f}] vs 250-400")
    for T in CHECKS:
        l, lo, hi, D = A[(R2, "all", T)]
        print(f"P6 d=0.45 (0.0296) R=2 {T // 1000}k: lam50 {l:.4f} [{lo:.4f}, {hi:.4f}]")
    for R in (Re, R3):
        for T in CHECKS:
            l, lo, hi, D = A[(R, "all", T)]
            print(f"Term3 0.0658 vs R={R:.3f} {T // 1000}k: lam50 {l:.4f} [{lo:.4f}, {hi:.4f}] "
                  f"shortfall {100 * (1 - l / 0.0658):.0f}% [{100 * (1 - hi / 0.0658):.0f}, {100 * (1 - lo / 0.0658):.0f}]")

    print("\n## D. persisting-rep k/lam, lowest cells (survival >= 0.5 at end of window, >= 1 persisting rep)")
    g = sets[0][1]
    kl = []
    for k, v in g.items():
        per = [r for r in v if r["fail"] is None]
        if per and len(per) / len(v) >= 0.5:
            kl.append((float(np.mean([r["k"] / r["lam"] for r in per])), k, len(per), len(v), v[0]["cell"] >= NPRE))
    kl.sort()
    for x in kl[:6]:
        print(f"k/lam {x[0]:.3f} {x[1]} persisting {x[2]}/{x[3]} posthoc={x[4]}")
    print(f"max k/lam {kl[-1][0]:.3f} {kl[-1][1]}")
    kl_all = sorted((float(np.mean([r['k'] / r['lam'] for r in v if r['fail'] is None])), k, v[0]["cell"] >= NPRE)
                    for k, v in g.items() if any(r["fail"] is None for r in v))
    print("min over any cell with a persisting rep:", " ; ".join(f"{a:.3f} {b} posthoc={c}" for a, b, c in kl_all[:4]))

    print("\n## E. open loci, implied sum of s_i, maxrel, Crow's I (persisting reps, all rows)")
    sel = []
    for k, v in g.items():
        arm = k[0]
        if arm in ("softWF", "softJ") or (arm == "hard" and k[3] in (R3, Re, R2) and k[4] in ("x=0.8", "x=1.0")):
            per = [r for r in v if r["fail"] is None]
            if per:
                m = lambda f: float(np.mean([r[f] for r in per]))
                sel.append((arm, k[3], k[2], k[4], m("nopen"), m("maxrel"), m("q99"), m("I"), m("k") / k[2],
                            m("D")))
    print("| arm | R | lam | label | nopen | sum s_i (het..hom) | maxrel | q99 | I | k/lam | D_obs |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for a in sorted(sel, key=lambda t: (t[0], t[1] or 0, t[2])):
        print(f"| {a[0]} | {a[1]} | {a[2]:.4g} | {a[3]} | {a[4]:.0f} | {a[4] * S:.2f}..{a[4] * 2 * S:.2f} | "
              f"{a[5]:.3f} | {a[6]:.3f} | {a[7]:.2e} | {a[8]:.2f} | {a[9]:.1f} |")

    print("\n## F. softJ per-generation log load k * D_obs and exp(-load)")
    for a in sorted(sel, key=lambda t: (t[0], t[1] or 0, t[2])):
        if a[0] == "softJ":
            load = a[8] * a[2] * a[9]
            print(f"softJ R={a[1]} lam={a[2]:.4g}: k*D_obs = {load:.2f} log units -> exp(-load) = {math.exp(-load):.2e}; "
                  f"D_obs/hard-D(~16.8) = {a[9] / 16.8:.1f}x")
    return 0


if __name__ == "__main__":
    sys.exit(main())
