"""L1b POST HOC, DESCRIPTIVE, NOT PRE-REGISTERED AS A TEST: what puts the genes of the X1 arm out of register.

Written 2026-10-13 in the L1b fix pass, to answer REVIEW-R4-L1b-correctness finding 1 (MAJOR: "What puts X1's genes
out of register is not known") and finding 2 (MINOR: the X1 concatenation follows MAF block order and the order was
not checked). The registered script l1b_t2t_dnds.py (0fe3c7f) is not edited and is not rerun. No band, prediction or
verdict move of L1b depends on this script.

WHAT WAS ALREADY SEEN when this was written (so nothing below is blind):
  - raw/l1b.out, raw/l1b.json, raw/l1b.genes.tsv.gz and the write-up R4-L1b.md (188ea43): X1 ALL 0.853 against V0 ALL
    0.271; 2,637 "affected" genes (X1 counts differ from V0) read 0.960 with a single-difference share of 73.6% and
    hold 94.1% of X1's differences; 2,291 of them have a gapped codon on V0, 346 have none.
  - the three reviews of R4-L1b. Correctness: first-row chimp coverage is 98.87% of CDS; 40.7% of X1's differences sit
    in 1,237 genes lacking a first-row chimp base over more than 1% of their CDS; 444 affected genes with no internal
    stop read 1.004. Steelman-day: V0 leaves out about 129,100 codons in 2,411 genes. Steelman-critic: share on
    affected genes 73.2-74.5% in four gene sets.
  - one line of raw/l1c.out (seen while checking L1c's band for the fix pass): L1c's diagnostics count on the same
    dump "cactus_frameshift_runs": 2596, "cactus_inframe_indel_runs": 2843, "genes_with_cactus_frameshift_run": 1228.
  - NOT seen: any per-class breakdown of the X1 excess; the segment dump itself.

INPUTS (read only, never executed; on na-workhorse):
  - L1b's segment dump sources/raw/l1b-seg-2026-10-13/seg.json.gz, sha256 expected
    86b0e672d70bb6be1bd2978f869c06519482f191d11fe06d829d21b573afeacd (the script prints the hash it finds and stops
    if it differs, unless `nohash` is given). One json line per chosen transcript: tid, human (hs1 CDS in genomic
    order, N where no block covers it), segs = [[g0, ref_slice, [[chimp_seq, strand, chimp_start, chimp_slice], ...]]]
    in MAF stream order (l1b_t2t_dnds.py `extract`; segment = one block x one CDS exon, columns from the first to the
    last CDS base).
  - the annotation L1b used (exon structure and strand; parsed by l1b_t2t_dnds.load_annotation, imported unchanged).
  - raw/l1b.genes.tsv.gz (per-gene V0 and X1 counts of the registered run).

WHAT X1 DOES (l1b_t2t_dnds.assemble): chimp string = first-row chimp bases of every segment in list order, gaps
  removed, chimp-only insertion columns kept; reverse-complemented for '-' transcripts; padded or cut to the human
  length; compared position by position. So X1's offset against the alignment changes at every place where the
  number of first-row chimp bases differs from the number of human CDS bases. This script lists those places.

EVENT CLASSES (each event changes the X1 offset; fixed here before any run on the dump)
  Indel classes: the first chimp row has bases on both sides and its coordinates run on without a break, so the
  alignment itself asserts a length difference between the two assemblies.
    del_fs / del_3   chimp-row gap run at human CDS bases, length not a multiple of 3 / a multiple of 3. A run that
                     meets a block boundary inside an exon is joined to the run on the other side when the first row
                     continues on the same chimp sequence and strand at the next coordinate.
    ins_fs / ins_3   human-row gap run with chimp bases (chimp-only insertion), same split.
  Hole classes: human CDS bases with no first-row chimp base, where the dump does not show continuous chimp sequence
  across the missing stretch.
    hole_noblock     human CDS bases that no CDS-overlapping block covers.
    hole_norow       segment whose block has no chimp row.
    hole_rowempty    segment whose first chimp row has no base over the CDS slice.
    hole_break       chimp-row gap run that meets a block boundary inside an exon where the first row does NOT
                     continue (other chimp sequence or strand, a jump or step back in coordinate, or one of the three
                     classes above next to it).
  Ambiguous class:
    edge_exon        chimp-row gap run that meets an exon edge or the CDS end. The flank is intronic or outside the
                     CDS and is not in the dump, so deletion and hole cannot be told apart here.
  Order check (correctness finding 2): transcripts whose g0 values are not strictly increasing in list order, i.e.
    where X1's concatenation is not in genomic (hence transcript) order. Such genes are reported as class
    `block_order` and are not analysed further.
  Flags, not events (they change no offset by themselves): first-row change of chimp sequence or strand between
    consecutive segments (`switch`), step back in chimp coordinate on the same sequence and strand (`backstep`).

PER GENE: events in transcript order; the first event ("first cause"); the set of coarse classes present (INDEL_FS,
  INDEL_3, HOLE, EDGE); per human codon the X1 offset (0 = in register; multiple of 3 = whole-codon shift; else frame
  shift; beyond the end of X1 = padding, not compared). An out-of-register codon is assigned to the event that took
  the offset away from 0. A deleted or missing stretch counts as out of register from its first base.
  Attribution of X1's excess differences (X1 Sd+Nd minus V0 Sd+Nd, from the registered per-gene table): per gene to
  its first cause, and separately to its combination of coarse classes. Codon level: base mismatches in compared
  codons (A, C, G, T only; stop codons not excluded, so totals exceed Sd+Nd slightly) by assigned class.
  Internal check of the offset model: every codon called in register must have an X1 codon equal to the
  column-paired first-row codon (V0), unless the latter holds a gap. The number of violations is printed.

PREDICTIONS (written before any run on the dump; each side's best reading; descriptive, no verdict moves on them)
  Day side: the affected genes are mostly genes in which the two assemblies really differ in length inside the CDS.
    Stated as numbers: more than 50% of affected genes have a frame-changing indel (del_fs or ins_fs) as first cause,
    those genes carry more than 50% of X1's excess differences, and hole classes carry less than 25%. If so, X1's
    high value marks genes where the chimp CDS as assembled does not keep the human frame: a real sequence difference
    as the alignment reports it, which a column-paired count passes over by skipping the gapped codons (the direction
    of Q181).
  Critic side: the excess is carried by what is paired with what, not by sequence difference. Stated as numbers: hole
    classes plus in-frame indels (del_3, ins_3) plus edge_exon carry at least 50% of X1's excess; frame-changing
    indels are the first cause in fewer than 50% of affected genes; and genes whose events are all in-frame indels
    or holes (no del_fs, no ins_fs) still read about 1 under X1 (0.85-1.15), as non-homologous codon pairs do.
  Both can hold in part (the criteria are reported one by one). The audit's own expectation, stated: mixed, with
    frame-changing indels the largest single class by genes (L1c's count of 1,228 genes was seen) and holes a
    substantial share of the excess (the coverage figures of the correctness review were seen).
  WHAT THIS CANNOT SHOW, whatever the numbers: (1) it cannot identify Day's pipeline, which is unreleased; (2) an
    alignment gap is the aligner's statement, so "real length difference" means "as Cactus aligns the two
    assemblies", and an assembly or annotation error in either genome looks the same; (3) under every class the
    excess differences X1 counts are differences between codons the alignment does not pair, not substitutions.

RESOURCES: one process, streaming the dump one gene at a time; under 1 GB; a few minutes (annotation parse ~1 min).
RUN (na-workhorse):
  research/.venv/bin/python -I research/checks/l1b_posthoc_x1_breakdown.py selftest
  research/.venv/bin/python -I research/checks/l1b_posthoc_x1_breakdown.py run \
    sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz \
    sources/raw/l1b-seg-2026-10-13/seg.json.gz research/checks/results/raw/l1b.genes.tsv.gz \
    research/checks/results/raw/l1b_x1_breakdown.json > research/checks/results/raw/l1b_x1_breakdown.out
"""
import gzip
import hashlib
import importlib.util
import json
import math
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SEG_SHA256 = "86b0e672d70bb6be1bd2978f869c06519482f191d11fe06d829d21b573afeacd"
COMP = str.maketrans("ACGTacgtNn-", "TGCAtgcaNn-")
ACGT = set("ACGT")
HOLES = ("hole_noblock", "hole_norow", "hole_rowempty", "hole_break")
CLASSES = ("del_fs", "del_3", "ins_fs", "ins_3") + HOLES + ("edge_exon",)
COARSE = dict(del_fs="INDEL_FS", ins_fs="INDEL_FS", del_3="INDEL_3", ins_3="INDEL_3", edge_exon="EDGE",
              **{h: "HOLE" for h in HOLES})
