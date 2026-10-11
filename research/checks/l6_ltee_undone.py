"""L6: Q178 'ten of the twelve populations even show intervals where fixations are being undone faster than any new
ones complete' -- recount from Good et al. 2017's public trajectory files. Low-stakes tier (one combined review).
Pre-registered: committed BEFORE the main run.

Run (builder or na-workhorse, 1 process, streams one file at a time, < 300 MB):
  research/.venv/bin/python -I research/checks/l6_ltee_undone.py run DATA_DIR OUT_JSON
DATA_DIR holds, per population x in m1..m6, p1..p6 (Ara-1..-6, Ara+1..+6), the files
  x_annotated_timecourse.txt and x_well_mixed_state_timecourse.txt from github.com/benjaminhgood/LTEE-metagenomic
  data_files/ (fetched into its own new dir, never executed). File layouts read from that repo's parse_file.py
  (read as text): annotated: header times from column 13 in (alt, depth) pairs, 'time' after ':' (times > 1e6 are
  clones), line 2 = average depths, column 12 = PASS flag; well-mixed: line 1 times, line 2 #unborn, line 3 #extinct,
  line 4 #fixed, line 5 #polymorphic (Good's HMM, states A/E/F/P).

ANTECEDENT (Day's own method, Zenodo 23003785 s4.1 and s5.3, sources/raw/day/zenodo-23003785.txt):
  s4.1 'Good et al. metagenomic data, mutations at >=95% population frequency', counts at 10K..60K for five
  non-mutators (Ara+2 19 25 31 45 55 64; Ara+4 4 31 36 38 28 68; Ara+5 16 13 38 34 14 0; Ara-5 9 16 36 7 63 60;
  Ara-6 15 22 26 24 24 35); s5.3 'Ten of twelve populations -- mutator and non-mutator alike -- show at least one
  10,000-generation interval where fixations are being undone faster than new ones complete.'
  Inferred method (derivation of the unstated): an interval 'undoes fixations faster than new ones complete' when the
  >=95% snapshot count falls between consecutive 10K timepoints (net change < 0).

COMPUTED
  R1 snapshot recount: PASS mutations with alt/depth >= 0.95 at the population sample nearest each 10K mark
     (within 500 generations; depth >= 5); per-population declines between consecutive snapshots.
  R2 Good's HMM well-mixed #fixed at the same marks; declines.
  R3 for every mutation counted at one snapshot and not at the next: its frequency at the next snapshot and at the
     last sample: 'dip' (back >= 0.95 at a later snapshot), 'lost' (last freq < 0.5), 'hover' (otherwise).
  R4 agreement of R1 with Day's 30 tabulated cells (|diff| <= 20% or <= 3).

PREDICTIONS (fixed now; the data files have not been opened)
  Day side: R1 reproduces his finding: >= 10 of 12 populations show >= 1 declining interval; the declines are real
    features of the trajectories (mutations that were >= 95% later fall back), not artefacts.
  Critic side: R2 (Good's own fixation calls) never declines in any population (0 of 12): a fixed mutation in a
    well-mixed population is not 'undone'; R1's declines come from mutations that were >= 95% in a dominant clade and
    were displaced by a coexisting clade (Good 2017's quasi-stable coexistence) or from threshold noise, so most
    R3 cases ('lost' + 'hover') were never fixed in Good's sense.
  Audit: R1 gives 9-12 populations with a decline; >= 20 of Day's 30 cells match under R4; R2 has 0 declines;
    among R3 cases 'lost' >= 30%.
  Reading rule (fixed): if R1 reproduces and R2 has no declines, Q178 holds on Day's counting rule (internal) and is
  a relabelling for its 'fixations' wording (a >= 95% snapshot is not a fixation), which is the A2c/E6 question.
"""
import json
import os
import sys

POPS = ["m1", "m2", "m3", "m4", "m5", "m6", "p1", "p2", "p3", "p4", "p5", "p6"]
NAME = {p: ("Ara-" if p[0] == "m" else "Ara+") + p[1] for p in POPS}
DAY = {"Ara+2": [19, 25, 31, 45, 55, 64], "Ara+4": [4, 31, 36, 38, 28, 68], "Ara+5": [16, 13, 38, 34, 14, 0],
       "Ara-5": [9, 16, 36, 7, 63, 60], "Ara-6": [15, 22, 26, 24, 24, 35]}
MARKS = [10000, 20000, 30000, 40000, 50000, 60000]


def nearest(times, t, tol=500):
    best = None
    for i, x in enumerate(times):
        if abs(x - t) <= tol and (best is None or abs(x - t) < abs(times[best] - t)):
            best = i
    return best


