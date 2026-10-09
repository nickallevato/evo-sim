"""D1 FIX PASS (POST HOC; written after the three D1 reviews and after all main/post-hoc D1 output was seen).
DMS-side re-analyses requested by the reviews.  No new data.  Script committed before its first run.
Run: research/.venv/bin/python -I research/checks/d1_fix_dms.py   -> results/raw/d1_fix_dms.json, d1_fix_dms.txt

Parts
 S   s-sweep: lam = m * lam_alt(s,T) (lam_alt = 2N(mu/3)T*2s, linear in s; Day-family N=1e4, mu=1.2e-8, T=3e5 or 146,250) for the
     key m values; s at which each row crosses lam_50(n_f) (n_f = 1e3, 1e4, 2e4 ~ gene count, 2e5, 2e7).  Haldane 2s overstates q at
     large s; s=0.03-0.05 is a stress test, not a prediction.
 K   gene pool as k needed changes drawing from ONE shared pool of m beneficial-proxy SNVs, each succeeding w.p. q: P(Bin(m,q) >= k),
     k = 10, 25, 50; s = 0.01 (q=0.381) and 0.001 (q=0.047), per dataset and at the median m.  Share of datasets with zero proxy.
 P10 G1's required beneficial fraction (any-n-of-M) vs the measured within-gene proxy fraction (pre-registered P10, never reported).
 N   normalisation sensitivity (W-hat and N-hat estimators), the baseline share of 'reduced' at the W-defining sites, a mirror (lower
     tail) check on the beneficial proxy, missense-only denominators, protein-level clustering.
 D   Day's D2h sentence scored as worded: 'reduce or destroy' (= reduced, s*<0.8) and 'destroy' alone.
Headline group = non-stability sets with coverage >= 0.5 (the same 114 as the post hoc aggregate).
"""
import os, sys, json, csv, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.stats import binom
import d1_sequence_space_spike as D

RAW = D.RAW
N_POP, MU = 1e4, 1.2e-8
out = {}
txt = []
P = txt.append


def lam_alt_s(s, T):
    return 2 * N_POP * (MU / 3) * T * 2 * s


def q_s(s, T):
    return 1 - math.exp(-lam_alt_s(s, T))


dms = json.load(open(os.path.join(RAW, "d1_dms.json")))
rna = json.load(open(os.path.join(RAW, "d1_rna.json")))
ph = json.load(open(os.path.join(RAW, "d1_posthoc.json")))
ref = {r["DMS_id"]: r for r in csv.DictReader(open(os.path.join(D.DMS_DIR, "reference.csv"), newline=""))}
head = {k: v for k, v in dms.items() if v["assay"] != "Stability" and v["coverage"] >= 0.5}
if "--smoke" in sys.argv:
    head = dict(list(head.items())[:3])
P(f"headline group n = {len(head)}")

# ------------------------------------------------------------------------------------------------ S: s-sweep
med = lambda xs: float(np.median([x for x in xs if x is not None and np.isfinite(x)]))
rows = {
    "RNA exact S2, m|reach (E0 uniform)": med([v["single"]["E0_uniform"]["mean_pos"] for v in rna.values()]),
    "RNA exact S2, m_all (unconditional)": med([v["single"]["E0_uniform"]["mean_all"] for v in rna.values()]),
    "RNA exact S2 >=5bp (E0far, post hoc), m|reach": med([v["single"]["E0far"]["mean_pos"] for v in ph.values() if "E0far" in v["single"]]),
    "RNA exact S2 >=5bp (E0far), m_all": med([v["single"]["E0far"]["mean_all"] for v in ph.values() if "E0far" in v["single"]]),
    "RNA <=2bp (E1 uniform), m|reach": med([v["single"]["E1_uniform"]["mean_pos"] for v in rna.values()]),
    "RNA topology-no-loss L>=76 (E2g), m|reach": med([v["single"]["E2g"]["mean_pos"] for v in ph.values() if v["L"] >= 76 and "E2g" in v["single"]]),
    "RNA topology-no-loss L>=76 (E2g), m_all": med([v["single"]["E2g"]["mean_all"] for v in ph.values() if v["L"] >= 76 and "E2g" in v["single"]]),
    "DMS one codon tolerated (s*>=0.5)": med([v["m_snv_site_mean_func_0.5"] for v in head.values()]),
    "DMS one codon near-WT (s*>=0.8)": med([v["m_snv_site_mean_nearWT_0.8"] for v in head.values()]),
    "DMS one codon beneficial proxy (s*>=1.2)": med([v["m_snv_site_mean_ben_proxy_1.2"] for v in head.values()]),
    "DMS gene-level beneficial proxy (s*>=1.2)": med([v["m_gene_snv_ben_proxy_1.2"] for v in head.values()]),
}
out["rows_m"] = rows
nfs = [1e3, 1e4, 2e4, 2e5, 2e7]
P("\n== S. lam = m * lam_alt(s, T); T=3e5.  lam_alt = %.3f * (s/0.01)" % lam_alt_s(0.01, 3e5))
P("lam_50(n_f): " + ", ".join(f"{nf:g}: {D.lam50(nf):.2f}" for nf in nfs))
svals = [0.001, 0.003, 0.01, 0.02, 0.03, 0.05]
P("row | m | " + " | ".join(f"s={s}" for s in svals) + " | s at which lam = lam50 for n_f=" + ",".join(f"{nf:g}" for nf in nfs))
out["s_sweep"] = {}
for name, m in rows.items():
    lams = [m * lam_alt_s(s, 3e5) for s in svals]
    cross = [D.lam50(nf) / (m * lam_alt_s(1.0, 3e5)) if m > 0 else float("inf") for nf in nfs]
    out["s_sweep"][name] = dict(m=m, lam=lams, s_cross_T3e5=cross, s_cross_T146250=[D.lam50(nf) / (m * lam_alt_s(1.0, 146250)) if m > 0 else float("inf") for nf in nfs])
    P(f"{name} | {m:.3g} | " + " | ".join(f"{l:.3g}" for l in lams) + " | " + ", ".join(f"{c:.3g}" for c in cross))
