"""F3a: small checks on Day's s = 0.001 "empirical mean for beneficial mutations in humans from Zeng et al. 2021".

Tier: LOW-STAKES (small checks: quote/fidelity re-confirmation plus closed-form arithmetic; one combined review).
F3a is load-bearing in hierarchy.yaml; this check computes its internal verdict (pending until now) and the R1
materiality of the misread, and re-confirms the fidelity reading from the raw text.  Closed form and string
scanning only; runs locally in < 1 s.  Pre-registered: this docstring is committed before the first run.

TARGET CLAIMS: F3a (s = 0.001), F3 / F (latency), parameters.yaml selection.s_zeng_2021.

VERBATIM QUOTES (checked against local raw text)
  Day, "The Education of a Population Geneticist", blog 2026-10-01, para 15:
    "It uses Kimura’s fixation time for beneficial mutations: t ≈ (2/s) × ln(2Nₑ), at s = 0.001 (the empirical
     mean for beneficial mutations in humans from Zeng et al. 2021). This is faster than the neutral time of 4Nₑ,
     not slower."
  Zeng et al. 2021, Nat Commun 12:1164 (local text sources/raw/sources/txt/Zeng2021.txt):
    Z1 "We detect widespread signatures of negative selection in the genetic architecture across 155 complex
        traits with a predicted mean selection coefficient of ~0.001"
    Z2 "about 1% of human genome sequence are mutational targets with a mean selection coefficient of ~0.001"
    Z3 "Since we only detected signatures of negative selection in real traits, our evolutionary simulations
        focused on the models of negative selection."
    Z4 "Common diseases had a mean s of 0.0010, which was significantly higher than that of 0.0005 for physical
        measures"
Day's Q&A latency "~19,800 gens/fixation" (PLAN.md row; R5-draft F3a) uses N_e = 1e4.

WHAT EACH SIDE PREDICTS
  Day side: s = 0.001 is a human-scale value; (2/s) ln(2N_e) at it is ~19,800 generations, which is "faster than
    the neutral time of 4N_e"; so PZ does not use the slow neutral time (answering McCarthy).
  Critic side (McCarthy; parameters.yaml note; fidelity ledger): Zeng's ~0.001 is the mean |s| of trait variants
    under NEGATIVE selection, not a beneficial mean; the formula overstates latency ~2x (B0.4); and latency does
    not cap the steady-state rate (F1), so the value matters less than Day's use implies.

THIS AUDIT'S PREDICTIONS (scored in results/R4-F3a.md)
  P1  Day's para-15 sentence and Z1-Z4 are found in the raw text (exact, or after NFKC/whitespace/ligature
      normalisation).
  P2  Fidelity: every Zeng sentence giving a numeric mean selection coefficient for real traits is in a
      negative-selection context; none gives a numeric mean POSITIVE (beneficial) s estimated from data
      (positive selection appears only as a simulation parameter).  -> F3a fidelity "misread" re-confirmed.
  P3  Internal arithmetic: (2/s) ln(2N_e) at s = 0.001, N_e = 1e4 = 19,807 (Day "~19,800"): holds.
  P4  "Faster than the neutral time of 4N_e": holds at N_e = 1e4 (19,807 < 40,000).  The crossover N_e* where
      (2/s) ln(2N_e) = 4N_e at s = 0.001 lies in [4,000, 5,000]; at Day's own human N_e = 3,300 (Z18525547)
      the beneficial formula is SLOWER than 4N_e.  Para 15 states no N_e; under rule C (charitable: the Q&A's
      1e4) the sentence holds.  Scored: holds (conditional on N_e >= N_e*).
  P5  Re-confirmation of B0.4: the stochastic asymptote (2/s)(ln(4N s) + gamma) at s = 0.001, N = 1e4 is
      8,532; Day's formula overstates it by a factor in [2.2, 2.4].
  P6  R1 materiality of the misread: latency is proportional to 1/s, so any replacement s outside
      [0.0008, 0.00133] moves the 19,807 by > 25%.  Even on Zeng's own category means (0.0005-0.0010, all
      negative selection) the latency spans 19,807-39,600, and at 0.0005 the "faster than 4N_e" sentence is
      marginal (ratio in [0.95, 1.0]).  Because the repo holds no sourced human beneficial mean s, the misread's
      effect on Day's conclusions is UNDETERMINED (external stays contested); the steady-state rate does not
      depend on latency (F1), which bounds the misread's reach to latency-based arguments (F branch, D9, E2).
What would change a verdict: P2 failing (Zeng gives a beneficial mean ~0.001) would make fidelity accurate; P3
failing would make internal arithmetic-error; P4 failing at N_e = 1e4 would make the para-15 sentence a
non-sequitur against Day's own Q&A input.
"""
import hashlib
import math
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
RAW = os.path.join(ROOT, "sources", "raw")
DAY = os.path.join(RAW, "day", "blog-2026-10-01-the-education-of-a-population-geneticist.txt")
ZENG = os.path.join(RAW, "sources", "txt", "Zeng2021.txt")
GAMMA = 0.5772156649

