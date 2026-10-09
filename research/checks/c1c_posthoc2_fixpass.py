"""C1c POST HOC 2 (review fix pass; NOT pre-registered; written after the main run and after reviews of it).

Reviews: results/REVIEW-R4-C1c-{correctness,steelman-day,steelman-critic}.md.  Everything here is labelled post hoc.  The main
script c1c_call_depth_replacement.py is imported unchanged.  What this script does, with the review finding it answers:

 (1) Correctness M1.  The main run's capture-heterogeneity variants (kappa) drew an independent Gamma multiplier for the MODERN
     bin too, although 82% of that bin is high-coverage shotgun diploid (uniform coverage).  Here kappa applies to the ANCIENT bins
     only (modern uniform) -- "anc" variants -- and the old modern-heterogeneous design is rerun beside it ("modhet") so the
     difference is visible.  kappa in {2, 1, 0.5, 0.25} x min-called-chromosomes m in {1, 10, 20, 40} (a bin with c < m counts as
     missing).  Every output records the full 11-bin profile, so the 0-500 BP count is reported for every variant.
 (2) Correctness M2.  The 10000+ bin is mostly older than 10,500 BP (anno: median 15,572 BP; quartiles 10,835 / 29,458; max
     50,000).  Variant "old": individuals of that bin are drawn at their real dates (7 date groups, weighted by hit probability),
     using the W lineage's allele frequency at that date (W drifted 2200 - (t-10500)/20 generations from the ancestor, recorded at
     checkpoints).  This is a BOUND (older individuals are modelled as lying on the W lineage nearer the ancestor), not a model
     of Upper Palaeolithic populations.  Compared by total-variation distance on all 11 bins and on bins 1-10 renormalised.
 (3) Day review F2/F7, critic review F5.  eps sweep {1e-4, 3e-4, 1e-3, 3e-3} (flat false-minor-call rate on pseudo-haploid calls).
 (4) Day review F6, critic review F1/F2.  Ne axis: Ne = 2 (Day's C5a "near 2"), 8,139 (keruru Bronze-Medieval), 8,139 -> 2e4
     (keruru "roughly doubles"), step schedule (1e4 until 8,000 BP, 1e5 until 4,000 BP, 1e6 after), plus constant 1e4..1e6 and
     growth 1e4->1e6 on the same panel.
 (5) Critic review F3.  S21 events by START band of the fixed allele in the Neolithic pooled sample ([99,100), [95,99), [90,95),
     <90 percent), for all scenarios.
 (6) Day review F12.  "mod524": modern bin with the unscaled 524 anno individuals (94 pseudo-haploid + 430 diploid) instead of the
     rescaled 625.
 (7) Analysis only: S21/eligible ratio (density-robust) from the main runs.

Run:  research/.venv/bin/python -I research/checks/c1c_posthoc2_fixpass.py dates <anno> <out.json>
      research/.venv/bin/python -I research/checks/c1c_posthoc2_fixpass.py run <rep> [outdir]
      research/.venv/bin/python -I research/checks/c1c_posthoc2_fixpass.py analyse [rawdir]
Raw: results/raw/c1c2_rep<rep>.json.   Seeds: SeedSequence([ROOT, 2, rep, ...]).  One sampling draw per variant.
"""
import os
import sys
import json
import time
import csv
import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import c1c_call_depth_replacement as m1

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = 20261012
NB, MOD = m1.NB, m1.MOD
OLD_JSON = os.path.join(HERE, "results", "c1c_old_bin_dates.json")
# date groups for the 10000+ bin: (upper BP bound, checkpoint BP)
GROUPS = [(11500, 10500), (13500, 12000), (17500, 15000), (25000, 20000), (35000, 30000), (45000, 40000), (1e9, 50000)]
CKPT_GENS = [int(round(m1.PRE_GENS["W"] - (t - 10500) / 20.0)) for _, t in GROUPS]   # W generations of drift at each checkpoint