def read_annotated(path):
    with open(path) as fh:
        items = fh.readline().strip().split(",")
        times = [int(float(items[i].split(":")[1])) for i in range(13, len(items), 2)]
        d = fh.readline().strip().split(",")
        avg = [float(d[i + 1]) for i in range(13, len(d), 2)]
        pop_idx = [k for k, t in enumerate(times) if t < 1000000]
        ptimes = [times[k] for k in pop_idx]
        muts = []
        for line in fh:
            it = line.strip().split(",")
            if it[12].strip() != "PASS":
                continue
            fr = []
            for k in pop_idx:
                a = float(it[13 + 2 * k])
                dp = float(it[14 + 2 * k])
                if dp >= 5 and avg[k] >= 5:
                    fr.append(a / dp)
                else:
                    fr.append(None)
            muts.append((int(it[0]), it[1].strip(), fr))
    return ptimes, muts


def read_wellmixed(path):
    with open(path) as fh:
        t = [float(x) for x in fh.readline().split(",")]
        fh.readline()
        fh.readline()
        nfix = [float(x) for x in fh.readline().split(",")]
    return t, nfix


def run(ddir, out):
    res = {}
    for p in POPS:
        ptimes, muts = read_annotated(os.path.join(ddir, f"{p}_annotated_timecourse.txt"))
        idx = [nearest(ptimes, m) for m in MARKS]
        snap = []
        sets = []
        for i in idx:
            if i is None:
                snap.append(None)
                sets.append(None)
                continue
            s = {k for k, (_, _, fr) in enumerate(muts) if fr[i] is not None and fr[i] >= 0.95}
            sets.append(s)
            snap.append(len(s))
        declines = [(MARKS[j], MARKS[j + 1], snap[j + 1] - snap[j]) for j in range(len(MARKS) - 1)
                    if snap[j] is not None and snap[j + 1] is not None and snap[j + 1] < snap[j]]
        cases = {"dip": 0, "lost": 0, "hover": 0}
        for j in range(len(MARKS) - 1):
            if sets[j] is None or sets[j + 1] is None:
                continue
            for k in sets[j] - sets[j + 1]:
                fr = muts[k][2]
                later = [sets[m] for m in range(j + 2, len(MARKS)) if sets[m] is not None]
                last = next((x for x in reversed(fr) if x is not None), None)
                if any(k in s for s in later):
                    cases["dip"] += 1
                elif last is not None and last < 0.5:
                    cases["lost"] += 1
                else:
                    cases["hover"] += 1
        wt, nfix = read_wellmixed(os.path.join(ddir, f"{p}_well_mixed_state_timecourse.txt"))
        widx = [nearest(wt, m) for m in MARKS]
        wfix = [nfix[i] if i is not None else None for i in widx]
        wdec = [(MARKS[j], MARKS[j + 1]) for j in range(len(MARKS) - 1)
                if wfix[j] is not None and wfix[j + 1] is not None and wfix[j + 1] < wfix[j]]
        allwdec = sum(1 for a, b in zip(nfix, nfix[1:]) if b < a)
        res[NAME[p]] = dict(n_pass=len(muts), sample_times=[ptimes[i] if i is not None else None for i in idx],
                            snapshot=snap, declines=declines, cases=cases, hmm_fixed=wfix, hmm_declines=wdec,
                            hmm_declines_any_timepoint=allwdec, last_time=ptimes[-1])
    match = 0
    cells = 0
    for pop, row in DAY.items():
        for a, b in zip(row, res[pop]["snapshot"]):
            if b is None:
                continue
            cells += 1
            if abs(a - b) <= max(3, 0.2 * a):
                match += 1
    summ = dict(pops_with_decline=sum(1 for r in res.values() if r["declines"]),
                pops_with_hmm_decline=sum(1 for r in res.values() if r["hmm_declines"]),
                pops_with_hmm_decline_any=sum(1 for r in res.values() if r["hmm_declines_any_timepoint"]),
                day_cells_matched=match, day_cells=cells,
                cases=dict((k, sum(r["cases"][k] for r in res.values())) for k in ("dip", "lost", "hover")))
    json.dump(dict(per_pop=res, summary=summ), open(out, "w"), indent=1)
    for pop, r in res.items():
        print(f"{pop}: snapshot {r['snapshot']} declines {r['declines']} | HMM fixed {r['hmm_fixed']} "
              f"declines {r['hmm_declines']} (any tp {r['hmm_declines_any_timepoint']}) | R3 {r['cases']}")
    print("summary", json.dumps(summ))


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "run":
        run(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
