"""A2e-alpha: map published human-lineage adaptive-substitution estimates (alpha) onto the A2e flip threshold.
Load-bearing tier (A2e is on the ROOT path; three reviews).  Analysis only (arithmetic + verbatim-quote verification
against the local raw texts, read as data); trivial compute, run locally.
Run:  research/.venv/bin/python -I research/checks/a2e_alpha_map.py
Pre-registered: this docstring is committed BEFORE the script is run.

THRESHOLD (R4-A2e.md, Flag 1 "Testable form", post hoc PH8): A2e per generation, adaptive-only, flips (F = 1) when the
human lineage fixed more than about 191 adaptive substitutions since the CHLCA:
  basis G1: Day's G_f = 1,322 generations per fixation (MITTENS 3.0 s7.3 p.13, "191 achievable") -> 252,000 / 1,322 = 190.6
  basis G2: G_f = 1,587 (2nd edition, R4-A2e) -> 252,000 / 1,587 = 158.8
  (also printed: Day's adaptive-only reading 1,408 -> 179.0; and the GAP-06 Yoo generation count 6.3e6 / 24.5 = 257,143)
  Day's statement under test (A2e, Z23003785 s8.6 p.15): "The objection implicitly claims that humans can fix
  mutations faster per generation than bacteria under ideal conditions" ("unattainable ceiling, the absolute
  best-case scenario" is the scored dialectic part).

ESTIMATES (verbatim; refresh-2026-10-10b s1; each is re-verified as a substring of the local raw text by this script)
  GV  Gaya-Vidal & Alba 2014 (BMC Genomics 15:599; OA full text): "Our overall estimate of the fraction of fixed
      adaptive substitutions (α) in the human lineage is very low, approximately 0.2%"; "resulted in 9,785 genes with
      human branch specific substitution data"; "The average number of Dn and Ds per gene in the human lineage was 2
      and 3.5"; "at least 40% of the non-synonymous substitutions in genes accelerated in the human branch".
  BO  Boyko et al. 2008 (PLoS Genet; OA full text): "we expect that 10–20% of human-chimp differences were fixed through
      positive selection"; "(observed fixed differences = 22,180)"; "is 9.3% less than what we observe (22,180";
      gene set: "17.8 Mb of genic sequence (approximately 61% of autosomal RefSeq gene bases)".
  EK  Eyre-Walker & Keightley 2009 (MBE; ABSTRACT ONLY): "comparison to macaque sequences reveals little evidence for
      adaptive substitutions"; "could be as high as 40%".
  UR  Uricchio, Petrov & Enard 2019 (Nat Ecol Evol; ABSTRACT ONLY): "estimate α = 0.135 in human protein-coding
      sequences, 72% of which is contributed by weakly adaptive variants".
  GA  Galtier 2016 (context, no human count): "with the notable exception of primates".

DENOMINATORS (nonsynonymous substitutions on the human lineage; all are gene-set counts, i.e. LOWER bounds on the
whole-exome count; coding-only adaptive counts are in turn lower bounds on all adaptive substitutions):
  N1 Gaya-Vidal human branch: 2 x 9,785 = 19,570 (the "2" is rounded in the text: +-25% band 14,700-24,500).
  N2 Boyko both lineages 22,180 / 2 = 11,090 per lineage (even split assumed).
  N3 Boyko scaled to all autosomal RefSeq gene bases: 11,090 / 0.61 = 18,180 per lineage (derived; assumes uniform density).
MAPPING: adaptive count = alpha x denominator; side = "critic (A2e flips)" if > threshold, "Day (A2e holds)" if <=.
  Estimates on human-chimp divergence (BO) use N2/N3; on the human branch (GV) use N1; abstract-only alphas (UR, EK)
  are applied to every denominator, marked "abstract only".  EK's "little evidence" is mapped as alpha in [0, 0.05]
  (no number is given; the 5% upper end is the audit's reading, labelled); EK's 40% is a conditional upper bound.
  GV's "at least 40%" is restricted to accelerated genes whose Dn is not extracted: a lower bound of unknown size
  (not mapped; reported).  alpha* = threshold / denominator is printed for each denominator.

PREDICTIONS (fixed now)
  Day side: the best human estimates put the lineage at or below ~191 (GV 0.2% -> ~40; EK "little evidence"; GA).
  Critic side: Boyko and Uricchio put it at >= 1,000, i.e. > 5x the threshold, on every denominator and both bases.
  Audit: Q1 alpha* lies between 0.8% and 1.8% on every denominator and basis.  Q2 GV maps to 20-60 (Day side);
  BO 10-20% maps to 1,100-3,700 (critic side); UR 0.135 maps to 1,500-2,700 (critic side, abstract only); EK range
  straddles the threshold.  Q3 Outcome: the published estimates fall on BOTH sides of the threshold, by more than
  10x each way, so the literature does not settle A2e; external stays `contested`, now with a named empirical
  disagreement (GV vs BO/UR) instead of an unfetched literature.  Asymmetry (stated in advance): a coding-only count
  above the threshold is sufficient for the flip if correct; a coding-only count below it is not sufficient for Day,
  because regulatory/non-coding adaptive substitutions are not counted (no human-lineage estimate exists in a
  comparable form, refresh s1).  Rule R1: the move from "unknown" to "both sides by > 10x" changes no verdict by
  itself (contested -> contested).
"""
import hashlib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RAWD = os.path.join(ROOT, "sources", "raw", "refresh-2026-10-10b")
SRC = {"GV": "ft/PMC4124166/ft.txt", "BO": "ft/PMC2377339/ft.txt", "EK": "epmc/ew09.json", "UR": "epmc/uric.json",
       "GA": "ft/PMC4709115/ft.txt"}
