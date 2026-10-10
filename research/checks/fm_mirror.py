"""FM-mirror: post hoc (after reviews 1796620) follow-ups to R4-FM, pre-registered before any of them is run.

Tier: part of the load-bearing FM check (ROOT-FM).  Post hoc relative to R4-FM (fm_mesa_replication.py, d723064):
these tests were asked for by the three FM reviews; this docstring and the code are committed BEFORE the run.
Only the first 30 lines of the chimp-referenced MAF were viewed (format and sequence names).  Nothing else of
the new inputs has been read.  Runs on na-workhorse only.  The FM code is imported unchanged (by file path).

WHY.  REVIEW-R4-FM-correctness C1 / steelman-critic K2: the only Day-favourable autosomal cells (F0: phi_res H/C
16.2/8.2 at 100 kb, 34.3/18.8 at 1 Mb) and chrX F1 (18.16/4.84 = 3.76 at 100 kb, correctness C2) sit where a
human-referenced projection (hal2maf --refGenome hs1) is expected to inflate the REFERENCE lineage: a
human-specific duplication puts two hs1 reference positions against one ape copy, so paralog-vs-ortholog
differences at the second copy can be counted as H without a second row being listed.  The mirror test
re-runs the frozen FM pipeline on the SAME Cactus alignment projected onto CHIMPANZEE (GCA_028858775.2).
If the human-heavy excess is a reference-projection artefact, it moves to the chimp lineage; if it is real
human-lineage sequence change, it stays on H.  Steelman-day D3: the "sharp boundaries" of FM4 and the chance
rate of lineage-specific mesas were not tested; they are tested here.  Cheap minors from the reviews are
added (C3 null calibration, C11 bin-count assertion, K3 beta-fitted null and gBGC, K4 Lorenz bound).

DATA (untrusted, read only, never executed; each in its own new directory on workhorse)
  sources/raw/fm-mirror-2026-10-10/pantro.maf.gz = 8-t2t-apes-2023v2.GCA_028858775.2.maf.gz (cgl.gi.ucsc.edu
    /data/cactus/t2t-apes/8-t2t-apes-2023v2/; 3,598,180,725 bytes; md5 checked against the published .md5
    before extraction).  Same 8-way Progressive Cactus alignment as R4-FM, chimp-referenced.
  sources/raw/fm-pantro-report-2026-10-10/report.txt = NCBI assembly report GCA_028858775.2_NHGRI_mPanTro3-v2.0_pri
    (sha256 f8ead51d2385990b52ed2204df59e5c2538bbcea38053942c02286ecf67dffd1): accession -> chromosome (PANTRO).
  sources/raw/fm-sd-2026-10-10/chm13v2.0_SD.bed (human-pangenomics T2T/CHM13/assemblies/annotation; the CHM13
    segmental-duplication annotation; first three columns used, intervals merged).
  results/raw/fm_bins.npz (R4-FM extract on hs1; workhorse only).

STAGE A  mirror: `extract <pantro.maf.gz> <fm_mirror_bins.npz>` then `mirror <npz> <fm_mirror_analyse.json>`.
  Extraction identical to FM.extract except: reference = the first chimp row of each block (chimp coordinates,
  1 kb bins); repeat class = chimp soft-mask; dup = > 1 row for any of the six core genomes (now counting the
  chimp reference rows); chimp accessions renamed chr1..chr23 (chimp numbering: chr12/chr13 = HSA2A/2B) and chrX
  from the assembly report.  Classification (H, C, B, G, DHC, ...) is FM.classify, unchanged, so lineage
  definitions are identical; only the projection differs.  Extra fields (gBGC, chimp-ref only): W->S and S->W
  substitutions on H and C (ancestral = g = o state).  Analysis = FM.analyse unchanged (same grid, nulls, seed).
  The chimp autosome set (23) differs from the human (22) only by the 2A/2B split.

  PREDICTIONS (chimp-referenced; ratio R = phi_res(H) / phi_res(C); hs1-referenced values in brackets)
   M1 autosomes F0, 100 kb and 1 Mb [hs1: R = 1.97, 1.82].
      Projection artefact (critics; correctness C1): the excess follows the reference: R <= 0.67 (C heavier)
        in both cells, i.e. C/H about 2.
      Real human-lineage change (Day; steelman-day D7): H stays heavier: R >= 1.5 in both cells.
      Between (0.67, 1.5), or the two cells disagree: indeterminate (part artefact, part real).
      Secondary (not scored): CV^2 ratio = ((phi_H - 1) / p_H) / ((phi_C - 1) / p_C) moves the same way.
   M2 autosomes F1, 100 kb [hs1: 4.48 / 4.08, R = 1.10].  Both sides: R in [0.67, 1.5] (symmetric).
   M3 chrX F1, 100 kb [hs1: 18.16 / 4.84 = 3.76] and 10 kb [7.33 / 2.97].
      Artefact (critics): R <= 1.5 at 100 kb (excess vanishes or flips).  Day: R > 3 at 100 kb persists.
   M4 lag-1 reversal, autosomes F0 100 kb [hs1: H 0.47 < C 0.59].  Artefact: C lag-1 < H lag-1 on chimp-ref
      (isolated high windows move to the reference lineage).  Day: H < C persists.
   M5 the registered discriminating cells re-run on chimp-ref (F2 100 kb unless stated):
      P3 phi_res(H) <= 0.3 phi(H) and R in [0.5, 2] (critics) vs R > 3 (Day);  P4 phi_HC in [1, 5] (critics)
      vs > 10 (Day);  P5 M-null/obs for H >= 0.5 (critics) vs < 0.2 (Day);  P7 DHC share in H mesas < 20%
      (critics) vs > 50% (Day).  Expectation (audit): the critic side holds again (single-copy sequence is
      projection-invariant up to coordinate differences).
   M6 gBGC (critic K3, descriptive; chimp-ref, F2 100 kb mesas vs genome): (W->S)/(S->W) ratio inside H mesas
      vs genome-wide H.  Critics: higher inside mesas (regional gBGC contributes, neutral); Day: no prediction
      stated (recorded as a description).  Same for C mesas.

STAGE B  extra: `extra <fm_bins.npz (hs1)> <chm13v2.0_SD.bed> <fm_extra.json>`
   S1 SD overlap (C1 cheaper step).  F0 autosomes, 100 kb and 1 Mb.  r_L = standardised het-mu residual (FM S3);
      d = r_H - r_C.  Report: mean SD coverage of the top 1% windows by d vs all used windows; the share of
      Delta = sum(r_H^2 - r_C^2) carried by windows with SD coverage >= 10% and >= 50%; R recomputed on windows
      with SD coverage < 10%.  Critics: >= 50% of Delta in SD >= 10% windows and R in [0.67, 1.5] without them.
      Day: < 50% of Delta in SD windows (the excess is not a duplication effect).  NOTE: SD localisation alone
      does not discriminate artefact from real human-specific SD evolution (steelman-day D7); M1 does.
      The SD file does not mark human-specific SDs; no human-specific SD list is used.
   S2 chrX (C2).  F1, 100 kb: the top 20 windows by r_H (start Mb, r_H, r_C, SD coverage, repeat share of core
      columns); R on chrX F1 windows with SD coverage < 10%.  Critics: the chrX F1 excess sits in SD-rich
      windows and R <= 1.5 without them.  Day: R > 3 without them.
   E1 edge sharpness (steelman-day D3 i).  Mesas from the FM rule (F0 and F2, 10 kb and 100 kb; H and C).  At each
      mesa edge (both ends; skipped if within 5 kb of a chromosome end or < 2,500 core columns on either side):
      Delta_rel = (d_in - d_out) / p_L with d_in, d_out the density in the 5 kb just inside / outside;
      S = Delta_rel / ((d_mesa - p_L) / p_L) (1 = a perfect step to the mean at the edge; 0 = no step).
      Comparator 1: the same S for H mesas called on a 1 kb-resolution shared-rate null (rho from C+G in a 5 kb
      running window, 5 replicates).  Comparator 2: C mesas.  Comparator 3 (shared edges): median Delta_rel of C
      at H-mesa edges / median Delta_rel of H at H-mesa edges.  Also a density profile (-20..+20 kb) per set.
      Day (discrete, human-lineage blocks): S_H / S_C >= 1.5 AND shared fraction < 0.2.
      Critics (shared rate landscape): S_H / S_C in [0.67, 1.5] AND shared fraction >= 0.4.
      Otherwise mixed.  Scored per cell; the headline is F2 100 kb and F0 10 kb.
      S_H / S_null is DESCRIPTIVE ONLY, not scored: a pre-run smoke test on a synthetic genome with a shared
      step-wise rate (no lineage-specific edges) gave S_H / S_null = 1.37-1.44, i.e. the 1 kb null's noisy rho
      blurs its own edges, so this comparator is biased toward "sharper than null" (toward Day).
   E2 lineage-specific mesas by chance (steelman-day D3 ii).  Paired M null: H* ~ Poisson(E_H), C* ~ Poisson(E_C)
      independently (FM S3 expectations), 20 replicates per cell (F0/F2 x 10/100 kb); count H*-specific vs C*
      and C*-specific vs H* with the FM rule.  Observed (already known from R4-FM): 35/70, 1/8, 2/2, 0/0.
      Day: observed H-specific > 95th percentile of the null in >= 2 of 4 cells.  Critics: observed H-specific
      <= null 95th percentile in >= 3 of 4 cells.  Caveat fixed now: C3 says this null is noise-inflated at
      10 kb (more null mesas, so more chance specific mesas): 10 kb cells lean critic; 100 kb cells are cleaner.
   C3 null calibration (correctness C3).  Synthetic genome: rho_true = observed all-lineage relative density
      smoothed over +-5 windows (per chromosome); n_L ~ Poisson(m p_L rho_true) for H, C, B, G; run FM's het-mu
      null procedure on the synthetic data; report M-null mesas / synthetic mesas (5 reps).  A calibrated
      procedure gives ~1.  Audit expectation: > 1 at 10 kb (1.3-2.5), ~1 (0.8-1.3) at 100 kb.
   K3 beta-fitted null (critic K3 i).  E = m p_L rho^beta rescaled to sum n_L, beta in {0.5, 0.75, ..., 2};
      report the minimising beta and phi_res for H, C, G (F0, F1, F2; 100 kb).  Critics: phi_res(H) falls
      below the beta = 1 value and R stays in [0.67, 1.5] (F1, F2).  Day: no prediction.
   K4 Lorenz bound for FM8b (critic K4).  DHC share held by the densest x% of core columns (windows ranked by DHC
      density), F0 and F1, W = 10 kb, 100 kb, 1 Mb; x at which the share reaches 50%.  Critics: x >= 30% in
      every cell (no mesa rule can make mesas hold most of the divergence).  Day: x < 10% in some cell.
   C11 assertion: max over 1 kb bins of core columns summed over classes (<= 1000 expected; > 1000 means
      repeated reference positions), per chromosome, hs1 npz (and chimp npz at extraction).

SCORING.  Each prediction is scored hit / miss / indeterminate against the raw JSON and reported in R4-FM
"Mirror test" with the hs1 values beside it.  None of these tests changes a P1-P9 score; they decide the
F0/chrX "Day-side" reading (M1, M3, S1, S2), FM4's "sharp boundaries" (E1) and FM7's lineage-specific mesas (E2).
"""
import gzip
import importlib.util
import json
import pathlib
import sys
import time