P("(same with T=146,250 -> crossing s doubles; see json)")

# ------------------------------------------------------------------------------------------------ K: k-of-m
P("\n== K. k needed changes from one shared pool of m proxy-beneficial SNVs, P(Bin(m,q)>=k)")
ms = np.array([v["m_gene_snv_ben_proxy_1.2"] for v in head.values()])
out["share_zero_proxy_m_gene"] = float((ms == 0).mean())
out["share_proxy_frac_zero"] = float(np.mean([v["frac_ben_proxy_1.2"] == 0 for v in head.values()]))
P(f"share of datasets with m_gene proxy == 0: {out['share_zero_proxy_m_gene']:.3f}; with proxy fraction exactly 0: {out['share_proxy_frac_zero']:.3f}; m_gene quantiles 0/10/25/50/75/90/100: {np.percentile(ms,[0,10,25,50,75,90,100]).round(1).tolist()}")
out["k_of_m"] = {}
for lab, s, T in (("s0.01_T3e5", 0.01, 3e5), ("s0.01_T146250", 0.01, 146250), ("s0.001_T3e5", 0.001, 3e5)):
    q = q_s(s, T)
    for k in (10, 25, 50):
        pm = float(binom.sf(k - 1, int(round(np.median(ms))), q))
        pd = np.array([binom.sf(k - 1, int(round(m)), q) if m >= k else 0.0 for m in ms])
        out["k_of_m"][f"{lab}_k{k}"] = dict(q=q, P_at_median_m=pm, share_datasets_P_ge_half=float((pd >= 0.5).mean()), median_P=float(np.median(pd)))
        P(f"{lab} q={q:.3f} k={k}: P at median m ({int(round(np.median(ms)))}) = {pm:.3g}; median over datasets {np.median(pd):.3g}; share of datasets with P>=0.5 {np.mean(pd>=0.5):.2f}")

# ------------------------------------------------------------------------------------------------ P10
P("\n== P10. G1 required beneficial fraction (n / (p * supply)) vs measured within-gene proxy fraction (s*>=1.2, upper bound)")
fb = np.array([v["frac_ben_proxy_1.2"] for v in head.values()])
out["proxy_frac"] = dict(median=float(np.median(fb)), q25=float(np.percentile(fb, 25)), q75=float(np.percentile(fb, 75)), mean=float(fb.mean()))
P(f"measured proxy fraction: median {np.median(fb):.4f}, IQR {np.percentile(fb,25):.4f}-{np.percentile(fb,75):.4f}, mean {fb.mean():.4f}")
out["P10"] = []
for n in (2e5, 2e7):
    for p in (0.02, 0.002):
        for sup in (4.5e11, 2.3e11):
            req = n / (p * sup)
            out["P10"].append(dict(n=n, p=p, supply=sup, required=req, ratio_median=float(np.median(fb) / req), share_datasets_ge=float((fb >= req).mean()), ratio_if_1pct_genome=float(np.median(fb) * 0.01 / req)))
            P(f"n={n:g} p={p} supply={sup:g}: required {req:.2e}; median proxy / required = {np.median(fb)/req:.3g}; share of datasets at or above {np.mean(fb>=req):.2f}; ratio if only 1% of mutations fall in such genes {np.median(fb)*0.01/req:.3g}")

