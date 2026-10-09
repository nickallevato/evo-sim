"""C1e -- the C1c ancestry-replacement model run on each PUBLISHED Holocene N_e trajectory.

THROWAWAY research check (queue item 1).  Reuses research/checks/c1c_call_depth_replacement.py unchanged (imports it and
replaces only its ne_schedule(); panel, source drift, pulses, AADR call depth, sampling and the statistic are C1c's).
Run (isolated venv, on na-workhorse only):
    research/.venv/bin/python -I research/checks/c1e_holocene_trajectories.py smoke
    research/.venv/bin/python -I research/checks/c1e_holocene_trajectories.py main <workers>     # one replicate per worker
    research/.venv/bin/python -I research/checks/c1e_holocene_trajectories.py analyse [rawdir]

TARGET CLAIMS.  C1c / C4 (Holocene N_e varied), C5b (keruru temporal N_e), B2e (measured N_e vs Wright's formula); the
Day statistic "21" (Z18525185 s4.1: "0-6000 BP: 21", quoted in c1c docstring; quote ids in docs/research/sources/quotes-day.md).
Source of trajectories: docs/research/sources/holocene-ne.md section 3-4 (S1 Gravel 2011, S2 Coventry 2010, S4 Nelson 2012,
S5 Gazave 2014; quotes in quotes-literature.md "Holocene Ne retrieval (2026-10-09)").  C1c's own result that this check
conditions on (R4-C1c.md section 2; S21 = tracked E1-T2 events dated 5000-6000 BP or younger; Day 21): constant N_e 1e4: 3,925;
2e4: 908; 5e4: 120; ~1.4e5: 21; growth-cell 1e4->1e6: 35; step cell: 32.

TRAJECTORIES (calendar-time functions of BP, 25 y/generation as published, converted to C1c's 20 y steps by date; N_e = size
parameter, so the C1c 2N is 2*N_e).  Derived from the published parameters, as in holocene-ne.md s4:
  Gravel   N_e(bp) = 35,900 * 1.0038^(-bp/25)                           (present 35,900, 0.38%/gen; growth throughout the window)
  Gazave   N_e = 5,633 flat until 141 gens (3,525 BP), then 5,633*1.034^(141-bp/25)      (present ~6.3e5; the s4 table prints 680k)
  Coventry N_e = 7,700 flat until 56 gens (1,400 BP), then 7,700*1.094^(56-bp/25)        (present ~1.2e6)
  Nelson   N_e = 4.0e6 * (1+g)^(-bp/25) for bp < 9,300 (start date SECONDHAND, from a review table), flat before; g = 1.7% central,
           1.2% and 2.3% as the growth-rate CI ends (4.0M and 9.3 kya held fixed; not a joint CI)
  Controls: constant 1e4 and constant 1.4e5 (C1c's flip point), to reproduce C1c on the same panels.
Replacement R0 (closed EU, the C1c reference) and R2 (literature-central W .12/A .50/S .38), 2 sampling draws each.
Same ROOT_SEED and panel construction as C1c, so replicate r here uses C1c's replicate-r panel.

PRE-REGISTERED PREDICTIONS (written before any run; smoke inspects timing and structure only, not S21).  S21 = mean over
replicates and sampling draws, R0 unless stated.  The ranking is monotone in the late-window N_e (events dated <= 6000 BP need
drift after the allele was visible in the old bins):
  P1  CONTROLS.  Constant 1e4 gives S21 within a factor 1.5 of 3,925; constant 1.4e5 within [10, 45] (C1c: 21).
  P2  GRAVEL (N_e 14k at 6 kya to 36k now).  S21 in [300, 3,000] (between C1c's 1e4 and 5e4 cells).  A deficit against Day's 21
      of at least 15x (S21/21 >= 15).
  P3  COVENTRY (7.7k flat to 1.4 kya).  S21 in [1,500, 6,000]; at least 70x Day's 21.
  P4  GAZAVE (5.6k flat to 3.5 kya).  S21 in [2,000, 8,000], and larger than the constant-1e4 cell (the 6-3.5 kya events occur at 5.6k).
  P5  NELSON CENTRAL (34k at 7 kya, 130k at 5 kya, 2M at 1 kya).  S21 in [25, 250] (central ~80); the only one of the four
      within 12x of Day's 21.  Nelson at 1.2%/gen (smaller N_e) S21 >= 300; at 2.3%/gen S21 in [5, 80].
  P6  TENSION (C1c P3) SURVIVES.  No trajectory cell has BOTH tracked-event total (sum of E1-T2 tracked counts) within 3x of
      Day's tracked 16,299 AND S21 in [7, 63] (Day 21 within 3x), AND pre-7000 share >= 90%.  Falsifier: any cell passes all three.
  P7  R2 vs R0 within a factor 2 of S21 for every trajectory (replacement second-order, C1c P4).

WHAT EACH SIDE'S MODEL PREDICTS.
  Day (clock stopped / punctuated; d = 0.45 scales the drift clock; Z18525185 abstract, s4.4): essentially no post-7000 events;
    the only simulable content is fewer drift generations, i.e. the thousands-of-events end for N_e <= 2e4.  Day-side reading of
    the retrieved literature: Gazave, Coventry, Gravel (and keruru's temporal-F values) say ~1e4, so 21 is a deficit of 40-190x.
  Critics (neutral drift + replacement + real depth): 21 is a neutral value if the Holocene N_e is large; the only retrieved
    trajectory that gets there is Nelson's (and Schaffner's fixed 100,000 step, not run here).  The critic-side reading is
    therefore conditional on choosing Nelson over the three flatter fits.
  RESULT THAT WOULD CHANGE A VERDICT: any of Gravel/Coventry/Gazave within 3x of 21 (then the critic reading needs no unusual
    N_e), or Nelson central above 500 (then even the high-growth reading leaves a deficit).

Raw output: research/checks/results/raw/c1e_rep<r>.json (committed by the caller, not by the script).
"""
import os
import sys
import json
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
if len(sys.argv) > 1 and sys.argv[1] == "smoke":
    os.environ.setdefault("C1C_NS", "30000")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import c1c_call_depth_replacement as c1c

