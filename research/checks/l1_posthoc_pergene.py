"""L1 POST HOC (labelled post hoc: designed after the three L1 reviews, REVIEW-R4-L1-{correctness,steelman-day,
steelman-critic}.md at a352991; committed BEFORE this script is run). Per-gene dump and three questions the reviews
asked that the committed outputs cannot answer (l1_dnds.json holds only n and dN/dS per filter row).

Run (builder, 1 process, streams the input; < 800 MB):
  research/.venv/bin/python -I research/checks/l1_posthoc_pergene.py PROTNUC_GZ ORTH_TSV TX2GENE_TSV OUT_PREFIX
Writes OUT_PREFIX.json (summaries) and OUT_PREFIX.tsv.gz (per-gene counts: tx, set, strand, and for each variant
len_bp, gapfrac, stop_h, stop_c, term_h, term_c, S, N, Sd, Nd, s1, n1). Same input files and hashes as the L1 main run
(raw/l1.host). Estimator, parser and filters are imported from l1_dnds_genesets.py by path (pre-registered 868bb60).

Day's triple (Q172-Q175, post body): pooled dN/dS 0.80; single-SNV codons 71.6% nonsynonymous; "No combination of
quality filters moves the number below 0.65"; the strictest stack "still produced dN/dS = 0.64 on 10 remaining genes".
Triple-reproduction rule (fixed now): pooled 0.70-0.90 AND single-diff nonsyn share 66-77% AND min over the 32 filter
stacks >= 0.60 AND full stack (S+G+M+L+O) keeps <= 200 genes.

Q1 (correctness #2/#3): the gene-level frame-error mixture. For F1, F2, RCa on ALL, refit f so pooled = 0.80 from the
  per-gene totals (should equal raw/l1_posthoc_mixture.out: 0.812 / 0.780 / 0.842), then compute the EXPECTED 32-stack
  grid under random assignment of genes to broken (prob f) or intact (1 - f): totals and survivor counts are
  expectations, sum over genes of (1-f)*[V0 gene passes]*V0 counts + f*[variant gene passes]*variant counts.
  PREDICTION: for F1 and F2, min over stacks < 0.50; for RCa, min < 0.65; for all three, full stack keeps > 1,000
  genes (expected). If so, the gene-level mixture is contradicted by Day's own Q175 (min >= 0.65; 10 survivors).
Q2 (steelman-day #1): a terminal-stop filter convention. S' = no stop codon in either species INCLUDING the final
  codon (the L1 filter S skips the final codon). Reported on V0 ALL: genes with a terminal stop in human; survivors
  of S' alone, of S'+G+M+L+O, and their pooled dN/dS; the 16-stack grid with S' in place of S.
  PREDICTION (Day-side reading, as the reviewer stated it): V0 survivors of S' alone are 10-200 genes. Audit
  prediction alongside: >= 95% of V0 genes end in a human stop codon; the S' full stack (if non-empty with >= 5
  genes) gives pooled 0.15-0.40, i.e. the convention explains a near-empty stack but not 0.64.
Q3 (correctness #3, optional; steelman-day): a within-gene contamination class W, applied to every gene, breakpoint
  codon k drawn uniformly from 0..ncod-1 with a per-gene seed (crc32 of the transcript id):
  W1 both species: delete one base at codon k in both sequences (frame +1 downstream in both; codons still paired).
  W2 chimp only: delete one base at codon k in chimp only, pad the end with a gap (human in frame, chimp shifted
     downstream: a chimp-only frame shift after an unhandled indel).
  For each: pooled, share, stop-free genes, 32-stack min/max, full stack n and dN/dS; if pooled > 0.80, also the
  expected grid of a V0/W mixture fitted to 0.80.
  PREDICTION: W1 pooled 0.55-0.90, share 60-75%, stop-free in both < 10% of genes, full stack < 500 genes; W2 pooled
  0.60-1.00. Neither W1 nor W2 meets the full triple, because filter S (and G for W2) preferentially keeps genes whose
  breakpoint lies near the 3' end, which are mostly intact: min over stacks < 0.60 for both.
Q4 (correctness #4): V0 pooled dN/dS for O121, NON121 split into mapped-not-one2one and UNMAPPED (482 transcripts
  with no current Ensembl gene id). No prediction (descriptive).
Any hit is evidence for or against a class of pipeline behaviour, not a finding about Day's unreleased code.
"""
import gzip
import importlib.util
import itertools
import json
import os
import random
import sys
import time
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("l1", os.path.join(HERE, "l1_dnds_genesets.py"))
L1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L1)

KEYS = ("len_bp", "gapfrac", "stop_h", "stop_c", "term_h", "term_c", "S", "N", "Sd", "Nd", "s1", "n1")
VARS = ["V0", "F1", "F2", "RCa", "W1", "W2"]


