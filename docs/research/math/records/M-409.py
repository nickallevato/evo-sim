#!/usr/bin/env python3
"""M-409 record: Ulam's serial improvement time (10^13 generations) and Mayr's two objections.

Object: docs/research/math/objects.yaml M-409 (formula, derivation). Ulam (Wistar p.24, claim file D4
q1-q3): 1e11 individuals living one day, 1e-10 chance of an improvement per individual, gamma = 1e-6,
about 1e6 generations to 'most', 1e7 to 'almost all', 1e6 improvements in succession, so about 1e13
generations. Claim file D4 recomputes the deterministic logistic from p0 = 1e-10 and the time available
in Ulam's scheme (one billion years of one-day generations). Mayr (claim file D4b q1, q2): gamma is
unreasonably low (mutants often 30 percent better) and the improvements could go on simultaneously.
The record asserts Ulam's figures, the logistic times, the gap to the time available, and the same
model under Mayr's gamma and under simultaneity (Ulam's own 10 improvements per generation), side by side.

Run: research/.venv/bin/python -I docs/research/math/records/M-409.py [--write]
Without --write it checks that M-409.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D4, D4B = CL + "D4-ulam-sequential-improvements-10-to-13-generations.md", CL + "D4b-mayr-gamma-unreasonable-and-simultaneous.md"
D2A = CL + "D2a-day-ulam-sides-with-eden.md"


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
Q1 = held(D4, "Let us assume that we have 1011 individuals. Each lives one day and let us say that the chance of a favorable "
              "mutation or \"improvement\" is 10- 10 per individual.")
Q2 = held(D4, "let us say y is 10- 6 , it will take about 106 generations before most of the population is endowed with "
              "this improvement.")
Q3 = held(D4, "In 10 7 generations, say, almost all individuals will have it. Now, remember that we want not just one "
              "improvement but, say, 106 in succession. So we need about, say, 10 13 generations and not much more.")
AVAIL = held(D4, "Time available in the scheme: 'one billion years' x 365.25 = 3.65e11 one-day generations")
OPT = held(D2A, "In contrast to the tone of the discussion I, personally, believe that the numbers I took are very optimistic "
                "rather than the opposite.")
MAYR_G = held(D4B, "This gamma you chose is really quite unreasonable. Fisher and Wright also took extremely low gammas when "
                   "they started; but the recent work indicates that very often a mutant has a 30 percent advantage-in other "
                   "words, up to 70 percent advantage.")
MAYR_S = held(D4B, "DR. MAYR: Couldn't they all go on simultaneously? DR. ULAM: This is extremely unlikely. DR. MAYR: No, no. "
                   "DR. ULAM: Look, there will be only ten individuals which received an improvement in one generation.")
WALD = held(D4B, "DR. WALD: It is very good. You have exaggerated the difficulties, so your argument is going to be a minimum.")

M, alpha, gamma, n = 1e11, 1e-10, 1e-6, 1e6        # Ulam p.24 (claim file D4 q1-q3)
p0 = alpha                                         # claim file D4: 10 carriers in 1e11


def logistic(p_from, p_to, s):
    """Deterministic logistic sweep time in generations."""
    return (math.log(p_to / (1 - p_to)) - math.log(p_from / (1 - p_from))) / s


# ---- Ulam's figures -----------------------------------------------------------------------
near(M * alpha, 10, 1e-9)                          # 'only ten individuals which received an improvement'
near(1 / gamma, 1e6, 1e-6)                         # 'about 10^6 generations before most'
near(n * 1e7, 1e13, 1)                             # '10^13 generations'
avail = 1e9 * 365.25
near(avail, 3.65e11, 0.0025e11)
near(1e13 / avail, 27.4, 0.05)                     # Ulam's total is 27x the time available

# ---- logistic recomputation (claim file D4) -------------------------------------------------
t_half = logistic(p0, 0.5, gamma)
near(t_half, 2.30e7, 0.005e7)                      # ln(1e10)/gamma
t_99 = logistic(p0, 0.99, gamma)
near(t_99, 2.76e7, 0.005e7)
near(t_half / 1e6, 23.0, 0.05)                     # Ulam's '10^6 to most' is 23x short of the logistic
near(t_99 / 1e7, 2.76, 0.005)                      # '10^7 to almost all' is 2.8x short
T_serial = (n * t_half, n * t_99)
near(T_serial[0] / avail, 63.0, 0.1)               # claim file D4: 63x
near(T_serial[1] / avail, 75.6, 0.1)

# ---- Mayr: gamma = 0.3 ----------------------------------------------------------------------
t_mayr = logistic(p0, 0.5, 0.3)
near(t_mayr, 76.8, 0.05)                           # claim file D4b: 77 (76.8)
T_mayr = n * t_mayr
near(T_mayr, 7.68e7, 0.005e7)                      # 10^6 serial improvements at gamma 0.3
assert T_mayr < avail
near(avail / T_mayr, 4757, 5)

# ---- Mayr: simultaneous sweeps, Ulam's own supply of 10 improvements per generation ----------
arrival = n / (M * alpha)                          # generations for 1e6 improvements to arise at 10 per generation
near(arrival, 1e5, 1e-6)
T_par = arrival + t_99                             # deterministic, every arrival kept, as in Ulam's model
near(T_par, 2.77e7, 0.005e7)
assert T_par < avail
near(1e13 / T_par, 3.6e5, 0.05e5)                  # serial premise accounts for a factor of about 360,000

finish({
    "object": "M-409",
    "inputs": [
        {"name": "Ulam scheme", "value": {"M": M, "alpha_per_individual": alpha, "gamma": gamma, "improvements": n,
                                          "generation": "1 day"},
         "cite": "claim file D4 q1-q3 (Wistar p.24)"},
        {"name": "time available", "value": "one billion years x 365.25 one-day generations",
         "cite": "claim file D4 formal statement (Ulam's scheme)"},
        {"name": "Mayr gamma", "value": 0.3, "cite": "claim file D4b q1 (Wistar p.24 discussion)"},
        {"name": "Mayr simultaneity; Ulam 'only ten individuals'", "value": 10, "cite": "claim file D4b q2"},
        {"name": "Ulam: numbers 'very optimistic'; Wald: 'a minimum'", "cite": "claim file D2a (p.25); D4b q3"},
    ],
    "values": {
        "improvements_per_generation": 10, "ulam_total": 1e13, "available_generations": g(avail),
        "ulam_total_over_available": g(1e13 / avail),
        "logistic_to_half": g(t_half), "logistic_to_0.99": g(t_99),
        "serial_logistic_total": [g(T_serial[0]), g(T_serial[1])],
        "mayr_gamma_0.3": {"sweep": g(t_mayr), "serial_total": g(T_mayr)},
        "simultaneous_gamma_1e-6": {"arrival": g(arrival), "total": g(T_par)},
    },
    "positions": {
        "day": {"reading": "Ulam's serial calculation stands and no faster rate was computed",
                "ulam_total": 1e13, "serial_logistic_total": [g(T_serial[0]), g(T_serial[1])],
                "over_available": [g(1e13 / avail), g(T_serial[0] / avail)]},
        "critic": {"reading": "Mayr: gamma too low and improvements can run simultaneously",
                   "serial_at_gamma_0.3": g(T_mayr), "simultaneous_at_gamma_1e-6": g(T_par),
                   "note": "both fit inside the 3.65e11 available; the R4 D1 shared-pool result is a simulation, not "
                           "recomputed here"},
    },
    "notes": "Ulam's 10 improvements per generation, 1e6 and 1e13 reproduce; the deterministic logistic from p0 = 1e-10 "
             "gives 2.30e7 to half and 2.76e7 to 0.99, so his '10^6 to most' is 23x short while the total, 2.3-2.8e13, "
             "stays within 3x of 1e13 and is 27-76x the 3.65e11 one-day generations available. Under Mayr's gamma = "
             "0.3 the serial total is 7.7e7; under simultaneity with Ulam's own supply of 10 per generation it is "
             "about 2.8e7. Both fit. The serial premise and gamma carry the whole gap; neither is measured in the "
             "volume. Drift loss of new improvements (fixation about 2 gamma) is outside Ulam's model and not added.",
})
