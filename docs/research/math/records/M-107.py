#!/usr/bin/env python3
"""M-107 record (model-choice, derivation): is the selective turnover coefficient d coherent and needed beyond Ne.

Object: docs/research/math/objects.yaml M-107 (model-choice, derivation). Duffy (evo008, relayed): Wright-Fisher and
Moran answer how fast drift moves neutral alleles, d answers how fast the gene pool turns over, and d "has essentially
nothing to do with" MITTENS. Hancock (evo009@L25, relayed; A4e, A4f): gene-pool turnover is not meaningful because
alleles are staggered; overlap is handled by scaling Ne or by Moran; d has no equivalent term. Day (evo009, evo010):
rates are averages of staggered events; Hancock must show d incoherent or already captured; Ne is drift, d is whether
selection has enough turnover. The record settles what the held formulas let it settle, by exact identities, and
cites the rest. (1) In every held formula d enters as one product: in the Term 3 sweep time tau = (2/(s d)) ln(2Ne)
(M-808) only through s x d, and in F_max = t_div d/(g G_f) (M-013, M-713) only through g/d, an effective generation
length (31.25 y at d = 0.80, 55.6 y at 0.45). So within these formulas d is "captured by existing parameters" (an
effective s or an effective generation time), which is also M-304's finding that trajectory fits identify s x d,
not d. (2) That does not make d incoherent: M-013 gives it a definition and units, and Day's quantity is not Ne
(Hancock's own Ne/N = 25/80 = 0.31 is a different number for a different job, A4e). (3) Separability (Duffy): in
F_max, d moves the count by 1/d, 1.25x at 0.80 and 2.22x at 0.45; the SNV-only shortfall of 91,600 (d = 1) only
grows for d < 1 (114,500 at 0.80, 203,556 at 0.45). So d is not "nothing" to MITTENS, but it is small beside it.
(4) "Staggered" events still have an average rate (M-101, M-706). Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-107.py [--write]
Without --write it checks that M-107.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo008": "sources/raw/refresh-2026-11-01/p-erica-and-the-evo-avengers-008/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt",
       "evo010": "sources/raw/refresh-2026-11-01b/evo010/body.txt"}
CL = "docs/research/claims/"
A4E = CL + "A4e-hancock-overlap-is-handled-by-ne-and-moran.md"
A4F = CL + "A4f-hancock-d-not-a-selection-coefficient.md"
OBJ = "docs/research/math/objects.yaml"
PY = "docs/research/parameters.yaml"
REC = "docs/research/math/records/"


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


# ---- the source sentences ------------------------------------------------------------------------------
WD_SEP = post("evo008", "It has essentially nothing to do with his Mittens argument that evolution by natural "
                        "selection is mathematically impossible.")                                    # evo008@L78, relay
if (ROOT / RAW["evo008"]).exists():                                   # WD's two-questions passage, body only
    held(RAW["evo008"], "How fast does genetic drift move neutral alleles through the population?")
    held(RAW["evo008"], "How fast does the entire gene pool turn over?")
H_STAG = post("evo009", "How fast the entire gene pool turns over is not meaningful, because alleles are not turning "
                        "over and appearing all at once, but are staggered through time.")           # evo009@L25, relay
D_RATES = post("evo009", "Rates are by definition averages of staggered events.")                    # evo009@LNone
D_BURDEN = post("evo009", "Hancock either needs to show that d is internally incoherent or that the generational "
                          "overlap it measures is adequately captured by existing parameters.")      # evo009@L28
E_POP = post("evo010", "Population genetics can already handle overlapping generations as well as a myriad of "
                       "different age class structures.")                                            # evo010@L4, relay
D_RETR = post("evo010", "That correction was not a retraction of the significance of overlapping generations or of my "
                        "claim that mainstream population genetics does not properly incorporate overlapping "
                        "generations as it absolutely must.")                                        # evo010@L6
D_NE = post("evo010", "Ne tells you how fast alleles drift while d tells you whether selection has enough "
                      "generational turnover to actually do its job.")                               # evo010@L13
H_MORAN = held(A4E, "And the Moran model is the model of overlapping generations.")                  # A4e q1
H_SCALE = held(A4E, "And you just scale that effective population size by the slowdown of drift due to overlapping "
                    "generations.")                                                                  # A4e q2
H_NOTERM = held(A4F, "I don't know what D is like there is no equivalent term in population genetics.")  # A4f q1
ID304 = held(OBJ, "Identifiability of d: trajectory fits identify the product s x d (logit gain s d G), not d")
held(PY, "turnover_d: {value: 0.45")                                 # selection.turnover_d
held(PY, "day_2026: {value: 25, source: Z23003785")                  # generation_time_years.day_2026
held(PY, "mittens3_snv_only: {value: 91600")                         # shortfall.mittens3_snv_only
held(PY, "day_mittens3_nonmutator: {value: 1322")                   # ltee.gens_per_fixation.day_mittens3_nonmutator

# ---- (1) d enters each held formula as one product ---------------------------------------------------------
tau = lambda s, d, ne: (2 / (s * d)) * math.log(2 * ne)              # M-808 sweep time
for s, d in ((Fr(1, 1000), Fr(45, 100)), (Fr(1, 100), Fr(4, 5)), (Fr(3, 2000), Fr(1, 3))):
    assert tau(s, d, 10_000) == tau(s * d, 1, 10_000)                # only s x d: an effective s
F = lambda t, d, g, gf: Fr(t) * d / (g * gf)                         # F_max (M-013, M-713)
T_DIV, G, GF = 6_300_000, Fr(25), 1_322
for d in (Fr(45, 100), Fr(4, 5), Fr(1)):
    assert F(T_DIV, d, G, GF) == F(T_DIV, 1, G / d, GF)              # only g / d: an effective generation length
assert G / Fr(4, 5) == Fr(125, 4)                                    # 31.25 y (the M-102 factor)
near(float(G / Fr(45, 100)), 55.556, 5e-4)

# ---- (2) d is not Ne: Hancock's Ne/N (A4e) and Day's d are different numbers ----------------------------------
hancock_ne_over_n = Fr(25, 80)
assert hancock_ne_over_n == Fr(5, 16) and hancock_ne_over_n != Fr(45, 100)   # 0.3125 vs 0.45
assert cited("M-013", "d_dims") == "dimensionless"
assert cited("M-013", "r4_c2")["per_gen_s_factor"] == 1              # for per-generation s, d's factor is 1 (R4 C2)
near(cited("M-304", "human_mean_d"), 0.4495, 5e-5)                   # three-locus required d (M-304, cited)

# ---- (3) separability: how far d moves F_max against the shortfall ---------------------------------------------
f1, f45, f80 = (F(T_DIV, d, G, GF) for d in (Fr(1), Fr(45, 100), Fr(4, 5)))
near(float(f1), 190.62, 0.005)                                       # 252,000 / 1,322
near(float(f45), cited("M-013", "F_max_with_d_0.45"), 1e-3)           # 85.78 (M-013)
assert f1 / f80 == Fr(5, 4) and f1 / f45 == Fr(20, 9)                # 1.25x and 2.22x
SHORT = 91_600
assert SHORT * f1 / f80 == 114_500                                   # the d = 1 shortfall (191 achievable) at d = 0.80
near(float(SHORT * f1 / f45), 203_556, 1)                            # and at d = 0.45
assert all(SHORT * f1 / F(T_DIV, d, G, GF) >= SHORT for d in (Fr(1, 10), Fr(45, 100), Fr(4, 5), Fr(1)))
                                                                     # d <= 1 only raises the shortfall

finish({
    "object": "M-107",
    "inputs": [
        {"name": "sweep time", "value": "tau = (2/(s d)) ln(2Ne)", "cite": "record M-808"},
        {"name": "F_max", "value": "t_div d / (g_len G_f)", "cite": "records M-013, M-713"},
        {"name": "t_div, g_len, G_f", "value": [T_DIV, 25, GF], "cite": "parameters divergence.t_div_years.day_2026_mittens3, generation_time_years.day_2026, ltee.gens_per_fixation"},
        {"name": "d", "value": [0.45, 0.80], "cite": "parameters selection.turnover_d; evo009@L54"},
        {"name": "Hancock's Ne/N", "value": "25/80", "cite": "claim file A4e formal statement (speaker-stated)"},
        {"name": "SNV-only shortfall", "value": SHORT, "cite": "parameters shortfall.mittens3_snv_only"},
    ],
    "values": {
        "d_enters_tau_only_as_s_times_d": True,
        "d_enters_F_max_only_as_g_over_d": True,
        "effective_generation_years": {"0.80": 31.25, "0.45": round(float(G / Fr(45, 100)), 3)},
        "F_max": {"d_1": round(float(f1), 2), "d_0.80": round(float(f80), 2), "d_0.45": round(float(f45), 2)},
        "F_max_factor_1_over_d": {"0.80": 1.25, "0.45": round(float(f1 / f45), 4)},
        "shortfall_snv_only": {"d_1": SHORT, "d_0.80": 114_500, "d_0.45": round(float(SHORT * f1 / f45))},
        "hancock_Ne_over_N": float(hancock_ne_over_n),
    },
    "positions": {
        "day": {"reading": "d is defined (M-013), measures turnover for selection rather than drift, and Hancock must "
                           "show it incoherent or already captured",
                "holds": "d has a definition and units (M-013) and is not Ne (0.45 against Hancock's 0.31, a different "
                         "quantity); 'staggered' events still have an average rate (M-101, M-706)"},
        "critic": {"reading": "overlap is already handled (Ne scaling, Moran); d has no counterpart and is not "
                              "meaningful",
                   "holds": "in every held formula d appears only as s x d or g/d, so it is captured by an effective "
                            "s or an effective generation time, and trajectory data identify s x d, not d (M-304)"},
        "duffy": {"reading": "d is harmless to concede; it has essentially nothing to do with MITTENS",
                  "holds": "in F_max d moves the count by 1/d (1.25x at 0.80, 2.22x at 0.45) and only raises the "
                           "shortfall (91,600 at d = 1, 203,556 at 0.45): small beside it, but not nothing"},
    },
    "notes": "Model-choice. The identities settle the narrow question Day sets at evo009@L28 for the held formulas: "
             "within tau and F_max, d is equivalent to rescaling s or the generation length, which is 'captured by "
             "existing parameters' in that algebraic sense; whether an age-structured model (Moran, Ne scaling) gives "
             "the same rescaling for selection is not derived in the corpus (A4e: literature not retrieved) and stays "
             "open. Coherence is M-013's definition, cited. Day's d trajectory from 0.86 to 0.015 is M-121, not here.",
})
