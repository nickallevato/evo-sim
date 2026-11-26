#!/usr/bin/env python3
"""M-919 record (derivation): the arithmetic of window 1 (t=01:28-02:05, the maths segment) of Gutsick Gibbon with
Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (GG-1, YouTube _Vu0ZVVjwHc, 2026-10-03),
that the library did not hold.

Object: docs/research/math/objects.yaml M-919 (identity, derivation, variant_of M-212). Source map
docs/research/math/sources/gutsick-gibbon-gg1-w1.md (locators gg1@HH:MM:SS = cue start in the 2026-11-26 fetch).
Already settled elsewhere and only loaded here, not recomputed: 252,000 and 180 (M-711); 360 and the shortfall under
each lineage convention (M-012); 76.8, 38.4, 76, 38,707,200 and 19,353,600 (M-213); 4.6e-5, 21,739, 4.1e-4, 2,439 and
the per-genome supply ratio 93,659 (M-007).
The record asserts every number the D-41 item-7 review page states that is not in an earlier record:
- the slide's 205e6 - 180 = 204,999,820;
- Kimura's fixation probability at p0 = 1/(2N) tends to 1/(2N) as s -> 0, and 2N mu x 2s/(4Ns) = mu (Hancock's
  Taylor step, exact on rationals);
- (98 + 206)/2 = 152;
- "orders of magnitude": 76.8 / (180/252,000) = 107,520 and 38.4 / (180/252,000) = 53,760;
- the 38M match: Hancock's first estimate 40M is +3.3% over 38,707,200; on the haploid SNV basis 19,353,600 the
  observed 35-40M SNVs are 1.81-2.07x;
- bacteria: "4e-5" is -13% against 4.6e-5; correcting mu 1e-11 to the measured 8.9e-11 moves the stated 22,000 to 2,439,
  -88.9% (rule R1: past 25%), while 4.1e-4 < 1 < 38.4 keeps his conclusion;
- GG-11: 205e6/(2 x 252,000) = 406.75 ("407"), / 76.8 = 5.30 ("five times"), / 6.4e9 = 6.355e-8 ("6.1e-8", -4.0%),
  / 3.2e9 = 1.271e-7; on Day's per-lineage 205M: 813.49 per generation, 10.59x 76.8, 21.18x 38.4, 2.542e-7 per haploid
  site; R1: 407 -> 813.5 is +100%.
Every quote in the source map's table is asserted to be in the map and, when this checkout holds the fetch, in the
fetched captions; the title is checked against the info JSON. The fifteen quotes on file for the window are checked
in quotes-critics.md as filed, in the 2026-10-14 caption copy when it is on disk, and in the fetched wording.

Run: research/.venv/bin/python -I docs/research/math/records/M-919.py [--write]
Without --write it checks that M-919.json is current; --write saves it.
"""
import hashlib, html, json, math, pathlib, re, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
REC = ROOT / "docs/research/math/records"
DATE = "2026-11-26"
MAP = "docs/research/math/sources/gutsick-gibbon-gg1-w1.md"
VTT = "sources/raw/gg-1-2026-11-26/_Vu0ZVVjwHc.en.vtt"
INFO = "sources/raw/gg-1-2026-11-26/_Vu0ZVVjwHc.info.json"
OLD = "sources/raw/refresh-2026-10-14b/yt-vu0/No, Vox Day's AI-Generated Books Did Not Debunk Evolution [_Vu0ZVVjwHc].en.vtt"
QC = "docs/research/sources/quotes-critics.md"


def norm(s):
    return " ".join(s.split())


