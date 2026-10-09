"""H3 POST-HOC REVIEW FIX PASS (written 2026-10-08 after the three H3 reviews; NOT pre-registered).
Answers REVIEW-R4-H3-correctness M1-M4, m8, m9 and the steelman requests for long windows, M < 0.1 and hard load
at larger K.  Reuses run() from the pre-registered h3_human_scale.py UNCHANGED (loaded by path; python -I drops the
script directory from sys.path).  Nothing here changes a pre-registered prediction; all output is post hoc.

Run:  research/.venv/bin/python -I research/checks/h3_fixpass.py STAGE [workers]
  STAGE in  L  long-window hazard, s = 0.01   (K=1000, free, R in {1.1,1.5,2,3}, x = lam/lam* grid, 100k gens)
            W  long-window hazard, s = 0.003  (R in {1.1,2}, x in 0.5-1.25, 50k gens, burn 6k)
            X  s = 0.001 probe                 (R in {1.1,2}, x in 0.75-1.25, 30k gens, burn 15k)
            M  finite supply M in {0.01,0.03,0.3} (stage-C model; 20k gens)
            H  hard load at K = 4000 / 10000    (U = 2.2: R in {10,20}; U = 0.35: R in {1.5,2})
            wfD2  single-locus cost with the exact -2 ln wbar charge, with SEs (fixes the 2 s q bias)
            pk    packet model: deterministic sweep-load pulses + ceiling demography (mechanism check for phi < 1)
            report  hazard / survival-over-T tables from L, W, X (and M, H summaries)
Seeds: SeedSequence([20261052, stage_code, cell, rep]).  Output: results/raw/h3_fx_<STAGE>.{jsonl,out}, h3_fx_report.*
Hazard: constant-hazard estimate h = deaths / exposure (generations from t = 0, burn-in included), exact Poisson 95% CI;
survival over T: S(T) = exp(-h T); zero deaths -> h < 3.0/exposure (one-sided 95%).
Expectations written before these runs (informal): long-window phi(T = 252k) at s = 0.01 below the 10k-window phi
(R = 1.1 lowest); s = 0.003 nearer the mean-field cap but with deaths at x ~ 1; D rises steeply as M falls below 0.1;
hard U = 2.2 at R = 20 persists at K >= 4000 at lam = 0 (reviewer scratch), extinct at R <= 9 by ln R < U.
"""
import os
import sys
import json
import math
import time
import importlib.util
import numpy as np
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("h3", os.path.join(HERE, "h3_human_scale.py"))
h3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h3)
RAW = h3.RAW
SEED = 20261052
CODES = {"L": 1, "W": 2, "X": 3, "M": 4, "H": 5, "smoke": 0}


def cells(stage):
    c = []      # (K, s, lam, R, U, load, linkage, M_sup, label, reps, gens, burn)
    if stage == "L":
        for R in (1.1, 1.5, 2.0, 3.0):
            xs = (0.15, 0.3, 0.45, 0.6, 0.75) if R <= 1.5 else (0.3, 0.45, 0.6, 0.75)
            for x in xs:
                c.append((1000, 0.01, x * math.log(R) / h3.Dpred(1000), R, 0.0, "none", "free", None, f"x={x}", 8, 100000, 2000))
    if stage == "W":
        for R in (1.1, 2.0):
            for x in (0.5, 0.75, 1.0, 1.25):
                c.append((1000, 0.003, x * math.log(R) / h3.Dpred(1000), R, 0.0, "none", "free", None, f"x={x}", 6, 50000, 6000))
    if stage == "X":
        for R in (1.1, 2.0):
            for x in (0.75, 1.0, 1.25):
                c.append((1000, 0.001, x * math.log(R) / h3.Dpred(1000), R, 0.0, "none", "free", None, f"x={x}", 4, 30000, 15000))
    if stage == "M":
        for M in (0.01, 0.03, 0.3):
            Dg = 15.2 + 0.6 / M          # rough guess from stage C (M = 0.1 gave D ~ 17-22); D_obs is the output
            for R in (1.1, 1.5, 2.0):
                for x in (0.25, 0.5, 1.0):
                    c.append((1000, 0.01, x * math.log(R) / Dg, R, 0.0, "none", "free", M, f"M={M} xg={x}", 8, 20000, 3000))
    if stage == "H":
        for K, reps in ((4000, 4), (10000, 3)):
            for R in ((10.0, 20.0) if K == 4000 else (20.0,)):
                for xh in (0.0, 0.5):
                    lam = xh * (math.log(R) - 2.2) / h3.Dpred(K)
                    c.append((K, 0.01, lam, R, 2.2, "hard", "map36", None, f"U=2.2 K={K} xh={xh}", reps, 3000, 1000))
        for R in (1.5, 2.0):
            for xh in (0.0, 0.5):
                lam = xh * (math.log(R) - 0.35) / h3.Dpred(4000)
                c.append((4000, 0.01, lam, R, 0.35, "hard", "map36", None, f"U=0.35 K=4000 xh={xh}", 4, 6000, 1500))
    if stage == "smoke":
        c.append((1000, 0.001, 0.02, 2.0, 0.0, "none", "free", None, "smoke", 1, 300, 100))
        c.append((4000, 0.01, 0.0, 20.0, 2.2, "hard", "map36", None, "smoke", 1, 40, 10))
        c.append((1000, 0.01, 0.002, 1.5, 0.0, "none", "free", 0.01, "smoke", 1, 300, 50))
    return c


