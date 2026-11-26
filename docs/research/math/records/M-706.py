#!/usr/bin/env python3
"""M-706 record (derivation, structural): serial against aggregate reading of the fixation count.

Object: docs/research/math/objects.yaml M-706 (inference, derivation). Serial: N_fix(T) = T / t_fix, t_fix the time
for one allele to arise and fix (Hancock, GG-01). Aggregate: N_fix(T) = T / G_f, G_f = T_obs / n_obs, a measured
throughput (Day, G1 q1). The record models fixations as intervals of length t_fix started every D generations and
counts them exactly on rationals at three test points: back-to-back (D = t_fix), overlapping (D = t_fix/3) and gapped
(D = 2 t_fix). G_f tends to D, so the readings coincide only when D = t_fix: with overlap the aggregate count exceeds
the serial one by the mean concurrency t_fix/D, and N_fix = T/G_f is then not a serial calculation. p^n is a function
of (p, n) only and has the same value under every schedule (M-703), so a serial reading adds nothing to the Bernoulli
arithmetic; the serial step is the Appendix A chain (G2g). Day's own concession (G2g q2) that the all-cause rate is
faster than a sequential rate is the overlapping case. Arithmetic in claim file G2 (252,000 divided by 1,400, 66,000,
20,000, 27,600) and the LTEE G_f = 60,000/45.4 = 1,322 is asserted. Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-706.py [--write]
Without --write it checks that M-706.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G1 = CL + "G1-average-rate-includes-parallelism.md"
G2 = CL + "G2-serial-critique-hancock.md"
G2A = CL + "G2a-marathon-analogy.md"
G2D = CL + "G2d-camestros-wording-reads-serial.md"
G2E = CL + "G2e-myers-massively-parallel.md"
G2F = CL + "G2f-bowers-serial-lottery.md"
G2G = CL + "G2g-appendix-a-fixation-must-be-sequential.md"
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


# ---- the source sentences ---------------------------------------------------------------------------
GG01 = held(G2, "it assumes that each mutation has to both arise and go to fixation before the next mutation can occur.")
FORMS = held(G2, "Serial reading: N_fix(T) = T / t_fix where t_fix is the time for one allele to fix. Aggregate "
                 "reading: N_fix(T) = T/G_f, G_f = observed T/n. The two coincide only if fixations do not overlap.")
G2_NUM = held(G2, "252,000/1,400 = 180 (Duffy, DeDzjang); 252,000/66,000 = 3.8 and 252,000/20,000 = 12.6, the \"4–13 "
                  "neutral fixations\" in Z23003785 s8.2 (a time/fixation-time division for drift); 252,000/27,600 = 9.1 (A5e).")
LANDS = held(G2, "p^n is timing-independent, so a serial reading adds nothing to the Bernoulli arithmetic; the critique "
                 "lands on the Appendix A chain (G2g), not on G_f (G1).")
DAY_G1 = held(G1, "The 1,322 gen/fix rate is not a sequential rate that needs to be divided by a parallelism factor. It "
                  "is the total throughput, the net output after parallel fixation, clonal interference, sweep "
                  "displacement, and every other concurrent dynamic has played out.")      # G1 q1 (Z23003785 s8.1)
LTEE = held(G1, "the per-population G_f = 60,000/45.4 = 1,322 applied to one lineage")
APPA = held(G2G, "Therefore fixation must be sequential.")                                  # G2g q1 (Appendix A as quoted)
CONC = held(G2G, "Now, perhaps I could have worded it better, but the statement is nevertheless correct because the "
                 "all-cause rate is obviously faster than a sequential rate.")              # G2g q2 (para 25)
PAR22 = held(G2G, "\"MITTENS … specifically includes and incorporates parallel fixation, with my subsequent disproofs "
                  "of parallel fixation.\"")                                                # G2g para 22
DZ01 = held(G2A, "Of course you say that's not possible, they run parallel. Well, the same goes with mutation and fixation.")
CA05 = held(G2D, "“Generations per fixation” reads as if he means each fixation must occur one at a time.")
PZ01 = held(G2E, "Evolution is a property of populations and involves massively parallel action on multiple traits "
                 "and individuals at once.")
PZ05 = held(G2E, "he thinks evolution is a simple serial process (the same thing Zach Hancock pointed out)")
BO02 = held(G2F, "Treating it like a serial lottery is a category error.")
T_HUM = 252_000; held(PY, "day_2026: {value: 252000, source: Z23003785")    # generations_available.day_2026
GF_3 = 1_322; held(PY, "day_mittens3_nonmutator: {value: 1322")             # ltee.gens_per_fixation


def schedule(t_fix, spacing, window):
    """Fixations as intervals [i*spacing, i*spacing + t_fix]; count those complete in [0, window], peak overlap."""
    n = math.floor((window - t_fix) / spacing) + 1
    peak = max(sum(1 for j in range(n) if j * spacing <= x < j * spacing + t_fix)
               for x in [i * spacing for i in range(n)])
    return n, peak


# ---- the identity at three test points (exact) ------------------------------------------------------------
T_FIX, WINDOW = Fr(1_000), Fr(60_000)
pts = {}
for label, spacing in (("back_to_back", T_FIX), ("overlap_x3", T_FIX / 3), ("gapped_x2", 2 * T_FIX)):
    n, peak = schedule(T_FIX, spacing, WINDOW)
    gf = WINDOW / n
    serial, aggregate = WINDOW / T_FIX, WINDOW / gf               # both read over the same window
    pts[label] = {"spacing": float(spacing), "n_obs": n, "G_f": float(gf), "peak_overlap": peak,
                  "serial": float(serial), "aggregate": n}
    assert aggregate == n
    if label == "back_to_back":
        assert peak == 1 and gf == T_FIX and serial == aggregate == 60    # coincide: no overlap
    if label == "overlap_x3":
        assert peak == 3 and gf < T_FIX and aggregate > serial          # overlap: aggregate exceeds serial
        near(aggregate / serial, 3, 0.05)                               # by the mean concurrency t_fix / spacing
    if label == "gapped_x2":
        assert peak == 1 and gf > T_FIX and aggregate < serial          # no overlap but gaps: serial overstates
# coincidence needs G_f = t_fix: with overlap G_f < t_fix, so "coincide => no overlap" (G2's "only if")
assert all(p["G_f"] == float(T_FIX) for p in pts.values() if p["serial"] == p["aggregate"])

# ---- p^n has no schedule term (M-703) -------------------------------------------------------------------
pn = lambda p, n: p ** n
assert pn(Fr(1, 50), pts["back_to_back"]["n_obs"]) == pn(Fr(1, 50), 60)        # same (p, n), any schedule
assert pn.__code__.co_varnames == ("p", "n")                      # no T, t_fix or spacing argument

# ---- Day's concession: an all-cause rate faster than a sequential one is the overlapping case -------------
rate_all, rate_seq = 1 / Fr(pts["overlap_x3"]["G_f"]), 1 / T_FIX
assert rate_all > rate_seq and "faster than a sequential rate" in CONC

# ---- the arithmetic in G2 and the LTEE throughput --------------------------------------------------------
assert T_HUM / 1_400 == 180
near(T_HUM / 66_000, 3.8, 0.05); near(T_HUM / 20_000, 12.6, 1e-9); near(T_HUM / 27_600, 9.1, 0.05)
near(60_000 / 45.4, GF_3, 0.5)                                    # G_f = T_obs / n_obs (Z23003785)
near(T_HUM / GF_3, 190.6, 0.05)

finish({
    "object": "M-706",
    "inputs": [
        {"name": "serial and aggregate forms", "value": ["T / t_fix", "T / G_f, G_f = T_obs / n_obs"], "cite": "G2 formal statement; GG-01 (G2 q1)"},
        {"name": "test schedule", "value": {"t_fix": 1000, "window": 60000, "spacings": [1000, "1000/3", 2000]}, "cite": "constructed test points"},
        {"name": "human generations; LTEE G_f", "value": [T_HUM, GF_3], "cite": "parameters generations_available.day_2026, ltee.gens_per_fixation.day_mittens3_nonmutator; G1"},
    ],
    "values": {
        "test_points": pts,
        "G2_arithmetic": {"252000/1400": 180, "252000/66000": round(T_HUM / 66_000, 2), "252000/20000": 12.6,
                          "252000/27600": round(T_HUM / 27_600, 2), "252000/1322": round(T_HUM / GF_3, 1),
                          "60000/45.4": round(60_000 / 45.4, 1)},
    },
    "positions": {
        "day": {"reading": "G_f is a measured throughput that already includes parallel fixation (G1 q1)",
                "holds": "on that reading T/G_f is the aggregate form and no parallelism factor is owed; the identity "
                         "shows such a G_f is shorter than the per-allele time when sweeps overlap"},
        "critic": {"reading": "dividing a window by a per-allele time assumes each fixation ends before the next starts",
                   "holds": "the two forms coincide only with no overlap; the critique holds against the Appendix A "
                            "'fixation must be sequential' chain (G2g), which Day's para 25 concedes is not purely serial"},
    },
    "notes": "Structural, exact on rationals. Over a window, G_f equals the start spacing; the serial and aggregate counts "
             "coincide only when it equals t_fix (back to back). Overlap makes the aggregate count larger by the mean "
             "concurrency, gaps make it smaller. p^n depends on (p, n) only (M-703), so neither reading changes it. "
             "The sources differ in target: Hancock (GG-01), Ghijselen (DZ-01), Camestros (CA-05), Myers (PZ-01, "
             "PZ-05) and Bowers (BO-02) are scored against the Appendix A chain or the 'generations per fixation' "
             "wording, not against T/G_f read as a throughput. The 66,000 and 20,000 divisions (Z23003785 s8.2) are "
             "drift fixation times, so those two are serial readings in Day's own text.",
})
