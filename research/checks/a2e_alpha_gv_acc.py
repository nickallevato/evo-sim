"""A2e-alpha POST HOC (fix pass, after reviews 651e0d3; answers critic review C2 and correctness M1).
Gaya-Vidal & Alba 2014 accelerated-gene set: how many adaptive substitutions does "at least 40%" imply, against the
A2e flip (G1 = 252,000 / 1,322 = 190.6; G2 = 252,000 / 1,587 = 158.8 per lineage)?
Analysis only (sums over a 9 MB spreadsheet; trivial, run locally, one process, < 1 min).

Run:
  research/.venv/bin/pip install --target <LIBDIR> xlrd==2.0.1     # pure-Python .xls reader, outside the repo
  research/.venv/bin/python -I research/checks/a2e_alpha_gv_acc.py <LIBDIR> > research/checks/results/raw/a2e_alpha_gv_acc.out
Input (untrusted data, read only): sources/raw/a2e-alpha-gv-supp-2026-10-10/12864_2014_6322_MOESM1_ESM.xls
  = BMC Genomics 15:599 Additional file 1 (CC BY 4.0), fetched 2026-10-10 from
  https://static-content.springer.com/esm/art%3A10.1186%2F1471-2164-15-599/MediaObjects/12864_2014_6322_MOESM1_ESM.xls
  sha256 7b6cb765ad5f3e58a464def105a439c795f74341720c9d1fce53619ccf46c3b9 (checked by this script).
Sheets used: S3 (all 9,785 genes: Dn, Ds, Pn, Ps), S4-S7 (genes polymorphic at DAF >= 1/15/30/60%), S10 (198 accelerated
genes, Dn Ds Pn Ps), S11 (198 rapidly evolving control genes, rates only).  Only sheet headers were looked at before this
docstring was committed; no sum below had been computed.

METHOD.  Pooled MK as in GV Table 1 ("Data are for genes with at least one polymorphic site"):
  alpha = 1 - (sum Ds * sum Pn) / (sum Dn * sum Ps), over the genes of a set that appear in the DAF sheet;
  adaptive count A = alpha * sum Dn = sum Dn - sum Ds * sum Pn / sum Ps (Smith & Eyre-Walker form).
  Gene bootstrap (10,000 resamples, seed 1) gives a 95% interval for A.
Rows:
  R0  validation: reproduce Table 1 (all genes 0.002 at N 2,766; accelerated 0.405 at N 75; Methods sum Dn 18,936).
  R1  accelerated, DAF >= 60%, the 75 polymorphic genes only (alpha applied only where it was estimated).
  R2  as R1 at DAF >= 1/15/30% (the lowest-alpha DAF class is the Day-charitable one).
  R3  alpha(DAF >= 60%) applied to all 198 accelerated genes' Dn (extrapolation to the non-polymorphic genes; critic-leaning).
  R4  Day-charitable (rule C) for ascertainment: the set was SELECTED for excess human-branch Dn, so Dn is inflated by
      selection noise while Pn/Ps is not (winner's curse inflates alpha).  Subtract GV's matched-rate control alpha
      (rapidly evolving set, Table 1: 0.163 at DAF >= 60%) from the accelerated alpha: (0.405 - 0.163) * sum Dn_75.
      This also removes any genuine adaptation the control set carries, so it is a deliberately low reading.
  R5  R4 at the lower 95% bootstrap bound of R1 (most Day-charitable row).
PREDICTIONS (written before any sum was computed):
  P1  R0 reproduces 0.002, 0.405 (+-0.005) and 18,936 exactly. If not, the mapping is wrong and nothing below is used.
  P2  sum Dn over the 198 accelerated genes is 1,000-2,000 (mean 5-10 per gene, against the genome mean ~1.9).
  P3  R1 lands in 150-350 (straddles G1); R3 clears 191 by > 2x.
  P4  R4 and R5 fall below 191 (Day side), so the C2 row does NOT clear 191 under charitable assumptions and A2e external
      stays `contested`.  If R5 is above 191, the critic review's "contradicted" condition is met.
"""
import hashlib
import os
import random
import sys

