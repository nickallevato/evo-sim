#!/usr/bin/env python3
"""M-915 record (derivation): the arithmetic of McCarthy's MC-2 post (as revised 2026-10-31) and MC-2c replies that the
library did not hold.

Object: docs/research/math/objects.yaml M-915 (identity, derivation, variant_of M-212). Sources: MC-2 (McCarthy, "Vox Day
Responds", Substack free repost 2026-09-17, `updated_at` 2026-10-31), MC-2c (his replies in that thread, 2026-09-17 to
2026-11-01) and the Day and commenter lines he answers there; source map docs/research/math/sources/mccarthy-mc2.md.
Already settled elsewhere and only cited here: the 25 y single-basis 16.0M and the 20 y lag-adjusted 2e7 (M-914), the
neutral share 1/4 under Day's "3x more harmful" (M-914), 252,000/1,400 = 180 and 205e6/180 = 1,138,889 (M-711),
1,570/14.74 = 106.5 (M-701), k = mu under a size change (M-209), Day's corrected 8.25 (M-212), 4Ne (M-203).
Inputs are the speakers' own: McCarthy's 2N_e = 20,000, 50 neutral per gene copy per generation, p_fix 1/20,000,
360,000 and 320,000 generations (mc2@L12-L16), 400 billion (mc2@L9), 3% deleterious and 1.5% coding (mc2@L19, MC-10),
Day's "3x more harmful" as relayed (mc2@L18), Day's 410 million, 35 million and 13.8% as relayed (mc2@L20-L21), Day's
Kelvin factor (mc2c#339543355), MITTENS 3.0 abstract as Day quotes it (mc2c#340102853), Day's corrected calculation as
Matev quotes it (mc2c#345248135).
The record asserts every number the D-41 item-2 review page states that is not in an earlier record, and the R1 tests:
- revised post: 20,000 x 50 = 1e6 per generation, x 1/20,000 = 50 per generation; 360,000 x 50 = 18M, 320,000 x 50 =
  16M; against the 2e7 requirement -10% and -20%; the same post's L9 still has 4e11 / 20,000 = 2e7 (the 20 y mixed
  basis of M-914), 4e11 against 320,000 x 1e6 = 3.2e11 (+25%), 2e7 against 16M (+25%; correction -20%, R1 ledger);
- mc2c#375157428: 50 x (1e6 / 25) = 2e6 fixations per My; with a 1 My mean transit about 2e6 alleles are in transit at
  once (L = lambda W); x 9 My = 18M, x 8 My = 16M;
- neutral share: MC-10's 3% deleterious gives 0.97 (17.46M, 15.52M); Day's 3:1 gives 1/4 (4.5M, 4.0M); the two inputs
  differ by 3.88x and the choice moves the count -75% (a flip against 2e7, R1); McCarthy's coding scope is consistent
  with his own 3%: 1.5% x 3/4 = 1.125% <= 3%;
- Day's 410 Mb as relayed: 410e6 / 35e6 = 11.7 ("10x"); 410e6 / 0.138 = 2.97e9 (the base implied by "13.8 percent"),
  against 410e6 / 3.2e9 = 12.8% on McCarthy's 3.2e9 (mc2@L19);
- thread: McCarthy's "400 million by 6 million" = 66.7 against Day's 410/6 = 68.3 (M-914); Day's Kelvin 4.54e9 / 2e7 =
  227; MITTENS 180 / 205e6 = 8.78e-7 = 0.0000878% ("0.000088%"); Day's corrected calculation as Matev quotes it:
  3,300 x 100 = 330,000, x 400,000 = 1.32e11, / 1.6e10 = 8.25, 2e7 / 8.25 = 2,424,242 ("133x" does not reproduce
  from the quoted inputs: 2e7 / 2e7 = 1); 2 x 8e9 = 1.6e10; McCarthy's original as Day restates it: 1e6 x 400,000 = 4e11.

Run: research/.venv/bin/python -I docs/research/math/records/M-915.py [--write]
Without --write it checks that M-915.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
MAP = "docs/research/math/sources/mccarthy-mc2.md"
RAW = ["sources/raw/mccarthy-mc2-2026-11-26/text.txt", "sources/raw/mccarthy-mc1-2026-11-26/comments-vdr.txt"]
M914, M711 = "docs/research/math/records/M-914.json", "docs/research/math/records/M-711.json"


def norm(s):
    return " ".join(s.split())


def held(text, quote, where):
    assert norm(quote) in norm(text), (where, quote[:60])
    return quote


def mc(quote):
    """A quote from MC-2 / MC-2c: in the committed source map, and in the held fetch when this checkout has it."""
    held((ROOT / MAP).read_text(encoding="utf-8"), quote, MAP)
    if all((ROOT / r).exists() for r in RAW):
        held("\n".join((ROOT / r).read_text(encoding="utf-8") for r in RAW), quote, "raw")
    return quote


def near(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


# ---- the source sentences ---------------------------------------------------------------------------
mc("Using Vox’s numbers, there have been roughly 400 billion mutations in the human race since the split that have had the time to fix—and 400 billion x 1/20,000 = 20 million mutations that have been observed.")
mc("That gives 20,000 times 50 = 1,000,000 new neutral mutations per generation.")
mc("Multiply by the fixation probability 1/20,000, and you get 50 expected neutral substitutions per generation.")
mc("Over 360,000 generations, that gives 18 million expected substitutions in the long-term neutral model. Over 320,000 generations gives 16 million substitutions.")
mc("Across the genome as a whole, only 3% of new mutations are deleterious.")
mc("The roughly 3-to-1 ratio of harmful to neutral mutations applies to mutations in protein-coding sequence, which makes up only about 1.5 percent of the human genome.")
mc("There are 3x more harmful mutations than neutral ones.")
mc("In fact, the genetic difference between chimps and humans turned out to be 13.8 percent, with 410 million base pairs separating the two lineages since the Chimpanzee-Human Last Common Ancestor. This 10x increase in the number of observed differences between the two genomes")
mc("Under our assumptions, approximately two million neutral mutations become fixed per million years, on average, even though each successful mutation takes an average of one million years to reach fixation.")
mc("And do you really think I can’t divide 400 million by 6 million?")
mc("That's only a factor of 227x.")
mc("This represents 0.000088% of the approximately 205 million fixations required on the human lineage.")
mc("Expected fixations: 132 billion × 1/16,000,000,000 = 8.25 fixations")
mc("Thus the shortfall increases from 133x to 2,424,242x when we go from the theoretical to the actual.")
m914 = json.loads((ROOT / M914).read_text(encoding="utf-8"))["values"]
assert m914["rf7_lag"]["single_basis_25y"] == 16e6 and m914["rf7_lag"]["as_written"] == 20e6
assert m914["mc1_match"]["neutral_share_quarter"] == 5.625e6
assert (ROOT / M711).exists()

# ---- revised post, L12-L16 ---------------------------------------------------------------------------------
TWO_NE, PER_COPY, R = 20_000, 50, 20e6
p_fix = 1 / TWO_NE
per_gen = TWO_NE * PER_COPY
assert per_gen == 1e6 and per_gen * p_fix == 50                         # "1,000,000" and "50 ... per generation"
G_FULL, G_LAG = 360_000, 320_000
assert 9e6 / 25 == G_FULL and G_FULL - 4 * 10_000 == G_LAG             # 25 y over 9 My; 4Ne lag (M-914)
full, lagged = G_FULL * 50, G_LAG * 50
assert full == 18e6 and lagged == 16e6 == m914["rf7_lag"]["single_basis_25y"]
vs_req = {"18M": full / R - 1, "16M": lagged / R - 1}
near(vs_req["18M"], -0.10, 1e-12); near(vs_req["16M"], -0.20, 1e-12)
assert all(abs(v) <= 0.25 for v in vs_req.values())                     # "roughly the expected number": holds under R1

# ---- the same post, L9 (unchanged 4e11 -> 2e7) against its own L16 ---------------------------------------------
l9_supply, l9_count = 4e11, 4e11 * p_fix
assert l9_count == 20e6
assert G_LAG * per_gen == 3.2e11
near(l9_supply / 3.2e11 - 1, 0.25, 1e-12)                               # 4e11 is 25% above the post's own 3.2e11
near(lagged / l9_count - 1, -0.20, 1e-12)                               # correcting L9 to L16: -20%, ledger (R1)

# ---- mc2c#375157428: rate and pipeline ----------------------------------------------------------------------
gens_per_my = 1e6 / 25
per_my = 50 * gens_per_my
assert gens_per_my == 40_000 and per_my == 2e6                          # "approximately two million ... per million years"
W_MY = 4 * 10_000 * 25 / 1e6
assert W_MY == 1.0                                                      # "one million years to reach fixation"
in_transit = per_my * W_MY
assert in_transit == 2e6                                                # Little's law: ~2e6 destined-to-fix alleles in transit
assert per_my * 9 == full and per_my * 8 == lagged

# ---- neutral share: MC-10 against Day's 3:1 ---------------------------------------------------------------
share_mc, share_day = 1 - 0.03, 1 / (1 + 3)
assert share_day == 0.25
near(full * share_mc, 17.46e6, 1e-3); near(lagged * share_mc, 15.52e6, 1e-3)
assert full * share_day == 4.5e6 and lagged * share_day == 4.0e6
near(share_mc / share_day, 3.88, 1e-12)
near(share_day / share_mc - 1, -0.742268, 1e-6)                         # choice of input moves the count ~-74%
assert full * share_day < 0.75 * R                                      # Day's input flips the match (R1)
near(0.015 * 0.75, 0.01125, 1e-15)
assert 0.015 * 0.75 <= 0.03                                             # coding share consistent with 3% genome-wide

# ---- Day's 410 Mb as relayed (mc2@L20) --------------------------------------------------------------------
near(410e6 / 35e6, 11.714, 1e-3)                                        # "10x increase"
near(410e6 / 0.138, 2.971e9, 1e6)                                       # base implied by "13.8 percent"
near(410e6 / 3.2e9, 0.128, 1e-3)                                        # on McCarthy's 3.2e9 (mc2@L19)

# ---- thread arithmetic -------------------------------------------------------------------------------------
near(400e6 / 6e6, 66.67, 0.01); near(410e6 / 6e6, 68.33, 0.01)          # McCarthy's restatement vs Day's question
assert round(4.54e9 / 20e6) == 227                                      # Day's Kelvin factor holds
near(100 * 180 / 205e6, 0.0000878, 1e-7)                                # "0.000088%"
assert 3_300 * 100 == 330_000 and 330_000 * 400_000 == 1.32e11
assert 2 * 8e9 == 1.6e10 and 1.32e11 / 1.6e10 == 8.25
assert round(20e6 / 8.25) == 2_424_242                                  # "2,424,242x" holds
assert 1e6 * 400_000 == 4e11 and 4e11 * p_fix == 20e6                   # "McCarthy's Original Calculation" as Day restates it
assert 20e6 / (4e11 * p_fix) == 1                                       # "133x" does not follow from the quoted inputs


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


finish({
    "object": "M-915",
    "variant_of": "M-212",
    "inputs": [
        {"name": "two_Ne", "value": TWO_NE, "cite": "mc2@L12"},
        {"name": "neutral_per_copy_per_generation", "value": PER_COPY, "cite": "mc2@L13"},
        {"name": "generations", "value": [G_FULL, G_LAG], "cite": "mc2@L16 (25 y over 9 My; minus 4Ne, M-914)"},
        {"name": "required_per_lineage", "value": R, "cite": "mc2@L9 (Day 2025, M-008)"},
        {"name": "l9_supply", "value": l9_supply, "cite": "mc2@L9"},
        {"name": "deleterious_share_genome", "value": 0.03, "cite": "mc2@L19 (MC-10, uncited)"},
        {"name": "coding_share", "value": 0.015, "cite": "mc2@L19 (uncited)"},
        {"name": "harmful_to_neutral", "value": 3, "cite": "mc2@L18 (Day as relayed; mc1c#337302874; uncited)"},
        {"name": "Day_410Mb_35M_13.8pct", "value": [410e6, 35e6, 0.138], "cite": "mc2@L20 (Day as relayed)"},
        {"name": "MITTENS_abstract", "value": [180, 205e6], "cite": "mc2c#340102853 (Day)"},
        {"name": "Day_corrected", "value": [3_300, 8e9, 400_000], "cite": "mc2c#345248135 (Matev quoting Day 2026-02-04)"},
    ],
    "values": {
        "revised_post": {"per_generation": per_gen, "fixations_per_generation": 50, "full_360k": full,
                         "lagged_320k": lagged, "vs_required": {k: round(v, 4) for k, v in vs_req.items()},
                         "r1": "match holds (|move| <= 20%)"},
        "l9_vs_l16": {"l9_count": l9_count, "l16_supply": 3.2e11, "l9_supply_excess": 0.25,
                      "correction": -0.20, "r1": "ledger"},
        "rate_and_pipeline": {"per_my": per_my, "transit_my": W_MY, "in_transit": in_transit},
        "neutral_share": {"mc10": share_mc, "day_3to1": share_day, "ratio": 3.88,
                          "counts_mc10": [17.46e6, 15.52e6], "counts_day": [4.5e6, 4.0e6],
                          "move": -0.7423, "r1": "flip: the input decides the match",
                          "coding_deleterious_share": 0.01125},
        "day_410": {"over_35M": 11.71, "implied_base_bp": 2.971e9, "share_of_3.2e9": 0.128},
        "thread": {"400M_over_6M": 66.67, "410M_over_6M": 68.33, "kelvin": 227,
                   "mittens_pct": 0.0000878, "day_corrected": 8.25, "shortfall": 2_424_242,
                   "133x": "not reproducible from the quoted inputs"},
    },
    "positions": {
        "day": {"reading": "the expected count needs the neutral share and the time; with three harmful per neutral the "
                           "revised 16-18M falls to 4.0-4.5M",
                "holds": "the neutral-share input decides the match (-74%); neither side cites its ratio"},
        "critic": {"reading": "on Day's inputs, with the 4Ne lag and parallel transit, the neutral expectation meets "
                              "the requirement (16-18M against 20M)",
                   "holds": "the revised post's arithmetic holds and stays within 20% of 2e7; 2e6/My with 2e6 in "
                            "transit answers the serial reading; the 3% input gives 15.5-17.5M"},
    },
    "notes": "MC-2 body was revised on 2026-10-31 (sha256 2f4dd854... against the 2026-10-07 78bf1ace...); the pre-revision "
             "text is not held. MC-09 is not in the revised body; on owner approval (EVOA-107, 2026-11-26) it is located "
             "at mc1c#337116873. L9 of the revised body keeps the 4e11 -> 2e7 of the mixed basis; L16 uses 25 y "
             "throughout. Matev's quote of Day's 'corrected calculation' is a double relay (Day blog 2026-02-04, not held).",
})
