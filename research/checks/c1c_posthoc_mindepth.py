"""C1c POST HOC (written after the main run; not pre-registered): minimum-depth threshold for "tracked".

The main run (c1c_call_depth_replacement.py) found that strong site-to-site capture heterogeneity (kappa=0.5) inflates S21
to ~1.5e4 because sites with almost no calls in the modern or an old bin are trivially "100%", while the tracked fraction
stays ~0.96 (Day: 0.727).  Day's s4.1 says the remainder "had insufficient coverage in intermediate time bins" without a
threshold.  This script asks: if a bin must have >= m called chromosomes to count as observed (otherwise missing), which
(kappa, m) reproduces tracked ~0.73, and what does S21 become?  Single replicate (rep 100), one sampling draw; reuses the
main script's functions unchanged.  Labelled POST HOC: the grid was chosen after seeing the kappa=0.5 result.

Run: research/.venv/bin/python -I research/checks/c1c_posthoc_mindepth.py [outjson]
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import c1c_call_depth_replacement as m1

SCEN = ["R0_Ne10000", "R0_Ne100000", "R2_Ne100000", "R2_Ne1e+06"]
KAPPAS = [None, 2.0, 1.0, 0.5]
MINS = [1, 5, 10, 20]


def main(out):
    depth = m1.load_depth()
    scens = {s["name"]: s for s in m1.scenario_list()}
    rng0 = np.random.default_rng(np.random.SeedSequence([m1.ROOT_SEED, 100, 1]))
    src = m1.make_panel(rng0, 1.0)
    traj = m1.source_trajectories(src, 20, np.random.default_rng(np.random.SeedSequence([m1.ROOT_SEED, 100, 2])))
    rows = []
    for si, name in enumerate(SCEN):
        xb = m1.simulate_scenario(src, traj, scens[name], np.random.default_rng(np.random.SeedSequence([m1.ROOT_SEED, 100, 3, si])))
        for ki, kappa in enumerate(KAPPAS):
            a0, c0 = m1.sample_bins(xb, depth, np.random.default_rng(np.random.SeedSequence([m1.ROOT_SEED, 100, 4, si, ki])), kappa, 0.0)
            for mn in MINS:
                a, c = a0.copy(), c0.copy()
                bad = c < mn
                a[bad] = 0
                c[bad] = 0
                r = m1.statistic(a, c)
                allv, trk = np.array(r["E1T2"]["all"]), np.array(r["E1T2"]["trk"])
                row = dict(scen=name, kappa=kappa, min_chrom=mn, elig_all=int(allv.sum()), elig_trk=int(trk.sum()),
                           trk_frac=float(trk.sum() / max(allv.sum(), 1)), pre7000=float(trk[:3].sum() / max(trk.sum(), 1)),
                           s21_trk=int(trk[4:].sum()), s23_trk=int(trk[3:].sum()), profile_trk=trk.tolist())
                rows.append(row)
                print("%s kappa=%s m=%d elig_all=%d trk_frac=%.2f pre7000=%.3f S21=%d" % (
                    name, kappa, mn, row["elig_all"], row["trk_frac"], row["pre7000"], row["s21_trk"]), flush=True)
    with open(out, "w") as f:
        json.dump(rows, f)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw", "c1c_posthoc_mindepth.json"))
