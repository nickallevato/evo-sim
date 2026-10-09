"""C1c POST HOC (after the main run): apply the pre-registered validity gate (P3: eligible within 3x of 22,428, pre-7000
share >= 0.90, S21 in [7, 63]) to the SAMPLING VARIANTS (kappa, eps), which the main analysis' Table 3 skipped (it gated only
the 'base' variant).  Written after seeing that the eps=1e-3 variant raises eligible and the pre-7000 share toward Day's table.
Also prints the bin profile, total-variation distance from Day's profile and the start-frequency table for each variant.
Run: research/.venv/bin/python -I research/checks/c1c_posthoc_variant_gate.py [rawdir]
"""
import os
import sys
import glob
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import c1c_call_depth_replacement as m1


def main(rawdir):
    reps = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(rawdir, "c1c_rep*.json")))]
    print("reps:", len(reps))
    print("| scenario | variant | eligible (all) | tracked frac | pre-7000 | TV dist | S21 | start % [99,100)/[95,99)/[90,95)/<90 | gate |")
    print("|---|---|---|---|---|---|---|---|---|")
    obs = np.array(m1.OBS, dtype=float) / sum(m1.OBS)
    for n in [k for k in reps[0] if k != "meta"]:
        for v in reps[0][n]:
            if v == "modern_fixed_frac" or v == "base" and "k2" not in reps[0][n]:
                continue
            al = np.array([s["E1T2"]["all"] for r in reps for s in r[n][v]], dtype=float).mean(axis=0)
            tr = np.array([s["E1T2"]["trk"] for r in reps for s in r[n][v]], dtype=float)
            m = tr.mean(axis=0)
            s21 = tr[:, 4:].sum(axis=1).mean()
            st = np.array([s["start"]["all"] for r in reps for s in r[n][v]], dtype=float).mean(axis=0)
            e_ok = m1.OBS_ELIG / 3 <= al.sum() <= m1.OBS_ELIG * 3
            p_ok = m[:3].sum() / m.sum() >= 0.9
            s_ok = 7 <= s21 <= 63
            print("| %s | %s | %.0f | %.2f | %.3f | %.2f | %.1f | %s | %s |" % (
                n, v, al.sum(), m.sum() / al.sum(), m[:3].sum() / m.sum(), np.abs(m / m.sum() - obs).sum() / 2, s21,
                "/".join("%.1f" % x for x in 100 * st / st.sum()), "PASS" if (e_ok and p_ok and s_ok) else
                "e%s p%s s%s" % ("+" if e_ok else "-", "+" if p_ok else "-", "+" if s_ok else "-")))
            if v == "e1e-3":
                print("|  | profile | " + " ".join("%.0f" % x for x in m) + " | | | | | |")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw"))