QUOTES = {
    "GV": ["Our overall estimate of the fraction of fixed adaptive substitutions (α) in the human lineage is very low, approximately 0.2%",
           "resulted in 9,785 genes with human branch specific substitution data",
           "The average number of Dn and Ds per gene in the human lineage was 2 and 3.5",
           "at least 40% of the non-synonymous substitutions in genes accelerated in the human branch"],
    "BO": ["we expect that 10–20% of human-chimp differences were fixed through positive selection",
           "(observed fixed differences = 22,180)",
           "is 9.3% less than what we observe (22,180",
           "17.8 Mb of genic sequence (approximately 61% of autosomal RefSeq gene bases)"],
    "EK": ["comparison to macaque sequences reveals little evidence for adaptive substitutions",
           "could be as high as 40%"],
    "UR": ["estimate α = 0.135 in human protein-coding sequences, 72% of which is contributed by weakly adaptive variants"],
    "GA": ["with the notable exception of primates"],
}


def norm(s):
    s = s.replace(" ", " ").replace(" ", " ").replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s)


def main():
    print("## quote verification (substring of the local raw text, whitespace-normalised)")
    allok = True
    for k, rel in SRC.items():
        p = os.path.join(RAWD, rel)
        b = open(p, "rb").read()
        t = norm(b.decode("utf-8", "replace"))
        if rel.endswith(".json"):
            t = norm(json.dumps(json.loads(b), ensure_ascii=False))
        for q in QUOTES[k]:
            ok = norm(q) in t
            allok &= ok
            print(f"  {k} {'OK  ' if ok else 'MISS'} {q[:90]}")
        print(f"  {k} sha256 {hashlib.sha256(b).hexdigest()}  {rel}")
    print(f"all quotes verified: {allok}")

    T = {"G1 (1,322)": 252000 / 1322, "G2 (1,587)": 252000 / 1587, "Day adaptive-only (1,408)": 252000 / 1408,
         "G1 at Yoo g 24.5 (257,143 gens)": 6.3e6 / 24.5 / 1322}
    D = {"N1 GV human branch 19,570": 19570, "N1 low (Dn 1.5/gene) 14,678": 14678, "N1 high (Dn 2.5/gene) 24,463": 24463,
         "N2 Boyko per lineage 11,090": 11090, "N3 Boyko scaled /0.61 18,180": 11090 / 0.61}
    print("\n## thresholds (adaptive substitutions per lineage) and alpha* = threshold / denominator")
    print("| denominator | " + " | ".join(T) + " |")
    print("|---|" + "---|" * len(T))
    for dn, dv in D.items():
        print(f"| {dn} | " + " | ".join(f"{tv:.1f} -> {100 * tv / dv:.2f}%" for tv in T.values()) + " |")

    est = [
        ("GV alpha 0.2% (human branch; full text)", 0.002, 0.002, ["N1 GV human branch 19,570", "N1 low (Dn 1.5/gene) 14,678", "N1 high (Dn 2.5/gene) 24,463"]),
        ("BO 10-20% (human-chimp divergence; full text)", 0.10, 0.20, ["N2 Boyko per lineage 11,090", "N3 Boyko scaled /0.61 18,180"]),
        ("BO 9.3% (gamma-model deficit, lower end; full text)", 0.093, 0.093, ["N2 Boyko per lineage 11,090", "N3 Boyko scaled /0.61 18,180"]),
        ("UR alpha 0.135 (ABSTRACT ONLY)", 0.135, 0.135, list(D)),
        ("UR strong-only 0.135 x 0.28 = 0.038 (ABSTRACT ONLY; derived)", 0.135 * 0.28, 0.135 * 0.28, list(D)),
        ("EK 'little evidence' read as 0-5% (ABSTRACT ONLY; audit reading)", 0.0, 0.05, list(D)),
        ("EK 'as high as 40%' (ABSTRACT ONLY; conditional upper bound)", 0.40, 0.40, list(D)),
    ]
    print("\n## mapped adaptive counts per lineage and side (threshold G1 190.6 / G2 158.8)")
    print("| estimate | denominator | adaptive count | x G1 threshold | side (G1) | side (G2) |")
    print("|---|---|---|---|---|---|")
    g1, g2 = T["G1 (1,322)"], T["G2 (1,587)"]
    for name, lo, hi, dens in est:
        for dn in dens:
            a, b = lo * D[dn], hi * D[dn]
            def side(th):
                if b <= th:
                    return "Day (holds)"
                if a > th:
                    return "critic (flips)"
                return "straddles"
            print(f"| {name} | {dn} | {a:.0f}-{b:.0f} | {a / g1:.2f}-{b / g1:.2f} | {side(g1)} | {side(g2)} |")
    print("\nGV 'at least 40%' in accelerated genes: not mapped (Dn of that gene set not extracted); a lower bound only.")
    print("Asymmetry: coding-only counts are lower bounds on all adaptive substitutions (non-coding not counted).")


if __name__ == "__main__":
    main()
