"""L7 POST HOC (labelled post hoc: asked by REVIEW-R4-L7-combined.md MAJOR-1, MAJOR-3 and MINOR-2 at a183774;
committed BEFORE this script is run). Local, one process, seconds, < 200 MB.
  research/.venv/bin/python -I research/checks/l7_posthoc_baserate.py [MOESM4.xlsx]
Same input as l7_410m_accounting.py (Yoo 2025 MOESM4.xlsx, sha256 865d4e868568b32dc0d233557c93d308b80b92168fe25d0196b0f5151c6671d1).

Q1 (MAJOR-3) R5 base rate redone on a PRIMITIVE pool: the composite readings R1 (SNV + gap), R3 and R4 (sums) are
   removed and replaced by their single components: SNV div x L and gap div x L per region (A, X, Y; sheets 14 x 19),
   (1 - k) x L per region for k in identical, identical 1:1, aligned, aligned 1:1 (sheet 19), the 18 sheet-24 SDR
   totals by lineage and haplotype, and the outside numbers 35 M (CSAC SNVs), 1,140 (inversions), 5.40 M (CSAC indel
   events), 48.27 M and 42.87 M (GAP-07t). Variant Q1b drops the sheet-19 R2 measures too. Counts of 1-3 element sums
   within 1% and 2% of 410 M, against 1,000 random targets uniform in 300-520 M (seed 20261011): mean, 5th-95th
   percentile, and the 410 M count's percentile.
   PREDICTION: the 410 M count lies inside the random 5-95% interval at both tolerances (ratio to the random mean
   0.5-2.0): a numerical match to 410 M is not evidence for any route.
Q2 (MINOR-2) R1 with the median instead of the mean, if sheet 14 has median columns (header printed).
   PREDICTION: none (sensitivity only).
Q3 (MAJOR-1) Day's printed components (Zenodo 23003785 s7.1: ~35 M SNVs + 1,140 inversions + ~187 Mb SDR) summed:
   35e6 + 1,140 + 187e6 = 222.0 M, i.e. 0.54 of 410 M (arithmetic only, printed for the record).
"""
import itertools
import random
import sys

import openpyxl

PATH = sys.argv[1] if len(sys.argv) > 1 else "sources/raw/sources/supp/Yoo2025/MOESM4.xlsx"
T = 410e6


def main():
    wb = openpyxl.load_workbook(PATH, read_only=True)
    t14 = [r for r in wb["14"].iter_rows(values_only=True)]
    for r in t14[:6]:
        print("sheet14 head:", r)
    hc = [r for r in t14 if r[0] == "mPanTro3#1/2" and r[1] == "hg002#M/P"][0]
    print("sheet14 human-chimp row:", hc)
    snv = dict(A=hc[2], X=hc[3], Y=hc[4])
    gap = dict(A=hc[5], X=hc[6], Y=hc[7])
    L, ident = {}, {}
    for r in list(wb["19"].iter_rows(values_only=True))[1:]:
        if r[2] in ("Chimp", "Chimp Pri"):
            reg = {"Autosomes": "A", "X": "X", "Y": "Y"}[r[0]]
            L[reg] = r[1]
            ident[reg] = dict(aligned=r[3], identical=r[4], aligned11=r[5], identical11=r[6])
    sdr = {}
    for r in wb["24"].iter_rows(min_row=10, values_only=True):
        if r[0] is None or not isinstance(r[6], (int, float)):
            continue
        sdr[(r[4], r[3])] = sdr.get((r[4], r[3]), 0) + r[6]
    comp = []
    for x in ("A", "X", "Y"):
        comp += [snv[x] * L[x], gap[x] * L[x]]
    r2 = [(1 - ident[x][k] / 100) * L[x] for x in ("A", "X", "Y") for k in ident[x]]
    outside = [35e6, 1140, 5.40e6, 48.27e6, 42.87e6]
    pools = {"Q1 primitive": comp + r2 + list(sdr.values()) + outside,
             "Q1b primitive minus sheet-19 R2": comp + list(sdr.values()) + outside}
    rng = random.Random(20261011)
    targets = [rng.uniform(300e6, 520e6) for _ in range(1000)]
    for name, pool in pools.items():
        pool = sorted(set(round(p) for p in pool))
        sums = [sum(c) for r in (1, 2, 3) for c in itertools.combinations(pool, r)]
        sums.sort()
        import bisect

        def hits(t, tol):
            return bisect.bisect_right(sums, t * (1 + tol)) - bisect.bisect_left(sums, t * (1 - tol))
        for tol in (0.01, 0.02):
            h = hits(T, tol)
            rt = sorted(hits(t, tol) for t in targets)
            mean = sum(rt) / len(rt)
            pct = sum(1 for v in rt if v < h) / len(rt)
            print(f"{name}: pool {len(pool)} values, {len(sums)} sums; within {tol:.0%}: 410 M {h}; random mean "
                  f"{mean:.1f}, 5-95% {rt[50]}-{rt[949]}, max {rt[-1]}; ratio {h / mean:.2f}; percentile {pct:.2f}")
    print("R1 mean x A:", round((snv["A"] + gap["A"]) * L["A"] / 1e6, 1), "M")
    print("Q3 Zenodo s7.1 components: 35e6 + 1140 + 187e6 =", round((35e6 + 1140 + 187e6) / 1e6, 1), "M; / 410 M =",
          round((35e6 + 1140 + 187e6) / T, 3))


if __name__ == "__main__":
    main()
