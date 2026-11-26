#!/usr/bin/env python3
"""M-407 record (inference): twenty questions against random assembly, each side's numbers side by side.

Object: docs/research/math/objects.yaml M-407 (inference, derivation). Wright (Wistar p.117, claim file
D6 q1; D2g) answers Eden's 10^350 with the game of twenty questions: 20 yes-or-no answers pick one of
about a million objects, so fewer than 1250 questions (250 residues x 5) pick a specified protein; he
adds (p.119, claim file D2g) that 3e9 humans at 1e-5 per locus make every single-step mutant recur each
generation. Eden replies (p.8) that Wright is correct but has misunderstood the argument. Ulam (p.21,
claim file D4a) says random construction 'is not the problem at all'. The record computes, without
choosing a side: under random assembly the expected trials to hit a specified 250-mer (20^250) and
under the twenty-questions model the questions needed (1250 printed; information bound log2 20^250 =
1080.5 bits), for both Eden figures (10^325 talk, 10^350 working paper), plus Wright's mutant supply.

Run: research/.venv/bin/python -I docs/research/math/records/M-407.py [--write]
Without --write it checks that M-407.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D6, D2G, D4A = CL + "D6-wright-twenty-questions-1250.md", CL + "D2g-day-no-biologist-produced-a-calculation.md", \
    CL + "D4a-ulam-random-construction-is-not-the-problem.md"


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


# ---- inputs -------------------------------------------------------------------------------
WRIGHT = held(D6, "Eden refers to the 10 350 proteins, each consisting of 250 amino acids. He seems to imply that it would "
                  "require something like this number of operations of natural selection to arrive at a particular useful "
                  "one. On the principle of the children's game of twenty questions in which it is possible to arrive at "
                  "the correct one of about a million objects by a succession of 20 yes-orono answers, it would require "
                  "less than 1250 questions to arrive at a specified one of these proteins.")
SUPPLY = held(D2G, "In a population as large as the human species, 3 x 10 9 , a mutation rate of 10 5 at each locus implies "
                   "that all single step mutations from the common alleles will recur in every generation.")
EDEN = held(D6, "Of course, he is correct, but I believe he has misunderstood my argument.")
ULAM = held(D4A, "But, I believe that the comments of Professor Eden, in the first five minutes of his talk at least, refer to "
                 "a random construction of such molecules and even those of us who are in the majority here, the "
                 "non-mathematicians, realize that this is not the problem at all.")
A, L = 20, 250

# ---- twenty questions ---------------------------------------------------------------------
assert 2 ** 20 == 1_048_576                        # 'about a million objects'
per_residue = 5
assert 2 ** (per_residue - 1) < A <= 2 ** per_residue  # 5 answers are the fewest that pick one of 20
Q = L * per_residue
assert Q == 1250                                   # Wright: 'less than 1250 questions'
bits_325 = L * math.log2(A)
near(bits_325, 1080.48, 0.005)                     # information bound for 20^250
bits_350 = 350 * math.log2(10)
near(bits_350, 1162.67, 0.005)                     # the bound for Eden's working-paper 10^350
assert bits_325 < bits_350 < Q                     # 1250 covers either of Eden's figures
near(Q - bits_325, 169.5, 0.05)                    # 1250 rounds the bound up by 170 questions

# ---- random assembly ------------------------------------------------------------------------
log_trials = L * math.log10(A)                     # expected uniform draws to hit one specified 250-mer
near(log_trials, 325.257, 0.0005)                  # M-401
near(log_trials - math.log10(Q), 322.16, 0.005)    # random typing needs 10^322 times more trials than questions
near(350 - math.log10(Q), 346.90, 0.005)

# ---- Wright's mutant supply ---------------------------------------------------------------
supply = 3e9 * 1e-5
near(supply, 3.0e4, 1e-6)                          # new mutants per locus per generation

finish({
    "object": "M-407",
    "inputs": [
        {"name": "Wright twenty questions", "value": {"answers": 20, "objects": "about a million", "questions": "< 1250"},
         "cite": "claim file D6 q1 (Wistar p.117); D2g"},
        {"name": "Eden figure Wright answers", "value": "10^350 (working paper p.110); talk p.7 gives 10^325",
         "cite": "claim file D6 q1; M-401"},
        {"name": "Wright mutant supply", "value": {"population": 3e9, "rate_per_locus": 1e-5}, "cite": "claim file D2g (Wistar p.119)"},
        {"name": "Eden reply", "value": "correct, but misunderstood my argument", "cite": "claim file D6 (Wistar p.8)"},
        {"name": "Ulam", "value": "random construction is not the problem at all", "cite": "claim file D4a q1 (Wistar p.21)"},
    ],
    "values": {
        "questions_printed": Q, "information_bound_bits_20_pow_250": g(bits_325), "bits_10_pow_350": g(bits_350),
        "random_assembly_log10_trials": g(log_trials), "mutants_per_locus_per_generation": g(supply),
    },
    "positions": {
        "day": {"reading": "Wright's analogy needs a fitness signal at every step; Eden said Wright misunderstood the "
                           "path-length argument; cumulative selection is not random typing either way",
                "random_assembly_log10_trials": g(log_trials),
                "number": "the path-length reading has no number: Eden offers none ('many powers of 10' above 120, "
                          "M-406, claim file D3b q4), so no count is computed for it here"},
        "critic": {"reading": "with a per-step signal a specified protein is reached in about 1250 steps, not 10^325 "
                              "(Wright); Ulam: random construction is not the problem",
                   "questions": Q, "information_bound_bits": g(bits_325),
                   "mutants_per_locus_per_generation": g(supply)},
    },
    "notes": "Both sides' numbers reproduce. 250 x 5 = 1250 questions is above the information bound log2 20^250 = "
             "1080.5 bits and above the 1162.7 bits of Eden's 10^350, so it holds for either of Eden's figures; random "
             "assembly needs 10^325.3 trials. Eden accepted the arithmetic (p.8) and moved the question to path length "
             "and per-step viability (M-405, M-404), which neither Wright's count nor Eden supplies a number for. "
             "Wright's 3e9 x 1e-5 = 3e4 mutants per locus per generation bears on mutation supply, not on the signal.",
})
