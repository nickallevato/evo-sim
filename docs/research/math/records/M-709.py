#!/usr/bin/env python3
"""M-709 record (lookup): does MITTENS 3.0 omit the Bernoulli Barrier and the Averaging Problem?

Object: docs/research/math/objects.yaml M-709 (empirical, lookup). Day (Ge q1, 2026-10-01 para 26) says he omitted
both from MITTENS 3.0 (Z23003785) and that both remain entirely correct. The held re-fetch of Z23003785 (R4
VID-01-score, 2026-10-13: sources/raw/vid01-score-2026-10-13/, main.pdf and addendum.pdf, read-only) matches the
sha256 pins in bib-day.md. When that directory is present the record re-hashes both PDFs against the pins and
repeats the case-insensitive, whitespace-normalised count over the pdftotext files main.txt and addendum.txt (read
as text, never executed): "bernoulli" 1 (main.txt line 55, s1, a rhetorical clause), "barrier" 1 (the same clause),
"averaging", "averaging problem", "law of large numbers", "polygenic" 0, "coefficient of variation" 1 (addendum,
unrelated). sources/raw/ is gitignored, so in a checkout without it the record checks the same counts against the
claim file Ge and R4 VID-01-score only and cannot repeat the count; its JSON is the same either way. The omission
half of the statement is a text fact; "entirely correct" is G's external question (contested), not a lookup.

Run: research/.venv/bin/python -I docs/research/math/records/M-709.py [--write]
Without --write it checks that M-709.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
GE = "docs/research/claims/Ge-bb-omitted-from-3-0.md"
G = "docs/research/claims/G-bernoulli-barrier.md"
BIB = "docs/research/sources/bib-day.md"
VID = "research/checks/results/R4-VID-01-score.md"
RAW = ROOT / "sources/raw/vid01-score-2026-10-13"


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


# ---- Day and the held reports ------------------------------------------------------------------------
DAY = held(GE, "Anyhow, the MITTENS 3.0 paper [URL: https://zenodo.org/records/23003785] renders those complicating "
               "elements moot to such an extent that I omitted both the Bernoulli Barrier and the Averaging Problem, "
               "even though both of them remain entirely correct.")              # Ge q1
GE_NUM = held(GE, "\"Bernoulli\" occurs exactly once, in a rhetorical clause in s1, undefined and underived; "
                  "\"Averaging\"/\"averaging problem\"/\"law of large numbers\" occur 0 times in body and addendum.")
GE_POLY = held(GE, "**`polygenic` 0 occurrences** in body and addendum")
GE_CV = held(GE, "| `coefficient of variation` | 1, addendum, descriptive statistics of per-population fixation counts; "
                 "unrelated to the barrier |")
VID_LINE = held(VID, "main:55, §1: \"When MITTENS demonstrates that sequential fixation cannot fill the timeline, the "
                     "defender invokes parallel fixation. **When the Bernoulli Barrier demonstrates that parallel "
                     "fixation is probabilistically self-defeating, the defender invokes neutral drift.**")
G_EXT = held(G, "external: \"contested\"")
PIN_MAIN = "22bb4ef8eae7d5c4756987e5418bf26d795ac65e58f36072c393735bdf7a37b2"
PIN_ADD = "d55e8a030716a0b913082dd04fd5d8967695775814265d348886d314d8df0ce7"
held(BIB, "sources/raw/day/zenodo-23003785.pdf | " + PIN_MAIN)  # bib-day Z23003785 pin
held(BIB, "sources/raw/day/zenodo-23003785-f2.pdf | " + PIN_ADD)  # bib-day Z23003785-f2 pin
held(VID, "| main.pdf (`MITTENS 3.0 …pdf`, 114,352 B) | `" + PIN_MAIN + "` | Z23003785, same | **yes** |")
held(VID, "| addendum.pdf (`Addendum …pdf`, 43,698 B) | `" + PIN_ADD + "` | Z23003785-f2, same | **yes** |")

# the counts as the held reports give them (main + addendum, case-insensitive)
COUNTS = {"bernoulli": 1, "barrier": 1, "bernoullian": 0, "averaging": 0, "averaging problem": 0,
          "law of large numbers": 0, "polygenic": 0, "coefficient of variation": 1}
assert "exactly once" in GE_NUM and "0 times" in GE_NUM and "0 occurrences" in GE_POLY and "| 1, addendum" in GE_CV
assert VID_LINE.count("Bernoulli") == 1 and "Barrier" in VID_LINE   # the one "barrier" is in the Bernoulli clause

# ---- repeat the count when the hash-matched re-fetch is in this checkout --------------------------------
if (RAW / "main.pdf").exists():
    assert hashlib.sha256((RAW / "main.pdf").read_bytes()).hexdigest() == PIN_MAIN
    assert hashlib.sha256((RAW / "addendum.pdf").read_bytes()).hexdigest() == PIN_ADD
    norm = lambda p: " ".join(p.read_text(encoding="utf-8").split()).lower()
    main, add = norm(RAW / "main.txt"), norm(RAW / "addendum.txt")
    for term, k in COUNTS.items():
        assert main.count(term) + add.count(term) == k, (term, main.count(term), add.count(term))
    assert add.count("coefficient of variation") == 1 and main.count("bernoulli") == 1
    line55 = (RAW / "main.txt").read_text(encoding="utf-8").split("\n")[54]      # grep numbering (form feeds kept)
    assert "Bernoulli Barrier" in line55
    print("M-709: count repeated on the hash-matched re-fetch")
else:
    print("M-709: sources/raw/vid01-score-2026-10-13 not in this checkout; counts held from Ge and R4 VID-01-score only")

finish({
    "object": "M-709",
    "inputs": [
        {"name": "Day's statement", "value": "omitted both ... both of them remain entirely correct", "cite": "Ge q1 (B2026-10-01-they-never-stop-lying para 26)"},
        {"name": "MITTENS 3.0 text", "value": {"main.pdf": PIN_MAIN, "addendum.pdf": PIN_ADD},
         "cite": "bib-day Z23003785, Z23003785-f2 pins; re-fetch sources/raw/vid01-score-2026-10-13 (R4 VID-01-score)"},
    ],
    "values": {
        "counts_main_plus_addendum": COUNTS,
        "bernoulli_locator": "main.txt line 55, s1 (rhetorical clause, no definition, derivation or number)",
        "omission_half": "true as stated",
        "entirely_correct_half": "not a lookup: G external contested",
    },
    "positions": {
        "day": {"reading": "3.0 renders the elements moot, so both were omitted; both remain entirely correct",
                "holds": "the omission is verified: one undefined mention of the Barrier, 0 of the Averaging Problem"},
        "critic": {"reading": "omission is not a retraction and not support",
                   "holds": "the 3.0 text is silent on the Barrier's correctness; that half rests on G (contested)"},
    },
    "notes": "Text lookup, not arithmetic. The count is repeated by this script only when the gitignored re-fetch is "
             "present and hash-matched; otherwise the record holds the counts as Ge and R4 VID-01-score report them. "
             "'barrier' occurs once, inside the same Bernoulli clause. 'coefficient of variation' occurs once, in the "
             "addendum's descriptive statistics, unrelated to the Barrier. Whether the Barrier and the Averaging Problem "
             "'remain entirely correct' is G's external question (contested) and M-701/M-702, not this record.",
})
