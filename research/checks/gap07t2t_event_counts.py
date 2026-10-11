"""GAP-07t: human-chimp divergence EVENT count re-run on the T2T ape alignment (CHM13/hs1 vs mPanTro3), replacing
the hg38/panTro6 count of GAP-07b (R4-GAP07b-alignment.md: 37.77 M SNV columns, 4.30 M indel events, 42.10 M events,
21.05 M per lineage).  QUEUE item 7.  THROWAWAY research check (not product code).

Pre-registered: this docstring and the code are committed BEFORE any run on real data (only `selftest`, synthetic, was
run, to debug the parser; it passed).  The MAFs were already parsed
for FM (fm_mesa_replication.py, fm_mirror.py) into per-lineage SNV bins; no indel or event count was made from them
and none of the FM numbers below sets a prediction except as noted (FM's DHC SNV totals were seen: disclosed).
Runs on na-workhorse only (streaming pass ~1-1.5 h per MAF, < 1 GB RAM).
Run:  research/.venv/bin/python -I research/checks/gap07t2t_event_counts.py extract <maf.gz> <ref: hs1|chimp> <out.json>
      research/.venv/bin/python -I research/checks/gap07t2t_event_counts.py report <hs1.json> [<chimp.json>]
      research/.venv/bin/python -I research/checks/gap07t2t_event_counts.py selftest   (synthetic MAF; trivial)

DATA (untrusted, read as text only; never executed; already on workhorse from the FM check):
  sources/raw/fm-maf-2026-10-10/hs1.maf.gz      8-t2t-apes-2023v2 Cactus, hal2maf --refGenome hs1 (md5 df51e5c3...)
  sources/raw/fm-mirror-2026-10-10/pantro.maf.gz same alignment, chimp-referenced (md5 bc332f33...)
  Genomes: hs1 (T2T-CHM13 v2.0), chimpanzee GCA_028858775.2 (mPanTro3), gorilla GCA_029281585.2, Sumatran orangutan
  GCA_028885655.2 (and hg38, bonobo, Bornean orangutan, siamang, unused here).

TARGETS (verbatim; locators in the claim files)
  A3 (Day 2025, Z18168236 s2.1 / claim A3): "Genetic divergence: ~40 million single-nucleotide variants; ~20 million
      fixations required on human lineage."
  A3x / B5 (Day, MITTENS 3.0, Z23003785): 205 M per lineage counted in base pairs (Yoo 2025 SVs + SNVs); 17.5 M SNV
      per lineage.  GAP-07b measured 21.05 M events per lineage on hg38/panTro6 (205 M / 21.05 M = 9.74).
  Yoo 2025 (Nature 641:401, abstract as quoted in R4-GAP07b) reports divergence on the T2T assemblies, which include
      sequence absent from hg38/panTro6 (centromeric satellites, acrocentric arms, segmental duplications).

DEFINITIONS (pairwise reference vs chimp projection of each MAF block; first row of each genome; a block with > 1 row
for the reference or chimp is "dup")
  SNV       column with A/C/G/T in both, differing (case-insensitive).  Lineage by gorilla (as GAP-07b): human-derived
            if g == c, chimp-derived if g == h, "third" if g differs from both, unpolarised if no gorilla base.
            Strict variant: also requires the Sumatran orangutan base == g.
  indel     maximal run of columns where exactly one of ref/chimp has a base (columns where both are gaps are skipped
            and do not break a run).  Type: H-only bases, C-only bases, or "both" (run contains both kinds).
            Lineage of an H-only run (chimp lacks the bases): gorilla has bases at >= 50% of the run's columns ->
            chimp deletion (chimp lineage), else human insertion (human lineage); mirror for C-only; "both" and
            no-gorilla runs unpolarised.  A run touching a block edge that continues into the next block (same
            ref chrom contiguous, same chimp sequence/strand contiguous, same type at the edge) is merged (counted once).
  inter-block indel: consecutive chimp-bearing blocks on the same reference chromosome with the same chimp
            sequence and strand, gap dt (reference) >= 0 and dq (chimp) >= 0, dt + dq > 0, max(dt, dq) <= CAP
            (CAP = 100 kb primary; 10 kb and 1 kb reported): one event, unpolarised.  (Proxy for GAP-07b's chain gaps
            inside nets; larger discontinuities are rearrangements/unaligned, counted separately.)
  unaligned: reference bases in blocks with no chimp row (bp only), and discontinuities > CAP (count).
  Filters: F0 all; F1 no N in either row and not dup; F2 = F1 and not repeat (lowercase in either row; indel run:
            >= 50% of its bases lowercase).  Chromosomes: autosomes, X, Y reported separately; totals over all
            three ("primary", as GAP-07b), chrM and unplaced excluded.
  Events per lineage = (SNV + indel + inter-block indel) / 2, F0, primary (the GAP-07b headline definition).
  Polymorphism-corrected per lineage: GAP-07c human-measured shares (s_snv 15.59%, s_ind 10.12%, human data only;
            chimp assumed equal) and the CSAC 0.78-0.86 fixed share; no chimp population data are used (refresh
            2026-10-10b s6: chimp VCFs not located; ENA portal errored).

DISCLOSED before registration: FM's F0 pairwise human-chimp SNV total on hs1 "core" columns (all six core genomes
present) was seen in fm_analyse.json (not reproduced here); it is a subset of this count (core columns only).

PRE-REGISTERED PREDICTIONS (hs1-referenced pass; primary chromosomes; F0 unless stated)
  Day side (A3 "~40 million SNVs", "~20 million fixations"; and the reading that T2T sequence raises the count):
    D1 SNVs >= 40 M and events per lineage >= 22 M (T2T adds divergence relative to hg38/panTro6).
    D2 205 M / events per lineage <= 9 (the bp-to-event gap shrinks on T2T).
  Critic side (GAP-07b's conclusion: events, not bp; ~20 M per lineage; the 205 M is a bp count):
    C1 events per lineage within 15% of 21.05 M (17.9-24.2 M); 205 M / events in [8.5, 11.5].
    C2 SNV share of events >= 85%; the large-bp share is carried by few events (median indel 1-2 bp).
  Audit (numeric):
    A1 SNV (F0) 38-46 M (T2T adds ~200 Mb of hard-to-align sequence; projection on hs1 drops chimp-only regions);
       F1 SNV 33-42 M; F2 SNV 15-25 M.
    A2 indel events (in-block + inter-block <= 100 kb) 3.5-6.0 M; median length 1-2 bp; >= 40% are 1 bp.
    A3 events per lineage 21-26 M; 205 M / events 7.9-9.8.
    A4 polarised human / (human + chimp) SNV share 0.46-0.54 (F1); indel lineage share 0.40-0.60.
    A5 chimp-referenced pass (if run): events per lineage within 10% of the hs1 pass (reference bias small for counts).
    A6 polymorphism-corrected per lineage (GAP-07c human shares, chimp assumed equal): 17.5-22.5 M.
  Verdict relevance: C1 holding re-confirms A3's 20 M magnitude on T2T (and A3x's bp-vs-events point); D1 + D2
  holding would mean the T2T assemblies move the event count materially (> 25%, rule R1) toward Day's 205 M.
"""
import gzip
import json
import sys
import time