import numpy as np

_spec = importlib.util.spec_from_file_location("fm", pathlib.Path(__file__).resolve().parent / "fm_mesa_replication.py")
FM = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(FM)

REF = 2  # chimp index in FM.SP
PANTRO = {"CM054434.2": "chr1", "CM068905.1": "chr2", "CM054437.2": "chr3", "CM054438.2": "chr4",
          "CM054439.2": "chr5", "CM054440.2": "chr6", "CM054441.2": "chr7", "CM054442.2": "chr8",
          "CM054443.2": "chr9", "CM054444.2": "chr10", "CM054445.2": "chr11", "CM054446.2": "chr12",
          "CM054447.2": "chr13", "CM054448.2": "chr14", "CM054449.2": "chr15", "CM054450.2": "chr16",
          "CM054451.2": "chr17", "CM054452.2": "chr18", "CM054453.2": "chr19", "CM054454.2": "chr20",
          "CM054455.2": "chr21", "CM054456.2": "chr22", "CM068906.1": "chr23", "CM054457.2": "chrX",
          "CM054458.2": "chrY"}
GB = ("H_WS", "H_SW", "C_WS", "C_SW")
W_ = np.zeros(256, bool)
for _ch in b"ATat":
    W_[_ch] = True
S_ = np.zeros(256, bool)
for _ch in b"CGcg":
    S_[_ch] = True