def build_dates(anno_path, out_json):
    def fl(x):
        try:
            return float(x)
        except ValueError:
            return None
    w = np.zeros(len(GROUPS))
    ds = []
    with open(anno_path, encoding="latin-1", newline="") as f:
        rd = csv.reader(f, delimiter="\t")
        next(rd)
        for row in rd:
            if len(row) < 41:
                continue
            d, la, lo, hit = fl(row[9]), fl(row[16]), fl(row[17]), fl(row[22])
            if None in (d, la, lo, hit) or not (35 <= la <= 72 and -25 <= lo <= 45) or row[15] in m1.NON_EUROPE or d < 10000:
                continue
            gid = row[0]
            if (".DG" in gid) or gid.endswith(".HO"):
                continue
            for g, (ub, _) in enumerate(GROUPS):
                if d < ub:
                    w[g] += hit
                    break
            ds.append(d)
    out = dict(groups=[dict(upper_bp=min(ub, 1e9), ckpt_bp=t, w_gens=gg, frac=float(w[i] / w.sum())) for i, ((ub, t), gg) in enumerate(zip(GROUPS, CKPT_GENS))],
               n=len(ds), median=float(np.median(ds)), q25=float(np.percentile(ds, 25)), q75=float(np.percentile(ds, 75)), max=float(max(ds)))
    with open(out_json, "w") as f:
        json.dump(out, f, indent=1)
    return out


# ------------------------------------------------------------------------------------------------ panel with W checkpoints
def make_panel_ckpt(rng):
    y0 = rng.random(m1.NS)
    N2 = 2 * m1.NE_PRE
    src = {}
    ck = {}
    for k in ("W", "A", "S"):
        x = y0.copy()
        for g in range(1, m1.PRE_GENS[k] + 1):
            x = m1.drift(x, N2, rng)
            if k == "W" and g in CKPT_GENS:
                ck[g] = x.copy()
        src[k] = x
    return src, [ck[g] for g in CKPT_GENS]


# ------------------------------------------------------------------------------------------------ Ne schedules (N2 array, index = generation step)
def sched(kind, T=525):
    t = np.arange(T + 1)
    bp = 10500 - 20 * t
    if kind[0] == "const":
        ne = np.full(T + 1, kind[1], float)
    elif kind[0] == "grow":
        ne = kind[1] * (kind[2] / kind[1]) ** (t / T)
    elif kind[0] == "step":
        ne = np.where(bp > 8000, 1e4, np.where(bp > 4000, 1e5, 1e6))
    return np.maximum(2, np.rint(2 * ne)).astype(np.int64)


def sim2(src, traj, R, N2):
    gy = 20
    x = src["W"].copy()
    pulses = {}
    if m1.REPL[R] is not None:
        mA, mS = m1.pulse_fractions(R)
        for t in m1.A_PULSES_BP:
            st = int(round((m1.START_BP - t) / gy))
            pulses.setdefault(st, []).append((mA, traj["A"][st]))
        for t in m1.S_PULSES_BP:
            st = int(round((m1.START_BP - t) / gy))
            pulses.setdefault(st, []).append((mS, traj["S"][st]))
    rec = {int(round((m1.START_BP - b[2]) / gy)): i for i, b in enumerate(m1.BINS)}
    xb = np.empty((NB, len(x)), dtype=np.float32)
    xb[rec[0]] = x
    for t in range(1, max(rec) + 1):
        x = _drift(N2[t], x)
        for m, y in pulses.get(t, ()):
            x = (1 - m) * x + m * y
        if t in rec:
            xb[rec[t]] = x
    return xb


_RNG = {}


def _drift(n2, x):
    return _RNG["r"].binomial(n2, np.clip(x, 0.0, 1.0)) / n2


