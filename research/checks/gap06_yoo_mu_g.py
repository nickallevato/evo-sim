"""GAP-06: propagate Yoo 2025's mutation rate and generation times into the numbers that use Day's mu = 1.2e-8 and
g = 25 y.  Low-stakes tier (re-confirmation / bookkeeping; one combined review).  Arithmetic only; run locally.
Run:  research/.venv/bin/python -I research/checks/gap06_yoo_mu_g.py
Pre-registered: committed BEFORE it is run.

SOURCE (refresh-2026-10-10b s2; Yoo D et al. Nature 641:401 (2025) SI Note VI, MOESM1 lines 1456-1478, local
sources/raw/sources/supp/Yoo2025/MOESM1.txt, sha256 979759be...e03c70c; verified by this script as substrings):
  "mutation rate of 1.25×10-8 and the average generation time across the species for specific node:"
  "Homo-Chimp-Bonobo: 24.5 years."   "Homo-Chimp-Gorilla: 21.75 years."   "Human: 25 years"
DAY's INPUTS (claim A1, Z23003785): "The divergence time is 6.3 million years. At 25 years per human generation, this
  provides 252,000 generations."; mu = 1.2e-8 per bp per generation (parameters.yaml mutation.mu_per_site_per_gen).

PROPAGATED QUANTITIES (each with Day's value, Yoo-basis values, and % change):
  A1  N_gen = 6.3e6 / g                                   g in {25 (human), 24.5 (HCB node), 21.75 (HCG node)}
  A   MITTENS F_max = N_gen / G_f (G_f 1,322; d omitted as in 3.0) and the 205 M shortfall 205e6 / F_max
  A3  rate route k = mu: expected per-lineage substitutions mu x L x N_gen (L = 3.1e9); Day's required 20 M and the
      measured 21.05 M (GAP-07b) do not depend on mu or g (count routes)
  B3d k/mu = 205e6 / (mu_B x L x N_gen), mu_B = Bergeron mammal mean 7.97e-9 (Day's input; only N_gen changes);
      sensitivity row: Yoo's own mu in place of Bergeron's (a change of source, not a correction; labelled)
  H   Haldane 1/300 count N_gen / 300, Haldane + d N_gen x 0.45 / 300, Term 3 count 0.0256 x N_gen
  A2e kappa = (3.2e9 x mu) / 4.1e-4; U_total = 3.2e9 x mu; the ~191 threshold N_gen / 1,322
  B4a Ne_anc rescaling Ne' = Ne_Yoo x mu_Yoo / 1.2e-8 (HCB 1.98e5, HCG 1.32e5)
  GAP-05 / B5 neutral expectations scale with mu x N_gen
RULE R1: a change is material only if it moves the author's stated conclusion or a downstream number in the same
  source by > 25%, or flips it.
PREDICTIONS (fixed now)
  Day side: every change is small; no conclusion moves (shortfalls of 1e5-1e6 are untouched).
  Critic side: the same arithmetic; the k = mu route moves toward the counted 21 M but does not close the ~2x gap.
  Audit: G1 every Day-basis number changes by <= 7% on the human (25 y) and HCB (24.5 y) bases (mu +4.2%, N_gen
  +2.0%); the HCG node basis (21.75 y) moves generation-count numbers by +14.9% and the k = mu route by +19.8%, all
  < 25%: no R1 error anywhere.  G2 B3d k/mu falls from 32.9 to 32.3 (24.5 y) and 28.7 (21.75 y); the Bergeron->Yoo mu
  swap row falls to 20.6 (-37%), reported as a source change, not scored.  G3 Ne_anc x1.042.  G4 the 2x tension of
  the k = mu route against the counted divergence (GAP-07b) stays (ratio counted / rate route >= 1.8 on every basis).
"""
import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MOE = os.path.join(ROOT, "sources", "raw", "sources", "supp", "Yoo2025", "MOESM1.txt")
QUOTES = ["mutation rate of 1.25×10-8 and the average generation time across the species for specific node:",
          "Homo-Chimp-Bonobo: 24.5 years.", "Homo-Chimp-Gorilla: 21.75 years.", "Human: 25 years"]


def main():
    b = open(MOE, "rb").read()
    t = re.sub(r"\s+", " ", b.decode("utf-8", "replace"))
    print(f"MOESM1 sha256 {hashlib.sha256(b).hexdigest()}")
    for q in QUOTES:
        print(f"  {'OK  ' if re.sub(r'[ ]+', ' ', q) in t else 'MISS'} {q}")
    L, Tdiv, G, req, meas = 3.1e9, 6.3e6, 1322, 205e6, 21.05e6
    bases = [("Day (1.2e-8, 25 y)", 1.2e-8, 25.0), ("Yoo human (1.25e-8, 25 y)", 1.25e-8, 25.0),
             ("Yoo HCB node (1.25e-8, 24.5 y)", 1.25e-8, 24.5), ("Yoo HCG node (1.25e-8, 21.75 y)", 1.25e-8, 21.75)]
    rows = []
    for name, mu, g in bases:
        N = Tdiv / g
        F = N / G
        rows.append((name, dict(
            N_gen=N, F_max=F, shortfall_205M=req / F, shortfall_20M=20e6 / F,
            k_mu_route=mu * L * N, counted_over_route=meas / (mu * L * N),
            B3d_k_over_mu=req / (7.97e-9 * L * N), B3d_swap_Yoo_mu=req / (mu * L * N),
            Haldane=N / 300, Haldane_d=N * 0.45 / 300, Term3=0.0256 * N,
            kappa=3.2e9 * mu / 4.1e-4, U_total=3.2e9 * mu, thr191=N / G,
            Ne_HCB=1.98e5 * mu / 1.2e-8, Ne_HCG=1.32e5 * mu / 1.2e-8)))
    keys = list(rows[0][1])
    base = rows[0][1]
    print("\n| quantity | " + " | ".join(r[0] for r in rows) + " |")
    print("|---|" + "---|" * len(rows))
    worst = {}
    for k in keys:
        cells = []
        for name, d in rows:
            ch = 100 * (d[k] / base[k] - 1)
            cells.append(f"{d[k]:.4g} ({ch:+.1f}%)")
            if name != rows[0][0] and k != "B3d_swap_Yoo_mu":
                worst[k] = max(worst.get(k, 0), abs(ch))
        print(f"| {k} | " + " | ".join(cells) + " |")
    print("\nB3d_swap_Yoo_mu is a source swap (Yoo mu for Bergeron's), not a correction of Day's input: "
          f"{rows[2][1]['B3d_swap_Yoo_mu']:.2f} vs {base['B3d_k_over_mu']:.2f} "
          f"({100 * (rows[2][1]['B3d_swap_Yoo_mu'] / base['B3d_k_over_mu'] - 1):+.1f}%)")
    print("largest |change| over Yoo bases (excluding the swap row): " +
          ", ".join(f"{k} {v:.1f}%" for k, v in sorted(worst.items(), key=lambda kv: -kv[1])[:6]))
    print(f"R1 (> 25%) triggered by any propagated Day number: {any(v > 25 for v in worst.values())}")


if __name__ == "__main__":
    main()