# ------------------------------------------------------------------------------------------------ stage A
def extract(maf, out):
    t0 = time.time()
    data, gbd, sizes = {}, {}, {}
    nblk = 0
    refname = [g for g, i in FM.SP.items() if i == REF][0]

    def flush(block):
        ref = None
        rows, counts = {}, {}
        for src, start, size, strand, srcsize, seq in block:
            gname = "hs1" if src.startswith("hs1.") else next((g for g in FM.SP if src.startswith(g + ".")), None)
            if gname is None:
                continue
            i = FM.SP[gname]
            if i == REF and ref is None:
                ref = (src[len(gname) + 1:], start, srcsize, strand, seq)
                continue
            counts[i] = counts.get(i, 0) + 1
            if i not in rows:
                rows[i] = seq
        if ref is None:
            return
        acc, start, srcsize, strand, rseq = ref
        assert strand == "+", "chimp reference row on minus strand"
        chrom = PANTRO.get(acc, acc)
        counts[REF] = counts.get(REF, 0) + 1
        dup = any(counts.get(i, 0) > 1 for i in FM.CORE)
        r = np.frombuffer(rseq.encode(), np.uint8)
        keep = r != ord("-")
        n = int(keep.sum())
        if n == 0:
            return
        arr = {REF: r[keep]}
        for i in range(8):
            if i == REF:
                continue
            arr[i] = np.frombuffer(rows[i].encode(), np.uint8)[keep] if i in rows else np.full(n, ord("-"), np.uint8)
        f = FM.classify(arr, keep)
        g, h, c = arr[4], arr[0], arr[2]
        f["H_WS"] = f["H"] & W_[g] & S_[h]
        f["H_SW"] = f["H"] & S_[g] & W_[h]
        f["C_WS"] = f["C"] & W_[g] & S_[c]
        f["C_SW"] = f["C"] & S_[g] & W_[c]
        rep = arr[REF] >= ord("a")
        cpg = FM.cpg_mask([arr[0] & 0xDF, arr[2] & 0xDF, arr[4] & 0xDF])
        cls = rep.astype(np.int64) + 2 * cpg.astype(np.int64) + 4 * int(dup)
        if chrom not in data:
            nb = srcsize // FM.BIN + 1
            data[chrom] = np.zeros((nb, 8, FM.NF), np.uint32)
            gbd[chrom] = np.zeros((nb, 8, len(GB)), np.uint32)
            sizes[chrom] = srcsize
        pos = start + np.arange(n)
        bins = pos // FM.BIN
        b0, b1 = int(bins[0]), int(bins[-1])
        idx = (bins - b0) * 8 + cls
        nn = (b1 - b0 + 1) * 8
        for D, names in ((data[chrom], FM.FIELDS), (gbd[chrom], GB)):
            for j, name in enumerate(names):
                sel = f[name]
                if sel.any():
                    D[b0:b1 + 1, :, j] += np.bincount(idx[sel], minlength=nn).reshape(b1 - b0 + 1, 8).astype(np.uint32)

    block = []
    with gzip.open(maf, "rt") as fh:
        for line in fh:
            if line.startswith("s"):
                p = line.split()
                block.append((p[1], int(p[2]), int(p[3]), p[4], int(p[5]), p[6]))
            elif line.startswith("a"):
                if block:
                    flush(block)
                    nblk += 1
                    if nblk % 1000000 == 0:
                        print(f"[{time.time() - t0:7.0f}s] blocks {nblk}", flush=True)
                block = []
        if block:
            flush(block)
            nblk += 1
    mx = {k: int(v[:, :, 0].sum(axis=1).max()) for k, v in data.items()}
    big = max(int(v.max()) for v in data.values())
    dt = np.uint16 if big <= 65535 else np.uint32
    np.savez_compressed(out, **{f"chr_{k}": v.astype(dt) for k, v in data.items()},
                        **{f"gb_{k}": v.astype(dt) for k, v in gbd.items()},
                        meta=json.dumps(dict(fields=FM.FIELDS, gb=GB, bin=FM.BIN, sizes=sizes, blocks=nblk, ref=refname,
                                             classes="rep(chimp) + 2*cpg + 4*dup", max_m_per_bin=mx, max_count=big)))
    print(f"C11 chimp-ref: max core columns per 1 kb bin {max(mx.values())} (bins > 1000: "
          f"{sum(int((v[:, :, 0].sum(axis=1) > 1000).sum()) for v in data.values())}); max field count {big}", flush=True)
    print(f"extract done: {nblk} blocks, {len(data)} sequences, {time.time() - t0:.0f} s", flush=True)


