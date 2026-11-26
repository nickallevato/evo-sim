#!/usr/bin/env python3
"""M-416 record (lookup): Day's account of the Wistar volume against what the volume prints.

Object: docs/research/math/objects.yaml M-416 (empirical, lookup). For each attribution in the object's
used_by claim files (D2a, D2b, D2d, D2f, D2j, D3a, D3c, D4a, D5) the record holds Day's words, the
volume's words at the locator as the claim file quotes them, and the claim file's fidelity verdict, all
checked verbatim. The Wistar volume itself is not in sources/raw/; where the finding is that a sentence
is absent from the volume ('not found', 'not in the volume'), the record holds the claim file's recorded
search and cannot repeat it. No arithmetic beyond the verdict tally and the two numbers Day restates
(Eden's biosphere inputs, M-402; Eden's hemoglobin result, M-406).

Run: research/.venv/bin/python -I docs/research/math/records/M-416.py [--write]
Without --write it checks that M-416.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
F = {k: CL + v for k, v in {
    "D2a": "D2a-day-ulam-sides-with-eden.md", "D2b": "D2b-day-lewontin-cannot-justify-continuity.md",
    "D2d": "D2d-day-crosby-supported-eden.md", "D2f": "D2f-day-mayr-argument-from-existence.md",
    "D2j": "D2j-day-eden-apologises-for-vagueness-ch6.md", "D3a": "D3a-eden-molecules-not-functional-proteins.md",
    "D3c": "D3c-eden-hemoglobin-2.7-million-generations.md", "D4a": "D4a-ulam-random-construction-is-not-the-problem.md",
    "D5": "D5-schutzenberger-gap-between-typographic-and-functional-space.md"}.items()}


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


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


def row(cid, day, volume, locator, verdict, absent=False):
    f = F[cid]
    v = held(f, verdict)
    return {"claim": cid, "day": held(f, day), "volume": held(f, volume) if volume else None, "locator": locator,
            "fidelity": v.split()[1], "verdict_line": v, "absence_rests_on_claim_file_search": absent}


ROWS = [
    row("D2a", "Ulam explicitly states: “What I am going to do will come to Eden’s conclusions.”",
        "Eden's conclusions; but we will come to that later.", "Ulam pp.22-23",
        "fidelity: partial      # quoted sentence not found; nearest text says the opposite about magnitude", absent=True),
    row("D2b", "“Dr. Schützenberger: I would like to know how you could use a notion like quasi-continuity.” “Dr. "
               "Lewontin: That is a very good question. I don’t know.”",
        "DR. SCHUTZENBERGER: That's a good question. I don't think I have time to answer it now.",
        "Schützenberger p.79 (answering Mayr); the only 'good question' exchange in the volume per claim file D2b",
        "fidelity: misread      # quoted sentence not found in the volume", absent=True),
    row("D2b", "Lewontin’s response was circular. The fitness topology, he suggested, was “itself a product of evolution.”",
        "In fact, its topology is, itself, a product of evolution", "Levins p.79 (not Lewontin)",
        "fidelity: misread      # quoted sentence not found in the volume"),
    row("D2d", "Crosby actually supported Eden’s argument, noting that each intermediate stage “has got to be capable of "
               "existing viably”",
        "We are going through a series of stages, each of which has got to be capable of existing viably, if it is going "
        "to have any possibility of giving rise to the next.", "Crosby p.17 (on Eden's frame-shift suggestion)",
        "fidelity: partial      # both Crosby quotes are accurate (p.17, p.31); \"supported Eden's argument\" is an "
        "interpretation"),
    row("D2f", "“The very fact that we have this conference,” he observed at one point, “is evidence that evolution has "
               "occurred.”",
        "We are comforted by knowing that evolution has occurred.", "Mayr p.30 (nearest text)",
        "fidelity: partial      # quote accurate (p.30)", absent=True),
    row("D2j", "“I must apologize for being so vague on the nature of R,” he said, referring to the fitness function",
        "DR. BOSSERT: I must apologize for having been so vague on the nature of R2 which appears in the figures.",
        "Bossert p.40 (not Eden)",
        "fidelity: misread      # the quoted remark is William Bossert's answer to Waddington"),
    row("D3a", "filled with cells at a density of a billion billion per cubic centimeter, each containing proteins at a "
               "concentration of one ten-thousandth",
        "a protein concentration in these cells of 30%, a density of 1", "Eden p.7 (M-402)",
        "fidelity: partial      # Eden: \"protein molecules ... ever existed\"; Day (Best I): \"functional proteins that "
        "have ever existed\""),
    row("D3c", "Eden calculated that even under generous assumptions about mutation rates and selection coefficients, the "
               "time required to do so vastly exceeds the time available.",
        "This is a little large but not implausible.", "Eden p.8 (2.7e6 generations, M-406)",
        "fidelity: misread      # Eden's printed result is \"a little large but not implausible\""),
    row("D4a", "But, I believe that the comments of Professor Eden, in the first five minutes of his talk at least, refer "
               "to a random construction of such molecules",
        None, "Ulam p.21 (Rosenhouse's quotation via Day matches)",
        "fidelity: accurate      # the quote as used by Rosenhouse (via Day) matches p.21"),
    row("D5", "concluded that “there is a considerable gap in the neo-Darwinian theory of evolution, and we believe that "
              "this gap cannot be bridged within the current conception of biology.”",
        "we believe this gap to be of such a nature that it cannot be bridged within the current conception of biology.",
        "Schützenberger p.75 (wording altered, sense kept)",
        "fidelity: partial      # Day's Best I quotation alters the wording"),
]
RAW_NOT_HELD = held(F["D2f"], "This sentence is not in the volume (searched 'this conference', 'evidence that evolution "
                              "has occurred' in the OCR text and PDF text layer)")

# ---- tally (one verdict per claim file) ------------------------------------------------------
per_claim = {r["claim"]: r["fidelity"] for r in ROWS}
assert len(per_claim) == 9
tally = Counter(per_claim.values())
assert tally == Counter({"partial": 5, "misread": 3, "accurate": 1})
wrong_speaker = [r["claim"] for r in ROWS if r["locator"].endswith("(not Lewontin)") or r["locator"].endswith("(not Eden)")]
assert wrong_speaker == ["D2b", "D2j"]
absent = sorted({r["claim"] for r in ROWS if r["absence_rests_on_claim_file_search"]})
assert absent == ["D2a", "D2b", "D2f"]

finish({
    "object": "M-416",
    "inputs": [{k: r[k] for k in ("claim", "day", "volume", "locator", "verdict_line")} for r in ROWS],
    "values": {
        "fidelity_by_claim": per_claim, "tally": dict(sorted(tally.items())),
        "misattributed_speaker": {"D2b": "Levins p.79 and Schützenberger p.79, not Lewontin", "D2j": "Bossert p.40, not Eden"},
        "sentence_absent_from_volume": absent,
        "volume_in_sources_raw": False,
    },
    "positions": {
        "day": {"reading": "the chapter and posts summarise the symposium accurately",
                "accurate_or_partial": [c for c, v in per_claim.items() if v in ("accurate", "partial")]},
        "critic": {"reading": "several quotations and attributions do not match the volume",
                   "misread": [c for c, v in per_claim.items() if v == "misread"]},
    },
    "notes": "Of nine attributions, one is accurate (Ulam p.21), five partial (Ulam's 'come to Eden's conclusions' not "
             "found, nearest text p.22-23 says the reverse about magnitude; Crosby's words accurate, 'supported Eden' "
             "an interpretation; Mayr p.30 accurate but the 'this conference' sentence is not in the volume; Eden's "
             "inputs restated; Schützenberger's conclusion reworded) and three misread (the 'I don't know' exchange "
             "and the topology remark are Schützenberger's and Levins's at p.79, not Lewontin's; the apology is "
             "Bossert's at p.40, not Eden's; Eden called his 2.7e6 'not implausible'). The fidelity concerns the "
             "historical half, not the arithmetic. The three 'not in the volume' findings rest on the claim files' "
             "recorded searches; the volume is not in sources/raw/.",
})
