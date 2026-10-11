"""L1: human-chimp dN/dS on two gene sets, and which method reproduces Day's 0.80 (Q172-Q176).
Tier: load-bearing candidate? No. Q172-Q177 sit under ROOT-FM / A2e as a NEW Day data claim; this check tests the
gene-set hypothesis Day himself proposed (Q176) and the unstated method. Low-stakes tier (one combined review) unless
a reviewer promotes it. Pre-registered: committed BEFORE the main run.

Run (on builder or na-workhorse, 1 process, < 800 MB; streams the input):
  research/.venv/bin/python -I research/checks/l1_dnds_genesets.py run PROTNUC_GZ ORTH_TSV TX2GENE_TSV OUT_JSON
Inputs (public; each fetched into its own new dir under sources/raw/, gitignored; never executed):
  PROTNUC_GZ  UCSC hg38 multiz30way alignments/knownCanonical.protNuc.fa.gz (GENCODE-based knownCanonical CDS,
              human-frame codon alignment incl. panTro5), fetched 2026-10-11, sha256 70d3dc76...0aac02
  ORTH_TSV    Ensembl BioMart, human genes x chimp homolog gene / orthology type (fetched 2026-10-11)
  TX2GENE_TSV Ensembl BioMart, human gene id x transcript id x biotype (fetched 2026-10-11)
Limitations fixed in advance: hg38 vs panTro5 (not T2T, Day used T2T + GENCODE v46); the Ensembl one2one set
(~17k protein-coding genes) is an analogue of, not the Consortium's 13,454 list; one codon alignment per gene
(knownCanonical), so paralog mis-projection in a whole-genome T2T extraction is not reproduced here (queued: L1b).

DAY's STATEMENTS (quotes-day.md Q172-Q177; post body ¶ in the quote file):
  "dN/dS = 0.80." on "20,400 protein-coding genes" (GENCODE v46, Nei-Gojobori, T2T aligned positions);
  "Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for single-SNV codons alone."
  "No combination of quality filters moves the number below 0.65" ... "dN/dS = 0.64 on 10 remaining genes"
  (strict stack: no stop codons in either species, low gap frequency, minimum substitution count, length, outliers).
  Q176: Consortium 13,454-gene list ~0.23 and complete set ~0.80 would mean the 0.23 is a gene-set artefact.
  Implied by Day's own two numbers (arithmetic, not a measurement): N_sites/S_sites = (71.6/28.4)/0.71 = 3.55.

METHODS COMPUTED (each a candidate for what Day did; same parser, same codons):
  Estimator per gene: Nei-Gojobori 1986 sites (stop changes counted nonsynonymous, N = 3 - S), pathway-averaged
  differences for multi-hit codons (pathways through stop codons excluded), codons with gap/N or a stop in either
  species skipped. pN = Nd/N, pS = Sd/S; Jukes-Cantor d = -3/4 ln(1 - 4p/3).
  Aggregation: (a) pooled ratio of totals (JC and raw p); (b) mean of per-gene ratios (dS > 0), uncapped and with
  per-gene dN/dS > 2 removed; (c) median per-gene ratio; (d) raw count ratio Nd/Sd with no site normalisation.
  Frame variants (an extraction error is applied to BOTH species, then codons are read in triplets from the start):
  V0 correct; F1/F2 frame offset +1/+2 for every gene; RCm reverse-complement minus-strand genes (genomic + order,
  as if strand were ignored); Rm reversed (no complement) minus-strand genes; RCa reverse-complement every gene.
  Gene sets: ALL (every knownCanonical gene with a panTro5 row), O121 (Ensembl ortholog_one2one), NON121 (the rest),
  O121q (O121 plus CSAC-like quality: no internal chimp stop, <= 5% gapped codons, >= 300 bp).
  Filter stack (Day's list, thresholds fixed here): S no internal stop in either species; G <= 5% gapped codons;
  M >= 5 differences (Nd+Sd); L >= 300 bp; O per-gene dN/dS <= 2 (genes with dS = 0 kept unless O); all 32 combos.
  Diagnostics per variant: single-difference-codon nonsyn share and single-diff dN/dS; site ratio N/S; number of
  genes with no internal stop in both species; survivors of the full stack S+G+M+L+O and their pooled dN/dS.
  Q176 arithmetic: the pooled dN/dS that NON121 genes would need (at their observed pS and site share) for ALL to
  reach 0.80, given O121 as observed.

PREDICTIONS (fixed now; nothing below has been computed on these data)
  Day side (Q176 gene-set hypothesis): O121 / O121q pooled ~0.23 and ALL pooled ~0.80 (>= 0.65) under V0;
    single-diff nonsyn share ~72% on ALL.
  Critic side (standard result): V0 O121 pooled JC dN/dS in 0.20-0.30; ALL pooled <= 0.35; ALL/O121 <= 1.3;
    single-diff nonsyn share 35-50%; every filter combination on V0 ALL stays below 0.40; the Q176 test fails for Day
    (gene set cannot carry 0.23 -> 0.80; the required NON121 dN/dS exceeds 1.5 or is impossible).
  Audit (derivation of the unstated; pre-registered so it can fail):
    D1 V0 site ratio N/S in 2.8-3.3 (so Day's implied 3.55 is not a correct-frame NG site ratio).
    D2 raw Nd/Sd on V0 ALL in 0.6-0.9: a missing site normalisation alone could give ~0.8 on the full set, but it
       would then give the same ~0.7-0.8 on O121 and a single-diff nonsyn share of 35-50%, not 71.6%.
    D3 mean of per-gene ratios on V0 ALL in 0.30-0.60 (above pooled, below 0.80).
    D4 every frame-error variant (F1, F2, RCa) gives pooled dN/dS in 0.7-1.2 and a single-diff nonsyn share of
       60-80%, and leaves < 5% of genes free of internal stops in both species; RCm/Rm (half the genes broken) give
       pooled 0.45-0.85.
    D5 V0 leaves > 80% of ALL genes stop-free in both species, so the full stack keeps thousands of genes, not ~10.
  Reproduction rule (fixed): a method "reproduces Day" if pooled dN/dS is in 0.70-0.90 AND single-diff nonsyn share
    is in 66-77%; "partly" if exactly one holds. Rule C: the charitable reading (a real gene-set effect) is scored by
    the Q176 arithmetic row and by NON121 pooled dN/dS.
"""
import gzip
import itertools
import json
import math
import statistics
import sys
import time

