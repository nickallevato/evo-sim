#!/usr/bin/env python3
"""M-007 record (identity): mutation-supply arithmetic between E. coli and humans.

Object: docs/research/math/objects.yaml M-007 (identity, derivation). Genome ratio (McCarthy),
per-site and per-genome rate ratios, the KITTENS decomposition (Sparky_6_4), the neutral supply
(Hancock) and Hoessjer's scaling inputs. Each input carries its quote id or claim file; held()
checks each quote verbatim. Every number the statement claims has an assert, including the
printed figures that are off ("roughly 690", "4e-5", 1,075,000 against 1,097,143).

Run: research/.venv/bin/python -I docs/research/math/records/M-007.py [--write]
Without --write it checks that M-007.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
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


# ---- inputs -------------------------------------------------------------------------------
MC05 = held(CL + "A5-genome-size-mutation-supply.md",
            "The human nuclear genome contains approximately 3.1 billion base pairs, roughly 690 times larger than "
            "the compact E. coli genome of about 4.6 million base pairs.")                  # A5 q1
WIEL = held(CL + "A5-genome-size-mutation-supply.md", "Per-site rate ratio 1.2e-8/8.9e-11 = 135 (8.9e-11 is the "
            "Wielgoss 2011 figure via McCarthy; not in the quote files)")
MU_H = held(PY, "pedigree_human: {value: 1.2e-8")
Q132 = held(QD, "neutral hitchhikers ≈ 4.1 × 10⁻⁴ × 50,000 = 20.5")
Q135 = held(QD, "(3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100)")
SP1 = held(CL + "A5b-kittens-94000x11p7.md", "The claimed shortfall is 94,000 × 11.7, or about 1.1 million.")  # A5b q1
Q14 = held(QD, "the shortfall is 1,075,000-fold for non-mutators")
Q16 = held(QD, "17.5 million required fixations on the human lineage")
GG07 = held(CL + "A5c-neutral-supply-ecoli-vs-human.md",
            "you only expect four e to the neg5 mutations to fix per generation.")            # A5c q1
GG08 = held(CL + "A5c-neutral-supply-ecoli-vs-human.md",
            "under neutrality, it should take like 22,000 generations to fix one mutation.")  # A5c q2
HANC = held(CL + "A5c-neutral-supply-ecoli-vs-human.md", "with μ = 1e-11 per site (Hancock) and L = 4.6e6")
HOS = held(CL + "A5a-hossjer-127-15800-10m.md",
           "F' = F_127 · (1.25e-8/1e-10) = 126.6 · 125 = 15,820 (\"15,800\");  F'' = F' · (3e9/4.6e6) = 15,820 · 652 = 10.3e6 vs R = 20e6 (ratio 1.94).")

# ---- genome ratio (McCarthy) -------------------------------------------------------------
L_h, L_E = 3.1e9, 4.6e6
g_ratio = L_h / L_E
assert round(g_ratio) == 674
assert round(L_h / 4.5e6) == 689                       # "roughly 690" follows from a 4.5 Mb genome
near(690 / g_ratio - 1, 0.024, 0.001)                  # 2.4% above his own stated inputs

# ---- per-site and per-genome rate ratios -------------------------------------------------
mu_h, mu_E = 1.2e-8, 8.9e-11
site_ratio = mu_h / mu_E
assert round(site_ratio) == 135
U_h = 3.2e9 * mu_h
near(U_h, 38.4, 1e-9)
U_E = 4.1e-4
kappa = U_h / U_E
assert round(kappa) == 93_659

# ---- KITTENS decomposition (Sparky_6_4) --------------------------------------------------
r_ratio = 205 / 17.5
near(r_ratio, 11.714, 0.0005)
kit = kappa * r_ratio
assert round(kit) == 1_097_143
near(kit / 1_075_000 - 1, 0.0206, 0.0005)             # 2.1% above the paper's 1,075,000
near(94_000 * 11.7, 1.1e6, 0.005e6)                    # "94,000 x 11.7, or about 1.1 million"

# ---- neutral supply in E. coli (Hancock) -------------------------------------------------
neut_h = 4.6e6 * 1e-11
near(neut_h, 4.6e-5, 1e-18)
assert round(1 / neut_h) == 21_739                     # "like 22,000 generations"
near(4e-5 / neut_h, 0.87, 0.005)                       # the spoken "4e-5" is 13% below 4.6e-5
neut_m = 4.6e6 * mu_E
near(neut_m, 4.1e-4, 0.01e-4)                          # 4.094e-4, the 4.1e-4 of MITTENS 3.0 s4.3
assert round(1 / U_E) == 2_439
near(mu_E / 1e-11, 8.9, 1e-9)                          # Hancock's mu is 8.9x below the measured rate

# ---- Hoessjer scaling inputs -------------------------------------------------------------
F127 = 9e6 * 0.45 / (20 * 1600)
mu_scale = 1.25e-8 / 1e-10
assert round(mu_scale) == 125
F1 = F127 * mu_scale
assert round(F1) == 15_820
L_scale = 3e9 / 4.6e6
assert round(L_scale) == 652
F2 = F1 * L_scale
near(F2, 10.3e6, 0.05e6)
near(20e6 / F2, 1.94, 0.005)
F2m = F127 * (1.25e-8 / mu_E) * L_scale                # with the measured E. coli rate
near(1.25e-8 / mu_E, 140, 0.5)
near(F2m, 11.6e6, 0.05e6)
near(20e6 / F2m, 1.7, 0.05)
near(mu_scale * L_scale, 81_500, 50)                   # Hoessjer's total scaling against KITTENS' 93,659

finish({
    "object": "M-007",
    "inputs": [
        {"name": "genome sizes and 'roughly 690'", "value": [3.1e9, 4.6e6, 690], "cite": "A5 q1 (MC-05)"},
        {"name": "per-site rates", "value": [1.2e-8, 8.9e-11], "cite": "parameters mutation.mu_per_site_per_gen.pedigree_human; claim file A5 (Wielgoss 2011 via McCarthy)"},
        {"name": "U_E, U_h factors", "value": [4.1e-4, 3.2e9], "cite": "Q132, Q135; parameters ltee.mu_genome_ancestral"},
        {"name": "KITTENS shortfall", "value": "94,000 x 11.7 = about 1.1 million", "cite": "A5b q1"},
        {"name": "R 205e6, 17.5e6, paper shortfall 1,075,000", "cite": "Q14, Q16"},
        {"name": "Hancock neutral supply", "value": [1e-11, 4.6e6, "4e-5", "22,000"], "cite": "A5c q1 (GG-07), q2 (GG-08); claim file A5c"},
        {"name": "Hoessjer scaling", "value": [1.25e-8, 1e-10, 3e9, 4.6e6], "cite": "claim file A5a formal statement (HO-01, HO-02)"},
    ],
    "values": {
        "genome_ratio": g(g_ratio), "genome_ratio_at_4.5Mb": g(L_h / 4.5e6), "mccarthy_690_over_ratio": g(690 / g_ratio),
        "site_ratio": g(site_ratio), "U_h": g(U_h), "kappa": g(kappa),
        "R_ratio_205_over_17.5": g(r_ratio), "kittens_product": g(kit), "paper_shortfall": 1_075_000,
        "neutral_supply_hancock": g(neut_h), "gens_per_fix_hancock": g(1 / neut_h),
        "neutral_supply_measured": g(neut_m), "gens_per_fix_at_4.1e-4": g(1 / U_E),
        "hoessjer": {"F127": g(F127), "mu_scale": mu_scale, "F_mu": g(F1), "L_scale": g(L_scale), "F_mu_L": g(F2),
                     "gap_to_20e6": g(20e6 / F2), "F_mu_L_measured_mu": g(F2m), "gap_measured_mu": g(20e6 / F2m)},
    },
    "positions": {
        "day": "the formula uses an observed rate, so supply is inside G_f; the LTEE per-genome supply is 4.1e-4 (Day's s4.3)",
        "critic": "the expected fixation rate is set by genome size and mutation rate; per-genome supply ratio 93,659 "
                  "(Hoessjer's version 81,500)",
    },
    "notes": "All identities reproduce; printed rounding: 'roughly 690' (674 on the stated inputs), '4e-5' (4.6e-5), "
             "KITTENS 1,097,143 against the paper's 1,075,000 (2.1%, from F rounded to 190.6).",
})
