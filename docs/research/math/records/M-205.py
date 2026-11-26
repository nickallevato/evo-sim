#!/usr/bin/env python3
"""M-205 record: census ceiling N < (Vk + 2) G / 16 + 1/2 from Ne = (4N - 2)/(Vk + 2) and 4 Ne < G.

Object: docs/research/math/objects.yaml M-205 (formula, derivation). The algebra is solved exactly,
then the species rows of Hard Limits Table 1 (as transcribed in claim file B2b, with Table 2's halved
and doubled Vk) are recomputed against Day's printed ceilings, and the abstract's "about ten
thousand" is compared with them. Inputs carry their quote id or claim file; held() checks each quote
verbatim. Mouse and fly inputs are flagged in the claim file as pending a proper source.

Run: research/.venv/bin/python -I docs/research/math/records/M-205.py [--write]
Without --write it checks that M-205.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
B2B = CL + "B2b-ceiling-x-vk-g-over-16.md"


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


def ne(n, vk):
    return (4 * n - 2) / (vk + 2)


def ceiling(vk, G):
    return (vk + 2) * G / 16


# ---- inputs -------------------------------------------------------------------------------
Q29 = held(CL + "B2-hard-limits-domain-of-k-mu.md",
           "Checking them yields a hard ceiling on population size, X = (Vₖ + 2)·G/16 — reproductive variance and "
           "lineage generations alone, with no mutation rate, no coalescent quantity, and no fitted constant.")
Q32 = held(B2B, "Nₑ = (4N − 2) / (Vₖ + 2)")
TENK = held(B2B, "For a large, long-lived vertebrate the effective ceiling falls to about ten thousand individuals.")
Q33 = held(B2B, "The human’s is thirty-five thousand as a species, a hundred thousand as a lineage. The elephant’s is twenty-eight thousand.")
DOMAIN = held(CL + "B2-hard-limits-domain-of-k-mu.md",
              "The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting.")
ROWS = {  # name: (T years, g years, Vk, Day's X), claim file B2b audit table (HL Table 1)
    "human_lineage": (6.5e6, 25, 5, 114_000, held(B2B, "| Homo sapiens (lineage) | 6.5, 25, 5 | 260,000 | 113,750 | 114,000 |")),
    "human_species": (2.0e6, 25, 5, 35_000, held(B2B, "| H. sapiens (species window) | 2.0, 25, 5 | 80,000 | 35,000 | 35,000 |")),
    "elephant": (2.0e6, 22, 3, 28_000, held(B2B, "| Loxodonta | 2.0, 22, 3 | 90,909 | 28,409 | 28,000 |")),
    "mouse": (1.5e6, 0.5, 25, 5.1e6, held(B2B, "| Mus musculus | 1.5, 0.5, 25 | 3.0e6 | 5.06e6 | 5.1e6 |")),
    "fly": (5.0e6, 0.08, 400, 1.57e9, held(B2B, "| D. melanogaster | 5.0, 0.08, 400 | 6.25e7 | 1.57e9 | 1.57e9 |")),
}
CENSUS = held(CL + "B2-hard-limits-domain-of-k-mu.md", "population.census_human = 8.2e9` (HL Table 1)")
KERURU = held(CL + "B2e-keruru-measured-ne-vs-wright.md", "it is wrong by three orders of magnitude")

# ---- algebra: 4 Ne < G  <=>  N < (Vk + 2) G / 16 + 1/2 -------------------------------------
for vk in (0, 3, 5, 25, 400):
    for G in (8e4, 2.6e5, 6.25e7):
        n_star = ceiling(vk, G) + 0.5
        near(4 * ne(n_star, vk), G, 1e-6 * G)            # boundary is exact
        assert 4 * ne(n_star - 1, vk) < G < 4 * ne(n_star + 1, vk)

# ---- species rows ---------------------------------------------------------------------------
X = {}
for k, (Ty, gy, vk, day_x, _) in ROWS.items():
    G = Ty / gy
    X[k] = ceiling(vk, G)
    assert abs(X[k] - day_x) / day_x < 0.015, (k, X[k], day_x)  # each printed ceiling within 1.5% (rounding)
near(X["human_lineage"], 113_750, 1e-6)
assert X["human_species"] == 35_000
near(X["elephant"], 28_409.1, 0.1)
near(X["mouse"], 5.0625e6, 1)
near(X["fly"], 1.5703e9, 0.0001e9)
assert abs(X["human_lineage"] - 100_000) / 100_000 < 0.14   # Q33 "a hundred thousand as a lineage" (114,000 in table)
# Table 2: Vk halved and doubled
t2 = {k: (ceiling(ROWS[k][2] / 2, ROWS[k][0] / ROWS[k][1]), ceiling(ROWS[k][2] * 2, ROWS[k][0] / ROWS[k][1]))
      for k in ("human_species", "elephant", "mouse", "fly")}
assert t2["human_species"] == (22_500, 60_000)
near(t2["elephant"][0], 19_886, 1); near(t2["elephant"][1], 45_455, 1)
near(t2["mouse"][0], 2.72e6, 0.01e6); near(t2["mouse"][1], 9.75e6, 0.01e6)
near(t2["fly"][0], 7.89e8, 0.01e8); near(t2["fly"][1], 3.13e9, 0.01e9)

# ---- the abstract's "about ten thousand" against the table ------------------------------------
ten_k = 10_000
near(X["human_species"] / ten_k, 3.5, 1e-9)
near(X["human_lineage"] / ten_k, 11.375, 1e-9)
near(X["elephant"] / ten_k, 2.84, 0.01)
assert all(X[k] > 2.5 * ten_k for k in ("human_species", "human_lineage", "elephant"))

# ---- human census against the ceiling; implied Ne at census ------------------------------------
over = 8.2e9 / X["human_lineage"]
near(over, 72_088, 1)                                    # Day 72,000
ne_census = ne(8.2e9, 5)
near(ne_census, 4.686e9, 0.001e9)                        # Wright at Vk = 5 treats census 8.2e9 as Ne 4.7e9
near(ne_census / 8.2e9, 0.5714, 0.0001)

finish({
    "object": "M-205",
    "inputs": [
        {"name": "ceiling", "value": "X = (Vk + 2) G/16", "cite": "Q29 (B2 q1)"},
        {"name": "Wright Ne", "value": "(4N - 2)/(Vk + 2)", "cite": "Q32 (B2b q1)"},
        {"name": "stated ceilings", "value": {"large vertebrate": 10_000, "human species": 35_000, "human lineage": 100_000, "elephant": 28_000}, "cite": "B2b q2, Q33 (B2b q3)"},
        {"name": "species T, g, Vk, printed X", "value": {k: list(v[:4]) for k, v in ROWS.items()}, "cite": "claim file B2b audit table (HL Table 1); mouse and fly inputs flagged 'pending a proper source'"},
        {"name": "human census", "value": 8.2e9, "cite": "claim file B2 (HL Table 1)"},
    ],
    "values": {
        "X": {k: g(v) for k, v in X.items()},
        "table2_halved_doubled": {k: [g(a), g(b)] for k, (a, b) in t2.items()},
        "ten_thousand_vs_table": {"human_species": 3.5, "human_lineage": 11.375, "elephant": g(X["elephant"] / ten_k)},
        "human_census_over_X": g(over),
        "Ne_at_census_vk5": g(ne_census),
    },
    "positions": {
        "day": {"algebra_exact": True, "ceilings_reproduce": True, "human_census_over_ceiling": g(over),
                "domain_claim": "census exceeds X for every listed species"},
        "critic": {"algebra_exact": True,
                   "disputed_inputs": "Vk, G (lineage 6.5 My vs species 2 My) and equating N with census; keruru reports measured temporal Ne three orders below Wright's value (M-206)",
                   "abstract_10k_below_table": [3.5, 11.375, g(X["elephant"] / ten_k)],
                   "number": None,
                   "why_none": "keruru's measured Ne and census inputs are not quoted in held text; that test is M-206 (data-check)"},
    },
    "notes": "The ceiling is exact algebra and every Table 1 and Table 2 value reproduces within 1.5% (rounding). The abstract's "
             "'about ten thousand' is 2.8x to 11x below the paper's own large-vertebrate ceilings. Whether census "
             "N, Vk and G are the right inputs is not settled here (M-206, M-202).",
})
