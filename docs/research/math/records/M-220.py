#!/usr/bin/env python3
"""M-220 record (lookup): is neutral theory a post-hoc retreat? Dates of the neutral and parallel-fixation results.

Object: docs/research/math/objects.yaml M-220 (inference, lookup). Each value is quoted verbatim from
held text with its locator: the publication years of Kimura 1962, Kimura 1968 and Kimura & Ohta 1969
(bib-literature), a sentence from each (quotes-literature, claim files B7a, B7b), Balloux & Lehmann's
citation of Kimura and Ohta 1971 and Kimura 1983, and the date of Day's earliest dated source
(bib-day, B2019-01-29). Hancock's two quotes and the Duffy slide (secondhand) give the two positions.
The arithmetic is the gap in years. Kimura's stated motive (the slide's "direct response to Haldane")
is not in held text and is not checked here.

Run: research/.venv/bin/python -I docs/research/math/records/M-220.py [--write]
Without --write it checks that M-220.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QL = "docs/research/sources/quotes-literature.md"
BL = "docs/research/sources/bib-literature.md"
BD = "docs/research/sources/bib-day.md"
B5J = CL + "B5j-hancock-neutral-theory-is-not-a-retreat.md"


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


# ---- lookups --------------------------------------------------------------------------------
LIT = {
    "Kimura1962": (1962, held(BL, "| Kimura1962 | Kimura M. 1962. On the probability of fixation of mutant genes in a population. Genetics 47(6):713-719."),
                   held(CL + "B7a-kimura-1962-fixation-probability.md", "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene."),
                   "Genetics 47:713, p.716 (B7a q2)"),
    "Kimura1968": (1968, held(BL, "| Kimura1968 | Kimura M. 1968. Evolutionary rate at the molecular level. Nature 217:624-626."),
                   held(QL, "Calculating the rate of evolution in terms of nucleotide substitutions seems to give a value so high "
                            "that many of the mutations involved must be neutral ones."),
                   "Nature 217:624, abstract (quotes-literature Kimura1968)"),
    "KimuraOhta1969": (1969, held(BL, "| KimuraOhta1969 | Kimura M, Ohta T. 1969. The average number of generations until fixation of a mutant gene in a finite population. Genetics 61(3):763-771."),
                       held(QL, "a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne."),
                       "Genetics 61:763, Summary p.770 (B7b q1)"),
}
BL_CITE = held(QL, "One of the central results of the Neutral Theory of evolution (Kimura and Ohta 1971; Kimura 1983) states "
                   "that the rate k of allele substitution (rate of evolution) at neutral loci is unaffected by fluctuations "
                   "in population size and is simply equal to the mutation rate.")
DAY_FIRST = held(BD, "| B2019-01-29-there-will-be-debate | blog | 2019-01-29 | There will be debate |")
HA1 = held(B5J, "So like drift can still dominate at the molecular level and selection is dominating at the phenotypic level.")
HA2 = held(B5J, "Um the these models existed long before Vox day um and exist completely independently of him.")
SLIDE = held(B5J, "\"Remove selection from the equation and you have removed Darwin.\" (t=02:14:14)")
SLIDE2 = held(B5J, "Day's slide says Kimura proposed neutral theory \"in 1968 as a direct response to Haldane's cost argument\" (t=02:13:32)")

years = {k: v[0] for k, v in LIT.items()}
for k, (y, bib, _, _) in LIT.items():
    assert f"{y}." in bib                               # year read from the held bibliography row
day_first = 2019
assert "2019-01-29" in DAY_FIRST
bd_dates = re.findall(r"\| ((?:19|20)\d\d-\d\d-\d\d) \|", (ROOT / BD).read_text(encoding="utf-8"))
assert min(bd_dates) == "2019-01-29"                    # earliest dated Day source in bib-day
gaps = {k: day_first - y for k, y in years.items()}
assert gaps == {"Kimura1962": 57, "Kimura1968": 51, "KimuraOhta1969": 50}
assert all(v > 0 for v in gaps.values())                # every result predates Day's earliest dated source
later = {"KimuraOhta1971": 1971, "Kimura1983": 1983}    # cited by Balloux & Lehmann 2012
assert all(day_first - y > 30 for y in later.values())

finish({
    "object": "M-220",
    "inputs": [
        {"name": k, "year": y, "quote": q, "locator": loc, "cite": "bib-literature; quotes-literature / claim files B7a, B7b"}
        for k, (y, _, q, loc) in LIT.items()
    ] + [
        {"name": "Balloux & Lehmann 2012 citing Kimura and Ohta 1971, Kimura 1983", "quote": BL_CITE, "cite": "quotes-literature BallouxLehmann2012"},
        {"name": "Day's earliest dated source", "value": "2019-01-29", "cite": "bib-day B2019-01-29-there-will-be-debate"},
        {"name": "Hancock", "quote": [HA1, HA2], "cite": "B5j q1, q2 (t=02:18:21, 02:20:03)"},
        {"name": "Duffy slide (secondhand)", "quote": SLIDE, "cite": "claim file B5j"},
    ],
    "values": {"years": years, "years_before_day_2019": gaps, "later_citations": later},
    "positions": {
        "day": {"reading": "neutral theory is where neo-Darwinists flee; removing selection removes Darwin",
                "number": None,
                "why_none": "the slide's claim is about motive (a 1968 response to Haldane); the held text does not quote Kimura's motive"},
        "critic": {"reading": "the models predate Day and exist independently of him", "years_before_day": gaps},
    },
    "notes": "The neutral fixation probability (1962), the neutral-majority argument (1968) and the 4Ne fixation time "
             "(1969) predate Day's earliest dated source (2019) by 50-57 years. Whether Kimura proposed neutrality in response to "
             "Haldane's cost (the slide) is a motive claim the held text does not settle; it does not bear on the dates.",
})
