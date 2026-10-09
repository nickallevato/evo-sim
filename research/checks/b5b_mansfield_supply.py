"""B5b -- Mansfield's supply argument with a SOURCED neutral fraction, against the GAP-07b/07c event counts.

THROWAWAY research check (queue item 2).  Pure arithmetic plus a tiny exact-identity check.  Run on na-workhorse:
    research/.venv/bin/python -I research/checks/b5b_mansfield_supply.py smoke
    research/.venv/bin/python -I research/checks/b5b_mansfield_supply.py main [workers]

TARGET CLAIMS.  B5b (Mansfield, YouTube comment under jDxFtCOGZ3A, retrieved 2026-10-07):
  "If even just 2 of these 100 are neutral - which is certainly way under the actual proportion - then in a population of size N
   there are about 2*N new neutral alleles introduced each generation."
  "So, the expectation is that there will be on average 1 neutral fixation every generation if just 2% of new mutations are neutral."
Also B5a/B5c/B5h (other critic supply counts), A3/A3x (the requirement), H8 (Day Z19984826 s6.4: "there is no independent
estimate of the neutral fraction left to invoke").  Requirements are the claim file's: 20M over 450,000 generations (2019 edition
count) and 17.5M over 252,000 generations (3.0, parameters.yaml day_2026 = Z23003785); measured events from RESULTS.md GAP-07b
(21.05M events per lineage; 42.10M both lineages) and GAP-07c (fixed events per lineage 17.2-17.9M).

INPUTS (all from the repo; none new):
  n_dn = 100 de novo per zygote (Mansfield, stated) and 76.8 = 6.4e9 x 1.2e-8 (Kong 2012 mu, parameters.yaml; Hancock's first-pass figure).
  Neutral fraction f: Mansfield 0.02 (stated, "way under"); SOURCED: Rands et al. 2014, PLoS Genet 10:e1004525, verbatim "8.2%
  (7.1-9.2%) of the human genome is presently subject to negative selection" (ledgers/gaps-review.md C16, verified), so the fraction
  NOT under negative selection is 0.918 (0.908-0.929).  That is an UPPER bound on the neutral fraction: not-constrained is not the
  same as neutral (positively selected and nearly neutral sites sit inside it), and the rate also needs the mutations at
  unconstrained sites to be as mutable as the average (CpG, repeats not modelled).
  Identity: new neutral mutations/generation = N x n_dn x f; each fixes with probability 1/(2N); rate = n_dn x f / 2 per generation
  per lineage (n_dn is per DIPLOID zygote, so 100 -> 50 per generation at f = 1; Kong's 76.8 -> 38.4, = Hancock's haploid 38.4).

WHAT IS COMPUTED.  (a) the identity check by exact enumeration at a small N; (b) supply S = rate x G for each (n_dn, f, G);
(c) ratios S/requirement for each requirement; (d) the f needed to meet each requirement; (e) for the measured events, the
"missing" fraction (the k = mu undershoot ~2x noted in GAP-07b; ancestral polymorphism, B4a).

PRE-REGISTERED PREDICTIONS (arithmetic; written before the run):
  P1  Identity: (N x 2 x 1/(2N)) = 1 exactly for all N; at f = 0.02 the supply is 1.0 per generation = 450,000 (G=450k) or 252,000.
  P2  Mansfield's own f = 0.02: 44.4x short of 20M, 69.4x short of 17.5M (claim file).  Needed f at n_dn = 100: 0.889 (20M/450k)
      and 1.389 (17.5M/252k, > 1: impossible).
  P3  With the SOURCED f = 0.918 (0.908-0.929) and n_dn = 100: supply at G = 450,000 = 20.66M (20.43-20.90M), i.e. covers 20M
      by 3.3% (2.2-4.5%); at G = 252,000 = 11.57M (11.44-11.71M), i.e. 0.66x of 17.5M (not covered).
  P4  With Kong's n_dn = 76.8 and f = 0.918: supply at 450,000 = 15.86M (0.79x of 20M); at 252,000 = 8.89M (0.51x of 17.5M).
  P5  Against the MEASURED per-lineage events (GAP-07b 21.05M; 07c fixed 17.2-17.9M) at the 3.0 generation count (252,000):
      supply 8.9M-11.6M covers 0.42-0.55x of 21.05M and 0.50-0.67x of the fixed events.  So the pure k = mu supply with the
      sourced f cannot account for the whole measured divergence at 252,000 generations; it needs the ancestral term (B4a) or a
      longer divergence time.  This is a statement about the clock/time (GAP-06), not about neutral theory.
  P6  Mansfield's illustration at f = 0.02 is correct as an identity and wrong as a magnitude; with a sourced f the magnitude
      reaches the 2019-edition requirement but not the 3.0 requirement.

WHAT EACH SIDE'S MODEL PREDICTS.
  Critics (Mansfield): "way under the actual proportion", i.e. the supply covers the requirement once the real neutral fraction
    is used.  Their model predicts covering 20M/450k but, as computed, that is the older count; at 252,000 the supply is short
    by ~1.5x (n_dn = 100) to ~2x (Kong) before any ancestral term.
  Day: k = mu requires a full pipe (B1c); his 17.5-20M are all treated as selected (Term 3).  His model predicts that even the
    maximum neutral supply cannot meet 17.5M at 252,000 generations unless nearly every site is neutral, which P3/P4 confirm for
    n_dn = 100 (needs f > 1) -- and the sourced f is an upper bound.  Day's requirement is however also not "all adaptive": the
    supply is neutral, and the claim that the requirement is ADAPTIVE is not tested here.
  RESULT THAT WOULD CHANGE A VERDICT: a sourced neutral fraction well below 0.89 (then B5b fails even at 450k), or a
    source that gives the unconstrained fraction as the neutral fraction with a positive-selection share (then P3 shrinks).

Raw output: research/checks/results/raw/b5b.out (stdout), b5b.json.
"""
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))