BASES = "TCAG"
AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODE = {a + b + c: AA[16 * i + 4 * j + k] for i, a in enumerate(BASES) for j, b in enumerate(BASES)
        for k, c in enumerate(BASES)}
COMP = str.maketrans("ACGTacgtNn-", "TGCAtgcaNn-")


def syn_sites(c):
    s = 0.0
    for p in range(3):
        for b in "ACGT":
            if b == c[p]:
                continue
            m = c[:p] + b + c[p + 1:]
            if CODE[m] == CODE[c]:
                s += 1.0 / 3.0
    return s


SITES = {c: syn_sites(c) for c in CODE if CODE[c] != "*"}


def pair_diffs(c1, c2):
    pos = [i for i in range(3) if c1[i] != c2[i]]
    if not pos:
        return 0.0, 0.0
    tot_s = tot_n = 0.0
    npaths = 0
    for order in itertools.permutations(pos):
        cur = c1
        s = n = 0
        ok = True
        for p in order:
            nxt = cur[:p] + c2[p] + cur[p + 1:]
            if CODE[nxt] == "*":
                ok = False
                break
            if CODE[nxt] == CODE[cur]:
                s += 1
            else:
                n += 1
            cur = nxt
        if ok:
            tot_s += s
            tot_n += n
            npaths += 1
    if npaths == 0:  # every path passes a stop: split evenly (rare)
        return len(pos) / 2.0, len(pos) / 2.0
    return tot_s / npaths, tot_n / npaths