sys.path.insert(0, sys.argv[1])
import xlrd  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
XLS = os.path.join(ROOT, "sources", "raw", "a2e-alpha-gv-supp-2026-10-10", "12864_2014_6322_MOESM1_ESM.xls")
SHA = "7b6cb765ad5f3e58a464def105a439c795f74341720c9d1fce53619ccf46c3b9"
G1, G2 = 252000 / 1322, 252000 / 1587
CONTROL_ALPHA = 0.163  # GV Table 1, rapidly evolving, DAF >= 60%


def rows(sh, idcol=0, cols=(1, 2, 3, 4)):
    out = {}
    for r in range(1, sh.nrows):
        gid = str(sh.cell_value(r, idcol)).strip()
        if not gid:
            continue
        out[gid] = tuple(float(sh.cell_value(r, c)) for c in cols)
    return out


def mk(genes):
    dn = sum(g[0] for g in genes); ds = sum(g[1] for g in genes)
    pn = sum(g[2] for g in genes); ps = sum(g[3] for g in genes)
    alpha = 1 - (ds * pn) / (dn * ps) if dn and ps else float("nan")
    return dn, ds, pn, ps, alpha, alpha * dn


def boot(genes, n=10000, seed=1):
    rng = random.Random(seed); k = len(genes); a = []
    for _ in range(n):
        s = [genes[rng.randrange(k)] for _ in range(k)]
        a.append(mk(s)[5])
    a.sort()
    return a[int(0.025 * n)], a[int(0.975 * n) - 1]


def side(x):
    return f"{x:8.1f}  x{x / G1:5.2f} G1  {'critic (A2e flips)' if x > G1 else 'Day (A2e holds)'} on G1; " \
           f"{'critic' if x > G2 else 'Day'} on G2"


def main():
    b = open(XLS, "rb").read()
    h = hashlib.sha256(b).hexdigest()
    print(f"sha256 {h}  {'OK' if h == SHA else 'MISMATCH'}")
    wb = xlrd.open_workbook(XLS, on_demand=True)
    s3 = rows(wb.sheet_by_name("S3"))
    daf = {t: rows(wb.sheet_by_name(s)) for t, s in (("1", "S4"), ("15", "S5"), ("30", "S6"), ("60", "S7"))}
    acc = rows(wb.sheet_by_name("S10"))
    print(f"G1 {G1:.1f}  G2 {G2:.1f}")
    print(f"R0 S3 genes {len(s3)}  sum Dn {sum(g[0] for g in s3.values()):.0f} (Methods: 18936)  "
          f"sum Ds {sum(g[1] for g in s3.values()):.0f} (Methods: 34241)")
    print(f"   accelerated genes in S10: {len(acc)}  in S3: {len(set(acc) & set(s3))}")
    dn198 = sum(g[0] for g in acc.values())
    print(f"   sum Dn over S10 (198 accelerated): {dn198:.0f}  mean {dn198 / len(acc):.2f}; "
          f"genome mean {sum(g[0] for g in s3.values()) / len(s3):.2f}")
    for t, d in daf.items():
        allg = mk(list(d.values()))
        sub = [d[g] for g in acc if g in d]
        a = mk(sub)
        print(f"R0/R2 DAF>={t:>2}%: all genes N {len(d)} alpha {allg[4]:.3f} | accelerated N {len(sub)} "
              f"Dn {a[0]:.0f} Ds {a[1]:.0f} Pn {a[2]:.0f} Ps {a[3]:.0f} alpha {a[4]:.3f}  A = {side(a[5])}")
    sub60 = [daf["60"][g] for g in acc if g in daf["60"]]
    dn75, _, _, _, a60, A1 = mk(sub60)
    lo, hi = boot(sub60)
    print(f"R1 accelerated DAF>=60% N {len(sub60)}: A = {side(A1)}  boot95 [{lo:.1f}, {hi:.1f}]")
    print(f"R3 alpha {a60:.3f} x sum Dn(198) {dn198:.0f} = {side(a60 * dn198)}")
    r4 = (a60 - CONTROL_ALPHA) * dn75
    print(f"R4 ({a60:.3f} - {CONTROL_ALPHA}) x {dn75:.0f} = {side(r4)}")
    r5 = lo * (a60 - CONTROL_ALPHA) / a60
    print(f"R5 R4 at lower boot bound: {lo:.1f} x ({a60:.3f} - {CONTROL_ALPHA}) / {a60:.3f} = {side(r5)}")


if __name__ == "__main__":
    main()