import numpy as np

CHIMP = "GCA_028858775.2"
GOR = "GCA_029281585.2"
ORA = "GCA_028885655.2"
CAPS = (1000, 10000, 100000)
ACGT = np.zeros(256, bool)
for ch in b"ACGTacgt":
    ACGT[ch] = True
NN = np.zeros(256, bool)
for ch in b"Nn":
    NN[ch] = True
LOW = np.zeros(256, bool)
for ch in b"acgtn":
    LOW[ch] = True
SIZE_EDGES = (1, 10, 50, 1000)


PANTRO = {"CM054434.2": "chr1", "CM068905.1": "chr2", "CM054437.2": "chr3", "CM054438.2": "chr4",
          "CM054439.2": "chr5", "CM054440.2": "chr6", "CM054441.2": "chr7", "CM054442.2": "chr8",
          "CM054443.2": "chr9", "CM054444.2": "chr10", "CM054445.2": "chr11", "CM054446.2": "chr12",
          "CM054447.2": "chr13", "CM054448.2": "chr14", "CM054449.2": "chr15", "CM054450.2": "chr16",
          "CM054451.2": "chr17", "CM054452.2": "chr18", "CM054453.2": "chr19", "CM054454.2": "chr20",
          "CM054455.2": "chr21", "CM054456.2": "chr22", "CM068906.1": "chr23", "CM054457.2": "chrX",
          "CM054458.2": "chrY"}   # copied from fm_mirror.py (NCBI assembly report, sha256 f8ead51d...)


