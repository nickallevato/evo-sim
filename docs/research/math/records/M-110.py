#!/usr/bin/env python3
"""M-110 record (parameter, derivation): effective generations since the CHLCA, 252,000 nominal and 201,600 at d = 0.80.

Object: docs/research/math/objects.yaml M-110 (parameter, derivation). Day (evo009@L54): "When d=1, as in the
Wright-Fisher model, there are 252,000 generations" and at d = 0.80 "201,600 effective generations". Asserted:
6.3e6 / 25 = 252,000 and 252,000 x 0.80 = 201,600, the same figure as 6.3e6 / 31.25 (the effective generation
length g/d of M-107), and the d = 0.45 row for contrast. Held verbatim: 6.3e6, 25 and 252,000 (Q18, MITTENS 3.0 p.11,
and parameters.yaml keys); 252,000, 0.80 and 201,600 (evo009@L54; Duffy's "d-coded size of 201,600", evo008@L89).
0.80 has no parameters.yaml key: the only d key, selection.turnover_d, holds 0.45 (Z18166234). How d enters, and
whether Wright-Fisher/Moran with N_e already carry the overlap correction, is M-107 (cited, not redone). Hancock's
answer (evo009@L51, relayed) is about attribution, not arithmetic: he used the number Duffy presented. Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-110.py [--write]
Without --write it checks that M-110.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo008": "sources/raw/refresh-2026-11-01/p-erica-and-the-evo-avengers-008/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt"}
QD = "docs/research/sources/quotes-day.md"
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


# ---- the source sentences ------------------------------------------------------------------------------
D_WF = post("evo009", "When d=1, as in the Wright-Fisher model, there are 252,000 generations separating the CHLCA "
                      "from modern humanity.")                                                         # evo009@L54
D_80 = raw("evo009", "When d=0.80, as the weighted time-average that corrects for overlapping human generations over "
                     "that period works out to be, that leaves 201,600 effective generations available.")  # evo009@L54
D_WFM = raw("evo009", "neither Wright-Fisher nor Moran accounts for this correction, which is precisely why the "
                      "selective turnover coefficient was developed in the first place.")              # evo009@L54
H_WILL = raw("evo009", "Again, I used the number that Will presented.")                                # evo009@L51, relay
WD_D = raw("evo008", "Second, minor: he’s using 252,000 generations instead of the d-coded size of 201,600.")  # L89
ROW54 = held(SM + "evo009.md", "Reproduces: 252,000 x 0.80 = 201,600; 6.3e6/25 = 252,000.")
Q18 = held(QD, "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 "
               "generations.")                                                                         # Q18, Z23003785 p.11
held(PY, "day_2026_mittens3: {value: 6.3e6, source: Z23003785")       # divergence.t_div_years.day_2026_mittens3
held(PY, "day_2026: {value: 25, source: Z23003785")                   # generation_time_years.day_2026
held(PY, "day_2026: {value: 252000, source: Z23003785")               # generations_available.day_2026
held(PY, "turnover_d: {value: 0.45, source: Z18166234")               # selection.turnover_d (the only d key)
held(PY, "day_2025_effective: {value: 146250, derived: \"325000*0.45\"")  # generations_available.day_2025_effective

# ---- the arithmetic -----------------------------------------------------------------------------------------
T, G, D80, D45 = 63 * 10 ** 5, 25, Fr(80, 100), Fr(45, 100)
nominal = Fr(T, G)
assert nominal == 252_000                                            # d = 1
eff80 = nominal * D80
assert eff80 == 201_600                                              # d = 0.80, as printed
assert Fr(T) / (Fr(G) / D80) == eff80                                # = 6.3e6 / 31.25, the g/d form (M-107)
assert cited("M-107", "effective_generation_years")["0.80"] == 31.25
assert cited("M-107", "d_enters_F_max_only_as_g_over_d") is True
eff45 = nominal * D45
assert eff45 == 113_400                                              # the parameters.yaml d (0.45), for contrast
assert Fr(325_000) * D45 == 146_250                                  # the 2025 series value, same operation
near(cited("M-107", "F_max")["d_0.80"], float(eff80 / 1322), 0.005)  # 152.5 = 201,600 / 1,322 (M-107)
assert nominal - eff80 == 50_400 and eff80 / nominal == D80          # the correction removes 20%

finish({
    "object": "M-110",
    "inputs": [
        {"name": "t_div (years)", "value": 6.3e6, "cite": "parameters divergence.t_div_years.day_2026_mittens3; Q18", "held_verbatim": True},
        {"name": "generation length (years)", "value": 25, "cite": "parameters generation_time_years.day_2026; Q18", "held_verbatim": True},
        {"name": "nominal generations", "value": 252_000, "cite": "parameters generations_available.day_2026; Q18; evo009@L54", "held_verbatim": True},
        {"name": "d", "value": 0.80, "cite": "evo009@L54 (no parameters.yaml key; selection.turnover_d is 0.45)", "held_verbatim": True},
        {"name": "effective generations", "value": 201_600, "cite": "evo009@L54; evo008@L89 (Duffy)", "held_verbatim": True},
    ],
    "values": {
        "nominal_d1": int(nominal), "effective_d080": int(eff80), "effective_d045": int(eff45),
        "effective_generation_years_d080": 31.25, "share_removed_d080": 0.2,
    },
    "positions": {
        "day": {"reading": "d = 0.80 corrects 252,000 for overlapping generations; critics should have used 201,600; "
                           "neither Wright-Fisher nor Moran carries the correction",
                "holds": "the arithmetic reproduces (6.3e6/25 = 252,000; x 0.80 = 201,600 = 6.3e6/31.25)"},
        "critic": {"reading": "Hancock used the number Duffy presented (evo009@L51); Wright-Fisher/Moran with N_e "
                              "already account for overlap",
                   "holds": "attribution is not arithmetic; whether N_e scaling captures what d does is M-107 (open "
                            "there for selection); 0.80 is not the d in parameters.yaml (0.45, which gives 113,400)"},
    },
    "notes": "Every input is held verbatim (Q18 and parameters.yaml for 6.3e6/25/252,000; evo009@L54 for 0.80 and "
             "201,600). d multiplies generations (equivalently the generation length is g/d), as M-107 records; "
             "the record does not redo whether that correction is needed. The d series in Day's own figures: 0.45 "
             "(parameters, Z18166234; 325,000 x 0.45 = 146,250 in the 2025 version) and 0.80 (10-21..10-30 posts); "
             "which one MITTENS 3.0 and the book use is M-114.",
})
