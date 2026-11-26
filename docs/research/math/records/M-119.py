#!/usr/bin/env python3
"""M-119 record (inference, derivation): is molecular-clock dating circular with k = mu.

Object: docs/research/math/objects.yaml M-119 (inference, derivation). Day (pgenetics@L16, the abstract of Z22903977
quoted in the post): the clock is k = mu's "sole practical application" and is "both circular and logically invalid
because divergence dates are derived from the identity, then cited as independent confirmation of the identity".
The same paper (claim file B4d q1-q2): the date was calculated from k = mu and the mutation rate "adjusted to keep the
date consistent". McCarthy (B4e, critic) and Hossjer (B4f, ally) state the same dependence. No number to recompute
for the circularity itself; the record quotes what each position rests on and asserts the little arithmetic in the
rows:
- for Day: a date from T = D/(2 mu) (B4d formal statement) moves as 1/mu, so the twofold lower pedigree rate
  (Keightley 2012, held abstract) doubles the date, the direction Day describes; every such date assumes k = mu per
  generation, whatever calibrates mu (B4d analysis);
- for the critics: a pedigree mu is a measurement that does not come from a date, and Langergraber 2012 dates the
  split "at least 7-8 million years" without fossil calibration (parameters divergence.t_div_years.langergraber_2012),
  so the loop is not closed by a measured date; and "sole practical application" is absolute, while Day's own
  Z18525185 uses k = mu to predict 630 fixations in 350 generations (C6 q2; 1.2e-8 x 1.5e8 x 350 = 630, record
  M-302), a second use in his own corpus.
k = mu as a long-run identity, and why it has no time term, is M-111 (cited, not recomputed). No verdict (B4d, C6).
Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-119.py [--write]
Without --write it checks that M-119.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"pgenetics": "sources/raw/refresh-2026-11-01/p-breaking-population-genetics/body.txt"}
CL = "docs/research/claims/"
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


# ---- Day: the circularity claim ----------------------------------------------------------------------------
D_CIRC = post("pgenetics", "Its sole practical application, the calibration of the molecular clock, is both circular "
                           "and logically invalid because divergence dates are derived from the identity, then cited as "
                           "independent confirmation of the identity.")                        # pgenetics@L16
D_NOTIME = post("pgenetics", "The identity contains no time term and therefore cannot address whether any number of "
                             "fixations can complete in any given window.")                     # pgenetics@L16 (M-111)
B4D_1 = held(SM + "branch-B.md", "The circularity is complete. The divergence date was calculated from k = μ. The "
                                 "mutation rate was adjusted to keep the date consistent with k = μ.")  # B4d q1
B4D_2 = held(SM + "branch-B.md", "The identity is its own evidence. At no point does an independent measurement enter "
                                 "the loop.")                                                   # B4d q2
B4E = held(SM + "branch-B.md", "population geneticists actually use Kimura’s neutral-theory result to date the "
                               "human–chimpanzee divergence.")                                  # B4e q1 (McCarthy, critic)
B4F = held(SM + "branch-B.md", "since the neutral theory is used in the first place to date the assumed time of "
                               "divergence.")                                                   # B4f q1 (Hossjer, ally)
held(CL + "B4d-clock-circularity-day.md", "T = D/(2μ) (IR §5).")                                # Day's dating formula
KEIGHTLEY = held(CL + "B4d-clock-circularity-day.md",
                 "Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is "
                 "about twofold lower than estimates based on the human-chimp divergence.")    # Keightley 2012 abstract

# ---- critics: what the dates also rest on -----------------------------------------------------------------------
LANGER = held(CL + "B4d-clock-circularity-day.md", "We date the human-chimpanzee split to at least 7-8 million years "
                                                   "and the population split between Neanderthals and modern humans to "
                                                   "400,000-800,000 y ago.")                    # Langergraber 2012
held(PY, "langergraber_2012: {value: \">=7e6-8e6\", note: \"independent of fossil calibration\"")
B4D_ANALYSIS = held(CL + "B4d-clock-circularity-day.md",
                    "a date from pedigree μ and generation time is independent of the fossil calibration but not of the "
                    "*assumption* k = μ per generation")
held(CL + "B4e-mccarthy-dates-use-kimura.md", "Implicit: All dates; not distinguishing fossil-calibrated, "
                                              "pedigree-based and phylogenetic ones.")
held(CL + "B4d-clock-circularity-day.md", "Fossil-calibrated and pedigree-based dates agree within a factor ~1.5; the "
                                          "agreement is evidence for the assumption.")          # opposing model, B4d
C6_Q2 = held(SM + "branch-C.md", "The molecular clock predicts approximately 630 fixations per 350 generations (based "
                                 "on k = μ for neutral sites; see Appendix A).")                # C6 q2 (Day, Z18525185)

# ---- arithmetic in the rows -------------------------------------------------------------------------------------
T = lambda D, mu: Fr(D) / (2 * mu)                   # B4d: T = D/(2 mu), any D
D = Fr(1)
assert T(D, Fr(1, 2) * Fr(22, 10 ** 9)) == 2 * T(D, Fr(22, 10 ** 9))   # mu twofold lower -> date twofold older
clock = Fr(12, 10 ** 9) * Fr(15, 10) * 10 ** 8 * 350                  # C6: mu x neutral sites x generations
assert clock == 630
assert record("M-302")["values"]["genome_wide"]["clock_C6"] == 630.0  # the same 630 in record M-302
m111 = record("M-111")["values"]
assert m111["k_over_mu_constant_sizes_any_N_over_Ne"] == 1            # M-111: k = mu as the long-run identity

finish({
    "object": "M-119",
    "inputs": [
        {"name": "dating formula", "value": "T = D/(2 mu)", "cite": "claim file B4d formal statement (Z22903977 s5)"},
        {"name": "pedigree mu vs divergence-based mu", "value": "about twofold lower", "cite": "Keightley 2012 abstract (B4d)"},
        {"name": "fossil-independent date", "value": ">=7e6-8e6 y", "cite": "parameters divergence.t_div_years.langergraber_2012"},
        {"name": "C6 clock prediction", "value": "1.2e-8 x 1.5e8 x 350", "cite": "branch-C C6 q2; record M-302"},
    ],
    "values": {
        "date_scales_as_1_over_mu": True,
        "date_factor_at_half_mu": 2,
        "c6_clock_fixations": 630,
        "uses_of_k_eq_mu_in_days_own_corpus": ["clock calibration (Z22903977 s5)", "fixation prediction (Z18525185 s5.3)"],
        "k_eq_mu_long_run_identity": "M-111",
    },
    "positions": {
        "day": {"reading": "dates come from k = mu and are then cited as confirmation of it; the mutation rate was "
                           "re-fitted to keep the date; no independent measurement enters (pgenetics@L16; B4d q1-q2)",
                "holds": "every date from T = D/(2 mu) assumes k = mu per generation, whatever calibrates mu (B4d "
                         "analysis); the twofold lower pedigree mu doubles the date, the direction Day describes "
                         "(Keightley 2012); McCarthy (B4e) and Hossjer (B4f) state the same dependence"},
        "critic": {"reading": "clock dates also rest on calibrations that do not come from k = mu; 'sole practical "
                              "application' is absolute",
                   "holds": "a pedigree mu is measured without a date, and Langergraber 2012 dates the split at "
                            ">= 7-8 My without fossil calibration, so the date is not derived from itself; Day's own "
                            "Z18525185 applies k = mu to predict 630 fixations (C6 q2, M-302), a use other than "
                            "calibration"},
    },
    "notes": "Inference; the two positions answer different questions. Day's holds for 'is the date independent of "
             "the k = mu assumption' (no: every clock date uses it). The critics' holds for 'is the date derived "
             "from the identity and then cited for it' (not for a pedigree-mu date: mu is measured, not fitted). "
             "Whether agreement between fossil-calibrated and pedigree dates tests k = mu is B4d's open external "
             "question. The 'sole' wording meets a counter-example in Day's own corpus (C6). No verdict.",
})
