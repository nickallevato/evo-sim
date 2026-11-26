#!/usr/bin/env python3
"""M-203 record (lookup): mean neutral fixation time 4 Ne and Day's pipe lengths 228,000 and 29 billion.

Object: docs/research/math/objects.yaml M-203 (parameter, lookup). The value 4 Ne is quoted from
Kimura & Ohta 1969 (B7b q1). Day's two applications (blog 2026-10-01 para 31, B1d q2 and q3) are
recomputed: 228,000 reproduces with Wright's Ne = (4N - 2)/(Vk + 2) at Vk = 5 (HL Table 1, claim file
B1d); 29 billion does not reproduce at the same Ne/N. The record also gives T/4Ne for the 252,000-
generation window at the Ne values in play (justatest90's condition, B5f q2). Inputs carry their
quote id, claim file or parameters.yaml key; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-203.py [--write]
Without --write it checks that M-203.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QL = "docs/research/sources/quotes-literature.md"
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"


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


def wright(n, vk):
    return (4 * n - 2) / (vk + 2)


# ---- inputs -------------------------------------------------------------------------------
KO15 = held(QL, "a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation "
                "in a population of effective size Ne.")                       # B7b q1, K&O 1969 p.770
KO_NN = held(CL + "B7b-kimura-ohta-1969-4ne-and-fraction-1-over-2n.md",
             "Since the ratio Ne/N is around 0.8 in man (CROW 1954)")         # B7b q3
D228 = held(CL + "B1d-full-but-short-pipe-revision.md",
            "Back then, at the ancestral census of ~100,000, the pipe was 4Nₑ ≈ 228,000 generations long.")  # B1d q2
D29B = held(CL + "B1d-full-but-short-pipe-revision.md", "At census 8 billion, it’s 29 billion generations long.")  # B1d q3
VK5 = held(CL + "B1d-full-but-short-pipe-revision.md", "human Vₖ = 5 in its Table 1")
D228F = held(CL + "B1d-full-but-short-pipe-revision.md",
             "At the time of the CHLCA split, we can assume that it was full and 228,000 generations long")  # Q160
JT = held(CL + "B5f-reddit-9-7-million-haploid.md", "It needs the elapsed time to be long compared with the fixation time.")
JT_RANGE = held(CL + "B5f-reddit-9-7-million-haploid.md", "(\"40,000–132,000 generations\")")
PY_B1D = held(PY, "day_b1d_implied: {value: 5.7e4")
PY_YOO = held(PY, "yoo_2025_HCB: {value: 1.98e5")
PY_NE = held(PY, "Ne_modern_human: {value: 1.0e4")

# ---- Day's 228,000 at census 100,000 (Vk = 5) ----------------------------------------------
ne_anc = wright(100_000, 5)
near(ne_anc, 57_142.6, 0.1)
pipe_anc = 4 * ne_anc
near(pipe_anc, 228_570, 1)
assert abs(pipe_anc - 228_000) / 228_000 < 0.003        # stated 228,000 is 0.25% below: rounding
ratio = ne_anc / 100_000
near(ratio, 0.5714, 0.0001)
near(4 * wright(1_000_000, 5), 2_285_714, 1)            # "2.28 million" at census 1e6 (B1d audit)

# ---- Day's 29 billion at census 8e9 ---------------------------------------------------------
pipe_same_ratio = 4 * wright(8e9, 5)
near(pipe_same_ratio, 1.8286e10, 0.0001e10)             # same Ne/N gives 1.83e10
gap = 29e9 / pipe_same_ratio
near(gap, 1.586, 0.001)                                 # stated figure is 1.59x the same-ratio value
ne_needed = 29e9 / 4
near(ne_needed / 8e9, 0.906, 0.001)                     # 29 billion needs Ne ~ 0.91 N
pipe_ko = 4 * 0.8 * 8e9                                  # K&O's Ne/N = 0.8 in man, for comparison
near(pipe_ko, 2.56e10, 1)
near(29e9 / pipe_ko, 1.133, 0.001)

# ---- elapsed time against 4 Ne (justatest90's condition) -------------------------------------
T = 252_000
win = {ne: T / (4 * ne) for ne in (10_000, 33_000, 57_143, 198_000)}
near(win[10_000], 6.3, 1e-9)
assert 4 * 10_000 == 40_000 and 4 * 33_000 == 132_000   # justatest90's 40,000-132,000
near(win[33_000], 1.909, 0.001)
near(win[57_143], 1.1025, 0.0001)                        # Day's ancestral pipe vs the window
near(win[198_000], 0.318, 0.001)                         # Yoo HCB Ne: window shorter than 4Ne
assert T - 228_000 == 24_000

finish({
    "object": "M-203",
    "inputs": [
        {"name": "mean conditional fixation time", "value": "4 Ne", "cite": "B7b q1 (Kimura & Ohta 1969 p.770, Eq. 15); quotes-literature KimuraOhta1969"},
        {"name": "K&O Ne/N in man", "value": 0.8, "cite": "B7b q3"},
        {"name": "Day ancestral pipe", "value": "census ~100,000, 4Ne ~ 228,000", "cite": "B1d q2 (blog 2026-10-01 para 31); Q160"},
        {"name": "Day modern pipe", "value": "census 8e9, 29 billion", "cite": "B1d q3 (para 31)"},
        {"name": "Vk", "value": 5, "cite": "claim file B1d audit (Z22129121 Table 1)"},
        {"name": "Ne values for T/4Ne", "value": [1e4, 3.3e4, 57_143, 1.98e5], "cite": "parameters population.Ne_modern_human, Ne_ancestral_hc.day_b1d_implied, yoo_2025_HCB; B5f (justatest90 40,000-132,000)"},
    ],
    "values": {
        "Ne_anc_vk5": g(ne_anc), "pipe_anc": g(pipe_anc), "Ne_over_N": g(ratio),
        "pipe_8e9_same_ratio": g(pipe_same_ratio), "stated_29e9_over_same_ratio": g(gap),
        "Ne_over_N_needed_for_29e9": g(ne_needed / 8e9), "pipe_8e9_KO_0.8": pipe_ko,
        "T_over_4Ne": {str(k): g(v) for k, v in win.items()},
    },
    "positions": {
        "day": {"pipe_anc": 228_000, "reproduces_with_vk5": True, "pipe_8e9_stated": 29e9,
                "reproduces_same_ratio": False},
        "critic": {"4Ne_accepted": True, "pipe_8e9_same_ratio": g(pipe_same_ratio),
                   "window_long_vs_4Ne_only_if_Ne_small": {"Ne_1e4": 6.3, "Ne_1.98e5": g(win[198_000])}},
    },
    "notes": "4 Ne is the textbook mean (both sides accept it). 228,000 reproduces (Vk = 5 is an implicit input). "
             "29 billion is 1.59x the value at the same Ne/N and needs Ne = 0.91 N; K&O's 0.8 would give 2.56e10. "
             "The 252,000-generation window is long against 4Ne only for Ne near 1e4.",
})
