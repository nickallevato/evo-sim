#!/usr/bin/env python3
"""M-808 record (derivation): Term 3 selection-limited rate, K_sel = s_max d / [2 ln(2Ne)] (Z19984826).

Object: docs/research/math/objects.yaml M-808 (formula, derivation). n_max = s_max / s-bar concurrent sweeps, each
lasting tau = (2/(s-bar d)) ln(2Ne), so K_sel = n_max / tau = s_max d / [2 ln(2Ne)] (s-bar cancels) and per site
k_sel = K_sel / L. Human case (s4.3, H8 q2): s_max = 1, d = 0.45, L = 3.1e9, Ne = 3,300: ln 6,600 = 8.795 (printed
8.79), k_sel = 8.25e-12 per site (printed 8.3e-12), K_sel = 0.02558 per generation (one per 39.1). Over 260,000
generations the closed form gives 6,652, the "about 6,650" of claim files H1 and H8; the "about 6,690" of H5 is the
printed 8.3e-12 x 3.1e9 x 260,000 = 6,690 (rounded rate). Ne = 1e4: 7.33e-12 (one per 44). Against Haldane + d
(1/667 per nominal generation, M-802) Term 3 is 17.06 times faster, on either basis (d on both sides or neither).
The 3,300 is unlocated in the corpus; Ne enters only through ln(2Ne). Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-808.py [--write]
Without --write it checks that M-808.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H1 = CL + "H1-term3-retraction.md"
H5 = CL + "H5-hossjer-cost-step.md"
H8 = CL + "H8-kimura-calculator-term3.md"
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
H8Q1 = held(H8, "Selection cannot operate without reproductive differential, and the differential available to any "
                "individual is bounded by what the organism can physically achieve.")                    # H8 q1 (s3.3)
H8Q2 = held(H8, "ksel = smax · d / [2L · ln(2Nₑ)] = 1 · 0.45 / [2 · 3.1 × 10⁹ · ln(6,600)] = 0.45 / [2 · 3.1 × 10⁹ · "
                "8.79] ≈ 8.3 × 10⁻¹²")                                                                    # H8 q2 (s4.3)
H8Q3 = held(H8, "None of them raises smax above order unity, and the reason is the same in all three cases.")  # H8 q3
FORM = held(H8, "n_max = s_max / s̄ concurrent sweeps (sum of s_i <= s_max); each sweep takes tau = (2/(s̄ d)) "
                "ln(2Ne) generations")
NE_SRC = held(H8, "Z18320599 contains no absolute Ne of 3,300 (searched: 0 occurrences)")
H8_6650 = held(H8, "Over 260,000 generations: 6,650 adaptive substitutions. Required 17.5M / 6,650 = 2,630 (paper: "
                   "2,700x at 6.5 MYA; holds within rounding).")
H1_6650 = held(H1, "For 260,000 generations this gives about 6,650 adaptive substitutions")
H5_6690 = held(H5, "about 6,690 from Term 3, H1")                   # H5 derived line (l.39)
Q67 = ("my error was in interpreting its output as a constraint on total k. Once corrected, Term 3 still limits "
       "adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2")
held(H1, Q67); held(QD, Q67)                                         # H1 q2 = Q67
H1Q3 = held(H1, "the realized substitution rate equals the minimum of three serial constraints")         # H1 q3 = Q66
held(PY, "Ne_modern_human: {value: 1.0e4")                          # population.Ne_modern_human
held(PY, "turnover_d: {value: 0.45")                                # selection.turnover_d
S_MAX, D, L, NE, GENS, NE_ALT, REQ = 1, 0.45, 3.1e9, 3_300, 260_000, 1e4, 17.5e6
assert "1 · 0.45" in H8Q2 and "3.1 × 10⁹" in H8Q2 and "ln(6,600)" in H8Q2

# ---- the formula: s-bar cancels ---------------------------------------------------------------------
def K_sel(s_max, d, ne, s_bar):
    n_max = s_max / s_bar
    tau = (2 / (s_bar * d)) * math.log(2 * ne)
    return n_max / tau

for sb in (0.001, 0.01, 0.1):
    near(K_sel(S_MAX, D, NE, sb), S_MAX * D / (2 * math.log(2 * NE)), 1e-15)   # independent of s-bar

# ---- human case ---------------------------------------------------------------------------------------
ln2ne = math.log(2 * NE)
near(ln2ne, 8.795, 5e-4)
near(ln2ne, 8.79, 0.006)                                            # printed 8.79 (truncated from 8.7948)
K = S_MAX * D / (2 * ln2ne)
k = K / L
near(k / 1e-12, 8.25, 0.005); assert round(k / 1e-12, 1) == 8.3    # 8.25e-12 per site (paper 8.3e-12)
near(K, 0.02558, 5e-6)                                              # 0.0256 per generation
near(1 / K, 39.09, 0.005); assert round(1 / K) == 39                # one per 39
total = K * GENS
near(total, 6_651.6, 0.05)                                          # closed form over 260,000 generations
assert round(total, -1) == 6_650                                    # matches H1 / H8 "about 6,650"
total_printed_rate = 8.3e-12 * L * GENS
near(total_printed_rate, 6_689.8, 0.05); assert round(total_printed_rate, -1) == 6_690   # H5's 6,690: rounded rate
near(total_printed_rate / total - 1, 0.0057, 1e-4)                  # the two printed totals differ by 0.6%
near(REQ / total, 2_630.9, 0.1)                                     # H8's 2,630
near(2_700 / (REQ / total) - 1, 0.026, 5e-4)                        # paper's 2,700x is 2.6% above
near(REQ / (L * GENS), 2.17e-8, 5e-11)                              # required k at 6.5 MYA (H8 Term 2 line)

# ---- Ne = 1e4 and the role of Ne -------------------------------------------------------------------------
k_alt = S_MAX * D / (2 * L * math.log(2 * NE_ALT))
near(k_alt / 1e-12, 7.33, 0.005); assert round(k_alt / 1e-12, 1) == 7.3
near(1 / (k_alt * L), 44.0, 0.05)                                   # one per 44
near(k / k_alt, math.log(2 * NE_ALT) / ln2ne, 1e-12)               # Ne enters only through ln(2Ne)
near(k / k_alt, 1.126, 5e-4)                                        # a 3x change in Ne moves k by 12.6%

# ---- against Haldane + d ----------------------------------------------------------------------------------
hal_d = D / 300                                                     # 1/667 per nominal generation (M-802)
near(1 / hal_d, 666.67, 0.01)
near(K / hal_d, 17.06, 0.005); assert round(K / hal_d, 1) == 17.1   # 17.1 with d on both sides
near((S_MAX / (2 * ln2ne)) / (1 / 300), 17.06, 0.005)               # and without d on both sides
near(300 / (1 / K), 7.675, 0.001)                                   # the withdrawn 7.7 mixed bases
near((K / hal_d) / (300 * K), 1 / D, 1e-9)                          # 17.1 / 7.7 = 1/d
near(1 / (0.1 * D / (2 * ln2ne)), 390.9, 0.05)                      # s_max = 0.1: one per 391, near Haldane's 300

finish({
    "object": "M-808",
    "inputs": [
        {"name": "s_max, d, L, Ne", "value": [S_MAX, D, L, NE], "cite": "H8 q2 (Z19984826 s4.3); parameters selection.turnover_d; Ne = 3,300 unlocated (H8 formal statement)"},
        {"name": "generations", "value": GENS, "cite": "claim files H1, H8 (6.5 MYA at 25 years)"},
        {"name": "alternative Ne", "value": NE_ALT, "cite": "parameters population.Ne_modern_human"},
        {"name": "required substitutions", "value": REQ, "cite": "claim file H8 derived (17.5M)"},
    ],
    "values": {
        "ln_2Ne": round(ln2ne, 4), "k_sel_per_site": f"{k:.3e}", "K_sel_per_generation": round(K, 5),
        "generations_per_substitution": round(1 / K, 2), "total_260k_closed_form": round(total, 1),
        "total_260k_from_printed_8.3e-12": round(total_printed_rate, 1), "required/total": round(REQ / total, 1),
        "k_sel_Ne_1e4": f"{k_alt:.3e}", "generations_per_substitution_Ne_1e4": round(1 / (k_alt * L), 1),
        "term3_over_haldane_d": round(K / hal_d, 2), "withdrawn_300/39": round(300 * K, 2),
        "s_max_0.1_generations_per_substitution": round(1 / (0.1 * D / (2 * ln2ne)), 1),
    },
    "positions": {
        "day": {"reading": "s_max of order unity bounds the adaptive rate at about 1e-12 per site (retracted 2026-05-07 as a "
                           "bound on total k, kept for adaptive substitution, Q67)",
                "holds": "8.25e-12 (8.3e-12), 0.0256 per generation and one per 39 reproduce; s-bar cancels"},
        "critic": {"reading": "the formula bounds adaptive substitutions only; Ne = 3,300 has no source; 300 and 39 generations "
                              "per substitution are not reconciled",
                   "holds": "Term 3 allows 17.1x Haldane + d on a same basis; Ne enters only via ln(2Ne), so the source "
                            "gap moves k by 12.6% between 3,300 and 1e4"},
    },
    "notes": "All printed Term 3 figures reproduce: ln 6,600 = 8.795 (printed 8.79), 8.25e-12 (8.3e-12), 0.02558 per "
             "generation (one per 39.1), 7.33e-12 at Ne = 1e4 (one per 44), 17.06x Haldane + d (the withdrawn 7.7 = "
             "300/39.1 differs by 1/d). Map-fix item: the closed-form total over 260,000 generations is 6,651.6, which "
             "matches 'about 6,650' in H1 and H8; H5's 'about 6,690' is the printed 8.3e-12 x 3.1e9 x 260,000 = "
             "6,689.8 (0.6% higher, from the rounded rate). 17.5M/6,652 = 2,631 against the paper's 2,700x (2.6%). "
             "The 3,300 is unlocated (Z18320599 has no absolute Ne of 3,300). Which mechanism raises s_max (H8 q3, R4 "
             "HF) is outside this record.",
})
