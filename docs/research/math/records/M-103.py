#!/usr/bin/env python3
"""M-103 record (model-choice, derivation): does the LTEE generations-per-fixation transfer to humans.

Object: docs/research/math/objects.yaml M-103 (model-choice, derivation). The LTEE starts clonal, has no recombination
and no standing variation. Day (evo005): standing variation shortens only the wait for a beneficial allele, "it cannot
reduce the fixation time once selection begins acting on it"; the LTEE is a worst case for mutation supply; correcting
for it makes humans worse; Lynch (relayed) says prokaryotes adapt more efficiently. Critics: the clonal, nonrecombining
start makes the comparison inapt (A5f RE-07, GA-01; A5 McCarthy). The record settles one new piece of arithmetic and
cites the rest. New: under the deterministic sweep M-601 uses (dp/dt = s p(1 - p)), the time from p0 to 1 - 1/(2Ne)
is (1/s)[ln((1 - p0)/p0) + ln(2Ne - 1)]; against a new mutation (p0 = 1/(2Ne)) standing variation at p0 = 0.01, 0.05
and 0.5 cuts it by 26.8%, 35.1% and 50.0% at Ne = 1e4, whatever s is. So "cannot reduce" fails as literally stated,
and the cut is bounded by a factor of two (p0 <= 0.5), which is Day's larger point. Cited, not recomputed: the supply
ratio kappa = 93,659 and the no-transfer count 191 (M-006, M-007; A2e), the recombination factor 1.5-172x
(extrapolated, R4 F2) and the Weissman-Barton asymptote 17.5-19 per generation (R4 GAP-04), both from claim file A2e.
Closed forms (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-103.py [--write]
Without --write it checks that M-103.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo005": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-005/body.txt"}
CL = "docs/research/claims/"
A2E = CL + "A2e-ltee-as-ceiling.md"
A5F = CL + "A5f-clonal-lineage-vs-recombining.md"
BRA = SM + "branch-A.md"
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
D_FASTER = post("evo005", "arguing that humans and chimpanzees can fixate mutations across their entire populations in "
                          "the wild faster than bacteria can in the long-term Lenski experiment")       # evo005@L2
D_SV = post("evo005", "Standing variation can reduce the waiting time for a beneficial allele to appear, since one "
                      "might already be segregating at low frequency. But it cannot reduce the fixation time once "
                      "selection begins acting on it")                                                  # evo005@L15
D_WORST = post("evo005", "the critics are correct that it captures a worst-case scenario")              # evo005@L16
D_LYNCH = post("evo005", "Prokaryotes appear to be much more efficient than eukaryotes at promoting simple to "
                         "moderately complex molecular adaptations.")                                  # evo005@L74, relay
D_SUM = post("evo005", "In sum, humans do not fixate faster than bacteria, measured in time or in generations")  # @L70
C_RE07 = held(A5F, "It follows largely nonrecombining bacteria descended from one clone, repeatedly transferred into "
                   "the same glucose-limited environment.")                                             # A5f q1
C_GA01 = held(A5F, "Fixation rate in single cell organism is not equal to fixation rate in mammal. And there is two "
                   "reasons for it. One is sexual reproduction. The second is variability of population size.")  # A5f q2
C_MC07 = held(BRA, "As clear, the expected rate of fixed mutations has to be determined according to the particular "
                   "circumstances of the population in question—its genome size, mutation rate, etc.")  # A5 q2
F2 = held(A2E, "free recombination would raise the rate 1.5-172x at the calibrated supply, but that factor is an "
               "EXTRAPOLATION of F2's R_int ~ 1 beyond its tested range (<= 272 active loci), not a simulation.")
F2_DAY = held(A2E, "Credit to Day: sublinearity and real interference under linkage are borne out")
WB = held(A2E, "in a recombining genome the adaptive-substitution asymptote is R/2 per generation (R/4 for an "
               "exponential DFE), independent of N and s; at R = 35-38 M that is 17.5-19 per generation")
WB_DOM = held(A2E, "The clonal LTEE is outside W&B's domain (they require R >> s), so W&B do not supply a transfer "
                   "factor from G_f")
held(PY, "Ne_modern_human: {value: 1.0e4")                            # population.Ne_modern_human
held(PY, "human_w_b_regime: {value: 36.8")                            # genetic_map_morgans.human_w_b_regime

# ---- new: standing variation and the deterministic sweep time (M-601's model) ------------------------------
NE = 10_000


def sweep_from(p0, ne=NE):
    """(time from p0 to 1 - 1/(2Ne)) x s under dp/dt = s p (1 - p); s cancels from every ratio."""
    return math.log((1 - p0) / p0) + math.log(2 * ne - 1)


new = sweep_from(1 / (2 * NE))
near(new, 2 * math.log(2 * NE - 1), 1e-12)                          # = (2/s) ln(2Ne - 1) x s, M-601's form
near(new / 0.001, cited("M-601", "sweep_time")["0.001"], 0.5)          # 19,807 at s = 0.001 (M-601)
cut = {p0: 1 - sweep_from(p0) / new for p0 in (0.01, 0.05, 0.5)}
near(cut[0.01], 0.268, 5e-4); near(cut[0.05], 0.351, 5e-4)
near(cut[0.5], 0.5, 1e-4)                                            # the ceiling of the cut: a factor of two
assert all(sweep_from(p) < new for p in (0.001, 0.01, 0.05, 0.5))    # any p0 > 1/(2Ne) is faster
assert all(sweep_from(p) >= new / 2 - 1e-9 for p in (0.01, 0.05, 0.25, 0.5))  # never below half for p0 <= 0.5
gens = {p0: round(19_807 * (1 - c)) for p0, c in cut.items()}          # at s = 0.001, Ne = 1e4 (M-601 base)

# ---- cited: supply, recombination and the no-transfer count -------------------------------------------------
kappa = near(cited("M-006", "kappa"), 93_658.5, 0.5)                  # human/LTEE genome-wide supply ratio (A2e)
f_none = cited("M-006", "F_no_scaling")
assert f_none == 191                                                  # 252,000 / 1,322 with no transfer factor
wb_lo, wb_hi = 35 / 2, 38 / 2
assert (wb_lo, wb_hi) == (17.5, 19.0)                                 # R/2 at R = 35-38 Morgans (GAP-04, quoted)
near(36.8 / 2, 18.4, 1e-12)                                           # at the parameters map length
near(wb_lo / (1 / 1_322), 23_135, 1)                                  # the asymptote per generation over 1/G_f

finish({
    "object": "M-103",
    "inputs": [
        {"name": "Ne", "value": NE, "cite": "parameters population.Ne_modern_human"},
        {"name": "sweep model", "value": "dp/dt = s p (1 - p); time p0 -> 1 - 1/(2Ne)", "cite": "record M-601 (same model)"},
        {"name": "standing-variation start frequencies", "value": [0.01, 0.05, 0.5], "cite": "constructed test points; evo005@L15 'segregating at low frequency'"},
        {"name": "supply ratio, no-transfer count", "value": {"kappa": kappa, "F_no_scaling": f_none}, "cite": "records M-006, M-007 (A2e)"},
        {"name": "recombination", "value": {"F2_factor": "1.5-172x (extrapolated)", "W&B_asymptote_per_gen": [wb_lo, wb_hi]},
         "cite": "claim file A2e: R4 F2, R4 GAP-04 (quoted, not rerun)"},
    ],
    "values": {
        "sweep_cut_vs_new_mutation": {str(k): round(v, 4) for k, v in cut.items()},
        "sweep_time_at_s_0.001_generations": {"new_mutation": 19_807, **{str(k): v for k, v in gens.items()}},
        "max_cut": 0.5,
        "kappa": kappa, "F_no_scaling": f_none,
        "WB_asymptote_per_generation": [wb_lo, wb_hi],
        "WB_over_LTEE_rate": round(wb_lo * 1_322),
    },
    "positions": {
        "day": {"reading": "standing variation shortens only the wait; recombination cannot close the gap; the LTEE is "
                           "a worst case for supply only, and s and Ne are worse in humans",
                "holds": "the cut from standing variation is bounded by a factor of two (p0 <= 0.5), small against the "
                         "shortfalls; the LTEE does under-supply mutations (kappa 93,659, a concession Day makes at "
                         "L16); interference under linkage is real (A2e, R4 F2 credit)"},
        "critic": {"reading": "a clonal, nonrecombining, zero-polymorphism start makes the LTEE rate inapt for humans",
                   "holds": "'cannot reduce the fixation time once selection begins' is false as stated: 26.8% at p0 = "
                            "0.01, 35.1% at 0.05; the LTEE ceiling holds only under a stated transfer factor (M-006), "
                            "and the recombining asymptote (17.5-19 per generation, W&B) is set by map length, not by "
                            "the clonal rate, though the clonal LTEE is outside W&B's domain"},
    },
    "notes": "Model-choice: no single number settles transfer. New arithmetic: the standing-variation cut, exact under "
             "M-601's deterministic sweep (s cancels in the ratio; stochastic establishment and the prior neutral "
             "phase are not modelled). The other numbers are cited from M-006 and claim file A2e. Day's 'roughly "
             "30,000 times slower in real time' (evo005@L16) and the Lynch relay are not checked: the population sizes "
             "behind the first are not stated and the Lynch book is not held. Whether critics hold that humans fixate "
             "faster than bacteria per generation (evo005@L2) is a fidelity question for the claim files.",
})