def job(a):
    stage, ci, (K, s, lam, R, U, load, link, M, lab, reps, gens, burn), rep = a
    rng = np.random.default_rng(np.random.SeedSequence([SEED, CODES[stage], ci, rep]))
    t0 = time.time()
    r = h3.run(K, s, lam, R, U, load, link, gens, burn, rng, M_sup=M)
    r.update(dict(stage=stage, cell=ci, K=K, s=s, lam=lam, R=R, U=U, load=load, linkage=link, M_sup=M, x=lab,
                  rep=rep, gens=gens, burn=burn, sec=time.time() - t0, D_pred=h3.Dpred(K),
                  lam_star=(math.log(R) - (U if load == "hard" else 0.0)) / h3.Dpred(K)))
    return r


def run_stage(stage, workers):
    jobs = [(stage, ci, c, rep) for ci, c in enumerate(cells(stage)) for rep in range(c[9])]
    jobs.sort(key=lambda a: -(a[2][2] + 1e-3) * a[2][10] * a[2][0] / max(a[2][1], 1e-3) ** 0.5)
    rows = []
    t0 = time.time()
    with Pool(workers) as pool, open(os.path.join(RAW, f"h3_fx_{stage}.jsonl"), "w") as f:
        for r in pool.imap_unordered(job, jobs, chunksize=1):
            rows.append(r)
            f.write(json.dumps(r) + "\n")
            f.flush()
    print(f"stage {stage}: {len(jobs)} runs, {time.time()-t0:.0f} s wall", flush=True)
    sm = h3.summarize(rows)
    json.dump(sm, open(os.path.join(RAW, f"h3_fx_{stage}_summary.json"), "w"), indent=1)
    for x in sm:
        print({k: (round(v, 5) if isinstance(v, float) else v) for k, v in x.items() if k != "stage"}, flush=True)


# ------------------------------------------------------------------------------------------- hazard / report
def chi2_ppf_poisson(k, upper):
    """Exact Poisson 95% CI for a count k (Garwood), via scipy if present."""
    from scipy.stats import chi2
    if upper:
        return chi2.ppf(0.975, 2 * k + 2) / 2
    return chi2.ppf(0.025, 2 * k) / 2 if k > 0 else 0.0


