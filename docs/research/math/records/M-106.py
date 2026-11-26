#!/usr/bin/env python3
"""M-106 record (formula, derivation): throughput ceiling sum(s_i) <= s_max, sum = n x s-bar, and the DFE shape.

Object: docs/research/math/objects.yaml M-106 (formula, derivation). evo007@L25-L27: throughput depends on the total
selection budget sum(s_i) <= s_max, not on the distribution of s; the sum is n x s-bar, so the mean suffices. The
post gives no worked example, so the record uses constructed DFEs with the same budget and cites M-808 for the Term 3
rate K_sel = s_max d / [2 ln(2Ne)] (there s-bar cancels for one common s). Three results. (1) sum = n x s-bar is an
identity. (2) Under M-808's sweep time tau_i = (2/(s_i d)) ln(2Ne), each sweep's rate 1/tau_i is linear in s_i, so the
throughput sum(1/tau_i) = d sum(s_i)/(2 ln 2Ne) is the same for every DFE with the same sum: the shape cancels
exactly, as Day says. (3) It cancels only because tau is proportional to 1/s. Under evo005's own form (2/s) ln(2Ne s)
the log carries s, and two DFEs with the same sum differ (a 0.0005/0.0015 split runs 1.4% slower than all-0.001 at
Ne = 1e4). On the supply side, Kimura's P(fix) (quoted by Day, evo007@L21) at a fixed mean s depends on the shape: a
DFE of +0.003/-0.001 (mean 0.001) fixes 1.50x as many new mutations as all-0.001. That is Hancock's point; it bears on
whether the budget is filled, not on the ceiling. Whether a fixed s_max exists is not derived in the post (H8 q3,
M-808). Closed forms (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-106.py [--write]
Without --write it checks that M-106.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo007": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-007/body.txt"}
H8 = "docs/research/claims/H8-kimura-calculator-term3.md"
PY = "docs/research/parameters.yaml"
REC = "docs/research/math/records/"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def post(src, quote):
    """A source-map quote (committed), re-checked against the held post body when sources/raw is in this checkout."""
    held(SM + src + ".md", quote)
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def cited(rec, key):
    """A value from a settled record's JSON (cited, not recomputed)."""
    return json.loads((ROOT / REC / f"{rec}.json").read_text(encoding="utf-8"))["values"][key]


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


# ---- the source sentences ------------------------------------------------------------------------------
BUDGET = post("evo007", "the throughput depends on the total selection budget (Σs_i ≤ s_max), not on the individual "
                        "distribution of s values. The s̄ cancels.")                                    # evo007@L25
SUM = post("evo007", "the mean is the correct summary statistic, because what matters is the sum of selection "
                     "coefficients across concurrent sweeps, and the sum is just n × s̄")              # evo007@L27
KIMURA = post("evo007", "P(fix) = (1 – e^(-2s)) / (1 – e^(-4Ns))")                                     # evo007@L21
IMPL = held(SM + "evo007.md", "P (implicit): a fixed s_max exists.")
H8_FORM = held(H8, "n_max = s_max / s̄ concurrent sweeps (sum of s_i <= s_max)")
H8_Q3 = held(H8, "None of them raises smax above order unity, and the reason is the same in all three cases.")
held(PY, "Ne_modern_human: {value: 1.0e4")                            # population.Ne_modern_human
held(PY, "turnover_d: {value: 0.45")                                 # selection.turnover_d

# ---- (1) the identity sum = n x s-bar (exact) ----------------------------------------------------------
DFES = {                                                             # constructed: n = 4 sweeps, same budget 0.004
    "point": [Fr(1, 1000)] * 4,
    "two_point": [Fr(1, 2000), Fr(1, 2000), Fr(3, 2000), Fr(3, 2000)],
    "skewed": [Fr(1, 4000), Fr(1, 4000), Fr(1, 4000), Fr(13, 4000)],
}
for v in DFES.values():
    n, s_bar = len(v), sum(v) / len(v)
    assert sum(v) == n * s_bar == Fr(4, 1000)                         # identity; same budget in every DFE

# ---- (2) M-808's sweep time: the shape cancels exactly -----------------------------------------------------
D, NE = Fr(45, 100), 10_000
LN = math.log(2 * NE)
rate_808 = lambda v: sum(float(s * D) / (2 * LN) for s in v)         # sum of 1/tau_i, tau_i = (2/(s_i d)) ln(2Ne)
r808 = {k: rate_808(v) for k, v in DFES.items()}
assert max(r808.values()) - min(r808.values()) < 1e-18                # identical for every shape
near(r808["point"], float(Fr(4, 1000) * D) / (2 * LN), 1e-18)        # = d sum(s_i) / (2 ln 2Ne), M-808's form
near(cited("M-808", "ln_2Ne"), math.log(6_600), 5e-5)                  # M-808's Ne = 3,300 (cited, not rerun)