RUNS = re.compile(r"D+|I+")


def revcomp(s):
    return s.translate(COMP)[::-1]


def markers(rs, cs):
    """Column classes of one segment: '.' both bases, 'D' human base and chimp gap, 'I' human gap and chimp base
    (columns where both are gaps are dropped)."""
    if "-" not in rs and "-" not in cs:
        return "." * len(rs)
    out = []
    for a, b in zip(rs, cs):
        if a != "-":
            out.append("D" if b == "-" else ".")
        elif b != "-":
            out.append("I")
    return "".join(out)


def gene_events(L, strand, cds, segs):
    """Events of one transcript. Returns dict(ordered, events=[(tstart, delta, cls)], flags, x1, v0).
    cds = sorted genomic (start, end) intervals; segs as in the dump (list order = MAF stream order)."""
    g0s = [s[0] for s in segs]
    ordered = all(a < b for a, b in zip(g0s, g0s[1:]))
    bounds = set()
    acc = 0
    for s, e in cds:
        bounds.add(acc)
        acc += e - s
    bounds.add(acc)
    x1 = "".join(rows[0][3].replace("-", "") for g0, rs, rows in segs if rows)  # list order, as assemble()
    flags = dict(switch=0, backstep=0, overlap=0)
    # tokens in genomic order: ('M', n) ('D', gpos, n) ('I', gpos, n) ('H', gpos, n, cls) ('B', kind)
    toks = [("B", "exon")]
    v0 = ["-"] * L
    pos = 0
    prev = None  # (src, strand, chimp_end) of the previous segment's first row, if it had bases
    for g0, rs, rows in sorted(segs, key=lambda s: s[0]):
        nref = len(rs) - rs.count("-")
        if g0 < pos:
            flags["overlap"] += 1
        if g0 > pos:
            toks.append(("H", pos, g0 - pos, "hole_noblock"))
            prev = None
        cs = rows[0][3] if rows else ""
        nch = len(cs) - cs.count("-")
        if not rows or nch == 0:
            if g0 in bounds:
                toks.append(("B", "exon"))
            toks.append(("H", g0, nref, "hole_norow" if not rows else "hole_rowempty"))
            prev = None
            pos = max(pos, g0 + nref)
            continue
        src, st, cst = rows[0][0], rows[0][1], rows[0][2]
        if prev is not None:
            if (prev[0], prev[1]) != (src, st):
                flags["switch"] += 1
            elif cst < prev[2]:
                flags["backstep"] += 1
        if g0 in bounds:
            toks.append(("B", "exon"))
        elif prev is not None:
            toks.append(("B", "contig" if (prev[0], prev[1], prev[2]) == (src, st, cst) else "break"))
        elif toks[-1][0] != "H":
            toks.append(("B", "break"))
        mk = markers(rs, cs)
        k = 0
        last = 0
        hp = g0
        for mo in RUNS.finditer(mk):
            if mo.start() > last:
                toks.append(("M", mo.start() - last))
                hp += mo.start() - last
            n = mo.end() - mo.start()
            if mk[mo.start()] == "D":
                toks.append(("D", hp, n))
                hp += n
            else:
                toks.append(("I", hp, n))
            last = mo.end()
        if last < len(mk):
            toks.append(("M", len(mk) - last))
        # column-paired first-row chimp (V0), for the internal check
        j = g0
        for a, b in zip(rs, cs):
            if a != "-":
                if 0 <= j < L:
                    v0[j] = b
                j += 1
        prev = (src, st, cst + nch)
        pos = max(pos, g0 + nref)
    if pos < L:
        toks.append(("H", pos, L - pos, "hole_noblock"))
    toks.append(("B", "exon"))
    # join D runs across contiguous block boundaries
    merged = []
    for t in toks:
        if (t[0] == "D" and len(merged) >= 2 and merged[-1] == ("B", "contig") and merged[-2][0] == "D"):
            merged.pop()
            d = merged.pop()
            merged.append(("D", d[1], d[2] + t[2]))
        else:
            merged.append(t)
    ev = []  # genomic: (gstart, gend, delta, cls)
    for i, t in enumerate(merged):
        if t[0] == "H":
            ev.append((t[1], t[1] + t[2], -t[2], t[3]))
        elif t[0] == "I":
            ev.append((t[1], t[1], t[2], "ins_3" if t[2] % 3 == 0 else "ins_fs"))
        elif t[0] == "D":
            nb = [merged[i - 1], merged[i + 1]]
            if any(x[0] == "H" or x == ("B", "break") for x in nb):
                cls = "hole_break"
            elif any(x == ("B", "exon") for x in nb):
                cls = "edge_exon"
            else:
                cls = "del_3" if t[2] % 3 == 0 else "del_fs"
            ev.append((t[1], t[1] + t[2], -t[2], cls))
    if strand == "-":
        tev = sorted(((L - b, d, c) for a, b, d, c in ev), key=lambda x: x[0])
        x1 = revcomp(x1)
        v0s = revcomp("".join(v0))
    else:
        tev = sorted(((a, d, c) for a, b, d, c in ev), key=lambda x: x[0])
        v0s = "".join(v0)
    return dict(ordered=ordered, events=tev, flags=flags, x1=x1, v0=v0s)


