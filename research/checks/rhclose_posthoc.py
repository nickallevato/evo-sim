"""R4-RHclose POST HOC (fix pass for REVIEW-R4-RHclose-combined.md MAJOR-1, MAJOR-2, MAJOR-3).  Labelled post hoc: the
registered run (rhclose.py, 7185f1e) is unchanged and its tags stand for the registered readings.  Stdlib only; reuses
rhclose.py's functions.  Run:  research/.venv/bin/python -I research/checks/rhclose_posthoc.py > research/checks/results/raw/rhclose_posthoc.out
Pre-registered (post hoc) in the commit that adds this file, BEFORE its run.

PART A (C7, MAJOR-1).
  A1 Census-frame reading: HL l.101-118 variance-N_e frame, N_e = 4N/(V_k+2), V_k = 5.  No sourced Holocene/early-modern
     European census is in the repo (grep parameters.yaml, sources/holocene-ne.md: only effective-size estimates, 1.5k-12k
     Holocene by coalescent/IBS/ROH/SFS methods, present-day 0.65M-27M Ne), so the census is UNSOURCED: report the flip
     point only.  Flip = the census at which F_drift(280 gen) = 3e-4, N_e = 280/(2 x 3e-4)-ish solved exactly.
     Prediction: flip N_e about 4.7e5, census about 8.2e5.  Tag on this reading: dialectic iff census >= flip; unsourced,
     so NOT adopted as the headline.
  A2 Fixation-count reading of "drift" (rule C referent; review: "drift is not producing fixations"): expected fraction of
     alleles starting at p0 in {0.5, 0.9} that reach fixation by drift within 280 generations, Gaussian-tail UPPER
     BOUND sqrt(p0(1-p0)F_drift) at N_e in {1e4, 2e4, 4.67e5}; and the exact Kimura conditional-time factor at p -> 0:
     F(x), x = 280/N_e.  Prediction: expected count is about 0 (<= 1e-3 per allele at p0=0.5, N_e <= 2e4; the Gaussian
     tail at p0 = 0.9 is larger and is an overestimate near the boundary), i.e. the literal count claim "no drift-driven
     fixations from below 50%" is true to a good approximation, which is also the neutral expectation (X1 row C).
     Tag on this reading: dialectic as a count; the inference "so drift is not happening" stays non-sequitur at C.
PART B (Q157/Q158, MAJOR-2).  Re-state, per reading, F or D at the registered inputs and the tag under the registered
  0.30 edge: F over 6.5 My (a) 0.697 (6.3 My 0.676) rhetoric; D at (a) 0.256 / 0.242 dialectic; Takahata 1e5 held for the
  whole lineage F 0.281 dialectic (just under 0.30); HL's 2 My window F 0.026 dialectic; S (current size, HL abstract
  l.22-24 and l.464-466) = restates B2, no new number, tag dialectic as a restatement.  Conclusion: tag not robust.
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rhclose", os.path.join(HERE, "rhclose.py"))
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)

T = 280


def solve_ne(target):
    lo, hi = 1e3, 1e9
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if rc.f_drift([(T, mid)]) > target:
            lo = mid
        else:
            hi = mid
    return hi


print("## A1 census-frame flip (census UNSOURCED)")
for edge in (3e-4, 1e-3):
    ne = solve_ne(edge)
    print(f"F_drift(280 gen) = {edge:g} at N_e {ne:,.0f} -> census {ne * 7 / 4:,.0f} (V_k 5)")

print("\n## A2 fixation-count reading (280 generations)")
print("| N_e | F_drift | p0 | Gaussian-tail upper bound on P(reach 1) | Kimura F(x), x=T/N_e, p->0 |\n|---|---|---|---|---|")
for ne in (1e4, 2e4, solve_ne(3e-4)):
    f = rc.f_drift([(T, ne)])
    for p0 in (0.5, 0.9):
        sd = math.sqrt(p0 * (1 - p0) * f)
        z = (1 - p0) / sd
        tail = 0.5 * math.erfc(z / math.sqrt(2))
        print(f"| {ne:,.0f} | {f:.3g} | {p0} | {tail:.2e} (z {z:.1f}) | {rc.F(T / ne):.2e} |")

print("\n## B per-reading (human lineage, N_e 57,143, empty start; tag vs registered 0.30 edge)")
ne = 4e5 / 7
rows = []
for Tmy in (6.3, 6.5):
    ep = [(Tmy * 1e6 / 25, ne)]
    X = rc.clock(ep)[0]
    rows.append((f"F over {Tmy} My", rc.F(X)))
    rows.append((f"D over {Tmy} My", rc.delivered(ep)))
ep = [(6.5e6 / 25, 1e5)]
rows.append(("Takahata 1e5 whole lineage F, 6.5 My", rc.F(rc.clock(ep)[0])))
ep = [(2e6 / 25, ne)]
rows.append(("HL 2 My window F", rc.F(rc.clock(ep)[0])))
for lab, v in rows:
    print(f"| {lab} | {v:.3f} | {'dialectic' if v <= 0.30 else 'rhetoric'} |")
