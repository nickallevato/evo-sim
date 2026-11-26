#!/usr/bin/env python3
"""M-707 record (derivation): the required beneficial input, 230 / 0.02 = 11,500 per transit, 7.84e6 in total.

Object: docs/research/math/objects.yaml M-707 (formula, derivation). Z18167588 s7.9 (Gd q1): required input per
transit period = C / P_escape = 230 / 0.02 = 11,500 with P_escape = 2s = 0.02 (Kimura 1962) at s = 0.01; times
300,000/440 transit periods = 7.84e6 (paper: 7.8 million). The population supply it is set against (Gd formal
statement): 2 x 38.4 = 76.8, about 77 new mutations per diploid individual per generation (3.2e9 bp x 1.2e-8 per
haploid genome), x 10,000 = 7.7e5 per generation, 2.3e11 over 300,000 generations; the need is a fraction 3.4e-5 of
that, or 1.7e-5 of McCarthy's 4.5e11 (MC-03). The paper calls the beneficial fraction an empirical question; the
record states the fraction and does not estimate it. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-707.py [--write]
Without --write it checks that M-707.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G = CL + "G-bernoulli-barrier.md"
GD = CL + "Gd-drift-input-constraint.md"
GC = CL + "Gc-pipeline-cap-230-sweeps.md"
QC = "docs/research/sources/quotes-critics.md"
PY = "docs/research/parameters.yaml"
R4G1 = "research/checks/results/R4-G1.md"


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
GD_Q = held(GD, "Required input ≈ 230 / 0.02 ≈ 11,500 beneficial mutations per transit period")   # Gd q1 (s7.9)
GD_TOT = held(GD, "\"Total required input ≈ (300,000 / 440) × 11,500 ≈ 7.8 million beneficial mutations\"")
GD_EMP = held(GD, "which the paper itself calls \"an empirical question\"")
GD_SUP = held(GD, "77 diploid per individual per generation x 10,000 = 7.7e5 per generation, 2.3e11 over 300,000 "
                  "generations")
GD_FRAC = held(GD, "The 7.8e6 beneficial arisings needed would then be 3.4e-5 of all new mutations")
KIM = held(G, "the probability of ultimate survival of an advantageous mutant gene is approximately twice the "
              "selection coefficient")                            # Kimura 1962
GC_T = held(GC, "fixations ≤ (T/t_transit)·C with C = 230, T = 300,000.")
MC03 = held(QC, "50,000 x 9 million = 450 billion new mutations altogether.")
G1_ANY = held(R4G1, "**Day's own Gd (s7.9) is an \"any n of M\" calculation:** 157,000/0.02 = 7.85e6.")
HAP = 38.4; held(PY, "new_mutations_per_haploid_genome: {value: 38.4, derived: \"3.2e9 bp x 1.2e-8\"")
MU = 1.2e-8; held(PY, "pedigree_human: {value: 1.2e-8")         # mutation.mu_per_site_per_gen.pedigree_human
N = 1.0e4; held(PY, "Ne_modern_human: {value: 1.0e4")             # population.Ne_modern_human (Day's N = 10,000)
C, S, T, T_TRANSIT = 230, 0.01, 300_000, 440

# ---- the required input ---------------------------------------------------------------------------------
p_esc = 2 * S
assert p_esc == 0.02
per_transit = C / p_esc
near(per_transit, 11_500, 1e-9)
n_transit = T / T_TRANSIT
near(n_transit, 681.82, 0.005)
total = n_transit * per_transit
near(total, 7.841e6, 500); assert round(total / 1e6, 1) == 7.8   # paper: 7.8 million
near(157_000 / p_esc, 7.85e6, 1e-6)                               # R4 G1's form: n / P_escape
near(total / (157_000 / p_esc), 0.9988, 5e-4)                     # the two differ only by 156,818 vs 157,000

# ---- the supply it is set against ------------------------------------------------------------------------
near(3.2e9 * MU, HAP, 1e-9)
per_ind = 2 * HAP
near(per_ind, 76.8, 1e-9); assert round(per_ind) == 77
per_gen = per_ind * N
near(per_gen, 7.68e5, 1e-6)
supply = per_gen * T
near(supply, 2.304e11, 1e6)
frac = total / supply
near(frac, 3.40e-5, 0.005e-5)
frac_77 = total / (77 * N * T)                                    # with the rounded 77
near(frac_77, 3.39e-5, 0.005e-5)
near(50_000 * 9e6, 4.5e11, 0)                                     # MC-03
frac_mc = total / 4.5e11
near(frac_mc, 1.74e-5, 0.005e-5)

finish({
    "object": "M-707",
    "inputs": [
        {"name": "C, P_escape, T, t_transit", "value": [C, p_esc, T, T_TRANSIT], "cite": "Gd q1 (Z18167588 s7.9); Gc formal statement; Kimura 1962 (G)"},
        {"name": "new mutations per haploid genome", "value": HAP, "cite": "parameters mutation.new_mutations_per_haploid_genome (3.2e9 x 1.2e-8)"},
        {"name": "N", "value": N, "cite": "parameters population.Ne_modern_human (Day's N = 10,000)"},
        {"name": "McCarthy supply", "value": 4.5e11, "cite": "MC-03"},
    ],
    "values": {
        "per_transit": per_transit, "transit_periods": round(n_transit, 3), "total_required": round(total),
        "n_over_P_escape": 157_000 / p_esc,
        "supply": {"per_individual": per_ind, "per_generation": per_gen, "over_T": supply},
        "beneficial_fraction_needed": {"of_2.3e11": round(frac, 8), "of_4.5e11": round(frac_mc, 8)},
    },
    "positions": {
        "day": {"reading": "the cap of 230 requires about 11,500 beneficial mutations per transit, 7.8 million in total",
                "holds": "11,500 and 7,840,909 reproduce (printed 7.8 million)"},
        "critic": {"reading": "an any-n-of-M supply calculation; whether the beneficial fraction is attainable is open",
                   "holds": "the need is 3.4e-5 of 2.3e11 new mutations (1.7e-5 of 4.5e11); the record gives no DFE"},
    },
    "notes": "Arithmetic reconciles. The calculation counts any 7.8e6 beneficial arisings, not a named list (R4 G1: "
             "Day's own s7.9 is an any-n-of-M calculation). Whether 3.4e-5 (or 1.7e-5) of new mutations are beneficial "
             "at s = 0.01 is the empirical question the paper names; no DFE source is held for it here. The 77 is the "
             "audit's diploid reading of 3.2e9 x 1.2e-8 per haploid genome (parameters, verified: false).",
})
