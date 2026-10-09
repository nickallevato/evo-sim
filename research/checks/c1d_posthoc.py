"""C1d POST HOC -- written AFTER seeing the main run of c1d_aadr_real.py (v62 and v66).  Nothing here is pre-registered.

THROWAWAY.  Run on na-workhorse after c1d_aadr_real.py extract has written the per-SNP group counts:
    research/.venv/bin/python -I research/checks/c1d_posthoc.py <v62|v66>
Reads the derived counts (C1D_OUT) and the .snp file (alleles); writes research/checks/results/raw/c1d_<rel>_posthoc.{json,txt}.

WHY (what the main run showed, which prompted these checks).  The literal E1/T2 reading of Day's method on the v62 genotypes gave
62,757 eligible alleles (Day 22,428) and 4,957 events in the 5000-6000 BP and younger bins (Day 21), of which 4,177 in the 0-500 BP
bin (Day 2).  Questions asked after seeing that:
  A. Are the post-6000 BP events frequency sweeps, or alleles near but not at fixation that a large bin happens to sample as 100%?
     (anatomy of the events: minor-allele frequency in the older bins; transitions vs transversions)
  B. Does restricting to transversion-only SNPs (immune to deamination damage) change eligible and the 21?
  C. Do other readings of "fixation event" come near Day's numbers: T3 = forward first passage (the first bin at 100% after an
     earlier bin <100%); polymorphism required to be more than a singleton (pooled Neolithic minor count >= 2, 3, 5)?
  D. (B2e) How large is F between REGIONS inside one time bin (pure spatial structure, no time elapsed) compared with the temporal
     F that keruru reads as drift?  F_adj between two same-time samples is about 2 Fst (+ relatedness/batch effects).
No predictions were registered for these.  They are exploratory and are reported as such.
"""
import os
import sys
import json
import importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("c1d", os.path.join(HERE, "c1d_aadr_real.py"))
c1d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c1d)


def load_alleles(rel):
    a1, a2 = [], []
    with open(os.path.join(c1d.DATA, c1d.REL[rel]["stem"] + ".snp")) as f:
        for line in f:
            p = line.split()
            if p:
                a1.append(p[4])
                a2.append(p[5])
    return np.array(a1), np.array(a2)


def t3_events(n, r, m=1, minor_min=0):
    """Forward first passage: event bin = first bin at 100% (observed) that has an EARLIER observed bin <100%; eligible =
    modern 100% and pooled Neolithic polymorphic (E1) with Neolithic minor count >= minor_min (0 = no extra condition)."""
    S = n.shape[1]
    obs = n >= m
    tr = obs.all(axis=0)
    hist = np.zeros(c1d.NB, dtype=np.int64)
    elig = 0
    for allele in (0, 1):
        k = r if allele == 0 else (n - r)
        fixed = obs & (k == n)
        neo_n, neo_k = n[2] + n[3], k[2] + k[3]
        e = fixed[10] & (neo_n >= m) & (neo_k < neo_n) & ((neo_n - neo_k) >= max(1, minor_min))
        seen_poly = np.zeros(S, dtype=bool)
        date = np.full(S, -1)
        for b in range(c1d.NB):
            hit = obs[b] & fixed[b] & seen_poly & (date < 0)
            date = np.where(hit, b, date)
            seen_poly |= obs[b] & ~fixed[b]
        elig += int(e.sum())
        hist += np.bincount(date[e & tr & (date >= 0)], minlength=c1d.NB)
    tot = int(hist.sum())
    return dict(eligible=elig, tracked_events=tot, profile=[int(x) for x in hist], pre7000_share=float(hist[:3].sum() / max(1, tot)),
                S21=int(hist[4:].sum()), S23=int(hist[3:].sum()))


def minor_t2(n, r, minor_min, snpmask=None):
    """E1 with the Neolithic polymorphism requirement 'minor count >= minor_min', T2 dating, tracked all11, m=1."""
    S = n.shape[1]
    obs = n >= 1
    tr = obs.all(axis=0)
    hist = np.zeros(c1d.NB, dtype=np.int64)
    elig = 0
    keep = np.ones(S, dtype=bool) if snpmask is None else snpmask
    for allele in (0, 1):
        k = r if allele == 0 else (n - r)
        fixed = obs & (k == n)
        neo_n, neo_k = n[2] + n[3], k[2] + k[3]
        e = fixed[10] & (neo_n >= 1) & ((neo_n - neo_k) >= minor_min) & keep
        dt = np.argmax(fixed, axis=0)
        elig += int(e.sum())
        hist += np.bincount(dt[e & tr], minlength=c1d.NB)
    tot = int(hist.sum())
    return dict(eligible=elig, tracked_events=tot, profile=[int(x) for x in hist], pre7000_share=float(hist[:3].sum() / max(1, tot)),
                S21=int(hist[4:].sum()), S23=int(hist[3:].sum()))


