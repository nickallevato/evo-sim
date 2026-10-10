"""FM fix pass 2: post hoc (after re-review 43dca91) follow-ups to R4-FM, pre-registered before any of them is run.

Tier: part of the load-bearing FM check (ROOT-FM).  Post hoc relative to R4-FM (d723064) and to fm_mirror.py
(737648e).  Asked for by REVIEW-R4-FM-mirror-combined.md (D-1 MAJOR; C-2, C-3, C-4 MINOR; C-8 NOTE).  This
docstring and the code are committed BEFORE the run.  Runs on na-workhorse only.  fm_mirror.py and
fm_mesa_replication.py are imported unchanged (by file path).

ALREADY KNOWN before this registration (disclosed; the tests below are scored against it, not tuned to it):
  E1 observed median S_H (fm_extra.json): F0 10 kb 0.51, F0 100 kb 0.06, F2 10 kb 0.51, F2 100 kb 0.22;
  S_C 0.48, 0.18, 0.47, -0.05.  S2 hs1 chrX F1 100 kb: top window 57.3 Mb (r_H 131.9, r_C -23.9, rep 0.98),
  approximate R without it 1.15 (no refit).  Mirror M3 chimp-ref chrX F1 100 kb: 16.38 / 4.84 = 3.39.
  The review's unverified memory pointer: the CHM13 chrX centromeric array begins near 57.8 Mb.
  The five annotation files below were fetched (md5 = the S3 ETag) but not opened.
  Pre-run smoke test (tiny synthetic genome, 8 edges, flat background, true steps at random positions): T1 gave
  S_step_aligned ~1.03, S_step_offset ~0.46, S_ramp10 ~0.40, S_ramp40 ~0.27 at 10 kb, i.e. the window grid alone
  roughly halves S for a perfect step.  T3 minus-strand conversion checked on a two-block MAF.

DATA (untrusted, read only, never executed; each in its own new directory on workhorse)
  results/raw/fm_bins.npz (hs1), results/raw/fm_mirror_bins.npz (chimp-ref), both workhorse only.
  sources/raw/fm-maf-2026-10-10/hs1.maf.gz and sources/raw/fm-mirror-2026-10-10/pantro.maf.gz (as in R4-FM / mirror).
  sources/raw/fm-annot-2026-10-10-<name>/<name>.bed from human-pangenomics T2T/CHM13/assemblies/annotation/:
    chm13v2.0_censat_v2.1.bed (md5 9838d9f1...4041), chm13v2.0_chrXY_sequence_class_v1.bed (867b9217...603fd),
    chm13v2.0_cytobands_allchrs.bed (1db3de2e...fbfd), chm13v2.0_composite-repeats_2022DEC.bed (f1e53a7d...ab9f6f6),
    chm13v2.0_new-satellites_2022DEC.bed (db535eda...e399).  Columns 1-4 used (chrom, start, end, name).

T1 (D-1) PERFECT-STEP CALIBRATION OF THE E1 SHARPNESS STATISTIC.  Autosomes, hs1, cells F0/F2 x 10/100 kb,
   the H lineage.  On the real core-column array m (1 kb bins) of each cell, build synthetic H counts
   n ~ Poisson(m * p_H * rho) where rho = 1 outside blocks and, for every observed H mesa (FM rule), a block of
   the same length at level d_mesa / p_H (d_mesa = the mesa's observed 1 kb density).  Four landscapes:
     step_aligned  block edges exactly on the window grid (best case for the estimator);
     step_offset   block shifted by a uniform integer offset in [-W/2, W/2] bins (a perfect step at a random
                   position relative to the window grid: the realistic benchmark for "sharp boundaries");
     ramp10, ramp40  same offset blocks, each edge a linear ramp over 10 kb / 40 kb centred on it ("soft").
   Synthetic mesas are called with FM.mesas on the synthetic window sums and scored with fm_mirror.edge_stats
   unchanged (5 kb inside/outside), 5 replicates; S_* = the median over replicates of the per-replicate median S.
   q = (S_obs - S_ramp40) / (S_step_offset - S_ramp40).  A cell is RESOLVED if S_step_offset - S_ramp40 >= 0.15
   and the step_offset replicates have >= 50 edges on average.
   Day (FM4 "sharp boundaries", descriptive): both 10 kb cells resolved and q >= 0.75 (observed edges as sharp as
     a perfect step, given the estimator).
   Critics (graded rate landscape): both 10 kb cells resolved and q <= 0.25 (as soft as a 40 kb ramp or softer).
   Otherwise indeterminate.  100 kb cells: descriptive; if unresolved there, "soft at 100 kb" is withdrawn as a
   resolution artefact (review D-1).  Audit expectation (not a side): S_step_offset < 1 at 10 kb (window-grid
   dilution and noise-selected d_mesa), and the 100 kb cells are unresolved.
   VERDICT MAPPING (FM4 "sharp boundaries" only; clustering is unaffected): Day hit -> external `supported` as a
   description at 10 kb resolution (non-discriminating, since S_C is alike); critic hit -> `contested`, leaning
   critic (edges graded); indeterminate -> `pending`.  The relative reading (H edges no sharper than C) stands
   in every case.

T2 (C-2, C-3) LEAVE-TOP-WINDOW, symmetric on both references.  Cells: autosomes F0 100 kb, F0 1 Mb, F1 100 kb,
   F2 100 kb; chrX F0 100 kb, F1 10 kb, F1 100 kb, F1 1 Mb, F2 100 kb; for hs1 and chimp-ref bins.  For each:
   R = mean r_H^2 / mean r_C^2 (fm_mirror.resid, het-mu null); the null is REFITTED after dropping (a) the window
   with the largest r_H^2, (b) the window with the largest r_C^2, (c) the top 1% of windows by max(r_H^2, r_C^2);
   share of sum r_H^2 and sum r_C^2 in the single top window.  chrX F1 100 kb: top 20 windows by r_H on each
   reference (start Mb, r_H, r_C, repeat share).
   P-T2a chimp-ref chrX F1 100 kb (C-3).  Critics/audit (review bound ~0.75): R after (a) <= 1.5.  Day: R after
     (a) > 1.5 (the excess is not one window on the chimp reference).
   P-T2b hs1 chrX F1 100 kb, refitted.  Audit: R after (a) within 0.1 of the approximate 1.15.  Descriptive.
   P-T2c single-window dominance of the critic-favourable cells (symmetry): chimp-ref autosomes F0 100 kb and 1 Mb
     (R 0.25 / 0.19).  Day: R after (b) >= 0.67 in either cell (the chimp-heavy excess is one window).  Critics:
     R after (b) <= 0.67 in both.  Same for hs1 autosomes F0 100 kb / 1 Mb (R 1.97 / 1.83) after (a):
     Day: >= 1.5 in both; critics: < 1.5 in either.  Other cells descriptive.

T3 (C-3) ORTHOLOGY OF THE chrX HOTSPOT.  (i) Stream pantro.maf.gz: for the top 5 chimp-ref chrX F1 100 kb windows
   by r_H, sum the aligned hs1 bases per hs1 chromosome and per hs1 100 kb bin (forward-strand coordinates).
   (ii) Stream hs1.maf.gz: for hs1 chrX:57,300,000-57,400,000, sum the aligned chimp bases per chimp chromosome
   (assembly-report names) and per chimp 100 kb bin.
   Prediction (critics/audit, review C-3): the top chimp-ref window maps to hs1 chrX 57.2-57.5 Mb (the same region
   carries M3).  Day: no prediction on location; if it maps elsewhere, the chimp-ref excess is a second region.

T4 (C-4) ANNOTATION OF THE hs1 57.3 Mb WINDOW.  For each of the hs1 chrX F1 100 kb top 20 windows: bp overlap with
   each named interval of the five files; the nearest censat interval within 2 Mb (name, distance).
   Critics/alignment-artefact reading: the top window overlaps a censat satellite/centromeric-transition class
   or an ampliconic/XTR class (a region known for assembly and alignment differences).  Day (real human-lineage
   hotspot): no satellite, ampliconic or XTR overlap.  Overlap with a censat class whose name marks it as
   centromeric transition ("ct") counts for critics.  Neither reading follows from the overlap alone: it says what
   the region is, not what caused the excess.

T5 (C-8) M6 counts: raw W->S and S->W counts in and outside H and C mesas, chimp-ref F2 100 kb (descriptive).

Usage (workhorse): `calib <hs1 npz> <out.json>`;  `lt <hs1 npz> <chimp npz> <annot dir glob prefix> <out.json>`;
  `mapc <chimp npz> <pantro.maf.gz> <out.json>`;  `maph <hs1.maf.gz> <out.json>`.
"""
import glob
import importlib.util
import json
import pathlib
import subprocess
import sys
import time