def hazard_table(stage):
    p = os.path.join(RAW, f"h3_fx_{stage}.jsonl")
    if not os.path.exists(p):
        return []
    rows = [json.loads(l) for l in open(p)]
    import collections
    g = collections.defaultdict(list)
    for r in rows:
        g[r["cell"]].append(r)
    out = []
    for ci in sorted(g):
        rs = g[ci]
        r0 = rs[0]
        total = r0["burn"] + r0["gens"]
        deaths = sum(r["ext"] for r in rs)
        expo = sum((r["t_ext"] + 1) if r["ext"] else total for r in rs)
        h = deaths / expo
        hlo = chi2_ppf_poisson(deaths, False) / expo
        hhi = chi2_ppf_poisson(deaths, True) / expo
        S = {T: (math.exp(-h * T), math.exp(-hhi * T), math.exp(-hlo * T)) for T in (146250, 252000, 450000)}
        alive = [r for r in rs if not r["ext"]]
        out.append(dict(stage=stage, cell=ci, R=r0["R"], s=r0["s"], K=r0["K"], M_sup=r0["M_sup"], U=r0["U"],
                        load=r0["load"], x=r0["x"], lam=r0["lam"], lam_star=r0["lam_star"],
                        x_num=r0["lam"] / r0["lam_star"] if r0["lam_star"] > 0 else float("nan"),
                        reps=len(rs), deaths=deaths, exposure=expo, h=h, h_lo=hlo, h_hi=hhi,
                        S252k=S[252000][0], S252k_lo=S[252000][1], S252k_hi=S[252000][2],
                        S146k=S[146250][0], S450k=S[450000][0],
                        t_ext=sorted(r["t_ext"] for r in rs if r["ext"]),
                        D_alive=float(np.mean([r["D"] for r in alive if r["D"] == r["D"]])) if alive else float("nan"),
                        D_all=float(np.nanmean([r["D"] if r["D"] is not None else np.nan for r in rs])),
                        k_over_lam=float(np.mean([r["k"] for r in alive])) / r0["lam"] if alive and r0["lam"] > 0 else float("nan"),
                        nfrac=float(np.mean([r["nfrac"] for r in alive])) if alive else float("nan"),
                        Ld=float(np.mean([r["Ld"] for r in rs]))))
    return out


def phi_long(rows, T=252000, Starget=0.5):
    """Per (stage, R): x at which the estimated S(T) crosses Starget (log-h linear interpolation between the last cell
    with S >= target and the first with S < target, using the point estimate; zero-death cells use h = 0).
    Returns (x_cross, x_lo_bracket, x_hi_bracket)."""
    import collections
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["stage"], r["R"], r["s"])].append(r)
    res = {}
    hT = -math.log(Starget) / T
    for key, rs in g.items():
        rs = sorted(rs, key=lambda r: r["x_num"])
        cross = (float("nan"), float("nan"), float("nan"))
        if rs[0]["h"] > hT:
            cross = (float("nan"), 0.0, rs[0]["x_num"])
        else:
            for a, b in zip(rs, rs[1:]):
                if a["h"] <= hT < b["h"]:
                    la = math.log(max(a["h"], 1e-9))
                    lb = math.log(b["h"])
                    w = (math.log(hT) - la) / (lb - la) if lb > la else 0.5
                    w = min(max(w, 0.0), 1.0)
                    cross = (a["x_num"] + w * (b["x_num"] - a["x_num"]), a["x_num"], b["x_num"])
                    break
            else:
                cross = (float("nan"), rs[-1]["x_num"], float("inf"))
        res[key] = cross
    return res


