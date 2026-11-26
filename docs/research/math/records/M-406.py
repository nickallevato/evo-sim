#!/usr/bin/env python3
"""M-406 record: Eden's hemoglobin conversion time (2.7e6 generations) against his printed inputs.

Object: docs/research/math/objects.yaml M-406 (formula, derivation). Eden (Wistar p.8, claim file D3c q2)
prints on the order of 2,700,000 generations for alpha to beta by a unique path of 120 point mutations,
'a little large but not implausible'; claim file D3c lists his inputs (420 nucleotides, mu 1e-6, N 1e6,
8-9 reachable amino acids per step, 20 generations per conversion). His formula is not printed. Claim
file D3c's model T = 120 x (t_wait + 20) with t_wait = 420 x 8.5 gives 430,800, and 1,287,600 with a
factor 3; the record asserts both, the per-step wait 2.7e6 needs and the size of each gap. Day (claim
file D3c q1) says the time 'vastly exceeds the time available' and states no time; Eden attaches 'many
powers of 10' only to the longer meandering path, for which he offers no estimate (claim file D3b q4).

Run: research/.venv/bin/python -I docs/research/math/records/M-406.py [--write]
Without --write it checks that M-406.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D3B, D3C = CL + "D3b-eden-two-hypotheses-and-path-length.md", CL + "D3c-eden-hemoglobin-2.7-million-generations.md"


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


# ---- inputs -------------------------------------------------------------------------------
EDEN = held(D3C, "On this basis we would expect on the order of 2,700,000 generations to be required for one hemoglobin "
                 "chain to transform to the other. This is a little large but not implausible.")
INPUTS = held(D3C, "Eden's inputs: 120 point mutations between alpha and beta by a unique path; 420 nucleotides; mutation "
                   "rate 10^-6; population 10^6; 8-9 amino acids reachable per step; 20 generations to convert the "
                   "population under strongest selection.")
MODEL = held(D3C, "Eden's stated model: T = 120 * (t_wait + 20), t_wait unspecified.")
DAY = held(D3C, "A minimum of 120 point mutations would be required to convert alpha to beta if evolution proceeded from one "
                "chain to the other, or from a common ancestor to both, then each step along the path must have been "
                "independently viable. But the path requires traversing sequence space through intermediate forms, and "
                "Eden calculated that even under generous assumptions about mutation rates and selection coefficients, the "
                "time required to do so vastly exceeds the time available.")
DAY_LEN = held(D3C, "The alpha chain contains 141 amino acids and the beta chain contains 146 amino acids.")
PATH = held(D3B, "The mathematical problem appears to me to be a difficult one and I have no estimate to offer except that it "
                 "clearly is many powers of 10 greater than the minimal distance of 120.")

steps, sites, aa, conv = 120, 420, 8.5, 20         # claim file D3c (Eden p.8); 8.5 = midpoint of '8-9'
printed = 2_700_000

# ---- reconstructions of claim file D3c -------------------------------------------------------
T1 = steps * (sites * aa + conv)
assert T1 == 430_800                               # object and claim file D3c
T3 = steps * (sites * aa * 3 + conv)
assert T3 == 1_287_600                             # with 3 nucleotide alternatives per site
near(printed / T1, 6.267, 0.001)                   # printed is 6.3x the first reconstruction
near(printed / T3, 2.097, 0.001)                   # and 2.1x the second
near(math.log10(printed / T1), 0.797, 0.001)       # gap under one order of magnitude (claim file D3c)

# ---- what 2.7e6 needs per step ------------------------------------------------------------
per_step = printed / steps
assert per_step == 22_500                          # claim file D3c '22,500 gen per step'
t_wait = per_step - conv
assert t_wait == 22_480
near(t_wait / (sites * aa), 6.297, 0.001)          # wait 6.3x the 420 x 8.5 reconstruction
near(t_wait / (sites * aa * 3), 2.099, 0.001)
# '8-9': the range at either end does not reach the printed figure
for a in (8, 9):
    assert steps * (sites * a * 3 + conv) < printed

finish({
    "object": "M-406",
    "inputs": [
        {"name": "Eden p.8 inputs", "value": {"steps": steps, "nucleotides": sites, "mu": 1e-6, "N": 1e6,
                                              "reachable_aa_per_step": "8-9 (8.5 used)", "generations_per_conversion": conv},
         "cite": "claim file D3c (Eden, Wistar p.8; the list is the claim file's reading, the formula is not printed)"},
        {"name": "Eden printed result", "value": printed, "cite": "claim file D3c q2 (Wistar p.8)"},
        {"name": "Day's account", "value": "vastly exceeds the time available (no figure)", "cite": "claim file D3c q1"},
        {"name": "meandering path", "value": "many powers of 10 greater than 120 (no estimate)", "cite": "claim file D3b q4"},
    ],
    "values": {
        "reconstruction_420x8.5": T1, "reconstruction_x3": T3,
        "printed_over_reconstructions": [g(printed / T1), g(printed / T3)],
        "printed_per_step": per_step, "printed_wait_per_step": t_wait,
        "mu_N_unused": "mu and N enter no reconstruction in claim file D3c; with them Eden's formula stays unrecovered",
    },
    "positions": {
        "day": {"reading": "Eden showed the time vastly exceeds the time available",
                "number": "none: Day gives no time and no time available; Eden's only computed figure is 2.7e6, "
                          "which he calls not implausible"},
        "critic": {"reading": "Eden's own figure is 2.7e6 'not implausible', and his inputs do not reproduce it",
                   "eden_printed": printed, "reconstructions": [T1, T3]},
    },
    "notes": "Eden's formula is not in the volume as held; T = 120 x (420 x 8.5 + 20) = 430,800 and with a factor 3 "
             "1,287,600. The printed 2,700,000 is 2.1x to 6.3x these (under one order), and needs 22,480 generations "
             "of waiting per step. The figure Eden prints is his own and he calls it 'not implausible'; Day's 'vastly "
             "exceeds' matches only Eden's uncomputed remark on the longer meandering path. Day's 141 and 146 residues "
             "are as in Day's text; claim file D3c reads Eden as 140 and 146 (minor, not a number in this object).",
})
