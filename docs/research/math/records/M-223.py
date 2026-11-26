#!/usr/bin/env python3
"""M-223 record (lookup): the reading of Chalub 2022 (Gegenbauer solution of the neutral Kimura equation).

Object: docs/research/math/objects.yaml M-223 (empirical, lookup). Each value is quoted verbatim from
held text with its locator: Day's sentences on Chalub in Z22903977 (the superseded 2026-09-22 file and
the 2026-10-13 file, Q288, Q286), Day's 2026-08-23 post (Q297), Chalub 2022's own sentences
(quotes-literature), Day's own statement of the outcome (claim file B1e) and Athos's para 4 (quotes-day
Q77 note). The arithmetic checks what the quoted claims say about the series: for a new copy
(x0 = 1/(2N)) the time-dependent fixation probability is x0 F(t), its limit is x0, its slowest term
decays as exp(-t/(2Ne)) (dominant eigenvalue), and exp(-pi^2 Ne/T) is its short-time form (the theta
transformation of the whole series, M-204), not the dominant-eigenvalue term.

Run: research/.venv/bin/python -I docs/research/math/records/M-223.py [--write]
Without --write it checks that M-223.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QD = "docs/research/sources/quotes-day.md"
QL = "docs/research/sources/quotes-literature.md"
B1E = CL + "B1e-chalub-2022-reading.md"


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


def F(x, n=400):
    """P(tau <= t | fixation) for a new copy, x = t/(4Ne) (diffusion series)."""
    return sum((-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x) for i in range(n))


# ---- lookups --------------------------------------------------------------------------------
DAY = {
    "Z22903977_2026-09-22_s1_superseded": held(B1E, "Chalub (2022), solving the neutral Kimura equation explicitly in terms of "
        "Gegenbauer polynomials, derives the time-dependent fixation probability as a series of exponential decay terms that "
        "converge to the steady-state value only as t → ∞."),
    "Q288_Z22903977_2026-10-13_s1": held(QD, "Chalub (2022), solving the neutral Kimura diffusion equation with absorbing "
        "boundaries, derives the explicit transient solution as a Gegenbauer polynomial expansion whose terms converge to the "
        "steady-state fixation probability u(p) = p only as t → ∞."),
    "Q286_Z22903977_2026-10-13_s1": held(QD, "Day and Athos (2026b) extract the dominant eigenvalue of that expansion via "
        "diffusion asymptotics in the arcsine-transformed coordinate system, converting Chalub's abstract series into the "
        "closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T)"),
    "Q297_blog_2026-08-23_para4": held(QD, "Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher "
        "model. It is not a result produced by the mathematics."),
    "blog_2026-08-23_outcome": held(B1E, "Impose that assumption and the fixation probability comes out equal to the starting frequency"),
}
CHALUB = {
    "abstract_model": held(QL, "we consider a population of two types evolving without mutation or selection, the so-called neutral evolution"),
    "abstract_constraints": held(QL, "Its solution is required to satisfy not only the equation but a series of conservation laws formulated as integral constraints."),
    "s3_time_dependent": held(QL, "Finally, the time-dependent fixation probability is given by"),
    "s2_classical": held(QL, "However, the classical solution decay in the limit t → ∞, and therefore cannot be the correct solution from the modeling point of view."),
}
ATHOS4 = held(QD, "For a neutral allele the chance of fixation is just its starting frequency, x₀ — for a new mutation, 1/(2N). That’s the standard result")

# ---- what the series does for a new copy ----------------------------------------------------------
N = 10_000
x0 = 1 / (2 * N)
for x in (5.0, 10.0, 25.0):
    near(x0 * F(x), x0, x0 * 3.1 * math.exp(-2 * x))     # u(x0, t) -> x0 as t -> inf
near(x0 * F(50.0), x0, 1e-30)                          # the limit is the starting frequency
# slowest term: 1 - F ~ 3 exp(-2x) = 3 exp(-t/(2Ne)): dominant eigenvalue 1/(2Ne) per generation
for x in (2.0, 4.0):
    near((1 - F(x)) / (3 * math.exp(-2 * x)), 1.0, 2 * math.exp(-4 * x))
# short-time form exp(-pi^2 Ne/T) is not the dominant-eigenvalue term (its exact form is checked in M-204)
x = 1 / 16
short = math.exp(-math.pi ** 2 / (4 * x))              # Day's closed form, Ne/T = 1/(4x)
dom = 1 - 3 * math.exp(-2 * x)                          # truncation to the dominant term (negative here)
assert dom < 0 < short                                  # one-term truncation is not a probability at short T

finish({
    "object": "M-223",
    "inputs": [{"name": k, "quote": v, "cite": "claim file B1e / quotes-day"} for k, v in DAY.items()]
            + [{"name": f"Chalub2022 {k}", "quote": v, "cite": "quotes-literature Chalub2022"} for k, v in CHALUB.items()]
            + [{"name": "Athos para 4 (posted by Day, 2026-09-21)", "quote": ATHOS4, "cite": "quotes-day Q77 note"}],
    "values": {
        "x0_new_copy_N1e4": x0, "limit_u": "x0", "dominant_decay_rate_per_gen": "1/(2Ne)",
        "short_time_form": "exp(-pi^2 Ne/T) x (4 pi Ne/T)^1.5 x e^(T/16Ne) (M-204)",
    },
    "positions": {
        "day": {"reading": "Chalub shows the transient, and 1/(2N) is imported from Wright-Fisher, not derived",
                "superseded_sentence_and_revision_agree": True},
        "critic": {"reading": "Chalub derives P(fix) = x0 under the neutral constraints; Wright-Fisher sets x0 = 1/(2N) as the starting frequency",
                   "supported_by_day_text": ["blog_2026-08-23_outcome", "Athos para 4"]},
    },
    "notes": "Both Day versions say the series converges to u(p) = p only as t -> inf, which the series confirms (limit "
             "x0). Day's own post states the outcome (fixation equals the starting frequency) and Athos para 4 calls "
             "1/(2N) the standard result. The 'dominant eigenvalue' gives the long-time decay exp(-t/2Ne); "
             "exp(-pi^2 Ne/T) is the short-time form of the whole series (M-204); the dominant term alone cannot "
             "give it (at T = Ne its one-term truncation is negative). A flag on Q286's wording, not on the closed form.",
})
