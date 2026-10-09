"""H3 POST-HOC runs (written 2026-10-08 AFTER seeing stage A, V, C and S output; NOT pre-registered).
Motivation: stage S showed the fluctuation factor phi = lam50 / lam* depends strongly on s (s = 0.03 far below
s = 0.01), and phi was measured at K = 1000 over a 10,000-generation window only.  These runs map phi against
s, window length and K so that the human-scale extrapolation is not built on one (s, K, window) point.
Reuses run() from the pre-registered h3_human_scale.py unchanged (loaded by path; python -I drops the script dir).
Run: research/.venv/bin/python -I research/checks/h3_posthoc.py [workers]
Seeds: SeedSequence([20261051, cell, rep]).  Output: results/raw/h3_P.jsonl, h3_P_summary.json, h3_P.out
Expectations written before these runs (informal, post hoc): phi rises toward 1 as s falls (s = 0.003) and as K
rises (K = 4000); a 4x longer window lowers persistence at x = 0.5 somewhat (R = 1.5) or not at all (R = 2).
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
SEED = 20261051


def cells():
    c = []
    for R in (1.1, 2.0):                                    # P1: weaker selection
        for x in (0.5, 0.75, 1.0):
            c.append((1000, 0.003, x * math.log(R) / h3.Dpred(1000), R, f"P1 s=.003 x={x}", 8, 10000, 4000))
    for R in (1.1, 1.5, 2.0):                               # P2: 4x longer window
        c.append((1000, 0.01, 0.5 * math.log(R) / h3.Dpred(1000), R, "P2 win=40k x=0.5", 8, 40000, 2000))
    for R in (1.1, 2.0):                                    # P3: larger K at x = 0.75
        c.append((4000, 0.01, 0.75 * math.log(R) / h3.Dpred(4000), R, "P3 K=4000 x=0.75", 6, 10000, 2000))
    return c


def job(a):
    ci, (K, s, lam, R, lab, reps, gens, burn), rep = a
    rng = np.random.default_rng(np.random.SeedSequence([SEED, ci, rep]))
    t0 = time.time()
    r = h3.run(K, s, lam, R, 0.0, "none", "free", gens, burn, rng)
    r.update(dict(stage="P", cell=ci, K=K, s=s, lam=lam, R=R, U=0.0, load="none", linkage="free", M_sup=None,
                  x=lab, rep=rep, gens=gens, burn=burn, sec=time.time() - t0, D_pred=h3.Dpred(K),
                  lam_star=math.log(R) / h3.Dpred(K)))
    return r


if __name__ == "__main__":
    w = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    jobs = [(ci, c, rep) for ci, c in enumerate(cells()) for rep in range(c[5])]
    jobs.sort(key=lambda a: -(a[1][2] * a[1][6] * a[1][0]))
    rows = []
    t0 = time.time()
    with Pool(w) as pool, open(os.path.join(h3.RAW, "h3_P.jsonl"), "w") as f:
        for r in pool.imap_unordered(job, jobs, chunksize=1):
            rows.append(r)
            f.write(json.dumps(r) + "\n")
            f.flush()
    print(f"stage P: {len(jobs)} runs, {time.time()-t0:.0f} s wall", flush=True)
    sm = h3.summarize(rows)
    json.dump(sm, open(os.path.join(h3.RAW, "h3_P_summary.json"), "w"), indent=1)
    for x in sm:
        print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in x.items() if k != "stage"}, flush=True)
