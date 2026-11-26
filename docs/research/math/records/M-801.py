#!/usr/bin/env python3
"""M-801 record (derivation): Haldane's cost budget, 30 N deaths per substitution at 10% selective mortality.

Object: docs/research/math/objects.yaml M-801 (formula, derivation). Cost per substitution C = 30 N selective deaths
(diploid, single new copy), sustainable selective mortality 0.10 N per generation, so the minimum interval is
C / (0.10 N) = 30 / 0.10 = 300 generations per beneficial substitution. N cancels, so the same 300 results with N_e
(Nesslig20, H6). The 300 is held only as Nunney 2003 reports it (Abstract, H2 q2); Haldane 1957 is not retrieved and
is not treated as held. Day (Z18168236, Q47 = H q1), Nesslig20 (H6 q2) and Hossjer (H5 q1) restate the budget; the
limit bounds selected substitutions (H4 q2, H6 q3 = PS-04). The D = 30 input is Haldane's; one new copy at N = 1e4
gives D = 2 ln(2N) = 19.8 (R4 P1, claim file H). Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-801.py [--write]
Without --write it checks that M-801.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H = CL + "H-haldane-limit.md"
H2 = CL + "H2-nunney-2003.md"
H4 = CL + "H4-worden-speed-limit.md"
H5 = CL + "H5-hossjer-cost-step.md"
H6 = CL + "H6-nesslig20-cost-vs-drift.md"
QD = "docs/research/sources/quotes-day.md"
QL = "docs/research/sources/quotes-literature.md"
QC = "docs/research/sources/quotes-critics.md"
PY = "docs/research/parameters.yaml"


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


# ---- inputs ---------------------------------------------------------------------------------------
NUNNEY = ("Based on mutation-selection balance and 10% selective mortality, he suggested that the limit to adaptive "
          "evolution was about one allelic substitution per 300 generations.")
held(H2, NUNNEY); held(QL, NUNNEY); held(H, NUNNEY)                 # H2 q2 (Nunney 2003 Abstract); H primary-lit table
NOT_HELD = held(QL, "**Haldane 1957**: not retrieved. The \"about one allelic substitution per 300 generations\" figure "
                    "is confirmed only as reported in Nunney 2003 (quoted above).")
PARAM = held(PY, "gens_per_substitution: {value: 300, source: Haldane1957, verified: \"via Nunney2003\"}")
Q47 = ("Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300 "
       "generations, based on the reproductive cost each substitution imposes on a population.")
held(H, Q47); held(QD, Q47)                                          # H q1 = Q47 (Z18168236 Abstract)
FORM = held(H, "Haldane: cost per substitution C = 30 N selective deaths (diploid, single new copy); sustainable "
               "selective mortality m = 0.10 N per generation; minimum interval = C/(m N) = 30/0.10 = 300 generations.")
H4Q2 = held(H4, "Haldane’s limit isn’t about purging bad mutations, it is about the cost of substituting good ones. Each "
                "beneficial fixation still requires selective deaths to drive it to fixation.")          # H4 q2 (Day)
H5Q1 = held(H5, "there is a reproductive cost of having many fixations going on in parallel.")          # H5 q1 (Hossjer)
H6Q1 = held(H6, "noted that selection has a limit, since it imposes a reproductive cost.")              # H6 q1
H6Q2 = held(H6, "Haldane argued that a reasonable 10% of the population can be culled per generation.") # H6 q2
PS04 = ("Haldane’s reproductive cost limit does not apply to drift, but can it account for most of the genomic "
        "differences between humans and chimps?")
held(H6, PS04); held(QC, PS04)                                       # H6 q3 = PS-04
H6F = held(H6, "30 N_e/(0.1 N_e) = 30/0.1 = 300 generations per beneficial mutation.")
SCOPE = held(H, "Scope: the quantity bounded is adaptive (selected) substitutions.")
P1 = held(H, "one new copy at N_e = 1e4 gives D = 2 ln(2e4) = 19.8")
COST_D, M_FRAC = 30, Fr(1, 10)
assert "C = 30 N" in FORM and "0.10 N" in FORM and "10% selective mortality" in NUNNEY

# ---- the budget -------------------------------------------------------------------------------------
interval = COST_D / M_FRAC
assert interval == 300                                              # 30 / 0.10 = 300 (exact)
assert "per 300 generations" in NUNNEY and "per 300 generations" in Q47
for n in (1_000, 10_000, 3_300, 10**8):                             # N (or N_e) cancels: C / (m N)
    assert (COST_D * n) / (M_FRAC * n) == 300
rate = 1 / interval
near(float(rate), 0.003333, 5e-7)                                   # 1/300 substitutions per generation
d_new = 2 * math.log(2 * 10_000)                                    # Haldane D for one new copy, N = 1e4
near(d_new, 19.8, 0.05)
near(d_new / M_FRAC, 198, 0.5)                                      # about 200 generations: same order as 300
assert COST_D / d_new > 1                                           # D = 30 is the conservative (slower) input

finish({
    "object": "M-801",
    "inputs": [
        {"name": "cost per substitution D (x N)", "value": COST_D, "cite": "claim file H formal statement (Haldane via Nunney 2003)"},
        {"name": "selective mortality budget", "value": 0.10, "cite": "Nunney 2003 Abstract (H2 q2); H6 q2"},
        {"name": "printed interval", "value": 300, "cite": "Nunney 2003 Abstract (H2 q2); Q47 = H q1; parameters haldane.gens_per_substitution"},
    ],
    "values": {
        "interval_generations": float(interval), "rate_per_generation": round(float(rate), 6),
        "N_cancels": True, "D_new_copy_N_1e4": round(d_new, 2), "interval_at_D_new_copy": round(d_new / float(M_FRAC), 1),
    },
    "positions": {
        "day": {"reading": "10% selective mortality is a total budget, about 1 beneficial substitution per 300 generations for mammals",
                "holds": "30/0.10 = 300 exactly; N cancels; the figure matches Nunney's report of Haldane"},
        "critic": {"reading": "the arithmetic is accepted; it bounds selected substitutions only, under hard selection, not drift",
                   "holds": "the budget is stated in deaths per beneficial substitution, so neutral fixations pay none (PS-04); hard/soft is M-803"},
    },
    "notes": "300 = 30/0.10 holds exactly and is independent of N, so Nesslig20's N_e notation changes nothing. The 300 "
             "is verified only as Nunney 2003 reports Haldane; Haldane 1957 is not retrieved, so the D = 30 and 10% "
             "inputs are Haldane's as relayed. D = 30 is above the new-copy value 2 ln(2N) = 19.8 at N = 1e4 (about "
             "200 generations at 10%), so 300 is the slower end of Haldane's own accounting. Whether the budget binds "
             "(hard vs soft selection, M = 2Ku) is M-803, not this record.",
})