DIFF = {}
SENSE = [c for c in CODE if CODE[c] != "*"]
for a in SENSE:
    for b in SENSE:
        DIFF[(a, b)] = pair_diffs(a, b)


def jc(p):
    x = 1 - 4.0 * p / 3.0
    return -0.75 * math.log(x) if x > 0 else float("nan")


def gene_stats(h, c):
    """h, c: aligned CDS strings (same length). Returns per-gene counts."""
    n_cod = len(h) // 3
    S = N = Sd = Nd = 0.0
    s1 = n1 = 0
    gapcod = 0
    stop_h = stop_c = 0
    for i in range(n_cod):
        a = h[3 * i:3 * i + 3].upper()
        b = c[3 * i:3 * i + 3].upper()
        last = (i == n_cod - 1)
        if "-" in b or "-" in a:
            gapcod += 1
            continue
        if a in CODE and CODE[a] == "*" and not last:
            stop_h += 1
        if b in CODE and CODE[b] == "*" and not last:
            stop_c += 1
        if a not in SITES or b not in SITES:
            continue
        sa, sb = SITES[a], SITES[b]
        S += (sa + sb) / 2.0
        N += 3.0 - (sa + sb) / 2.0
        if a != b:
            ds, dn = DIFF[(a, b)]
            Sd += ds
            Nd += dn
            if sum(1 for k in range(3) if a[k] != b[k]) == 1:
                if ds > 0:
                    s1 += 1
                else:
                    n1 += 1
    return dict(len_bp=len(h.replace("-", "")), ncod=n_cod, gapfrac=gapcod / max(n_cod, 1), stop_h=stop_h,
                stop_c=stop_c, S=S, N=N, Sd=Sd, Nd=Nd, s1=s1, n1=n1)


def transform(h, c, strand, v):
    if v == "V0":
        return h, c
    if v == "F1":
        return h[1:], c[1:]
    if v == "F2":
        return h[2:], c[2:]
    if v == "RCa" or (v == "RCm" and strand == "-"):
        return h.translate(COMP)[::-1], c.translate(COMP)[::-1]
    if v == "Rm" and strand == "-":
        return h[::-1], c[::-1]
    return h, c


VARIANTS = ["V0", "F1", "F2", "RCm", "Rm", "RCa"]


def parse_blocks(path):
    """Yield (tx, strand, hseq, cseq) per transcript; streams the gz FASTA."""
    cur = None
    strand = None
    hs = cs = None
    sp = None
    buf = []

    def flush():
        return "".join(buf)

    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(">"):
                if sp is not None:
                    seq = flush()
                    if sp == "hg38":
                        hs = seq
                    elif sp == "panTro5":
                        cs = seq
                buf = []
                head = line[1:].split()
                txsp = head[0]
                tx, _, sp = txsp.rpartition("_")
                if tx != cur:
                    if cur is not None and hs is not None:
                        yield cur, strand, hs, cs
                    cur, hs, cs = tx, None, None
                if sp == "hg38":
                    strand = head[2][-1] if len(head) > 2 else "?"
            else:
                buf.append(line.strip())
        if sp is not None:
            seq = flush()
            if sp == "hg38":
                hs = seq
            elif sp == "panTro5":
                cs = seq
        if cur is not None and hs is not None:
            yield cur, strand, hs, cs


def load_maps(orth, tx2g):
    tx = {}
    with open(tx2g) as fh:
        next(fh)
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) >= 2 and f[1]:
                tx[f[1]] = f[0]
    otype = {}
    rank = {"ortholog_one2one": 3, "ortholog_one2many": 2, "ortholog_many2many": 1}
    with open(orth) as fh:
        next(fh)
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) >= 3 and f[2]:
                if rank.get(f[2], 0) > rank.get(otype.get(f[0], ""), 0):
                    otype[f[0]] = f[2]
    return tx, otype


