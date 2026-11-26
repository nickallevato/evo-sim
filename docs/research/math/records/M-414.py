#!/usr/bin/env python3
"""M-414 record (lookup): stated probability figures with no model (Milton 1 in 10^65; Schützenberger
under 10^-1000 and under 10^-100).

Object: docs/research/math/objects.yaml M-414 (parameter, lookup). Each value is quoted verbatim from
held text with its locator: Day's 2025-10-02 post relaying Milton (claim file D8 q1) and Schützenberger
at Wistar p.75 and p.76 (claim file D5a; OCR readings as the claim file gives them). The lookup answer
is what the held text supplies for each figure: a number, and whether a length, function, model or
derivation comes with it. Milton's 1992 book is not held (claim file D8, fidelity unverifiable), so the
answer for Milton is about the relay; the volume text around Schützenberger's figures is held only as
the claim file quotes it. The one piece of arithmetic is claim file D8's candidate reading (a specific
50-mer: 20^-50 = 10^-65.05), which no source states.

Run: research/.venv/bin/python -I docs/research/math/records/M-414.py [--write]
Without --write it checks that M-414.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D8, D5A = CL + "D8-milton-single-protein-1-in-1e65.md", CL + "D5a-schutzenberger-probability-figures-1e-100-1e-1000.md"


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


# ---- lookups --------------------------------------------------------------------------------
LOOK = {
    "milton_1_in_1e65": {
        "quote": held(D8, "When he examines the probability calculations for even a single protein forming by chance (1 in "
                          "10^65), he finds odds so astronomical that they’re equivalent to winning the lottery every week "
                          "for a thousand years with the same numbers."),
        "locator": "voxday.net, The Foundation of Sand, 2025-10-02 (blockquote, unattributed in the extracted text); "
                   "claim file D8 q1",
        "value_log10": -65,
        "model_given": held(D8, "Single stated number: P(single protein by chance) = 10^-65, no length, function or fold stated."),
        "source_held": held(D8, "fidelity: unverifiable      # Milton's 1992 book not retrieved"),
    },
    "schutzenberger_mechanism_lt_1e-1000": {
        "quote": held(D5A, "Further, there is no chance « I 0-1.000) to see this mechanism appear spontaneously and, if it "
                           "did, even less for it to remain."),
        "locator": "Wistar p.75 (Schützenberger); claim file D5a q1; OCR '« I 0-1.000)' read as '< 10^-1000'",
        "value_log10": -1000,
        "model_given": held(D5A, "Neither is derived in the text; on p.73 he says the cycle numbers are quoted from other "
                                 "speakers"),
    },
    "schutzenberger_meaningful_change_lt_1e-100": {
        "quote": held(D5A, "'I mean less than one out' ... 'of 10100' (OCR: 'less than one out ... of 10100 •')"),
        "locator": "Wistar p.76, discussion (column-interleaved OCR); claim file D5a",
        "value_log10": -100,
        "model_given": held(D5A, "P(a random typographic change preserves 'meaningful' function) < 10^-100 (for "
                                 "programs/meaningfulness in his sense)"),
    },
}
OCR_READ = held(D5A, "(OCR: '« I 0-1.000)' read as '< 10^-1000')")
UNTEST = held(D5A, "external: untestable      # the figures concern a hypothetical class of programs, not a measured "
                   "biological quantity")
CAND = held(D8, "Candidate reconstruction (this file; not in the source): a specific 50-residue sequence has probability "
                "20^-50 = 10^-65.05 (50*log10(20) = 65.05), so the figure is consistent with a specific 50-mer; no "
                "source says this.")

# ---- the one checkable arithmetic: claim file D8's candidate reading ------------------------
L50 = 50 * math.log10(20)
near(L50, 65.05, 0.005)
assert len(str(20 ** 50)) == 66                    # 20^50 = 1.13e65, exact integer
assert round(L50) == 65
# no other figure in the lookup carries an input, so nothing else can be recomputed

finish({
    "object": "M-414",
    "inputs": [{"name": k, "quote": v["quote"], "locator": v["locator"]} for k, v in LOOK.items()],
    "values": {
        k: {"log10_probability_bound": v["value_log10"], "derivation_in_held_text": False,
            "held_finding": v["model_given"]} for k, v in LOOK.items()
    } | {"milton_candidate_50mer_log10": round(-L50, 2),
         "milton_book_held": False},
    "positions": {
        "day": {"reading": "the figures show astronomical odds against chance formation",
                "figures_log10": [-65, -1000, -100]},
        "critic": {"reading": "no model, inputs or derivation are given, so the figures cannot be checked or tied to a "
                              "biological quantity",
                   "number": "none: the critic position is that there is nothing to compute"},
    },
    "notes": "Milton's figure is held only as Day's unattributed relay (1 in 10^65, no length, function or fold); the "
             "book is not held, so whether Milton derives it is unknown, and the held text gives no derivation. Claim "
             "file D8's candidate 50-mer reading (20^-50 = 10^-65.05) fits the number but no source states it. "
             "Schützenberger's < 10^-1000 (p.75) and < 10^-100 (p.76) come with no derivation in the volume as quoted; "
             "they concern a hypothetical class of programs (claim file D5a, external untestable).",
})