def report():
    allrows = []
    lines = []
    for st in ("L", "W", "X", "M", "H"):
        rows = hazard_table(st)
        allrows += rows
        if not rows:
            continue
        lines.append(f"== stage {st}: hazard per cell (deaths/exposure), S(252k) [95% CI], D_alive, k/lam, N/K, t_ext")
        for r in rows:
            lines.append(f"  R={r['R']:<5} s={r['s']:<6} K={r['K']:<6} M={str(r['M_sup']):5s} U={r['U']:<4} {r['load']:4s} "
                         f"{r['x']:22s} lam={r['lam']:.5f} x={r['x_num']:.2f} dead {r['deaths']}/{r['reps']} "
                         f"h={r['h']:.2e} [{r['h_lo']:.1e},{r['h_hi']:.1e}] S252k={r['S252k']:.3f} "
                         f"[{r['S252k_lo']:.3f},{r['S252k_hi']:.3f}] D={r['D_alive']:.2f} k/l={r['k_over_lam']:.2f} "
                         f"N/K={r['nfrac']:.3f} Ld={r['Ld']:.2f} t_ext={r['t_ext']}")
    pl = phi_long([r for r in allrows if r["stage"] in ("L", "W", "X")])
    lines.append("\n== long-run phi: x = lam/lam* at which S(252,000) = 0.5 under constant hazard (bracket = grid cells)")
    for k in sorted(pl):
        lines.append(f"  stage {k[0]} R={k[1]} s={k[2]}: phi_252k = {pl[k][0]:.3f}  bracket [{pl[k][1]:.2f}, {pl[k][2]:.2f}]")
    pl146 = phi_long([r for r in allrows if r["stage"] in ("L", "W", "X")], T=146250)
    pl450 = phi_long([r for r in allrows if r["stage"] in ("L", "W", "X")], T=450000)
    for nm, d in (("146,250", pl146), ("450,000", pl450)):
        lines.append(f"== long-run phi for T = {nm}")
        for k in sorted(d):
            lines.append(f"  stage {k[0]} R={k[1]} s={k[2]}: phi = {d[k][0]:.3f}  bracket [{d[k][1]:.2f}, {d[k][2]:.2f}]")
    # R_min with long-run phi (s = 0.01): interpolate phi(R) in ln R; for R > 3 hold at phi(3)
    lines.append("\n== R_min = smallest R with phi_T(R) ln R >= D K_a / T (s = 0.01, stage L; phi held at phi(3) beyond R = 3;"
                 " phi(R) linear in ln R; soft load)")
    out_rmin = []
    for T, d in ((146250, pl146), (252000, pl), (450000, pl450)):
        pts = sorted((k[1], v[0]) for k, v in d.items() if k[0] == "L" and k[2] == 0.01 and v[0] == v[0])
        if len(pts) < 2:
            continue

        def phiR(R):
            if R <= pts[0][0]:
                return pts[0][1] if R >= pts[0][0] * 0.999 else pts[0][1]
            if R >= pts[-1][0]:
                return pts[-1][1]
            for (a, pa), (b, pb) in zip(pts, pts[1:]):
                if a <= R <= b:
                    w = (math.log(R) - math.log(a)) / (math.log(b) - math.log(a))
                    return pa + w * (pb - pa)

        for D in (5, 10, 20, 30):
            cells_ = []
            for Ka in (1e3, 3e3, 1e4, 1e5, 1e6):
                need = D * Ka / T
                R = 1.0005
                while R < 1e12 and phiR(R) * math.log(R) < need:
                    R *= 1.002
                cells_.append(R if R < 1e12 else float("inf"))
                out_rmin.append(dict(T=T, D=D, Ka=Ka, Rmin=cells_[-1]))
            lines.append(f"  T={T} D={D}: " + "  ".join(f"K_a={Ka:.0e}: {R:.3g}" for Ka, R in zip((1e3, 3e3, 1e4, 1e5, 1e6), cells_)))
        lines.append(f"    phi_T(R) points used: {[(a, round(b, 3)) for a, b in pts]}")
    txt = "\n".join(lines)
    print(txt)
    open(os.path.join(RAW, "h3_fx_report.out"), "w").write(txt + "\n")
    json.dump(dict(hazard=allrows, phi252k={str(k): v for k, v in pl.items()},
                   phi146k={str(k): v for k, v in pl146.items()}, phi450k={str(k): v for k, v in pl450.items()},
                   Rmin=out_rmin), open(os.path.join(RAW, "h3_fx_report.json"), "w"), indent=1)


# ------------------------------------------------------------------------------------------- wfD2 (exact charge)
def wf_D_exact(N, S2N, reps, rng):
    M = 2 * N
    s = S2N / M
    es = math.exp(-s)
    k = np.ones(reps, dtype=np.int64)
    cost = np.zeros(reps)
    alive = np.ones(reps, bool)
    fixed = np.zeros(reps, bool)
    while alive.any():
        a = np.flatnonzero(alive)
        p = k[a] / M
        m = p + (1 - p) * es
        cost[a] += -2.0 * np.log(m)                 # exact -ln wbar (HWE, log-additive), as in the IBM and D_det
        k[a] = rng.binomial(M, p / m)
        fx = k[a] == M
        ls = k[a] == 0
        fixed[a[fx]] = True
        alive[a[fx | ls]] = False
    nf = int(fixed.sum())
    tot = cost.sum() / nf if nf else float("nan")
    # SE of the ratio sum(cost)/nfix by the delta method over replicates (each replicate: (cost_i, fixed_i))
    if nf:
        c = cost
        f = fixed.astype(float)
        mc, mf = c.mean(), f.mean()
        var = (np.var(c) / mf ** 2 + mc ** 2 * np.var(f) / mf ** 4 - 2 * mc * np.cov(c, f)[0, 1] / mf ** 3) / reps
        se_tot = math.sqrt(max(var, 0.0))
    else:
        se_tot = float("nan")
    return dict(N=N, twoNs=S2N, s=s, reps=reps, nfix=nf,
                D_fix=float(cost[fixed].mean()) if nf else float("nan"),
                D_fix_se=float(cost[fixed].std() / math.sqrt(nf)) if nf > 1 else float("nan"),
                D_total_per_fix=tot, D_total_se=se_tot, two_ln_2N=2 * math.log(2 * N))


