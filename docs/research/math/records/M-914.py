#!/usr/bin/env python3
"""M-914 record (derivation): the arithmetic of McCarthy's MC-1 post and MC-1c replies that the library did not hold.

Object: docs/research/math/objects.yaml M-914 (identity, derivation, variant_of M-212). Sources: MC-1 (McCarthy, Substack
free repost, 2026-09-11), MC-1c (his replies, 2026-09-12 to 2026-09-18, incl. RF-6 in the MC-2 thread); source map
docs/research/math/sources/mccarthy-mc1.md. Already settled elsewhere and only cited here: 450e9/20,000 = 22.5M (M-212),
the Darwillion exponent 86,020,600 (M-703), P_any at 527 sigma (M-704), 450,000/1,600 = 281.25 (M-001), 3.1e9/4.6e6 = 674
and 1/4.1e-4 = 2,439 (M-007), 4Ne (M-203).
Inputs are the speakers' own: Day's as McCarthy quotes them (100 mutations per individual per generation, N = 10,000,
1/(2N), 50,000 per year, 20 M fixations, 9 My; mc1@L35-L36), McCarthy's lag (4Ne = 40,000 generations, 25 y per
generation, mc1c#337116873), RF-6 (400 billion x 1/20000, mc2c#340149310), F_max = 180 (MITTENS 3.0 as Day quotes it at
mc2c#340102853), Wielgoss 0.00041 per genome per generation (mc1@L75), Day's "3x more harmful" (mc1c#337302874).
The record asserts every number the D-41 review page states that is not in an earlier record, and the R1 tests:
- the Day text McCarthy quotes: 1e6 per generation, 50,000/y (g = 20 y), 2.22/y, 1 in 22,727 ("23,000"), 0.0044%
  ("0.004%"); supply x p_fix = 2.5/y, 12.5% above the 2.22/y needed; two lineages 10^-172,041,200 ("10^-172,000,000");
- RF-7 lag: 9e6/25 = 360,000, minus 40,000 = 320,000 generations = 8e6 y, x 50,000 = 4e11, / 20,000 = 2e7 as written;
  the 50,000/y rests on 20 y generations, the lag on 25 y: single basis 16.0M (25 y, -20%) or 20.5M (20 y, +2.5%);
  neither moves "the exact correct result" by more than 25% (R1: ledger);
- RF-6: 4e11/20,000 = 2e7, printed 35 million (+75%; the correction is -42.9% on the printed figure); against
  F_max = 180 the ratio is 111,111, not 194,444, and the inequality does not flip;
- MC-1 match 22.5M/20M = +12.5%; under Day's "3x more harmful" (neutral share 1/4): 5.625M and 5.0M lag-adjusted;
- E. coli: 1 - 4.1e-4 = 99.959% ("over 99.9%"); per-genome ratio human/E. coli at 60-100 de novo = 146,341-243,902;
- Day's thread: 4 x 10,000 x 25 = 1e6 y; 410e6/6e6 = 68.3.

Run: research/.venv/bin/python -I docs/research/math/records/M-914.py [--write]
Without --write it checks that M-914.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
MAP = "docs/research/math/sources/mccarthy-mc1.md"
RAW = ["sources/raw/mccarthy-mc1-2026-11-26/" + f for f in ("text.txt", "comments.txt", "comments-vdr.txt")]
M212, M703 = "docs/research/math/records/M-212.json", "docs/research/math/records/M-703.json"


def norm(s):
    return " ".join(s.split())


def held(text, quote, where):
    assert norm(quote) in norm(text), (where, quote[:60])
    return quote


def mc(quote):
    """A quote from MC-1 / MC-1c: in the committed source map, and in the held fetch when this checkout has it."""
    held((ROOT / MAP).read_text(encoding="utf-8"), quote, MAP)
    if all((ROOT / r).exists() for r in RAW):
        held("\n".join((ROOT / r).read_text(encoding="utf-8") for r in RAW), quote, "raw")
    return quote


def near(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


# ---- the source sentences ---------------------------------------------------------------------------
mc("that’s roughly 1 million new mutations entering the population per generation, or about 50,000 per year.")
mc("If 50,000 mutations arise per year and 2.2 need to succeed, the required success rate would be one in 23,000, or 0.004%.")
mc("10−86,000,000 ⋅ 10−86,000,000 = 10−172,000,000")
mc("And that is a pretty close approximation to the 20 million fixed mutations that have been observed.")
mc("E. Coli produces an exact, mutation-free clone over 99.9% of the time, with one mutation occurring every 1000-2400 divisions.")
mc("360,000-40,000=320,000 generations")
mc("50,000 x 8,000,000=400 billion mutations")
mc("400 billion x 1/20,000 =20 million fixations. So when we apply the time available to the numbers we land on the exact correct result.")
mc("And the numbers work 400 billion x 1/20000 = 35 million point mutations fixing alone. That's 35 million right there, not 180.")
mc("t̄ = 4 × 10,000 = 40,000 generations. At 25 years per generation, that's 1,000,000 years per neutral fixation.")
mc("What is 410 million divided by 6 million?")
mc("There are 3x more harmful mutations than neutral ones.")
assert json.loads((ROOT / M212).read_text(encoding="utf-8"))["values"]["counts"]["mccarthy"] == 22.5e6
m703 = json.loads((ROOT / M703).read_text(encoding="utf-8"))["values"]["log10_P"]["Darwillion_(1/20000)^2e7"]
assert round(m703) == -86_020_600, "M-703 exponent"

# ---- Day's text as McCarthy quotes it (mc1@L35-L36, L39-L42) ----------------------------------------------
U, N, R, T_Y = 100, 10_000, 20e6, 9e6
per_gen = U * N
assert per_gen == 1e6
g_supply = per_gen / 50_000
assert g_supply == 20                                                   # 50,000/y implies 20 y generations
need_per_y = R / T_Y
near(need_per_y, 2.222, 1e-3)
assert round(50_000 / 2.2) == 22_727                                    # "one in 23,000"
near(100 * 2.2 / 50_000, 0.0044, 1e-9)                                  # "0.004%"
p_fix = 1 / (2 * N)
assert p_fix == 1 / 20_000
got_per_y = 50_000 * p_fix
assert got_per_y == 2.5
near(got_per_y / need_per_y - 1, 0.125, 1e-9)                           # supply x p_fix 12.5% above the need
exp1 = R * math.log10(20_000)
assert round(exp1) == 86_020_600                                        # M-703
assert round(2 * exp1) == 172_041_200                                   # "10^-172,000,000": rounding

# ---- MC-1 match and Day's neutral-share objection ----------------------------------------------------------
mc1 = 50_000 * T_Y * p_fix
assert mc1 == 22.5e6
near(mc1 / R - 1, 0.125, 1e-12)                                         # "a pretty close approximation"
neutral_share = 1 / (1 + 3)                                             # "3x more harmful ... than neutral"
assert mc1 * neutral_share == 5.625e6 and R * neutral_share == 5.0e6

# ---- RF-7 lag (mc1c#337116873) and its basis --------------------------------------------------------------
G_LAG, LAG = 25, 4 * N
assert LAG == 40_000 and LAG * G_LAG == 1e6                             # Day's "1,000,000 years" holds too
gens = T_Y / G_LAG
assert gens == 360_000 and gens - LAG == 320_000
years_left = (gens - LAG) * G_LAG
assert years_left == 8e6
as_written = 50_000 * years_left * p_fix
assert 50_000 * years_left == 4e11 and as_written == 20e6
basis_25 = (gens - LAG) * per_gen * p_fix                               # 25 y throughout: 40,000/y
basis_20 = (T_Y / 20 - LAG) * per_gen * p_fix                           # 20 y throughout: 410,000 generations
assert basis_25 == 16e6 and basis_20 == 20.5e6
moves = {"25y": basis_25 / as_written - 1, "20y": basis_20 / as_written - 1}
near(moves["25y"], -0.20, 1e-12); near(moves["20y"], 0.025, 1e-12)
assert all(abs(m) <= 0.25 for m in moves.values())                      # R1: no move > 25% -> ledger

# ---- RF-6 (mc2c#340149310) ---------------------------------------------------------------------------------
F_MAX = 180
true_rf6, printed = 4e11 * p_fix, 35e6
assert true_rf6 == 20e6
near(printed / true_rf6 - 1, 0.75, 1e-12)                               # printed is 75% high
near(true_rf6 / printed - 1, -0.428571, 1e-6)                           # correction moves the figure -42.9%
assert round(printed / F_MAX) == 194_444 and round(true_rf6 / F_MAX) == 111_111
assert true_rf6 > F_MAX and printed > F_MAX                             # "not 180": no flip
near(round(252_000 / 1_400), F_MAX, 0)                                  # F_max = 180 (MITTENS 3.0 as Day quotes it)

# ---- E. coli and per-genome ratios (mc1@L61, L75) ----------------------------------------------------------
U_E = 0.00041
near(8.9e-11 * 4.6e6, U_E, 1e-6)                                        # Wielgoss: 8.9e-11 x 4.6e6 = 4.09e-4
near(100 * (1 - U_E), 99.959, 1e-9)                                     # "over 99.9%"
assert round(1 / U_E) == 2_439                                          # "2400" (M-007); 1,000 unsourced
ratios = (round(60 / U_E), round(100 / U_E))
assert ratios == (146_341, 243_902)                                     # "orders of magnitude"

# ---- Day's thread arithmetic -------------------------------------------------------------------------------
near(410e6 / 6e6, 68.33, 0.01)


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
    "object": "M-914",
    "variant_of": "M-212",
    "inputs": [
        {"name": "U_per_individual", "value": U, "cite": "mc1@L35 (Day, as McCarthy quotes PZ)"},
        {"name": "N", "value": N, "cite": "mc1@L35-L36; p_fix = 1/(2N)"},
        {"name": "required_per_lineage", "value": R, "cite": "mc1@L33, mc1@L35"},
        {"name": "t_years", "value": T_Y, "cite": "mc1@L35"},
        {"name": "supply_per_year", "value": 50_000, "cite": "mc1@L35 (implies g = 20 y)"},
        {"name": "g_lag_years", "value": G_LAG, "cite": "mc1c#337074301 (Day), mc1c#337116873 (McCarthy)"},
        {"name": "F_max", "value": F_MAX, "cite": "mc2c#340102853 (Day quotes MITTENS 3.0: 252,000 / 1,400)"},
        {"name": "U_Ecoli", "value": U_E, "cite": "mc1@L75 (Wielgoss et al. 2011, quoted)"},
        {"name": "harmful_to_neutral", "value": 3, "cite": "mc1c#337302874 (Day)"},
    ],
    "values": {
        "day_text": {"per_generation": per_gen, "g_implied_y": g_supply, "need_per_y": round(need_per_y, 4),
                     "one_in": 22_727, "pct": 0.0044, "supply_x_pfix_per_y": got_per_y,
                     "excess_over_need": 0.125, "log10_two_lineages": -172_041_200},
        "mc1_match": {"expected": mc1, "vs_required": 0.125, "neutral_share_quarter": 5.625e6,
                      "lag_adjusted_neutral_share_quarter": 5.0e6},
        "rf7_lag": {"generations": gens, "productive_generations": gens - LAG, "years": years_left,
                    "as_written": as_written, "single_basis_25y": basis_25, "single_basis_20y": basis_20,
                    "moves": {k: round(v, 4) for k, v in moves.items()}, "r1": "ledger (max |move| 20% <= 25%)"},
        "rf6": {"true": true_rf6, "printed": printed, "printed_over_true": 0.75, "correction": -0.4286,
                "ratio_to_180_printed": 194_444, "ratio_to_180_true": 111_111, "flips": False},
        "ecoli": {"clone_fraction_pct": 99.959, "divisions_per_mutation": 2_439, "human_over_ecoli": list(ratios)},
        "day_thread": {"lag_years": 1e6, "410M_over_6M": 68.33},
    },
    "positions": {
        "day": {"reading": "the count ignores the fixation time and treats every mutation as neutral; with Day's "
                           "3x harmful ratio the neutral expectation is a quarter",
                "holds": "the time point is answered by McCarthy's own lag (16-20.5M); the neutral-share point "
                         "moves 22.5M to 5.6M only if three quarters of new mutations are harmful, an input"},
        "critic": {"reading": "on Day's quoted inputs the expected neutral count meets the requirement",
                   "holds": "22.5M (+12.5%), 16-20.5M lag-adjusted; Day's own quoted 1 in 22,727 need sits below "
                            "his 1 in 20,000 p_fix; RF-6's 35M is a slip for 20M and leaves '>> 180' standing"},
    },
    "notes": "RF-6 is in the MC-2 thread (mc2c#340149310). R1 on RF-6 is reading-dependent: as a comparison with 180 "
             "(the stated conclusion, 'not 180') it is ledger; read as a headline total it moves 42.9% (R1(i)); "
             "see the review page. The RF-7 mixed generation basis (20 y supply, 25 y lag) is new to the library.",
})