# ------------------------------------------------------------------------------------------------ sampling
def sample2(xb, depth, rng, kappa=None, eps=0.0, kappa_mod=None, xold=None, fold=None):
    S = xb.shape[1]
    a = np.empty((NB, S), dtype=np.int32)
    c = np.empty((NB, S), dtype=np.int32)
    w_anc = 1.0 if kappa is None else rng.gamma(kappa, 1.0 / kappa, size=S)
    w_mod = 1.0 if kappa_mod is None else rng.gamma(kappa_mod, 1.0 / kappa_mod, size=S)
    for b in range(NB):
        w = w_mod if b == MOD else w_anc
        dd = depth[b]
        ph = rng.binomial(dd["n_ph"], np.minimum(1.0, dd["p_ph"] * w), size=S) if dd["n_ph"] else np.zeros(S, dtype=np.int64)
        dp = rng.binomial(dd["n_dip"], np.minimum(1.0, dd["p_dip"] * w), size=S) if dd["n_dip"] else np.zeros(S, dtype=np.int64)
        if b == 0 and xold is not None:
            rem, remf = ph.copy(), 1.0
            al = np.zeros(S, dtype=np.int64)
            for g in range(len(fold) - 1):
                ng = rng.binomial(rem, min(1.0, fold[g] / remf))
                x = np.clip(xold[g].astype(np.float64), 0, 1)
                xe = x * (1 - eps) + (1 - x) * eps if eps > 0 else x
                al += rng.binomial(ng, xe)
                rem -= ng
                remf -= fold[g]
            x = np.clip(xold[-1].astype(np.float64), 0, 1)
            xe = x * (1 - eps) + (1 - x) * eps if eps > 0 else x
            al += rng.binomial(rem, xe)
            al += rng.binomial(2 * dp, np.clip(xold[0].astype(np.float64), 0, 1))
            a[b] = al
        else:
            x = np.clip(xb[b].astype(np.float64), 0.0, 1.0)
            xe = x * (1 - eps) + (1 - x) * eps if eps > 0 else x
            a[b] = rng.binomial(ph, xe) + rng.binomial(2 * dp, x)
        c[b] = ph + 2 * dp
    return a, c


def apply_min(a, c, mn):
    if mn <= 1:
        return a, c
    bad = c < mn
    a2, c2 = a.copy(), c.copy()
    a2[bad] = 0
    c2[bad] = 0
    return a2, c2


def s21_start(a, c):
    obs = c > 0
    trk = obs.all(axis=0)
    ap, cp = a[2].astype(np.int64) + a[3], c[2].astype(np.int64) + c[3]
    out = np.zeros((2, 4), dtype=np.int64)
    for j in (1, 0):
        fx = obs & ((a == c) if j == 1 else (a == 0))
        mod = fx[MOD]
        pooled_fx = (cp > 0) & ((ap == cp) if j == 1 else (ap == 0))
        E1 = mod & (cp > 0) & ~pooled_fx
        T2 = fx.argmax(axis=0)
        sel = E1 & (T2 >= 4)
        f = ap / np.maximum(cp, 1)
        f = f if j == 1 else 1 - f
        cat = np.where(f >= 0.99, 0, np.where(f >= 0.95, 1, np.where(f >= 0.90, 2, 3)))
        out[0] += np.bincount(cat[sel], minlength=4)[:4]
        out[1] += np.bincount(cat[sel & trk], minlength=4)[:4]
    return out.tolist()


def record(a, c):
    r = m1.statistic(a, c)
    return dict(all=r["E1T2"]["all"], trk=r["E1T2"]["trk"], start=r["start"]["all"], s21start=s21_start(a, c))