def chrom_class(ch):
    if ch in PANTRO:                 # chimp reference: chr1..chr23 are autosomes (chimp numbering)
        c = PANTRO[ch].replace("chr", "")
        return "X" if c == "X" else "Y" if c == "Y" else "auto"
    c = ch.replace("chr", "")
    if c in ("X",):
        return "X"
    if c in ("Y",):
        return "Y"
    if c.isdigit() and 1 <= int(c) <= 22:
        return "auto"
    return None


def size_class(n):
    for i, e in enumerate(SIZE_EDGES):
        if n <= e:
            return i
    return len(SIZE_EDGES)


def new_acc():
    a = {}
    for f in ("F0", "F1", "F2"):
        a[f] = dict(snv=0, snv_h=0, snv_c=0, snv_third=0, snv_unpol=0, snv_h_strict=0, snv_c_strict=0,
                    snv_rep=0, cols=0, indel=0, indel_h=0, indel_c=0, indel_unpol=0, indel_bp=0,
                    indel_type=[0, 0, 0], indel_size=[0] * (len(SIZE_EDGES) + 1),
                    inter={str(c): 0 for c in CAPS}, inter_bp={str(c): 0 for c in CAPS})
    a["unaligned_ref_bp"] = 0
    a["discont"] = 0
    a["blocks"] = 0
    a["blocks_chimp"] = 0
    a["blocks_dup"] = 0
    return a


def runs_of(t):
    """t: int8 array of column types (0 aligned, 1 ref-only bases, 2 chimp-only bases), already without skipped columns.
    Returns list of (start, end, kinds_mask)."""
    nz = t != 0
    if not nz.any():
        return []
    d = np.diff(np.concatenate(([0], nz.astype(np.int8), [0])))
    st = np.flatnonzero(d == 1)
    en = np.flatnonzero(d == -1)
    out = []
    for s, e in zip(st, en):
        seg = t[s:e]
        km = (1 if (seg == 1).any() else 0) | (2 if (seg == 2).any() else 0)
        out.append((int(s), int(e), km))
    return out