def near(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


def val(m, *path):
    v = json.loads((REC / f"{m}.json").read_text(encoding="utf-8"))["values"]
    for p in path:
        v = v[p]
    return v


def captions(path):
    """Cue texts in order, rolling duplicates dropped, tags removed, entities unescaped (as vtt.py)."""
    out, last = [], ""
    for line in path.read_text(encoding="utf-8").split("\n"):
        if re.match(r"\d\d:\d\d:\d\d\.\d+ --> ", line) or not line.strip():
            continue
        if line.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        txt = html.unescape(re.sub(r"<[^>]+>", "", line).strip())
        if txt and txt != last:
            out.append(txt)
            last = txt
    return " ".join(out)


# ---- the source sentences ---------------------------------------------------------------------------
MAP_TEXT = (ROOT / MAP).read_text(encoding="utf-8")
CAP = norm(captions(ROOT / VTT)) if (ROOT / VTT).exists() else None
OLD_CAP = norm(captions(ROOT / OLD)) if (ROOT / OLD).exists() else None
TITLE = "No, Vox Day's AI-Generated Books Did Not Debunk Evolution"
if (ROOT / INFO).exists():
    info = json.loads((ROOT / INFO).read_text(encoding="utf-8"))
    assert info["id"] == "_Vu0ZVVjwHc" and info["upload_date"] == "20261003" and info["duration"] == 12_628
    assert info["title"] == TITLE and 3 * 3600 + 30 * 60 + 28 == 12_628

rows = [l for l in MAP_TEXT.splitlines() if l.startswith("| gg1")]
seen_gg = set()
for l in rows:
    loc, speaker, cell = l.split(" | ")[0][2:], l.split(" | ")[1], l.split(" | ")[2]
    q = re.match(r'^"(.*)"(?: \((GG-\d\d)\))?$', cell)
    assert q, cell[:60]
    if q.group(2):
        seen_gg.add(q.group(2))
    if loc == "gg1@title":
        assert q.group(1) == TITLE
    elif CAP is not None:
        assert norm(q.group(1)) in CAP, (loc, q.group(1)[:60])
assert len(rows) == 64, len(rows)

# quotes on file for the window: as filed (quotes-critics.md, 2026-10-14 copy) and as fetched (this map)
ON_FILE = {
    "GG-01": ("it assumes that each mutation has to both arise and go to fixation before the next mutation can occur.", None),
    "GG-02": ("this basic math is off by a factor of two", None),
    "GG-03": ("and then what you're left with is a neutral substitution rate that's equal to the mutation rate", None),
    "GG-04": ("that's about 76.8 uh new mutations that are fixed in the population every single generation.", None),
    "GG-05": ("we can't use 6.4. This is the diploid genome size for the fixation rate because you fix on a hloid genome. So, it should be 3.2 e to the 9.",
              "we can't use 6.4. This is the diploid genome size for the fixation rate, because you fix on a haploid genome. So, it should be 3.2 e to the nine, okay?"),
    "GG-06": ("If we divide that in half to take the the hloid genome size that gives us 76.",
              "If we divide that in half to take the the haploid genome size, that gives us 76."),
    "GG-07": ("you only expect four e to the neg5 mutations to fix per generation.",
              "you only expect 4 e to the -5 mutations to fix per generation."),
    "GG-08": ("under neutrality, it should take like 22,000 generations to fix one mutation.", None),
    "GG-09": ("we'll say about 38 million.", "We'll say about 38 million."),
    "GG-10": ("the number is 205 million differences, right?", None),
    "GG-11": ("when you divide this out over 200 205 million you get something like 407",
              "when you divide this out uh over 200 205 million, you get something like 407."),
    "GG-12": ("we can account even for the highest end of the mutational differences with a model that assumes that selection was not involved at all.", None),
    "GG-13": ("there would basically be no genetic variation amongst individuals except for the mutation that's increasing in frequency", None),
    "GG-24": ("Notice that his model had no mutation rate, right?", None),
    "GG-25": ("this is not even necessarily a measure of selection", None),
}
qc = (ROOT / QC).read_text(encoding="utf-8")
exact_new = 0
for k, (filed, fetched) in ON_FILE.items():
    assert f'- **{k}**' in qc and f'> "{filed}"' in qc, k
    if OLD_CAP is not None:
        assert norm(filed) in OLD_CAP, k
    form = fetched or filed
    assert norm(form) in MAP_TEXT, k
    if CAP is not None:
        assert norm(form) in CAP, k
        exact_new += norm(filed) in CAP
assert seen_gg >= set(ON_FILE), set(ON_FILE) - seen_gg
if CAP is not None:
    assert exact_new == 10, exact_new                              # GG-05, -06, -07, -11 differ in wording; -09 in a capital
    for ctx in ("reached fixation in the human lineage?",          # gg1@01:26:23, the slide's lineage
                "fixed in the human lineage since our hypothesized divergence",   # gg1@01:26:49
                "as you can see here from Will's slides or presentation",         # gg1@00:32:12
                "Moving on to issue two, this Will says is the more damning",     # gg1@01:23:53
                "think it's around the range of about 40 million",                # gg1@01:56:14
                "38,707,200",                                                     # gg1@01:56:37
                "again, it's wrong, but I think it still"):                       # gg1@02:03:36
        assert ctx in CAP, ctx
    assert "Appendix" not in CAP and "fixation must be sequential" not in CAP

# ---- reused, loaded from their records -----------------------------------------------------------------------------
T = val("M-711", "generations")
F_MAX = val("M-711", "fixations_book")
assert T == 252_000 and F_MAX == T / 1_400 == 180
assert 2 * F_MAX == 360 and val("M-012", "shortfall_day_per_lineage") == val("M-012", "shortfall_hancock_total") == 1_138_890
assert val("M-012", "shortfall_both_double_count") == 569_444
K_DIP, K_HAP, K_76 = val("M-213", "per_gen", "diploid"), val("M-213", "per_gen", "haploid"), val("M-213", "per_gen", "cited_halved")
assert (K_DIP, K_HAP, K_76) == (76.8, 38.4, 76)
near(1.2e-8 * 6.4e9, K_DIP, 1e-9)
near(1.2e-8 * 3.2e9, K_HAP, 1e-9)
C_DIP, C_HAP = val("M-213", "counts", "diploid_x2"), val("M-213", "counts", "haploid_x2")
assert C_DIP == 38_707_200 and C_HAP == 19_353_600
assert round(2 * T * K_DIP) == C_DIP and round(2 * T * K_HAP) == C_HAP
U_E_HANCOCK, GEN_HANCOCK = val("M-007", "neutral_supply_hancock"), val("M-007", "gens_per_fix_hancock")
U_E_MEAS, GEN_MEAS = val("M-007", "neutral_supply_measured"), val("M-007", "gens_per_fix_at_4.1e-4")
assert U_E_HANCOCK == 4.6e-05 and GEN_HANCOCK == 21739.1 and GEN_MEAS == 2439.02
near(val("M-007", "kappa"), 93_658.5, 0.1)

# ---- the slide (gg1@01:28:09) ------------------------------------------------------------------------------------
REQ = 205_000_000
assert REQ - F_MAX == 204_999_820

# ---- Kimura's fixation probability and the Taylor step (gg1@01:43:58-01:48:50) -------------------------------------


def u_fix(N, s):
    """(1 - e^(-4 N s p0)) / (1 - e^(-4 N s)) at p0 = 1/(2N), as spoken (N in both places)."""
    return -math.expm1(-2 * s) / -math.expm1(-4 * N * s)


for N in (1_000, 10_000, 100_000):
    for s in (1e-9, 1e-11):
        near(u_fix(N, s) * 2 * N, 1.0, 4 * N * s)        # first-order error ~ 2Ns
N_, mu_, s_ = Fr(10_000), Fr(12, 10**9), Fr(1, 10**9)
assert 2 * N_ * mu_ * (2 * s_) / (4 * N_ * s_) == mu_              # "2 n mu 2 s over 4 n s" = 2N mu x 1/(2N) = mu

# ---- de novo count (gg1@01:53:22, 01:53:30) ---------------------------------------------------------------------
DN = (98 + 206) / 2
assert DN == 152 and DN / 2 == K_76

# ---- "orders of magnitude" (gg1@01:52:18) ------------------------------------------------------------------------
rate_day = F_MAX / T                                               # fixations per generation on the slide
near(rate_day, 7.142857e-4, 1e-9)
oom_dip, oom_hap = K_DIP / rate_day, K_HAP / rate_day
near(oom_dip, 107_520, 1e-6)
near(oom_hap, 53_760, 1e-6)
near(math.log10(oom_dip), 5.03, 0.005)

# ---- the 38M match (gg1@01:56:14-01:57:10) ------------------------------------------------------------------------
near((40e6 - C_DIP) / C_DIP, 0.0334, 0.0005)                       # first estimate "about 40 million"
assert 35e6 <= C_DIP <= 40e6                                       # inside his 35-40M on the diploid basis
snv_lo, snv_hi = 35e6 / C_HAP, 40e6 / C_HAP
near(snv_lo, 1.808, 0.0005)
near(snv_hi, 2.067, 0.0005)

# ---- bacteria (gg1@01:54:04-01:54:31) ----------------------------------------------------------------------------
near((4e-5 - U_E_HANCOCK) / U_E_HANCOCK, -0.1304, 0.0005)          # "4 e to the -5" against 1e-11 x 4.6e6
near(1 / 4e-5, 25_000, 1e-6)
near((22_000 - GEN_HANCOCK) / GEN_HANCOCK, 0.012, 0.0005)          # "like 22,000" against 21,739
r1_bact = (GEN_MEAS - 22_000) / 22_000
near(r1_bact, -0.8891, 0.0005)                                     # R1: -88.9%, past 25%
assert U_E_MEAS < 1 < K_HAP                                        # his conclusion survives

# ---- GG-11 and the per-lineage reading (gg1@02:00:51-02:01:20) ----------------------------------------------------
need_tot = REQ / (2 * T)                                           # 205M read as a two-lineage total
near(need_tot, 406.746, 0.0005)
near(need_tot / K_DIP, 5.296, 0.0005)                              # "around five times"
r_dip, r_hap = need_tot / 6.4e9, need_tot / 3.2e9
near(r_dip, 6.355e-8, 5e-11)
near((6.1e-8 - r_dip) / r_dip, -0.040, 0.0005)                     # "6.1 e to the -8": -4.0%
near(r_hap, 1.271e-7, 5e-11)
need_lin = REQ / T                                                 # Day's 205M per human lineage (Q14, Q15)
near(need_lin, 813.492, 0.0005)
near(need_lin / K_DIP, 10.592, 0.0005)
near(need_lin / K_HAP, 21.185, 0.0005)
near(need_lin / 3.2e9, 2.542e-7, 5e-11)
assert need_lin / need_tot == 2                                    # R1: 407 -> 813.5 is +100%


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


finish({
    "object": "M-919",
    "variant_of": "M-212",
    "inputs": [
        {"name": "T, G_f, required", "value": [T, 1_400, REQ], "cite": "gg1@01:28:09-01:28:37 (slide; Q91, Q14; M-711)"},
        {"name": "mu, L diploid, L haploid", "value": [1.2e-8, 6.4e9, 3.2e9], "cite": "gg1@01:51:08-01:51:32, 01:52:48 (M-213)"},
        {"name": "de novo range", "value": [98, 206], "cite": "gg1@01:53:22"},
        {"name": "E. coli mu stated, measured; L", "value": [1e-11, 8.9e-11, 4.6e6], "cite": "gg1@01:54:04; M-007"},
        {"name": "observed SNV divergence (spoken)", "value": [35e6, 40e6], "cite": "gg1@01:57:02"},
    ],
    "values": {
        "slide_short": REQ - F_MAX,
        "kimura_limit_2N_u": 1.0,
        "de_novo_mean": DN,
        "orders_of_magnitude": {"day_rate_per_gen": round(rate_day, 9), "at_76.8": round(oom_dip), "at_38.4": round(oom_hap)},
        "match_38M": {"first_estimate_move": round((40e6 - C_DIP) / C_DIP, 4), "snv_over_haploid": [round(snv_lo, 3), round(snv_hi, 3)]},
        "bacteria": {"said_4e-5_move": round((4e-5 - U_E_HANCOCK) / U_E_HANCOCK, 4), "inverse_4e-5": 25_000,
                     "said_22000_move": round((22_000 - GEN_HANCOCK) / GEN_HANCOCK, 4), "r1_to_measured": round(r1_bact, 4)},
        "gg11": {"per_gen_total": round(need_tot, 3), "over_76.8": round(need_tot / K_DIP, 3),
                 "rate_diploid": float(f"{r_dip:.4g}"), "said_rate_move": round((6.1e-8 - r_dip) / r_dip, 4),
                 "rate_haploid": float(f"{r_hap:.4g}"),
                 "per_gen_per_lineage": round(need_lin, 3), "per_lineage_over_76.8": round(need_lin / K_DIP, 3),
                 "per_lineage_over_38.4": round(need_lin / K_HAP, 3), "per_lineage_rate_haploid": float(f"{need_lin / 3.2e9:.4g}"),
                 "r1_move": 1.0},
        "quotes": {"map_rows": len(rows), "on_file": len(ON_FILE), "on_file_exact_in_fetch": exact_new if CAP is not None else None},
    },
    "positions": {
        "day": {"reading": "the 205M is per human lineage (slide gg1@01:26:49; Q14) and G_f is a parallel throughput (slide gg1@01:28:09; Q125)",
                "holds": "the factor of two and GG-11's 407 treat 205M as a two-lineage total: per lineage 813.5 per generation, "
                         "10.6x 76.8 and 21.2x the haploid SNV 38.4; the 38M match is on the diploid 76.8, and on 38.4 the SNV "
                         "count is 19.35M, 1.81-2.07x short of the 35-40M he cites; the E. coli 22,000 is 2,439 at the measured mu"},
        "critic": {"reading": "neutral supply is the null: k = mu, 2 T mu L, with E. coli's supply 93,659x below the human genome's (M-007)",
                   "holds": "k = mu reproduces exactly (2N mu x 2s/(4Ns) = mu); 76.8 per generation is 107,520x the slide's 180 per "
                            "252,000 (53,760x at 38.4); 1,400 is E. coli's throughput and 2,439 its neutral clock; the slide's "
                            "205M is bases, not events (M-011), so 407 or 813 per generation is not a point-mutation rate"},
    },
    "notes": "Rationals for the Taylor identity; floats elsewhere. The Kimura limit is checked numerically at s = 1e-9 and "
             "1e-11 for N = 1e3-1e5. The ancestral-polymorphism remainder (about 15M SNVs) is B5c's R4 B4a and is not "
             "recomputed. The fetched caption track differs from the 2026-10-14 copy in recogniser wording only.",
})