import numpy as np

_p = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("fmm", _p / "fm_mirror.py")
MM = importlib.util.module_from_spec(_s)
_s.loader.exec_module(MM)
FM = MM.FM


def auto_of(chroms):
    return [c for c in chroms if c.replace("chr", "").isdigit()]


# ------------------------------------------------------------------------------------------------ T1
def calib(npz, outjson):
    z, meta, chroms = FM.load(npz)
    auto = auto_of(chroms)
    rng = np.random.default_rng(FM.SEED + 2)
    res = {}
    for filt in ("F0", "F2"):
        for W in (10, 100):
            t = time.time()
            w, cid, ok, per = MM.build(z, auto, filt, W)
            m_ = w["m"].astype(float)
            t0 = w["t0"]
            pH = w["H"][ok].sum() / w["m"][ok].sum()
            runs = FM.mesas(w["H"].astype(float), m_, cid, ok, pH)
            obs = MM.edge_stats(runs, per, "H", cid, t0, W, pH)
            blocks = []
            for i, j in runs:
                ci = cid[i]
                s, e = int(t0[i]), int(t0[j] + W)
                dm = per[ci]["H"][s:e].sum() / max(per[ci]["m"][s:e].sum(), 1)
                blocks.append((ci, s, e, dm / pH))
            cell = {"obs_S_q": obs["S_q"], "obs_edges": obs["edges"], "n_mesas": len(runs)}
            for variant in ("step_aligned", "step_offset", "ramp10", "ramp40"):
                Sm, ne, nm = [], [], []
                for rep in range(5):
                    rho = [np.ones(len(b["m"])) for b in per]
                    for ci, s, e, lev in blocks:
                        off = 0 if variant == "step_aligned" else int(rng.integers(-(W // 2), W // 2 + 1))
                        a, b = max(s + off, 0), min(e + off, len(rho[ci]))
                        if b <= a:
                            continue
                        if variant.startswith("ramp"):
                            hw = int(variant[4:]) // 2
                            lo, hi = max(a - hw, 0), min(b + hw, len(rho[ci]))
                            x = np.arange(lo, hi) + 0.5
                            up = np.clip((x - (a - hw)) / (2 * hw), 0, 1)
                            dn = np.clip(((b + hw) - x) / (2 * hw), 0, 1)
                            seg = 1 + (lev - 1) * np.minimum(up, dn)
                            rho[ci][lo:hi] = np.maximum(rho[ci][lo:hi], seg)
                        else:
                            rho[ci][a:b] = np.maximum(rho[ci][a:b], lev)
                    nb = [rng.poisson(per[k]["m"] * pH * rho[k]).astype(float) for k in range(len(per))]
                    nw = MM.agg(nb, W)
                    ps = nw[ok].sum() / w["m"][ok].sum()
                    rr = FM.mesas(nw, m_, cid, ok, ps)
                    st = MM.edge_stats(rr, per, "H", cid, t0, W, ps, nfun=lambda ci, nb=nb: nb[ci])
                    Sm.append(st["S_q"][1]); ne.append(st["edges"]); nm.append(len(rr))
                cell[variant] = {"median_S_per_rep": Sm, "S": float(np.median(Sm)), "edges": ne, "mesas": nm}
            Sobs, Sst, Sr = obs["S_q"][1], cell["step_offset"]["S"], cell["ramp40"]["S"]
            cell["q"] = float((Sobs - Sr) / (Sst - Sr)) if Sst != Sr else float("nan")
            cell["resolved"] = bool((Sst - Sr) >= 0.15 and np.mean(cell["step_offset"]["edges"]) >= 50)
            res[f"{filt}|{W}kb"] = cell
            print("T1", filt, W, json.dumps({"S_obs": Sobs, "edges_obs": obs["edges"],
                                             **{v: cell[v]["S"] for v in ("step_aligned", "step_offset", "ramp10", "ramp40")},
                                             "edges_step_offset": cell["step_offset"]["edges"],
                                             "q": cell["q"], "resolved": cell["resolved"]}),
                  f"{time.time() - t:.0f}s", flush=True)
    json.dump(res, open(outjson, "w"), indent=1)


# ------------------------------------------------------------------------------------------------ T2, T4, T5
def r_after(w, ok, drop_idx):
    ok2 = ok.copy()
    ok2[drop_idx] = False
    rH, rC = MM.resid(w, "H", ok2), MM.resid(w, "C", ok2)
    return float((rH ** 2).mean() / (rC ** 2).mean())


def lt_cells(npz, tag):
    z, meta, chroms = FM.load(npz)
    auto = auto_of(chroms)
    out = {}
    for set_name, cs, filt, W in (("auto", auto, "F0", 100), ("auto", auto, "F0", 1000), ("auto", auto, "F1", 100),
                                  ("auto", auto, "F2", 100), ("chrX", ["chrX"], "F0", 100), ("chrX", ["chrX"], "F1", 10),
                                  ("chrX", ["chrX"], "F1", 100), ("chrX", ["chrX"], "F1", 1000), ("chrX", ["chrX"], "F2", 100)):
        w, cid, ok, per = MM.build(z, cs, filt, W)
        idx = np.where(ok)[0]
        rH, rC = MM.resid(w, "H", ok), MM.resid(w, "C", ok)
        h2, c2 = rH ** 2, rC ** 2
        mx = np.maximum(h2, c2)
        k1 = max(1, int(round(0.01 * len(idx))))
        cell = {"k": int(len(idx)), "R": float(h2.mean() / c2.mean()), "phi_res_H": float(h2.mean()),
                "phi_res_C": float(c2.mean()),
                "R_drop_topH": r_after(w, ok, idx[np.argmax(h2)]), "R_drop_topC": r_after(w, ok, idx[np.argmax(c2)]),
                "R_drop_top1pct": r_after(w, ok, idx[np.argsort(-mx)[:k1]]),
                "topH_share_sumH2": float(h2.max() / h2.sum()), "topC_share_sumC2": float(c2.max() / c2.sum()),
                "topH_start_Mb": round(float(w["t0"][idx[np.argmax(h2)]] * FM.BIN / 1e6), 2),
                "topC_start_Mb": round(float(w["t0"][idx[np.argmax(c2)]] * FM.BIN / 1e6), 2),
                "topH_chrom": cs[cid[idx[np.argmax(h2)]]], "topC_chrom": cs[cid[idx[np.argmax(c2)]]]}
        if set_name == "chrX" and filt == "F1" and W == 100:
            o = np.argsort(-rH)[:20]
            cell["top20"] = [{"start_Mb": round(float(w["t0"][idx[q]] * FM.BIN / 1e6), 1), "r_H": round(float(rH[q]), 1),
                              "r_C": round(float(rC[q]), 1),
                              "rep_share": round(float(w["rep_m"][idx[q]] / max(w["m"][idx[q]], 1)), 2)} for q in o]
        key = f"{set_name}|{filt}|{W}kb"
        out[key] = cell
        print("T2", tag, key, json.dumps({k: v for k, v in cell.items() if k != "top20"}), flush=True)
        if "top20" in cell:
            print("T2 top20", tag, json.dumps(cell["top20"]), flush=True)
    return out


def read_bed(path):
    iv = []
    with open(path) as fh:
        for line in fh:
            if line.startswith(("#", "track", "browser")) or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 3:
                continue
            try:
                iv.append((p[0], int(p[1]), int(p[2]), p[3] if len(p) > 3 else ""))
            except ValueError:
                continue
    return iv


def lt(npz_h, npz_c, annot_prefix, outjson):
    res = {"hs1": lt_cells(npz_h, "hs1"), "chimp": lt_cells(npz_c, "chimp")}
    # T4
    files = sorted(glob.glob(annot_prefix + "*/*.bed"))
    res["T4"] = {"files": [pathlib.Path(f).name for f in files], "windows": []}
    beds = {pathlib.Path(f).name: read_bed(f) for f in files}
    for wd in res["hs1"]["chrX|F1|100kb"]["top20"]:
        s = int(round(wd["start_Mb"] * 1e6))
        e = s + 100_000
        row = {"start_Mb": wd["start_Mb"], "r_H": wd["r_H"], "overlaps": {}}
        for fn, iv in beds.items():
            ov = {}
            near = None
            for ch, a, b, nm in iv:
                if ch != "chrX":
                    continue
                o = min(b, e) - max(a, s)
                if o > 0:
                    ov[nm] = ov.get(nm, 0) + o
                elif "censat" in fn:
                    d = a - e if a >= e else s - b
                    if d <= 2_000_000 and (near is None or d < near[1]):
                        near = (nm, d, a, b)
            row["overlaps"][fn] = ov
            if "censat" in fn:
                row["nearest_censat_within_2Mb"] = near
        res["T4"]["windows"].append(row)
    for row in res["T4"]["windows"][:5]:
        print("T4", json.dumps(row), flush=True)
    # T5
    z, meta, chroms = FM.load(npz_c)
    auto = auto_of(chroms)
    w, cid, ok, per = MM.build(z, auto, "F2", 100, gb=True)
    t5 = {}
    for L in ("H", "C"):
        pm = w[L][ok].sum() / w["m"][ok].sum()
        runs = FM.mesas(w[L].astype(float), w["m"].astype(float), cid, ok, pm)
        inm = np.zeros(len(ok), bool)
        for i, j in runs:
            inm[i:j + 1] = True
        t5[L] = {"mesas": len(runs), "WS_in": int(w[L + "_WS"][inm].sum()), "SW_in": int(w[L + "_SW"][inm].sum()),
                 "WS_all": int(w[L + "_WS"][ok].sum()), "SW_all": int(w[L + "_SW"][ok].sum())}
    res["T5"] = t5
    print("T5", json.dumps(t5), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)


# ------------------------------------------------------------------------------------------------ T3
def stream_blocks(maf):
    pr = subprocess.Popen(["zcat", maf], stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    block = []
    for line in pr.stdout:
        c = line[:1]
        if c == "s":
            p = line.split(None, 6)
            block.append((p[1], int(p[2]), int(p[3]), p[4], int(p[5])))
        elif c == "a":
            if block:
                yield block
            block = []
    if block:
        yield block
    pr.wait()


def fwd(start, size, strand, srcsize):
    return (start, start + size) if strand == "+" else (srcsize - start - size, srcsize - start)


def tally(block, tgt_prefix, tgt_iv, other_prefix, names, acc):
    ri = next((i for i, r in enumerate(block) if r[0].startswith(tgt_prefix)), None)
    if ri is None:
        return
    ref = block[ri]
    a, b = fwd(ref[1], ref[2], ref[3], ref[4])
    for k, (s, e) in enumerate(tgt_iv):
        if b <= s or a >= e:
            continue
        for i, (src, st, sz, strand, ss) in enumerate(block):
            if i == ri or not src.startswith(other_prefix):
                continue
            ch = names(src[len(other_prefix):])
            x, y = fwd(st, sz, strand, ss)
            d = acc[k]
            d["by_chrom"][ch] = d["by_chrom"].get(ch, 0) + sz
            key = f"{ch}:{(x // 100_000) / 10:.1f}"
            d["by_100kb"][key] = d["by_100kb"].get(key, 0) + sz


def finish(acc):
    for d in acc:
        d["by_100kb"] = dict(sorted(d["by_100kb"].items(), key=lambda kv: -kv[1])[:10])
    return acc


def mapc(npz_c, maf, outjson):
    z, meta, chroms = FM.load(npz_c)
    w, cid, ok, per = MM.build(z, ["chrX"], "F1", 100)
    idx = np.where(ok)[0]
    rH = MM.resid(w, "H", ok)
    top = [int(w["t0"][idx[q]]) * FM.BIN for q in np.argsort(-rH)[:5]]
    iv = [(s, s + 100_000) for s in top]
    acc = [{"chimp_chrX_start_Mb": s / 1e6, "r_H": float(rH[q]), "by_chrom": {}, "by_100kb": {}}
           for s, q in zip(top, np.argsort(-rH)[:5])]
    acc_name = [k for k, v in MM.PANTRO.items() if v == "chrX"][0]
    t = time.time()
    for n, blk in enumerate(stream_blocks(maf)):
        tally(blk, "GCA_028858775.2." + acc_name, iv, "hs1.", lambda x: x, acc)
        if n % 1_000_000 == 0:
            print(f"[{time.time() - t:.0f}s] {n}", flush=True)
    res = finish(acc)
    print("T3c", json.dumps(res), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)


def maph(maf, outjson):
    iv = [(57_300_000, 57_400_000)]
    acc = [{"hs1_chrX_start_Mb": 57.3, "by_chrom": {}, "by_100kb": {}}]
    t = time.time()
    for n, blk in enumerate(stream_blocks(maf)):
        tally(blk, "hs1.chrX", iv, "GCA_028858775.2.", lambda x: MM.PANTRO.get(x, x), acc)
        if n % 1_000_000 == 0:
            print(f"[{time.time() - t:.0f}s] {n}", flush=True)
    res = finish(acc)
    print("T3h", json.dumps(res), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "calib":
        calib(sys.argv[2], sys.argv[3])
    elif c == "lt":
        lt(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif c == "mapc":
        mapc(sys.argv[2], sys.argv[3], sys.argv[4])
    elif c == "maph":
        maph(sys.argv[2], sys.argv[3])