def codon_walk(L, human_t, ge):
    """Per codon state under X1. Returns dict(counts by (cls, state), mism by cls, inreg_mism, violations, pad)."""
    ev = ge["events"]
    T = len(ge["x1"])
    x1 = (ge["x1"] + "-" * L)[:L].upper()
    v0 = ge["v0"].upper()
    h = human_t.upper()
    out = dict(codons={}, mism={}, inreg=0, inreg_mism=0, viol=0, pad=0, oor=0)
    k = 0
    off = 0
    owner = None
    for c in range(L // 3):
        p = 3 * c
        st_off = 0
        st_owner = None
        for q in (p, p + 1, p + 2):
            while k < len(ev) and ev[k][0] <= q:
                was = off
                off += ev[k][1]
                if was == 0 and off != 0:
                    owner = ev[k][2]
                elif off == 0:
                    owner = None
                k += 1
            if off != 0 and st_owner is None:
                st_off, st_owner = off, owner
        hc, xc = h[p:p + 3], x1[p:p + 3]
        if st_owner is None:
            out["inreg"] += 1
            vc = v0[p:p + 3]
            if "-" not in vc and p + 3 <= T and vc != xc:
                out["viol"] += 1
            if set(hc) <= ACGT and set(xc) <= ACGT:
                out["inreg_mism"] += sum(a != b for a, b in zip(hc, xc))
            continue
        out["oor"] += 1
        if p + 3 > T:
            out["pad"] += 1
            state = "pad"
        else:
            state = "codon_shift" if st_off % 3 == 0 else "frame_shift"
        key = st_owner + "|" + state
        out["codons"][key] = out["codons"].get(key, 0) + 1
        if state != "pad" and set(hc) <= ACGT and set(xc) <= ACGT:
            out["mism"][st_owner] = out["mism"].get(st_owner, 0) + sum(a != b for a, b in zip(hc, xc))
    return out


def jc(p):
    return -0.75 * math.log(1 - 4 * p / 3) if 0 <= p < 0.75 else float("nan")


def pooled(rows, v):
    S = sum(r[v + "_S"] for r in rows)
    N = sum(r[v + "_N"] for r in rows)
    Sd = sum(r[v + "_Sd"] for r in rows)
    Nd = sum(r[v + "_Nd"] for r in rows)
    s1 = sum(r[v + "_s1"] for r in rows)
    n1 = sum(r[v + "_n1"] for r in rows)
    if not S or not N or not Sd:
        return dict(dnds=None, share=None, diffs=Sd + Nd)
    return dict(dnds=jc(Nd / N) / jc(Sd / S), share=(n1 / (n1 + s1)) if n1 + s1 else None, diffs=Sd + Nd)


def load_tsv(path):
    out = {}
    with gzip.open(path, "rt") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        ix = {k: i for i, k in enumerate(head)}
        num = [k for k in head if k[:3] in ("V0_", "X1_")]
        for line in fh:
            f = line.rstrip("\n").split("\t")
            r = {k: float(f[ix[k]]) for k in num}
            r.update(tid=f[ix["tid"]], otype=f[ix["otype"]], SYN=int(f[ix["SYN"]]), cov=float(f[ix["cov"]]),
                     L=int(f[ix["L"]]))
            r["affected"] = any(r["X1_" + k] != r["V0_" + k] for k in ("Sd", "Nd", "s1", "n1"))
            r["excess"] = (r["X1_Sd"] + r["X1_Nd"]) - (r["V0_Sd"] + r["V0_Nd"])
            out[r["tid"]] = r
    return out


def fmt(x, nd=3):
    return "n/a" if x is None or x != x else f"{x:.{nd}f}"


def summarise(recs):
    """recs: per-gene dicts with the TSV row merged in. Returns the result dict."""
    res = {}
    allg = [g for g in recs if g["in_tsv"]]
    aff = [g for g in allg if g["affected"]]
    tot_excess = sum(g["excess"] for g in allg)
    aff_excess = sum(g["excess"] for g in aff)
    res["n_dump"] = len(recs)
    res["n_tsv"] = len(allg)
    res["n_affected"] = len(aff)
    res["excess_total"] = tot_excess
    res["excess_in_affected"] = aff_excess
    res["order"] = dict(not_increasing=sum(1 for g in recs if not g["ordered"]),
                        not_increasing_in_ALL=sum(1 for g in allg if not g["ordered"]),
                        overlap=sum(1 for g in recs if g["flags"]["overlap"]))
    res["consistency"] = {
        "events_and_affected": sum(1 for g in allg if g["n_events"] and g["affected"]),
        "events_not_affected": sum(1 for g in allg if g["n_events"] and not g["affected"]),
        "no_events_affected": sum(1 for g in allg if not g["n_events"] and g["affected"]),
        "no_events_not_affected": sum(1 for g in allg if not g["n_events"] and not g["affected"]),
        "inreg_violations": sum(g["viol"] for g in allg),
        "oor_codons_in_not_affected": sum(g["oor"] for g in allg if not g["affected"]),
    }

    def table(keyf, genes):
        t = {}
        for g in genes:
            t.setdefault(keyf(g), []).append(g)
        out = {}
        for k, gs in sorted(t.items(), key=lambda kv: -sum(g["excess"] for g in kv[1])):
            px, pv = pooled(gs, "X1"), pooled(gs, "V0")
            ex = sum(g["excess"] for g in gs)
            out[k] = dict(genes=len(gs), genes_share=len(gs) / len(genes) if genes else None, excess=ex,
                          excess_share=ex / aff_excess if aff_excess else None, x1=px["dnds"],
                          x1_share=px["share"], v0=pv["dnds"], oor_codons=sum(g["oor"] for g in gs))
        return out

    res["first_cause"] = table(lambda g: g["first"] or "none", aff)
    res["first_cause_coarse"] = table(lambda g: COARSE.get(g["first"], g["first"] or "none"), aff)
    res["combination"] = table(lambda g: "+".join(g["coarse"]) or "none", aff)
    res["only_inframe_or_hole"] = table(lambda g: "no_frame_changing_indel" if "INDEL_FS" not in g["coarse"]
                                        else "has_frame_changing_indel", aff)
    res["only_inframe_indel"] = table(lambda g: "INDEL_3_only" if g["coarse"] == ["INDEL_3"] else "other", aff)
    res["flags_affected"] = dict(switch=sum(1 for g in aff if g["flags"]["switch"]),
                                 backstep=sum(1 for g in aff if g["flags"]["backstep"]),
                                 either=sum(1 for g in aff if g["flags"]["switch"] or g["flags"]["backstep"]))
    res["flags_affected_excess_share"] = (sum(g["excess"] for g in aff if g["flags"]["switch"]
                                              or g["flags"]["backstep"]) / aff_excess) if aff_excess else None
    ev = {c: dict(events=0, bp=0, genes=0) for c in CLASSES}
    cod = {}
    mism = {}
    for g in allg:
        for c, (n, bp) in g["ev_counts"].items():
            ev[c]["events"] += n
            ev[c]["bp"] += bp
            ev[c]["genes"] += 1
        for k, n in g["codons"].items():
            cod[k] = cod.get(k, 0) + n
        for k, n in g["mism"].items():
            mism[k] = mism.get(k, 0) + n
    res["events_ALL"] = ev
    res["oor_codons_by_class_state"] = cod
    res["oor_mismatch_by_class"] = mism
    res["codons_total"] = sum(g["L"] // 3 for g in allg)
    res["oor_codons_total"] = sum(g["oor"] for g in allg)
    res["pad_codons_total"] = sum(g["pad"] for g in allg)
    res["inreg_mismatch"] = sum(g["inreg_mism"] for g in allg if g["n_events"])
    # each side's criteria
    fc = res["first_cause_coarse"]
    g_fs = fc.get("INDEL_FS", {}).get("genes", 0)
    hole = fc.get("HOLE", {}).get("excess_share", 0) or 0
    crit = hole + (fc.get("INDEL_3", {}).get("excess_share", 0) or 0) + (fc.get("EDGE", {}).get("excess_share", 0)
                                                                         or 0)
    nofs = res["only_inframe_or_hole"].get("no_frame_changing_indel", {})
    res["criteria"] = dict(
        day_fs_first_cause_gene_share=g_fs / len(aff) if aff else None,
        day_fs_first_cause_excess_share=fc.get("INDEL_FS", {}).get("excess_share", 0),
        day_hole_excess_share=hole,
        critic_hole_inframe_edge_excess_share=crit,
        critic_no_fs_genes=nofs.get("genes"), critic_no_fs_x1=nofs.get("x1"), critic_no_fs_v0=nofs.get("v0"))
    return res


def report(res):
    p = print
    p(f"transcripts in dump {res['n_dump']}; in the registered gene table (ALL) {res['n_tsv']}; affected "
      f"(X1 Sd,Nd,s1,n1 differ from V0) {res['n_affected']}")
    p(f"X1 excess differences (X1 Sd+Nd - V0 Sd+Nd): ALL {res['excess_total']:.0f}; in affected genes "
      f"{res['excess_in_affected']:.0f}")
    p(f"ORDER CHECK: transcripts with g0 not strictly increasing in list order: {res['order']['not_increasing']} "
      f"(in ALL: {res['order']['not_increasing_in_ALL']}); with overlapping segments: {res['order']['overlap']}")
    c = res["consistency"]
    p(f"MODEL CHECK: genes with >=1 event and affected {c['events_and_affected']}; event(s) but not affected "
      f"{c['events_not_affected']}; no event but affected {c['no_events_affected']}; neither "
      f"{c['no_events_not_affected']}; in-register codons whose X1 codon differs from the column-paired codon: "
      f"{c['inreg_violations']}; out-of-register codons in not-affected genes {c['oor_codons_in_not_affected']}")

    def tab(title, t):
        p("")
        p(title)
        p(f"  {'class':34s} {'genes':>6s} {'%genes':>7s} {'excess':>9s} {'%excess':>8s} {'X1':>6s} {'X1shr':>6s} "
          f"{'V0':>6s} {'oor codons':>10s}")
        for k, d in t.items():
            p(f"  {k:34s} {d['genes']:6d} {100 * d['genes_share']:7.1f} {d['excess']:9.0f} "
              f"{100 * d['excess_share']:8.1f} {fmt(d['x1']):>6s} {fmt(d['x1_share']):>6s} {fmt(d['v0']):>6s} "
              f"{d['oor_codons']:10d}")

    tab("AFFECTED GENES BY FIRST CAUSE (transcript order; shares of affected genes and of their X1 excess)",
        res["first_cause"])
    tab("AFFECTED GENES BY FIRST CAUSE, COARSE", res["first_cause_coarse"])
    tab("AFFECTED GENES BY COMBINATION OF COARSE CLASSES PRESENT", res["combination"])
    tab("AFFECTED GENES WITH / WITHOUT A FRAME-CHANGING INDEL ANYWHERE", res["only_inframe_or_hole"])
    tab("AFFECTED GENES WHOSE ONLY EVENTS ARE IN-FRAME INDELS", res["only_inframe_indel"])
    p("")
    p("EVENTS IN ALL GENES (events, human or chimp bases involved, genes with >=1)")
    for k, d in res["events_ALL"].items():
        p(f"  {k:14s} events {d['events']:6d}  bp {d['bp']:8d}  genes {d['genes']:6d}")
    p("")
    p(f"CODONS: total {res['codons_total']}; out of register under X1 {res['oor_codons_total']} "
      f"({100 * res['oor_codons_total'] / max(1, res['codons_total']):.2f}%), of which beyond the end of X1 "
      f"(padding, not compared) {res['pad_codons_total']}")
    p("  out-of-register codons by assigned class | state:")
    for k, n in sorted(res["oor_codons_by_class_state"].items(), key=lambda kv: -kv[1]):
        p(f"    {k:28s} {n:9d}")
    tm = sum(res["oor_mismatch_by_class"].values())
    p(f"  base mismatches in compared out-of-register codons: {tm} (in-register codons of genes with events: "
      f"{res['inreg_mismatch']})")
    for k, n in sorted(res["oor_mismatch_by_class"].items(), key=lambda kv: -kv[1]):
        p(f"    {k:28s} {n:9d} {100 * n / max(1, tm):6.1f}%")
    f = res["flags_affected"]
    p("")
    p(f"FLAGS among affected genes: first-row switch of chimp sequence/strand {f['switch']}; step back in chimp "
      f"coordinate {f['backstep']}; either {f['either']} (excess share "
      f"{100 * (res['flags_affected_excess_share'] or 0):.1f}%)")
    cr = res["criteria"]
    p("")
    p("CRITERIA STATED IN THE DOCSTRING (descriptive; no verdict moves)")
    p(f"  Day side: frame-changing indel as first cause in > 50% of affected genes: "
      f"{100 * (cr['day_fs_first_cause_gene_share'] or 0):.1f}%; those genes carry > 50% of the excess: "
      f"{100 * (cr['day_fs_first_cause_excess_share'] or 0):.1f}%; hole classes < 25% of the excess: "
      f"{100 * cr['day_hole_excess_share']:.1f}%")
    p(f"  Critic side: hole + in-frame indel + exon-edge first causes >= 50% of the excess: "
      f"{100 * cr['critic_hole_inframe_edge_excess_share']:.1f}%; frame-changing first cause in < 50% of affected "
      f"genes: {100 * (cr['day_fs_first_cause_gene_share'] or 0):.1f}%; genes with no frame-changing indel read "
      f"0.85-1.15 under X1: {fmt(cr['critic_no_fs_x1'])} on {cr['critic_no_fs_genes']} genes (V0 "
      f"{fmt(cr['critic_no_fs_v0'])})")


def analyse_gene(r, human, segs, row):
    ge = gene_events(r["L"], r["strand"], r["cds"], segs)
    g = dict(tid=r["tid"], L=r["L"], ordered=ge["ordered"], flags=ge["flags"], n_events=len(ge["events"]),
             first=None, coarse=[], ev_counts={}, codons={}, mism={}, oor=0, pad=0, viol=0, inreg_mism=0,
             in_tsv=row is not None)
    if row is not None:
        g.update(row)
    if not ge["ordered"]:
        g["first"] = "block_order"
        g["coarse"] = ["ORDER"]
        return g
    if ge["events"]:
        g["first"] = ge["events"][0][2]
        g["coarse"] = sorted({COARSE[e[2]] for e in ge["events"]})
        for t, d, c in ge["events"]:
            n, bp = g["ev_counts"].get(c, (0, 0))
            g["ev_counts"][c] = (n + 1, bp + abs(d))
        ht = revcomp(human) if r["strand"] == "-" else human
        w = codon_walk(r["L"], ht, ge)
        g.update(codons=w["codons"], mism=w["mism"], oor=w["oor"], pad=w["pad"], viol=w["viol"],
                 inreg_mism=w["inreg_mism"])
    return g


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def run(gff, seg_path, tsv, out_json, nohash=None):
    t0 = time.time()
    hs = sha256(seg_path)
    print(f"seg dump sha256 {hs} ({'as expected' if hs == SEG_SHA256 else 'NOT the expected ' + SEG_SHA256})")
    print(f"gene table sha256 {sha256(tsv)}")
    if hs != SEG_SHA256 and nohash != "nohash":
        sys.exit("segment dump hash differs; stopping")
    spec = importlib.util.spec_from_file_location("l1b", os.path.join(HERE, "l1b_t2t_dnds.py"))
    L1B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(L1B)
    txs, counts = L1B.load_annotation(gff)
    by_tid = {r["tid"]: r for r in txs}
    rows = load_tsv(tsv)
    recs = []
    missing = 0
    with gzip.open(seg_path, "rt") as fh:
        for line in fh:
            d = json.loads(line)
            r = by_tid.get(d["tid"])
            if r is None:
                missing += 1
                continue
            recs.append(analyse_gene(r, d["human"], d["segs"], rows.get(d["tid"])))
    res = summarise(recs)
    res["seg_sha256"] = hs
    res["tid_not_in_annotation"] = missing
    res["seconds"] = time.time() - t0
    with open(out_json, "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    print(f"transcripts in the dump not found in the annotation: {missing}; {res['seconds']:.0f} s")
    report(res)


# ---------------------------------------------------------------- selftest (synthetic)
def _one(L, strand, cds, segs, human=None):
    human = human or "".join(random.Random(1).choice("ACGT") for _ in range(L))
    ge = gene_events(L, strand, cds, segs)
    w = codon_walk(L, revcomp(human) if strand == "-" else human, ge)
    return ge, w


def selftest():
    rng = random.Random(7)
    L = 30
    h = "".join(rng.choice("ACGT") for _ in range(L))
    one = [(100, 130)]
    row = lambda c, st=0, src="chrS", sd="+": [[src, sd, st, c]]
    # 1 no gap
    ge, w = _one(L, "+", one, [[0, h, row(h)]], h)
    assert ge["events"] == [] and w["oor"] == 0 and w["viol"] == 0
    # 2 internal 1-base deletion at 9: frame shift from codon 3 on, last codon is padding
    ge, w = _one(L, "+", one, [[0, h, row(h[:9] + "-" + h[10:])]], h)
    assert ge["events"] == [(9, -1, "del_fs")], ge["events"]
    assert w["oor"] == 7 and w["pad"] == 1 and w["codons"] == {"del_fs|frame_shift": 6, "del_fs|pad": 1}, w
    # 3 internal 3-base deletion: whole-codon shift
    ge, w = _one(L, "+", one, [[0, h, row(h[:9] + "---" + h[12:])]], h)
    assert ge["events"] == [(9, -3, "del_3")] and w["codons"] == {"del_3|codon_shift": 6, "del_3|pad": 1}, w
    # 4 chimp-only insertion of 3 after base 11
    ge, w = _one(L, "+", one, [[0, h[:12] + "---" + h[12:], row(h[:12] + "AAA" + h[12:])]], h)
    assert ge["events"] == [(12, 3, "ins_3")] and w["codons"] == {"ins_3|codon_shift": 6}, (ge["events"], w)
    # 5 deletion split by a block boundary, chimp row contiguous: joined (1 + 2 = 3, in frame)
    segs = [[0, h[:10], row(h[:9] + "-", 500)], [10, h[10:], row("--" + h[12:], 509)]]
    ge, w = _one(L, "+", one, segs, h)
    assert ge["events"] == [(9, -3, "del_3")], ge["events"]
    # 6 same, chimp row not contiguous: hole_break (two events)
    segs = [[0, h[:10], row(h[:9] + "-", 500)], [10, h[10:], row("--" + h[12:], 900)]]
    ge, w = _one(L, "+", one, segs, h)
    assert [e[2] for e in ge["events"]] == ["hole_break", "hole_break"], ge["events"]
    #   and a switch of chimp sequence with no gap changes no offset but is flagged
    segs = [[0, h[:10], row(h[:10], 500)], [10, h[10:], row(h[10:], 0, "chrOther")]]
    ge, w = _one(L, "+", one, segs, h)
    assert ge["events"] == [] and ge["flags"]["switch"] == 1 and w["oor"] == 0
    # 7 block without chimp row; 8 uncovered human bases
    segs = [[0, h[:9], row(h[:9], 500)], [9, h[9:15], []], [15, h[15:], row(h[15:], 515)]]
    ge, w = _one(L, "+", one, segs, h)
    assert ge["events"] == [(9, -6, "hole_norow")] and w["oor"] == 7 and w["viol"] == 0, (ge["events"], w)
    hn = h[:9] + "NNNNNN" + h[15:]
    segs = [[0, h[:9], row(h[:9], 500)], [15, h[15:], row(h[15:], 515)]]
    ge, w = _one(L, "+", one, segs, hn)
    assert ge["events"] == [(9, -6, "hole_noblock")], ge["events"]
    segs = [[0, h[:9], row(h[:9], 500)], [9, h[9:15], row("------", 509)], [15, h[15:], row(h[15:], 515)]]
    ge, w = _one(L, "+", one, segs, h)
    assert ge["events"] == [(9, -6, "hole_rowempty")], ge["events"]
    # 9 gap at an exon edge (two exons of 15)
    two = [(100, 115), (200, 215)]
    segs = [[0, h[:15], row(h[:15], 500)], [15, h[15:], row("--" + h[17:], 700)]]
    ge, w = _one(L, "+", two, segs, h)
    assert ge["events"] == [(15, -2, "edge_exon")], ge["events"]
    # 10 minus strand: deletion of genomic base 27 hits the transcript's first codon; of base 0 only its last
    ge, w = _one(L, "-", one, [[0, h, row(h[:27] + "-" + h[28:])]], h)
    assert ge["events"] == [(2, -1, "del_fs")] and w["oor"] == 10 and w["viol"] == 0, (ge["events"], w)
    ge, w = _one(L, "-", one, [[1, h[1:], row(h[1:])]], "N" + h[1:])
    assert ge["events"] == [(29, -1, "hole_noblock")] and w["oor"] == 1 and w["pad"] == 1, (ge["events"], w)
    # 11 list order not genomic
    segs = [[10, h[10:], row(h[10:], 510)], [0, h[:10], row(h[:10], 500)]]
    ge, w = _one(L, "+", one, segs, h)
    assert not ge["ordered"]
    # 12 offset returns to 0: deletion of base 6, insertion of one base after base 11
    hs_ = h[:12] + "-" + h[12:]
    cs_ = h[:6] + "-" + h[7:12] + "A" + h[12:]
    ge, w = _one(L, "+", one, [[0, hs_, row(cs_)]], h)
    assert [e[2] for e in ge["events"]] == ["del_fs", "ins_fs"] and w["oor"] == 2 and w["viol"] == 0, (ge, w)
    # 13 random alignments, both strands, several blocks: in-register codons must equal the column-paired codons
    nviol = ncheck = 0
    for trial in range(400):
        Lr = 3 * rng.randrange(20, 80)
        hh = "".join(rng.choice("ACGT") for _ in range(Lr))
        cuts = sorted(rng.sample(range(1, Lr), rng.randrange(0, 4)))
        segs = []
        cpos = 1000
        for a, b in zip([0] + cuts, cuts + [Lr]):
            rs, cs = [], []
            for ch in hh[a:b]:
                u = rng.random()
                if u < 0.04 and rs:
                    rs.append(ch)
                    cs.append("-")
                elif u < 0.07 and rs:
                    rs.append("-")
                    cs.append(rng.choice("ACGT"))
                    rs.append(ch)
                    cs.append(ch)
                else:
                    rs.append(ch)
                    cs.append(ch if rng.random() > 0.02 else rng.choice("ACGT"))
            cs = "".join(cs)
            if rng.random() < 0.1:
                rows = []
            else:
                rows = row(cs, cpos)
            cpos += len(cs) - cs.count("-") + (0 if rng.random() < 0.7 else 50)
            if rng.random() < 0.9:
                segs.append([a, "".join(rs), rows])
        strand = rng.choice("+-")
        ge, w = _one(Lr, strand, [(0, Lr)], segs, hh)
        assert ge["ordered"]
        nviol += w["viol"]
        ncheck += w["inreg"]
        net = sum(e[1] for e in ge["events"])
        assert len(ge["x1"]) == Lr + net, (len(ge["x1"]), Lr, net)
    assert nviol == 0 and ncheck > 1000, (nviol, ncheck)
    # 14 summarise on a toy set
    recs = []
    for i, (cls, ex) in enumerate((("del_fs", 50.0), ("hole_norow", 30.0), (None, 0.0))):
        rowd = {f"{v}_{k}": 1.0 for v in ("V0", "X1") for k in ("S", "N", "Sd", "Nd", "s1", "n1")}
        rowd.update({"V0_S": 100.0, "V0_N": 300.0, "X1_S": 100.0, "X1_N": 300.0, "X1_Nd": 1.0 + ex})
        recs.append(dict(tid=str(i), L=300, ordered=True, flags=dict(switch=0, backstep=0, overlap=0),
                         n_events=int(cls is not None), first=cls, coarse=[COARSE[cls]] if cls else [],
                         ev_counts={cls: (1, 1)} if cls else {}, codons={}, mism={}, oor=0, pad=0, viol=0,
                         inreg_mism=0, in_tsv=True, affected=ex > 0, excess=ex, **rowd))
    res = summarise(recs)
    assert res["n_affected"] == 2 and abs(res["first_cause"]["del_fs"]["excess_share"] - 0.625) < 1e-9
    assert abs(res["criteria"]["day_hole_excess_share"] - 0.375) < 1e-9
    report(res)
    print(f"selftest OK ({ncheck} in-register codons checked against column pairing, 0 violations)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "selftest":
        selftest()
    elif len(a) in (5, 6) and a[0] == "run":
        run(*a[1:])
    else:
        print(__doc__)
