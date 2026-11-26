#!/usr/bin/env python3
"""M-126 record (model-choice, derivation): gene flow as "a structural hindrance to the pace of fixation".

Object: docs/research/math/objects.yaml M-126 (model-choice, derivation). gene-flow@L3 (Day): gene flow "is a
structural hindrance to the pace of fixation by both natural selection and neutral substitution"; L6: it "redistributes
alleles that already exist"; L7: within a structured species migrants must carry a drifting allele between demes, so
"limited gene flow adds an extra stage to the journey and makes fixation slower", and between diverging lineages it
"erases differences". The post gives no transit-time formula; above L7 nothing names demes, a stage or slower fixation
(L5 names only "drift's transit time"), so "as discussed above" has no held antecedent. Quoted, not tested.
Two readings of "pace", recorded both ways:
- rate (substitutions per generation over a window, the reading M-115 settles for MITTENS): for neutral sites Day's own
  Hard Limits paper states Maruyama invariance (B7 q1): under conservative migration the neutral rate is exactly mu and
  P_fix exactly 1/(2N). Record M-209 gives k/mu = 1; not recomputed. On this reading structure does not slow neutral
  substitution, on Day's own cited principle.
- latency (generations one fixation takes): Day's extra-stage claim. No held text gives a structured-population
  fixation time, neutral or selected (gaps ledger K9 lists Day's Z18167588 as citing Whitlock & Barton and Maruyama; its
  text is not quoted in any held file). A latency does not bound a window count once fixations overlap (M-115), but from
  an empty start the count loses about one mean fixation time (M-201: mu L (T - 4 Ne)), so a longer transit would cut an
  empty-start count. Not derived here (no transit-time formula).
Between lineages: gene flow after the split is "low materiality" and changes no verdict direction (gaps ledger K4).
LTEE: each population is serially transferred as one population (Q312, Day's MITTENS 3.0; generations_per_day 6.64 =
log2(100)) and the twelve evolved "independently" (Day, Z23020792; branch-E E q1): no demes and no migration between
flasks, so the measured G_f carries neither gene flow nor its hindrance. Within a flask there is clonal lineage structure
(E9: two coexisting lineages in nine of twelve; Day s5.2: "permanently competing sub-populations"), which is not demic
structure. Whether the LTEE rate transfers to humans at all is M-115's transfer question (M-103, M-006), not settled here.
No verdict (F).

Run: research/.venv/bin/python -I docs/research/math/records/M-126.py [--write]
Without --write it checks that M-126.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"gene-flow": "sources/raw/refresh-2026-11-08/p-neutral-drift-and-gene-flow/body.txt"}
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"
QD = "docs/research/sources/quotes-day.md"
GAPS = "docs/research/ledgers/gaps.md"


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


def raw(src, quote):
    """A sentence from the held post body that the source map does not copy; checked when sources/raw is present."""
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


# ---- Day's position (gene-flow post, 2026-11-08) ------------------------------------------------------------------------
HIND = post("gene-flow", "gene flow not only doesn’t help, it is a structural hindrance to the pace of fixation by both "
                         "natural selection and neutral substitution.")                          # gene-flow@L3
REDIS = raw("gene-flow", "It doesn’t create new alleles and doesn’t fix them. It redistributes alleles that already "
                         "exist.")                                                               # L6
DEMES = raw("gene-flow", "Within a structured species, gene flow is what lets drift produce a species-wide substitution "
                         "at all. An allele drifting upward in one deme needs migrants to carry it into the others.")  # L7
STAGE = raw("gene-flow", "That’s why limited gene flow adds an extra stage to the journey and makes fixation slower, as "
                         "discussed above.")                                                     # L7
ERASE = raw("gene-flow", "Between diverging lineages, gene flow works directly against substitution-driven divergence. "
                         "It mixes the two gene pools back together and erases differences.")    # L7
TRANSIT = raw("gene-flow", "That’s why the Hard Limit treats the two together: the transit time is drift’s transit time, "
                           "and a substitution is a mutation that completed the journey.")       # L5, the "above"
held(SM + "gene-flow.md", "n/a (qualitative; no transit-time formula given)")
if (ROOT / RAW["gene-flow"]).exists():
    body = (ROOT / RAW["gene-flow"]).read_text(encoding="utf-8").splitlines()
    above = " ".join(body[1:6]).lower()                                    # L2-L6, before the L7 claim
    assert "deme" not in above and "slow" not in above and "stage" not in above  # "above" has no extra-stage passage
    assert not any(c in " ".join(body[1:7]) for c in "=≈×")               # no formula anywhere in L2-L7

# ---- neutral case: rate, on Day's own cited principle (cited, not recomputed) -------------------------------------------
MARU = held(CL + "B7-neutral-fixation-probability-is-1-over-2n.md",
            "Maruyama’s invariance principle (1970, 1974) holds that under conservative migration the neutral "
            "substitution rate is exactly μ and the neutral fixation probability exactly 1/(2N)")  # B7 q1, Z22129121
held(CL + "B7-neutral-fixation-probability-is-1-over-2n.md", "external: supported")
k_mu = cited("M-209", "k_over_mu_cancelled")
assert set(k_mu.values()) == {1}                                           # k = mu for every held N, Ne pair

# ---- rate vs latency, and the empty start (cited) --------------------------------------------------------------------------
assert cited("M-115", "seconds_per_car") == 10 and cited("M-115", "bunched_average") == 10  # a window count is a rate
held("docs/research/math/objects.yaml", "MITTENS is a rate calculation, not a latency calculation")  # M-115 day
EMPTY = held("docs/research/math/objects.yaml", "E[F(T)] = mu L int_0^T F_X(u) du ~ mu L (T - 4 Ne)")  # M-201

# ---- selected case: what is held ----------------------------------------------------------------------------------------------
K9 = held(GAPS, "| Population structure, overlapping generations, sweepstakes (K9) | Addressed by Day and the audit. | "
                "Day: Z18167588 (Whitlock & Barton; Maruyama)")
selected_structured_fixation_time_held = False   # no claim file, quotes file or R4 result quotes one (grep 2026-11-26)

# ---- between lineages ---------------------------------------------------------------------------------------------------------
K4 = held(GAPS, "| Gene flow after the split (K4) | Addressed in passing on both sides, and low materiality.")
held(GAPS, "It adds a parameter to B4a but does not change any verdict direction.")

# ---- LTEE: isolated, serially transferred populations ------------------------------------------------------------------------
TRANSFER = held(QD, "Each population is transferred daily into fresh minimal glucose medium with a 1:100 dilution, "
                    "yielding approximately 6.64 generations per day and an effective population size (Ne) of "
                    "approximately 3 × 10⁷.")                                                  # Q312, Z23003785 s1
INDEP = held(SM + "branch-E.md", "Six of the twelve populations independently evolved hypermutator phenotypes")  # E q1
held(PY, "generations_per_day: {value: 6.64, source: standard (log2 of the 100-fold daily dilution)")
near(math.log2(100), 6.64, 0.005)                                         # 6.644: regrowth from a 1:100 dilution
CLONES = held(CL + "E9-good2017-dynamics.md", "two coexisting lineages in nine of twelve populations")
SUBPOP = held("research/checks/e5_external.py", "The population fragmented into permanently competing")  # Day s5.2

finish({
    "object": "M-126",
    "inputs": [
        {"name": "Day's claim", "value": "structural hindrance to the pace of fixation", "cite": "gene-flow@L3, L6, L7"},
        {"name": "Maruyama invariance (Day's own Hard Limits)", "value": "k = mu, P_fix = 1/(2N) under conservative "
         "migration", "cite": "B7 q1 (Z22129121); record M-209"},
        {"name": "rate vs latency; empty-start loss", "cite": "records M-115, M-201"},
        {"name": "structured fixation times, selected", "value": "not held", "cite": "gaps ledger K9 (Z18167588 cited, "
         "text not quoted in held files)"},
        {"name": "gene flow after the split", "value": "low materiality", "cite": "gaps ledger K4"},
        {"name": "LTEE regime", "value": "12 populations, each transferred daily at 1:100, evolved independently",
         "cite": "Q312 (Z23003785 s1); branch-E E q1 (Z23020792); parameters ltee.generations_per_day; E9; Day s5.2"},
    ],
    "values": {
        "transit_time_formula_in_post": False,
        "neutral_rate_over_mu_under_conservative_migration": 1,
        "neutral_rate_slowed_by_structure_on_days_cited_principle": False,
        "structured_fixation_time_neutral_held": False,
        "structured_fixation_time_selected_held": selected_structured_fixation_time_held,
        "ltee_demes_per_population": 1,
        "ltee_migration_between_populations": False,
        "ltee_clonal_lineage_structure_within_flasks": True,
        "log2_100": round(math.log2(100), 3),
    },
    "positions": {
        "day": {"reading": "gene flow only redistributes alleles; in a structured species a species-wide substitution "
                           "waits on migrants (an extra stage, slower fixation), and between lineages gene flow erases "
                           "differences, so it cannot help close the accounting gap",
                "holds": "gene flow creates and fixes no allele, so it adds no substitutions to the count; between "
                         "lineages it works against divergence (direction agreed; K4: low materiality); if structure "
                         "lengthens transit, an empty-start count loses more (M-201); the LTEE flasks have no gene flow, "
                         "so its G_f carries no such stage"},
        "critic": {"reading": "pace is a rate over a window (M-115); structure changes latency, not the neutral rate",
                   "holds": "Day's own Hard Limits paper states Maruyama invariance: under conservative migration the "
                            "neutral rate is exactly mu (M-209: k/mu = 1), so structure does not slow neutral "
                            "substitution as a rate; the post gives no transit time and none is held for selected "
                            "alleles; the LTEE comparison turns on transfer (M-103, M-006), not on gene flow"},
    },
    "notes": "Model choice, qualitative. Both readings of 'pace' are recorded; no structured-population transit time is "
             "derived (brief: not in scope) and none is held, so the latency claim is quoted, not tested. Selected-case "
             "fixation times in subdivided populations would need Z18167588's Whitlock & Barton passage or a primary "
             "source; neither is quoted in held files.",
})