C1E_SEED_TAG = 11


def gravel(bp):
    return 35900.0 * 1.0038 ** (-bp / 25.0)


def gazave(bp):
    return 5633.0 * 1.034 ** np.maximum(0.0, 141.0 - bp / 25.0)


def coventry(bp):
    return 7700.0 * 1.094 ** np.maximum(0.0, 56.0 - bp / 25.0)


def nelson_g(g):
    def f(bp):
        bpc = np.minimum(bp, 9300.0)
        return 4.0e6 * (1.0 + g) ** (-bpc / 25.0)
    return f


def const(n):
    return lambda bp: n + 0.0 * bp


TRAJ = [("ctrl_Ne1e4", const(1e4)), ("ctrl_Ne1.4e5", const(1.4e5)), ("Gravel", gravel), ("Gazave", gazave),
        ("Coventry", coventry), ("Nelson", nelson_g(0.017)), ("Nelson_g1.2", nelson_g(0.012)), ("Nelson_g2.3", nelson_g(0.023))]


def ne_schedule_patched(scen, T):
    t = np.arange(T + 1)
    bp = c1c.START_BP - t * scen["gy"]
    ne = scen["fn"](bp)
    return np.maximum(2, np.rint(2 * ne / scen["d"])).astype(np.int64)


c1c.ne_schedule = ne_schedule_patched


def scen_list(smoke=False):
    L = []
    trajs = TRAJ[:3] if smoke else TRAJ
    for R in ("R0", "R2"):
        for name, fn in trajs:
            L.append(dict(name="%s_%s" % (R, name), fn=fn, R=R, d=1.0, gy=20, fs=1.0, variants=[("base", None, 0.0)]))
    return L


def summarize(st):
    trk = st["E1T2"]["trk"]
    al = st["E1T2"]["all"]
    tot = float(sum(trk))
    return dict(S21=int(sum(trk[4:])), S23=int(sum(trk[3:])), trk_total=int(tot), elig=int(sum(al)),
                pre7000=(sum(trk[:3]) / tot if tot > 0 else None), n_trk_sites=st["n_trk_sites"], raw_trk=trk)


def run_rep(rep, outdir, smoke=False):
    depth = c1c.load_depth()
    t0 = time.time()
    res = {"meta": {"rep": rep, "NS": c1c.NS, "smoke": smoke}}
    prng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 1, 10]))      # = C1c panel for this rep
    src = c1c.make_panel(prng, 1.0)
    trng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 2, 10, 20]))
    traj = c1c.source_trajectories(src, 20, trng)
    for si, scen in enumerate(scen_list(smoke)):
        rng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 3, C1E_SEED_TAG, si]))
        xb = c1c.simulate_scenario(src, traj, scen, rng)
        out = {"modern_fixed_frac": float(np.mean((xb[c1c.MOD] == 0) | (xb[c1c.MOD] == 1))),
               "ne_bp": {str(b): float(scen["fn"](np.array([float(b)]))[0]) for b in (10500, 7000, 5000, 3000, 1000, 0)}}
        out["base"] = []
        for sr in range(2):
            srng = np.random.default_rng(np.random.SeedSequence([c1c.ROOT_SEED, rep, 4, C1E_SEED_TAG, si, sr]))
            a, c = c1c.sample_bins(xb, depth, srng, None, 0.0)
            out["base"].append(summarize(c1c.statistic(a, c)))
        res[scen["name"]] = out
        print("rep %d scen %d %s done t=%.0fs S21=%s" % (rep, si + 1, scen["name"], time.time() - t0,
                                                         [b["S21"] for b in out["base"]]), flush=True)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "c1e_rep%d.json" % rep), "w") as f:
            json.dump(res, f)
    return res


def _job(args):
    rep, outdir = args
    run_rep(rep, outdir)
    return rep


def analyse(rawdir):
    import glob
    reps = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(rawdir, "c1e_rep[0-9]*.json")))]
    names = [k for k in reps[0] if k != "meta"]
    print("replicates:", len(reps), "NS", reps[0]["meta"]["NS"])
    print("%-24s %9s %9s %9s %9s %8s  n_draws" % ("scenario", "S21", "S21/21", "trk_tot", "pre7000", "ne(5kya)"))
    for n in names:
        v = [b for r in reps if n in r for b in r[n]["base"]]
        s21 = np.mean([b["S21"] for b in v])
        trk = np.mean([b["trk_total"] for b in v])
        pre = np.mean([b["pre7000"] for b in v if b["pre7000"] is not None])
        ne5 = reps[0][n]["ne_bp"]["5000"]
        print("%-24s %9.1f %9.1f %9.0f %9.3f %8.0f  %d  (draws: %s)" % (n, s21, s21 / 21.0, trk, pre, ne5, len(v),
                                                                       [b["S21"] for b in v]))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    outdir = os.path.join(HERE, "results", "raw")
    if cmd == "smoke":
        run_rep(0, os.path.join(HERE, "results", "raw", "smoke_c1e"), smoke=True)
    elif cmd == "main":
        import multiprocessing as mp
        w = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        with mp.get_context("spawn").Pool(w) as pool:
            for r in pool.imap_unordered(_job, [(r, outdir) for r in range(w)]):
                print("replicate", r, "finished", flush=True)
    elif cmd == "analyse":
        analyse(sys.argv[2] if len(sys.argv) > 2 else outdir)
