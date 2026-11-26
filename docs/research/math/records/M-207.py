#!/usr/bin/env python3
"""M-207 record (inference): does the neutral pipe fill within the lineage window under HL's demography?

Object: docs/research/math/objects.yaml M-207 (inference, derivation). From an empty start at constant
Ne, the share of destined-to-fix mutations already fixed by T (fill F) is the conditional fixation-
time CDF F_X(T); the share of mu T delivered by T (D) is (1/T) int_0^T F_X. Both use the diffusion
series F_X(t) = 1 + sum_{i>=1} (-1)^i (2i+1) exp(-i(i+1) t/(4Ne)). The record recomputes every
reading in the B claim file (R4 RHclose table): F over 6.5 and 6.3 My, D, Takahata's Ne = 1e5 held
throughout, and HL's 2 My window, against the registered edge F >= 0.30 ("not nearly empty"). It
computes each side's reading and chooses neither. Inputs carry their quote id or claim file; held()
checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-207.py [--write]
Without --write it checks that M-207.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"
B = CL + "B-neutral-theory-cannot-rescue.md"


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


def fill(T, ne, n=400):
    x = T / (4 * ne)
    return sum((-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x) for i in range(n))


def delivered(T, ne, n=400):
    x = T / (4 * ne)
    tail = 1 - sum((-1) ** (i + 1) * (2 * i + 1) / (i * (i + 1)) * math.exp(-i * (i + 1) * x) for i in range(1, n))
    return 1 - tail / x                                  # (1/T) int_0^T F_X = 1 - 4Ne(...)/T


# ---- inputs -------------------------------------------------------------------------------
Q157 = held(B, "the neutral substitutions cannot be finished, because the pipe that would finish them never fills. "
               "Both the priced channel and the free channel shut inside the same lineage duration.")
NARROW = held(CL + "B2d-parallel-fixation-second-objection.md", "The correct interpretation is narrower: the pipeline cannot fill.")
FLUX = held(CL + "B2d-parallel-fixation-second-objection.md",
            "At steady state the total flux out is μ per site regardless of how long any individual site took to traverse.")
EDGE = held(B, "Registered edge: fill F >= 0.30 is 'not nearly empty'. Human lineage, empty start, N_e 57,143:")
TAB = held(B, "| D, delivered share (Day's own mu L integral of F, Q34) | 0.256 (6.3 My: 0.242) |")
TAK = held(B, "| Takahata N_e = 1e5 held for the whole lineage | F 0.281 |")
W2 = held(B, "| HL's 2 My window (l.416 'entire lineage') | F 0.025 (D 0.003) |")
F65 = held(B, "| 0.697 (6.3 My: 0.676); 2.25x the edge |")

NE = (4 * 100_000 - 2) / 7                               # Wright, census 1e5, Vk = 5 (M-203, M-205)
near(NE, 57_142.6, 0.1)
EDGE_F = 0.30
T65, T63, T2 = 6.5e6 / 25, 6.3e6 / 25, 2.0e6 / 25
assert (T65, T63, T2) == (260_000, 252_000, 80_000)

r = {
    "F_6.5My": fill(T65, NE), "F_6.3My": fill(T63, NE),
    "D_6.5My": delivered(T65, NE), "D_6.3My": delivered(T63, NE),
    "F_Takahata_1e5_6.5My": fill(T65, 1e5), "D_Takahata_1e5_6.5My": delivered(T65, 1e5),
    "F_2My": fill(T2, NE), "D_2My": delivered(T2, NE),
}
near(r["F_6.5My"], 0.697, 0.0005)
near(r["F_6.3My"], 0.676, 0.0005)
near(r["F_6.5My"] / EDGE_F, 2.32, 0.01)                  # claim file "2.25x the edge" (0.676/0.30 = 2.25)
near(r["F_6.3My"] / EDGE_F, 2.25, 0.005)
near(r["D_6.5My"], 0.256, 0.0005)
near(r["D_6.3My"], 0.242, 0.0005)
near(r["F_Takahata_1e5_6.5My"], 0.281, 0.0005)
near(r["D_Takahata_1e5_6.5My"], 0.065, 0.0005)
near(r["F_2My"], 0.025, 0.001)
near(r["D_2My"], 0.003, 0.0005)
assert r["F_6.5My"] > EDGE_F and r["F_6.3My"] > EDGE_F   # lineage window: not nearly empty
assert r["F_Takahata_1e5_6.5My"] < EDGE_F                # just under the edge
assert r["F_2My"] < EDGE_F and r["D_6.5My"] < EDGE_F     # 2 My window and delivered share: under the edge
# steady state (full pipe) delivers mu per generation regardless of transit time
near(fill(1e9, NE), 1.0, 1e-12)

finish({
    "object": "M-207",
    "inputs": [
        {"name": "Day: pipe never fills; channel shuts in the lineage duration", "cite": "Q157 (B q3)"},
        {"name": "Day: 'the pipeline cannot fill' after conceding throughput", "cite": "B2d q3, B2d q1 (Q146)"},
        {"name": "Ne", "value": g(NE), "cite": "Wright (4N-2)/(Vk+2), census 1e5, Vk 5 (claim file B1d; M-203)"},
        {"name": "windows", "value": {"6.5My": T65, "6.3My": T63, "2My": T2}, "cite": "HL l.249 lineage 6.5 My, l.416 2 My (claim file B); 25 y per generation"},
        {"name": "Takahata Ne", "value": 1e5, "cite": "parameters population.Ne_histories.takahata_1995 (human lineage >4.6 My ago ~1e5)"},
        {"name": "edge", "value": EDGE_F, "cite": "claim file B, R4 RHclose registered edge"},
    ],
    "values": {k: g(v) for k, v in r.items()},
    "positions": {
        "day": {"reading": "same window, no fill: the 2 My window or the delivered share",
                "F_2My": g(r["F_2My"]), "D_6.5My": g(r["D_6.5My"]), "F_Takahata_1e5": g(r["F_Takahata_1e5_6.5My"]),
                "all_under_edge": True},
        "critic": {"reading": "fill over HL's own 6.5 My lineage window",
                   "F_6.5My": g(r["F_6.5My"]), "F_6.3My": g(r["F_6.3My"]), "over_edge": True,
                   "note": "both numbers assume an empty start; any pre-split fill raises them (start state is M-202)"},
    },
    "notes": "Every RHclose reading reproduces from the diffusion law. On the 6.5 My lineage window the pipe is ~70% "
             "filled (2.3x the 0.30 edge); on HL's 2 My window it is 2.5% filled; the delivered share over 6.5 My is "
             "26%; Takahata's 1e5 throughout gives 0.28. Which reading the quote takes is rule RD (claim file B); the "
             "arithmetic of each is fixed here.",
})