def mirror(npz, outjson):
    FM.analyse(npz, outjson)
    # M6 gBGC on F2 100 kb mesas (chimp-ref)
    z, meta, chroms = FM.load(npz)
    auto = [c for c in chroms if c.replace("chr", "").isdigit()]
    w, cid, ok, per = build(z, auto, "F2", 100, gb=True)
    res = {}
    for L in ("H", "C"):
        pm = w[L][ok].sum() / w["m"][ok].sum()
        runs = FM.mesas(w[L].astype(float), w["m"].astype(float), cid, ok, pm)
        inm = np.zeros(len(ok), bool)
        for i, j in runs:
            inm[i:j + 1] = True
        ws, sw = w[L + "_WS"], w[L + "_SW"]
        res[L] = {"mesas": len(runs), "WS_SW_in_mesas": float(ws[inm].sum() / max(sw[inm].sum(), 1)),
                  "WS_SW_genome": float(ws[ok].sum() / max(sw[ok].sum(), 1))}
    print("M6 gBGC", json.dumps(res), flush=True)
    d = json.load(open(outjson))
    d["gbgc_F2_100kb"] = res
    json.dump(d, open(outjson, "w"), indent=1)


# ------------------------------------------------------------------------------------------------ helpers
BASEF = ("m", "H", "C", "B", "G", "DHC")