# ------------------------------------------------------------------------------------------------ scenarios
def scen_list():
    L = []
    for R in ("R0", "R2"):
        for ne in (1e4, 1e5, 3e5, 1e6):
            L.append(dict(name="%s_Ne%g" % (R, ne), R=R, kind=("const", ne), full=True))
        L.append(dict(name="%s_grow1e4-1e6" % R, R=R, kind=("grow", 1e4, 1e6), full=True))
        L.append(dict(name="%s_Ne2" % R, R=R, kind=("const", 2), full=False))
        L.append(dict(name="%s_Ne8139" % R, R=R, kind=("const", 8139), full=False))
        L.append(dict(name="%s_grow8139-2e4" % R, R=R, kind=("grow", 8139, 2e4), full=False))
        L.append(dict(name="%s_step1e4-1e5-1e6" % R, R=R, kind=("step",), full=False))
    L.append(dict(name="R1_Ne100000", R="R1", kind=("const", 1e5), full=True))
    L.append(dict(name="R3_Ne100000", R="R3", kind=("const", 1e5), full=True))
    L.append(dict(name="R3_Ne1e+06", R="R3", kind=("const", 1e6), full=True))
    return L


def variants(full):
    V = [("base", dict())]
    if not full:
        return V
    for k in (2.0, 1.0, 0.5, 0.25):
        for mn in (1, 10, 20, 40):
            V.append(("anc_k%g_m%d" % (k, mn), dict(kappa=k, mn=mn)))
    for k in (1.0, 0.5):
        for mn in (1, 20):
            V.append(("modhet_k%g_m%d" % (k, mn), dict(kappa=k, kappa_mod=k, mn=mn)))
    for e in (1e-4, 3e-4, 1e-3, 3e-3):
        V.append(("eps%g" % e, dict(eps=e)))
    V.append(("mod524", dict(depth524=True)))
    V.append(("old", dict(old=True)))
    V.append(("old_eps1e-3", dict(old=True, eps=1e-3)))
    return V


def run_rep(rep, outdir):
    depth = m1.load_depth()
    depth524 = [dict(d) for d in depth]
    depth524[MOD].update(n_ph=94, n_dip=430)
    old = json.load(open(OLD_JSON))
    fold = [g["frac"] for g in old["groups"]]
    t0 = time.time()
    prng = np.random.default_rng(np.random.SeedSequence([ROOT, 2, rep, 1]))
    src, wck = make_panel_ckpt(prng)
    traj = m1.source_trajectories(src, 20, np.random.default_rng(np.random.SeedSequence([ROOT, 2, rep, 2])))
    res = {"meta": {"rep": rep, "NS": m1.NS, "old": old}}
    for si, sc in enumerate(scen_list()):
        _RNG["r"] = np.random.default_rng(np.random.SeedSequence([ROOT, 2, rep, 3, si]))
        xb = sim2(src, traj, sc["R"], sched(sc["kind"]))
        out = {}
        kcache = {}
        for vi, (vn, p) in enumerate(variants(sc["full"])):
            rng = np.random.default_rng(np.random.SeedSequence([ROOT, 2, rep, 4, si, vi]))
            key = (p.get("kappa"), p.get("kappa_mod"), p.get("eps", 0.0), p.get("old", False), p.get("depth524", False))
            # reuse one sampled (a, c) across the m thresholds of the same kappa design
            if key not in kcache:
                kcache = {}
                kcache[key] = sample2(xb, depth524 if p.get("depth524") else depth, rng, p.get("kappa"), p.get("eps", 0.0),
                                      p.get("kappa_mod"), wck if p.get("old") else None, fold if p.get("old") else None)
            a, c = kcache[key]
            a, c = apply_min(a, c, p.get("mn", 1))
            out[vn] = record(a, c)
        res[sc["name"]] = out
        print("rep %d scen %d %s done t=%.0fs" % (rep, si + 1, sc["name"], time.time() - t0), flush=True)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "c1c2_rep%d.json" % rep), "w") as f:
            json.dump(res, f)


# ------------------------------------------------------------------------------------------------ analysis
OBS = np.array(m1.OBS, float)


