#!/usr/bin/env python3
"""M-218 record (inference): which terms of the three-term bound constrain total k and which only the adaptive rate.

Object: docs/research/math/objects.yaml M-218 (inference, derivation). Day's retraction (Q67, B4c q2):
Term 3 (selection-cost limit) bounds the adaptive rate at ~1e-12 per site per generation; total k is
governed by Terms 1 and 2. The record recomputes Term 3 = s_max d / [2 L ln(2 Ne)] at the Z19984826
human inputs (claim file H1), its per-genome and per-lineage counts, and sets it beside the neutral
rate k = mu (the critic position, and Day's "10^-7 to 10^-8" for total k). Both sides agree on the
scope; the record fixes the numbers. Inputs carry their quote id, claim file or parameters.yaml key;
held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-218.py [--write]
Without --write it checks that M-218.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QD = "docs/research/sources/quotes-day.md"
PY = "docs/research/parameters.yaml"
H1 = CL + "H1-term3-retraction.md"


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
Q67 = held(QD, "my error was in interpreting its output as a constraint on total k. Once corrected, Term 3 still limits "
               "adaptive substitution rate at ~10⁻¹², but total substitution rate is only governed by Terms 1 and 2")
Q66 = held(H1, "the realized substitution rate equals the minimum of three serial constraints: the corrected input flux "
               "(Term 1), the polymorphism throughput ceiling (Term 2), and the selection-cost limit (Term 3).")
FORM = held(H1, "Term 3 = k_sel = s_max d / [2 L ln(2 Ne)] (H8)")
TOTAL = held(H1, "k_total = min(Term 1, Term 2), \"in the 10⁻⁷ to 10⁻⁸ range\"")
INP = held(H1, "8.3e-12 per site (Z19984826 §4.3 human case, Ne = 3,300, d = 0.45, s_max = 1, L = 3.1e9)")
PY_MU = held(PY, "pedigree_human: {value: 1.2e-8")

S_MAX, D, L, NE, MU = 1.0, 0.45, 3.1e9, 3_300, 1.2e-8

t3 = S_MAX * D / (2 * L * math.log(2 * NE))
near(t3, 8.25e-12, 0.01e-12)                            # claim file 8.3e-12
near(math.log10(t3), -11.08, 0.01)                      # "~10^-12" is the order Day states; value is 8.3x 1e-12
per_gen = t3 * L
near(per_gen, 0.02558, 0.00001)                         # 0.45/(2 ln 6600)
near(1 / per_gen, 39.1, 0.05)                           # one adaptive substitution per 39 generations
near(per_gen * 260_000, 6_650, 5)                       # about 6,650 over 260,000 generations
# total k from the neutral terms
assert 1e-8 <= MU <= 1e-7                               # pedigree mu sits in Day's "10^-7 to 10^-8"
share = t3 / MU
near(share, 6.88e-4, 0.01e-4)                           # Term 3 is under 0.07% of the neutral rate
near(per_gen * 260_000 / 20e6, 3.3e-4, 0.05e-4)         # against 20M differences

finish({
    "object": "M-218",
    "inputs": [
        {"name": "retraction", "cite": "Q67 (B4c q2; H1 q1)"},
        {"name": "three-term framework", "cite": "Q66 (claim file H1)"},
        {"name": "Term 3 and inputs", "value": {"s_max": S_MAX, "d": D, "L": L, "Ne": NE}, "cite": "claim file H1 (Z19984826 s4.3 human case)"},
        {"name": "total k range", "value": "1e-8 to 1e-7", "cite": "claim file H1 (retraction post)"},
        {"name": "neutral mu", "value": MU, "cite": "parameters mutation.mu_per_site_per_gen.pedigree_human"},
    ],
    "values": {"term3_per_site": g(t3), "term3_log10": g(math.log10(t3)), "per_genome_per_gen": g(per_gen),
               "gens_per_adaptive": g(1 / per_gen), "adaptive_260k_gens": g(per_gen * 260_000),
               "term3_over_mu": g(share)},
    "positions": {
        "day": {"reading": "Term 3 bounds the adaptive rate only; total k from Terms 1 and 2",
                "term3": g(t3), "total_k_range": [1e-8, 1e-7]},
        "critic": {"reading": "concedes the point; the total rate is the neutral rate",
                   "total_k": MU, "term3_share_of_total": g(share)},
    },
    "notes": "Both sides agree on the scope. Term 3 at the stated inputs is 8.3e-12 per site (Day: '~10^-12'), 0.0256 "
             "per genome per generation, about 6,650 adaptive substitutions over 260,000 generations, under 0.07% of "
             "a neutral rate of 1.2e-8, which lies inside Day's stated total range.",
})