def build(z, chroms, filt, W, gb=False, cls_fields=False):
    """Windows as in FM.windows plus the 1 kb arrays per chromosome (per[ci]) and window start bins (w['t0'])."""
    cl = list(FM.FILTERS[filt])
    names = BASEF + (GB if gb else ())
    w = {f: [] for f in names + ("t0", "rep_m")}
    cid, ok, per = [], [], []
    for ci, ch in enumerate(chroms):
        a = z["chr_" + ch].astype(np.int64)
        b = {f: a[:, cl, FM.FIELDS.index(f)].sum(axis=1) for f in BASEF}
        b["rep_m"] = a[:, [k for k in cl if k & 1], 0].sum(axis=1)
        if gb:
            g = z["gb_" + ch].astype(np.int64)
            for j, f in enumerate(GB):
                b[f] = g[:, cl, j].sum(axis=1)
        per.append(b)
        nb = a.shape[0] // W
        if nb == 0:
            continue
        for f in names + ("rep_m",):
            w[f].append(b[f][: nb * W].reshape(nb, W).sum(axis=1))
        w["t0"].append(np.arange(nb) * W)
        cid.append(np.full(nb, ci))
        ok.append(w["m"][-1] >= 0.5 * W * FM.BIN)
    w = {f: np.concatenate(v) for f, v in w.items()}
    return w, np.concatenate(cid), np.concatenate(ok), per


def resid(w, L, ok):
    E, No = FM.het_expect(w, L, ok)
    return (w[L][ok] - E) / np.sqrt(E * (1 + E / np.maximum(No, 1)) + 1e-9)


def sd_cov(bed, chroms, sizes):
    iv = {}
    with open(bed) as fh:
        for line in fh:
            if line.startswith(("#", "track", "browser")):
                continue
            p = line.split("\t")
            if len(p) < 3:
                continue
            try:
                iv.setdefault(p[0], []).append((int(p[1]), int(p[2])))
            except ValueError:
                continue
    cov = {}
    for ch in chroms:
        n = sizes[ch] // FM.BIN + 1
        diff = np.zeros(sizes[ch] + 2, np.int32)
        for s, e in iv.get(ch, []):
            diff[max(s, 0)] += 1
            diff[min(e, sizes[ch])] -= 1
        covered = (np.cumsum(diff)[: sizes[ch]] > 0)
        pad = np.zeros(n * FM.BIN, bool)
        pad[: sizes[ch]] = covered
        cov[ch] = pad.reshape(n, FM.BIN).sum(axis=1)
    return cov, {k: len(v) for k, v in iv.items()}


def agg(arrs, W):
    """1 kb arrays per chromosome -> concatenated window sums, in the same order as build()."""
    out = []
    for a in arrs:
        nb = len(a) // W
        if nb:
            out.append(a[: nb * W].reshape(nb, W).sum(axis=1))
    return np.concatenate(out)


def edge_stats(runs, per, nkey, cid, t0, W, pm, nfun=None):
    """Edge sharpness for runs (window index pairs).  nfun(ci) returns the 1 kb count array to use."""
    S, dr, prof_n, prof_m = [], [], np.zeros(40), np.zeros(40)
    for i, j in runs:
        ci = cid[i]
        n1 = nfun(ci) if nfun else per[ci][nkey]
        m1 = per[ci]["m"]
        s, e = t0[i], t0[j] + W
        dm = n1[s:e].sum() / max(m1[s:e].sum(), 1)
        if dm <= pm:
            continue
        for side in (0, 1):
            if side == 0:
                inn, out = slice(s, s + 5), slice(s - 5, s)
                lo, hi = s - 20, s + 20
            else:
                inn, out = slice(e - 5, e), slice(e, e + 5)
                lo, hi = e - 20, e + 20
            if lo < 0 or hi > len(m1) or m1[inn].sum() < 2500 or m1[out].sum() < 2500:
                continue
            di = n1[inn].sum() / m1[inn].sum()
            do = n1[out].sum() / m1[out].sum()
            dr.append((di - do) / pm)
            S.append((di - do) / (dm - pm))
            pn, pmm = n1[lo:hi].astype(float), m1[lo:hi].astype(float)
            if side == 1:
                pn, pmm = pn[::-1], pmm[::-1]
            prof_n += pn
            prof_m += pmm
    prof = (prof_n / np.maximum(prof_m, 1) / pm).round(3).tolist()
    q = lambda a: [float(x) for x in np.percentile(a, [25, 50, 75])] if len(a) else [float("nan")] * 3
    return {"edges": len(S), "S_q": q(S), "dr_q": q(dr), "profile_outside_to_inside": prof}


