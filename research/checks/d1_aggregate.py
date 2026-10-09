"""D1 POST HOC aggregation of d1_rna.json / d1_nn.json / d1_posthoc.json / d1_dms.json into the headline numbers used in
R4-D1-spike.md.  Analysis only, no new measurement.  Run: research/.venv/bin/python -I research/checks/d1_aggregate.py
Output: research/checks/results/raw/d1_aggregate.txt
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import d1_sequence_space_spike as D

RAW = D.RAW
LAM_ALT = {k: D.lam_alt(q) for k, q in D.Q_BASES.items()}
out = []
P = out.append


def load(n):
    p = os.path.join(RAW, n)
    return json.load(open(p)) if os.path.exists(p) else None


def rng_(a):
    a = [x for x in a if x is not None and np.isfinite(x)]
    if not a:
        return "-"
    return f"med {np.median(a):.3g} [{min(a):.3g}..{max(a):.3g}] n={len(a)}"


rn, nn, ph, dm = load("d1_rna.json"), load("d1_nn.json"), load("d1_posthoc.json"), load("d1_dms.json")
P("== flip thresholds (G1): m* = lam50(n_f)/lam_alt for each q basis")
for k, la in LAM_ALT.items():
    P(f"  {k}: lam_alt={la:.3f}  m*(n_f=1e3,1e4,2e5,2e7) = " + ", ".join(f"{D.lam50(nf)/la:.0f}" for nf in D.NF_LIST))
if rn:
    groups = {"all": lambda v: True, "L30": lambda v: v["L"] == 30, "L50": lambda v: v["L"] == 50,
              "L76(rand)": lambda v: v["L"] == 76 and v["name"] != "tRNA76", "L100": lambda v: v["L"] == 100,
              "tRNA76": lambda v: v["name"] == "tRNA76"}
    for g, f in groups.items():
        vs = [v for v in rn.values() if f(v)]
        P(f"\n-- RNA group {g} (n={len(vs)} targets)")
        P("  nu_mean: " + rng_([v["nu_mean"] for v in vs]))
        P("  site_neu paired: " + rng_([v["site_neu_paired"] for v in vs]) + " ; unpaired: " + rng_([v["site_neu_unpaired"] for v in vs]))
        P("  del strict / >2bp / shape: " + rng_([v["del_strict"] for v in vs]) + " | " + rng_([v["del_medium_gt2bp"] for v in vs]) + " | " + rng_([v["del_lenient_shape"] for v in vs]))
        for key in ("E0_uniform", "E0_freqw", "E1_uniform", "E1_freqw", "E2_uniform", "E2_freqw"):
            ss = [v["single"][key] for v in vs if key in v["single"]]
            if not ss:
                continue
            P(f"  {key}: reach {rng_([s['reach'] for s in ss])} ; m|reach {rng_([s['mean_pos'] for s in ss])} ; m_all {rng_([s['mean_all'] for s in ss])}")
            kb = [[kk for kk in s if kk.startswith('mpop') and kk.endswith('_mean') and kk not in ('mpop1_mean', 'mpop5_mean', 'mpop20_mean')] for s in ss]
            P(f"       mpop5 mean {rng_([s['mpop5_mean'] for s in ss])} ; mpop(K=KB) mean {rng_([s[k[0]] for s, k in zip(ss, kb) if k])}")
            mp = [s['mean_pos'] for s in ss if s['mean_pos']]
            if mp:
                P("       lam = m|reach * lam_alt: " + "; ".join(f"{k}: {np.median(mp)*la:.2f}" for k, la in LAM_ALT.items()))
        for cls in ("E0", "E1", "E2"):
            ds = [v["double"][cls] for v in vs if cls in v.get("double", {})]
            if ds:
                P(f"  double {cls}: frac_m1_zero {rng_([d['frac_m1_zero'] for d in ds])}; P(m2>0|m1=0) {rng_([d['P_m2_pos_given_m1_zero'] for d in ds])}; m2|pos {rng_([d['m2_mean_pos'] for d in ds])}")
        gr = [v["graded"] for v in vs]
        for kind in ("near", "far"):
            for bn in ("d0_1-4", "d0_5-10", "d0_11+"):
                xs = [g[kind][bn] for g in gr if kind in g and bn in g[kind]]
                if xs:
                    P(f"  graded {kind} {bn}: f_ben {rng_([x['f_ben'] for x in xs])}; f_worse {rng_([x['f_worse'] for x in xs])}; P_any_improver {rng_([x['P_any_improver'] for x in xs])}; strict_local_opt {rng_([x['strict_local_opt'] for x in xs])}")
        for kind in ("near", "far"):
            ws = [v["walk"][kind] for v in vs if kind in v.get("walk", {})]
            if ws:
                P(f"  walk {kind}: success {rng_([w['success'] for w in ws])}; trapped_no_move {rng_([w['trapped_no_move'] for w in ws])}; mean d_end {rng_([w['mean_d_end'] for w in ws])}")
if nn:
    P("\n-- NN size")
    for g, L in (("L30", 30), ("L50", 50), ("L76", 76), ("L100", 100)):
        vs = [v for v in nn.values() if v["L"] == L and v["log10_NN"] is not None]
        P(f"  {g}: log10|NN| {rng_([v['log10_NN'] for v in vs])} ; log10 fraction of 4^L {rng_([v['log10_frac_space'] for v in vs])}")
    P("  zero-hit targets (upper bound only): " + ", ".join(f"{k}: log10|NN|<={v['log10_NN_hi']:.1f}" for k, v in nn.items() if v["log10_NN"] is None))
if ph:
    P("\n-- post hoc refined classes")
    for nm in ("E0far", "E2g", "E2rare", "E2g_rare"):
        for g, f in (("all", lambda v: True), ("L<=50", lambda v: v["L"] <= 50), ("L>=76", lambda v: v["L"] >= 76), ("tRNA76", lambda v: v["name"] == "tRNA76")):
            ss = [v["single"][nm] for v in ph.values() if nm in v["single"] and f(v)]
            if ss:
                mp = [s['mean_pos'] for s in ss if s['mean_pos']]
                P(f"  {nm} {g}: reach {rng_([s['reach'] for s in ss])}; m|reach {rng_([s['mean_pos'] for s in ss])}; p90 {rng_([s['p90_pos'] for s in ss])}; mpop(K=KB) " +
                  rng_([s[[k for k in s if k.startswith('mpop') and k.endswith('_mean') and k not in ('mpop1_mean','mpop5_mean','mpop20_mean')][0]] for s in ss if any(k.startswith('mpop') for k in s)]) +
                  (("; lam@T3e5s.01 " + f"{np.median(mp)*LAM_ALT['T3e5_s0.01']:.2f}") if mp else ""))
    P("  neighbourhood composition: same-shape share " + rng_([v["nbr_share_same_shape_as_S1"] for v in ph.values()]) + "; fewer-helix share " + rng_([v["nbr_share_shape_change_fewer_helices"] for v in ph.values()]) + "; >=helix share " + rng_([v["nbr_share_shape_change_ge_helices"] for v in ph.values()]))
    P("  distinct shapes: " + rng_([v["n_distinct_shapes"] for v in ph.values()]) + "; top3 share " + rng_([v["top3_shape_share"] for v in ph.values()]))
    P("  Hamming mean/L among samples (random pair = 0.75): " + rng_([v["hamming_mean_over_L"] for v in ph.values()]) + "; seed->last " + rng_([v["hamming_seed_to_last_over_L"] for v in ph.values()]))
    P("  E0 pool d_bp(S1,S2) quantiles 10/25/50/75/90 (median across targets): " + str(np.median([v["pool_dbp_quantiles_E0"] for v in ph.values()], axis=0).round(1).tolist()))
if dm:
    P("\n-- DMS lam at single-codon and gene granularity (non-stability, coverage>=0.5; post hoc subset)")
    vs = [v for v in dm.values() if v["assay"] != "Stability" and v["coverage"] >= 0.5 and "m_snv_site_mean_func_0.5" in v]
    for nm in ("func_0.5", "nearWT_0.8", "ben_proxy_1.2"):
        ms = [v[f"m_snv_site_mean_{nm}"] for v in vs]
        mg = [v[f"m_gene_snv_{nm}"] for v in vs]
        P(f"  {nm}: m_snv per codon {rng_(ms)} -> lam@0.48 {np.median(ms)*0.48:.2f}; m_gene {rng_(mg)} -> lam@0.48 {np.median(mg)*0.48:.3g}")
    P(f"  n datasets = {len(vs)}; share with m_gene(ben proxy) >= m*(n_f=1e3, T3e5 s.01)=15: {np.mean([v['m_gene_snv_ben_proxy_1.2']>=15 for v in vs]):.2f}; >= 36 (n_f=2e7): {np.mean([v['m_gene_snv_ben_proxy_1.2']>=36 for v in vs]):.2f}; >=151 (s=.001,n_f=1e3): {np.mean([v['m_gene_snv_ben_proxy_1.2']>=151 for v in vs]):.2f}")
    P(f"  share of datasets with m_snv per codon (functional) >= 15: {np.mean([v['m_snv_site_mean_func_0.5']>=15 for v in vs]):.2f} (max possible ~7)")
txt = "\n".join(out)
open(os.path.join(RAW, "d1_aggregate.txt"), "w").write(txt)
print(txt)
