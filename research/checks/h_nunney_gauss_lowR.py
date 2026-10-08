"""Check H2 follow-up (THROWAWAY): Haldane-like 10% budget (R=2.2, ln(R/2)=0.095) x low M in the Gaussian model.
Run: research/.venv/bin/python -I research/checks/h_nunney_gauss_lowR.py
PRE-REGISTERED (written after seeing h_nunney_gauss.py give T50 ~8-25 at R=10 for n=1, i.e. below Nunney's values):
 Prediction: with R=2.2 (selective-death budget ~10%, Haldane's assumption) and M <= 0.25 the hard-selection interval for
 n=1 rises toward the hundreds (Nunney's 300 at M=0.1 is for K=1e4, u=5e-6, whose R is not stated in the Discussion
 example; his Fig.1 uses R=10); soft selection with R=2.2 is no better (juvenile surplus only 10%).
 Verdict-changing: hard, R=2.2, M=0.1 giving T50 << 300 would mean Haldane's 300 is not the binding value even at 10% budget.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from multiprocessing import Pool
import h_nunney_gauss as g

if __name__ == "__main__":
    conds = []
    i = 0
    for reg in ("hard", "soft"):
        for M in (0.1, 0.25, 1.0, 10.0):
            i += 1
            conds.append((500, 1, 2.2, M, reg, 20261020 + i))
    with Pool(3) as p:
        res = p.map(g.cond, conds, chunksize=1)
    print("Gaussian model, K=500, n=1, R=2.2 (10% budget); success = no extinction and adult mean sq. deviation < 0.5; grid max T=1000")
    for K, n, R, M, reg, T50 in res:
        print(f" {reg:4s} R={R} M={M:<5} T50={T50:7.1f}  rate={1/T50 if T50==T50 else float('nan'):.4f}/gen" + ("" if T50 == T50 else "  (no success up to T=1000)"))
