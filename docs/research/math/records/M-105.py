#!/usr/bin/env python3
"""M-105 record (formula, derivation): sweep time (2/s) ln(2Ne s) at s = 1.5e-4 and the division by d = 0.80.

Object: docs/research/math/objects.yaml M-105 (formula, derivation). evo005@L58-L72 prints (2/s) ln(2Ne s) at s =
0.00015 for Ne = 1e4, 1e5, 1e6 as 14,648, 45,349 and 76,051 generations against the neutral 4Ne, and divides by d =
0.80: 14,648 -> 18,310 and 40,000 -> 50,000. The quoted Gemini table (s = 0.01, 0.001) is checked too. All printed
values reproduce except 76,051, which is 76,050.4 (0.57 high; the source map says 76,050.6). Two checks the post does not make: (a) 2Ne s = 3 at Ne = 1e4, so the
formula, an approximation for Ne s >> 1, is outside its domain there; (b) the Kimura-Ohta conditional mean fixation
time (diffusion, additive, Ne = N, one new copy), validated here against RESULTS B0.4's 8,480 at Ne = 1e4, s = 0.001,
is 28,898, 62,060 and 92,965 at s = 1.5e-4: the printed values are 2.0x, 1.4x and 1.2x too short, so the formula
understates the time on Day's own inputs (the opposite direction to M-601's (2/s) ln(2Ne), which overstates). Day's
L72 remark that the average over all fixations "gets even worse" holds: 0.875 x 40,000 + 0.125 x T(0.0012) = 35,662
(formula) or 35,922 (diffusion), both above 14,648. Whether dividing by d is the right overlap correction is M-013 and
M-107, not settled here. Numerical quadrature (composite Simpson, stdlib), well under a second.

Run: research/.venv/bin/python -I docs/research/math/records/M-105.py [--write]
Without --write it checks that M-105.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo005": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-005/body.txt",
       "evo006": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-006/body.txt"}
RESULTS = "research/checks/RESULTS.md"
PY = "docs/research/parameters.yaml"


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
D_D = post("evo005", "Incorporating d means the 14,648-generation fixation time at the empirical s for N_e = 10,000 "
                     "becomes roughly 18,310 generations.")                                             # evo005@LNone
ROW = held(SM + "evo005.md", "Reproduces: 14,648/0.80 = 18,310; table values at s = 0.00015 reproduce (14,648; 45,349; "
                             "76,050.6 stated 76,051); Gemini-table 1,060/1,520/1,980 reproduce.")
D_OVER = post("evo006", "The only innovation on my part is to provide the necessary time-weighted correction for "
                        "overlapping generations")                                                      # evo006@L44
if (ROOT / RAW["evo005"]).exists():                                   # table cells and L72 are in the body only
    for cell in ("14,648 generations", "45,349 generations", "76,051 generations", "1,060 generations",
                 "6,000 generations", "10,600 generations", "15,200 generations", "4,000,000 generations",
                 "The neutral baseline of 40,000 becomes 50,000.",
                 "And the weighted average across all fixations, where 87.5% are neutral, gets even worse.",
                 "which is still (2/s)·ln(2Ne·s) for the beneficial case and 4Ne for the neutral case"):
        held(RAW["evo005"], cell)
B04 = held(RESULTS, "| **10⁴ (Day's)** | **0.001** | **20** | — | **8,480** | **19,807** | 8,532 |")   # B0.4 diffusion row
held(PY, "Ne_modern_human: {value: 1.0e4")                            # population.Ne_modern_human

S_EMP, D = 1.5e-4, 0.80
sweep = lambda s, ne: (2 / s) * math.log(2 * ne * s)                  # Day's / Gemini's formula


def cond_fix_time(ne, s, n=20_000):
    """Kimura-Ohta (1969) mean time to fixation conditional on fixation, from p = 1/(2N), additive genic selection,
    M = s x(1 - x), V = x(1 - x)/(2N), N = Ne, S = 4Ns; integrands rewritten so that e^S never overflows."""
    S, p = 4 * ne * s, 1 / (2 * ne)
    den = -math.expm1(-S)
    f1 = lambda x: (4 * ne / S) * (-math.expm1(-S * x)) * (-math.expm1(-S * (1 - x))) / (x * (1 - x) * den)
    f2 = lambda x: (4 * ne / S) * (-math.expm1(-S * x)) * math.expm1(S * x) / (x * (1 - x) * den)

    def simpson(f, a, b, m):
        h = (b - a) / m
        return h / 3 * (f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, m)))
    edges = sorted({p, min(0.5, 20 / S), 0.5, max(0.5, 1 - 20 / S), 1 - 1e-15})   # resolve the 1/S boundary layers
    i1 = sum(simpson(f1, a, b, n) for a, b in zip(edges, edges[1:]))
    u = -math.expm1(-S * p) / den
    return i1 + (1 - u) / u * simpson(f2, 1e-300, p, 200)


# ---- the printed values ----------------------------------------------------------------------------------
t = {ne: sweep(S_EMP, ne) for ne in (10_000, 100_000, 1_000_000)}
near(t[10_000], 14_648, 0.5); near(t[100_000], 45_349, 0.5)
near(t[1_000_000], 76_050.43, 0.005)                                  # printed 76,051; the source-map row says 76,050.6
near(76_051 - t[1_000_000], 0.57, 0.005)                              # rounding slip of under one generation (R1: ledger size)
assert round(t[1_000_000]) == 76_050
gem = {(s, ne): sweep(s, ne) for s in (0.01, 0.001) for ne in (10_000, 100_000, 1_000_000)}
for (s, ne), printed, tol in (((0.01, 10_000), 1_060, 1), ((0.01, 100_000), 1_520, 1), ((0.01, 1_000_000), 1_980, 1),
                              ((0.001, 10_000), 6_000, 9), ((0.001, 100_000), 10_600, 4), ((0.001, 1_000_000), 15_200, 2)):
    near(gem[(s, ne)], printed, tol)                                   # the Gemini table, rounded
assert [4 * ne for ne in t] == [40_000, 400_000, 4_000_000]            # neutral baseline 4Ne
near(t[10_000] / D, 18_310, 0.5); assert 40_000 / D == 50_000          # division by d = 0.80
near(14_648 / D, 18_310, 1e-9)

# ---- domain and the conditional mean ----------------------------------------------------------------------
two_ne_s = {ne: 2 * ne * S_EMP for ne in t}
near(two_ne_s[10_000], 3, 1e-9); near(two_ne_s[100_000], 30, 1e-9); near(two_ne_s[1_000_000], 300, 1e-9)
near(cond_fix_time(10_000, 0.001), 8_480, 1)                          # validates the integral against B0.4
near(cond_fix_time(10_000, 1e-9), 40_000, 2)                          # neutral limit 4Ne
c = {ne: cond_fix_time(ne, S_EMP) for ne in t}
near(c[10_000], 28_898, 1); near(c[100_000], 62_060, 1); near(c[1_000_000], 92_965, 1)
assert abs(cond_fix_time(10_000, S_EMP, 40_000) - c[10_000]) < 0.1     # quadrature converged
ratio = {ne: c[ne] / t[ne] for ne in t}
near(ratio[10_000], 1.973, 1e-3); near(ratio[100_000], 1.368, 1e-3); near(ratio[1_000_000], 1.222, 1e-3)
asym = (2 / S_EMP) * (math.log(4 * 1_000_000 * S_EMP) + 0.5772156649)
near(asym, c[1_000_000], 25)                                          # (2/s)(ln 4Ns + gamma) where Ns >> 1
assert all(c[ne] < 4 * ne for ne in t)                                # still faster than neutral

# ---- Day's mixture remark (L72) ----------------------------------------------------------------------------
S_ADAPT = 0.0012                                                     # s+ (M-104)
t_ad, c_ad = sweep(S_ADAPT, 10_000), cond_fix_time(10_000, S_ADAPT)
near(t_ad, 5_296.76, 0.005); near(c_ad, 7_378, 1)
mix_formula, mix_diff = 0.875 * 40_000 + 0.125 * t_ad, 0.875 * 40_000 + 0.125 * c_ad
near(mix_formula, 35_662, 0.5); near(mix_diff, 35_922, 1)
assert mix_formula > t[10_000] and mix_diff > t[10_000]                # "gets even worse" holds

finish({
    "object": "M-105",
    "inputs": [
        {"name": "s", "value": S_EMP, "cite": "evo005@L55 (record M-104)"},
        {"name": "Ne", "value": [10_000, 100_000, 1_000_000], "cite": "evo005 table; parameters population.Ne_modern_human (1e4)"},
        {"name": "d", "value": D, "cite": "evo005@LNone; evo006@L44 (definition: record M-013)"},
        {"name": "diffusion check point", "value": {"Ne": 10_000, "s": 0.001, "T": 8_480}, "cite": "RESULTS B0.4 row (quoted in record M-601)"},
        {"name": "s+ for the mixture", "value": S_ADAPT, "cite": "evo005@L52 (record M-104)"},
    ],
    "values": {
        "sweep_formula": {str(ne): round(v, 1) for ne, v in t.items()},
        "divided_by_d": {"14648": 18_310, "40000": 50_000},
        "gemini_table": {f"{s}|{ne}": round(v, 1) for (s, ne), v in gem.items()},
        "two_Ne_s": {str(ne): round(v, 6) for ne, v in two_ne_s.items()},
        "conditional_mean_diffusion": {str(ne): round(v) for ne, v in c.items()},
        "diffusion_over_formula": {str(ne): round(v, 3) for ne, v in ratio.items()},
        "mixture_mean_time_Ne_1e4": {"formula": round(mix_formula), "diffusion": round(mix_diff),
                                     "adaptive_formula": round(t_ad, 1), "adaptive_diffusion": round(c_ad)},
    },
    "positions": {
        "day": {"reading": "(2/s) ln(2Ne s) at the empirical s gives 14,648-76,051 generations; d = 0.80 rescales to "
                           "18,310 and 50,000",
                "holds": "every printed value reproduces; the diffusion mean is longer still (28,898 at Ne = 1e4), so "
                         "the formula errs in the direction that helps the critics, not Day; the all-fixation average "
                         "is worse, as L72 says (35,662)"},
        "critic": {"reading": "Ne scaling already handles overlap (Hancock); dividing by d is open; the formula is "
                              "applied outside its domain",
                   "holds": "2Ne s = 3 at Ne = 1e4, where the large-Ne s formula is off by 2.0x; feeding a mixture "
                            "mean s into a sweep formula times an allele that does not exist (87.5% fix neutrally in "
                            "4Ne, 12.5% sweep in about 5,300-7,400); the d correction is M-013/M-107"},
    },
    "notes": "All printed arithmetic reproduces. The diffusion integral is the standard Kimura-Ohta conditional "
             "fixation time with Ne = N, from one new copy; it reproduces B0.4's 8,480 and the neutral 4Ne, and "
             "matches the (2/s)(ln 4Ns + gamma) asymptote within 24 generations at Ne = 1e6. It shows the printed "
             "(2/s) ln(2Ne s) values understate the conditional mean by 1.2-2.0x at s = 1.5e-4. This does not move "
             "Day's direction: the times are longer, not shorter. The division by d is recorded as arithmetic only.",
})
