"""C1e post hoc (review MAJOR-1): generation length matched to each trajectory's source (25 y per generation).

POST HOC (review MAJOR): REVIEW-R4-C1e-combined.md MAJOR-1.  The original C1e (c1e_holocene_trajectories.py, 2c245ec) used
C1c's 20 y engine step with trajectories published at 25 y/generation.  Source check (docs/research/sources/holocene-ne.md
s2 line 27 and the S1/S4/S5 rows): Gravel 25 y, Gazave 25 y, Coventry (in generations; the dates 1.4 kya / 56 gens = 25 y),
Nelson (review-table start 9.3 kya at 25 y in the C1e conversion).  So all four use 25 y here: engine gy=25, T=420 steps.
Controls: constant 1e4 and 1.4e5 at BOTH gy=20 (reproduces C1c / original C1e) and gy=25.
Reuses c1e (imports; its patched ne_schedule), same panels (C1c replicate-r panel) and scenario seeds scheme.
PREDICTIONS (before the run): S21 falls to 0.6-0.8x of the original C1e values for the non-control cells (C1c: 25 y/gen gave
0.6-0.7x); ordering Nelson < Gravel << Gazave ~ Coventry unchanged; Nelson central R0 S21 in [15, 40]; Gravel R0 in [500, 900];
no flat fit within 3x of 21 (closest > 63); P6 tension still holds (no cell passes all three of tracked total in [5.4k, 48.9k],
S21 in [7, 63], pre-7000 >= 90%); the gy=20 controls reproduce the original (1e4: ~3.9k).
Run: research/.venv/bin/python -I research/checks/c1e_gen25_post_hoc.py main <workers>   (replicates 0..workers-1)
     ... analyse [rawdir]
"""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
if len(sys.argv) > 1 and sys.argv[1] == "smoke":
    os.environ.setdefault("C1C_NS", "30000")
import numpy as np
import c1e_holocene_trajectories as c1e
c1c = c1e.c1c


def scen_list(smoke=False):
    L = []
    gen25 = c1e.TRAJ[:3] if smoke else c1e.TRAJ
    for R in ("R0", "R2"):
        for name, fn in c1e.TRAJ[:2]:
            L.append(dict(name="%s_%s_gy20" % (R, name), fn=fn, R=R, d=1.0, gy=20, fs=1.0, variants=[("base", None, 0.0)]))
        for name, fn in gen25:
            L.append(dict(name="%s_%s" % (R, name), fn=fn, R=R, d=1.0, gy=25, fs=1.0, variants=[("base", None, 0.0)]))
    return L


def run_rep(rep, outdir, smoke=False):
    depth = c1c.load_depth()
    t0 = time.time()
    res = {"meta": {"rep": rep, "NS": c1c.NS, "smoke": smoke, "gy": "25 (controls also 20)"}}
    prng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 1, 10]))
    src = c1c.make_panel(prng, 1.0)
    trajs = {}
    for gy in (20, 25):
        trng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 2, 10, gy]))
        trajs[gy] = c1c.source_trajectories(src, gy, trng)
    for si, scen in enumerate(scen_list(smoke)):
        rng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 3, 12, si]))
        xb = c1c.simulate_scenario(src, trajs[scen["gy"]], scen, rng)
        out = {"modern_fixed_frac": float(np.mean((xb[c1c.MOD] == 0) | (xb[c1c.MOD] == 1))),
               "ne_bp": {str(b): float(scen["fn"](np.array([float(b)]))[0]) for b in (10500, 7000, 5000, 3000, 1000, 0)},
               "base": []}
        for sr in range(2):
            srng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 4, 12, si, sr]))
            a, c = c1c.sample_bins(xb, depth, srng, None, 0.0)
            out["base"].append(c1e.summarize(c1c.statistic(a, c)))
        res[scen["name"]] = out
        print("rep %d scen %d %s done t=%.0fs S21=%s" % (rep, si + 1, scen["name"], time.time() - t0,
                                                         [b["S21"] for b in out["base"]]), flush=True)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "c1e25_rep%d.json" % rep), "w") as f:
            json.dump(res, f)
    return res


def _job(args):
    run_rep(*args)
    return args[0]


def analyse(rawdir):
    import glob
    reps = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(rawdir, "c1e25_rep[0-9]*.json")))]
    names = [k for k in reps[0] if k != "meta"]
    print("replicates:", len(reps), "NS", reps[0]["meta"]["NS"])
    for label, sel in (("ALL replicates", reps), ("replicates 0-2 only (the original C1e panels)", reps[:3])):
        print("==", label, len(sel))
        print("%-26s %9s %9s %9s %9s %8s %s" % ("scenario", "S21", "S21/21", "trk_tot", "pre7000", "ne5kya", "per-rep S21"))
        for n in names:
            v = [b for r in sel if n in r for b in r[n]["base"]]
            per = [round(float(np.mean([b["S21"] for b in r[n]["base"]])), 1) for r in sel if n in r]
            s21 = np.mean([b["S21"] for b in v]); trk = np.mean([b["trk_total"] for b in v])
            pre = np.mean([b["pre7000"] for b in v if b["pre7000"] is not None])
            print("%-26s %9.1f %9.1f %9.0f %9.3f %8.0f %s" % (n, s21, s21 / 21.0, trk, pre, reps[0][n]["ne_bp"]["5000"], per))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    outdir = os.path.join(HERE, "results", "raw")
    if cmd == "smoke":
        run_rep(0, os.path.join(outdir, "smoke_c1e25"), smoke=True)
    elif cmd == "main":
        import multiprocessing as mp
        w = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        with mp.get_context("spawn").Pool(w) as pool:
            for r in pool.imap_unordered(_job, [(r, outdir) for r in range(w)]):
                print("replicate", r, "finished", flush=True)
    elif cmd == "analyse":
        analyse(sys.argv[2] if len(sys.argv) > 2 else outdir)
