#!/usr/bin/env python3
"""M-217 record: clock recalibration t_actual = t_clock x 2 / [(Nh/Ne,h) + (Nc/Ne,c)] (eq. 7).

Object: docs/research/math/objects.yaml M-217 (formula, derivation). The record recomputes Table 2 of
Z18525547 (200-580 kya for a 6-7 My clock; 200-360 kya "most plausible"), the 68 kya of Z18637333 at
census 600,000 and its 130-330 kya alternative, the 6.5e6/68e3 = 95.6x compression, and what eq. 7
would need for Day's later 250 kya-1.3 Mya (Q68; no computation in the held post). Under the critic
reading (supply and fixation in the same N, M-209) every N/Ne factor is 1 and t_actual = t_clock.
The Yoo-Ne reading in claim file B4 is included. Inputs carry their quote id or claim file; held()
checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-217.py [--write]
Without --write it checks that M-217.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QD = "docs/research/sources/quotes-day.md"
PY = "docs/research/parameters.yaml"
B4 = CL + "B4-clock-recalibration-200-580-kya.md"
B4B = CL + "B4b-chlca-68-kya.md"


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


def eq7(t_clock, nh, neh, nc, nec):
    return t_clock * 2 / (nh / neh + nc / nec)


# ---- inputs -------------------------------------------------------------------------------
EQ = held(B4, "t_{actual} = t_{clock} × 2 / [(N_{h}/N_{e,h}) + (N_{c}/N_{e,c})]          (7)")
ABS = held(B4, "The consensus molecular clock estimate of 6–7 Mya collapses to 200–580 kya, with the most plausible "
               "demographic parameters yielding 200–360 kya.")
INP = held(B4, "Inputs: Nₑ,h = 3,300 (aDNA drift variance, branch C), Nₑ,c = 33,000 (F_ST across chimp subspecies), "
               "census N_h ∈ {50k, 100k}, N_c ∈ {300k, 1M}.")
K68 = held(B4B, "At the midpoint of 600,000, the consensus molecular clock date of 6.5 Mya compresses to 68 kya.")
K68IN = held(B4B, "N_h = 600,000 (Biraben 2003), N_c = 300,000, Nₑ,h = 3,300, Nₑ,c = 33,000")
ALT = held(B4B, "Alternate census 100–300k: 330–130 kya ✓ (paper \"130–330 kya\")")
Q68 = held(QD, "the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed.")
NOCALC = held(CL + "B4c-chlca-250-kya-to-1-3-mya.md", "The harvested post gives no computation for 250 kya–1.3 Mya.")
YOO = held(B4, "With Yoo 2025 ancestral Nₑ (198,000 / 132,000) and census 100,000 the ratio is 0.51 / 0.76 per lineage "
               "and Eq. (7) gives 12.5 / 8.3 My (older, not younger) for a 6.3 My clock.")
PY_Y = held(PY, "yoo_2025_HCB: {value: 1.98e5")

NEH, NEC = 3_300, 33_000

# ---- Table 2 (Z18525547) ----------------------------------------------------------------------
table = {(100_000, 300_000): (305, 355, 457), (100_000, 1_000_000): (198, 231, 297),
         (50_000, 300_000): (494, 577, 741), (50_000, 1_000_000): (264, 308, 396)}
got = {}
for (nh, nc), printed in table.items():
    vals = tuple(eq7(t, nh, NEH, nc, NEC) / 1e3 for t in (6e6, 7e6, 9e6))
    got[f"{nh}/{nc}"] = [round(v) for v in vals]
    for v, p in zip(vals, printed):
        near(v, p, 1.5)                                  # kya; (50k,300k) 6 My is 495.0 exact, paper 494 (rounded ratios)
near(100_000 / NEH, 30.30, 0.01)
near(300_000 / NEC, 9.09, 0.01)
six_seven = [v for (nh, nc) in table for v in (eq7(6e6, nh, NEH, nc, NEC), eq7(7e6, nh, NEH, nc, NEC))]
near(min(six_seven) / 1e3, 198, 0.6)                    # "200-580 kya" = 6-7 My columns, min 198
near(max(six_seven) / 1e3, 577, 0.6)                    #                               max 577
plaus = [eq7(t, 100_000, NEH, nc, NEC) / 1e3 for nc in (300_000, 1_000_000) for t in (6e6, 7e6)]
near(min(plaus), 198, 0.6)                              # "most plausible 200-360": census N_h = 100k rows
near(max(plaus), 355, 0.6)

# ---- Z18637333: census 600,000 -------------------------------------------------------------------
t68 = eq7(6.5e6, 600_000, NEH, 300_000, NEC)
near(600_000 / NEH, 181.8, 0.1)
near(t68, 68_100, 50)                                   # 68 kya
near(6.5e6 / 68e3, 95.59, 0.01)                         # compression 95.6x
alt = [eq7(6.5e6, nh, NEH, 300_000, NEC) for nh in (100_000, 300_000)]
near(alt[0], 330_000, 1_500)
near(alt[1], 130_000, 1_500)

# ---- Day 2026-05-07: 250 kya-1.3 Mya from 6.3 My (no computation held) ------------------------------
need = {"250kya": 2 * 6.3e6 / 250e3, "1.3Mya": 2 * 6.3e6 / 1.3e6}
near(need["250kya"], 50.4, 1e-9)                        # sum of N/Ne factors eq. 7 would need
near(need["1.3Mya"], 9.69, 0.01)

# ---- critic: same N in supply and fixation, every factor is 1 ---------------------------------------
for t in (6e6, 6.3e6, 6.5e6, 7e6):
    assert eq7(t, 1, 1, 1, 1) == t
# ---- Yoo ancestral Ne at census 100,000 (claim file B4) ----------------------------------------------
yoo = {ne: eq7(6.3e6, 100_000, ne, 100_000, ne) for ne in (198_000, 132_000)}
near(yoo[198_000], 12.47e6, 0.01e6)
near(yoo[132_000], 8.32e6, 0.01e6)

finish({
    "object": "M-217",
    "inputs": [
        {"name": "eq. 7", "cite": "B4 q2 (Z18525547 para 141)"},
        {"name": "Ne,h, Ne,c, census grid", "value": {"Ne_h": NEH, "Ne_c": NEC, "N_h": [50_000, 100_000], "N_c": [300_000, 1_000_000]}, "cite": "claim file B4 (Z18525547)"},
        {"name": "outputs", "value": "200-580 kya; 200-360 most plausible", "cite": "B4 q1"},
        {"name": "census 600,000 -> 68 kya", "cite": "B4b q2; claim file B4b (Biraben 2003)"},
        {"name": "later range", "value": "250 kya-1.3 Mya", "cite": "Q68 (B4c q1); claim file B4c: no computation in the post"},
        {"name": "Yoo ancestral Ne", "value": [198_000, 132_000], "cite": "parameters population.Ne_ancestral_hc.yoo_2025_HCB/HCG; claim file B4"},
    ],
    "values": {
        "table2_kya": got, "range_6_7My_kya": [g(min(six_seven) / 1e3), g(max(six_seven) / 1e3)],
        "census_600k_kya": g(t68 / 1e3), "compression": g(6.5e6 / 68e3),
        "census_100k_300k_kya": [g(a / 1e3) for a in alt],
        "factor_sum_needed_for_250kya_1.3Mya": [g(need["250kya"]), g(need["1.3Mya"])],
        "yoo_Ne_My": {str(k): g(v / 1e6) for k, v in yoo.items()},
    },
    "positions": {
        "day": {"reading": "supply uses census N, so the clock date shrinks by the mean N/Ne",
                "range_kya": [198, 577], "census_600k_kya": g(t68 / 1e3)},
        "critic": {"reading": "with the cancellation (M-209) every N/Ne factor is 1 and t_actual = t_clock",
                   "t_actual_for_6.3My": 6.3e6,
                   "yoo_Ne_reading_My": {str(k): g(v / 1e6) for k, v in yoo.items()}},
    },
    "notes": "Table 2, the 68 kya and the 130-330 kya alternative all reproduce from the stated inputs. The 250 kya-"
             "1.3 Mya revision has no held computation; eq. 7 would need factor sums 9.7-50.4. The recalibration "
             "rests on M-209: with the same N in supply and fixation it returns the clock date unchanged, and with "
             "Yoo's ancestral Ne at census 1e5 it gives older dates (8.3-12.5 My).",
})