def wfD2():
    rows = []
    for i, (N, S) in enumerate([(1000, 1), (1000, 4), (1000, 10), (1000, 40), (1000, 100), (1000, 400),
                                (1000, 2000), (10000, 10), (10000, 100), (10000, 2000)]):
        rng = np.random.default_rng(np.random.SeedSequence([SEED, 9, i]))
        reps = 400000 if S <= 10 else 60000
        r = wf_D_exact(N, S, reps, rng)
        rows.append(r)
        print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}), flush=True)
    with open(os.path.join(RAW, "h3_fx_wfD2.jsonl"), "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


# ------------------------------------------------------------------------------------------- packet model (m8)
def packet(R, x, s=0.01, K=1000, gens=12000, reps=400, seed=0):
    """Deterministic sweep-load pulses arriving Poisson(lam); each pulse = the deterministic log-load trajectory
    -2 ln(p + q e^-s) from p0 = 1/2K to 1 - 1/2K (total = 2 ln 2K = D_pred).  Demography: ln N' = min(ln N + ln R, ln K)
    - L_t (no demographic noise, no drift); extinct if N < 20.  Returns the fraction persisting `gens` generations."""
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 7, int(R * 1000), int(x * 1000), seed]))
    p, traj = 1 / (2 * K), []
    es = math.exp(-s)
    while p < 1 - 1 / (2 * K):
        m = p + (1 - p) * es
        traj.append(-2 * math.log(m))
        p = p / m
    traj = np.array(traj)
    Lp = len(traj)
    lam = x * math.log(R) / (2 * math.log(2 * K))
    arrivals = rng.poisson(lam, size=(reps, gens)).astype(float)
    # load[:, t] = sum_k arrivals[:, t - k] * traj[k]  (same model; FFT convolution replaces the original O(gens*Lp)
    # Python loop, which was too slow -- edit made after the first launch, before any pk output existed)
    from scipy.signal import fftconvolve
    load = np.maximum(fftconvolve(arrivals, traj[None, :], axes=1), 0.0)
    lnN = np.full(reps, math.log(K))
    alive = np.ones(reps, bool)
    lnR, lnK, lnE = math.log(R), math.log(K), math.log(20)
    for t in range(gens):
        lnN = np.minimum(lnN + lnR, lnK) - load[:, t]
        alive &= lnN >= lnE
    return float(alive.mean())


def pk():
    out = []
    for R in (1.05, 1.1, 1.2, 1.5, 2.0, 3.0):
        xs = np.round(np.arange(0.1, 1.31, 0.05), 3)
        ps = [packet(R, float(x)) for x in xs]
        x50 = float("nan")
        for (x1, p1), (x2, p2) in zip(zip(xs, ps), zip(xs[1:], ps[1:])):
            if p1 >= 0.5 > p2:
                x50 = float(x1 + (x2 - x1) * (p1 - 0.5) / (p1 - p2))
                break
        out.append(dict(R=R, phi_packet=x50, curve=[(float(a), b) for a, b in zip(xs, ps)]))
        print(f"R={R}: packet-model phi(12k gens incl. burn) = {x50:.3f}", flush=True)
    json.dump(out, open(os.path.join(RAW, "h3_fx_pk.json"), "w"), indent=1)


if __name__ == "__main__":
    st = sys.argv[1] if len(sys.argv) > 1 else "report"
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    os.makedirs(RAW, exist_ok=True)
    if st == "report":
        report()
    elif st == "wfD2":
        wfD2()
    elif st == "pk":
        pk()
    else:
        run_stage(st, w)