def null_1kb(per, L, others, p, rng):
    """1 kb shared-rate null: rho from the other lineages in a 5 kb running window."""
    k = np.ones(5)
    out = []
    so = sum(p[o] for o in others)
    for b in per:
        No = np.convolve(sum(b[o] for o in others).astype(float), k, "same")
        m5 = np.convolve(b["m"].astype(float), k, "same")
        E = b["m"] * p[L] * (No + 1.0) / (m5 * so + 1.0)
        out.append(rng.poisson(E).astype(float))
    return out


def specific(runsA, nB, m, pB):
    return int(sum(nB[i:j + 1].sum() / max(m[i:j + 1].sum(), 1) < 1.1 * pB for i, j in runsA))


# ------------------------------------------------------------------------------------------------ stage B
def extra(npz, bed, outjson):
    z, meta, chroms_all = FM.load(npz)
    sizes = meta["sizes"]
    auto = [c for c in chroms_all if c.replace("chr", "").isdigit()]
    rng = np.random.default_rng(FM.SEED + 1)
    res = {}
    # C11
    mx = {}
    for ch in chroms_all:
        s = z["chr_" + ch][:, :, 0].astype(np.int64).sum(axis=1)
        mx[ch] = (int(s.max()), int((s > 1000).sum()))
    res["C11"] = {"max_m_per_bin": max(v[0] for v in mx.values()), "bins_gt_1000": sum(v[1] for v in mx.values()),
                  "per_chrom": mx}
    print("C11", json.dumps(res["C11"]["max_m_per_bin"]), res["C11"]["bins_gt_1000"], flush=True)
    # SD coverage per 1 kb bin
    cov, nint = sd_cov(bed, [c for c in chroms_all if c in sizes], sizes)
    res["sd_intervals_per_chrom"] = nint
    print("SD intervals", sum(nint.values()), "chroms", len(nint), flush=True)

    # S1 / S2
    res["S1"], res["S2"] = {}, {}
    for set_name, chroms, filt, Ws in (("auto", auto, "F0", (100, 1000)), ("auto", auto, "F1", (100,)),
                                       ("chrX", ["chrX"], "F1", (100, 10)), ("chrX", ["chrX"], "F0", (100,))):
        for W in Ws:
            w, cid, ok, per = build(z, chroms, filt, W)
            sdw = np.array([cov[chroms[cid[k]]][w["t0"][k]: w["t0"][k] + W].sum() for k in range(len(cid))]) / (W * FM.BIN)
            rH, rC = resid(w, "H", ok), resid(w, "C", ok)
            sd = sdw[ok]
            d = rH - rC
            top = d >= np.percentile(d, 99)
            delta = rH ** 2 - rC ** 2
            cell = {"k": int(ok.sum()), "R_all": float((rH ** 2).mean() / (rC ** 2).mean()),
                    "phi_res_H": float((rH ** 2).mean()), "phi_res_C": float((rC ** 2).mean()),
                    "sd_mean_all": float(sd.mean()), "sd_mean_top1pct": float(sd[top].mean()),
                    "frac_windows_sd10": float((sd >= 0.1).mean()),
                    "delta_total": float(delta.sum()),
                    "delta_share_sd10": float(delta[sd >= 0.1].sum() / delta.sum()),
                    "delta_share_sd50": float(delta[sd >= 0.5].sum() / delta.sum())}
            ok2 = ok.copy()
            ok2[ok] = sd < 0.1
            rH2, rC2 = resid(w, "H", ok2), resid(w, "C", ok2)
            cell.update({"k_sd_lt10": int(ok2.sum()), "phi_res_H_sd_lt10": float((rH2 ** 2).mean()),
                         "phi_res_C_sd_lt10": float((rC2 ** 2).mean()),
                         "R_sd_lt10": float((rH2 ** 2).mean() / (rC2 ** 2).mean())})
            if set_name == "chrX" and filt == "F1" and W == 100:
                idx = np.where(ok)[0]
                o = np.argsort(-rH)[:20]
                cell["top20"] = [{"start_Mb": round(float(w["t0"][idx[q]] * FM.BIN / 1e6), 1), "r_H": round(float(rH[q]), 1),
                                  "r_C": round(float(rC[q]), 1), "sd": round(float(sd[q]), 2),
                                  "rep_share": round(float(w["rep_m"][idx[q]] / max(w["m"][idx[q]], 1)), 2)} for q in o]
            res["S1" if set_name == "auto" else "S2"][f"{filt}|{W}kb"] = cell
            print("S", set_name, filt, W, json.dumps({k: v for k, v in cell.items() if k != "top20"}), flush=True)
            if "top20" in cell:
                print("S2 top20", json.dumps(cell["top20"]), flush=True)

    # E1, E2, C3 (autosomes; F0/F2 x 10/100 kb)
    res["E1"], res["E2"], res["C3"] = {}, {}, {}
    for filt in ("F0", "F2"):
        for W in (10, 100):
            key = f"{filt}|{W}kb"
            w, cid, ok, per = build(z, auto, filt, W)
            m_ = w["m"].astype(float)
            t0 = w["t0"]
            p = {L: w[L][ok].sum() / w["m"][ok].sum() for L in ("H", "C", "B", "G")}
            runs = {L: FM.mesas(w[L].astype(float), m_, cid, ok, p[L]) for L in ("H", "C")}
            e = {"H_obs": edge_stats(runs["H"], per, "H", cid, t0, W, p["H"]),
                 "C_obs": edge_stats(runs["C"], per, "C", cid, t0, W, p["C"]),
                 "C_at_H_edges": edge_stats(runs["H"], per, "C", cid, t0, W, p["C"])}
            nullS, nulldr, nulln = [], [], []
            for rep in range(5):
                nb = null_1kb(per, "H", ("C", "G"), p, rng)
                nw = agg(nb, W)
                rr = FM.mesas(nw, m_, cid, ok, p["H"])
                st = edge_stats(rr, per, "H", cid, t0, W, p["H"], nfun=lambda ci, nb=nb: nb[ci])
                nullS.append(st["S_q"][1]); nulldr.append(st["dr_q"][1]); nulln.append(len(rr))
                if rep == 0:
                    e["H_null_rep0"] = st
            e["H_null_median_S"] = nullS
            e["H_null_median_dr"] = nulldr
            e["H_null_mesas"] = nulln
            sH, sC, sN = e["H_obs"]["S_q"][1], e["C_obs"]["S_q"][1], float(np.median(nullS))
            shared = e["C_at_H_edges"]["dr_q"][1] / e["H_obs"]["dr_q"][1] if e["H_obs"]["dr_q"][1] else float("nan")
            e["summary"] = {"S_H": sH, "S_C": sC, "S_null": sN, "S_H/S_null": sH / sN if sN else float("nan"),
                            "S_H/S_C": sH / sC if sC else float("nan"), "shared_fraction": shared}
            res["E1"][key] = e
            print("E1", key, json.dumps(e["summary"]), "edges", e["H_obs"]["edges"], e["C_obs"]["edges"], flush=True)
            # E2
            EH, _ = FM.het_expect(w, "H", ok)
            EC, _ = FM.het_expect(w, "C", ok)
            EHf, ECf = np.zeros(len(m_)), np.zeros(len(m_))
            EHf[ok], ECf[ok] = EH, EC
            hs, cs = [], []
            for rep in range(20):
                h = rng.poisson(EHf).astype(float)
                c = rng.poisson(ECf).astype(float)
                rh = FM.mesas(h, m_, cid, ok, p["H"])
                rc = FM.mesas(c, m_, cid, ok, p["C"])
                hs.append(specific(rh, c, m_, p["C"]))
                cs.append(specific(rc, h, m_, p["H"]))
            obsH = specific(runs["H"], w["C"].astype(float), m_, p["C"])
            obsC = specific(runs["C"], w["H"].astype(float), m_, p["H"])
            res["E2"][key] = {"obs_H_spec": obsH, "obs_C_spec": obsC, "null_H_spec": hs, "null_C_spec": cs,
                              "null_H_p95": float(np.percentile(hs, 95)), "null_C_p95": float(np.percentile(cs, 95)),
                              "obs_H_gt_p95": bool(obsH > np.percentile(hs, 95))}
            print("E2", key, json.dumps({k: v for k, v in res["E2"][key].items()}), flush=True)
            # C3 calibration
            tot = sum(w[L] for L in ("H", "C", "B", "G")).astype(float)
            ps = sum(p.values())
            rho = np.ones(len(m_))
            for ci in np.unique(cid):
                s = cid == ci
                num = np.convolve(np.where(ok[s], tot[s], 0.0), np.ones(11), "same")
                den = np.convolve(np.where(ok[s], m_[s] * ps, 0.0), np.ones(11), "same")
                rho[s] = np.where(den > 0, num / np.maximum(den, 1e-9), 1.0)
            cal = {L: {"syn": [], "M": []} for L in ("H", "C", "B", "G")}
            for rep in range(5):
                syn = {L: rng.poisson(m_ * p[L] * rho).astype(np.int64) for L in ("H", "C", "B", "G")}
                syn["m"] = w["m"]
                ps_ = {L: syn[L][ok].sum() / syn["m"][ok].sum() for L in ("H", "C", "B", "G")}
                for L in ("H", "C", "B", "G"):
                    cal[L]["syn"].append(len(FM.mesas(syn[L].astype(float), m_, cid, ok, ps_[L])))
                    E, _ = FM.het_expect(syn, L, ok)
                    Ef = np.zeros(len(m_)); Ef[ok] = E
                    cal[L]["M"].append(len(FM.mesas(rng.poisson(Ef).astype(float), m_, cid, ok, ps_[L])))
            for L in cal:
                cal[L]["M_over_syn"] = float(np.sum(cal[L]["M"]) / max(np.sum(cal[L]["syn"]), 1))
            res["C3"][key] = cal
            print("C3", key, json.dumps({L: round(v["M_over_syn"], 3) for L, v in cal.items()}), flush=True)

    # K3 beta-fitted null
    res["K3"] = {}
    for filt in ("F0", "F1", "F2"):
        w, cid, ok, per = build(z, auto, filt, 100)
        cell = {}
        for L in ("H", "C", "G"):
            m = w["m"][ok].astype(float)
            p = {k: w[k][ok].sum() / m.sum() for k in ("H", "C", "B", "G")}
            No = sum(w[k][ok] for k in FM.OTHERS[L]).astype(float)
            rho = (No + 1.0) / (m * sum(p[k] for k in FM.OTHERS[L]) + 1.0)
            best = None
            for beta in np.arange(0.5, 2.01, 0.25):
                E = m * p[L] * rho ** beta
                E *= w[L][ok].sum() / E.sum()
                pr = float((((w[L][ok] - E) ** 2) / (E * (1 + E / np.maximum(No, 1)) + 1e-9)).mean())
                if beta == 1.0:
                    cell[L + "_beta1"] = pr
                if best is None or pr < best[1]:
                    best = (float(beta), pr)
            cell[L] = {"beta": best[0], "phi_res": best[1]}
        cell["R_best"] = cell["H"]["phi_res"] / cell["C"]["phi_res"]
        res["K3"][filt] = cell
        print("K3", filt, json.dumps(cell), flush=True)

    # K4 Lorenz
    res["K4"] = {}
    for filt in ("F0", "F1"):
        for W in (10, 100, 1000):
            w, cid, ok, per = build(z, auto, filt, W)
            n, m = w["DHC"][ok].astype(float), w["m"][ok].astype(float)
            o = np.argsort(-(n / m))
            cm, cn = np.cumsum(m[o]) / m.sum(), np.cumsum(n[o]) / n.sum()
            share = {f"top{x}pct": float(np.interp(x / 100, cm, cn)) for x in (1, 5, 10, 20, 33)}
            share["x_for_50pct"] = float(np.interp(0.5, cn, cm))
            res["K4"][f"{filt}|{W}kb"] = share
            print("K4", filt, W, json.dumps(share), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)


