#!/usr/bin/env python3
"""M-114 record (parameter, lookup): Day's two human parameter sets inside one fortnight (variant of M-110).

Object: docs/research/math/objects.yaml M-114 (parameter, lookup; variant_of M-110). Set A, the 10-23 post
(evo007@L32): N_e ~ 33,000, s-bar ~ 0.001, g ~ 29 y, d ~ 0.45. Set B, the 10-21..10-30 posts: N_e = 10,000 (evo005,
the d-rescaled 14,648-generation row), g = 25 y (Q18, MITTENS 3.0 p.11), d = 0.80 (evo009@L54). Each value is looked
up with its parameters.yaml key or source-map row; no new keys. Flags: g = 29 has no held source for Day (his keyed
generation lengths are 20, 25 and 32.5; 29 appears only as the top of the audit's own R4 A2e range); N_e = 33,000 has
no parameters key, and in Day's own Z18525547 (claim files B3, B4) 33,000 is the chimpanzee N_e with human N_e =
3,300, yet evo007@L32 calls it a human parameter; s = 0.001 is keyed (Zeng 2021) as a mean |s| under negative
selection; 0.80 has no key (selection.turnover_d is 0.45). The 10-23 post states no t_div; with the shared 6.3e6
the sets give 97,759 against 201,600 effective generations (0.485x) and 4 N_e of 132,000 against 40,000 generations
(3.3x). Which set MITTENS 3.0 and the book use is a provenance question for parameters.yaml, not settled here.
Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-114.py [--write]
Without --write it checks that M-114.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo007": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-007/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt"}
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def post(src, quote):
    """A source-map quote (committed), re-checked against the held post body when sources/raw is in this checkout."""
    held(SM + src + ".md", quote)
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def raw(src, quote):
    """A sentence from the held post body that the source map does not copy; checked when sources/raw is present."""
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def cited(rec, key):
    """A value from a settled record's JSON (cited, not recomputed)."""
    return json.loads((ROOT / REC / f"{rec}.json").read_text(encoding="utf-8"))["values"][key]


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def finish(rec):
    rec = {"id": HERE.stem, "date": DATE, "script": f"docs/research/math/records/{HERE.name}",
           "script_sha256": hashlib.sha256(HERE.read_bytes()).hexdigest(), **rec}
    out = json.dumps(rec, indent=2, ensure_ascii=False) + "\n"
    js = HERE.with_suffix(".json")
    if "--write" in sys.argv:
        js.write_text(out, encoding="utf-8")
    elif js.exists():
        assert js.read_text(encoding="utf-8") == out, f"{js.name} is stale; rerun with --write"
    print(f"{HERE.stem}: all asserts pass")


# ---- set A: the 10-23 post ------------------------------------------------------------------------------
A_ROW = post("evo007", "when you set human parameters (N_e ≈ 33,000, s̄ ≈ 0.001, generation time ≈ 29 years, "
                       "d ≈ 0.45), you get an answer")                                        # evo007@L32
A_NE = raw("evo007", "he’d cite the textbook ~10,000, we’ve calculated ~33,000")              # evo007@L22
held("docs/research/math/objects.yaml", "the post gives no source for g = 29")                # M-114 positions.day
held(PY, "s_zeng_2021: {value: 0.001, sign: negative")                # selection.s_zeng_2021
held(PY, "turnover_d: {value: 0.45, source: Z18166234")               # selection.turnover_d
held(PY, "a2e_per_year_range: {value: [20, 29], note: \"range used for the per-year context rows of R4 A2e")  # audit's
held(PY, "day_2019: {value: 20, source: B2019-02-07")                 # generation_time_years.day_2019
held(PY, "day_alt: {value: 32.5, source: B2025-01-18")                # generation_time_years.day_alt
B4_33 = held(CL + "B4-clock-recalibration-200-580-kya.md", "Nₑ,h = 3,300 (aDNA drift variance, branch C), Nₑ,c = 33,000 "
                                                         "(F_ST across chimp subspecies)")
B3_33 = held(CL + "B3-k-neq-mu-values-umbrella.md", "N = 50–100k, Nₑ = 3,300; chimp N = 300k–1M, Nₑ = 33,000")

# ---- set B: the 10-21..10-30 posts ---------------------------------------------------------------------------
B_NE = held(SM + "evo005.md", "Incorporating d means the 14,648-generation fixation time at the empirical s for "
                              "N_e = 10,000 becomes roughly 18,310 generations.")             # evo005 (10-21)
held(PY, "Ne_modern_human: {value: 1.0e4, source: textbook")          # population.Ne_modern_human
B_G = held(QD, "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 "
               "generations.")                                                               # Q18
