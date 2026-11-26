#!/usr/bin/env python3
"""M-602 record (derivation): the human 19,807 divisor and the six/seven-fixation figure.

Object: docs/research/math/objects.yaml M-602 (formula, derivation). Day's Q&A (F1a q3, Q44) gives Ne = 10,000,
s = 0.001 and "t ≈ 19,800 generations per fixation" without the formula; (2/s) ln(2Ne) = 2000 x 9.9035 = 19,807
(M-601). The Education post (F1a q5) says the six (now seven) fixations come from this time. Day does not print the
window inputs: the 6.3 and 7.4 are claim file F1a's reconstruction (9e6 y / 32.5 y x 0.45 / 19,807 and
146,250 / 19,807), labelled as such here; the window values are parameters.yaml entries with Day sources, all
verified: false. The record checks those quotients, that the implied spacing between fixations equals the one-allele
latency (width factor 1, the serial reading), the alternative divisor readings F1a lists, and the comparison with the
LTEE 1,600 and 1,322 gen/fix (throughput figures). Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-602.py [--write]
Without --write it checks that M-602.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
F1A = "docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md"
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


# ---- inputs: Day's words ---------------------------------------------------------------------------
Q2 = held(F1A, "The Probability Zero derivation at s = 0.001 does compute a per-fixation time, but dividing total "
               "generations by per-fixation time to get maximum achievable fixations is not an assumption of sequential "
               "processing. It is also a throughput calculation")  # F1a q2
Q44 = held(F1A, "N_e = 10,000 (standard effective population constant) T = 22 years (generation, Gurven & Kaplan 2007) "
                "L = 51 years (lifespan based on Coale-Demeny-West life tables) s = 0.001 (selection coefficient, Zeng et "
                "al 2021) t ≈ 19,800 generations per fixation")    # F1a q3
held(QD, Q44)                                                     # Q44, Q&A para 5
Q4 = held(F1A, "It probably won’t escape your attention that 19,800 > 1,600. So using the 1,600 generations rate was "
               "extremely generous to the Modern Synthesis model.")  # F1a q4
Q5 = held(F1A, "The six-fixation figure (now seven at updated parameters) comes from the beneficial fixation time at "
               "s = 0.001, not from neutral drift.")                # F1a q5
Q1 = held(F1A, "The LTEE rate of 1,322 gen/fix is a total throughput measurement")   # F1a q1
NOFORM = held(QD, "Formula not shown in the Q&A; (2/0.001) x ln(20,000) = 19,807 (derived)")
ADJ = held(F1A, "describes the division as a throughput calculation \"adjusted for parallelism\" but does not identify a "
                "width factor in the six/seven figure")

# ---- inputs: the claim file's reconstruction (not Day's printed inputs) --------------------------
RECON = held(F1A, "Reconstruction (derived; Day does not print the inputs): 9×10⁶ y / 32.5 y × 0.45 / 19,807 = 6.3; and "
                  "146,250 / 19,807 = 7.4 (\"now seven at updated parameters\").")
OTHER = held(F1A, "Other readings of the same divisor: 252,000/19,807 = 12.7; 252,000 × 0.45/19,807 = 5.7.")
WIDTH = held(F1A, "Z18167588 (Bernoulli) §7.8 multiplies by a parallel width instead: (300,000/440) × 230 = 157,000, "
                  "where 440 ≈ (2/0.01) ln 9 = 439 is a latency and 230 is a number of simultaneous sweeps")
T_DIV = 9.0e6; held(PY, "day_2019: {value: 9.0e6, source: B2019-02-07")      # divergence.t_div_years.day_2019
G_ALT = 32.5; held(PY, "day_alt: {value: 32.5, source: B2025-01-18")         # generation_time_years.day_alt
D = 0.45; held(PY, "turnover_d: {value: 0.45, source: Z18166234")            # selection.turnover_d
G_EFF = 146250; held(PY, "day_2025_effective: {value: 146250, derived: \"325000*0.45\"")   # generations_available
G_2026 = 252000; held(PY, "day_2026: {value: 252000, source: Z23003785")     # generations_available.day_2026
GF_1600 = 1600; held(PY, "day_2019: {value: 1600, source: B2019-02-07")      # ltee.gens_per_fixation.day_2019
GF_1322 = 1322; held(PY, "day_mittens3_nonmutator: {value: 1322")            # ltee.gens_per_fixation
NE, S = 10_000, 0.001
assert "N_e = 10,000" in Q44 and "s = 0.001" in Q44 and "19,800" in Q44

# ---- the divisor ----------------------------------------------------------------------------------
L = near(math.log(2 * NE), 9.9035, 5e-5)
near(2 / S, 2000, 0)
t = near((2 / S) * L, 19807, 0.5)
near(2000 * 9.9035, 19807, 0)                                     # the statement's product with the rounded log
assert round(t, -2) == 19800
rate = near(1 / t, 5.05e-5, 5e-8)                                 # G_f = 19,807 read as gen/fix: 5.05e-5 fix/gen

# ---- six and seven (claim-file reconstruction) -----------------------------------------------------
window = T_DIV / G_ALT * D
near(T_DIV / G_ALT, 276923, 0.5); near(window, 124615, 0.5)
six = near(window / t, 6.3, 0.05)                                 # "six-fixation figure"
near(G_EFF, 325000 * D, 0)
seven = near(G_EFF / t, 7.4, 0.05)                                # "now seven at updated parameters"
assert round(six) == 6 and math.floor(seven) == 7
twelve = near(G_2026 / t, 12.7, 0.05)                             # other readings F1a lists
five = near(G_2026 * D / t, 5.7, 0.05)

# ---- no width factor: the implied spacing equals the one-allele latency ---------------------------
for count, gens in ((six, window), (seven, G_EFF)):
    near(gens / count, t, 1e-6)                                   # spacing = window / count = latency, width W = 1
width_implied = t / (window / six)
near(width_implied, 1.0, 1e-12)
near((300000 / 440) * 230, 157000, 200)                           # Z18167588 s7.8 width product (branch G; contrast)
near((2 / 0.01) * math.log(9), 439, 0.5)
for W in (10, 230):                                               # what a width factor would do to the count
    near(W * window / t, W * six, 1e-9)

# ---- comparison with the LTEE throughput figures --------------------------------------------------
assert t > GF_1600 and t > GF_1322 and "19,800 > 1,600" in Q4
near(t / GF_1600, 12.38, 0.005); near(t / GF_1322, 14.98, 0.005)
near(1 / GF_1600, 6.25e-4, 1e-9)
assert "throughput" in Q1 and "throughput" in Q2

finish({
    "object": "M-602",
    "inputs": [
        {"name": "Ne, s, t", "value": [NE, S, 19800], "cite": "Q44 (F1a q3); formula not printed in the Q&A"},
        {"name": "window 9e6 y, 32.5 y, d = 0.45", "value": [T_DIV, G_ALT, D],
         "cite": "CLAIM-FILE RECONSTRUCTION (F1a formal statement; Day does not print the inputs); values from parameters "
                 "divergence.t_div_years.day_2019, generation_time_years.day_alt, selection.turnover_d (verified: false)"},
        {"name": "window 146,250", "value": G_EFF,
         "cite": "CLAIM-FILE RECONSTRUCTION (F1a); parameters generations_available.day_2025_effective (325000*0.45, verified: false)"},
        {"name": "alternative windows", "value": [G_2026, G_2026 * D], "cite": "F1a formal statement; parameters generations_available.day_2026"},
        {"name": "LTEE gen/fix", "value": [GF_1600, GF_1322], "cite": "F1a q4, q1; parameters ltee.gens_per_fixation.day_2019, day_mittens3_nonmutator"},
    ],
    "values": {
        "ln_2Ne": round(L, 4), "divisor": round(t, 1), "fixations_per_generation_if_spacing": round(rate, 8),
        "six": round(six, 2), "seven": round(seven, 2), "other_readings": {"252000": round(twelve, 2), "252000x0.45": round(five, 2)},
        "window_generations": {"9e6/32.5x0.45": round(window, 1), "146250": G_EFF},
        "implied_width_factor": width_implied,
        "divisor_over_ltee": {"1600": round(t / GF_1600, 3), "1322": round(t / GF_1322, 3)},
    },
    "positions": {
        "day": {"reading": "the division is a throughput calculation adjusted for parallelism; 19,800 > 1,600",
                "holds": "the arithmetic is exact (19,807; 6.3; 7.4) and 19,807 > 1,600"},
        "critic": {"reading": "a one-allele latency used as generations per fixation is the serial reading",
                   "holds": "the reconstructed counts are window x d / latency, implied width exactly 1; no width factor"},
    },
    "notes": "19,807 is a per-allele sweep latency (M-601); dividing a window by it gives one fixation per latency, so the "
             "six/seven figure carries width 1 whatever the division is called. Day's 'adjusted for parallelism' names no "
             "width factor in this figure; the Bernoulli paper's (300,000/440) x 230 shows what one looks like. The 1,600 "
             "and 1,322 gen/fix are LTEE throughputs (counts over a window), so '19,800 > 1,600' compares a latency with a "
             "throughput. The 6.3 and 7.4 inputs are the claim file's reconstruction; Day prints neither the window nor "
             "the quotient, and the parameters.yaml values carry verified: false.",
})
