#!/usr/bin/env python3
"""M-606 record (lookup): SD of the conditional neutral fixation time, 0.538 x 4Ne.

Object: docs/research/math/objects.yaml M-606 (formula, lookup). Day & Athos (Z22903977 s3, Q294; F5 q1): mean 4Ne
"and a broad distribution around that mean (SD ≈ 0.538 × 4Nₑ under Kimura's diffusion treatment)". The record
computes sqrt(pi^2/3 - 3) = 0.538 (Q294 note) and 0.538 x 4 = 2.15, cross-checks it against the series form of the
same law (the conditional fixation time from p -> 0 has the moments of a sum of independent exponentials with rates
k(k - 1)/2 per 2Ne generations, k >= 2: mean 4Ne, variance (2Ne)^2 x sum 4/(k^2 (k - 1)^2) = (4Ne)^2 (pi^2/3 - 3)),
and quotes the simulated SD of t_fix/N = 2.105 (N = 50) and 2.108 (N = 200) from RESULTS B0.2 (not re-simulated).
"Not in Kimura and Ohta 1969": the fidelity ledger and claim file F5 record that the paper derives the first moment
only; the paper is not in this checkout's sources/raw/, so the record holds that finding, not the paper's text. The
Z22903977 local copy named in Q294 is not in this checkout either; the quote is checked against quotes-day and F5.

Run: research/.venv/bin/python -I docs/research/math/records/M-606.py [--write]
Without --write it checks that M-606.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
F5 = "docs/research/claims/F5-kimura-ohta-sd-not-in-paper.md"
QD = "docs/research/sources/quotes-day.md"
FL = "docs/research/ledgers/fidelity.md"
RES = "research/checks/RESULTS.md"


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
Q1 = "a broad distribution around that mean (SD ≈ 0.538 × 4Nₑ under Kimura's diffusion treatment)"
held(F5, Q1)                                                      # F5 q1, Z22903977 s3 The Empty Pipe
Q294 = held(QD, "The process has a mean length of 4Nₑ generations and a broad distribution around that mean (SD ≈ "
                "0.538 × 4Nₑ under Kimura's diffusion treatment).")  # Q294, s3 para 1 sentence 3
NOTE = held(QD, "0.538 = √(π²/3 − 3) is the value for the exact conditional fixation-time law (audit arithmetic)")
RAW = held(QD, "local copy `sources/raw/refresh-2026-10-13/zenodo-22903977-new/new.txt`")
SIM = held(RES, "| SD of t_fix / N | 2.105, 2.108 | ≈2.15 (diffusion) | — |")   # RESULTS B0 table
SIM_F5 = held(F5, "SD of t_fix/N = 2.105 (N=50) and 2.108 (N=200) vs diffusion ≈ 2.15 (derived consistency)")
MEAN_SIM = [held(RES, "| B0.2 conditional mean t_fix / N, N=50 | 3.908 |"),
            held(RES, "| B0.2 conditional mean t_fix / N, N=200 | 4.006 |")]
KO_SD = held(FL, "| Kimura & Ohta 1969 | SD ≈ 2.15Nₑ (Day) | **not-found in this paper** | Only the first moment is "
                 "derived here; the paper says higher moments can be obtained \"step by step\". The SD figure must come "
                 "from a later source. Our B0.2 simulation gives SD ≈ 2.1N. |")
KO_MEAN = held(FL, "Eq. 15 and Summary: \"takes about 4Nₑ generations until fixation in a population of effective size Nₑ\"")
KO_F5 = held(F5, "| Kimura & Ohta 1969 | Eq. 15: t̄(0) = 4Nₑ; no SD | not-found in this paper (ledger) |")
KO_FILES = held(FL, "All six blocked papers were downloaded by the user into `sources/raw/sources/manual/`")

# ---- the closed form ------------------------------------------------------------------------------
c = math.sqrt(math.pi ** 2 / 3 - 3)
near(c, 0.538, 5e-4)
assert "0.538" in Q1 and "0.538" in Q294
sd_ne = near(4 * c, 2.15, 5e-3)                                   # SD in units of Ne: 2.154
near(4 * 0.538, 2.152, 1e-12)                                     # F5: 0.538 x 4 = 2.152 (rounded c)
cv = c                                                            # SD / mean, since the mean is 4Ne

# ---- series cross-check (same law, written as a sum of exponential phases) -------------------------
K = 200_000
mean_series = sum(2 / (k * (k - 1)) for k in range(2, K))         # in units of 2Ne; -> 2 (mean 4Ne)
var_series = sum(4 / (k * k * (k - 1) ** 2) for k in range(2, K))  # in units of (2Ne)^2
near(mean_series, 2.0, 2e-5)
near(math.sqrt(var_series) / mean_series, c, 1e-5)                # SD / mean = sqrt(pi^2/3 - 3)
near(sum(1 / (k * k * (k - 1) ** 2) for k in range(2, K)), math.pi ** 2 / 3 - 3, 1e-12)

# ---- simulated values (quoted from RESULTS B0.2, not re-simulated) --------------------------------
sims = {50: 2.105, 200: 2.108}
assert "2.105, 2.108" in SIM and "(N=50)" in SIM_F5 and "(N=200)" in SIM_F5
gaps = {n: near(v / sd_ne - 1, -0.02, 0.005) for n, v in sims.items()}   # about 2% below the diffusion value
near(sd_ne - sims[200], 0.046, 0.001)
assert "3.908" in MEAN_SIM[0] and "4.006" in MEAN_SIM[1]

# ---- attribution ----------------------------------------------------------------------------------
assert "not-found in this paper" in KO_SD and "no SD" in KO_F5 and "4Nₑ generations" in KO_MEAN
assert "sources/raw/sources/manual/" in KO_FILES and "zenodo-22903977-new" in RAW   # both absent from this checkout (2026-11-26)

finish({
    "object": "M-606",
    "inputs": [
        {"name": "Day's sentence", "value": Q294, "cite": "Q294 (Z22903977 s3 para 1, sentence 3); F5 q1"},
        {"name": "closed form", "value": "sqrt(pi^2/3 - 3)", "cite": "Q294 note (audit arithmetic)"},
        {"name": "simulated SD of t_fix/N", "value": sims, "cite": "RESULTS B0 table (baseline_textbook.py, seed 20261007); F5 formal statement"},
        {"name": "Kimura & Ohta 1969 content", "value": KO_SD, "cite": "ledgers/fidelity.md; F5 primary-literature table"},
    ],
    "values": {
        "sd_over_4Ne": round(c, 5), "sd_over_Ne": round(sd_ne, 4), "cv": round(cv, 5),
        "series_mean_over_2Ne": round(mean_series, 6), "series_sd_over_mean": round(math.sqrt(var_series) / mean_series, 6),
        "simulated_sd_over_N": sims, "simulated_gap_to_2.154": {str(n): round(g, 4) for n, g in gaps.items()},
        "in_kimura_ohta_1969": "not found (ledger; paper derives the first moment only)",
        "raw_texts_read_by_record": False,
    },
    "positions": {
        "day": {"reading": "mean 4Ne with a broad distribution, SD about 0.538 x 4Ne, under Kimura's diffusion",
                "holds": "0.538 = sqrt(pi^2/3 - 3) is the exact diffusion value; simulation gives 2.105-2.108 against 2.154"},
        "critic": {"reading": "the number reproduces but is not in the cited Kimura & Ohta 1969",
                   "holds": "the ledger finds only the first moment (Eq. 15) there; the count formula needs only the mean"},
    },
    "notes": "The figure is right: SD/mean = sqrt(pi^2/3 - 3) = 0.5384, so SD = 2.154 Ne; the series form of the same law "
             "gives the same ratio, and the B0.2 simulation (2.105, 2.108) sits about 2% below it at N = 50 and 200. "
             "Fidelity concerns the attribution only: 'Kimura's diffusion treatment' is fair as a method, but the cited "
             "Kimura & Ohta 1969 derives the first moment and says higher moments follow 'step by step' (ledger). "
             "Neither Kimura & Ohta 1969 (ledger: sources/raw/sources/manual/) nor the Z22903977 text named in Q294 is "
             "present in this checkout, so the 'not in the paper' finding is the ledger's, held here, not re-read.",
})