def terminal(h, c):
    n = len(h) // 3
    a, b = h[3 * (n - 1):3 * n].upper(), c[3 * (n - 1):3 * n].upper()
    return int(L1.CODE.get(a) == "*"), int(L1.CODE.get(b) == "*")


def wtransform(tx, h, c, v):
    n = len(h) // 3
    k = random.Random(zlib.crc32(tx.encode())).randrange(max(n, 1))
    i = 3 * k
    if v == "W1":
        return h[:i] + h[i + 1:], c[:i] + c[i + 1:]
    return h, c[:i] + c[i + 1:] + "-"


def stats(h, c):
    g = L1.gene_stats(h, c)
    g["term_h"], g["term_c"] = terminal(h, c)
    return {k: g[k] for k in KEYS}


def pooled_w(rows):
    """rows: iterable of (weight, gene dict). Expected totals -> pooled JC dN/dS and expected n."""
    S = N = Sd = Nd = s1 = n1 = n = 0.0
    for w, g in rows:
        if w == 0:
            continue
        n += w
        S += w * g["S"]; N += w * g["N"]; Sd += w * g["Sd"]; Nd += w * g["Nd"]; s1 += w * g["s1"]; n1 += w * g["n1"]
    if S <= 0 or N <= 0 or Sd <= 0:
        return dict(n=n, dnds=None)
    d = L1.jc(Nd / N) / L1.jc(Sd / S)
    return dict(n=n, dnds=d, share=n1 / (n1 + s1) if n1 + s1 else None)


def Sprime(g):
    return g["stop_h"] + g["term_h"] == 0 and g["stop_c"] + g["term_c"] == 0


def grid(genes_a, genes_b=None, f=0.0, stopf=None):
    """Expected 32-stack grid. genes_a intact (weight 1-f), genes_b broken (weight f). stopf replaces filter S."""
    F = dict(L1.FILTERS)
    if stopf is not None:
        F["S"] = stopf
    out = {}
    keys = list(F)
    for r in range(len(keys) + 1):
        for combo in itertools.combinations(keys, r):
            rows = []
            for i, ga in enumerate(genes_a):
                if all(F[k](ga) for k in combo):
                    rows.append((1.0 - f, ga))
                if genes_b is not None and f > 0:
                    gb = genes_b[i]
                    if all(F[k](gb) for k in combo):
                        rows.append((f, gb))
            out["+".join(combo) or "none"] = pooled_w(rows)
    vals = [v["dnds"] for v in out.values() if v["dnds"] is not None and v["n"] >= 1]
    return dict(rows=out, min=min(vals), max=max(vals), argmin=min((v["dnds"], k) for k, v in out.items()
                                                                   if v["dnds"] is not None and v["n"] >= 1)[1],
                full=out["S+G+M+L+O"])


def fit_f(a, b, target=0.80):
    pa = [(1.0, g) for g in a]
    if pooled_w([(1.0, g) for g in b])["dnds"] < target:
        return None
    lo, hi = 0.0, 1.0
    for _ in range(50):
        m = (lo + hi) / 2
        d = pooled_w([(1 - m, g) for g in a] + [(m, g) for g in b])["dnds"]
        lo, hi = (m, hi) if d < target else (lo, m)
    return lo


def summary(gs):
    p = pooled_w([(1.0, g) for g in gs])
    p["stopfree_both"] = sum(1 for g in gs if g["stop_h"] == 0 and g["stop_c"] == 0)
    p["term_stop_h"] = sum(g["term_h"] for g in gs)
    p["Sprime_alone"] = sum(1 for g in gs if Sprime(g))
    return p


