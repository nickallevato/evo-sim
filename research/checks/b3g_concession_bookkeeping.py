"""B3g: bookkeeping check of Day's 2026-08-27 concession ("Kimura's derivation never needed N_e").

Tier: LOW-STAKES (bookkeeping; one combined review).  B3g is load-bearing in hierarchy.yaml, but this check
moves no verdict by computation: it verifies quotes, reproduces the arithmetic, and lists which of Day's k/mu
values the concession removes and which it leaves standing.  Pure string matching and arithmetic; runs locally
in < 1 s (AGENTS.md "trivial checks").  Pre-registered: this docstring is committed before the first run.

TARGET CLAIMS: B3g (concession), B3 (umbrella of k/mu values), B3a (k = mu N/N_e), B3f (800,000 mu), B4 (clock
recalibration 200-580 kya).  Versions ledger "N vs N_e in k".

VERBATIM QUOTES (locators from the claim files; the script checks each against the local raw text)
  Q-B3g-1  Day, "The Response to the Retraction", 2026-08-27, para 2: "the derivation of Kimura's substitution
           identity never needed Nₑ on either side of the algebraic equation. Supply is 2Nμ in the census N, the
           fixation probability of a new copy is 1/(2N) in the same N, the two correctly cancel"
  Q-B3g-2  same post, para 4: "His own supply term at Nₑ = 10,000 gives 740,000 new mutations per generation;
           Kong et al. (2012) times the global birth rate gives 2.5 × 10¹¹, a factor of 330,000 — which does not
           touch his repaired algebra"
  Q-B3a    Z18525547 (2026-02-08) para 10: "k = 2Nμ × 1/(2N_{e}) = μ × (N/N_{e})"; blog 2026-02-04 para 29
           "k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)".
  Q-B4     Z18525547 para 4: "The consensus molecular clock estimate of 6–7 Mya collapses to 200–580 kya";
           para 141, eq. (7): t_actual = t_clock × 2 / [(N_h/N_e,h) + (N_c/N_e,c)].
  Q-B3f    blog 2026-04-30 para 36 (Grok, posted by Day; secondhand): "This equals 800,000 μ, not μ."
  Q-B3-1   Z18429937 para 6: "In mammals, census populations exceed diversity-derived N_{e} by 19- to 46-fold."
  Q-B3-2   Z18525262 para 4: "it yields k = 0.743μ"
  Q-B3-3   blog 2026-10-01 para 7: "gives k = 32.3μ, not k = μ."
  Q105     McCarthy thread comment 337302874, Day, 2026-09-15: "1/2Nₑ is the fixation probability for a neutral
           mutation."
  E4       Z23188201 (2026-10-06): "The fixation probability p = 1/(2N) is protected by the martingale property"
Inputs for the N/N_e values are the claim-file table (B3): human N = 50-100k, N_e = 3,300; chimp N = 300k-1M,
N_e = 33,000 (Z18525547); 800,000 = N 8e9 / N_e 1e4 (B3f); t_clock 6-7 My.  Kong mu = 1.2e-8 per site, haploid
genome 3.1e9 (claim file).

WHAT EACH SIDE PREDICTS
  Day side (2026-08-27 post, para 3-4; Z23188201): the concession withdraws only the N/N_e leg.  Day's other k/mu
    values rest on other mechanisms (Balloux-Lehmann overlap for 0.743; a rate comparison for 32.3) and stand
    or fall on their own.  The census supply arithmetic (330,000x) is correct and "does not touch" k = mu.
  Critic side (keruru 2026-08-26 "The Epicycle Was Elsewhere"; McCarthy thread): the concession removes the
    k != mu recalibration (the 15-150x and 800,000 mu figures and the 200-580 kya clock) wholesale; later
    statements restating 1/(2N_e) (Q105) are inconsistent with it.

THIS AUDIT'S PREDICTIONS (scored in results/R4-B3g.md)
  P1  Every quote above is found in its local raw text, exactly or after Unicode NFKC + whitespace
      normalisation (quotes whose raw file is absent are reported "unverified locally", not failed).
  P2  Identity: 2N mu x 1/(2N) = mu for every N; the withdrawn form 2N mu x 1/(2N_e) = (N/N_e) mu.
  P3  The N/N_e family reproduces as plain N/N_e ratios within 1%: 30.3 and 15.2 (human), 9.1-30.3 (chimp),
      800,000; and B4's 200-580 kya reproduces from eq. (7) within 5% at the corners (t_clock 6.0 x 2/(30.3 +
      30.3) and 7 x 2/(15.2 + 9.1)).  Under the concession (census N in both terms) each becomes k/mu = 1 and
      t_actual = t_clock (6-7 My): a change of 15x to 800,000x, far beyond R1's 25%, so each N/N_e value is
      removed as an ERROR-level change by its own author (rule SC does not apply: different source, later date).
  P4  0.743 and 32.3 are not N/N_e ratios of any inputs stated in their sources; the concession does not remove
      them (Day-side point).  Their own status (B3c, B3d) is unchanged by this check.
  P5  740,000 = 2 x 1e4 x 1.2e-8 x 3.1e9 within 1%; 2.5e11 / 7.4e5 = 3.4e5 within 3% of "330,000".  Implied
      census supply 2.5e11 / (2 x 37.2) = 3.4e9 new diploid genomes per generation; Day's "does not touch his
      repaired algebra" is internally consistent (k = mu is independent of N).  The 2.5e11 input itself is
      uncited (rule F: decomposition unverifiable; scored, not re-sourced).
  P6  Post-concession tension (bookkeeping only): Q105 (2026-09-15) gives 1/(2N_e) as the neutral P(fix) and
      E4 (2026-10-06) gives 1/(2N); these differ unless N = N_e.  Scored as a versions-ledger item, not an error,
      because Q105's comment draws no k/mu number from it (R1: no downstream number moves).
What would change a verdict: P3 failing (a value that is not N/N_e) would narrow the concession's reach; P4
failing (0.743 or 32.3 reducible to N/N_e) would widen it.  Neither moves B3g's own verdicts (holds / accurate /
supported); they set which B3-family values the concession removes.
"""
import hashlib
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
RAW = os.path.join(ROOT, "sources", "raw")