# ------------------------------------------------------------------------------------------------ N: normalisation sensitivity
def analyse(path, wmeth, nmeth):
    sites, wts, muts, sc, binv = D.load_dms(path)
    usites = np.unique(sites)
    sidx = {s: i for i, s in enumerate(usites)}
    si = np.array([sidx[s] for s in sites])
    ns = len(usites)
    srt = np.sort(sc)
    frac_low = {"low5": 0.05, "low1": 0.01, "low10": 0.10}[nmeth]
    N_hat = float(np.median(srt[: max(5, int(frac_low * len(sc)))]))
    med_site = np.array([np.median(sc[si == i]) if (si == i).sum() >= 5 else np.nan for i in range(ns)])
    if wmeth == "q75sites":
        top = np.flatnonzero(~np.isnan(med_site) & (med_site >= np.nanpercentile(med_site, 75)))
        W_hat = float(np.median(sc[np.isin(si, top)]))
    elif wmeth == "top10sites":
        top = np.flatnonzero(~np.isnan(med_site) & (med_site >= np.nanpercentile(med_site, 90)))
        W_hat = float(np.median(sc[np.isin(si, top)]))
    else:  # p90all
        top = np.array([], int)
        W_hat = float(np.percentile(sc, 90))
    if W_hat - N_hat < 1e-9:
        return None
    ss = (sc - N_hat) / (W_hat - N_hat)
    r = dict(func=float((ss >= 0.5).mean()), reduced=float((ss < 0.8).mean()), destroyed=float((ss < 0.2).mean()), ben=float((ss >= 1.2).mean()))
    if wmeth == "q75sites":
        t = ss[np.isin(si, top)]
        r["baseline_reduced_at_Wsites"] = float((t < 0.8).mean())
        r["Wsites_ben"] = float((t >= 1.2).mean())
        r["Wsites_below_mirror0.8"] = float((t <= 0.8).mean())
    # missense-only denominator and per-codon counts
    F = np.full((ns, 20), np.nan)
    wt_of = {}
    for k in range(len(sc)):
        F[si[k], D.AAS.index(muts[k])] = ss[k]
        wt_of[si[k]] = wts[k]
    nm = (~np.isnan(F)).sum(axis=1)
    good = nm >= 10
    if good.any():
        mfun, mtot, mben = [], [], []
        for i in np.flatnonzero(good):
            a = D.AAS.index(wt_of[i])
            meas = ~np.isnan(F[i])
            fr = (np.nansum(F[i] >= 0.5) / meas.sum())
            frb = (np.nansum(F[i] >= 1.2) / meas.sum())
            w = D.SNV[a, :20]
            fp = np.where(meas, (np.nan_to_num(F[i]) >= 0.5).astype(float), fr)
            bp = np.where(meas, (np.nan_to_num(F[i]) >= 1.2).astype(float), frb)
            mfun.append(float((w * fp).sum()))
            mben.append(float((w * bp).sum()))
            mtot.append(float(w.sum()))
        r["m_snv_func"] = float(np.mean(mfun))
        r["m_snv_ben"] = float(np.mean(mben))
        r["missense_per_codon"] = float(np.mean(mtot))
        r["stop_per_codon"] = float(np.mean([D.SNV[D.AAS.index(wt_of[i]), 20] for i in np.flatnonzero(good)]))
        r["frac_missense_func"] = float(np.sum(mfun) / np.sum(mtot))
    return r


variants = [("q75sites", "low5"), ("q75sites", "low1"), ("q75sites", "low10"), ("top10sites", "low5"), ("p90all", "low5"), ("p90all", "low1")]
P("\n== N. normalisation sensitivity over the headline group (median over datasets; share of datasets with majority reduced / destroyed)")
out["norm"] = {}
per = {}
for wm, nm_ in variants:
    rs = {}
    for k in head:
        rr = analyse(os.path.join(D.DMS_DIR, "x", "DMS_ProteinGym_substitutions", ref[k]["DMS_filename"]), wm, nm_)
        if rr:
            rs[k] = rr
    per[(wm, nm_)] = rs
    a = lambda key: [r[key] for r in rs.values() if key in r]
    d = dict(n=len(rs), func=float(np.median(a("func"))), reduced=float(np.median(a("reduced"))), destroyed=float(np.median(a("destroyed"))),
             maj_reduced=float(np.mean([x > 0.5 for x in a("reduced")])), maj_destroyed=float(np.mean([x > 0.5 for x in a("destroyed")])), ben=float(np.median(a("ben"))))
    out["norm"][f"{wm}/{nm_}"] = d
    P(f"{wm}/{nm_}: n={d['n']} functional {d['func']:.3f}, reduced {d['reduced']:.3f}, destroyed {d['destroyed']:.3f}, majority-reduced {d['maj_reduced']:.2f}, majority-destroyed {d['maj_destroyed']:.2f}, ben {d['ben']:.4f}")
