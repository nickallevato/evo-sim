#!/usr/bin/env python3
"""M-402 record: count of protein molecules that ever existed (Eden's biosphere inputs and Day's).

Object: docs/research/math/objects.yaml M-402 (parameter, derivation). Eden (Wistar p.7, claim file D3a
q1) states the inputs and prints about 10^52 (claim file D3 q2); his working paper (p.110) says less than
10^55; Day's chapter 6 (claim file D3a q3) restates the inputs differently (10^18 cells per cm^3, protein
concentration 1e-4) and prints approximately 10^52. The record recomputes both from the count
N = (protein mass / molar mass) x N_A x (age / lifetime), with the reconstruction constants of claim
file D3a (Earth radius 6.371e8 cm, 250 residues x 110 Da = 27.5 kDa, 1e10 y = 3.156e17 s), asserts the
gap to the printed 10^52, the mass-fraction reading under which Day's inputs give 3.5e51, and the cell
size implied by Day's inputs read as printed. Inputs carry their claim file and quote number.

Run: research/.venv/bin/python -I docs/research/math/records/M-402.py [--write]
Without --write it checks that M-402.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D3, D3A = CL + "D3-eden-sequence-space-arithmetic.md", CL + "D3a-eden-molecules-not-functional-proteins.md"


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
EDEN = held(D3A, "Assume a biosphere of cells 1 cm. thick over the surface of the earth, a protein concentration in these "
                 "cells of 30%, a density of 1, an age for life on earth of 10 billion years and an average lifetime of a "
                 "protein molecule of 1 second. Of course all these quantities except density err very heavily toward "
                 "the high side.")
EDEN_N = held(D3, "The number of protein molecules that ever existed is by this computation about 10 52 •")
EDEN_USEFUL = held(D3A, "Yet this relatively small set of 1052 proteins contains within it all the useful proteins which "
                        "have existed to date.")
EDEN_SPECIES = held(D3, "Clearly the number of species of protein molecules is much smaller than this, say 1040")
WP = held(D3, "In fact the number of protein molecules of such size that ever existed on earth can be estimated to be less "
              "than 10 55 •")
DAY = held(D3A, "Assume a biosphere one centimeter thick covering the entire Earth, filled with cells at a density of a "
                "billion billion per cubic centimeter, each containing proteins at a concentration of one ten-thousandth, "
                "with each protein molecule lasting an average of one second, over a total span of ten billion years. This "
                "yields approximately one followed by fifty-two zeros—ten thousand trillion trillion trillion trillion—"
                "protein molecules that could ever have existed.")
CONST = held(D3A, "Biosphere volume V = 4*pi*R^2 * 1 cm = 5.10e18 cm^3 (R = 6.371e8 cm); protein mass m = V * density(1 "
                  "g/cm^3) * c; molecules alive = m*N_A/M; ever = alive * (1e10 yr = 3.156e17 s) / (1 s). With M = 27.5 "
                  "kDa (250 residues x 110 Da):")

R_cm, thick_cm, density = 6.371e8, 1.0, 1.0       # claim file D3a reconstruction; Eden p.7 '1 cm', 'density of 1'
M = 250 * 110                                      # g/mol, claim file D3a
N_A = 6.02214076e23                                # exact SI value
age_s = 1e10 * 3.156e7                             # 10 billion years (Eden; Day), claim file D3a 3.156e17 s
life_s = 1.0                                       # Eden; Day
assert M == 27_500
near(age_s, 3.156e17, 1e3)


def ever(c):
    V = 4 * math.pi * R_cm ** 2 * thick_cm
    m = V * density * c
    alive = m * N_A / M
    return V, m, alive, alive * age_s / life_s


# ---- Eden's p.7 inputs ---------------------------------------------------------------------
V, m_e, alive_e, N_e = ever(0.30)
near(V, 5.10e18, 0.005e18)
near(m_e, 1.53e18, 0.005e18)
near(alive_e, 3.35e37, 0.005e37)
near(N_e, 1.06e55, 0.005e55)
logN_e = math.log10(N_e)
near(logN_e, 55.02, 0.005)                         # object: 10^55.0
assert 1e55 < N_e < 10 ** 55.03                    # working paper 'less than 10^55': matches to rounding, 0.02 orders over
gap_e = logN_e - 52
near(gap_e, 3.02, 0.005)                           # 3 orders above the printed 10^52

# ---- Day's ch.6 inputs ---------------------------------------------------------------------
_, m_d, alive_d, N_d = ever(1e-4)                  # 1e-4 read as a mass fraction of the biosphere volume
near(m_d, 5.10e14, 0.005e14)
near(alive_d, 1.12e34, 0.005e34)
near(N_d, 3.5e51, 0.05e51)                         # object and claim file D3a: 3.5e51
logN_d = math.log10(N_d)
near(logN_d, 51.55, 0.005)
assert round(logN_d) == 52                         # 'approximately one followed by fifty-two zeros'
# read as printed: 1e18 cells per cm^3 means a cell volume of 1e-18 cm^3
cell_cm = (1 / 1e18) ** (1 / 3)
near(cell_cm * 1e7, 10.0, 1e-6)                    # 10 nm across (1 cm = 1e7 nm), below virus size

# ---- molecules against distinct sequences --------------------------------------------------
near(logN_e - 40, 15.02, 0.005)                    # Eden's own 'say 10^40' species: 15 orders below his molecule count
near(52 - 40, 12, 0)

finish({
    "object": "M-402",
    "inputs": [
        {"name": "Eden biosphere inputs", "value": {"thickness_cm": thick_cm, "protein_fraction": 0.30, "density": density,
                                                    "age_y": 1e10, "lifetime_s": life_s},
         "cite": "claim file D3a q1 (Eden, Wistar p.7)"},
        {"name": "Eden printed counts", "value": {"talk_p7": "about 10^52", "working_paper_p110": "less than 10^55",
                                                  "species": "say 10^40"},
         "cite": "claim file D3 q2, q3 and working-paper quote; claim file D3a q2 ('all the useful proteins')"},
        {"name": "Day ch.6 inputs", "value": {"cells_per_cm3": 1e18, "protein_concentration": 1e-4, "lifetime_s": 1,
                                              "age_y": 1e10, "printed": "approximately 10^52"},
         "cite": "claim file D3a q3 (Dembski Substack 2026-09-28, ch.6)"},
        {"name": "reconstruction constants", "value": {"R_cm": R_cm, "molar_mass_g": M, "N_A": N_A, "age_s": age_s},
         "cite": "claim file D3a formal statement (not parameters.yaml keys)"},
    ],
    "values": {
        "biosphere_volume_cm3": g(V),
        "eden_p7_inputs": {"protein_mass_g": g(m_e), "alive": g(alive_e), "ever": g(N_e), "log10": g(logN_e),
                           "orders_above_printed_1e52": g(gap_e)},
        "day_ch6_mass_fraction_reading": {"protein_mass_g": g(m_d), "alive": g(alive_d), "ever": g(N_d), "log10": g(logN_d)},
        "day_ch6_as_printed_cell_size_nm": g(cell_cm * 1e7),
    },
    "positions": {
        "day": {"reading": "about 10^52 molecules ever, standing for all useful (Day: functional) proteins",
                "printed": 52, "day_inputs_log10_mass_fraction_reading": g(logN_d)},
        "critic": {"reading": "the printed inputs do not give 10^52; the count is of molecules, not functional sequences",
                   "eden_inputs_log10": g(logN_e), "species_log10": 40,
                   "note": "the 273-order comparison moves by 3 orders at most (M-401)"},
    },
    "notes": "Eden's p.7 inputs give 1.06e55 (10^55.02), 0.02 orders over his working paper's 'less than 10^55' (a match to rounding) and 3.0 orders "
             "above the 10^52 printed in the talk. Day's ch.6 inputs give 3.5e51 (approximately 10^52) only if the 1e-4 "
             "concentration is a mass fraction of the whole biosphere volume; read as printed, 10^18 cells per cm^3 "
             "means 10 nm cells. Either count is of molecules, not distinct sequences: Eden's own 'say 10^40' species is "
             "12 to 15 orders lower. None of this moves the 273-order gap of M-401 by more than 3 orders.",
})
