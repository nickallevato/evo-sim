"""L6 POST HOC (labelled post hoc: asked by REVIEW-R4-L6-combined.md MAJOR-1 at a183774; committed BEFORE this script
is run). Question: is Good 2017's well-mixed HMM 'fixed' state absorbing, so that the #fixed count (line 4 of
x_well_mixed_state_timecourse.txt) cannot fall by construction?

Run (builder, 1 process, seconds, < 100 MB; reads the L6 data dir as text, never executes anything in it):
  research/.venv/bin/python -I research/checks/l6_posthoc_absorbing.py DATA_DIR
Layout (read in the file itself, 2026-10-11): line 1 times; lines 2-5 the counts #unborn, #extinct, #fixed,
#polymorphic (as read by l6_ltee_undone.py from parse_file.py); lines 6+ one integer state per timepoint per mutation.
Step 1 identifies the integer code of each state by matching per-timepoint code counts over lines 6+ against lines 2-5.
Step 2 counts, over all mutations and populations, transitions OUT of the fixed code and out of the extinct code.
PREDICTION: lines 6+ are per-mutation state paths whose code counts reproduce lines 2-5 exactly; there are 0
transitions out of 'fixed' (and 0 out of 'extinct'): the state is absorbing in the published output, so '0 of 12
populations with a falling #fixed' holds by construction. If transitions out of 'fixed' exist, the L6 '0 of 12' is an
empirical finding after all.
"""
import os
import sys
from collections import Counter

POPS = ["m1", "m2", "m3", "m4", "m5", "m6", "p1", "p2", "p3", "p4", "p5", "p6"]
LABELS = ["unborn", "extinct", "fixed", "polymorphic"]


def row(line):
    return [float(x) for x in line.strip().strip(",").split(",") if x.strip()]


def main(d):
    tot_out = Counter()
    tot_paths = 0
    for p in POPS:
        lines = open(os.path.join(d, f"{p}_well_mixed_state_timecourse.txt")).read().splitlines()
        T = len(row(lines[0]))
        counts = [row(l) for l in lines[1:5]]
        paths = [[int(v) for v in row(l)] for l in lines[5:] if l.strip()]
        paths = [x for x in paths if len(x) == T]
        tot_paths += len(paths)
        codes = sorted({v for x in paths for v in x})
        code_of = {}
        for lab, cnt in zip(LABELS, counts):
            for c in codes:
                if all(sum(1 for x in paths if x[t] == c) == round(cnt[t]) for t in range(T)):
                    code_of[lab] = c
        out = Counter()
        for x in paths:
            for t in range(1, T):
                if x[t] != x[t - 1]:
                    out[(x[t - 1], x[t])] += 1
        fx, ex = code_of.get("fixed"), code_of.get("extinct")
        from_fixed = sum(n for (a, b), n in out.items() if a == fx)
        from_ext = sum(n for (a, b), n in out.items() if a == ex)
        tot_out["from_fixed"] += from_fixed
        tot_out["from_extinct"] += from_ext
        print(f"{p}: T={T} mutations={len(paths)} codes={codes} matched={code_of} "
              f"transitions out of fixed={from_fixed}, out of extinct={from_ext}; all transitions "
              f"{dict(sorted(out.items()))}")
    print(f"TOTAL mutations {tot_paths}; out of fixed {tot_out['from_fixed']}; out of extinct {tot_out['from_extinct']}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(__doc__)
