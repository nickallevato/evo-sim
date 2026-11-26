#!/usr/bin/env python3
"""M-002 record (lookup): divergence-time and generation-length inputs, and N_gen = t_div / g_len.

Object: docs/research/math/objects.yaml M-002 (parameter, lookup). Each value is quoted verbatim
from held text with its locator (quote id in docs/research/sources/quotes-day.md, or the claim
file's Statement blockquote); held() checks the quote against that file. One value, Day's
alternative g_len = 32.5 y (B2025-01-18), has no held verbatim quote: it is read from
parameters.yaml (verified: false) and flagged in the JSON.

Run: research/.venv/bin/python -I docs/research/math/records/M-002.py [--write]
Without --write it checks that M-002.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def g(x):
    return float(f"{x:.6g}")


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


# ---- lookups: value, verbatim quote, locator ---------------------------------------------
L = []


def look(name, value, rel, quote, locator):
    L.append({"name": name, "value": value, "quote": held(rel, quote), "locator": locator})
    return value


t19 = look("t_div Day 2019", 9.0e6, QD, "CHLCA Years: 9,000,000 Years per generation: 20",
           "Q03, B2019-02-07 ¶19")
g19 = look("g_len Day 2019", 20, QD, "CHLCA Years: 9,000,000 Years per generation: 20",
           "Q03, B2019-02-07 ¶19")
t25 = look("t_div Day 2025 (range), g_len 20", [6e6, 7e6], QD,
           "Time available: 6–7 million years at 20 years/generation = 300,000–350,000 nominal generations.",
           "Q12, Z18165980 ¶34")
t30 = look("t_div Day MITTENS 3.0", 6.3e6, QD, "The divergence time is 6.3 million years.", "Q18, Z23003785 p.11")
g30 = look("g_len Day MITTENS 3.0", 25, QD, "At 25 years per human generation, this provides 252,000 generations.",
           "Q18, Z23003785 p.11")
tyoo = look("t_div Yoo et al. 2025 (min-max)", [5.5e6, 6.3e6], CL + "A1a-divergence-time-literature.md",
            "Our analyses dated the human-chimpanzee split between 5.5 and 6.3 million years ago (Ma; minimum to "
            "maximum estimate of divergence)", "A1a q1, Yoo et al. 2025 main text, Divergence and selection")
tlan = look("t_div Langergraber et al. 2012 (lower bound)", [7e6, 8e6], CL + "A1a-divergence-time-literature.md",
            "We date the human-chimpanzee split to at least 7-8 million years", "A1a q2, Langergraber et al. 2012 Abstract")
tsca = look("t_div Scally et al. 2012 (approximate)", 6e6, CL + "A1a-divergence-time-literature.md",
            "placing the human-chimpanzee and human-chimpanzee-gorilla speciation events at approximately 6 and 10 "
            "million years ago (Mya)", "A1a q3, Scally et al. 2012 Abstract")
trev = look("t_div Day revision 2026-05-07", [2.5e5, 1.3e6], QD,
            "the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed.",
            "Q68, B2026-05-07 ¶7")
gqa = look("g_len Day Q&A", 22, QD, "T = 22 years (generation, Gurven & Kaplan 2007)", "Q44, B2026-01-19 ¶5")
galt = look("g_len Day alternative (NO held verbatim quote; parameters.yaml, verified: false)", 32.5, PY,
            "day_alt: {value: 32.5, source: B2025-01-18, verified: false}",
            "parameters.yaml generation_time_years.day_alt (source B2025-01-18; raw page not in the local checkout)")
gchimp = look("chimpanzee generation time, Langergraber et al. 2012", [24.3, 24.9], CL + "A1b-generation-length-literature.md",
              "The average generation time for the former communities was 24.9, whereas it was 24.3 for the latter.",
              "A1b q1, Langergraber et al. 2012 Results")

# ---- N_gen = t_div / g_len ---------------------------------------------------------------
n30 = t30 / g30
assert n30 == 252_000                                  # Q18
n19 = t19 / g19
assert n19 == 450_000                                  # 2019 (Q04 prints 450,000)
n25 = [t / 20 for t in t25]
assert n25 == [300_000, 350_000]                       # Q12
n_min = tyoo[0] / galt
assert round(n_min) == 169_231                         # 5.5 My at 32.5 y
n_max = n19                                            # 9 My at 20 y
spread = near(n_max / n_min, 2.66, 0.005)              # "2.7x"
n_lan = tlan[1] / g30
assert n_lan == 320_000
near(n_lan / n30, 1.27, 0.005)                         # Langergraber 8 My at 25 y against 252,000
n_chimp = t30 / gchimp[1]
assert round(n_chimp) == 253_012                       # 6.3 My at 24.9 y, 0.4% from 252,000
near(n_chimp / n30 - 1, 0.004, 0.0005)
n_rev = [t / g30 for t in trev]
assert n_rev == [10_000, 52_000]                       # revision range at 25 y
assert round(t30 / gqa) == 286_364 and round(t30 / galt) == 193_846
assert t30 == tyoo[1]                                  # 6.3 My is the Yoo maximum

# critic: the input range alone (2.7x) cannot close a 1e5-1e6 shortfall
assert spread < 1e5

finish({
    "object": "M-002",
    "inputs": L,
    "values": {
        "N_gen_3.0": n30, "N_gen_2019": n19, "N_gen_2025_range": n25,
        "N_gen_min_5.5My_32.5y": g(n_min), "N_gen_max_9My_20y": n_max, "range_factor": g(spread),
        "N_gen_langergraber_8My_25y": n_lan, "ratio_langergraber_to_3.0": g(n_lan / n30),
        "N_gen_6.3My_24.9y": g(n_chimp), "N_gen_revision_range_25y": n_rev,
        "N_gen_6.3My_22y": g(t30 / gqa), "N_gen_6.3My_32.5y": g(t30 / galt),
        "day_3.0_t_div_is_yoo_max": True,
    },
    "positions": {
        "day": {"t_div": t30, "g_len": g30, "N_gen": n30,
                "dates": "revision 250 kya-1.3 Mya posted 2026-05-07 (Q68); MITTENS 3.0 with 6.3 My published 2026-09-28 (Q18)"},
        "critic": {"literature_t_div": "5.5 to at least 8 My", "literature_g_len_chimp": gchimp,
                   "range_factor": g(spread), "closes_1e5_shortfall": False},
    },
    "unverified": ["g_len 32.5 y (day_alt): value from parameters.yaml only, verified: false; no verbatim quote held "
                   "(sources/raw/day/blog-2025-01-18-generational-length-update.html is not in the local checkout)"],
})
