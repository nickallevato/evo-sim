#!/usr/bin/env python3
"""M-102 record (formula, derivation): Day's cross-ape average rate, 63.281 bp/y and 1,958.81 bp per effective generation.

Object: docs/research/math/objects.yaml M-102 (formula, derivation). evo006@L33: 398,673,272 bp over about 6.3 My
gives 63.281 bp/y. evo006@L35: the mean of six ape rates (37.8 to 99.4 bp/y, not listed one by one) is 62.7 bp/y, or
1,958.81 bp per effective generation. The conversion factor is not printed; the source map infers 25 y / d = 0.80 =
31.25 y per effective generation (Day's g = 25 y and d = 0.80, evo009@L54). The record asserts 63.281, the factor, the
gap 62.7 x 31.25 = 1,959.375 against the printed 1,958.81 (0.029%), and the unrounded mean that the printed figure
implies: 1,958.81 / 31.25 = 62.682 (the interval [62.68176, 62.68208) if 1,958.81 is rounded to cents), which rounds to
the printed 62.7. No other round factor fits: 1,958.81 / 62.7 = 31.241 = 25 / 0.80023. The six rates are not held, so
their mean is not recomputed. Two readings of the numerator are recorded, not scored: 398,673,272 is Day's total
divergence over both lineages "from the human perspective" (refresh-2026-10-15), and Day's own per-lineage figure is
199,336,636, which halves the rate to 31.64 bp/y; and it counts base pairs, not events (A3x, R4 GAP-07b: 42.10M events,
both lineages). Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-102.py [--write]
Without --write it checks that M-102.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo006": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-006/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt"}
PY = "docs/research/parameters.yaml"
R1015 = "docs/research/sources/refresh-2026-10-15.md"
A3X = "docs/research/claims/A3x-bp-vs-events.md"


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


# ---- inputs -------------------------------------------------------------------------------------------
Q33 = post("evo006", "That’s the average rate of post-CHLCA human evolution: 63.281 base-pairs per year.")  # evo006@L33
Q35 = post("evo006", "62.7 base pairs per year, or 1,958.81 base pairs per effective generation.")        # evo006@L35
Q36 = post("evo006", "that’s the speed at which evolution by natural selection, neutral drift, and relictation has "
                     "to take place, assuming it took place at all and is responsible for all of the observed "
                     "divergences")                                                                     # evo006@L36
Q40 = post("evo006", "Not a single number in that calculation came from Lenski.")                       # evo006@L40
ROW33 = held(SM + "evo006.md", "P: 398,673,272 bp over about 6.3 My. I: divide. C: 63.281 bp/y.")
ROW35 = held(SM + "evo006.md", "P: six rates of 37.8-99.4 bp/y averaged. I: convert by 25 y / d = 0.80 (factor 31.25, "
                               "inferred).")
D1 = post("evo009", "When d=1, as in the Wright-Fisher model, there are 252,000 generations separating the CHLCA from "
                    "modern humanity.")                                                                 # evo009@L54
ROW54 = held(SM + "evo009.md", "P: d = 1 gives 252,000; d = 0.80 gives 201,600 effective.")
TOTAL_Q = held(R1015, "\"the total chimpanzee-human divergence from the human perspective is 398,673,272 base-pairs, "
                      "or 12.79 percent of the human genome\"")
HALF_Q = held(R1015, "\"the most relevant number to plug into MITTENS is 199,336,636, not 205 million\"")
EVENTS = held(A3X, "37.77M SNVs, 4.30M indel events (2.17M extra-human-base, 2.09M extra-chimp-base, 35k both-sided), "
                   "42.10M events, 21.05M per lineage")                                                 # R4 GAP-07b
held(PY, "day_2026_mittens3: {value: 6.3e6, source: Z23003785")       # divergence.t_div_years.day_2026_mittens3
held(PY, "day_2026: {value: 25, source: Z23003785")                   # generation_time_years.day_2026

BP, T_DIV, G, D = 398_673_272, Fr(6_300_000), Fr(25), Fr(4, 5)

# ---- 63.281 bp/y --------------------------------------------------------------------------------------
rate = BP / T_DIV
near(float(rate), 63.281, 0.0005)                                    # 63.28147 -> printed 63.281
assert T_DIV / G == 252_000 and T_DIV / G * D == 201_600             # evo009@L54 generation counts

# ---- 62.7 bp/y and 1,958.81 bp per effective generation -------------------------------------------------
factor = G / D                                                       # inferred: 25 y / 0.80
assert factor == Fr(125, 4)                                          # 31.25 y per effective generation
naive = Fr(627, 10) * factor
assert naive == Fr(15675, 8)                                         # 62.7 x 31.25 = 1,959.375
gap = naive - Fr(195881, 100)
assert gap == Fr(113, 200)                                           # 0.565 bp above the printed 1,958.81
near(float(gap / Fr(195881, 100)), 2.88e-4, 1e-6)                     # 0.029%
implied = Fr(195881, 100) / factor
near(float(implied), 62.68192, 1e-5)                                 # the unrounded mean the print implies
lo, hi = Fr(1958805, 1000) / factor, Fr(1958815, 1000) / factor
near(float(lo), 62.68176, 1e-5); near(float(hi), 62.68208, 1e-5)     # if 1,958.81 is rounded to 2 dp
assert round(float(lo), 1) == round(float(hi), 1) == 62.7            # every such mean prints as 62.7
alt = Fr(195881, 100) / Fr(627, 10)
near(float(alt), 31.2410, 5e-5)                                      # factor if the mean were exactly 62.7
near(float(G / alt), 0.80023, 5e-6)                                  # = 25 / 0.80023: not a round d
chimp_eff = rate * factor
near(float(chimp_eff), 1977.55, 0.01)                                # the chimp-only rate per effective generation

# ---- the two readings of the numerator (recorded, not scored) --------------------------------------------
assert BP // 2 == 199_336_636 and BP % 2 == 0                        # Day's per-lineage figure (refresh 10-15)
per_lineage = Fr(BP, 2) / T_DIV
near(float(per_lineage), 31.6407, 5e-5)                              # bp/y on the human lineage alone
near(float(per_lineage * factor), 988.77, 0.01)                      # bp per effective generation, one lineage
ev_rate = Fr(4210, 100) * 10 ** 6 / T_DIV
near(float(ev_rate), 6.6825, 5e-5)                                   # events/y, both lineages (GAP-07b 42.10M)
near(BP / 42.10e6, 9.470, 5e-4)                                      # bp per event on Day's total

finish({
    "object": "M-102",
    "inputs": [
        {"name": "divergence, both lineages, from the human perspective", "value": BP, "cite": "evo006@L33; refresh-2026-10-15 (Day, 'Evo-Avengers 002')"},
        {"name": "t_div", "value": 6.3e6, "cite": "parameters divergence.t_div_years.day_2026_mittens3; evo006@L33"},
        {"name": "generation time", "value": 25, "cite": "parameters generation_time_years.day_2026"},
        {"name": "d", "value": 0.80, "cite": "evo009@L54 (252,000 x 0.80 = 201,600); the use of 25/0.80 in L35 is inferred (source map)"},
        {"name": "six-ape mean (printed)", "value": 62.7, "cite": "evo006@L35; individual rates 37.8-99.4 bp/y not listed"},
        {"name": "events, both lineages", "value": 42.10e6, "cite": "claim file A3x, R4 GAP-07b (hg38 vs panTro6)"},
    ],
    "values": {
        "rate_bp_per_y": round(float(rate), 5),
        "factor_y_per_effective_generation": 31.25,
        "mean_62.7_times_factor": 1959.375,
        "printed_per_effective_generation": 1958.81,
        "gap_bp": 0.565, "gap_relative": round(float(gap / Fr(195881, 100)), 6),
        "implied_unrounded_mean": round(float(implied), 5),
        "implied_mean_interval": [round(float(lo), 5), round(float(hi), 5)],
        "factor_if_mean_exactly_62.7": round(float(alt), 4),
        "chimp_rate_per_effective_generation": round(float(chimp_eff), 2),
        "per_lineage_bp_per_y": round(float(per_lineage), 4),
        "per_lineage_bp_per_effective_generation": round(float(per_lineage * factor), 2),
        "events_per_y_both_lineages": round(float(ev_rate), 4),
        "bp_per_event": round(BP / 42.10e6, 3),
    },
    "positions": {
        "day": {"reading": "an average divergence rate with no LTEE input is the speed any mechanism must have run at",
                "holds": "the arithmetic reproduces: 63.281 exactly, 1,958.81 from an unrounded mean of 62.682 and the "
                         "inferred factor 25/0.80; no input is from the LTEE (evo006@L40)"},
        "critic": {"reading": "a required fixation rate needs more steps than divergence / time",
                   "holds": "the numerator is both lineages (Day's own per-lineage figure halves the rate to 31.64 bp/y) "
                            "and counts base pairs (about 9.5 bp per event on GAP-07b's count); constant rate, fixed "
                            "rather than polymorphic sites and lineage assignment are not addressed in the post"},
    },
    "notes": "Every printed number reproduces. The 0.565 bp gap is the rounding of the six-ape mean: 1,958.81 implies a "
             "mean of 62.682 bp/y, which prints as 62.7. The factor 25/0.80 is inferred by the source map; it is the "
             "only round factor that fits. 'Rate of post-CHLCA human evolution' (L33) is read on a numerator that Day "
             "himself describes as the total over both lineages from the human perspective; on his per-lineage "
             "199,336,636 the rate is 31.64 bp/y. Which reading the post intends is not stated; both are recorded. The "
             "six individual rates, the 60.5 My and the 25,302,032,866 bp are not held and not checked.",
})
