#!/usr/bin/env python3
"""M-918 record (derivation): the arithmetic of Jan Ghijselen's "Will Duffy's math on Gutsick Gibbon's channel."
(JG-1, YouTube nTVRiEcswI8, 2026-09-28) and his replies in the comments that the library did not hold.

Object: docs/research/math/objects.yaml M-918 (identity, derivation, variant_of M-706). Source map
docs/research/math/sources/ghijselen-jg1.md (locators jg1@MM:SS, jg1c#<id>, B2026-09-30).
Already settled elsewhere and only loaded here, not recomputed: 6.3e6/25 = 252,000 and 252,000/1,400 = 180 (M-711);
the serial and aggregate readings coincide only without overlap (M-706); 4 x 1e4 (M-914).
The record asserts every number the D-41 item-6 review page states that is not in an earlier record:
- the per-fixation time two ways: 25 x 1,400 = 35,000 y and 6.3e6/180 = 35,000 y (same quantity, T / F_max = g G_f);
- the marathon: 60,000 x 4 h = 240,000 h = 10,000 d = 27.38 y ("27", -1.4%);
- the marathon as M-706's overlap case at a constructed bound (all 60,000 run the same 4 h): time per finisher at the
  line G_f = 4 h / 60,000 = 0.24 s, mean concurrency t / G_f = 60,000, serial count in the 4 h window 1 against the
  aggregate 60,000, ratio = concurrency; the serial total n t = 240,000 h is n times the parallel finish time;
- the comment's logarithm: 2e6/200 = 1e4, log10 1e4 = 4; under the exponent reading ln(p^n) = n ln p the ratio stays
  1e4 for any p (checked at p = 0.02 and 1/20,000); under the concurrent-completion reading ln(2e6)/ln(200) = 2.738 and
  for exponential durations H_2e6 / H_200 = 2.566; the printed 4 is +46% over 2.738;
- neutral fixation time: 4Ne = 40,000 at Ne = 10,000, above the comment's "more than 10 000 generations".
Every quote in the source map's table is asserted to be in the map and, when this checkout holds the fetch, in the
fetched captions (video rows) or the uploader's comments (jg1c rows); Day rows are checked against the claim file and
bibliography that hold them.

Run: research/.venv/bin/python -I docs/research/math/records/M-918.py [--write]
Without --write it checks that M-918.json is current; --write saves it.
"""
import hashlib, html, json, math, pathlib, re, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
REC = ROOT / "docs/research/math/records"
DATE = "2026-11-26"
MAP = "docs/research/math/sources/ghijselen-jg1.md"
VTT = "sources/raw/jg-1-2026-11-26/nTVRiEcswI8.en.vtt"
COM = "sources/raw/jg-1-2026-11-26/comments/nTVRiEcswI8.info.json"
QC = "docs/research/sources/quotes-critics.md"
G2A = "docs/research/claims/G2a-marathon-analogy.md"
BIBD = "docs/research/sources/bib-day.md"


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
CAP = captions(ROOT / VTT) if (ROOT / VTT).exists() else None
OWN = None
if (ROOT / COM).exists():
    info = json.loads((ROOT / COM).read_text(encoding="utf-8"))
    assert info["id"] == "nTVRiEcswI8" and info["upload_date"] == "20260928" and info["duration"] == 293
    OWN = {c["id"][-11:]: c["text"] for c in info["comments"] if c.get("author_is_uploader")}
    assert len(info["comments"]) == 124 and len(OWN) == 44

rows = [l for l in MAP_TEXT.splitlines() if l.startswith(("| jg1", "| B2026-09-30"))]
assert len(rows) == 34, len(rows)
video = comments = 0
for l in rows:
    loc, cell = l.split(" | ")[0][2:], l.split(" | ")[2]
    q = re.match(r'^"(.*)"(?: \(DZ-0\d\))?$', cell)
    assert q, cell[:60]
    q = q.group(1)
    if loc.startswith("jg1@"):
        video += 1
        if CAP is not None:
            assert norm(q) in norm(CAP), q[:60]
    elif loc.startswith("jg1c#"):
        comments += 1
        if OWN is not None:
            assert q in OWN[loc[5:]], (loc, q[:60])                    # exact substring of his own reply
    elif loc == "B2026-09-30@title":
        assert f"| {q} |" in (ROOT / BIBD).read_text(encoding="utf-8")
    else:
        assert norm(q) in norm((ROOT / G2A).read_text(encoding="utf-8")), q[:60]
assert (video, comments) == (15, 16)
ON_FILE = {  # quotes-critics.md DZ-01..DZ-03, verbatim
    "DZ-01": "Of course you say that's not possible, they run parallel. Well, the same goes with mutation and fixation.",
    "DZ-02": "The length of a generation for humans is 25 years times 1,000 400",
    "DZ-03": "I am a math teacher in secondary education.",
}
qc = (ROOT / QC).read_text(encoding="utf-8")
for k, q in ON_FILE.items():
    assert f'> "{q}"' in qc and q in MAP_TEXT, k
    if CAP is not None:
        assert norm(q) in norm(CAP), k

# ---- reused, loaded from their records -----------------------------------------------------------------------------
T_Y, G, GF, D = 6_300_000, 25, 1_400, 1
assert val("M-711", "generations") == T_Y / G == 252_000
F_MAX = val("M-711", "fixations_book")
assert F_MAX == T_Y * D / (G * GF) == 180

# ---- per-fixation time, two ways (jg1@02:33, jg1@03:04) --------------------------------------------------------
per_fix = G * GF
assert per_fix == 35_000 and T_Y / F_MAX == per_fix               # T / F_max = g G_f / d, the same quantity

