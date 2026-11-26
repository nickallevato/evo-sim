#!/usr/bin/env python3
"""M-018 record (inference): detectable sweep signatures, E_detect = K x W / T at power 1.

Object: docs/research/math/objects.yaml M-018 (inference, derivation). Human case (Z18452504:
3,200+ sweeps in 325,000 generations) and bonobo case (Z18441321: 326,000 loci in 930,000 y).
The record computes, side by side, Day's implied count of visible sweeps (all K) and the
critics' upper bound in a detection window W, and asserts each figure the statement claims.
Scan powers (SweepFinder2, iHS, Tajima's D) are not computed (R4 GAP-02 holds the audit
calculation; the statement says so). Inputs carry their quote id or claim file.

Run: research/.venv/bin/python -I docs/research/math/records/M-018.py [--write]
Without --write it checks that M-018.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
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


A6 = CL + "A6-sweep-signatures-absent.md"
A6A = CL + "A6a-bonobo-sweep-mosaic.md"
Q_A6_1 = held(A6, "If 3,200+ sweeps occurred in the human lineage over 325,000 generations, approximately one sweep "
                  "completes every 100 generations.")                                           # A6 q1
Q_A6_3 = held(A6, "identify dozens to hundreds of candidate sweep regions—not thousands.")       # A6 q3
BLOCKS = held(A6, "The human genome of 3.2 Gb therefore contains 3,200–32,000 independent linkage blocks.")
W_HUM = held(A6, "with W ≈ 10,000 generations (Hernandez 2011, citing Przeworski 2002)")
W_33K = held(A6, "325–3,250 at W = 33,000 (0.25 × 4 × Day's upper N_e of 33,000, MITTENS 3.0 §8.2)")
Q_A6A_1 = held(A6A, "If 326,000 loci fixed by selection in bonobos over 930,000 years, the entire genome should be a "
                    "mosaic of overlapping sweep signatures.")                                  # A6a q1
BON_T = held(A6A, "generations = 930,000 / 20 = 46,500 nominal, 40,000 effective with d = 0.86 (l.69)")
W_BON = held(A6A, "detection window W ≈ 0.25 × 4N_e = 20,000 generations at Day's N_e ≈ 20,000")
YOO30 = held(A6A, "against 30 SweepFinder2 candidates in bonobos (Yoo 2025)")


def e_detect(K, W, T):
    return K * min(W, T) / T


# ---- human case -----------------------------------------------------------------------------
K_lo, K_hi, T_h = 3_200, 32_000, 325_000
near(T_h / K_lo, 101.6, 0.05)                          # "one sweep completes every 100 generations"
E_lo = e_detect(K_lo, 10_000, T_h)
E_hi = e_detect(K_hi, 10_000, T_h)
assert int(E_lo) == 98                                 # "at most about 98"
assert round(E_hi) == 985
E33_lo, E33_hi = e_detect(K_lo, 33_000, T_h), e_detect(K_hi, 33_000, T_h)
assert round(E33_lo) == 325 and round(E33_hi, -1) == 3_250
assert round(0.25 * 4 * 33_000) == 33_000
near(E_lo / K_lo, 10_000 / T_h, 1e-12)                 # window share of the span: 3.1%

# ---- bonobo case ----------------------------------------------------------------------------
K_b = 326_000
T_nom = 930_000 / 20
assert T_nom == 46_500
T_eff = 40_000
near(T_nom * 0.86, T_eff, 10)                          # 39,990
W_b = 0.25 * 4 * 20_000
assert W_b == 20_000
Eb_nom, Eb_eff = e_detect(K_b, W_b, T_nom), e_detect(K_b, W_b, T_eff)
near(Eb_nom, 1.4e5, 0.005e5)
near(Eb_eff, 1.6e5, 0.05e5)
near(W_b / T_nom, 0.43, 0.005)
near(W_b / T_eff, 0.50, 1e-12)
Eb_small = e_detect(K_b, W_b / 10, T_eff)
near(Eb_small, 1.6e4, 0.05e4)                          # still 1.6e4 with a 10x smaller window
near(Eb_small / 30, 543, 1)                            # against Yoo's 30 candidates

finish({
    "object": "M-018",
    "inputs": [
        {"name": "human K, T", "value": [3_200, 325_000], "cite": "A6 q1 (Z18452504 s4.3 l.325)"},
        {"name": "human block range", "value": [3_200, 32_000], "cite": "claim file A6 (Z18452504 l.318)"},
        {"name": "scan counts", "value": "dozens to hundreds", "cite": "A6 q3"},
        {"name": "W human", "value": [10_000, 33_000], "cite": "claim file A6 (Hernandez 2011; MITTENS 3.0 s8.2 N_e); R4 GAP-02"},
        {"name": "bonobo K, years, g", "value": [326_000, 930_000, 20], "cite": "A6a q1; claim file A6a (Z18441321 l.69, l.71)"},
        {"name": "W bonobo", "value": 20_000, "cite": "claim file A6a (R4 GAP-02)"},
        {"name": "bonobo SweepFinder2 candidates", "value": 30, "cite": "claim file A6a (Yoo 2025, R4 GAP-02)"},
    ],
    "values": {
        "human": {"gens_per_sweep": g(T_h / K_lo), "E_detect_W10k": [g(E_lo), g(E_hi)], "E_detect_W33k": [g(E33_lo), g(E33_hi)]},
        "bonobo": {"T_nominal": T_nom, "T_effective": T_eff, "E_detect": [g(Eb_nom), g(Eb_eff)],
                   "window_share": [g(W_b / T_nom), g(W_b / T_eff)], "E_detect_window_div10": g(Eb_small),
                   "yoo_candidates": 30},
        "scan_powers": "not computed here (R4 GAP-02 holds the audit calculation)",
    },
    "positions": {
        "day": {"reading": "all K sweeps would leave visible signatures; scans would be saturated",
                "visible_human": [K_lo, K_hi], "visible_bonobo": K_b},
        "critic": {"reading": "only sweeps completed within the window W are detectable, at most K x W / T at power 1",
                   "visible_human_W10k": [g(E_lo), g(E_hi)], "visible_bonobo": [g(Eb_nom), g(Eb_eff)]},
    },
    "notes": "Human: at W = 10,000 the bound (98) is 'dozens to hundreds', so the observation does not contradict 3,200; "
             "at K = 32,000 or W = 33,000 it is 325-3,250. Bonobo: the window covers 43-50% of the span, so the bound "
             "(1.4-1.6e5) is far above Yoo's 30 candidates whatever the window. Powers are R4 GAP-02's.",
})
