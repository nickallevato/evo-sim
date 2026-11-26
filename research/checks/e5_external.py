"""E5 external: are MITTENS 3.0's Ara-2 '-906' and Ara+5 '0 at 60K' cells estimator artefacts or biology?
Pre-registered: committed BEFORE the main run (brief research/checks/briefs/E5-analyst-1.md). Gap: E5.

TARGET (claim E5, verdicts.external pending). Critic quotes (claim file E5-ara2-ara5-counts.md):
  RE-03 Dumb-and-Dumber, r/DebateEvolution 1wss2wj, 2026-09-28: "Their correction formula then produces minus 906
        "true fixations" in Ara-2."
  RE-04 same post: "Their Ara+5 count drops from 38 such mutations at 30,000 generations to zero at 60,000."
  RE-10 Sparky_6_4, 1wxgsjm, 2026-10-04: "A count of fixed mutations cannot be negative; the negative value comes from
        the paper's own correction"
Day's text, Z23003785 (MITTENS 3.0, pub. 2026-09-28, modified 2026-10-04). Held copy: sources/raw/vid01-score-2026-10-13/
  main.txt (gitignored; sha256 0287f54b...6dd5b42; the canonical sources/raw/day/zenodo-23003785.txt is not on disk):
  s3.1 l.167-171: "To correct for this, we estimate the number of false-shared mutations under a neutral site-frequency
        spectrum for n=2 sampling: false_shared ~ (private1 + private2) / 2. The corrected fixation count is shared -
        false_shared."
  s5.1 l.321: "Ara-2   Point mutator (~100x)   -906   N/A"
  s5.2 l.342-349: "Ara-2 achieved negative net fixations at 50,000 generations: -906 by clone-pair analysis. The sharing
        rate between its two clones at 50K was 4.2% [...] The population fragmented into permanently competing
        sub-populations [...] none able to displace the others. [...] One in seven mutator populations -- 14% --
        responded to supermutation by achieving zero fixations."
  s3.2: a mutation is "fixed at a given milestone if its frequency reached >=95% at that timepoint" (Good 2017 data);
        s3.3 calls this method "methodologically superior". s4.1: Ara+5 = 16, 13, 38, 34, 14, 0 at 10K..60K.

FEASIBILITY (the brief's gate). R4-E5E6 said the clone-pair formula is not in the extracted text. It is in the held
re-fetch (s3.1 above): corrected = S - (P1+P2)/2, S shared, P1, P2 private. That is not bounded below by 0: it is
negative whenever P1+P2 > 2S. With -906 and the 4.2% sharing rate the pair's inputs can be rebuilt (two readings of
"sharing rate"; R0 below). The Tenaillon 2016 clone .gd files are NOT held, so Day's pair cannot be recounted. The Good
2017 per-population trajectories ARE held (fetched for L6 on 2026-10-11; builder:sources/raw/l6-good2017-data-2026-10-11/,
sha256 list research/checks/results/raw/l6_data.sha256), so the population-level state of Ara-2 at 50K and of Ara+5
near 60K can be measured by Day's own s3.2 rule. No fetch is needed. Under a neutral SFS with n = 2, (P1+P2)/2 is the
expected count of shared-but-unfixed sites (E[x^2] vs E[2x(1-x)] over density 1/x), so the formula is right on
average for an unstructured neutral population; the test is what the measured Ara-2 population implies for it.
DISCLOSED, NOT BLIND: R4-L6 (raw/l6_undone.json) already reports Ara-2 >=95% snapshot 198 at 40K and 708 at 50K, Good's
HMM fixed 939 at 50K; Ara+5 has no sample within 500 generations of 60K (last 57,500) and 14 at 50K. Those numbers fix
the F95 half of the Ara-2 band and the sample half of the Ara+5 band in advance. The unseen quantities are M_mid, D_min
and E2 for Ara-2 (they decide band A against band B) and F95 at Ara+5's last sample. PREREG-STATUS: criterion-only.

COMPUTED (DATA_DIR = the 24 Good 2017 files; parsers imported from l6_ltee_undone.py, PASS, depth >= 5)
  R0 arithmetic: rebuild (S, P = P1+P2) from S - P/2 = -906 with sharing r = 0.042 read as (a) S/(S+P):
     S = 1812 r/(1-3r) = 87.1, P = 1986; (b) S/mean clone size S/(S+P/2): S = 906 r/(1-2r) = 41.5, P = 1895.
     S_hi = 87 (larger reading).
  R1 per population at the sample t50 nearest 50,000 (within 500): F95 = #PASS with x >= 0.95 (Day's s3.2 rule);
     M_mid = # with 0.05 < x < 0.95; M_lo = # with 0 < x <= 0.05; E2 = sum x(2x-1), the expected value of Day's
     corrected count for two clones drawn at random (P(both) = x^2, P(one) = 2x(1-x); exact by linearity, any linkage);
     D_min = F95 - M_mid/2, the corrected count for the most divergent pair that the detected spectrum allows (every
     >=95% mutation shared, every mid-frequency mutation private to one clone). Undetected clone-private mutations
     and a clone lacking a >=95% mutation would both push a real pair below D_min.
  R2 Ara+5: sample nearest 60,000 within 500 (present or not); F95 at that sample, else at the last sample.
  R3 assertions: the 24 sha256 match l6_data.sha256; Ara-2 F95 at 50K == L6's 708 and Ara+5 last time == 57,500
     (labels read from L6, asserted, not assumed); Day's mutator clone-pair values printed beside E2 (descriptive).

BANDS (exhaustive; first matching row wins within a cell)
  Ara-2 cell:  U2 no Ara-2 sample within 500 of 50K, or an assertion fails       -> untestable
               C2 F95 <= 100 (~ S_hi: population agrees nothing swept)          -> biology (Day)
               M2 100 < F95 < 300                                              -> indeterminate
               B2 F95 >= 300 and D_min <= -906 (a cross-clade pair from the measured population reproduces -906; the
                  count is not the population's state, the low sharing is real sub-population structure) -> mixed
               A2 F95 >= 300 and D_min > -906 (hundreds near-fixed; no pair from the detected spectrum reaches -906;
                  the value comes from the correction charging private load the population does not show) -> artefact
               (300 = 3 x 100, the RH 3x band convention, fixed now.)
  Ara+5 cell:  U5 no Ara+5 data                                                -> untestable
               D5 a sample within 500 of 60K and F95 there <= 2                 -> biology (Day: a measured 0)
               X5 a sample within 500 of 60K and F95 there >= 3                 -> artefact (0 not reproduced)
               G5 no such sample and F95 at the last sample >= 3                -> artefact (missing sample read as 0)
               Z5 no such sample and F95 at the last sample <= 2                -> mixed (unmeasured, last sample agrees)
VERDICT MOVE (E5 external; the field moves only after write-up and the combined review, D-40)
  untestable if either cell is U; supported if A2 and (X5 or G5); contradicted if C2 and D5; contested otherwise.

PREDICTIONS (each can fail)
  Day side: Ara-2 fragmented and "no single lineage could sweep", so F95(50K) is near zero (C2) and the -906 overshoots
    a real near-zero; Ara+5 "collapses entirely", a measured 0 near 60K (D5). Verdict: contradicted.
  Critic side: a count cannot be negative; the population had many near-fixed mutations (F95 >= 300) and the -906 comes
    from the correction (A2); Ara+5's 0 is not a measurement (G5 or X5). Verdict: supported.
  Audit (with the L6 numbers above in hand): F95 = 708, so not C2 or M2; M_mid < 3,228 (B2 needs M_mid >= 2(708+906)
    = 3,228 of Ara-2's 3,488 PASS mutations), so A2; 200 <= E2 <= 708 (a random pair gives a positive count); Ara+5
    G5 with F95 at 57,500 in 5-40. Verdict: supported. Reachability: C2 needs F95 <= 100 (ruled out by L6, disclosed);
    B2 needs 3,228 mid-frequency mutations (reachable, unlikely); D5/X5 need a 60K Ara+5 sample (ruled out by L6).
    The Day side's live route is therefore B2 (contested), not C2; stated so the reviewer can weigh it.

RUN (trivial: one process, < 1 min, < 300 MB; no smoke beyond `selftest`). Compute on na-workhorse only:
  ssh -o BatchMode=yes builder 'cd ~/projects/evo-sim/sources/raw && tar cf - l6-good2017-data-2026-10-11' |
    ssh -o BatchMode=yes na-workhorse 'mkdir -p ~/projects/evo-sim/sources/raw && cd ~/projects/evo-sim/sources/raw && tar xf -'
  rsync research/checks/{e5_external,l6_ltee_undone}.py research/checks/results/raw/l6_{data.sha256,undone.json} \
    to the same paths on na-workhorse; then
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup research/.venv/bin/python -I research/checks/e5_external.py
    run sources/raw/l6-good2017-data-2026-10-11 research/checks/results/raw/e5_external.json
    > research/checks/results/raw/e5_external.out 2>&1 < /dev/null &'
  Collect: rsync na-workhorse:projects/evo-sim/research/checks/results/raw/e5_external.* back; host and md5s in
  raw/e5_external.host. Local: `python -I research/checks/e5_external.py selftest` (arithmetic and quotes only).
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from l6_ltee_undone import NAME, POPS, nearest, read_annotated  # noqa: E402

RAW = os.path.join(HERE, "results", "raw")
MAIN = os.path.join(HERE, "..", "..", "sources", "raw", "vid01-score-2026-10-13", "main.txt")
DAY_CP = {"Ara+1": 110, "Ara+3": 932, "Ara+6": 803, "Ara-1": 978, "Ara-2": -906, "Ara-3": 273, "Ara-4": 1153}
V, R = -906, 0.042


def rebuild():
    sa = 2 * -V * R / (1 - 3 * R)
    sb = -V * R / (1 - 2 * R)
    return {"a_S/(S+P)": (sa, 2 * (sa - V)), "b_S/(S+P/2)": (sb, 2 * (sb - V))}


def spectrum(fr):
    xs = [x for x in fr if x is not None]
    f95 = sum(1 for x in xs if x >= 0.95)
    mid = sum(1 for x in xs if 0.05 < x < 0.95)
    lo = sum(1 for x in xs if 0 < x <= 0.05)
    return dict(F95=f95, M_mid=mid, M_lo=lo, E2=sum(x * (2 * x - 1) for x in xs), D_min=f95 - mid / 2)


def band2(s):
    if s is None:
        return "U2"
    if s["F95"] <= 100:
        return "C2"
    if s["F95"] < 300:
        return "M2"
    return "B2" if s["D_min"] <= V else "A2"


def band5(present, f95):
    if f95 is None:
        return "U5"
    if present:
        return "D5" if f95 <= 2 else "X5"
    return "G5" if f95 >= 3 else "Z5"


def verdict(b2, b5):
    if "U" in (b2[0], b5[0]):
        return "untestable"
    if b2 == "A2" and b5 in ("X5", "G5"):
        return "supported"
    if b2 == "C2" and b5 == "D5":
        return "contradicted"
    return "contested"


def selftest():
    rb = rebuild()
    for k, (s, p) in rb.items():
        assert abs(s - p / 2 - V) < 1e-9, k
    assert abs(rb["a_S/(S+P)"][0] / sum(rb["a_S/(S+P)"]) - R) < 1e-9
    assert abs(spectrum([1.0, 0.5, 0.25, None])["E2"] - (1 + 0 - 0.125)) < 1e-12
    if os.path.exists(MAIN):
        t = " ".join(open(MAIN, encoding="utf-8").read().split())
        for q in ["The corrected fixation count is shared − false_shared.", "−906 by clone-pair analysis",
                  "The sharing rate between its two clones at 50K was 4.2%", "achieving zero fixations"]:
            assert q in t, q
        print("quotes found in held Z23003785 copy")
    print("rebuild:", {k: (round(s, 1), round(p, 1)) for k, (s, p) in rb.items()})
    print("selftest ok")


def run(ddir, out):
    want = dict(line.split()[::-1] for line in open(os.path.join(RAW, "l6_data.sha256")) if line.strip())
    for fn, h in want.items():
        got = hashlib.sha256(open(os.path.join(ddir, fn), "rb").read()).hexdigest()
        assert got == h, (fn, got, h)
    l6 = json.load(open(os.path.join(RAW, "l6_undone.json")))["per_pop"]
    res = {"rebuild": rebuild(), "pops": {}}
    for p in POPS:
        ptimes, muts = read_annotated(os.path.join(ddir, f"{p}_annotated_timecourse.txt"))
        i50, i60 = nearest(ptimes, 50000), nearest(ptimes, 60000)
        s50 = spectrum([fr[i50] for _, _, fr in muts]) if i50 is not None else None
        il = i60 if i60 is not None else len(ptimes) - 1
        res["pops"][NAME[p]] = dict(t50=ptimes[i50] if i50 is not None else None, at50=s50,
                                    t60_present=i60 is not None, t_last=ptimes[il],
                                    F95_late=spectrum([fr[il] for _, _, fr in muts])["F95"], day_clone_pair=DAY_CP.get(NAME[p]))
    a2, a5 = res["pops"]["Ara-2"], res["pops"]["Ara+5"]
    assert a2["at50"] is None or a2["at50"]["F95"] == l6["Ara-2"]["snapshot"][4], (a2["at50"], l6["Ara-2"]["snapshot"])
    assert a5["t60_present"] or a5["t_last"] == l6["Ara+5"]["last_time"] == 57500, (a5, l6["Ara+5"]["last_time"])
    b2, b5 = band2(a2["at50"]), band5(a5["t60_present"], a5["F95_late"])
    res.update(band_ara2=b2, band_ara5=b5, verdict=verdict(b2, b5))
    print("rebuild (S, P):", {k: (round(s, 1), round(q, 1)) for k, (s, q) in res["rebuild"].items()})
    print("%-6s %6s %5s %5s %5s %8s %8s %6s" % ("pop", "t50", "F95", "M_mid", "M_lo", "E2", "D_min", "Day_cp"))
    for k, v in res["pops"].items():
        s = v["at50"] or {}
        print("%-6s %6s %5s %5s %5s %8.1f %8.1f %6s" % (k, v["t50"], s.get("F95"), s.get("M_mid"), s.get("M_lo"),
              s.get("E2", float("nan")), s.get("D_min", float("nan")), v["day_clone_pair"]))
    print("Ara+5: sample within 500 of 60K:", a5["t60_present"], "| last/used sample", a5["t_last"], "F95", a5["F95_late"])
    print("BANDS: Ara-2 %s | Ara+5 %s -> E5 external %s" % (b2, b5, res["verdict"]))
    json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    if sys.argv[1:2] == ["selftest"]:
        selftest()
    elif sys.argv[1:2] == ["run"] and len(sys.argv) == 4:
        run(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