# ---- (3a) evo005's form (2/s) ln(2Ne s): the shape does not cancel ------------------------------------------
rate_005 = lambda v: sum(float(s) / (2 * math.log(2 * NE * float(s))) for s in v)  # needs 2Ne s > 1
assert all(2 * NE * s > 1 for v in DFES.values() for s in v)
r005 = {k: rate_005(v) for k, v in DFES.items()}
near(r005["two_point"] / r005["point"], 0.9858, 5e-5)                 # 1.4% slower at the same budget
near(r005["skewed"] / r005["point"], 0.9321, 5e-5)                    # 6.8% slower
# ---- (3b) supply side: Kimura P(fix) at a fixed mean s --------------------------------------------------------
pfix = lambda s, n: -math.expm1(-2 * s) / -math.expm1(-4 * n * s)
SUPPLY = {"point": [0.001, 0.001], "two_point": [0.0005, 0.0015], "pos_neg": [0.003, -0.001]}
assert all(abs(sum(v) / 2 - 0.001) < 1e-15 for v in SUPPLY.values())  # every DFE has mean s = 0.001
mp = {k: sum(pfix(s, NE) for s in v) / 2 for k, v in SUPPLY.items()}
near(mp["point"], 0.0019980, 5e-7)                                   # about 2s
near(mp["pos_neg"] / mp["point"], 1.497, 5e-4)                       # shape changes the fixation supply
near(mp["two_point"] / mp["point"], 1.0, 5e-3)                       # nearly linear while every s > 0

finish({
    "object": "M-106",
    "inputs": [
        {"name": "budget rule", "value": "sum(s_i) <= s_max; sum = n x s-bar", "cite": "evo007@L25, @L27; H8 formal statement"},
        {"name": "sweep time (Term 3)", "value": "tau = (2/(s d)) ln(2Ne)", "cite": "record M-808 (H8)"},
        {"name": "sweep time (evo005)", "value": "(2/s) ln(2Ne s)", "cite": "evo005@L15 (record M-105)"},
        {"name": "fixation probability", "value": "(1 - e^(-2s)) / (1 - e^(-4Ns))", "cite": "evo007@L21"},
        {"name": "d, Ne", "value": [0.45, NE], "cite": "parameters selection.turnover_d, population.Ne_modern_human"},
        {"name": "DFEs", "value": {k: [str(s) for s in v] for k, v in DFES.items()} | {"supply": SUPPLY},
         "cite": "constructed test points (the post gives no example)"},
    ],
    "values": {
        "term3_throughput_per_generation": {k: f"{v:.6e}" for k, v in r808.items()},
        "term3_shape_cancels": True,
        "evo005_form_ratio_to_point": {k: round(v / r005["point"], 4) for k, v in r005.items()},
        "mean_pfix_at_mean_s_0.001": {k: f"{v:.6e}" for k, v in mp.items()},
        "pfix_ratio_to_point": {k: round(v / mp["point"], 4) for k, v in mp.items()},
    },
    "positions": {
        "day": {"reading": "the mean is the right statistic for a throughput ceiling; the DFE shape drops out",
                "holds": "exactly, under the Term 3 sweep time (tau proportional to 1/s): every DFE with the same "
                         "sum(s_i) gives the same throughput, and sum = n x s-bar is an identity"},
        "critic": {"reading": "each mutation has its own fixation probability; s_max is not derived",
                   "holds": "the cancellation needs tau proportional to 1/s (under (2/s) ln(2Ne s) the shape shifts the "
                            "rate 1.4-6.8% in the test DFEs), and at a fixed mean s the shape moves the supply of "
                            "fixations 1.50x (P(fix), evo007@L21). The post asserts a fixed s_max (implicit premise); "
                            "it is not derived there"},
    },
    "notes": "Derivation on constructed DFEs; the post has no numeric example. The ceiling statement (given a budget, "
             "throughput is set by the budget) holds exactly under M-808's sweep time and approximately under evo005's. "
             "The critic's point concerns a different quantity: how many new mutations fix (supply), which depends on "
             "the DFE shape at a fixed mean. Whether s_max of order unity exists is H8's question (M-808, H8 q3), "
             "not settled here.",
})
