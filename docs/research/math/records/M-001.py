#!/usr/bin/env python3
"""M-001 record: F_max = (t_div x d) / (g_len x G_f) and shortfall = R / F_max, by version.

Object: docs/research/math/objects.yaml M-001 (formula, derivation). Versions: 2019 blog, 2025
(Z18165980), MITTENS 3.0 (Z23003785), Hoessjer's recalculation. Every input is stated with its
quote id (docs/research/sources/quotes-day.md) or claim file; held() checks each quote verbatim
against that file. Every number the statement claims has an assert, including the printed 2019
figures (125, 562) that do not reconcile.

Run: research/.venv/bin/python -I docs/research/math/records/M-001.py [--write]
Without --write it checks that M-001.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"


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


def f_max(t_div, d, g_len, g_f):
    return t_div * d / (g_len * g_f)


# ---- inputs -------------------------------------------------------------------------------
Q06 = held(QD, "F_max = (t_div × d) / (g_len × G_f)")
Q03 = held(QD, "CHLCA Years: 9,000,000 Years per generation: 20 Generations per fixed mutation: 1600")
Q03b = held(QD, "Years per fixed mutation: 32000 Maximum fixed mutations: 125")
Q04 = held(QD, "there have been 450,000 chimp and human generations since the CHLCA. Based on the number of "
               "mutations observed fixing in parallel in the Nature study, that would permit 562 total fixed "
               "mutations in that time frame. Which is only 29,999,438 short of the approximate number observed.")
Q05 = held(QD, "it requires a minimum of 15,000,000 mutations to become fixed in the human population, and "
               "another 15,000,000 mutations to become fixed in the chimpanzee population")
Q09 = held(QD, "Effective generations = 325,000 × 0.45 = 146,250 Fixation time: ~1,600 generations per fixation "
               "under strong selection (E. coli LTEE^3). Achievable fixations: 146,250 / 1,600 = 91 fixations "
               "Shortfall: 20,000,000 / 91 = 219,780-fold")
Q18 = held(QD, "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations.")
Q58 = held(QD, "The average across all five non-mutator populations at 60,000 generations is 45.4 fixations, "
               "yielding a cumulative rate of 1,322 generations per fixation.")
Q14 = held(QD, "Applied to human-chimpanzee divergence (205 million required fixations on the human lineage across "
               "252,000 available generations), the shortfall is 1,075,000-fold for non-mutators")
HO01 = held(CL + "A5a-hossjer-127-15800-10m.md", "This is a lot larger than the previous upper bound 127")
HO_F = held(CL + "A5a-hossjer-127-15800-10m.md", "F_127 = 9e6 · 0.45 / (20 · 1,600) = 126.6")

# ---- 2019 (B2019-02-07): 9.0 My, 20 y, G_f 1,600, R = 30e6 (15e6 per lineage) -------------
n19 = 9_000_000 / 20
assert n19 == 450_000                                   # Q04 "450,000 ... generations"
f19 = f_max(9_000_000, 1, 20, 1600)
assert f19 == 281.25 == 9_000_000 / 32_000              # Q03 "Years per fixed mutation: 32000"
assert 20 * 1600 == 32_000
table_125, text_562 = 125, 562
assert table_125 * 32_000 == 4.0e6                      # the table's 125 needs t_div = 4.0 My
assert math.floor(2 * f19) == text_562                  # 562 = 2 x 281.25, a doubling the post does not state
assert 30_000_000 - text_562 == 29_999_438              # Q04 "29,999,438 short", against total R = 2 x 15e6 (Q05)
gap_125 = near(table_125 / f19, 0.444, 0.001)           # printed table figure is 44% of its own inputs
gap_562 = near(text_562 / f19, 1.998, 0.001)            # printed text figure is 2.0x
short19_total = 30_000_000 / (2 * f19)                  # total R over two-lineage F (the text's convention)
short19_lineage = 15_000_000 / f19                      # per-lineage R over one-lineage F
assert short19_total == short19_lineage
near(short19_lineage, 53_333, 1)

# ---- 2025 (Z18165980): 325,000 nominal x d 0.45, G_f 1,600, R = 20e6 ---------------------
n25 = 325_000 * 0.45
assert n25 == 146_250
f25 = n25 / 1600
near(f25, 91.4, 0.01)                                   # paper prints 91
assert round(20_000_000 / 91) == 219_780                # paper's shortfall reproduces from its rounded 91
short25 = 20_000_000 / f25
near(short25, 218_803, 1)                               # unrounded F: 0.45% below the printed 219,780

# ---- MITTENS 3.0 (Z23003785): 6.3 My / 25 y, G_f 1,322, no d term, R = 205e6 --------------
n30 = 6_300_000 / 25
assert n30 == 252_000
gf30 = 60_000 / 45.4
assert round(gf30) == 1322                              # Q58
f30 = n30 / 1322
near(f30, 190.6, 0.05)
short30 = 205e6 / f30
near(short30, 1.0754e6, 0.0001e6)                       # paper 1,075,000-fold (Q14)
assert abs(short30 - 1_075_000) / 1_075_000 < 0.001
# with Day's d = 0.45 restored (the 2025 term)
f30d = f_max(6_300_000, 0.45, 25, 1322)
near(f30d, 85.8, 0.05)
short30d = 205e6 / f30d
near(short30d, 2.39e6, 0.005e6)
near(short30d / short30, 1 / 0.45, 1e-9)                # dropping d makes the shortfall 2.22x smaller

# ---- Hoessjer (HO-01): 9e6 x 0.45 / (20 x 1,600) -----------------------------------------
fh = f_max(9e6, 0.45, 20, 1600)
near(fh, 126.6, 0.05)
assert round(fh) == 127                                 # HO-01 "previous upper bound 127"

# ---- positions, side by side -------------------------------------------------------------
day = {
    "versions_after_2019_reconcile": True,
    "2025_F_max": g(f25), "2025_shortfall_printed_inputs": 219_780,
    "3.0_F_max": g(f30), "3.0_shortfall": g(short30),
    "3.0_shortfall_with_d_0.45": g(short30d),
    "dropping_d_is_conservative": short30d > short30,
}
critic = {
    "2019_F_max_from_table_inputs": f19,
    "2019_table_printed": table_125, "2019_text_printed": text_562,
    "2019_table_reconciles": round(f19) == table_125, "2019_text_reconciles": round(f19) == text_562,
    "note": "the formula is arithmetic on inputs whose transfer is the dispute (M-103, M-713); not computed here",
}
assert day["dropping_d_is_conservative"] and not critic["2019_table_reconciles"] and not critic["2019_text_reconciles"]

finish({
    "object": "M-001",
    "inputs": [
        {"name": "formula", "value": "F_max = (t_div x d)/(g_len x G_f)", "cite": "Q06"},
        {"name": "2019 t_div, g_len, G_f, table F", "value": [9.0e6, 20, 1600, 125], "cite": "Q03; parameters divergence.t_div_years.day_2019, generation_time_years.day_2019, ltee.gens_per_fixation.day_2019"},
        {"name": "2019 text generations, F, shortfall", "value": [450_000, 562, 29_999_438], "cite": "Q04"},
        {"name": "2019 R", "value": "15e6 per lineage, 30e6 total", "cite": "Q05; parameters divergence.required_fixations.day_2019"},
        {"name": "2025 nominal gens, d, G_f, F, R, shortfall", "value": [325_000, 0.45, 1600, 91, 20e6, 219_780], "cite": "Q09"},
        {"name": "3.0 t_div, g_len, N_gen", "value": [6.3e6, 25, 252_000], "cite": "Q18"},
        {"name": "3.0 G_f", "value": "60,000/45.4 = 1,322", "cite": "Q58; parameters ltee.gens_per_fixation.day_mittens3_nonmutator"},
        {"name": "3.0 R and shortfall", "value": [205e6, 1_075_000], "cite": "Q14; parameters shortfall.mittens3_full"},
        {"name": "Hoessjer F", "value": "9e6 x 0.45/(20 x 1,600) = 126.6, 'upper bound 127'", "cite": "A5a q1 (HO-01); claim file A5a formal statement"},
    ],
    "values": {
        "2019": {"N_gen": n19, "F_max": f19, "table_printed": table_125, "table_over_F": g(gap_125),
                 "t_div_needed_for_125": 4.0e6, "text_printed": text_562, "text_over_F": g(gap_562),
                 "shortfall_per_lineage": g(short19_lineage)},
        "2025": {"N_eff": n25, "F_max": g(f25), "printed_F": 91, "shortfall_printed": 219_780, "shortfall_unrounded": g(short25)},
        "3.0": {"N_gen": n30, "G_f": g(gf30), "F_max": g(f30), "shortfall": g(short30), "printed": 1_075_000,
                "F_max_with_d": g(f30d), "shortfall_with_d": g(short30d), "ratio_with_d": g(short30d / short30)},
        "hoessjer": {"F_max": g(fh), "printed": 127},
    },
    "positions": {"day": day, "critic": critic},
    "notes": "2019 table (125) and text (562) do not reconcile with 450,000/1,600 = 281.25; the text's 562 and "
             "29,999,438 use two-lineage F against total R, which gives the same shortfall as per-lineage R over "
             "one-lineage F (53,333). 2025 and 3.0 reconcile. Which inputs transfer is not settled here (M-103, M-713).",
})