def main(protnuc, orth, tx2g, prefix):
    t0 = time.time()
    tx, otype = L1.load_maps(orth, tx2g)
    genes = {v: [] for v in VARS}
    sets = []
    tsv = gzip.open(prefix + ".tsv.gz", "wt")
    tsv.write("tx\tset\tstrand\t" + "\t".join(f"{v}_{k}" for v in VARS for k in KEYS) + "\n")
    for t, strand, h, c in L1.parse_blocks(protnuc):
        if c is None or len(c) != len(h):
            continue
        gid = tx.get(t.split(".")[0])
        st = "UNMAPPED" if gid is None else ("O121" if otype.get(gid) == "ortholog_one2one" else "NON121m")
        sets.append(st)
        row = []
        for v in VARS:
            hh, cc = wtransform(t, h, c, v) if v in ("W1", "W2") else L1.transform(h, c, strand, v)
            g = stats(hh, cc)
            genes[v].append(g)
            row += [f"{g[k]:.4g}" if isinstance(g[k], float) else str(g[k]) for k in KEYS]
        tsv.write(f"{t}\t{st}\t{strand}\t" + "\t".join(row) + "\n")
        if len(sets) % 4000 == 0:
            print(f"  {len(sets)} transcripts, {time.time() - t0:.0f} s", flush=True)
    tsv.close()
    res = dict(n=len(sets), seconds_parse=time.time() - t0)
    V0 = genes["V0"]
    res["sets_V0"] = {s: summary([g for g, x in zip(V0, sets) if x == s]) for s in ("O121", "NON121m", "UNMAPPED")}
    res["sets_V0"]["NON121"] = summary([g for g, x in zip(V0, sets) if x != "O121"])
    res["variants_ALL"] = {v: summary(genes[v]) for v in VARS}
    # Q1 mixture grids
    res["Q1"] = {}
    for v in ("F1", "F2", "RCa"):
        f = fit_f(V0, genes[v])
        f = 1.0 if f is None else f  # variant alone below 0.80: report it unmixed (f = 1)
        gr = grid(V0, genes[v], f)
        res["Q1"][v] = dict(f=f, min=gr["min"], argmin=gr["argmin"], max=gr["max"], full=gr["full"],
                            S_alone=gr["rows"]["S"], rows=gr["rows"])
    # Q2 terminal-stop convention
    g2 = grid(V0, stopf=Sprime)
    res["Q2"] = dict(term_stop_h=sum(g["term_h"] for g in V0), term_stop_c=sum(g["term_c"] for g in V0),
                     Sprime_alone=g2["rows"]["S"], Sprime_full=g2["full"], min=g2["min"], max=g2["max"],
                     rows=g2["rows"])
    for v in ("F1", "F2", "RCa"):
        f = res["Q1"][v]["f"]
        gm = grid(V0, genes[v], f, stopf=Sprime)
        res["Q2"]["mix_" + v] = dict(Sprime_alone=gm["rows"]["S"], Sprime_full=gm["full"], min=gm["min"])
    # Q3 within-gene class
    res["Q3"] = {}
    for v in ("W1", "W2"):
        gw = grid(genes[v])
        d = dict(summary=res["variants_ALL"][v], min=gw["min"], argmin=gw["argmin"], max=gw["max"], full=gw["full"],
                 S_alone=gw["rows"]["S"], rows=gw["rows"])
        f = fit_f(V0, genes[v])
        if f is not None:
            gm = grid(V0, genes[v], f)
            d["mix"] = dict(f=f, min=gm["min"], argmin=gm["argmin"], full=gm["full"], S_alone=gm["rows"]["S"])
        res["Q3"][v] = d
    res["seconds"] = time.time() - t0
    json.dump(res, open(prefix + ".json", "w"), indent=1, default=float)
    report(res)


def fmt(p):
    if p is None or p.get("dnds") is None:
        return f"n={0 if p is None else p['n']:.0f} dnds=nan"
    return f"n={p['n']:.0f} dnds={p['dnds']:.3f}"


def report(r):
    print(f"genes {r['n']}")
    print("Q4 V0 sets: " + "; ".join(f"{k} {fmt(v)} share={v['share']:.3f}" for k, v in r["sets_V0"].items()))
    for v, s in r["variants_ALL"].items():
        print(f"ALL {v:4s} {fmt(s)} share={s['share']:.3f} stopfree_both={s['stopfree_both']} "
              f"term_stop_h={s['term_stop_h']} Sprime_alone={s['Sprime_alone']}")
    for v, d in r["Q1"].items():
        print(f"Q1 mix {v}: f={d['f']:.3f} min={d['min']:.3f} ({d['argmin']}) max={d['max']:.3f} "
              f"S alone {fmt(d['S_alone'])}; full {fmt(d['full'])}")
    q = r["Q2"]
    print(f"Q2 V0: term stop human {q['term_stop_h']}, chimp {q['term_stop_c']}; S' alone {fmt(q['Sprime_alone'])}; "
          f"S' full {fmt(q['Sprime_full'])}; grid with S' min={q['min']:.3f} max={q['max']:.3f}")
    for v in ("F1", "F2", "RCa"):
        m = q["mix_" + v]
        print(f"Q2 mix {v}: S' alone {fmt(m['Sprime_alone'])}; S' full {fmt(m['Sprime_full'])}; min={m['min']:.3f}")
    for v, d in r["Q3"].items():
        s = d["summary"]
        print(f"Q3 {v}: {fmt(s)} share={s['share']:.3f} stopfree_both={s['stopfree_both']} min={d['min']:.3f} "
              f"({d['argmin']}) max={d['max']:.3f} S alone {fmt(d['S_alone'])}; full {fmt(d['full'])}")
        if "mix" in d:
            m = d["mix"]
            print(f"   mix f={m['f']:.3f} min={m['min']:.3f} ({m['argmin']}) S alone {fmt(m['S_alone'])}; "
                  f"full {fmt(m['full'])}")
    print(f"seconds {r['seconds']:.0f}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        main(*sys.argv[1:5])
    elif len(sys.argv) == 3 and sys.argv[1] == "report":
        report(json.load(open(sys.argv[2])))
    else:
        print(__doc__)