REQ = {"Day 20M (450k gen)": (20_000_000, 450_000), "Day 17.5M (252k gen)": (17_500_000, 252_000)}
MEASURED = {"GAP-07b events/lineage 21.05M": 21_050_000, "GAP-07c fixed events/lineage lo 17.2M": 17_200_000,
            "GAP-07c fixed events/lineage hi 17.9M": 17_900_000}
NDN = {"Mansfield 100": 100.0, "Kong 76.8": 6.4e9 * 1.2e-8}
FRAC = {"Mansfield 0.02": 0.02, "Rands lo 0.908": 0.908, "Rands mid 0.918": 0.918, "Rands hi 0.929": 0.929, "all sites 1.0": 1.0}
GENS = (252_000, 450_000)


def identity_check():
    # N zygotes x n_neutral per zygote new neutral alleles, each fixes with prob 1/(2N): rate per generation = n_neutral / 2 ... for n=2: 1.
    out = []
    for N in (10, 100, 1000, 10_000, 1_000_000):
        rate = Fraction(N * 2, 1) * Fraction(1, 2 * N)
        out.append((N, str(rate)))
        assert rate == 1
    return out


def main():
    res = {"identity": identity_check(), "supply": [], "needed_f": [], "vs_measured": []}
    print("identity (2 neutral per zygote x N zygotes x 1/(2N)):", res["identity"])
    print("\n(b,c) supply S = n_dn*f/2 * G per lineage; ratio to each requirement")
    hdr = "%-14s %-16s %8s %12s " % ("n_dn", "f", "G", "S (M)") + " ".join("%-22s" % k for k in REQ)
    print(hdr)
    for nk, n in NDN.items():
        for fk, f in FRAC.items():
            for G in GENS:
                S = n * f / 2.0 * G
                ratios = {k: S / v[0] for k, v in REQ.items()}
                res["supply"].append(dict(n_dn=nk, f=fk, G=G, S=S, ratios=ratios))
                print("%-14s %-16s %8d %12.3f " % (nk, fk, G, S / 1e6) + " ".join("%-22.3f" % r for r in ratios.values()))
    print("\n(d) f needed to meet each requirement: f = 2*R/(n_dn*G)")
    for nk, n in NDN.items():
        for rk, (R, G) in REQ.items():
            fn = 2.0 * R / (n * G)
            res["needed_f"].append(dict(n_dn=nk, req=rk, f_needed=fn))
            print("  %-14s %-22s f_needed = %.3f%s" % (nk, rk, fn, "  (> 1: impossible)" if fn > 1 else ""))
    print("\n(e) vs MEASURED events per lineage at G = 252,000 (supply/measured)")
    for nk, n in NDN.items():
        for fk in ("Rands lo 0.908", "Rands mid 0.918", "Rands hi 0.929", "all sites 1.0"):
            S = n * FRAC[fk] / 2.0 * 252_000
            row = {mk: S / mv for mk, mv in MEASURED.items()}
            res["vs_measured"].append(dict(n_dn=nk, f=fk, S=S, ratios=row))
            print("  %-14s %-16s S=%.2fM  " % (nk, fk, S / 1e6) + "  ".join("%s: %.2f" % (k.split()[0] + k.split()[-1], v) for k, v in row.items()))
    print("\nshortfall at f=0.02, n_dn=100: 20M/450k = %.1fx; 17.5M/252k = %.1fx" % (20e6 / (1.0 * 450_000), 17.5e6 / (1.0 * 252_000)))
    with open(os.path.join(HERE, "results", "raw", "b5b.json"), "w") as fh:
        json.dump(res, fh, indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "main"
    if cmd == "smoke":
        print(identity_check())
        print("smoke ok")
    else:
        main()
