"""L1 POST HOC (labelled post hoc: designed after reading raw/l1_dnds.out and raw/l1_posthoc_mixture.out; committed
BEFORE this script is run). Question: does an exon-level reading-frame error -- the kind a whole-genome extraction
that rebuilds CDS from per-exon aligned positions can make -- reproduce Day's three numbers at once?
  Day (Q172-Q175, post body): pooled dN/dS 0.80; single-SNV codons 71.6% nonsynonymous; the strict stack (incl.
  'no stop codons in either species') leaves 10 genes (dN/dS 0.64).
Why: the L1 main run found that a frame error on ~80% of genes (mixture) reproduces 0.80 AND ~72% together, but a
gene-level mixture leaves ~5,000 stop-free genes, not ~10. An error inside genes (some exons out of frame in nearly
every multi-exon gene) would leave almost no stop-free gene.

Run (builder, 1 process, streams; < 500 MB):
  research/.venv/bin/python -I research/checks/l1_posthoc_exon.py EXONNUC_GZ OUT_JSON
Input: UCSC hg38 multiz30way alignments/knownCanonical.exonNuc.fa.gz (fetched 2026-10-11 into its own dir,
sha256 6196fa5b...b050970a). Headers: '>TX_species_k_n len frameStart frameEnd chr:start-end strand'; exons are in
transcript order and orientation (read from the file's first records; not executed).
Variants (applied to both species; the estimator and counters are imported from l1_dnds_genesets.py by path):
  X0  correct: concatenate exons in transcript order (should equal L1 V0 up to exon-boundary handling).
  E1  per-exon frame restart: each exon is read in triplets from its own first base; the len % 3 remainder of each
      exon is dropped (phase ignored).
  E2  genomic exon order: for minus-strand genes the exons are concatenated in ascending genomic order (reverse of
      transcript order) while each exon keeps transcript orientation; then read as one CDS.
  E3  E1 for minus-strand genes only.
PREDICTIONS (post hoc, fixed before the run):
  E1: pooled JC dN/dS 0.60-0.95; single-diff nonsyn share 65-75%; genes stop-free in both species < 10% of genes;
      full stack S+G+M+L+O keeps < 1% of genes.  If all three hold, E1 is a candidate that reproduces Day's pooled
      value, his single-SNV share and the near-empty strict stack together (reproduction rule as in L1: pooled in
      0.70-0.90 AND share in 66-77%).
  E2: pooled 0.35-0.65 (only multi-exon minus-strand genes broken).
  E3: pooled 0.35-0.65.
  X0: within 0.01 of L1 V0 ALL (0.271).
A hit is evidence for a class of pipeline error, not proof of what Day's code did: only his code or per-gene table
can show that (Q176's promised release).
"""
import gzip
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("l1", os.path.join(HERE, "l1_dnds_genesets.py"))
L1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L1)


def parse(path):
    """yield (tx, strand, [(start, h_exon, c_exon)...]) in transcript order."""
    cur = None
    ex = {}
    meta = {}
    sp = key = None
    buf = []

    def put():
        if key is not None:
            ex.setdefault(key, {})[sp] = "".join(buf)

    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(">"):
                put()
                buf = []
                head = line[1:].split()
                parts = head[0].split("_")
                tx, sp, k = parts[0], parts[1], int(parts[2])
                if tx != cur:
                    if cur is not None:
                        yield cur, meta.get("strand", "?"), [(meta[i], ex[i].get("hg38"), ex[i].get("panTro5"))
                                                             for i in sorted(ex)]
                    cur, ex, meta = tx, {}, {}
                key = k
                if sp == "hg38":
                    loc = head[-1]
                    meta["strand"] = loc[-1]
                    meta[k] = int(loc.split(":")[1].split("-")[0])
            else:
                buf.append(line.strip())
        put()
        if cur is not None:
            yield cur, meta.get("strand", "?"), [(meta[i], ex[i].get("hg38"), ex[i].get("panTro5")) for i in sorted(ex)]


def build(exons, strand, v):
    if v == "X0":
        return "".join(e[1] for e in exons), "".join(e[2] for e in exons)
    if v == "E2":
        if strand == "-":
            ex = sorted(exons, key=lambda e: e[0])
        else:
            ex = exons
        return "".join(e[1] for e in ex), "".join(e[2] for e in ex)
    if v == "E1" or (v == "E3" and strand == "-"):
        h = c = ""
        for _, a, b in exons:
            # drop the remainder by human ungapped-length-independent alignment columns: trim columns to a multiple of 3
            n = len(a) - len(a) % 3
            h += a[:n]
            c += b[:n]
        return h, c
    return "".join(e[1] for e in exons), "".join(e[2] for e in exons)


def main(path, out):
    var = ["X0", "E1", "E2", "E3"]
    per = {v: [] for v in var}
    n = 0
    for tx, strand, exons in parse(path):
        if any(e[1] is None or e[2] is None or len(e[1]) != len(e[2]) for e in exons):
            continue
        n += 1
        for v in var:
            h, c = build(exons, strand, v)
            g = L1.gene_stats(h, c)
            per[v].append(g)
    res = {"n_genes": n}
    for v in var:
        s = L1.summarise(per[v])
        s["filters_ALL"] = L1.filter_grid(per[v])
        full = [g for g in per[v] if all(f(g) for f in L1.FILTERS.values())]
        s["full_stack"] = L1.pooled(full)
        res[v] = s
        print(f"{v}: n {s['n']} pooled {s['dnds']:.3f} raw {s['NdSd_raw']:.3f} N/S {s['NS_ratio']:.2f} "
              f"1diff share {s['single_nonsyn_share']:.3f} 1diff dnds {s['single_dnds']:.3f} "
              f"stopfree both {s['stopfree_both']} ({100 * s['stopfree_both'] / s['n']:.1f}%) "
              f"filters min {s['filters_ALL']['min']:.3f} max {s['filters_ALL']['max']:.3f} "
              f"full stack n {s['full_stack']['n']} dnds {s['full_stack'].get('dnds', float('nan')):.3f}")
    json.dump(res, open(out, "w"), indent=1, default=float)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print(__doc__)
