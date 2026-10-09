"""C1d POST HOC 3 (review fix pass): arithmetic on the stored B2e outputs; no genotypes.  Written after the main run and the reviews.

    research/.venv/bin/python -I research/checks/c1d_posthoc3_keruru.py
Reads results/raw/c1d_<rel>_ne.json, _posthoc.json, _groups.json; writes results/raw/c1d_posthoc3_keruru.{json,txt}.
 1. Composition counterfactual.  For two mixtures of the same regional populations with proportion shifts d_r (sum 0) and pairwise
    F_rs between regional samples, the F produced by the shift alone is F_comp = sum_{r<s} (-d_r d_s) F_rs  (since
    (sum d_r p_r)^2 = -sum_{r<s} d_r d_s (p_r - p_s)^2).  Proportions: individuals in the five regions, BA bin vs Medieval bin;
    F_rs: F_adj between regions in the BA bin and, separately, in the Medieval bin (c1d_posthoc.py section D).  Five regions only.
 2. Census sensitivity of the Wright comparison: N_e = 4N/(V_k+2), V_k = 5; drift-only F = t/(2 N_e); share of the measured F_adj
    that would have to be non-drift for Wright to hold at that N; break-even N.
 3. Decomposition of the sampling-correction effect for each window: (K) his formula with mean individuals; (B1) the correct
    1/n0 + 1/nt at MEAN chromosome counts; (B) site-wise (ratio of sums).  (B1)/(K) is the factor-of-2 effect; (B)/(B1) is the depth
    heterogeneity effect.  Also against his published numbers.
 4. Within-region BA-to-Medieval N_e values (form B), for reading against the pooled value.
Predictions (before the run, from the review arithmetic): F_comp 0.0003-0.0011 (6-20% of the BA-Med F_adj) on v66; correction effect
about +17% from the factor of 2 and about +6 points from depth heterogeneity for BA-Med.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, "results", "raw")
REG = ["Iberia", "CentralEur", "ItalyBalkans", "Scandinavia", "EastEur"]
PUB = {"BA-Med": 8139, "EN-Mod": 9835, "Meso-EN": 938, "EN-LN": 4922, "EN-BA": 6933, "EN-Iron": 9792, "EN-Med": 8530}
out, L = {}, []
for rel in ("v62", "v66"):
    ne = json.load(open(os.path.join(RAW, "c1d_%s_ne.json" % rel)))
    ph = json.load(open(os.path.join(RAW, "c1d_%s_posthoc.json" % rel)))
    gr = {g["name"]: g["n"] for g in json.load(open(os.path.join(RAW, "c1d_%s_groups.json" % rel)))["groups"]}
    pairs = {p["pair"]: p for p in ne["pairs"]}
    FB = pairs["BA-Med"]["B"]["F_adj"]; tB = pairs["BA-Med"]["t_gen"]; NeB = pairs["BA-Med"]["B"]["ne"]
    pi = {}
    for b in ("BA", "Med"):
        tot = sum(gr["krreg_%s:%s" % (r, b)] for r in REG)
        pi[b] = [gr["krreg_%s:%s" % (r, b)] / tot for r in REG]
    d = [pi["Med"][i] - pi["BA"][i] for i in range(5)]
    res = {"shares_BA": pi["BA"], "shares_Med": pi["Med"], "F_adj_BA_Med": FB}
    for b in ("BA", "Med"):
        Frs = {(x["a"], x["b"]): x["F_adj"] for x in ph["region_floor"] if x["bin"] == b}
        tot = 0.0
        for i in range(5):
            for j in range(i + 1, 5):
                f = Frs.get((REG[i], REG[j]))
                tot += -d[i] * d[j] * f
        res["F_comp_using_%s_pairs" % b] = tot
        res["F_comp_share_using_%s_pairs" % b] = tot / FB
    L.append("== %s ==" % rel)
    L.append("BA shares %s  Med shares %s" % ([round(x, 3) for x in pi["BA"]], [round(x, 3) for x in pi["Med"]]))
    L.append("BA-Med F_adj (B) %.5f ; F_comp %.5f (%.1f%%) with BA-bin pairs ; %.5f (%.1f%%) with Medieval-bin pairs" % (
        FB, res["F_comp_using_BA_pairs"], 100 * res["F_comp_share_using_BA_pairs"], res["F_comp_using_Med_pairs"], 100 * res["F_comp_share_using_Med_pairs"]))
    cen = []
    for N in (1e5, 3e5, 1e6, 3e6, 1e7):
        NeW = 4 * N / 7.0
        Fd = tB / (2 * NeW)
        cen.append(dict(N=N, Ne_wright=NeW, F_drift=Fd, ratio=FB / Fd, nondrift_share_needed=1 - Fd / FB))
        L.append("census %.0e: Wright N_e %.3g, F_drift %.2e, measured F_adj / F_drift %.1f, non-drift share needed %.2f%%" % (N, NeW, Fd, FB / Fd, 100 * (1 - Fd / FB)))
    res["census"] = cen
    res["break_even_N"] = NeB / (4 / 7.0)
    L.append("break-even census N = Ne(B)/0.571 = %.0f" % res["break_even_N"])
    dec = []
    for k, p in pairs.items():
        if k not in PUB:
            continue
        K, B = p["K"], p["B"]
        # K uses individuals; B1 uses mean chromosomes with the correct 1/n form
        nb0, nb1 = B["S"]
        corr1 = 1 / nb0 + 1 / nb1
        ne1 = p["t_gen"] / (2 * (B["F"] - corr1))
        dec.append(dict(pair=k, t=p["t_gen"], K=K["ne"], B1=ne1, B=B["ne"], pub=PUB[k], B1_over_K=ne1 / K["ne"], B_over_B1=B["ne"] / ne1,
                        B_over_K=B["ne"] / K["ne"], B_over_pub=B["ne"] / PUB[k], K_over_pub=K["ne"] / PUB[k]))
        L.append("%-8s K %6.0f  B1(mean n) %6.0f (%+.1f%% vs K)  B(site-wise) %6.0f (%+.1f%% vs B1; %+.1f%% vs K; %+.1f%% vs published %d)" % (
            k, K["ne"], ne1, 100 * (ne1 / K["ne"] - 1), B["ne"], 100 * (B["ne"] / ne1 - 1), 100 * (B["ne"] / K["ne"] - 1), 100 * (B["ne"] / PUB[k] - 1), PUB[k]))
    res["correction"] = dec
    reg = {}
    for rg, dd in ne["regions"].items():
        r = dd.get("BA-Med", {})
        if "ne" in r and r["ne"] == r["ne"]:
            reg[rg] = dict(ne=r["ne"], S=r["S"], F=r["F"], corr=r["corr"], power_ratio=min(r["S"]) / (10 * r["ne"] / r["t_gen"]))
            L.append("within-region BA-Med %-13s N_e %6.0f  S %.0f/%.0f  S / (10 N_e / t) = %.2f" % (rg, r["ne"], r["S"][0], r["S"][1], reg[rg]["power_ratio"]))
    res["within_region_BA_Med"] = reg
    out[rel] = res
json.dump(out, open(os.path.join(RAW, "c1d_posthoc3_keruru.json"), "w"), indent=1)
open(os.path.join(RAW, "c1d_posthoc3_keruru.txt"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
