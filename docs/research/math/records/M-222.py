#!/usr/bin/env python3
"""M-222 record (inference): extinction "within centuries" if drift fixed at the maximum neutral speed.

Object: docs/research/math/objects.yaml M-222 (inference, derivation). Q104 with its two premises.
Reading A (R4 B9, charitable: relaxed selection, mutation load): W_t = (1 - d)^t per generation,
25 y per generation, d = U x f x s; the record recomputes years to W = 0.5 and W = 0.1 at Lynch's
anchors (0.5%, 1%, 5%) and under Day's premise 2 (f = 0.75, U 76.8-100, s assumed 0.1%). Reading B
(literal "substitutions"): a harmful allele drifting like a neutral one needs ~4 Ne generations to fix,
and under selection its fixation probability is Kimura's u(s), far below 1/(2N) (claim file B9).
Both readings are computed and neither is chosen. Inputs carry their quote id, claim file or result
file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-222.py [--write]
Without --write it checks that M-222.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"
RB9 = "research/checks/results/R4-B9.md"


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


def years_to(w, d, gen=25):
    return math.log(w) / math.log(1 - d) * gen


def kimura_u(s, ne, n):
    """Fixation probability of a new mutant, initial frequency 1/(2N) (Kimura 1962)."""
    p = 1 / (2 * n)
    return (1 - math.exp(-4 * ne * s * p)) / (1 - math.exp(-4 * ne * s))


# ---- inputs -------------------------------------------------------------------------------
Q104 = held(QD, "So if genetic drift were capable of producing actual changes to the genome, the human species would "
                "have been rendered infertile and gone extinct within centuries.")
P1 = held(QD, "1. For neutral substitution to work to fixation at its maximum speed, natural selection cannot be operating.")
P2 = held(QD, "2. There are 3x more harmful substitutions than neutral substitutions.")
LYNCH = held(RB9, "Lynch's inputs: \"∼100×0.01×1%=1% per generation\"; \"as high as 5% per generation\"; for mice, "
                  "\"Extrapolating by dividing by 6.7 suggests a human decline rate of ∼0.5%\"")
CRIT = held(RB9, "Pre-registered operational criterion: \"centuries\" means 100-999 y.")
U_B9 = held(CL + "B9-drift-would-cause-extinction-within-centuries.md", "N_e = 1e4, s = -0.001: 4N_e s = -40, u = 8.5e-21 against 1/(2N) = 5e-5")
PY_TAK = held(PY, "takahata_1995: {value: 1.0e4")
PY_PM = held(PY, "humans: [1.31e4, 1.62e4]")

# ---- reading A: relaxed selection, W_t = (1 - d)^t ----------------------------------------------
lynch = {d: (years_to(0.5, d), years_to(0.1, d)) for d in (0.005, 0.01, 0.05)}
near(lynch[0.005][0], 3_457, 1); near(lynch[0.005][1], 11_484, 1)
near(lynch[0.01][0], 1_724, 1); near(lynch[0.01][1], 5_728, 1)
near(lynch[0.05][0], 338, 1); near(lynch[0.05][1], 1_122, 1)
assert 100 <= lynch[0.05][0] <= 999                     # only Lynch's upper value is inside "centuries"
assert lynch[0.01][0] > 999 and lynch[0.005][0] > 999   # central and mouse values: millennia
f = 0.75                                                 # premise 2: 3 harmful per neutral
dprem = {U: U * f * 0.001 for U in (76.8, 100)}         # s = 0.1% assumed (R4 B9 'Day premise 2' row)
near(dprem[76.8], 0.0576, 1e-9); near(dprem[100], 0.075, 1e-9)
prem_years = {U: years_to(0.5, d) for U, d in dprem.items()}
near(prem_years[76.8], 292, 1)
near(prem_years[100], 222, 1)
assert all(100 <= y <= 999 for y in prem_years.values())

# ---- reading B: literal "substitutions" ------------------------------------------------------------
fix_years = {ne: 4 * ne * 25 for ne in (1.0e4, 1.62e4)}
assert fix_years == {1.0e4: 1.0e6, 1.62e4: 1.62e6}      # 1.0-1.62 million years to fix one neutral-like allele
near(fix_years[1.0e4] / 999, 1_001, 1)                   # ~1,000x the top of "centuries"
u = kimura_u(-0.001, 1e4, 1e4)
near(u, 8.5e-21, 0.05e-21)
near(1 / (2 * 1e4), 5e-5, 1e-18)
near(math.log10(5e-5 / u), 15.77, 0.01)                  # harmful s = -0.001 fixes 6e15x less often than neutral

finish({
    "object": "M-222",
    "inputs": [
        {"name": "Day reductio and premises", "cite": "Q104 (B9 q1); premises in the same comment (quotes-day Q104 note)"},
        {"name": "Lynch anchors d", "value": [0.005, 0.01, 0.05], "cite": "R4-B9.md readings (Lynch 2016)"},
        {"name": "criterion 'centuries'", "value": "100-999 y", "cite": "R4-B9.md (owner rule 2026-10-11)"},
        {"name": "premise 2 inputs", "value": {"f": f, "U": [76.8, 100], "s": "0.001 assumed"}, "cite": "R4-B9.md results table"},
        {"name": "Ne", "value": [1.0e4, 1.62e4], "cite": "parameters population.Ne_histories.takahata_1995, prado_martinez_2013_table1.humans"},
        {"name": "Kimura u(s)", "value": "Ne 1e4, s -0.001", "cite": "claim file B9"},
    ],
    "values": {
        "lynch_years_W0.5_W0.1": {str(k): [g(a), g(b)] for k, (a, b) in lynch.items()},
        "premise2_d": {str(k): g(v) for k, v in dprem.items()},
        "premise2_years_W0.5": {str(k): g(v) for k, v in prem_years.items()},
        "neutral_like_fix_years": {str(k): v for k, v in fix_years.items()},
        "kimura_u_s-0.001": g(u),
    },
    "positions": {
        "day": {"reading": "A: with selection off, load accumulates within centuries",
                "years_to_half_fitness": {"lynch_5pct": g(lynch[0.05][0]), "premise2_s0.1pct": [g(prem_years[100]), g(prem_years[76.8])]}},
        "critic": {"reading": "the premise (all selection off at once) is counterfactual and the 3x ratio is an input",
                   "years_to_half_fitness_lynch_central_mouse": [g(lynch[0.01][0]), g(lynch[0.005][0])],
                   "literal_substitution_years": [1.0e6, 1.62e6], "kimura_u_harmful": g(u)},
    },
    "notes": "Every R4 B9 cell reproduces. Reading A: centuries on Lynch's upper value (338 y) and on Day's premise 2 "
             "with an assumed s (222-292 y); millennia on Lynch's central and mouse values (1,724-3,457 y). Reading B: "
             "a harmful allele drifting like a neutral one needs 1.0-1.6 My to fix, and with s = -0.001 it fixes with "
             "probability 8.5e-21, not 5e-5.",
})