def selftest():
    import os
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "t.maf.gz")
    # chimp reference; column 3 H-lineage (h=G, ancestral A: W->S), column 5 C-lineage (c=G, ancestral C: S->S)
    blk = ("a\ns GCA_028858775.2.CM054434.2 0 10 + 5000 AAAAAGGGAA\ns hs1.chr1 0 10 + 9 AAAGACGGAA\n"
           "s hg38.chr1 0 10 + 9 AAAGACGGAA\ns GCA_029289425.2.c1 0 10 + 9 AAAAACGGAA\n"
           "s GCA_029281585.2.c1 0 10 + 9 AAAAACGGAA\ns GCA_028885655.2.c1 0 10 + 9 AAAAACGGAA\n\n")
    with gzip.open(p, "wt") as fh:
        fh.write("##maf version=1\n\n" + blk)
    extract(p, os.path.join(d, "t.npz"))
    z = np.load(os.path.join(d, "t.npz"))
    a = z["chr_chr1"].astype(int).sum(axis=1)[0]
    got = dict(zip(FM.FIELDS, a))
    g = dict(zip(GB, z["gb_chr1"].astype(int).sum(axis=1)[0]))
    print(got, g)
    assert got["m"] == 10 and got["H"] == 1 and got["C"] == 1 and got["DHC"] == 2, got
    assert g["H_WS"] == 1 and g["H_SW"] == 0 and g["C_WS"] == 0 and g["C_SW"] == 0, g
    print("selftest ok")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "extract":
        extract(sys.argv[2], sys.argv[3])
    elif cmd == "mirror":
        mirror(sys.argv[2], sys.argv[3])
    elif cmd == "extra":
        extra(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "selftest":
        selftest()
