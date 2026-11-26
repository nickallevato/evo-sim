#!/usr/bin/env python3
"""M-601 record (derivation): beneficial sweep latency (2/s) ln(2Ne) against the stochastic conditional mean.

Object: docs/research/math/objects.yaml M-601 (formula, derivation). Day's formula t = (2/s) ln(2Ne) (F q1 = F3 q1,
Q45; with s_eff in Z18166426, F3 q2) is the deterministic logistic sweep dp/dt = s p (1 - p) from p0 = 1/(2Ne) to
1 - p0: t = (1/s) [logit(1 - p0) - logit(p0)] = (2/s) ln((1 - p0)/p0) ~ (2/s) ln(2Ne). The record evaluates it at
Ne = 10,000 and s = 0.001 / 0.01 / 0.0005 (19,807 / 1,981 / 39,614), the conditional stochastic mean
(2/s)(ln 4Ns + gamma) (RESULTS B0.4 after review #2: 8,532 / 1,314 / 14,292), the 2.32x overstatement at s = 0.001,
and the logarithm the Z18166426 window p = 0.01 to 0.99 gives with the same dynamics (ln 99 = 4.595 under the
(2/s) prefactor, 9,190 generations; or ln 9,801 = 9.190 if the full logit difference is put under the same (2/s),
18,380) against ln(2Ne) = 9.9035. The diffusion value 8,480 and the simulated rows are quoted from RESULTS B0.4,
not recomputed. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-601.py [--write]
Without --write it checks that M-601.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
F = CL + "F-kimura-fixation-time-limits-fixations.md"
F1A = CL + "F1a-day-reply-throughput-and-serial-use-19800.md"
F3 = CL + "F3-beneficial-fixation-time-2-over-s-ln-2ne.md"
F3A = CL + "F3a-s-0-001-zeng-2021-misread.md"
QD = "docs/research/sources/quotes-day.md"
PY = "docs/research/parameters.yaml"
RES = "research/checks/RESULTS.md"
GAMMA = 0.5772156649015329                                        # Euler-Mascheroni constant


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
FORMULA = "Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one."
for rel in (F, F3, QD):
    held(rel, FORMULA)                                            # F q1, F3 q1, Q45
ZEN = held(F3, "Time to fixation calculated using t ≈ (2/s_eff) × ln(2N_e) for N_e = 10,000, from initial frequency "
               "p = 0.01 to p = 0.99.")                           # F3 q2, Z18166426 para 135
Q44 = held(F1A, "N_e = 10,000 (standard effective population constant) T = 22 years (generation, Gurven & Kaplan 2007) "
                "L = 51 years (lifespan based on Coale-Demeny-West life tables) s = 0.001 (selection coefficient, Zeng et "
                "al 2021) t ≈ 19,800 generations per fixation")    # F1a q3, Q44
held(QD, Q44)
FIVE = held(F1A, "The six-fixation figure (now seven at updated parameters) comes from the beneficial fixation time at "
                 "s = 0.001, not from neutral drift.")              # F1a q5
FORMAL = held(F3, "Deterministic logistic sweep: time from p₀ to 1 − p₀ at selection s (per Day's parametrisation) is "
                  "(2/s) ln((1−p₀)/p₀) ≈ (2/s) ln(2Nₑ) when p₀ = 1/(2Nₑ). The stochastic conditional mean time is "
                  "(2/s)(ln(4Ns) + γ) (RESULTS review #2 correction).")
F3_NUM = held(F3, "s = 0.001: (2/s)ln(2N) = 19,807 vs (2/s)(ln 4Ns + γ) = 8,532; s = 0.01: 1,981 vs 1,314; s = 0.0005: "
                  "39,614 vs 14,292.")
CORR = held(RES, "the stochastic asymptote is (2/s)(ln(**4**Ns)+γ), not ln(2Ns)")
B04_ROW = held(RES, "| **10⁴ (Day's)** | **0.001** | **20** | — | **8,480** | **19,807** | 8,532 |")
B04_SIM = held(RES, "| 500 | 0.01 | 10 | 698±3 | 703 | 1382 | 715 |")
OVER = held(F3A, "The B0.4 asymptote is 8,532 and Day overstates it 2.32x.")      # R4 F3a paragraph
ATTRIB = held(F, "not found in Kimura & Ohta 1969 or Kimura 1962")               # F Assumptions
CHARLES = held(F3, "Zenodo calculator Z19984826 writes the selected-sweep time as (2/(s̄·d)) ln(2Nₑ) and cites "
                   "Charlesworth 1994 for it")
NE = 1.0e4; held(PY, "Ne_modern_human: {value: 1.0e4")           # population.Ne_modern_human (= Day's N_e, Q44)
S = 0.001; held(PY, "s_zeng_2021: {value: 0.001")                # selection.s_zeng_2021 (= Day's s, Q44)
assert "N_e = 10,000" in Q44 and "s = 0.001" in Q44


def sweep(s, ne):                                                 # Day's formula
    return (2 / s) * math.log(2 * ne)


def logistic(s, p0, p1):                                          # dp/dt = s p (1 - p), time p0 -> p1
    lg = lambda p: math.log(p / (1 - p))
    return (lg(p1) - lg(p0)) / s


def cond_mean(s, n):                                              # (2/s)(ln 4Ns + gamma), B0.4 corrected
    return (2 / s) * (math.log(4 * n * s) + GAMMA)


# ---- Day's formula and its exact logistic form -----------------------------------------------------
L2N = near(math.log(2 * NE), 9.9035, 5e-5)
t = {s: sweep(s, NE) for s in (0.001, 0.01, 0.0005)}
near(t[0.001], 19807, 0.5); near(t[0.01], 1981, 0.5); near(t[0.0005], 39614, 0.5)
assert round(t[0.001], -2) == 19800                               # Day's printed 19,800 (Q44)
p0 = 1 / (2 * NE)
exact = logistic(S, p0, 1 - p0)
near(exact, 2 / S * math.log((1 - p0) / p0), 1e-6)                # the F3 formal statement's (2/s) ln((1-p0)/p0)
near(exact, t[0.001], 0.11)                                       # 19,806.6 against 19,807.0: the ~ is exact to 0.1 gen
for s in (0.01, 0.0005):                                          # latency scales as 1/s
    near(t[s] * s, t[0.001] * 0.001, 1e-9)

# ---- conditional stochastic mean and the overstatement -------------------------------------------
c = {s: cond_mean(s, NE) for s in t}
near(c[0.001], 8532, 0.5); near(c[0.01], 1314, 0.5); near(c[0.0005], 14292, 0.5)
ratio = {s: t[s] / c[s] for s in t}
near(ratio[0.001], 2.32, 0.005)                                   # B0.4 / R4 F3a: 2.32x at Day's parameters
near(ratio[0.01], 1.508, 0.001); near(ratio[0.0005], 2.772, 0.001)
diff_8480 = 8480                                                  # RESULTS B0.4 diffusion integral (quoted, not rerun)
assert "**8,480**" in B04_ROW
near(t[0.001] / diff_8480, 2.336, 0.001)                          # against the diffusion integral
near(c[0.001] / diff_8480, 1.006, 0.001)                          # asymptote within 0.6% of the diffusion value
assert "ln(**4**Ns)+γ" in CORR
near(cond_mean(0.01, 500), 715, 0.5); near(sweep(0.01, 500), 1382, 0.5)      # B0.4 first row, both closed forms
assert "698±3 | 703" in B04_SIM                                   # its simulated and diffusion columns (quoted)

# ---- the Z18166426 window p = 0.01 -> 0.99 -------------------------------------------------------
assert "p = 0.01 to p = 0.99" in ZEN
L99 = near(math.log(99), 4.595, 5e-4)
L9801 = near(math.log(9801), 9.190, 5e-4)
near(L9801, 2 * L99, 1e-12)
win = logistic(S, 0.01, 0.99)                                     # same dynamics as (2/s) ln(2Ne)
near(win, (2 / S) * L99, 1e-6); near(win, 9190, 0.5)              # (2/s) x 4.595
alt = (2 / S) * L9801; near(alt, 18380, 0.5)                      # full logit difference under the (2/s) prefactor
near(L2N - L99, 5.308, 5e-4); near(L2N - L9801, 0.713, 5e-4)
near(t[0.001] / win, 2.155, 0.001); near(t[0.001] / alt, 1.078, 0.001)

finish({
    "object": "M-601",
    "inputs": [
        {"name": "formula", "value": "t = (2/s) ln(2Ne)", "cite": "F q1, F3 q1 (Q45); Z18166426 with s_eff: F3 q2"},
        {"name": "Ne, s", "value": [NE, S], "cite": "Q44 (F1a q3); parameters population.Ne_modern_human, selection.s_zeng_2021"},
        {"name": "conditional mean asymptote", "value": "(2/s)(ln 4Ns + gamma)", "cite": "RESULTS B0.4 (review #2 correction); F3 formal statement"},
        {"name": "diffusion integral at Ne = 1e4, s = 0.001", "value": diff_8480, "cite": "RESULTS B0.4 table (quoted, not rerun)"},
        {"name": "Zenodo window", "value": [0.01, 0.99], "cite": "F3 q2 (Z18166426 para 135)"},
    ],
    "values": {
        "ln_2Ne": round(L2N, 4),
        "sweep_time": {str(s): round(v, 1) for s, v in t.items()},
        "exact_logistic_p0_to_1_minus_p0_s0.001": round(exact, 1),
        "conditional_mean": {str(s): round(v, 1) for s, v in c.items()},
        "overstatement": {str(s): round(v, 3) for s, v in ratio.items()},
        "over_diffusion_8480": round(t[0.001] / diff_8480, 3),
        "window_0.01_0.99": {"ln_99": round(L99, 4), "ln_9801": round(L9801, 4),
                             "time_logistic_(2/s)ln99": round(win, 1), "time_(2/s)ln9801": round(alt, 1),
                             "log_gap_to_ln2Ne": [round(L2N - L99, 4), round(L2N - L9801, 4)]},
    },
    "positions": {
        "day": {"reading": "(2/s) ln(2Ne) is the fixation time of a beneficial allele and enters the six/seven figure",
                "holds": "arithmetic exact: 19,807 (printed 19,800); a standard deterministic sweep-time approximation"},
        "critic": {"reading": "deterministic sweep time, not the conditional mean; a latency, not a spacing (F1)",
                   "holds": "conditional mean 8,532 (diffusion 8,480), so the formula overstates it 2.32x at s = 0.001"},
    },
    "notes": "The formula is the exact deterministic time from 1/(2Ne) to 1 - 1/(2Ne) under dp/dt = s p(1 - p) "
             "(19,806.6 against 19,807.0). The Zenodo text's window 0.01 -> 0.99 does not match it: the same dynamics "
             "give (2/s) ln 99 = 9,190, and ln 9,801 = 9.190 under the same prefactor gives 18,380; neither log is "
             "ln(2Ne) = 9.9035, so the stated window and the computed 19,807 use different starting points. Attribution: "
             "the claim files find the formula not in Kimura & Ohta 1969 (Z19984826 cites Charlesworth 1994); neither "
             "paper is in sources/raw/, so the record holds the claim files' statements, not the papers. The latency "
             "question (does it bound the count) is M-115/M-602, not this record.",
})
