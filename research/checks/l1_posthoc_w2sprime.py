"""L1 POST HOC, EXPLORATORY, NOT PRE-REGISTERED (written after reading raw/l1_posthoc_pergene.out). Local, one
process, seconds; reads only the audit's own per-gene dump raw/l1_posthoc_pergene.tsv.gz (md5 6cecaa20...).
  research/.venv/bin/python -I research/checks/l1_posthoc_w2sprime.py research/checks/results/raw/l1_posthoc_pergene.tsv.gz
Why: W2 (chimp-only frame shift from a random codon onward, every gene) met three of the four parts of Day's triple
(pooled 0.845, share 72.7%, min over 32 stacks 0.756) and missed the fourth (full stack 1,736 genes vs Day's 10).
This prints, for W2 and for V0: the 32-stack grid with filter S' (stop codons counted INCLUDING the final codon) in
place of S, the S'-alone and S'-full-stack survivors and pooled dN/dS. No prediction; any match is a fitted,
post hoc observation about a class of pipeline behaviour, not a finding about Day's code.
"""
import gzip
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("pg", os.path.join(HERE, "l1_posthoc_pergene.py"))
PG = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PG)


def load(path, v):
    with gzip.open(path, "rt") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        idx = {k: head.index(f"{v}_{k}") for k in PG.KEYS}
        out = []
        for line in fh:
            f = line.rstrip("\n").split("\t")
            out.append({k: float(f[i]) for k, i in idx.items()})
    return out


if __name__ == "__main__":
    for v in ("V0", "W2"):
        g = load(sys.argv[1], v)
        for name, stopf in (("S", None), ("S'", PG.Sprime)):
            gr = PG.grid(g, stopf=stopf)
            print(f"{v} with {name}: alone {PG.fmt(gr['rows']['S'])}; full {PG.fmt(gr['full'])}; "
                  f"min {gr['min']:.3f} ({gr['argmin']}) max {gr['max']:.3f}")
