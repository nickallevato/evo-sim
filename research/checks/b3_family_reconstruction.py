"""B3: the k/mu family after the concession -- a pre-registered reconstruction of 32.3 and its R1 materiality.

Tier: LOAD-BEARING (B3 is a ROOT-path node, R5-draft section 1; three reviews).  Closed-form arithmetic and a
small enumeration grid (< 1,000 combinations): runs locally in < 1 s.  Pre-registered: this docstring is
committed before the first run.  It replaces the uncommitted reconstruction search recorded in the B3d claim file.

TARGET CLAIMS: B3 (umbrella; internal pending), B3d (32.3), with B3g (concession, R4-B3g) and B3c (0.743) as
inputs.  Related: A3x (bp vs events), GAP-07b / GAP-07c (measured counts), B4a (ancestral polymorphism).

VERBATIM QUOTES (checked against the local raw text)
  B3-1  Z18429937 (2026-01-29) para 6: "In mammals, census populations exceed diversity-derived N_{e} by 19- to
        46-fold."
  B3-2  Z18525262 (2026-02-08) para 4: "Applied to four generations of human census data, it yields k = 0.743μ"
  B3-3  blog 2026-10-01 para 7: "comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against
        the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ."
  B3d-2 blog 2026-05-07 para 5: "pedigree μ and phylogenetic k disagree by a median factor of 25 across 55
        vertebrates"
  A3a   MITTENS 3.0 (Z23003785) s7.1: "Apportioned symmetrically to the human lineage this yields approximately
        205 million required fixations."  (not re-checked here: its raw file is a PDF; quote verified in A3a)

INPUTS (provenance)
  Bergeron 2023 mammal mean pedigree mu 7.97e-9 per site per generation (B3d claim file; main text);
  human pedigree mu 1.2e-8 (Kong 2012, parameters.yaml; range 1.1-1.5e-8);  L = 3.1e9 (haploid; 3.0-3.2e9);
  T = 252,000 generations (B4a: 6.3 My at 25 y);  Day's count 205e6 per lineage (A3a, base pairs);
  measured: 21.05e6 events per lineage (GAP-07b, hg38 vs panTro6); about 17.8e6 FIXED events per lineage
  (GAP-07c: 205 M / fixed = 11.5); SNV-only 17.5e6 (A3b).  Ancestral N_e: 1e4 (textbook), 5.7e4 (Day's implied,
  B1d), 1.32e5 (Yoo HCG; mu rescaling open).
  Generation time 25 y is Day's/B4a's; 29 y is a SENSITIVITY value only (unsourced here; GAP-06).

WHAT EACH SIDE PREDICTS
  Day side: pedigree mu and the divergence-required rate disagree by a large factor (32.3; median 25 across 55
    vertebrates), so k = mu is falsified directly, independent of the withdrawn N/N_e leg.
  Critic side (Hancock, Nesslig20, keruru): with SNV/event counts and ancestral coalescence the ratio is of order
    1-3 (Keightley 2012: pedigree mu "about twofold lower" than divergence-based); 32.3 comes from mixing base
    pairs of structural variation with per-site point-mutation rates.

THIS AUDIT'S PREDICTIONS
  P1  B3-1, B3-2, B3-3 and B3d-2 are found in the local raw text (exact or normalised).
  P2  Reconstruction: k/mu = (count / T) / (mu x L).  The "natural" input set (205e6, 252,000, 7.97e-9, 3.1e9)
      gives 32.9, within 2% of 32.3.  On the pre-registered grid (counts {17.5e6, 20e6, 21.05e6, 205e6, 410e6},
      T {252,000, 260,000, 280,000, 325,000}, mu {7.97e-9, 1.1e-8, 1.2e-8, 1.25e-8}, L {3.0, 3.1, 3.2}e9, with and
      without halving the count), every combination within 2% of 32.3 uses a count of 205e6 or 410e6 (base-pair
      totals); none uses an SNV or event count.
  P3  R1 materiality of the count unit, holding Day's other inputs (T, Bergeron mu, L): measured events per
      lineage give 3.2-3.5; fixed events 2.7-3.0; with human mu 1.2e-8: 1.9-2.3 (events) and 1.6-2.0 (fixed).
      Each is a > 25% change (about 10-17x), so IF the 205 M base-pair count is the input (P2), the unit choice
      is error-level by R1 for the 32.3 figure.  Because Day gives no derivation (rule S/F), the score is
      conditional: "32.3 reconstructs only with the base-pair count; with measured events it is ~2-3.5".
  P4  Ancestral polymorphism (B4a): expected per-lineage divergence per site = mu T + 2 N_anc mu, so the neutral
      expectation of k_obs/mu is 1 + 2 N_anc / T = 1.08 (1e4), 1.45 (5.7e4), 2.05 (1.32e5).  The measured-events
      ratio with human mu (P3) divided by this lies in [0.9, 2.2] for every N_anc: the residual is of order the
      "twofold" pedigree-vs-phylogenetic gap (Keightley), not 32x.  At 29 y (sensitivity) T = 217,000 and the
      residual rises by 252/217 = 1.16x.
  P5  Family bookkeeping (Day's in-force human k/mu values, same quantity read per generation): 0.743 (Z18525262,
      unrevised), 32.3 (blog 2026-10-01) and k = mu inside the identity (B3g, 2026-08-27).  The span 0.743-32.3 is
      43x with opposite signs.  Under rule C they measure different windows (0.743 a modern four-cohort census
      transient, B3c; 32.3 a 6-My lineage average), so this is a versions-ledger inconsistency in direction, not
      scored as a non-sequitur.
  P6  The "median factor of 25 across 55 vertebrates" (05-07) cites no source: rule F, unverifiable; not computed.
What would change a verdict: P2 failing (32.3 reachable from an event or SNV count with natural inputs) would
remove the unit-error reading and leave 32.3 an unverified but coherent figure; P4 residual >= 5 would support
Day's "k = mu falsified directly" at a magnitude the critics deny.
"""
import itertools
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
DAY = os.path.join(ROOT, "sources", "raw", "day")
QUOTES = [
    ("B3-1", "zenodo-18429937.txt", "In mammals, census populations exceed diversity-derived N_{e} by 19- to 46-fold."),
    ("B3-2", "zenodo-18525262.txt", "Applied to four generations of human census data, it yields k = 0.743μ"),
    ("B3-3", "blog-2026-10-01-the-education-of-a-population-geneticist.txt",
     "comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate "
     "from Yoo et al. (2025) gives k = 32.3μ, not k = μ."),
    ("B3d-2", "blog-2026-05-07-a-retraction-and-a-revision.txt",
     "pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates"),
]


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("’", "'")
    s = re.sub(r"[{}_\\]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def kmu(count, T, mu, L):
    return (count / T) / (mu * L)


def main():
    ok = True
    print("## P1 quotes")
    for qid, fn, q in QUOTES:
        t = open(os.path.join(DAY, fn), encoding="utf-8").read()
        st = "exact" if q in t else ("normalised" if norm(q) in norm(t) else "NOT FOUND")
        print(f"| {qid} | {fn} | {st} |")
        ok &= st != "NOT FOUND"

    print("\n## P2 reconstruction of 32.3")
    nat = kmu(205e6, 252000, 7.97e-9, 3.1e9)
    print(f"natural set: {nat:.2f} (within 2% of 32.3: {abs(nat - 32.3) / 32.3 <= 0.02})")
    ok &= abs(nat - 32.3) / 32.3 <= 0.02
    counts = (17.5e6, 20e6, 21.05e6, 205e6, 410e6)
    hits = []
    for c, T, mu, L, half in itertools.product(counts, (252000, 260000, 280000, 325000), (7.97e-9, 1.1e-8, 1.2e-8, 1.25e-8),
                                               (3.0e9, 3.1e9, 3.2e9), (False, True)):
        v = kmu(c / (2 if half else 1), T, mu, L)
        if abs(v - 32.3) / 32.3 <= 0.02:
            hits.append((c, T, mu, L, half, v))
    for h in hits:
        print(f"  hit: count {h[0]:.4g}{' /2' if h[4] else ''}, T {h[1]}, mu {h[2]:.3g}, L {h[3]:.2g} -> {h[5]:.2f}")
    p2 = bool(hits) and all(h[0] in (205e6, 410e6) for h in hits)
    print(f"grid size {len(counts) * 4 * 4 * 3 * 2}; hits {len(hits)}; all hits use a bp total: {p2}")
    ok &= p2

    print("\n## P3 R1: count unit, Day's other inputs held")
    rows = [("events (GAP-07b)", 21.05e6, 7.97e-9, (3.2, 3.5)), ("fixed events (GAP-07c)", 17.8e6, 7.97e-9, (2.7, 3.0)),
            ("events, human mu", 21.05e6, 1.2e-8, (1.9, 2.3)), ("fixed, human mu", 17.8e6, 1.2e-8, (1.6, 2.0))]
    res = {}
    for lab, c, mu, (lo, hi) in rows:
        v = kmu(c, 252000, mu, 3.1e9)
        res[lab] = v
        hit = lo <= v <= hi
        ok &= hit
        print(f"| {lab} | {v:.2f} | pred [{lo}, {hi}] | {hit} | 32.3 / this = {32.3 / v:.1f}x |")

    print("\n## P4 ancestral polymorphism and residual")
    allin = True
    for Na in (1e4, 5.7e4, 1.32e5):
        exp_ratio = 1 + 2 * Na / 252000
        for lab in ("events, human mu", "fixed, human mu"):
            r = res[lab] / exp_ratio
            allin &= 0.9 <= r <= 2.2
            print(f"N_anc {Na:g}: neutral expectation {exp_ratio:.2f}; {lab}: residual {r:.2f} (x1.16 at 29 y: {r * 252 / 217:.2f})")
    print(f"P4 residuals in [0.9, 2.2]: {allin}")
    ok &= allin

    print("\n## P5 family span")
    print(f"0.743 (k<mu) to 32.3 (k>mu): span {32.3 / 0.743:.1f}x, opposite signs; plus k = mu (B3g). Versions ledger, rule C.")
    print("\n## P6: 'median factor of 25 across 55 vertebrates' -- no source cited; rule F, not computed.")
    print(f"\nALL MECHANICAL PREDICTIONS (P1-P4) MET: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
