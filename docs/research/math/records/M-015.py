#!/usr/bin/env python3
"""M-015 record (identity): supermutator arithmetic of MITTENS 3.0 s6.4.

Object: docs/research/math/objects.yaml M-015 (identity, derivation). Asserts the corrected
product (3,840, printed 38,400), the deleterious count (384, printed 3,840), the fitnesses at the
corrected count (0.68, 0.021) against the printed ones (0.02, 1e-17), and that Day's
exponentiation is right for his printed inputs. Inputs carry their quote id or claim file;
held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-015.py [--write]
Without --write it checks that M-015.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"


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


A5H = CL + "A5h-supermutator-38400-slip.md"
Q135 = held(QD, "A 100-fold increase in mutation rate in the human genome would produce approximately 38,400 mutations "
                "per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100).")
DEL = held(A5H, "At a conservatively estimated 10% deleterious fraction, this means 3,840 deleterious mutations per "
                "individual per generation.")                                          # A5h q1
FIT = held(A5H, "fitness equals (0.999)^3,840 ≈ 0.02, a 98% fitness reduction. At a more realistic s = 0.01, fitness "
                "equals (0.99)^3,840 ≈ 10⁻¹⁷.")                                          # A5h q2
RE02 = held(CL + "A2h-supermutation-arithmetic-slip.md", "3.2 billion × 1.2 × 10⁻⁸ × 100 is 3,840 mutations per haploid "
            "genome, not 38,400.")                                                        # A2h q1

# ---- the product -------------------------------------------------------------------------
n_mut = 3.2e9 * 1.2e-8 * 100
near(n_mut, 3840, 1e-6)
printed_mut = 38_400
near(printed_mut / n_mut, 10, 1e-9)                    # printed figure is 10x
n_del = 0.10 * n_mut
near(n_del, 384, 1e-6)
printed_del = 3840
near(printed_del / n_del, 10, 1e-9)

# ---- fitness at the corrected count --------------------------------------------------------
w1 = 0.999 ** n_del
w2 = 0.99 ** n_del
near(w1, 0.681, 0.0005)                                # printed 0.02
near(w2, 0.0211, 0.00005)                              # printed 1e-17
near(1 - w1, 0.319, 0.0005)                            # 32% reduction, not 98%

# ---- Day's exponentiation on his printed count is right --------------------------------------
w1p = 0.999 ** printed_del
w2p = 0.99 ** printed_del
near(w1p, 0.0215, 0.00005)                             # "≈ 0.02"
near(1 - w1p, 0.98, 0.005)                             # "a 98% fitness reduction"
near(w2p, 1.73e-17, 0.01e-17)                          # "≈ 10^-17"
near(w1 / w1p, 31.7, 0.05)                             # size of the gap at s = 0.001
near(w2 / w2p, 1.22e15, 0.01e15)                       # and at s = 0.01

finish({
    "object": "M-015",
    "inputs": [
        {"name": "genome length, per-site rate, fold", "value": [3.2e9, 1.2e-8, 100], "cite": "Q135 (Z23003785 s6.4 p.11)"},
        {"name": "printed mutations", "value": 38_400, "cite": "Q135"},
        {"name": "deleterious fraction and printed count", "value": [0.10, 3840], "cite": "A5h q1"},
        {"name": "s and printed fitnesses", "value": [[0.001, 0.02], [0.01, 1e-17]], "cite": "A5h q2"},
        {"name": "critic correction", "cite": "A2h q1 (RE-02)", "quote": RE02},
    ],
    "values": {
        "mutations": g(n_mut), "printed_mutations": printed_mut, "deleterious": g(n_del), "printed_deleterious": printed_del,
        "fitness_s0.001": g(w1), "fitness_s0.01": g(w2),
        "fitness_s0.001_at_printed_3840": g(w1p), "fitness_s0.01_at_printed_3840": g(w2p),
        "ratio_s0.001": g(w1 / w1p), "ratio_s0.01": g(w2 / w2p),
    },
    "positions": {
        "day": {"claim": "a 100-fold supermutator is near zero fitness ('functionally dead')",
                "printed": {"mutations": printed_mut, "deleterious": printed_del, "fitness": [0.02, 1e-17]},
                "exponentiation_correct_for_printed_inputs": True},
        "critic": {"claim": "the product is 3,840, not 38,400",
                   "corrected": {"mutations": g(n_mut), "deleterious": g(n_del), "fitness": [g(w1), g(w2)]}},
    },
})