def anatomy(n, r, chrom, is_ts):
    res = c1d.day_events(n, r, "E1", "T2", 1, "all11", None, ret_idx=True)
    rows = []
    for (allele, ie, dt, tr) in res["idx"]:
        k = r if allele == 0 else (n - r)
        for j in range(len(ie)):
            if not tr[j] or dt[j] < 3:
                continue
            i = ie[j]
            older = slice(0, dt[j])
            nn, kk = n[older, i].sum(), k[older, i].sum()
            nall, kall = n[:, i].sum(), k[:, i].sum()
            rows.append((int(dt[j]), (nn - kk) / max(1, nn), (nall - kall) / max(1, nall), bool(is_ts[i]), int(nn - kk)))
    arr = np.array(rows, dtype=float)
    out = {}
    bins = [(0, 0.01), (0.01, 0.02), (0.02, 0.05), (0.05, 0.10), (0.10, 1.01)]
    for name, sel in (("S23_all", np.ones(len(arr), bool)), ("S21", arr[:, 0] >= 4), ("modern_only_0-500", arr[:, 0] == 10),
                      ("dated_3-9", (arr[:, 0] >= 3) & (arr[:, 0] <= 9))):
        a = arr[sel]
        out[name] = dict(n=int(len(a)),
                         minor_freq_older_bins={"%g-%g" % b: int(((a[:, 1] >= b[0]) & (a[:, 1] < b[1])).sum()) for b in bins},
                         minor_freq_all_bins={"%g-%g" % b: int(((a[:, 2] >= b[0]) & (a[:, 2] < b[1])).sum()) for b in bins},
                         share_transition=float(a[:, 3].mean()) if len(a) else None,
                         median_minor_copies_older=float(np.median(a[:, 4])) if len(a) else None)
    return out


def region_floor(cnt, chrom):
    """F_adj (form B) between regional samples in the SAME time bin."""
    regs = list(c1d.REGIONS)
    out = []
    for b in ("EN", "LN", "BA", "Iron", "Med"):
        for i in range(len(regs)):
            for j in range(i + 1, len(regs)):
                ga, gb = "krreg_%s:%s" % (regs[i], b), "krreg_%s:%s" % (regs[j], b)
                try:
                    r = c1d.ne_pair(cnt, ga, gb, 100.0, chrom, "B", min_called=20)
                except Exception:               # noqa: BLE001
                    continue
                if r["n_snp"] > 100000 and r["F_adj"] == r["F_adj"]:
                    out.append(dict(bin=b, a=regs[i], b=regs[j], F=r["F"], corr=r["corr"], F_adj=r["F_adj"], S=r["S"], n_snp=r["n_snp"]))
    return out


def main(rel):
    N, D, names, sel, ic, ih = c1d.load_counts(rel)
    cnt = c1d.Counts(N, D, names)
    ids, chrom, pos = c1d.load_snp(rel)
    a1, a2 = load_alleles(rel)
    is_ts = ((a1 == "A") & (a2 == "G")) | ((a1 == "G") & (a2 == "A")) | ((a1 == "C") & (a2 == "T")) | ((a1 == "T") & (a2 == "C"))
    S = len(chrom)
    n = np.zeros((c1d.NB, S), dtype=np.int32)
    r = np.zeros((c1d.NB, S), dtype=np.int32)
    for i, nm in enumerate(c1d.DAY_NAMES):
        n[i], r[i] = cnt.chrom("day1:%s" % nm)
    out = {"rel": rel, "n_snp": int(S), "share_transition_panel": float(is_ts.mean())}
    # A anatomy
    out["anatomy"] = anatomy(n, r, chrom, is_ts)
    # B transversion / transition only
    out["by_substitution_class"] = {}
    for label, mask in (("all", None), ("transversions", ~is_ts), ("transitions", is_ts), ("transversions_autosomes", (~is_ts) & (chrom <= 22))):
        s = c1d.summarise_day(c1d.day_events(n, r, "E1", "T2", 1, "all11", mask))
        out["by_substitution_class"][label] = s
    # C other readings
    out["readings"] = {"T3_forward": t3_events(n, r)}
    for mm in (2, 3, 5, 10):
        out["readings"]["minor>=%d_T2" % mm] = minor_t2(n, r, mm)
        out["readings"]["minor>=%d_T2_transversions" % mm] = minor_t2(n, r, mm, ~is_ts)
    out["readings"]["T3_minor>=2"] = t3_events(n, r, minor_min=2)
    # D spatial floor
    out["region_floor"] = region_floor(cnt, chrom)
    res = os.path.join(c1d.RES, "c1d_%s_posthoc" % rel)
    with open(res + ".json", "w") as f:
        json.dump(out, f, indent=1)
    L = ["== C1d POST HOC %s ==" % rel, "panel transition share %.3f" % out["share_transition_panel"]]
    L.append("-- A. anatomy of events dated 6000-7000 BP and younger (E1-T2, m=1, all11) --")
    for k, v in out["anatomy"].items():
        L.append("%s: n=%d  older-bin minor freq %s  all-bin minor freq %s  transition share %.3f  median minor copies %.1f" % (
            k, v["n"], v["minor_freq_older_bins"], v["minor_freq_all_bins"], v["share_transition"] or 0, v["median_minor_copies_older"] or 0))
    L.append("-- B. substitution class (E1-T2 m=1 all11) --")
    for k, v in out["by_substitution_class"].items():
        L.append("%s: elig %d tracked %d pre7000 %.4f S21 %d S23 %d profile %s start %s" % (
            k, v["eligible"], v["tracked"], v["pre7000_share"] or 0, v["S21"], v["S23"], v["profile"], ["%.1f" % x for x in v["start_pct"]]))
    L.append("-- C. other readings --")
    for k, v in out["readings"].items():
        L.append("%s: elig %d events %d pre7000 %.4f S21 %d S23 %d profile %s" % (k, v["eligible"], v["tracked_events"], v["pre7000_share"], v["S21"], v["S23"], v["profile"]))
    L.append("-- D. F_adj between regions in the same bin (form B) --")
    for x in out["region_floor"]:
        L.append("%-5s %-13s %-13s F %.5f corr %.5f F_adj %.5f S %.0f/%.0f nSNP %d" % (x["bin"], x["a"], x["b"], x["F"], x["corr"], x["F_adj"], x["S"][0], x["S"][1], x["n_snp"]))
    with open(res + ".txt", "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1])
