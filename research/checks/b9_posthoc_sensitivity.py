"""B9 POST HOC (review fix pass): W = 0.01 sensitivity and a tighter (3x) band check.  Stdlib only, local, <1 s.
Run:  research/.venv/bin/python -I research/checks/b9_posthoc_sensitivity.py
Labelled POST HOC: requested by REVIEW-R4-B9-combined.md (MINOR-2, MINOR-9, NOTE-3, MAJOR-3).  Committed before its run.
Does not change b9_relaxed_load.py or its pre-registered criterion; adds two reported lines.
PREDICTIONS (from the closed form years = 25 ln(W)/ln(1-d)):
  P1  W = 0.01 gives about 2x the W = 0.1 values: ~2,240 y (5%), ~11,450 y (1%), ~22,970 y (0.5%); range ~2,240-22,970 y,
      still intersecting the 10x band [10, 9,990].
  P2  Tighter 3x band (100/3 to 999*3 = 33-2,997 y): the registered central range 338-11,484 y still intersects it
      (5% anchor: 338 and 1,122 y; 1% anchor at W = 0.5: 1,724 y), so the tag survives.
  P3  Strict overlap with 100-999 y only: survives through the 5% anchor alone (338 y at W = 0.5; 1,122 y is above 999).
"""
import math

G = 25.0
ANCH = [("mouse 0.5%", 0.005), ("central 1%", 0.01), ("upper 5%", 0.05)]


def yrs(d, w):
    return math.log(w) / math.log(1.0 - d) * G


def main():
    print("| anchor | W=0.5 | W=0.1 | W=0.01 |\n|---|---|---|---|")
    allv = {0.5: [], 0.1: [], 0.01: []}
    for lab, d in ANCH:
        cells = []
        for w in (0.5, 0.1, 0.01):
            y = yrs(d, w)
            allv[w].append(y)
            cells.append(f"{y:,.0f}")
        print(f"| {lab} | " + " | ".join(cells) + " |")
    reg = allv[0.5] + allv[0.1]
    ext = reg + allv[0.01]
    for name, vals in (("registered (W 0.5, 0.1)", reg), ("with W=0.01 added", ext), ("W=0.01 only", allv[0.01])):
        lo, hi = min(vals), max(vals)
        print(f"\n{name}: central range {lo:,.0f}-{hi:,.0f} y")
        for bname, (a, b) in (("strict 100-999", (100, 999)), ("3x band 33.3-2,997", (100 / 3, 999 * 3)),
                              ("10x band 10-9,990", (10, 9990))):
            print(f"  intersects {bname}: {lo <= b and hi >= a}")
    print("\nAnchors individually inside 100-999 y:",
          [(l, w, round(yrs(d, w))) for l, d in ANCH for w in (0.5, 0.1, 0.01) if 100 <= yrs(d, w) <= 999])
    print("Anchors individually inside 3x band 33-2,997 y:",
          [(l, w, round(yrs(d, w))) for l, d in ANCH for w in (0.5, 0.1, 0.01) if 100 / 3 <= yrs(d, w) <= 2997])


if __name__ == "__main__":
    main()