def pooled(gs, jcorr=True):
    S = sum(g["S"] for g in gs)
    N = sum(g["N"] for g in gs)
    Sd = sum(g["Sd"] for g in gs)
    Nd = sum(g["Nd"] for g in gs)
    if S <= 0 or N <= 0 or Sd <= 0:
        return dict(n=len(gs), dnds=float("nan"))
    pS, pN = Sd / S, Nd / N
    out = dict(n=len(gs), S=S, N=N, Sd=Sd, Nd=Nd, pN=pN, pS=pS, dnds_p=pN / pS,
               dnds=(jc(pN) / jc(pS)) if jcorr else pN / pS, NS_ratio=N / S, NdSd_raw=Nd / Sd if Sd else None)
    s1 = sum(g["s1"] for g in gs)
    n1 = sum(g["n1"] for g in gs)
    if s1 + n1:
        out["single_nonsyn_share"] = n1 / (s1 + n1)
        out["single_dnds"] = (n1 / N) / (s1 / S) if s1 else float("nan")
        out["single_codons"] = s1 + n1
    return out


def per_gene_ratio(g):
    if g["S"] <= 0 or g["N"] <= 0 or g["Sd"] <= 0:
        return None
    a, b = jc(g["Nd"] / g["N"]), jc(g["Sd"] / g["S"])
    if not (b > 0) or math.isnan(a):
        return None
    return a / b


def summarise(gs):
    out = pooled(gs)
    r = [x for x in (per_gene_ratio(g) for g in gs) if x is not None]
    out["mean_ratio"] = statistics.fmean(r) if r else None
    rc = [x for x in r if x <= 2.0]
    out["mean_ratio_cap2"] = statistics.fmean(rc) if rc else None
    out["median_ratio"] = statistics.median(r) if r else None
    out["n_ratio_genes"] = len(r)
    out["stopfree_both"] = sum(1 for g in gs if g["stop_h"] == 0 and g["stop_c"] == 0)
    out["stopfree_human"] = sum(1 for g in gs if g["stop_h"] == 0)
    return out


FILTERS = {
    "S": lambda g: g["stop_h"] == 0 and g["stop_c"] == 0,
    "G": lambda g: g["gapfrac"] <= 0.05,
    "M": lambda g: g["Nd"] + g["Sd"] >= 5,
    "L": lambda g: g["len_bp"] >= 300,
    "O": lambda g: (per_gene_ratio(g) is not None and per_gene_ratio(g) <= 2.0),
}


def filter_grid(gs):
    rows = {}
    keys = list(FILTERS)
    for r in range(len(keys) + 1):
        for combo in itertools.combinations(keys, r):
            sub = [g for g in gs if all(FILTERS[k](g) for k in combo)]
            p = pooled(sub)
            rows["+".join(combo) or "none"] = dict(n=len(sub), dnds=p.get("dnds"))
    vals = [v["dnds"] for v in rows.values() if v["n"] > 0 and v["dnds"] == v["dnds"]]
    return dict(rows=rows, min=min(vals) if vals else None, max=max(vals) if vals else None)


def required_non121(o, non, target=0.80):
    """pooled dN/dS (p-ratio) the NON121 genes need, at their observed S, N, Sd, for ALL to reach target."""
    S, N, Sd, Nd = o["S"] + non["S"], o["N"] + non["N"], o["Sd"] + non["Sd"], o["Nd"]
    need_Nd_total = target * (Sd / S) * N
    need_Nd_non = need_Nd_total - Nd
    if not non.get("Sd"):
        return float("nan")
    return (need_Nd_non / non["N"]) / (non["Sd"] / non["S"])


