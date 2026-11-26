#!/usr/bin/env python3
"""M-017 record (identity): the human-derived rate of MITTENS 3.0 s8.6 (one fixation per 27,600).

Object: docs/research/math/objects.yaml M-017 (identity, derivation). Asserts 252,000/27,600 =
9.13 against the printed 8, what the printed 8 implies (220,800 generations, 5.5 My at 25 y),
the size of the gap (12%) and that it is immaterial to the 205M shortfall. Inputs carry their
quote id; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-017.py [--write]
Without --write it checks that M-017.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"


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


Q19 = held(QD, "yields approximately one fixation per 27,600 effective generations (Day and Athos 2025, Appendix D). "
               "Applied to 252,000 generations provides 8 achievable fixations against the 205 million required.")
Q18 = held(QD, "At 25 years per human generation, this provides 252,000 generations.")

F = 252_000 / 27_600
near(F, 9.13, 0.005)
printed = 8
assert printed * 27_600 == 220_800
assert printed * 27_600 * 25 == 5_520_000              # the printed 8 fits t_div = 5.5 My at 25 y
off = 1 - printed / F
near(off, 0.124, 0.001)                                # printed 8 is 12% below its own inputs
s_printed, s_corr = 205e6 / printed, 205e6 / F
near(s_printed, 25.6e6, 0.05e6)
near(s_corr, 22.45e6, 0.01e6)
near(1 - s_corr / s_printed, 0.124, 0.001)             # shortfall moves 12%, still about 2e7
assert s_corr > 1e7                                    # immaterial to the conclusion

finish({
    "object": "M-017",
    "inputs": [
        {"name": "human-derived G_f, N_gen, printed F, R", "value": [27_600, 252_000, 8, 205e6], "cite": "Q19 (Z23003785 s8.6 p.15)"},
        {"name": "g_len", "value": 25, "cite": "Q18"},
    ],
    "values": {
        "F": g(F), "printed_F": printed, "gens_for_printed_F": 220_800, "t_div_for_printed_F_at_25y": 5.52e6,
        "printed_below_by": g(off), "shortfall_printed": g(s_printed), "shortfall_corrected": g(s_corr),
    },
    "positions": {
        "day": "about 8 achievable fixations against 205 million required",
        "critic": "the printed 8 is 9.13 on its own inputs; the figure does not reproduce but the conclusion is unchanged",
    },
})