held(PY, "day_2026: {value: 25, source: Z23003785")                   # generation_time_years.day_2026
held(PY, "day_2026_mittens3: {value: 6.3e6, source: Z23003785")       # divergence.t_div_years.day_2026_mittens3
B_D = raw("evo009", "When d=0.80, as the weighted time-average that corrects for overlapping human generations over "
                    "that period works out to be, that leaves 201,600 effective generations available.")  # evo009@L54
held(SM + "evo006.md", "convert by 25 y / d = 0.80 (factor 31.25, inferred)")                 # evo006@L35 (10-22)

# ---- the two sets, side by side ----------------------------------------------------------------------------------
A = {"Ne": 33_000, "s": Fr(1, 1000), "g": 29, "d": Fr(45, 100)}
B = {"Ne": 10_000, "g": 25, "d": Fr(80, 100)}
T = 63 * 10 ** 5
eff_a, eff_b = Fr(T, A["g"]) * A["d"], Fr(T, B["g"]) * B["d"]
assert eff_b == 201_600 == cited("M-110", "effective_d080")          # set B is M-110
near(float(eff_a), 97_758.62, 0.005)                                 # set A on the same t_div
near(float(eff_a / eff_b), 0.484914, 5e-7)
assert Fr(T, A["g"]) == Fr(63 * 10 ** 5, 29) and near(float(Fr(T, 29)), 217_241.38, 0.005)
assert 4 * A["Ne"] == 132_000 and 4 * B["Ne"] == 40_000              # 4 N_e generations
near(4 * A["Ne"] / (4 * B["Ne"]), 3.3, 1e-12)
assert A["Ne"] == 10 * 3_300                                         # 33,000 is Day's chimp N_e; his human N_e is 3,300
assert A["g"] not in (20, 25, 32.5)                                  # no keyed Day generation length is 29
diffs = sorted(k for k in ("Ne", "g", "d") if A[k] != B[k])
assert diffs == ["Ne", "d", "g"]                                     # all three shared inputs differ

finish({
    "object": "M-114",
    "inputs": [
        {"set": "A (10-23)", "name": "N_e", "value": 33_000, "cite": "evo007@L32, evo007@L22; no parameters key; Z18525547 uses 33,000 for chimpanzee (B3, B4)", "flag": "no held human source"},
        {"set": "A (10-23)", "name": "s-bar", "value": 0.001, "cite": "evo007@L32; parameters selection.s_zeng_2021 (sign negative)"},
        {"set": "A (10-23)", "name": "g (years)", "value": 29, "cite": "evo007@L32", "flag": "no held source; Day's keyed values are 20, 25, 32.5"},
        {"set": "A (10-23)", "name": "d", "value": 0.45, "cite": "evo007@L32; parameters selection.turnover_d (Z18166234)"},
        {"set": "B (10-21..10-30)", "name": "N_e", "value": 10_000, "cite": "evo005 row (14,648 -> 18,310); parameters population.Ne_modern_human"},
        {"set": "B (10-21..10-30)", "name": "g (years)", "value": 25, "cite": "Q18; parameters generation_time_years.day_2026; evo006@L35"},
        {"set": "B (10-21..10-30)", "name": "d", "value": 0.80, "cite": "evo009@L54; evo006@L35 (inferred); no parameters key"},
    ],
    "values": {
        "differing_inputs": diffs,
        "effective_generations_on_6.3e6": {"A": round(float(eff_a), 2), "B": int(eff_b)},
        "A_over_B_effective_generations": round(float(eff_a / eff_b), 5),
        "four_Ne_generations": {"A": 132_000, "B": 40_000},
        "unsourced": ["g = 29", "N_e = 33,000 as a human value"],
    },
    "positions": {
        "day": {"reading": "set A is the human parameter set that 'gets an answer'; inputs are 'known or bounded'",
                "holds": "s = 0.001 and d = 0.45 carry parameters.yaml keys; N_e is 'a number either way' (evo007@L22)"},
        "critic": {"reading": "version drift inside one fortnight; which set MITTENS 3.0 and the book use is a "
                              "provenance question",
                   "holds": "all three shared inputs differ; on the same t_div set A gives 0.485x the effective "
                            "generations of set B; g = 29 has no held source and 33,000 is Day's chimpanzee N_e "
                            "elsewhere"},
    },
    "notes": "Lookup only; no verdict. Neither set is shown to be the one MITTENS 3.0 uses beyond Q18 (g = 25, 252,000). "
             "The 0.80 and 0.45 values of d are both Day's (M-110 notes); 33,000 against 3,300 is a factor of 10 "
             "that matches Day's chimp/human pair in Z18525547. s = 0.001 is keyed as a negative-selection mean "
             "(claim file F3a); set B's posts use other s values (M-104, M-105).",
})