QUOTES = [
    ("Q-B3g-1", "day/blog-2026-08-27-the-response-to-the-retraction.txt",
     "the derivation of Kimura’s substitution identity never needed Nₑ on either side of the algebraic equation. "
     "Supply is 2Nμ in the census N, the fixation probability of a new copy is 1/(2N) in the same N, the two "
     "correctly cancel"),
    ("Q-B3g-2", "day/blog-2026-08-27-the-response-to-the-retraction.txt",
     "His own supply term at Nₑ = 10,000 gives 740,000 new mutations per generation; Kong et al. (2012) times the "
     "global birth rate gives 2.5 × 10¹¹, a factor of 330,000 — which does not touch his repaired algebra"),
    ("Q-B3a-Z", "day/zenodo-18525547.txt", "k = 2Nμ × 1/(2N_{e}) = μ × (N/N_{e})"),
    ("Q-B3a-blog", "day/blog-2026-02-04-response-to-dennis-mccarthy-round-2.txt", "k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)"),
    ("Q-B4", "day/zenodo-18525547.txt", "The consensus molecular clock estimate of 6–7 Mya collapses to 200–580 kya"),
    ("Q-B3f", "day/blog-2026-04-30-conceding-the-math.txt", "This equals 800,000 μ, not μ."),
    ("Q-B3-1", "day/zenodo-18429937.txt", "In mammals, census populations exceed diversity-derived N_{e} by 19- to 46-fold."),
    ("Q-B3-2", "day/zenodo-18525262.txt", "it yields k = 0.743μ"),
    ("Q-B3-3", "day/blog-2026-10-01-the-education-of-a-population-geneticist.txt", "gives k = 32.3μ, not k = μ."),
    ("Q105", "refresh-2026-10-09/mccarthy-comments-why/comments.json",
     "1/2Nₑ is the fixation probability for a neutral mutation."),
    ("E4", "day/zenodo-23188201.txt", "The fixation probability p = 1/(2N) is protected by the martingale property"),
]


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[{}_\\]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def strings_of(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings_of(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_of(v)


def check_quotes():
    out = []
    for qid, rel, q in QUOTES:
        p = os.path.join(RAW, rel)
        if not os.path.exists(p):
            out.append((qid, rel, "unverified locally (no raw file)", ""))
            continue
        raw = open(p, "rb").read()
        sha = hashlib.sha256(raw).hexdigest()[:16]
        txt = raw.decode("utf-8", "replace")
        if rel.endswith(".json"):
            txt = "\n".join(strings_of(json.loads(txt)))
        if q in txt:
            st = "exact"
        elif norm(q) in norm(txt):
            st = "normalised"
        else:
            st = "NOT FOUND"
        out.append((qid, rel, st, sha))
    return out


def close(a, b, tol):
    return abs(a - b) <= tol * abs(b)


def main():
    ok = True
    print("## P1 quotes")
    for qid, rel, st, sha in check_quotes():
        print(f"| {qid} | {rel} | {st} | sha256:{sha} |")
        ok &= st != "NOT FOUND"

    print("\n## P2 identity (symbolic check over a grid of N, N_e)")
    good = all(close(2 * N * 1e-8 * (1 / (2 * N)), 1e-8, 1e-12) for N in (1e2, 1e4, 3.3e3, 8e9))
    mixed = [(N, Ne, 2 * N * 1e-8 / (2 * Ne) / 1e-8) for N, Ne in ((1e5, 3300), (8e9, 1e4))]
    print(f"2N mu/(2N) = mu at all N: {good}; withdrawn (N/N_e) form: " + "; ".join(f"N={N:g}, Ne={Ne:g} -> {r:.4g}" for N, Ne, r in mixed))
    ok &= good

    print("\n## P3 N/N_e family")
    fam = [("human high (Z18525547)", 1e5 / 3300, 30.3), ("human low", 5e4 / 3300, 15.2),
           ("chimp low", 3e5 / 33000, 9.1), ("chimp high", 1e6 / 33000, 30.3), ("B3f Grok", 8e9 / 1e4, 800000)]
    for lab, val, day in fam:
        hit = close(val, day, 0.01)
        ok &= hit
        print(f"| {lab} | N/N_e = {val:.4g} | Day {day:g} | within 1%: {hit} | under concession: 1 (factor {day:g}x) |")
    young = 6.0 * 2 / (30.3 + 30.3) * 1000
    old = 7.0 * 2 / (15.2 + 9.1) * 1000
    p3b = close(young, 200, 0.05) and close(old, 580, 0.05)
    print(f"B4 eq.(7) corners: {young:.0f} kya (Day 200) and {old:.0f} kya "
          f"(Day 580); match: {p3b}. Under the concession the ratios are 1 -> t_actual = t_clock = 6-7 My "
          f"(factor {6000 / young:.1f}-{7000 / old:.1f}x).")
    ok &= p3b

    print("\n## P4 values not of N/N_e form")
    print("0.743 (Z18525262): census-history B&L ratio over four cohorts 1950-2025 (B3c); k < mu, opposite sign to N/N_e >= 1.")
    print("32.3 (blog 2026-10-01): Bergeron pedigree mu vs Yoo required rate; no derivation given (B3d); not an N/N_e ratio.")
    print("Not removed by the concession: True (classification from the stated bases; both keep their own B3c/B3d status).")

    print("\n## P5 Day's census-supply arithmetic")
    g = 1.2e-8 * 3.1e9
    sup = 2 * 1e4 * g
    fac = 2.5e11 / 7.4e5
    print(f"haploid genome mu = {g:.1f}; 2 x 1e4 x {g:.1f} = {sup:.4g} (Day 740,000; within 1%: {close(sup, 7.4e5, 0.01)}); "
          f"2.5e11 / 7.4e5 = {fac:.4g} (Day 330,000; within 3%: {close(fac, 3.3e5, 0.03)}); implied census genomes per "
          f"generation = {2.5e11 / (2 * g):.3g}")
    ok &= close(sup, 7.4e5, 0.01) and close(fac, 3.3e5, 0.03)

    print("\n## P6 post-concession tension")
    print("Q105 (2026-09-15) neutral P(fix) = 1/(2N_e); E4 (2026-10-06) p = 1/(2N): equal only if N = N_e. "
          "Q105's comment derives no k/mu value from it -> versions ledger, not scored (R1).")
    print(f"\nALL MECHANICAL PREDICTIONS (P1-P3, P5) MET: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
