#!/usr/bin/env python3
"""M-016 record (inference): units of G_f, years against generations (X = A x B).

Object: docs/research/math/objects.yaml M-016 (inference, derivation). Years per fixation X = A x B,
with A generations per fixation and B years per generation (1 = LTEE, 2 = humans). The record
computes X1 and X2 under Day's transfer (A2 = A1) and shows that the per-year gap X2/X1 is B2/B1
whatever A is. Matev's position has no number to compute: it says A2 >= A1 is not shown, and no
held text gives A2. Inputs carry their quote id, parameters.yaml key or claim file.

Run: research/.venv/bin/python -I docs/research/math/records/M-016.py [--write]
Without --write it checks that M-016.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

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


RF4 = held(CL + "A2i-matev-gf-units-years-vs-generations.md",
           "The reasoning is that 1/X1 is high (due to 1/B1 being high), so it very generous for the estimation of X2 "
           "to use the A1 value as an estimate for A2 even though A1 isn't why 1/X1 is high.")   # A2i q1
GPD = held(PY, "generations_per_day: {value: 6.64")
Q58 = held(QD, "1,322 generations per fixation")
Q85 = held(QD, "is 1,587 generations per fixation")
Q18 = held(QD, "At 25 years per human generation")

YEAR_D = 365.25
B1 = 1 / (6.64 * YEAR_D)                               # LTEE years per generation
near(B1 * YEAR_D * 24, 3.61, 0.005)                    # about 3.6 hours per generation
B2 = 25
A1 = (1322, 1587)

# ---- LTEE years per fixation -----------------------------------------------------------------
X1 = [a * B1 for a in A1]
near(X1[0], 0.545, 0.0005)
near(X1[1], 0.654, 0.0005)
assert all(x < 1 for x in X1)                          # well under a year per fixation

# ---- Day: A2 = A1 (generations transfer, years do not) -------------------------------------
X2 = [a * B2 for a in A1]
assert X2 == [33_050, 39_675]
ratio = [x2 / x1 for x1, x2 in zip(X1, X2)]
for r in ratio:
    near(r, B2 / B1, 1e-6)                             # per-year gap is B2/B1 for any A
near(B2 / B1, 25 * 6.64 * 365.25, 1e-6)
near(B2 / B1, 60_631.5, 0.01)
assert math.isclose(ratio[0], ratio[1])

# ---- Matev: whether A2 >= A1 is not shown; for any A2 the per-year factor is B2 x A2 ----------
# Day's transfer is 'generous' to evolution only if A2 >= A1; held text gives no A2, so no number.
for A2 in (A1[0] / 10, A1[0], A1[0] * 10):             # illustrative grid, not a position
    assert math.isclose((A2 * B2) / X1[0], (A2 / A1[0]) * (B2 / B1))

finish({
    "object": "M-016",
    "inputs": [
        {"name": "Matev units argument", "cite": "A2i q1 (RF-4)", "quote": RF4},
        {"name": "LTEE generations per day", "value": 6.64, "cite": "parameters ltee.generations_per_day (also Z23003785 p.4; verified: false)"},
        {"name": "A1 (G_f)", "value": list(A1), "cite": "Q58, Q85"},
        {"name": "B2 (human g_len)", "value": B2, "cite": "Q18"},
    ],
    "values": {
        "B1_years": g(B1), "B1_hours": g(B1 * YEAR_D * 24), "X1_years": [g(x) for x in X1],
        "X2_years_if_A2_eq_A1": X2, "X2_over_X1": g(B2 / B1),
    },
    "positions": {
        "day": {"reading": "G_f is in generations, so generation time is not a factor; A2 = A1",
                "X2_years": X2, "per_year_gap_from_B_only": g(B2 / B1)},
        "critic": {"reading": "the LTEE's high per-year rate comes from short B1, not low A1, so it says nothing about A2 against A1",
                   "number": None,
                   "why_none": "Matev states no A2; the position is that A2 >= A1 is unshown, which has no figure to check"},
    },
    "notes": "Both readings agree on the arithmetic: X = A x B and X2/X1 = (A2/A1)(B2/B1). The dispute is A2/A1, which "
             "no held source measures; the statement claims no number for it, so the object is resolved, not blocked.",
})
