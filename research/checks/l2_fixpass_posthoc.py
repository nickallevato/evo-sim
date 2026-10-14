"""POST HOC (fix pass, EVO-46, 2026-10-14): recompute the figures the three L2 reviews added.

Status: post hoc. Written after the registered run (`ade0542`, run `1d9a32f`), the write-up (`8d17245`)
and all three reviews (correctness `4b97637`, steelman-day `74c5250`, steelman-critic `333afc0`) had been
read. Every number below has already been seen, in a review or in the write-up; this script only
re-derives them in one committed place so the fix pass does not carry reviewer arithmetic unchecked.
It governs nothing: no band, score or verdict move is re-decided here (registered values stand).

Inputs: the committed `raw/l2_inputs.json` (route (b) components) and gamma / SE values typed in below
from C1440 (Madsen, Robertson and Ye 2019 working paper, sha256 c24bca98...3903, pdftotext -layout,
read 2026-10-14): Table 3 row "ln Lit-T" columns (1)-(7) (L2Q-21); Table 4 "Convergence by Country",
Population 1470-1870 column; Table 5 "Convergence by Country Group", Population rows. Mapping is the
registered one (`l2_hardness.beta_from`, halflife_years, through the source's half-life formula):
h = (1 + gamma*30)^(G/30), interval gamma +- 1.96 SE, G bracket [25, 30], negative base clipped to 0.

What each side expects (from the reviews; stated before this script runs):
- Correctness review: column 4 with SE [0.005, 0.116]; columns 5, 6 [0.112, 0.203], [0.106, 0.210];
  column 7 [0.335, 0.471]; union of SUR columns 2-7 [0, 0.471]; R-a2 (columns 2 + 4) gives B-LH, PD-w
  miss; Albeza printed shares give h 0.278 / 0.194 / 0.344; rounding ranges Cerro [0.272, 0.296],
  Chanarcito [0.281, 0.302]; excluding Pd < 0.15 gives route (b) [0.333, 0.641], B-MH; column 7 with
  that cut is the only B-HH combination.
- Steelman-day: R-a4 (column 7) governing [0.284, 0.641], B-MH, DISJOINT False; G over Day's values
  [20, 32.5] gives column 2 [0.105, 0.337]; Table 4 country points span h 0 to about 0.98, median
  about 0.70-0.74; Table 5 Protestant [0.269, 0.418]; Table 5 baseline 1470-1600 (-0.017) 0.49-0.55;
  upward E2-false records Maca 0.639, Zapotec 1978 0.477, Brazilian isolate 0.522, Halfmoon 1850
  0.427, Nicobarese 0.380; M-b1 on the mix model (R - 1)/R.
- Steelman-critic: clause-(i)-only route (b) [0.333, 0.641]; M-b1 on the model I_m = R - 1 at every h.
If any figure differs from the review's, the fix pass reports the difference and uses this output.

Workstation, trivial check (stdlib, one process, < 1 s), as the registered run was (EVO-43 ruling).
"""
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l2_hardness as L  # noqa: E402

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw", "l2_inputs.json")
Z, T = 1.96, 30.0

# C1440 Table 3, ln L(t-T), columns 1-7: (gamma, robust SE)
TAB3 = {1: (-0.002, 0.0001), 2: (-0.028, 0.0006), 3: (-0.034, 0.0004), 4: (-0.032, 0.0006),
        5: (-0.029, 0.0003), 6: (-0.029, 0.0004), 7: (-0.021, 0.0006)}
# C1440 Table 4, Population 1470-1870
TAB4 = {"Austria": -0.001, "Belgium": -0.006, "France": -0.010, "Germany": -0.029, "Italy": -0.037,
        "Netherlands": -0.005, "Spain": -0.024, "Sweden": -0.010, "UK": -0.027}
# C1440 Table 5, Population: Protestant 1470-1870; Baseline subperiods
TAB5_PROT = (-0.023, 0.0007)
TAB5_BASE = {"1470-1600": (-0.017, 0.0006), "1600-1870": (-0.030, 0.0007)}


def h_of(g, G):
    base = 1.0 + g * T
    return 0.0 if base <= 0 else base ** (G / T)


def iv_se(g, se, G=(25.0, 30.0)):
    lo, hi = g - Z * se, g + Z * se
    return (min(h_of(lo, G[0]), h_of(lo, G[1])), max(h_of(hi, G[0]), h_of(hi, G[1])))


def iv_pt(g, G=(25.0, 30.0)):
    return (min(h_of(g, G[0]), h_of(g, G[1])), max(h_of(g, G[0]), h_of(g, G[1])))


def f(iv):
    return "[%.3f, %.3f]" % iv


def crow_h(im, i_f, ps):
    return im / (im + i_f / ps)


