"""R4-GAP05 POST HOC sensitivity (answers MAJOR-2 / MINOR-3 of REVIEW-R4-GAP05-combined.md).  Post hoc: written after the
pre-registered run gap05_slightly_deleterious.py (b59f2e5, unchanged) and after seeing its output and the review.
Run: research/.venv/bin/python -I research/checks/gap05_posthoc.py   (local, numpy only, <10 s).  Reading A only
(Boyko 2008 / Kim 2017 Methods: s = heterozygote disadvantage, gamma = 2 N s, additive).  Reuses the pre-registered functions.

Grid: DFE rows (Kim 2017 Table 3): Boyko 1.8e-8; 1000G gamma 1.8e-8; ESP gamma; 1000G gamma 1.5e-8.
  Base mu*T*Nsites multiplier: pre-registered mu=1.2e-8; mu 1.5e-8; mu 1.8e-8 (the DFE's own mu); divergence-calibrated
  k = observed synonymous Sd/2 (R4-L1 V0 ALL, 70,926) / (1.2e-8 * Ssites * 252000) = 2.82 applied to the pre-registered base;
  k scaled 1.5, 2.2 (2.82 x 0.78, removing 22% ancestral polymorphism, upper end of the repo's 14-22%), 2.42 (x 0.86), 2.82.
  N_e: 7,778 (Kim's N for the Boyko reanalysis), 1e4, 2e4; 57,143 flagged (inconsistent with the N_A behind s).
PREDICTIONS (before run): decline is linear in the base multiplier. At k = 2.82 and N_e 1e4: Boyko ~1.04 (< ln 3 = 1.099),
  1000G 1.2 (> ln 3); at k = 2.2 both below ln 3 (0.8, 0.95). N_e 7,778 gives a 5-15% larger decline than 1e4. ESP row
  between Boyko and 1000G. The 1.5e-8 DFE row gives a decline within +/-15% of the 1000G 1.8e-8 row. Calibrated nonsyn
  fixations (pred) land within 25% of the observed 64,740 per lineage. dN/dS is base-independent.
"""
import importlib.util, os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("g05", os.path.join(here, "gap05_slightly_deleterious.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

ROWS = {"Boyko 1.8e-8": [0.183, 0.096, 0.147, 0.219, 0.355],
        "1000G gamma 1.8e-8": [0.217, 0.112, 0.169, 0.243, 0.259],
        "ESP gamma": [0.229, 0.105, 0.152, 0.216, 0.298],
        "1000G gamma 1.5e-8": [0.237, 0.127, 0.192, 0.266, 0.178]}
S_SITES, SD_LIN = 8311550.5, 141852.83333333334 / 2
BASE0 = g.MU * g.NSITES * g.T
K = SD_LIN / (g.MU * S_SITES * g.T)
LN3 = float(np.log(3))
BASES = [("mu 1.2e-8 (pre-reg)", 1.0), ("mu 1.5e-8", 1.5e-8 / g.MU), ("mu 1.8e-8", 1.8e-8 / g.MU),
         ("calibrated x1.5", 1.5), ("calibrated x2.20", K * 0.78), ("calibrated x2.42", K * 0.86), (f"calibrated x{K:.2f}", K)]
NES = (7778.0, 1e4, 2e4)


def run(sh, Ne, k, alt=False):
    f, c = g.per_bin(Ne, "A", alt)
    sh = np.array(sh)
    nb = sh * BASE0 * k * f
    return float((sh * f).sum()), float(nb.sum()), float((nb * c).sum())


print(f"# R4-GAP05 post hoc sensitivity (Reading A). observed synonymous per lineage {SD_LIN:,.0f}; mu*T*S = {g.MU*S_SITES*g.T:,.0f}; K = {K:.3f}")
print(f"observed nonsyn per lineage {g.ND_OBS_LINEAGE:,.0f}; neutral-equivalent at pre-reg base {BASE0:,.0f}; ln 3 = {LN3:.4f}")
for Ne in NES:
    print(f"\n## N_e = {Ne:g}")
    print("| DFE row | base | k | dN/dS pred | nonsyn del. fixations | decline | >= ln 3 |")
    print("|---|---|---|---|---|---|---|")
    for row, sh in ROWS.items():
        for lab, k in BASES:
            d, n, cst = run(sh, Ne, k)
            print(f"| {row} | {lab} | {k:.2f} | {d:.3f} | {n:,.0f} | {cst:.3f} | {'YES' if cst >= LN3 else 'no'} |")
print("\n## k needed for ln 3 (N_e 1e4)")
for row, sh in ROWS.items():
    for Ne in NES:
        _, _, c0 = run(sh, Ne, 1.0)
        print(f"  {row} N_e {Ne:g}: decline at k=1 {c0:.3f}; k* = {LN3/c0:.2f}")
print("\n## Bin-0 log-uniform shape at k = K (N_e 1e4)")
for row, sh in ROWS.items():
    d, n, c = run(sh, 1e4, K, alt=True)
    print(f"  {row}: decline {c:.3f}, fixations {n:,.0f}, dN/dS {d:.3f}")
print("\n## Predicted vs observed nonsyn divergence per lineage (N_e 1e4): predicted del. fixations / 64,740 (dN/dS-pred x Sd also shown)")
for row, sh in ROWS.items():
    d, n, c = run(sh, 1e4, K)
    print(f"  {row}: calibrated del. fixations {n:,.0f} ({n/g.ND_OBS_LINEAGE:.2f} of observed); pre-reg base {run(sh,1e4,1.0)[1]:,.0f} ({run(sh,1e4,1.0)[1]/g.ND_OBS_LINEAGE:.2f})")
print("\n## Flagged inconsistent row: N_e 57,143 with the Boyko/1000G s (N_A about 7.8-10k)")
for row in ("Boyko 1.8e-8", "1000G gamma 1.8e-8"):
    for lab, k in (BASES[0], BASES[-1]):
        d, n, c = run(ROWS[row], 57143.0, k)
        print(f"  {row} {lab}: dN/dS {d:.3f}, fixations {n:,.0f}, decline {c:.3f}")
