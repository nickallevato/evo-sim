#!/usr/bin/env python3
"""M-415 record (lookup): did any Wistar biologist or later critic give a quantitative reply to Eden,
Ulam and Schützenberger?

Object: docs/research/math/objects.yaml M-415 (empirical, lookup). Day's claims (claim files D q2, q4,
q5; D2 q1-q3; D2g q1, q2) are universal: no biologist produced one calculation that even attempts to
contradict the mathematicians. The lookup lists what held text shows, with locators: the numbers
biologists gave in the volume (Wright p.117 and p.119, Mayr p.24; claim files D2g, D6, D4b), Fraser's
p.80 statement (no number), Eden's p.8 reply to Wright, and for later critics what is held of Rosenhouse
(chapter summaries only; claim files D1, D1c, D2) and Camestros Felapton (D1d, with R4 D1's existence
finding). The arithmetic is the two Wright figures and Mayr's gamma in Ulam's model (M-409). One held
counterexample answers the 'did any' question; whether it 'contradicts' depends on the reading of Eden.

Run: research/.venv/bin/python -I docs/research/math/records/M-415.py [--write]
Without --write it checks that M-415.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D, D1, D1C, D1D = (CL + "D-sequence-space-wistar.md", CL + "D1-rosenhouse-wistar-critiques-refuted.md",
                   CL + "D1c-rosenhouse-ch6-protein-space-weasel.md", CL + "D1d-camestros-no-developments-since-1966.md")
D2, D2G, D4B, D6 = (CL + "D2-day-rosenhouse-ch4-no-quantification.md", CL + "D2g-day-no-biologist-produced-a-calculation.md",
                    CL + "D4b-mayr-gamma-unreasonable-and-simultaneous.md", CL + "D6-wright-twenty-questions-1250.md")


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


# ---- Day's claims ---------------------------------------------------------------------------
DAY = {
    "D_q2_BestI_para26": held(D, "Eden calculated the size of sequence space. No one calculated a smaller space. Ulam "
                                 "calculated a rate. No one calculated a faster rate. Schützenberger asked for a mechanism. "
                                 "No one demonstrated one."),
    "D_q4_ch6": held(D, "The biologists did not answer the mathematicians. They could not."),
    "D_q5_ch6": held(D, "There is not one single example of a biologist producing one single calculation that even "
                        "attempts to contradict the mathematicians’ conclusions."),
    "D2_q1_BestII_para9": held(D2, "But his own chapter provides no quantitative refutation of any of the three "
                                   "mathematical arguments provided by the biologists at the time or by anyone else since."),
}

# ---- Wistar biologists (volume text as the claim files quote it) -------------------------------
WISTAR = {
    "Wright_p117": {"quote": held(D2G, "it would require less than 1250 questions to arrive at a specified one of these proteins."),
                    "number": True, "bears_on": "Eden's size argument read as random assembly"},
    "Wright_p119": {"quote": held(D2G, "In a population as large as the human species, 3 x 10 9 , a mutation rate of 10 5 at "
                                       "each locus implies that all single step mutations from the common alleles will "
                                       "recur in every generation."),
                    "number": True, "bears_on": "Ulam's supply of ten improvements per generation"},
    "Mayr_p24": {"quote": held(D4B, "but the recent work indicates that very often a mutant has a 30 percent advantage-in "
                                    "other words, up to 70 percent advantage."),
                 "number": True, "bears_on": "Ulam's gamma = 1e-6 (no source given for the 30 percent)"},
    "Fraser_p80": {"quote": held(D2G, "What is surprising is how fast rational information is produced by the machine within "
                                      "the meaning of the original context."),
                   "number": False, "bears_on": "Schützenberger (a simulation result stated without numbers)"},
}
EDEN_REPLY = held(D6, "Of course, he is correct, but I believe he has misunderstood my argument.")
D2G_DAY_POST = held(D2G, "Day's own post of 2024-07-13 reproduces Wright's 1250-question passage (as an example of an "
                         "'attempt' that fails), so the existence of Wright's calculation is not in dispute.")
D2G_NOTFOUND = held(D2G, "internal verdict depends on whether Eden's revised argument (path length) was ever quantitatively "
                         "answered at Wistar (not found).")

# ---- later critics ----------------------------------------------------------------------------
LATER = {
    "Rosenhouse_ch4": {"held": held(D1, "fidelity: unverifiable      # only Felsenstein's chapter summary seen"),
                       "text_held": False},
    "Rosenhouse_ch6": {"held": held(D1C, "| Rosenhouse 2022 ch.6 | not retrieved | unverifiable |"), "text_held": False},
    "Camestros_Felapton": {"held": held(D1D, "if he was making a serious attempt to discuss maths and evolution he’d talk "
                                             "about what developments happened since 1966. He doesn’t."),
                           "text_held": True},
    "R4_D1_existence": {"held": held(D1D, "existence part only (R4 D1): the quantitative post-1966 literature exists and is "
                                          "usable"),
                        "text_held": True},
}

# ---- the numbers biologists gave ---------------------------------------------------------------
assert 250 * 5 == 1250
near(250 * math.log2(20), 1080.5, 0.05)            # 1250 is above the information bound (M-407)
near(3e9 * 1e-5, 3e4, 1e-9)                        # mutants per locus per generation (M-407)
near(math.log(1e10) / 0.3, 76.8, 0.05)             # Mayr's gamma in Ulam's sweep (M-409)
near(math.log(1e10) / 1e-6, 2.30e7, 0.005e7)       # Ulam's gamma, same model
n_numbers = sum(v["number"] for v in WISTAR.values())
assert n_numbers == 3                              # three numerical replies at Wistar in held text

finish({
    "object": "M-415",
    "inputs": [{"name": k, "quote": v, "cite": "claim files D, D2"} for k, v in DAY.items()]
            + [{"name": k, "quote": v["quote"], "cite": "claim files D2g, D4b (Wistar volume)"} for k, v in WISTAR.items()]
            + [{"name": "Eden reply to Wright (p.8)", "quote": EDEN_REPLY, "cite": "claim file D6"}]
            + [{"name": k, "quote": v["held"], "cite": "claim files D1, D1c, D1d"} for k, v in LATER.items()],
    "values": {
        "wistar_numerical_replies": [k for k, v in WISTAR.items() if v["number"]],
        "wistar_non_numerical": [k for k, v in WISTAR.items() if not v["number"]],
        "wright_questions": 1250, "wright_mutants_per_locus_per_gen": 3e4,
        "sweep_generations": {"mayr_gamma_0.3": 76.8, "ulam_gamma_1e-6": 2.30e7},
        "eden_conceded_wright_arithmetic": True,
        "path_length_answered_at_wistar": False,
        "rosenhouse_chapters_held": False,
    },
    "positions": {
        "day": {"reading": "no biologist answered with a calculation that contradicts the conclusions; Wright's "
                           "attempt fails because Eden's argument is about path length",
                "supported_by": ["no numerical answer to the path-length argument at Wistar (D2g, not found)",
                                 "Mayr's 30 percent has no source"]},
        "critic": {"reading": "Wright gave a calculation and Eden conceded its arithmetic; Mayr gave a gamma that "
                              "changes Ulam's answer; later work exists",
                   "supported_by": ["Wright p.117, p.119", "Mayr p.24", "R4 D1 (existence of post-1966 data)"]},
    },
    "notes": "Held text answers 'did any' with yes: Wright p.117 (1250 questions) and p.119 (3e4 mutants per locus per "
             "generation) and Mayr p.24 (30 percent advantage) are numbers given in reply, and Eden accepted Wright's "
             "arithmetic. Day's 'not one single ... calculation that even attempts' is contradicted by these; his "
             "narrower point stands in the held text: no one at Wistar computed the path-length or serial-rate "
             "question as Eden and Ulam re-posed it, and Mayr's figure is unsourced. Rosenhouse's chapters 4 and 6 are "
             "not held, so what he computes is unknown here; post-1966 data exist (R4 D1), which says nothing about "
             "whether Rosenhouse uses them.",
})
