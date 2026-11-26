#!/usr/bin/env python3
"""M-116 record (inference, derivation): is MITTENS the waiting-time problem or a distinct fixation problem.

Object: docs/research/math/objects.yaml M-116 (inference, derivation). Classification, no numbers. Duffy (evo008@L104,
relayed by Day): "Mittens is not the waiting time problem"; the waiting-time problem is the time "required for
beneficial genetic mutations to occur"; MITTENS "isn't concerned with mutation rates at all" and is "an empirical
audit of observable fixations". Matthews (evo008@L148, relayed): "I do still maintain that this is a waiting time
problem"; in creationist usage the waiting-time problem "is a fixation problem", and mutation and fixation rates are
"used interchangeably" (Axe, early 2000s). Gutsick Gibbon and Hancock (claim file F1c) place MITTENS in that lineage.
Both positions rest on quoted sentences; the record checks each verbatim and records what each rests on:
- for Duffy: F_max has no mutation-rate input, which Hancock himself says (G2h q1), so the formula is not a
  mutation-arrival calculation in form;
- for Matthews: the G_f MITTENS divides by is an observed LTEE rate that includes the wait for mutations to arise in
  a clonal population, which Day concedes is "a worst-case scenario" (evo005@L16; M-103; supply ratio kappa = 93,659,
  parameters mutation.supply_ratio_kappa), so arrival waiting sits inside the input even if not in the formula.
The rate-vs-distribution point is M-101 and the transfer point M-103 (cited). Axe 2004 is held as an abstract only
(bib Axe2004), so Matthews's Axe attribution is not checked here. No number to assert; no verdict (claim file F1c).

Run: research/.venv/bin/python -I docs/research/math/records/M-116.py [--write]
Without --write it checks that M-116.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo008": "sources/raw/refresh-2026-11-01/p-erica-and-the-evo-avengers-008/body.txt",
       "evo005": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-005/body.txt"}
F1C = "docs/research/claims/F1c-hancock-waiting-time-lineage.md"
BIB = "docs/research/sources/bib-literature.md"
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


def raw(src, quote):
    """A sentence from the held post body that the source map does not copy; checked when sources/raw is present."""
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def record(rec):
    return json.loads((ROOT / REC / f"{rec}.json").read_text(encoding="utf-8"))


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


# ---- Duffy / Day ------------------------------------------------------------------------------------------
WD_NOT = post("evo008", "Mittens is not the waiting time problem.")                                  # evo008@L104
WD_DEF = raw("evo008", "The waiting time problem refers to the significant amount of time required for beneficial "
                       "genetic mutations to occur in a population.")                                # evo008@L104
WD_AUDIT = raw("evo008", "The Mittens argument isn’t concerned with mutation rates at all. It is an empirical audit of "
                         "observable fixations. Mittens would be better referred to as the fixation problem.")  # L104
H_NOMU = held(SM + "branch-G.md", "Notice that his model had no mutation rate, right?")              # G2h q1 (Hancock)

# ---- Matthews, Gutsick Gibbon, Hancock -----------------------------------------------------------------------
M_STILL = post("evo008", "I do still maintain that this is a waiting time problem.")                 # evo008@L148
M_FIX = raw("evo008", "The waiting time problem in traditional creationist circles is a fixation problem.")  # L148
M_INTER = raw("evo008", "Mutation rate and fixation rate are used interchangeably a lot, inappropriately")   # L148
M_AXE = raw("evo008", "You can go back to Doug Axe’s original paper in the early 2000s and see exactly this")  # L148
GG = held(SM + "branch-F.md", "Now my understanding is that this is just the waiting time problem.")  # F1c q1
HANCOCK = held(SM + "branch-F.md", "we're going to show how the waiting time problem actually is not a problem for "
                                   "evolution at all")                                                # F1c q2
held(F1C, "Hancock's classification as 'in the lineage of waiting-time problems' is a family resemblance, conceded "
          "as such")

# ---- what each side rests on, in held text -----------------------------------------------------------------------
D_WORST = post("evo005", "the critics are correct that it captures a worst-case scenario")            # evo005@L16
held(SM + "evo005.md", "Concession: the LTEE rate includes mutation-arrival waiting in a clonal population.")
held(PY, "supply_ratio_kappa: {value: 93659, derived: \"38.4 / 4.1e-4\"")    # mutation.supply_ratio_kappa
held(BIB, "| Axe2004, KeefeSzostak2001, Taylor2001 | see refresh file section 5 | PMIDs 15321723, 11287961, 11535813 "
          "| abstracts only")
m103 = record("M-103")["positions"]
assert "kappa 93,659" in m103["day"]["holds"]                        # M-103 records the same under-supply
FMAX = held(SM + "branch-A.md", "F_max = (t_div × d) / (g_len × G_f) F_max = maximum achievable fixations t_div = "
                                "divergence time (in years) g_len = generation length (in years) d = Selective Turnover "
                                "Coefficient G_f = generations per fixation")                # A q1 (Q06), Day's definition
F_MAX_INPUTS = ["t_div", "d", "g_len", "G_f"]
assert all(f"{v} = " in FMAX for v in F_MAX_INPUTS)                  # every input Day defines
assert "mutation" not in FMAX.lower() and "μ" not in FMAX            # none of them is a mutation rate

finish({
    "object": "M-116",
    "inputs": [
        {"name": "F_max inputs", "value": F_MAX_INPUTS, "cite": "branch-A A q1 (Q06)"},
        {"name": "LTEE supply ratio kappa", "value": 93_659, "cite": "parameters mutation.supply_ratio_kappa; M-103"},
    ],
    "values": {
        "formula_has_mutation_rate_input": False,
        "G_f_input_includes_mutation_arrival_wait": True,
        "axe_2004_held": "abstract only",
    },
    "positions": {
        "day": {"reading": "Duffy: not the waiting-time problem; an empirical audit of observable fixations, better "
                           "called the fixation problem",
                "holds": "in form F_max has no mutation-rate input (Hancock says the same, G2h q1); it counts "
                         "fixations from an observed rate, not arrivals"},
        "critic": {"reading": "Matthews: still a waiting-time problem, since in creationist usage the waiting-time "
                              "problem is a fixation problem and the two rates are used interchangeably (Axe)",
                   "holds": "the observed G_f MITTENS divides by includes the wait for mutations to arise in a clonal "
                            "population, which Day concedes ('worst-case scenario', evo005@L16; kappa 93,659, M-103), "
                            "so arrival waiting is inside the input; Hancock's lineage claim is a family resemblance "
                            "(F1c)"},
    },
    "notes": "Inference, classification only; no number is printed in the rows. The two sides use 'waiting-time "
             "problem' in different senses: Duffy's is mutation arrival; Matthews's is the creationist usage in "
             "which it is a fixation problem. Under Duffy's sense the formula is not one (no mutation rate); under "
             "Matthews's sense the label fits, and the LTEE input carries arrival waiting either way. The Axe "
             "attribution is not checked (abstract only). The rate-vs-distribution point is M-101; transfer is "
             "M-103.",
})