def main():
    # collect every non-synthetic record dict, wherever it sits in the inputs file
    d = json.load(open(RAW))
    allrecs = {}

    def walk(x):
        if isinstance(x, dict):
            if "id" in x and "stat" in x and "values" in x and not x.get("synthetic", False):
                allrecs[x["id"]] = x
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(d)

    print("== P1 / MINOR-2: Table 3 columns, registered interval rule (+-1.96 SE, G 25-30) ==")
    t3 = {}
    for c, (g, se) in TAB3.items():
        t3[c] = iv_se(g, se)
        print("col %d gamma %.3f SE %.4f: SE %s | point %s%s" % (
            c, g, se, f(t3[c]), f(iv_pt(g)), "  (1+30g<0 at point: clipped)" if 1 + 30 * g < 0 else ""))
    rb = (0.2839, 0.6410)  # registered route (b) M-b1 hull (l2_main.out)
    readings = {"R-a1 col 2": [2], "R-a2 cols 2+4": [2, 4], "R-a3 union cols 2-7": [2, 3, 4, 5, 6, 7],
                "R-a4 col 7": [7]}
    print("\n== MAJOR-1 / SD-3: readings of the specification clause ==")
    for name, cols in readings.items():
        ra = L.hull([t3[c] for c in cols])
        gov = L.hull([ra, rb])
        print("%-20s route(a) %s governing %s band B-%s PD-w %s PC-w %s PA-4 %s DISJOINT %s" % (
            name, f(ra), f(gov), L.band(gov), "hit" if gov[0] >= 0.1 else "miss",
            "hit" if gov[1] < 0.3 else "miss", "hit" if ra[0] < 0.3 <= ra[1] else "miss",
            ra[1] < rb[0] or rb[1] < ra[0]))

    print("\n== SD-4: column 2 over G brackets ==")
    for G in ((25.0, 30.0), (20.0, 32.5), (20.0, 20.0), (32.5, 32.5)):
        ra = iv_se(*TAB3[2], G=G)
        gov = L.hull([ra, rb])
        print("G %s: route(a) %s governing %s band B-%s DISJOINT %s" % (
            G, f(ra), f(gov), L.band(gov), ra[1] < rb[0]))

    print("\n== SD-3: Table 4 countries (point gamma, G 25-30) ==")
    mids = []
    for k, g in TAB4.items():
        iv = iv_pt(g)
        mids.append(iv)
        print("%-12s %.3f %s" % (k, g, f(iv)))
    med = statistics.median(TAB4.values())
    print("median gamma %.3f -> %s; countries with h_lo >= 0.70: %d of 9" % (
        med, f(iv_pt(med)), sum(1 for iv in mids if iv[0] >= 0.70)))
    print("Table 5 Protestant 1470-1870 with SE: %s" % f(iv_se(*TAB5_PROT)))
    for k, (g, se) in TAB5_BASE.items():
        print("Table 5 Baseline %s: point %s, SE %s" % (k, f(iv_pt(g)), f(iv_se(g, se))))

    print("\n== route (b): M-b1 point, Pd = Im/(1+Im) ==")
    rows = {}
    for rid, r in sorted(allrecs.items()):
        if r["route"] != "b":
            continue
        v = {k: x["est"] for k, x in r["values"].items()}
        if r["stat"] == "crow":
            h, pd = crow_h(v["Im"], v["If"], v["Ps"]), v["Im"] / (1 + v["Im"])
        else:
            h, pd = v["I_surv"] / (v["I_surv"] + v["I_mate"] + v["I_fpm"]), None
        rows[rid] = (h, pd, r.get("pre_transition"))
        print("%-22s E2 %-5s h %.3f Pd %s" % (rid, r.get("pre_transition"), h,
                                              "-" if pd is None else "%.3f" % pd))
    elig = {k: x for k, x in rows.items() if x[2]}
    cut = [x[0] for k, x in elig.items() if x[1] is None or x[1] >= 0.15]
    print("\nMAJOR-2 illustrative cut (drop eligible Pd < 0.15): route (b) [%.3f, %.3f], band B-%s" % (
        min(cut), max(cut), L.band(L.hull([(0.1247, 0.2564), (min(cut), max(cut))]))))
    cl1 = [rows[k][0] for k in ("b-slovincian-g1", "b-slovincian-g2", "b-utah-early")]
    print("critic NOTE-1 clause (i) only: [%.3f, %.3f]" % (min(cl1), max(cl1)))
    print("NOTE-5: col 7 + cut: governing %s band B-%s" % (
        f(L.hull([t3[7], (min(cut), max(cut))])), L.band(L.hull([t3[7], (min(cut), max(cut))]))))

    print("\n== MINOR-3: Albeza printed If/ps shares of the total index (L2Q-15) ==")
    for k, share in (("Chanarcito", 0.7223), ("Santa Rosa", 0.8064), ("Olacapato", 0.6557)):
        print("%-11s h = 1 - share = %.3f" % (k, 1 - share))
    for k, im, i_f in (("Cerro", 0.11, 0.25), ("Chanarcito", 0.13, 0.28)):
        lo = crow_h(im - 0.005, i_f + 0.005, 1 / (1 + im - 0.005))
        hi = crow_h(im + 0.005, i_f - 0.005, 1 / (1 + im + 0.005))
        print("%-11s rounding range [%.3f, %.3f]" % (k, lo, hi))
    print("gap to route (a) hi 0.256: registered %.3f, printed share %.3f" % (
        rows["b-mapuche-cerro"][0] - 0.2564, (1 - 0.7223) - 0.2564))

    print("\n== SD-1 / critic MAJOR-1: mappings applied to the HF mix model (analytic) ==")
    for R in (1.111, 1.5, 2.0):
        print("R %.3f: M-b1 at N=K, Im = R-1 = %.3f, If/Ps = 1 -> h_Mb1 = (R-1)/R = %.3f (any model h)" % (
            R, R - 1, (R - 1) / R))
    R, load, shock = 1.111, 0.05, 0.95
    nxt = min(1.0, R * (2.718281828459045 ** -load) * shock)
    print("A1, model h=1, R 1.111, log-load 0.05, 5%% shock: N'/K = %.3f -> beta_gen = %s" % (
        nxt, "0 (fully compensated)" if nxt >= 1.0 else "> 0"))


if __name__ == "__main__":
    main()