# ---- the marathon (jg1@03:32, jg1@04:09) ---------------------------------------------------------------------
N_RUN, T_RUN = 60_000, 4                                           # runners, hours each
hours = N_RUN * T_RUN
days = hours / 24
years = days / 365.25
assert hours == 240_000 and days == 10_000
near(years, 27.38, 0.005)
said = 27
near((said - years) / years, -0.0139, 0.0005)                      # "27": truncation, -1.4%

# the marathon as M-706's overlap case, at a constructed bound: all 60,000 run the same 4 h window
W = Fr(T_RUN * 3600)                                               # seconds
gf_line = W / N_RUN                                                # time per finisher at the line
assert gf_line == Fr(6, 25)                                        # 0.24 s
concurrency = Fr(T_RUN * 3600) / gf_line
assert concurrency == N_RUN
serial_in_W, aggregate_in_W = W / (T_RUN * 3600), W / gf_line
assert serial_in_W == 1 and aggregate_in_W == N_RUN and aggregate_in_W / serial_in_W == concurrency
assert N_RUN * T_RUN / T_RUN == N_RUN                              # serial total n t is n times the parallel 4 h

# ---- the comment's logarithm (jg1c#AbOZjfoynVk) ----------------------------------------------------------------
n_small, n_big = 200, 2_000_000
ratio = n_big / n_small
assert ratio == 10_000 and math.log10(ratio) == 4
for p in (0.02, 1 / 20_000):                                       # exponent reading: ln p^n = n ln p
    near((n_big * math.log(p)) / (n_small * math.log(p)), 10_000, 1e-6)
ln_ratio = math.log(n_big) / math.log(n_small)
near(ln_ratio, 2.738, 0.0005)
near(math.log10(n_big) / math.log10(n_small), ln_ratio, 1e-12)     # base-free


def harmonic(k):
    return math.fsum(1 / i for i in range(1, k + 1))


h_small, h_big = harmonic(n_small), harmonic(n_big)               # E[max of k iid Exp(1)] = H_k
near(h_big - (math.log(n_big) + 0.5772156649 + 1 / (2 * n_big)), 0, 1e-9)
h_ratio = h_big / h_small
near(h_ratio, 2.566, 0.0005)
move = (4 - ln_ratio) / ln_ratio
near(move, 0.461, 0.0005)                                          # "4" over 2.738: +46% (conclusion unchanged)

# ---- neutral fixation time (jg1c#AbPZ3OnnqSO) ------------------------------------------------------------------
NE = 10_000
assert 4 * NE == 40_000 > 10_000 and 2 * NE == 20_000 > 10_000


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
    "object": "M-918",
    "variant_of": "M-706",
    "inputs": [
        {"name": "t_div_years, g_len, G_f, d", "value": [T_Y, G, GF, D], "cite": "jg1@01:03-01:46 (Duffy's values as Ghijselen reads them; M-711)"},
        {"name": "marathon", "value": {"runners": N_RUN, "hours_each": T_RUN}, "cite": "jg1@03:32"},
        {"name": "base_pair_counts", "value": [n_small, n_big], "cite": "jg1c#AbOZjfoynVk"},
        {"name": "Ne", "value": NE, "cite": "M-914 (Day's 4 x 1e4)"},
    ],
    "values": {
        "years_per_fixation": {"g_x_Gf": per_fix, "T_over_Fmax": per_fix},
        "marathon": {"hours": hours, "days": days, "years": round(years, 2), "said": said,
                     "said_move": round((said - years) / years, 4)},
        "marathon_overlap_bound": {"window_s": int(W), "G_f_line_s": float(gf_line), "concurrency": int(concurrency),
                                   "serial_in_window": int(serial_in_W), "aggregate_in_window": int(aggregate_in_W)},
        "log_comment": {"ratio": ratio, "log10_ratio": 4.0, "exponent_reading_ratio": 10_000,
                        "ln_ratio": round(ln_ratio, 4), "harmonic_ratio": round(h_ratio, 4),
                        "said": 4, "said_over_ln_ratio": round(move, 3)},
        "neutral": {"4Ne": 4 * NE, "2Ne": 2 * NE, "said_more_than": 10_000},
        "quotes": {"video_rows": video, "comment_rows": comments, "day_rows": len(rows) - video - comments,
                   "uploader_comments_held": 44 if OWN is not None else None},
    },
    "positions": {
        "day": {"reading": "G_f = T_obs / n_obs is a throughput that already counts overlapping fixations (G1 q1; ¶7)",
                "holds": "35,000 years is the mean spacing g G_f, not one allele's time; the marathon's analogue of G_f is the "
                         "0.24 s per finisher at the line, not 4 h per runner, so T/G_f counts right at any overlap (M-706); "
                         "the comment's '4 times' reproduces under neither reading (1e4 or 2.74)"},
        "critic": {"reading": "the 180 is a serial count: one allele per 35,000 years (the book's Appendix A, G2g q1)",
                   "holds": "on that reading the marathon is exact: n t = 240,000 h against 4 h in parallel, a factor of n; "
                            "the concurrent-completion reading makes the time grow as ln k (2.74x from 200 to 2e6), not as k"},
    },
    "notes": "Exact on rationals for the marathon bound; floats elsewhere. The 0.24 s line time is a constructed bound "
             "(all runners in one 4 h window), not a race statistic; with a longer finish window the line time grows and "
             "the concurrency falls, the identity is unchanged. The H_k ratio models each duration as Exp(1); it is one "
             "charitable reading of the comment, not a population-genetics model, and it needs all k changes present at once.",
})
