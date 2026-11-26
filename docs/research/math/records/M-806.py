#!/usr/bin/env python3
"""M-806 record (derivation): the Dawkins figures in Day's 88 Million x post, 642,888 and 87,916,307x.

Object: docs/research/math/objects.yaml M-806 (identity, derivation). Dawkins as posted by Day (secondhand: The
Genetic Book of the Dead not retrieved; Q50 = H3 q1): 11,739 generations to half frequency if dominant, 321,444 if
recessive, for 999 against 1,000 survivors (s about 0.001). Day (Q51 = H3 q2): t_site = 2 x 321,444 = 642,888;
642,888 / 146,250 = 4.3958 (printed "4.4"); x 20,000,000 = 87,916,307.7 (printed 87,916,307, truncated). The doubling
from half frequency to fixation is not explained in the post; the recessive/dominant choice moves the answer by
321,444/11,739 = 27.4; 20M x t_site treats the substitutions as sequential (M-706). The record does not recompute
Haldane's times: the starting frequency behind 11,739 and 321,444 is not held. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-806.py [--write]
Without --write it checks that M-806.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H3 = CL + "H3-dawkins-haldane-figures.md"
QD = "docs/research/sources/quotes-day.md"
PY = "docs/research/parameters.yaml"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
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


# ---- inputs ---------------------------------------------------------------------------------------
Q50 = "His answer was a mere 11,739 generations if the gene is dominant, 321,444 generations if it is recessive."
held(H3, Q50); held(QD, Q50)                                         # H3 q1 = Q50 (secondhand Dawkins)
Q51 = ("Dawkins somehow imagines that even 642,888 generations for one single base pair is more than enough time for "
       "evolution to take place. He’s off by a mere factor of 4.4 x 20 million, or 87,916,307x.")
held(H3, Q51); held(QD, Q51)                                         # H3 q2 = Q51
H3Q3 = held(H3, "that leaves 146,250 generations to fixate all of those base pairs.")                    # H3 q3
SECOND = held(H3, "Dawkins as posted by Day (`secondhand`: The Genetic Book of the Dead, 2024, not retrieved):")
SURV = held(H3, "\"for every 1,000 individuals with the mutation who survive, 999 individuals without the mutation will survive\"")
held(QD, "Figures are Dawkins' (after Haldane), not computed by Day")
held(PY, "dawkins_figures: {value: [11739, 321444]")               # haldane.dawkins_figures
held(PY, "day_2025_effective: {value: 146250")                      # generations_available.day_2025_effective
DOM, REC, G_EFF, N = 11_739, 321_444, 146_250, 20_000_000

# ---- Day's chain ------------------------------------------------------------------------------------
s = 1 - 999 / 1000
near(s, 0.001, 1e-12)                                               # 999 vs 1,000 survivors
t_site = 2 * REC
assert t_site == 642_888                                            # doubling of the recessive half-time
ratio = t_site / G_EFF
near(ratio, 4.3958, 5e-5); assert round(ratio, 1) == 4.4            # printed "4.4"
total = ratio * N
near(total, 87_916_307.69, 0.01)
assert math.floor(total) == 87_916_307 and round(total) == 87_916_308    # printed figure is truncated
near(4.4 * N, 88e6, 1e-6)                                           # the post title's "88 Million x" uses the rounded 4.4
near(4.4 * N / total - 1, 0.00095, 1e-5)                            # 0.1% above the unrounded product

# ---- what the choices move ----------------------------------------------------------------------------
spread = REC / DOM
near(spread, 27.38, 0.005)                                          # recessive/dominant: 27.4x
dom_total = 2 * DOM * N / G_EFF
near(dom_total, 3_210_667, 1)                                       # dominant doubled: 23,478 gens, 3.2 million x
near(total / dom_total, spread, 1e-9)
assert 2 * DOM == 23_478 and 2 * DOM < G_EFF                        # a dominant site, doubled, fits in G_eff 6.2x over
near(G_EFF / (2 * DOM), 6.23, 0.005)
near(REC / G_EFF, 2.198, 5e-4)                                      # without the doubling: 2.2 (factor 2 from the doubling)
serial = N * t_site
near(serial / G_EFF, total, 1e-6)                                   # 20M x t_site / G_eff: substitutions laid end to end

finish({
    "object": "M-806",
    "inputs": [
        {"name": "Dawkins half-frequency times (dominant, recessive)", "value": [DOM, REC], "cite": "Q50 = H3 q1 (secondhand, as posted by Day); parameters haldane.dawkins_figures"},
        {"name": "G_eff", "value": G_EFF, "cite": "H3 q3; parameters generations_available.day_2025_effective (M-802)"},
        {"name": "n", "value": N, "cite": "Q51 = H3 q2 ('20 million')"},
    ],
    "values": {
        "s": round(s, 6), "t_site_2x321444": t_site, "t_site/G_eff": round(ratio, 4),
        "shortfall_exact": round(total, 2), "shortfall_printed_floor": math.floor(total),
        "shortfall_with_4.4": 88_000_000.0, "recessive/dominant": round(spread, 2),
        "dominant_doubled_t_site": 2 * DOM, "dominant_shortfall": round(dom_total),
        "recessive_without_doubling_t/G_eff": round(REC / G_EFF, 3),
    },
    "positions": {
        "day": {"reading": "even 642,888 generations for one base pair exceeds the available time; for 20 million the factor is 87,916,307",
                "holds": "2 x 321,444 = 642,888; 642,888/146,250 = 4.3958; x 20M = 87,916,307.7 (printed truncated)"},
        "critic": {"reading": "a single-allele time to half frequency is not a fixation time for a parallel process; x 20M is serial",
                   "holds": "the factor is 20M x t_site / G_eff, the sequential form (M-706); the doubling is unexplained "
                            "(x2) and the recessive choice multiplies the answer by 27.4 over the dominant one"},
    },
    "notes": "The arithmetic reproduces: 642,888, 4.3958 (4.4), 87,916,307.7 (printed 87,916,307, truncated; 88 million "
             "with 4.4). The Dawkins figures are secondhand (book not retrieved), so the record does not test whether "
             "11,739 and 321,444 follow from s = 0.001: their starting frequency is not held. Three choices set the "
             "answer: the doubling from half frequency (x2, not explained in the post), recessive over dominant "
             "(x27.4; the dominant case doubled is 23,478 generations, 6.2 times inside G_eff) and the serial "
             "multiplication by 20 million (M-706, M-115).",
})
