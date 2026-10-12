"""R4-A2e-alpha, POST HOC addendum: Uricchio, Petrov & Enard 2019 (full text) mapped to the A2e flip.

POST HOC LABEL: the abstract value alpha = 0.135 (VIPs 0.224) was already known and mapped in
a2e_alpha_map.py (abstract only). What was NOT known when this is written: the full-text method, the table
(including HPDs for the weak/strong split) and the study's own fixation counts. The predictions below are
registered before the first run of this script, but they are post hoc relative to the abstract value.

Source: PMC6693860 (NIH author manuscript, OA), efetch XML, sha256 3e7c44cb27fb68ffbe07b4ba2884dc31c448145c93d365142643e22c5b865977
(local, gitignored: sources/raw/refresh-2026-10-11b-lit/uric/a.xml). Read as data only.

WHAT IS MAPPED (same mapping and same Day-charitable rows as a2e_alpha_map.py / the Review resolution):
  adaptive substitutions per lineage = alpha x N(nonsynonymous fixations on the human lineage), compared with
  G1 = 252000/1322 = 190.6 and G2 = 252000/1587 = 158.8. Denominators: the five used in a2e_alpha_map.py
  (N1 19,570; N1-low 14,678; N1-high 24,463; N2 11,090; N3 18,180), PLUS the paper's own count NS = 29,925
  (VIPs 6,249). Rows: point estimate; lower 95% HPD (0.096); lower HPD x 0.75 (Day-charitable: the abstract says
  linkage reduces alpha by ~25%; if 0.135 is already net of that, 0.75 is a pure charity haircut); strongly-adaptive
  component only (0.041, HPD 0.0-0.13; Day-charitable because weak variants are near-neutral in pace); VIP subset.
  Compounded lowest "any effect size" row = 0.096 x 0.75 x min denominator (N2 11,090).

CLASSIFICATION CHECK (quoted from the method text, verified as substrings by this script):
  (a) human-branch: "number of human-specific fixed substitutions in coding sequences since divergence with
      chimpanzees", "identified by parsimony" on human, chimpanzee, orangutan alignments.
  (b) bias-corrected: aMK baseline is cited as correcting slightly deleterious polymorphism; ABC-MK adds weakly
      beneficial alleles and background selection ("our method nearly doubles the estimated human adaptation rate").
  Both must hold for the milestone-13 condition.

VERDICT RULE (pre-committed in milestone 13, docs/2026-10-11-1-...md): A2e external moves from "contested,
leaning contradicted" to "contradicted" with a full-text Uricchio, or any other bias-corrected human-branch alpha
above about 1%. alpha* = 0.65-1.75%.
  BLOCKS the move if any of: (1) the estimate is not human-lineage specific (pooled with chimp or other branch);
  (2) not bias-corrected; (3) the lower HPD bound falls below alpha* (1.75%); (4) the lowest Day-charitable
  any-effect-size row is <= 191 (the flip no longer holds under charity).

PREDICTIONS (Day-side and critic-side; each stated before the run):
  P1 (critic): (a) and (b) both hold; every quote verifies.
  P2 (critic): lower HPD 0.096 / alpha*_max 1.75% >= 5; every "any effect size" row, including the compounded
     lowest (0.096 x 0.75 x 11,090 ~ 799), is >= 3.5 x G1, i.e. above 191 by >= 600.
  P3 (Day): the strongly-adaptive-only row at the lower HPD (0.0) is 0, i.e. a strong-only reading is NOT excluded
     by this paper; the strong-only POINT (0.041) is above G1 on every denominator (>= 450 for N2). So a strong-only
     reading is a point-estimate clearance only (not an interval clearance).
  P4 (Day): the paper's own NS = 29,925 exceeds the A2e-alpha denominators (11,090-24,463) and is not reconciled
     with them in the text read; the own-count rows (4,040 point) are therefore NOT used for the verdict (reported only).
  P5 (verdict): the move to "contradicted" is proposed, on the N1-N3 denominators and the lower HPD, for the
     coding-only, any-effect-size per-generation reading. It does not claim anything about a strong-only reading
     or about Day's other A2e arguments.
"""
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
P = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-11b-lit", "uric", "a.xml")
QUOTES = [
    "number of human-specific fixed substitutions in coding sequences since divergence with chimpanzees",
    "Fixed substitutions were identified by parsimony based on alignments of human (hg19 assembly), chimpanzee (panTro4 assembly) and orangutan (ponAbe2 assembly) coding sequences",
    "estimate α = 0.135 in human protein-coding sequences, 72% of which is contributed by weakly-adaptive variants",
    "We show that in this adaptation regime α is reduced ≈ 25% by linkage genome-wide",
    "Deleterious polymorphism effectively makes the test overly conservative",
    "while our method nearly doubles the estimated human adaptation rate (to α ^ = 0.135 )",
    "Values in parentheses represent the area of 95% highest posterior density",
    "29925 38135 0.135 (0.096,0.17) 0.097 (0.0,0.21) 0.041 (0.0,0.13) VIPs 6249 10309 0.224 (0.17,0.28) 0.098 (0.0,0.24) 0.126 (0.018,0.26)",
    "for all 661 samples with African ancestry",
]