def extract(maf, ref, out):
    t0 = time.time()
    refpfx = "hs1." if ref == "hs1" else CHIMP + "."
    othpfx = CHIMP + "." if ref == "hs1" else "hs1."
    acc = {k: new_acc() for k in ("auto", "X", "Y")}
    state = dict(prev=None)          # last chimp-bearing block: (chrom, ref_end, oth_src, oth_strand, oth_end, edge)

    def flush(block):
        rrows = [b for b in block if b[0].startswith(refpfx)]
        if not rrows:
            return
        rsrc, rstart, rsize, rstrand, rsrcsize, rseq = rrows[0]
        cls = chrom_class(rsrc[len(refpfx):])
        if cls is None:
            return
        A = acc[cls]
        A["blocks"] += 1
        orows = [b for b in block if b[0].startswith(othpfx)]
        grows = [b for b in block if b[0].startswith(GOR + ".")]
        arows = [b for b in block if b[0].startswith(ORA + ".")]
        dup = len(rrows) > 1 or len(orows) > 1
        A["blocks_dup"] += int(dup)
        r = np.frombuffer(rseq.encode(), np.uint8)
        if not orows:
            A["unaligned_ref_bp"] += int(ACGT[r].sum() + NN[r].sum())
            return
        A["blocks_chimp"] += 1
        osrc, ostart, osize, ostrand, osrcsize, oseq = orows[0]
        c = np.frombuffer(oseq.encode(), np.uint8)
        g = np.frombuffer(grows[0][5].encode(), np.uint8) if grows else None
        o = np.frombuffer(arows[0][5].encode(), np.uint8) if arows else None
        # inter-block discontinuity
        pv = state["prev"]
        merge_first = None
        if pv is not None and pv[0] == rsrc and pv[2] == osrc and pv[3] == ostrand:
            dt = rstart - pv[1]
            dq = ostart - pv[4]
            if dt >= 0 and dq >= 0 and (dt + dq) > 0:
                m = max(dt, dq)
                if m <= CAPS[-1]:
                    for f in ("F0", "F1", "F2"):
                        for cap in CAPS:
                            if m <= cap:
                                A[f]["inter"][str(cap)] += 1
                                A[f]["inter_bp"][str(cap)] += dt + dq
                else:
                    A["discont"] += 1
            elif dt == 0 and dq == 0:
                merge_first = pv[5]
            else:
                A["discont"] += 1
        elif pv is not None and pv[0] == rsrc:
            A["discont"] += 1
        ru, cu = r & 0xDF, c & 0xDF
        rb, cb = ACGT[r], ACGT[c]
        rgap, cgap = r == ord("-"), c == ord("-")
        anyN = NN[r] | NN[c]
        rep = LOW[r] | LOW[c]
        # SNVs
        snv = rb & cb & (ru != cu)
        if g is not None:
            gu = g & 0xDF
            gb = ACGT[g]
            hder = snv & gb & (gu == cu)
            cder = snv & gb & (gu == ru)
            third = snv & gb & (gu != cu) & (gu != ru)
            unp = snv & ~gb
            if o is not None:
                ou = o & 0xDF
                ok_o = ACGT[o] & (ou == gu)
            else:
                ok_o = np.zeros(len(r), bool)
        else:
            hder = cder = third = np.zeros(len(r), bool)
            unp = snv
            ok_o = np.zeros(len(r), bool)
        alig = rb & cb
        masks = {"F0": np.ones(len(r), bool)}
        masks["F1"] = ~anyN & (not dup)
        masks["F2"] = masks["F1"] & ~rep
        for f, mk in masks.items():
            if f != "F0" and dup:
                continue
            a = A[f]
            a["cols"] += int((alig & mk).sum())
            a["snv"] += int((snv & mk).sum())
            a["snv_h"] += int((hder & mk).sum())
            a["snv_c"] += int((cder & mk).sum())
            a["snv_third"] += int((third & mk).sum())
            a["snv_unpol"] += int((unp & mk).sum())
            a["snv_h_strict"] += int((hder & ok_o & mk).sum())
            a["snv_c_strict"] += int((cder & ok_o & mk).sum())
            a["snv_rep"] += int((snv & rep & mk).sum())
        # indels
        rbase = ~rgap
        cbase = ~cgap
        keep = rbase | cbase
        t = np.zeros(len(r), np.int8)
        t[rbase & cgap] = 1
        t[cbase & rgap] = 2
        idx = np.flatnonzero(keep)
        tk = t[idx]
        runs = runs_of(tk)
        last_edge = 0
        for k, (s, e, km) in enumerate(runs):
            cols = idx[s:e]
            nref = int(rbase[cols].sum())
            noth = int(cbase[cols].sum())
            if e == len(tk):
                last_edge = km
            if s == 0 and merge_first is not None and merge_first == km and km in (1, 2):
                for f in ("F0", "F1", "F2"):
                    A[f]["indel_bp"] += nref + noth
                continue
            hasN = bool(anyN[cols].any())
            bases = np.concatenate((r[cols][rbase[cols]], c[cols][cbase[cols]]))
            isrep = bool(LOW[bases].mean() >= 0.5) if len(bases) else False
            if km == 3 or g is None:
                lin = "u"
            else:
                gpres = float((~(g[cols] == ord("-"))).mean()) >= 0.5
                if km == 1:            # ref has bases, chimp lacks them
                    lin = ("c" if gpres else "h") if ref == "hs1" else ("h" if gpres else "c")
                else:                  # chimp (other) has bases, ref lacks them
                    lin = ("h" if gpres else "c") if ref == "hs1" else ("c" if gpres else "h")
            ln = max(nref, noth)
            for f in ("F0", "F1", "F2"):
                if f != "F0" and (dup or hasN):
                    continue
                if f == "F2" and isrep:
                    continue
                a = A[f]
                a["indel"] += 1
                a["indel_bp"] += nref + noth
                a["indel_" + ("h" if lin == "h" else "c" if lin == "c" else "unpol")] += 1
                a["indel_type"][km - 1] += 1
                a["indel_size"][size_class(ln)] += 1
        oend = ostart + osize
        state["prev"] = (rsrc, rstart + rsize, osrc, ostrand, oend, last_edge)

    nblk = 0
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
    json.dump(dict(ref=ref, maf=maf, blocks=nblk, acc=acc), open(out, "w"), indent=1)
    print(f"extract done: {nblk} blocks, {time.time() - t0:.0f} s", flush=True)