base = per[("q75sites", "low5")]
bl = [r["baseline_reduced_at_Wsites"] for r in base.values()]
P(f"baseline: share of substitutions AT THE W-DEFINING (most tolerant quartile) SITES with s*<0.8: median {np.median(bl):.3f} IQR {np.percentile(bl,25):.3f}-{np.percentile(bl,75):.3f}")
ben_w = [r["Wsites_ben"] for r in base.values()]
mir_w = [r["Wsites_below_mirror0.8"] for r in base.values()]
P(f"mirror check at W-defining sites: share s*>=1.2 median {np.median(ben_w):.3f}; share s*<=0.8 (mirror of 1.2 about W) median {np.median(mir_w):.3f}; datasets where upper tail > lower tail: {np.mean(np.array(ben_w) > np.array(mir_w)):.2f}")
P("(the lower tail contains real damage, so it is an UPPER bound on a symmetric-noise tail; the proxy has no replicate-based noise null)")
out["baseline_reduced"] = dict(median=float(np.median(bl)), q25=float(np.percentile(bl, 25)), q75=float(np.percentile(bl, 75)))
out["mirror"] = dict(ben_median=float(np.median(ben_w)), mirror_median=float(np.median(mir_w)), share_upper_gt_lower=float(np.mean(np.array(ben_w) > np.array(mir_w))))
mc = lambda key: [r[key] for r in base.values() if key in r]
P(f"missense-only: missense SNVs per codon {np.median(mc('missense_per_codon')):.2f}, stop SNVs per codon {np.median(mc('stop_per_codon')):.2f}; functional per codon {np.median(mc('m_snv_func')):.2f}; fraction of missense SNVs functional {np.median(mc('frac_missense_func')):.3f}")
out["missense"] = dict(missense_per_codon=float(np.median(mc("missense_per_codon"))), stop_per_codon=float(np.median(mc("stop_per_codon"))), frac_missense_func=float(np.median(mc("frac_missense_func"))))

# protein-level clustering
groups = collections.defaultdict(list)
for k, v in head.items():
    groups["_".join(k.split("_")[:2])].append(v)
P(f"\nprotein-level: {len(groups)} distinct proteins among {len(head)} datasets (key = first two tokens of DMS_id)")
out["n_proteins"] = len(groups)
for key in ("frac_func_0.5", "frac_nearWT_0.8", "frac_reduced_lt0.8", "frac_destroyed_lt0.2", "frac_ben_proxy_1.2", "m_snv_site_mean_func_0.5", "m_gene_snv_ben_proxy_1.2"):
    pm = [np.mean([x[key] for x in g]) for g in groups.values()]
    P(f"  {key}: dataset median {np.median([v[key] for v in head.values()]):.4g}; protein-level median {np.median(pm):.4g}")
    out.setdefault("protein_level", {})[key] = float(np.median(pm))
mr = [np.mean([x["frac_reduced_lt0.8"] > 0.5 for x in g]) > 0.5 for g in groups.values()]
P(f"  proteins whose (averaged) datasets have majority reduced: {np.mean(mr):.2f}")

# ------------------------------------------------------------------------------------------------ D: Day's sentence
P("\n== D. D2h as worded")
red = np.array([v["frac_reduced_lt0.8"] for v in head.values()])
des = np.array([v["frac_destroyed_lt0.2"] for v in head.values()])
man = [v["frac_authorcutoff_bin1"] for v in head.values() if v.get("frac_authorcutoff_bin1") is not None]
P(f"'reduce or destroy' (s*<0.8) majority in {np.mean(red>0.5):.2f} of datasets (median share {np.median(red):.3f}); 'destroy' alone (s*<0.2) majority in {np.mean(des>0.5):.2f} (median {np.median(des):.3f}); author-cutoff manual sets n={len(man)}: fit {np.median(man):.3f}, unfit {1-np.median(man):.3f}")
out["day_sentence"] = dict(maj_reduced=float(np.mean(red > 0.5)), maj_destroyed=float(np.mean(des > 0.5)), author_fit_median=float(np.median(man)), n_manual=len(man))
sfx = "_smoke" if "--smoke" in sys.argv else ""
open(os.path.join(RAW, f"d1_fix_dms{sfx}.txt"), "w").write("\n".join(txt))
json.dump(out, open(os.path.join(RAW, f"d1_fix_dms{sfx}.json"), "w"), indent=1, default=float)
print("\n".join(txt))
