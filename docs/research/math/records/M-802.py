#!/usr/bin/env python3
"""M-802 record (derivation): Day's Haldane + d extension, 146,250 effective generations and 487 fixations.

Object: docs/research/math/objects.yaml M-802 (formula, derivation). Z18168236 s4.2: G_eff = G x d = 325,000 x 0.45 =
146,250 (parameters generations_available.day_2025_effective); achievable fixations 146,250/300 = 487.5, printed 487
(truncated, Q48 = H q2); shortfall 20,000,000/487 = 41,067.8, printed 41,068 (rounded; with the untruncated 487.5 it
is 41,025.6). Without d: 325,000/300 = 1,083. The d step ("selection operates at only 45% of the rate Haldane
assumed", H q4) applies a time rescaling (d, M-107) to a per-generation death budget, an additional step the record
names but does not settle. The 88 Million x post uses the same 146,250 (H3 q3). Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-802.py [--write]
Without --write it checks that M-802.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H = CL + "H-haldane-limit.md"
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
Q48 = "Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations"
held(H, Q48); held(QD, Q48)                                          # H q2 = Q48 (Z18168236 s4.2)
HQ4 = held(H, "If that cohort represents only 45% of the population-generation product, then selection operates at "
              "only 45% of the rate Haldane assumed.")                                                   # H q4 (s4.2)
H3Q3 = held(H3, "Based on my necessary Bio-Cycle correction to the bacteria-based Kimura fixation model, that leaves "
                "146,250 generations to fixate all of those base pairs.")                                # H3 q3 (88 Million x)
EXT = held(H, "Day's extension: effective generations G_eff = G x d = 325,000 x 0.45 = 146,250 "
              "(`generations_available.day_2025_effective`), achievable = G_eff/300.")
R2 = held(H, "146,250/300 = 487.5 (the paper truncates to 487; holds); 20,000,000/487 = 41,068 (the paper's 41,068x; holds)")
NOD = held(H, "Same arithmetic without d: 325,000/300 = 1,083")
STEP = held(H, "Applying d to a death-budget argument is an additional step (the budget is per generation of deaths; d "
               "rescales time).")
held(PY, "day_2025_effective: {value: 146250, derived: \"325000*0.45\"")   # generations_available.day_2025_effective
held(PY, "day_2025: {value: 2.0e7, source: Z18165980")                    # divergence.required_fixations.day_2025
held(PY, "turnover_d: {value: 0.45")                                      # selection.turnover_d
G, D, INTERVAL, REQ = 325_000, 0.45, 300, 20_000_000

# ---- the chain --------------------------------------------------------------------------------------
g_eff = G * D
near(g_eff, 146_250, 1e-6)                                          # 325,000 x 0.45
fix_exact = g_eff / INTERVAL
near(fix_exact, 487.5, 1e-9)                                        # 146,250 / 300 = 487.5
fix_printed = math.floor(fix_exact)
assert fix_printed == 487                                           # the paper truncates (floor), not rounds (488)
assert round(fix_exact + 1e-9) == 488 and fix_printed != round(fix_exact + 1e-9)
short_printed = REQ / fix_printed
near(short_printed, 41_067.76, 0.01); assert round(short_printed) == 41_068    # printed 41,068 (rounded)
short_exact = REQ / fix_exact
near(short_exact, 41_025.64, 0.01)                                  # with the untruncated 487.5
near(short_printed / short_exact - 1, 0.00103, 1e-5)                # truncation moves the shortfall by 0.1%
fix_nod = G / INTERVAL
near(fix_nod, 1_083.33, 0.01); assert math.floor(fix_nod) == 1_083  # without d
near(fix_nod / fix_exact, 1 / D, 1e-12)                             # d is a pure 1/0.45 = 2.22 factor on the count
near(REQ / math.floor(fix_nod), 18_467.2, 0.1)                      # shortfall without d
near(INTERVAL / D, 666.67, 0.01)                                    # d as a rate: 1 per 667 nominal generations

finish({
    "object": "M-802",
    "inputs": [
        {"name": "G, d", "value": [G, D], "cite": "claim file H formal statement; parameters generations_available.day_2025_effective, selection.turnover_d"},
        {"name": "Haldane interval", "value": INTERVAL, "cite": "M-801; parameters haldane.gens_per_substitution"},
        {"name": "required fixations", "value": REQ, "cite": "parameters divergence.required_fixations.day_2025"},
        {"name": "printed 146,250, 487, 41,068", "value": [146_250, 487, 41_068], "cite": "Q48 = H q2; H3 q3; claim file H derived"},
    ],
    "values": {
        "G_eff": g_eff, "fixations_exact": fix_exact, "fixations_printed_floor": fix_printed,
        "shortfall_20M/487": round(short_printed, 2), "shortfall_20M/487.5": round(short_exact, 2),
        "fixations_without_d": round(fix_nod, 2), "shortfall_without_d_20M/1083": round(REQ / math.floor(fix_nod), 1),
        "nominal_generations_per_fixation_with_d": round(INTERVAL / D, 2),
    },
    "positions": {
        "day": {"reading": "d = 0.45 rescales the generations available: 146,250, 487 fixations against 20 million",
                "holds": "146,250, 487 (487.5 truncated) and 41,068 (41,067.8 rounded) reproduce"},
        "critic": {"reading": "d rescales time for overlapping generations, not a death budget; the extension is an extra step",
                   "holds": "the arithmetic is not at issue; d enters only as a 1/0.45 factor on the count (1,083 -> 487), "
                            "so whether it belongs in a per-generation death budget (H q4) is the open modelling step"},
    },
    "notes": "All printed figures reproduce: 146,250 = 325,000 x 0.45; 146,250/300 = 487.5, floored to 487 (rounding "
             "would give 488); 20M/487 = 41,067.8, printed 41,068 (41,025.6 with 487.5, a 0.1% difference). Without d "
             "the count is 1,083 (shortfall 18,467). The step 'selection operates at only 45% of the rate Haldane "
             "assumed' turns a time rescaling into a cut of the death budget; the record asserts only that d acts as "
             "a pure 2.22 factor. d's provenance is M-114, its meaning M-107.",
})
