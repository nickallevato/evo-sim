#!/usr/bin/env python3
"""M-019 record (model-choice): all-fixations model against adaptive-only model for sweeps.

Object: docs/research/math/objects.yaml M-019 (model-choice, derivation). Day counts every
required fixation as carried by a sweep (3,200 to 32,000 linkage blocks in humans, 326,000 loci
in bonobos); critics count only the adaptive K_a as sweeps. The record fixes the arithmetic of
Day's counts and of the sweep load each model implies, side by side. The critics' position has
no number to compute: no held source states K_a for the human or bonobo lineage. The statement
claims no K_a value, so the object is resolved, not blocked.

Run: research/.venv/bin/python -I docs/research/math/records/M-019.py [--write]
Without --write it checks that M-019.json is current; --write saves it.
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


A6 = CL + "A6-sweep-signatures-absent.md"
A6A = CL + "A6a-bonobo-sweep-mosaic.md"
BLOCKS = held(A6, "The human genome of 3.2 Gb therefore contains 3,200–32,000 independent linkage blocks. If every sweep "
                  "fixed all variants in its block, 3,200–32,000 independent sweeps would be required")
PERBLK = held(A6, "\"each block must accumulate ~2,000 fixed differences on average\", l.322")
Q_A6_2 = held(A6, "The human genome does not display these signatures at the required scale.")    # A6 q2
Q12 = held(QD, "~20 million fixations required on human lineage")
BON = held(A6A, "Required fixations (bonobo lineage) = 326,000 (10% of 3,263,686 private alleles, l.71)")
Q_A6A_1 = held(A6A, "If 326,000 loci fixed by selection in bonobos over 930,000 years")              # A6a q1
HERN = held(A6, "Hernandez's trough test supports the premise that classic sweeps were rare (< 10% of human-specific "
                "amino-acid substitutions strongly favoured)")
Q132 = held(QD, "Subtracting from the clone-pair total of 56.0 fixations yields approximately 35.5 beneficial fixations")

# ---- Day: every fixation is sweep-carried (blocks swept whole) ------------------------------
L_h = 3.2e9
blk = (3_200, 32_000)
assert L_h / blk[0] == 1e6 and L_h / blk[1] == 1e5    # block sizes 1 Mb to 100 kb
R_h = 20e6
per_sweep = [R_h / k for k in blk]
assert per_sweep == [6_250, 625]                        # fixed differences per sweep (claim file A6 prints "600–6,250")
near(R_h / 2_000, 10_000, 1e-9)                         # Day's "~2,000 per block" implies about 10,000 blocks
K_b = 0.10 * 3_263_686
near(K_b, 326_000, 400)                                 # 326,368.6, printed 326,000

# ---- critics: only the adaptive K_a are sweeps; the rest need none ---------------------------
# No held source gives K_a for the human or bonobo lineage, so no count is computed.
# Day's own LTEE split (s4.3) is the only held adaptive share, for E. coli, not for apes:
ltee_adaptive_share = 35.5 / 56.0
near(ltee_adaptive_share, 0.634, 0.0005)
assert 56.0 - 35.5 == 20.5

finish({
    "object": "M-019",
    "inputs": [
        {"name": "human block range and genome length", "value": [3_200, 32_000, 3.2e9], "cite": "claim file A6 (Z18452504 l.318)"},
        {"name": "human required fixations", "value": 20e6, "cite": "Q12"},
        {"name": "Day's per-block figure", "value": "~2,000", "cite": "claim file A6 (Z18452504 l.322)"},
        {"name": "bonobo required fixations", "value": "10% of 3,263,686", "cite": "claim file A6a (Z18441321 l.71); A6a q1"},
        {"name": "rarity of classic sweeps (Hernandez 2011)", "value": "< 10% of human-specific amino-acid substitutions", "cite": "claim file A6 (R4 GAP-02)"},
        {"name": "LTEE beneficial share (Day s4.3)", "value": [35.5, 56.0], "cite": "Q132"},
    ],
    "values": {
        "block_size_bp": [1e6, 1e5], "fixations_per_sweep_human": per_sweep, "blocks_implied_by_2000_per_block": 10_000,
        "bonobo_required": g(K_b), "ltee_adaptive_share_day_s4.3": g(ltee_adaptive_share),
    },
    "positions": {
        "day": {"model": "all required fixations are sweeps (hitchhikers included)", "sweeps_human": list(blk),
                "sweeps_bonobo": g(K_b), "fixations_per_sweep_human": per_sweep},
        "critic": {"model": "only adaptive fixations K_a pass through sweeps; neutral fixations need no sweep",
                   "number": None,
                   "why_none": "no held source states K_a for the human or bonobo lineage; the statement claims no K_a value"},
    },
    "notes": "Under either model the sweep count is the K fed to M-018 (E_detect = K x W / T): K = 3,200-32,000 or "
             "326,000 under Day's model, K_a <= K under the critics'. Claim file A6 prints 20M/32,000 as '600'; it is 625.",
})