DAYQ = ("It uses Kimura’s fixation time for beneficial mutations: t ≈ (2/s) × ln(2Nₑ), at s = 0.001 (the empirical "
        "mean for beneficial mutations in humans from Zeng et al. 2021). This is faster than the neutral time of 4Nₑ, "
        "not slower.")
ZQ = {
    "Z1": "We detect widespread signatures of negative selection in the genetic architecture across 155 complex traits "
          "with a predicted mean selection coefficient of ~0.001",
    "Z2": "about 1% of human genome sequence are mutational targets with a mean selection coefficient of ~0.001",
    "Z3": "Since we only detected signatures of negative selection in real traits, our evolutionary simulations "
          "focused on the models of negative selection.",
    "Z4": "Common diseases had a mean s of 0.0010, which was significantly higher than that of 0.0005 for physical "
          "measures",
}


POSTHOC = "--posthoc" in sys.argv  # POST HOC (after the first run): strip C0 control characters left by PDF
# extraction (Zeng2021.txt has "mean \x02s of" for the italic s); the first run's output is kept as raw/f3a.out.


def norm(s):
    if POSTHOC:
        s = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", s)
    s = unicodedata.normalize("NFKC", s)  # also expands the "fi" ligature
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s).strip()


def found(q, txt):
    return "exact" if q in txt else ("normalised" if norm(q) in norm(txt) else "NOT FOUND")


def lat(s, Ne):
    return (2 / s) * math.log(2 * Ne)


def main():
    ok = True
    day = open(DAY, encoding="utf-8").read()
    zraw = open(ZENG, "rb").read()
    zeng = zraw.decode("utf-8", "replace")
    print("## P1 quotes")
    print(f"| Day para 15 | {found(DAYQ, day)} | sha256:{hashlib.sha256(open(DAY, 'rb').read()).hexdigest()[:16]} |")
    ok &= found(DAYQ, day) != "NOT FOUND"
    for k, q in ZQ.items():
        st = found(q, zeng)
        ok &= st != "NOT FOUND"
        print(f"| {k} | {st} | sha256:{hashlib.sha256(zraw).hexdigest()[:16]} |")

    print("\n## P2 Zeng sentences with a numeric mean selection coefficient")
    z = norm(zeng)
    sents = re.split(r"(?<=[.;])\s+(?=[A-Z])", z)
    hits = [s for s in sents if re.search(r"selection coefficient|mean s of|average s\b", s, re.I)
            and re.search(r"\b0\.\d+|~0\.0", s)]
    pos_numeric = []
    for s in hits:
        neg = bool(re.search(r"negative|deleterious", s, re.I))
        pos = bool(re.search(r"positive|beneficial", s, re.I))
        print(f"- neg={neg} pos={pos}: {s[:230]}")
        if pos and not neg:
            pos_numeric.append(s)
    print(f"sentences: {len(hits)}; positive-only with a number: {len(pos_numeric)}")
    p2 = not pos_numeric
    print(f"P2 (no numeric beneficial mean from data): {p2}")
    ok &= p2

    print("\n## P3 Day's latency")
    t = lat(0.001, 1e4)
    print(f"(2/s) ln(2Ne), s=0.001, Ne=1e4: {t:.0f} (Day ~19,800): {abs(t - 19800) / 19800 < 0.01}")
    ok &= abs(t - 19800) / 19800 < 0.01

    print("\n## P4 'faster than the neutral 4Ne'")
    lo, hi = 100.0, 1e6
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        lo, hi = (mid, hi) if lat(0.001, mid) > 4 * mid else (lo, mid)
    print(f"crossover Ne* = {lo:.0f} (pred [4000, 5000]): {4000 <= lo <= 5000}")
    for Ne in (3300, 1e4, 1e5):
        print(f"  Ne={Ne:g}: beneficial {lat(0.001, Ne):.0f} vs 4Ne {4 * Ne:.0f} -> faster: {lat(0.001, Ne) < 4 * Ne}")
    ok &= 4000 <= lo <= 5000 and lat(0.001, 1e4) < 4e4

    print("\n## P5 B0.4 re-confirmation")
    asy = (2 / 0.001) * (math.log(4 * 1e4 * 0.001) + GAMMA)
    r = t / asy
    print(f"(2/s)(ln 4Ns + gamma) = {asy:.0f}; overstatement {r:.2f} (pred [2.2, 2.4]): {2.2 <= r <= 2.4}")
    ok &= 2.2 <= r <= 2.4

    print("\n## P6 R1 sensitivity")
    print(f"window keeping latency within 25%: s in [{0.001 / 1.25:.5f}, {0.001 / 0.75:.5f}]")
    for s in (0.0005, 0.0007, 0.001):
        print(f"  Zeng category s={s}: latency {lat(s, 1e4):.0f}; ratio to 4Ne(1e4) = {lat(s, 1e4) / 4e4:.3f}")
    rr = lat(0.0005, 1e4) / 4e4
    print(f"at s=0.0005 ratio in [0.95, 1.0]: {0.95 <= rr <= 1.0}")
    print(f"\nALL MECHANICAL PREDICTIONS (P1-P5) MET: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