def run(protnuc, orth, tx2g, out):
    t0 = time.time()
    tx, otype = load_maps(orth, tx2g)
    per = {v: {"ALL": [], "O121": [], "NON121": [], "O121q": []} for v in VARIANTS}
    nmap = nmiss = ntx = nnochimp = 0
    for t, strand, h, c in parse_blocks(protnuc):
        ntx += 1
        if c is None or len(c) != len(h):
            nnochimp += 1
            continue
        g_id = tx.get(t.split(".")[0])
        if g_id is None:
            nmiss += 1
        else:
            nmap += 1
        is121 = g_id is not None and otype.get(g_id) == "ortholog_one2one"
        for v in VARIANTS:
            hh, cc = transform(h, c, strand, v)
            g = gene_stats(hh, cc)
            g["tx"] = t
            per[v]["ALL"].append(g)
            (per[v]["O121"] if is121 else per[v]["NON121"]).append(g)
            if is121 and g["stop_c"] == 0 and g["gapfrac"] <= 0.05 and g["len_bp"] >= 300 and v == "V0":
                per[v]["O121q"].append(g)
        if ntx % 2000 == 0:
            print(f"  {ntx} transcripts, {time.time() - t0:.0f} s", flush=True)
    res = dict(inputs=dict(protnuc=protnuc, orth=orth, tx2gene=tx2g), n_transcripts=ntx, no_chimp_row=nnochimp,
               tx_mapped=nmap, tx_unmapped=nmiss, variants={})
    for v in VARIANTS:
        d = {k: summarise(gs) for k, gs in per[v].items() if gs}
        d["filters_ALL"] = filter_grid(per[v]["ALL"])
        full = [g for g in per[v]["ALL"] if all(f(g) for f in FILTERS.values())]
        d["full_stack_ALL"] = pooled(full)
        res["variants"][v] = d
    o, non = res["variants"]["V0"]["O121"], res["variants"]["V0"]["NON121"]
    res["q176_required_non121_p_ratio"] = required_non121(o, non)
    res["q176_non121_share_of_sites"] = non["N"] / (o["N"] + non["N"])
    res["seconds"] = time.time() - t0
    json.dump(res, open(out, "w"), indent=1, default=float)
    report(res)


def report(res):
    print(f"transcripts {res['n_transcripts']}, no chimp row {res['no_chimp_row']}, "
          f"mapped {res['tx_mapped']}, unmapped {res['tx_unmapped']}")
    hdr = "variant set     n      pooledJC  pooled_p  NdSd_raw  N/S   mean  mean<=2 median  1diff_nonsyn 1diff_dnds stopfree_both"
    print(hdr)
    for v, d in res["variants"].items():
        for k in ("ALL", "O121", "NON121", "O121q"):
            if k not in d:
                continue
            s = d[k]
            print(f"{v:7s} {k:7s} {s['n']:6d}  {s.get('dnds', float('nan')):.3f}    {s.get('dnds_p', float('nan')):.3f}"
                  f"     {s.get('NdSd_raw') or float('nan'):.3f}    {s.get('NS_ratio', float('nan')):.2f}  "
                  f"{s.get('mean_ratio') or float('nan'):.3f} {s.get('mean_ratio_cap2') or float('nan'):.3f}   "
                  f"{s.get('median_ratio') or float('nan'):.3f}   {s.get('single_nonsyn_share', float('nan')):.3f}"
                  f"        {s.get('single_dnds', float('nan')):.3f}      {s['stopfree_both']}")
        fg = d["filters_ALL"]
        fs = d["full_stack_ALL"]
        nz = lambda x: float("nan") if x is None else x
        print(f"        filters ALL: min {nz(fg['min']):.3f} max {nz(fg['max']):.3f}; full stack n={fs['n']} "
              f"dnds={nz(fs.get('dnds')):.3f}")
    print(f"Q176: NON121 share of N sites {res['q176_non121_share_of_sites']:.3f}; NON121 pooled p-ratio needed for "
          f"ALL = 0.80: {res['q176_required_non121_p_ratio']:.3f}")
    print(f"seconds {res['seconds']:.0f}")


if __name__ == "__main__":
    if len(sys.argv) >= 6 and sys.argv[1] == "run":
        run(*sys.argv[2:6])
    elif len(sys.argv) == 3 and sys.argv[1] == "report":
        report(json.load(open(sys.argv[2])))
    else:
        print(__doc__)