def summarise(d, label):
    acc = d["acc"]
    print(f"\n## {label} (reference {d['ref']}; {d['blocks']} blocks)")
    print("| filter | class | aligned cols | SNV | indel (in-block) | inter <=1k / 10k / 100k | events (SNV+indel+inter100k) | per lineage | 205M / per lineage | SNV share |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    res = {}
    for f in ("F0", "F1", "F2"):
        tot = dict(cols=0, snv=0, indel=0, i1=0, i10=0, i100=0)
        for cls in ("auto", "X", "Y", "primary"):
            if cls == "primary":
                a = tot
                cols, snv, ind, i1, i10, i100 = a["cols"], a["snv"], a["indel"], a["i1"], a["i10"], a["i100"]
            else:
                a = acc[cls][f]
                cols, snv, ind = a["cols"], a["snv"], a["indel"]
                i1, i10, i100 = (a["inter"][str(c)] for c in CAPS)
                for k, v in (("cols", cols), ("snv", snv), ("indel", ind), ("i1", i1), ("i10", i10), ("i100", i100)):
                    tot[k] += v
            ev = snv + ind + i100
            res[(f, cls)] = dict(snv=snv, indel=ind + i100, events=ev, per=ev / 2)
            print(f"| {f} | {cls} | {cols / 1e6:.1f} M | {snv / 1e6:.2f} M | {ind / 1e6:.2f} M | {i1 / 1e6:.3f} / {i10 / 1e6:.3f} / "
                  f"{i100 / 1e6:.3f} M | {ev / 1e6:.2f} M | {ev / 2e6:.2f} M | {205e6 / (ev / 2) if ev else float('nan'):.2f} | "
                  f"{snv / ev if ev else float('nan'):.3f} |")
    print("\nlineage (primary): SNV human / chimp / third / unpolarised; strict h/c; indel h / c / unpol; size classes 1,2-10,11-50,51-1000,>1000; types ref-only/oth-only/both")
    for f in ("F0", "F1", "F2"):
        S = {k: sum(acc[c][f][k] for c in ("auto", "X", "Y")) for k in
             ("snv_h", "snv_c", "snv_third", "snv_unpol", "snv_h_strict", "snv_c_strict", "indel_h", "indel_c", "indel_unpol", "indel_bp", "indel")}
        sz = np.sum([acc[c][f]["indel_size"] for c in ("auto", "X", "Y")], axis=0)
        ty = np.sum([acc[c][f]["indel_type"] for c in ("auto", "X", "Y")], axis=0)
        hs = S["snv_h"] / max(S["snv_h"] + S["snv_c"], 1)
        hi = S["indel_h"] / max(S["indel_h"] + S["indel_c"], 1)
        print(f"  {f}: SNV {S['snv_h'] / 1e6:.2f} / {S['snv_c'] / 1e6:.2f} / {S['snv_third'] / 1e6:.2f} / {S['snv_unpol'] / 1e6:.2f} M "
              f"(human share {hs:.3f}; strict {S['snv_h_strict'] / 1e6:.2f} / {S['snv_c_strict'] / 1e6:.2f} M); indel "
              f"{S['indel_h'] / 1e6:.2f} / {S['indel_c'] / 1e6:.2f} / {S['indel_unpol'] / 1e6:.2f} M (human share {hi:.3f}); "
              f"size {list(map(int, sz))} (1 bp share {sz[0] / max(sz.sum(), 1):.3f}); types {list(map(int, ty))}; "
              f"in-block indel bp {S['indel_bp'] / 1e6:.1f} M")
    un = sum(acc[c]["unaligned_ref_bp"] for c in ("auto", "X", "Y"))
    dc = sum(acc[c]["discont"] for c in ("auto", "X", "Y"))
    print(f"  reference bp in blocks without a chimp row: {un / 1e6:.1f} M; discontinuities > 100 kb or non-collinear: {dc}")
    return res


def report(paths):
    out = {}
    for p in paths:
        d = json.load(open(p))
        out[d["ref"]] = summarise(d, p)
    r = out.get("hs1")
    if r:
        F0 = r[("F0", "primary")]
        print("\n## polymorphism-corrected per lineage (hs1 pass, F0 primary)")
        for lab, ss, si in (("GAP-07c human shares, chimp assumed equal", 0.1559, 0.1012),
                            ("GAP-07c pooled (human data only)", 0.0825, 0.0528),
                            ("CSAC fixed 0.86 (all events)", 0.14, 0.14), ("CSAC fixed 0.78 (all events)", 0.22, 0.22)):
            fx = (F0["snv"] * (1 - ss) + F0["indel"] * (1 - si)) / 2
            print(f"  {lab}: {fx / 1e6:.2f} M per lineage; 205 M / that = {205e6 / fx:.2f}")
        print(f"\nGAP-07b reference: 37.77 M SNV, 4.30 M indel events, 21.05 M per lineage, 9.74.  hs1 F0 primary: "
              f"SNV {F0['snv'] / 1e6:.2f} M ({F0['snv'] / 37.77e6:.3f}x), indel {F0['indel'] / 1e6:.2f} M ({F0['indel'] / 4.30e6:.3f}x), "
              f"per lineage {F0['per'] / 1e6:.2f} M ({F0['per'] / 21.05e6:.3f}x)")
        if "chimp" in out:
            c0 = out["chimp"][("F0", "primary")]
            print(f"chimp-referenced F0 primary per lineage {c0['per'] / 1e6:.2f} M; ratio to hs1 {c0['per'] / F0['per']:.3f} (A5 within 10%)")


def selftest():
    import os
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "t.maf.gz")
    blk1 = ("a\ns hs1.chr1 0 10 + 100 ACGTA--CGTA\ns GCA_028858775.2.chr1 0 9 + 100 ACCTAGGCG-A\n"
            "s GCA_029281585.2.chr1 0 11 + 100 ACGTAGGCGTA\ns GCA_028885655.2.chr1 0 11 + 100 ACGTAGGCGTA\n\n")
    blk2 = ("a\ns hs1.chr1 12 4 + 100 ACGT\ns GCA_028858775.2.chr1 10 4 + 100 ACGA\n"
            "s GCA_029281585.2.chr1 12 4 + 100 ACGT\n\n")
    with gzip.open(p, "wt") as fh:
        fh.write("##maf version=1\n\n" + blk1 + blk2)
    o = os.path.join(d, "o.json")
    extract(p, "hs1", o)
    a = json.load(open(o))["acc"]["auto"]["F0"]
    # block1: SNV at col 2 (G vs C; gorilla G = human -> chimp-derived); chimp-only run 'GG' (gorilla has bases ->
    # human deletion -> human lineage); ref-only run at col 9 ('T' vs '-', gorilla has T -> chimp deletion);
    # block2: dt = 12 - 10 = 2, dq = 10 - 9 = 1 -> one inter-block event; SNV T/A, gorilla T -> chimp-derived.
    exp = dict(snv=2, snv_c=2, indel=2, indel_h=1, indel_c=1)
    got = {k: a[k] for k in exp}
    print("selftest", got, "inter", a["inter"], "expected", exp, "inter 1 at every cap")
    assert got == exp and all(v == 1 for v in a["inter"].values()), "selftest FAILED"
    print("selftest PASS")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "extract":
        extract(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "report":
        report(sys.argv[2:])
    else:
        selftest()