def norm(s):
    s = re.sub(r"<[^>]+>", " ", s).replace("&amp;", "&").replace(" ", " ")
    return re.sub(r"\s+", " ", s)


def main():
    b = open(P, "rb").read()
    t = norm(b.decode("utf-8", "replace"))
    print("sha256", hashlib.sha256(b).hexdigest())
    ok = True
    for q in QUOTES:
        f = norm(q) in t
        ok &= f
        print("  %s %s" % ("OK  " if f else "MISS", q[:100]))
    print("all quotes verified:", ok)

    G1, G2 = 252000 / 1322, 252000 / 1587
    D = {"N1 19,570": 19570, "N1-low 14,678": 14678, "N1-high 24,463": 24463, "N2 11,090": 11090,
         "N3 18,180": 11090 / 0.61}
    print("\nG1 %.1f  G2 %.1f   alpha* range 0.65-1.75%%; lower HPD 0.096 / 0.0175 = %.1f x" % (G1, G2, 0.096 / 0.0175))
    rows = [("point 0.135", 0.135), ("lower HPD 0.096", 0.096), ("lower HPD x 0.75 (charity)", 0.096 * 0.75),
            ("strong-only point 0.041", 0.041), ("strong-only lower HPD 0.0", 0.0), ("strong-only upper HPD 0.13", 0.13),
            ("point x 0.75", 0.135 * 0.75)]
    print("\n| row | denominator | count | x G1 | x G2 | side (G1) |")
    print("|---|---|---|---|---|---|")
    for name, a in rows:
        for dn, n in D.items():
            c = a * n
            print("| %s | %s | %.0f | %.2f | %.2f | %s |" % (name, dn, c, c / G1, c / G2, "critic" if c > G1 else "NOT above"))
    lo = 0.096 * 0.75 * min(D.values())
    print("\nCompounded lowest any-effect-size row: 0.096 x 0.75 x 11,090 = %.0f  (%.2f x G1, %.2f x G2)" % (lo, lo / G1, lo / G2))
    print("Strong-only point on N2: %.0f (%.2f x G1); strong-only lower HPD: 0" % (0.041 * 11090, 0.041 * 11090 / G1))
    print("\nPaper's own counts (NOT used for the verdict; denominator unreconciled with N1-N3):")
    NS, VNS = 29925, 6249
    for name, a, n in [("all genes point", 0.135, NS), ("all genes lower HPD", 0.096, NS), ("all genes lower HPD x 0.75", 0.072, NS),
                       ("all genes strong-only point", 0.041, NS), ("VIPs point", 0.224, VNS), ("VIPs lower HPD", 0.17, VNS),
                       ("VIPs strong-only point 0.126", 0.126, VNS), ("VIPs strong-only lower HPD 0.018", 0.018, VNS)]:
        c = a * n
        print("  %s: %.0f (%.2f x G1)" % (name, c, c / G1))
    print("\nBlocker checks: (1) human-specific %s; (2) bias-corrected %s; (3) lower HPD 0.096 >= 1.75%%: %s; (4) compounded %0.f > 191: %s"
          % (ok, ok, 0.096 > 0.0175, lo, lo > G1))


if __name__ == "__main__":
    main()
