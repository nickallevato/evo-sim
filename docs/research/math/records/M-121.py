#!/usr/bin/env python3
"""M-121 record (parameter, lookup): d = 0.86 (wild chimps) and 0.015 (humanity 2026), against 0.80 and 0.45.

Object: docs/research/math/objects.yaml M-121 (parameter, lookup; variant_of M-110). evo010@L14 states d declining
"from 0.86 (wild chimps) to 0.015 (humanity 2026) over evolutionary time", "which is what the chart shows"; L15 draws
the consequence (no selection, genome degrading). Looked up: both values verbatim; neither has a parameters.yaml key
or a source in the post (the turnover key is selection.turnover_d = 0.45, Z18166234); "the chart" is an image in the
post (wp-image-73248, voxday.net/wp-content/uploads/2026/11/image.png, alt text empty), and the image file is not held,
so what it plots, and its source, are not read here. Compared with Day's other human d values in one fortnight:
0.80 (evo009@L54, record M-110) and 0.45 (evo007@L32 and Z18166234, records M-114, M-014). Asserted: the ratios
0.86/0.015 = 57.3, 0.80/0.015 = 53.3, 0.45/0.015 = 30, 0.80/0.45 = 1.78. Day dates the human fall elsewhere: selection
has not done its work "since around 1800" (Q89, H10 q1). Camestros (A4b q1) objected that a single d "would clearly
have changed during human evolution"; Day's L14 now says d declines over time, which concedes that premise, while
MITTENS uses one d over the whole 6.3 My (M-110). No new parameter keys. No verdict (H10, A4a, A4b). Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-121.py [--write]
Without --write it checks that M-121.json is current; --write saves it.
"""
import hashlib, json, pathlib, re, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo010": "sources/raw/refresh-2026-11-01b/evo010/body.txt",
       "evo010_html": "sources/raw/refresh-2026-11-01b/evo010/page.html"}
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


# ---- the two values and the chart -------------------------------------------------------------------------------
D_ROW = post("evo010", "Neither Wright-Fisher nor Moran can model the equivalent of d declining from 0.86 (wild "
                       "chimps) to 0.015 (humanity 2026) over evolutionary time")               # evo010@L14
CHART = raw("evo010", "progressively drain selection of its operating powe which is what the chart shows is what "
                      "actually happened over time.")                                           # evo010@L14 (typo as printed)
CONSEQ = post("evo010", "humanity is no longer subject to natural selection and the human genome is no longer being "
                        "cleansed of deleterious mutations")                                    # evo010@L15
MEDIUM = raw("evo010", "When d = 0.015, nearly everyone survives and reproduces regardless of their mutational load. "
                       "Selection has no medium to work through.")                              # evo010@L26 (Athos, rule U)
IMG = "https://voxday.net/wp-content/uploads/2026/11/image.png"
raw("evo010_html", f'src="{IMG}" alt="" class="wp-image-73248')                                 # the chart: a link only
img_dir = ROOT / RAW["evo010"].rsplit("/", 1)[0]
if img_dir.exists():
    assert sorted(p.name for p in img_dir.iterdir()) == ["body.txt", "page.html"]            # no image file is held
held(SM + "evo010.md", "No data for the 0.86 and 0.015 values in the post.")                  # map row evo010@L14

# ---- no parameters key for either value ------------------------------------------------------------------------------
ptxt = (ROOT / PY).read_text(encoding="utf-8")
assert not re.search(r"value: 0\.86\b", ptxt) and not re.search(r"value: 0\.015\b", ptxt)
held(PY, "turnover_d: {value: 0.45, source: Z18166234")                # selection.turnover_d

# ---- Day's other human d values, cited ------------------------------------------------------------------------------
assert cited("M-110", "effective_d080") == 201_600                    # d = 0.80 (evo009@L54)
assert cited("M-014", "d") == 0.45                                    # d = 0.45 (Z18166234, Q22)
held(SM + "evo007.md", "d ≈ 0.45")                                    # 10-23 post (M-114)
Q89 = held(QD, "natural selection hasn't been performing its real function, keeping the genome from degrading, since "
               "around 1800.")                                                                  # Q89, H10 q1
CAMESTROS = held(SM + "branch-A.md", "As this figure would clearly have changed during human evolution (and indeed "
                                     "demonstrably changed during human history), it doesn’t make a lot of sense.")  # A4b q1

# ---- ratios ---------------------------------------------------------------------------------------------------------
d = {"chimp_wild": Fr(86, 100), "human_2026": Fr(15, 1000), "M-110": Fr(80, 100), "M-114": Fr(45, 100)}
near(float(d["chimp_wild"] / d["human_2026"]), 57.333, 5e-4)
near(float(d["M-110"] / d["human_2026"]), 53.333, 5e-4)
assert d["M-114"] / d["human_2026"] == 30
near(float(d["M-110"] / d["M-114"]), 1.7778, 5e-5)
assert d["human_2026"] < d["M-114"] < d["M-110"] < d["chimp_wild"]

finish({
    "object": "M-121",
    "inputs": [
        {"name": "d wild chimps", "value": 0.86, "cite": "evo010@L14 (no source, no parameters key)"},
        {"name": "d humanity 2026", "value": 0.015, "cite": "evo010@L14 (no source, no parameters key)"},
        {"name": "d human, MITTENS window", "value": 0.80, "cite": "evo009@L54; record M-110"},
        {"name": "d human, aDNA estimate", "value": 0.45, "cite": "parameters selection.turnover_d; records M-014, M-114"},
    ],
    "values": {
        "d_values_human_one_fortnight": [0.80, 0.45, 0.015],
        "ratio_0.86_over_0.015": 57.333,
        "ratio_0.80_over_0.015": 53.333,
        "ratio_0.45_over_0.015": 30,
        "ratio_0.80_over_0.45": 1.7778,
        "chart_held": False,
        "chart_url": IMG,
        "source_for_0.86_or_0.015_in_held_text": False,
    },
    "positions": {
        "day": {"reading": "d = 0.86 in wild chimps, 0.015 in 2026 humanity; at 0.015 selection has 'no medium to "
                           "work through' and the genome degrades (since about 1800, Q89)",
                "holds": "both values are stated verbatim and a chart is placed in the post; a falling d over time "
                         "agrees with Day's earlier dating of the change (Q89)"},
        "critic": {"reading": "no data, chart source or derivation for either value; three human d values in one "
                              "fortnight (0.80, 0.45, 0.015)",
                   "holds": "neither value has a held source or parameters key and the chart image is not held; a d "
                            "that changes over time is Camestros's premise (A4b q1), while MITTENS applies one d "
                            "(0.80) over the whole window (M-110)"},
    },
    "notes": "Lookup. 0.86 and 0.015 are quoted, not sourced; the chart is a link (not held). The 0.80 and 0.45 "
             "values are different quantities in time (window average vs aDNA estimate vs 2026 present), so the "
             "spread is a provenance question for parameters.yaml, not an arithmetic error. L26 ('no medium') sits in "
             "the Athos block (M-120 attribution note).",
})