def analyse(rawdir):
    reps = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(rawdir, "c1c2_rep*.json")))]
    L = []
    P = L.append
    P("post hoc 2: %d reps, NS=%d, one sampling draw per variant" % (len(reps), reps[0]["meta"]["NS"]))
    o = reps[0]["meta"]["old"]
    P("10000+ bin dates (anno, pseudo-haploid individuals >= 10,000 BP): n=%d median %.0f q25 %.0f q75 %.0f max %.0f; hit-weighted group fractions: %s" % (
        o["n"], o["median"], o["q25"], o["q75"], o["max"], ", ".join("%d BP: %.2f" % (g["ckpt_bp"], g["frac"]) for g in o["groups"])))
    P("")
    names = [k for k in reps[0] if k != "meta"]

    def get(n, v):
        rr = [r[n][v] for r in reps if n in r and v in r[n]]
        if not rr:
            return None
        al = np.mean([x["all"] for x in rr], axis=0)
        tr = np.mean([x["trk"] for x in rr], axis=0)
        st = np.mean([x["start"] for x in rr], axis=0)
        s21 = np.mean([x["s21start"][1] for x in rr], axis=0)
        return dict(al=al, tr=tr, st=st, s21st=s21, n=len(rr),
                    s21=tr[4:].sum(), elig_all=al.sum(), elig_trk=tr.sum(), trk=tr.sum() / max(al.sum(), 1), pre=tr[:3].sum() / max(tr.sum(), 1),
                    b10=tr[10], tv=np.abs(tr / max(tr.sum(), 1) - OBS / OBS.sum()).sum() / 2,
                    tv1=np.abs(tr[1:] / max(tr[1:].sum(), 1) - OBS[1:] / OBS[1:].sum()).sum() / 2)

    def row(n, v, label=None):
        g = get(n, v)
        if g is None:
            return None
        return "| %s | %s | %.0f | %.2f | %.3f | %.1f | %.0f | %.2g | %.2f / %.2f |" % (
            n, label or v, g["elig_all"], g["trk"], g["pre"], g["s21"], g["b10"], g["s21"] / max(g["elig_trk"], 1), g["tv"], g["tv1"])
    hdr = "| scenario | variant | eligible (all) | tracked | pre-7000 | S21 (tracked) | 0-500 BP events | S21/eligible | TV all / TV bins1-10 |\n|---|---|---|---|---|---|---|---|---|"
    P("Day: eligible 22,428; tracked 0.727; pre-7000 0.9986; S21 21; 0-500 BP 2; S21/eligible 9.4e-4 (21/22,428) or 1.29e-3 (21/16,299); TV 0")
    P("")
    P("## A. Capture heterogeneity: ANCIENT bins only (anc) vs the main run's design with modern het too (modhet); m = min called chromosomes per bin")
    P(hdr)
    for n in ("R0_Ne100000", "R2_Ne1e+06", "R0_Ne10000", "R2_Ne100000"):
        for v in ["base"] + ["anc_k%g_m%d" % (k, m) for k in (2.0, 1.0, 0.5, 0.25) for m in (1, 10, 20, 40)] + \
                 ["modhet_k%g_m%d" % (k, m) for k in (1.0, 0.5) for m in (1, 20)]:
            r = row(n, v)
            if r:
                P(r)
    P("")
    P("## B. Matched capture: ancient-only (kappa, m) cells with tracked closest to 0.727 per scenario (grid above)")
    P(hdr)
    for n in names:
        best = None
        for k in (2.0, 1.0, 0.5, 0.25):
            for m in (1, 10, 20, 40):
                g = get(n, "anc_k%g_m%d" % (k, m))
                if g and (best is None or abs(g["trk"] - 0.727) < abs(best[1]["trk"] - 0.727)):
                    best = ("anc_k%g_m%d" % (k, m), g)
        if best:
            P(row(n, best[0]))
    P("")
    P("## C. Error sweep (flat false-minor-call rate eps on pseudo-haploid calls; homogeneous capture)")
    P(hdr)
    for n in names:
        if get(n, "eps0.0001"):
            for e in ("eps0.0001", "eps0.0003", "eps0.001", "eps0.003"):
                P(row(n, e))
    P("")
    P("## D. 10000+ bin at real dates (old) and unscaled modern bin (mod524); TV on all bins and on bins 1-10 only")
    P(hdr)
    for n in names:
        if get(n, "old"):
            for v in ("base", "old", "eps0.001", "old_eps1e-3", "mod524"):
                P(row(n, v))
    P("")
    P("## E. Ne axis (base sampling): S21, eligible, S21/eligible")
    P("| scenario | eligible (all) | pre-7000 | S21 | S21/21 | S21/eligible | 0-500 BP |")
    P("|---|---|---|---|---|---|---|")
    for n in names:
        g = get(n, "base")
        P("| %s | %.0f | %.3f | %.1f | %.2g | %.2g | %.1f |" % (n, g["elig_all"], g["pre"], g["s21"], g["s21"] / 21, g["s21"] / max(g["elig_trk"], 1), g["b10"]))
    P("")
    P("## F. S21 events by start band of the fixed allele in the Neolithic pooled sample (tracked, base): %% in [99,100) / [95,99) / [90,95) / <90")
    P("| scenario | S21 | start band % |")
    P("|---|---|---|")
    for n in names:
        g = get(n, "base")
        s = g["s21st"]
        if s.sum() > 0:
            P("| %s | %.1f | %s |" % (n, s.sum(), " / ".join("%.1f" % v for v in 100 * s / s.sum())))
    P("")
    P("## G. Day-style gate on variants (post hoc criteria): eligible within 3x of 22,428; pre-7000 >= 0.90; S21 in [7,63]; start [99,100) share in 70-90%")
    P("| scenario | variant | e | p | s | start | start %% [99,100) |")
    P("|---|---|---|---|---|---|---|")
    for n in names:
        for v in reps[0][n]:
            g = get(n, v)
            st = 100 * g["st"] / max(g["st"].sum(), 1)
            e = 22428 / 3 <= g["elig_all"] <= 22428 * 3
            p = g["pre"] >= 0.9
            s = 7 <= g["s21"] <= 63
            sa = 70 <= st[0] <= 90
            if sum([e, p, s, sa]) >= 3:
                P("| %s | %s | %s | %s | %s | %s | %.1f |" % (n, v, e, p, s, sa, st[0]))
    P("")
    # main-run density-robust ratio
    P("## H. S21 / eligible from the MAIN run (density-robust), tracked E1-T2 (Day: 21/16,299 = 1.29e-3; 21/22,428 = 9.4e-4)")
    main = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(rawdir, "c1c_rep[0-9].json")))]
    P("| scenario | variant | eligible | S21 | S21/eligible |")
    P("|---|---|---|---|---|")
    for n in [k for k in main[0] if k != "meta"]:
        for v in main[0][n]:
            if v == "modern_fixed_frac":
                continue
            if v != "base" and v not in ("e1e-3",):
                continue
            tr = np.mean([s["E1T2"]["trk"] for r in main for s in r[n][v]], axis=0)
            if n.split("_")[0] in ("R0", "R1", "R2", "R3") and (n.endswith(("Ne10000", "Ne100000", "Ne1e+06", "Ne300000")) or "grow" in n):
                P("| %s | %s | %.0f | %.1f | %.2g |" % (n, v, tr.sum(), tr[4:].sum(), tr[4:].sum() / max(tr.sum(), 1)))
    return "\n".join(L)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "dates":
        print(build_dates(sys.argv[2], sys.argv[3]))
    elif cmd == "run":
        run_rep(int(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "results", "raw"))
    elif cmd == "analyse":
        print(analyse(sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "results", "raw")))
