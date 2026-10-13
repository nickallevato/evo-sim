"""grade_certainty.py: sample and counts for docs/research/criticality/grade-certainty-2026-10-12.md (read-only).

    research/.venv/bin/python -I research/tools/grade_certainty.py sample
    research/.venv/bin/python -I research/tools/grade_certainty.py count

`sample` prints the frame and the seeded, stratified sample of 30 decided external verdicts on claim files
that are not load-bearing. It was committed with the adaptation, before any rating.
`count` re-computes every certainty in the summary-of-findings table from its code
column under the three starting-level mappings, checks the printed values, and prints the aggregates.
Changes nothing.
"""
import collections
import glob
import random
import re
import sys

import yaml

SEED = 2026101206          # criticality pass vi
TRIAL_SEED = 20261012      # proposal (c)'s seed (method_audit_stats.py)
# Additional draws per stratum (verdict, party), fixed before the draw; see section 3.2 of the pass.
EXTRA = [("supported", "critic", 2), ("supported", "day", 2), ("supported", "literature", 2),
         ("contradicted", "day", 2), ("contradicted", "critic", 1),
         ("untestable", "day", 1), ("untestable", "critic", 1),
         ("contested", "critic", 2)]
PASS = "docs/research/criticality/grade-certainty-2026-10-12.md"
LEVELS = ["very-low", "low", "moderate", "high"]


def load():
    rows = {}
    for f in sorted(glob.glob("docs/research/claims/*.md")):
        if f.endswith("_TEMPLATE.md"):
            continue
        fm = yaml.safe_load(open(f, encoding="utf-8").read().split("---", 2)[1])
        rows[str(fm["id"])] = {"side": fm["side"], "lb": bool(fm.get("load_bearing")),
                               "ext": str(fm["verdicts"]["external"]), "status": fm["status"], "file": f}
    return rows


def decided(rows):
    return {k: r for k, r in rows.items() if r["ext"] not in ("pending", "n/a")}


def draw(rows):
    dec = decided(rows)
    contested = sorted(k for k, r in dec.items() if r["ext"] == "contested")
    trial = sorted(random.Random(TRIAL_SEED).sample(contested, 20))
    forced = [k for k in trial if not dec[k]["lb"]]
    rng = random.Random(SEED)
    extra = []
    for verdict, side, n in EXTRA:
        pool = sorted(k for k, r in dec.items()
                      if not r["lb"] and r["ext"] == verdict and r["side"] == side and k not in forced)
        extra += [(k, verdict, side) for k in rng.sample(pool, min(n, len(pool)))]
    return trial, forced, extra


def sample():
    rows = load()
    dec = decided(rows)
    lb = sorted(k for k, r in dec.items() if r["lb"])
    print("claim files:", len(rows), " decided external:", len(dec), " on load-bearing nodes:", len(lb))
    print("load-bearing:", ", ".join("%s(%s)" % (k, dec[k]["ext"]) for k in lb))
    frame = collections.Counter((r["ext"], r["side"]) for r in dec.values() if not r["lb"])
    print("frame (not load-bearing):", sum(frame.values()))
    for k in sorted(frame):
        print("   %-13s %-11s %d" % (k[0], k[1], frame[k]))
    trial, forced, extra = draw(rows)
    print("proposal (c) trial sample (seed %d):" % TRIAL_SEED, trial)
    print("  of which load-bearing (rated in the load-bearing set):", [k for k in trial if dec[k]["lb"]])
    print("  forced into the sample:", len(forced), forced)
    print("extra draws (seed %d):" % SEED)
    for k, verdict, side in extra:
        print("   %-8s %-13s %s" % (k, verdict, side))
    ids = forced + [k for k, _, _ in extra]
    print("sample of", len(ids), "by verdict:", dict(collections.Counter(dec[k]["ext"] for k in ids)),
          "by party:", dict(collections.Counter(dec[k]["side"] for k in ids)))


# ---- part 2: recomputation and aggregates (section 2.7 of the pass) ----

START_M0 = {("D", "W"): 3, ("D", "F"): 3, ("L", "W"): 3, ("L", "F"): 3,
            ("Lm", "W"): 1, ("Lm", "F"): 3, ("S", "W"): 1, ("S", "F"): 3, ("T", "W"): 1, ("T", "F"): 3}
START_MD = {"D": 3, "L": 1, "Lm": 0, "S": 0, "T": 0}


def clamp(x):
    return max(0, min(3, x))


def certainty(c):
    """c: dict of the code column. Returns (M0, M-D, M-C, FR, lenient M0, M0 without mw) as level names."""
    if c["dir"] in ("ne", "na") or c["b"] in ("C", "N"):
        x = "NE" if c["dir"] != "na" else "NR"
        return (x,) * 6
    g = lambda k: int(c[k])
    oi = min(2, max(g("sp"), g("rd")))
    ind0 = min(2, g("mw") + oi)
    s0 = START_M0[(c["b"], c["k"])]
    d0 = g("rob") + g("inc") + ind0 + g("imp") + g("sel")
    m0 = clamp(s0 - d0 + (g("upf") if s0 == 1 and d0 == 0 else 0))
    sd = START_MD[c["b"]]
    dd = g("rob") + g("inc") + oi + g("imp") + g("sel")
    md = clamp(sd - dd + (g("upf") if sd <= 1 and dd == 0 else 0))
    mc = clamp(3 - (max(g("rob"), g("ur")) + g("inc") + oi + g("imp") + g("sel")))
    fr = LEVELS[clamp(3 - (g("rob") + g("inc") + g("rd") + g("imp")))] if c["b"] in ("S", "T", "Lm") else "-"
    len_ok = s0 == 1 and g("upf") and g("rob") == 0 and max(g("inc"), ind0, g("imp"), g("sel")) < 2
    lenient = clamp(s0 - d0 + (g("upf") if len_ok else 0))
    dn = g("rob") + g("inc") + oi + g("imp") + g("sel")
    nomw = clamp(s0 - dn + (g("upf") if s0 == 1 and dn == 0 else 0))
    return LEVELS[m0], LEVELS[md], LEVELS[mc], fr, LEVELS[lenient], LEVELS[nomw]


def parse_table():
    rows = []
    for line in open(PASS, encoding="utf-8"):
        m = re.search(r"`(id=[^`]*)`", line)
        if not (line.startswith("| ") and m):
            continue
        c = dict(kv.split("=", 1) for kv in m.group(1).split(";"))
        p = re.search(r"M0 \*\*([a-zA-Z-]+)\*\* · M-D ([a-zA-Z-]+) · M-C ([a-zA-Z-]+) · FR ([a-zA-Z-]+)", line)
        ne = re.search(r"\*\*(NE|NR) \(", line)
        c["printed"] = p.groups() if p else ((ne.group(1),) * 4 if ne else None)
        rows.append(c)
    return rows


def tab(title, rows, key, val, order=None):
    cnt = collections.Counter((key(r), val(r)) for r in rows)
    cols = [x for x in LEVELS[::-1] + ["NE", "NR", "-"] if any(v == x for _, v in cnt)]
    keys = order or sorted({k for k, _ in cnt})
    print("\n" + title)
    print("| | " + " | ".join(cols) + " | Total |")
    print("|---|" + "---|" * (len(cols) + 1))
    for k in keys:
        if any(kk == k for kk, _ in cnt):
            print("| %s | " % k + " | ".join(str(cnt[(k, c)]) for c in cols) + " | %d |" % sum(cnt[(k, c)] for c in cols))
    print("| **All** | " + " | ".join(str(sum(cnt[(k, c)] for k in keys)) for c in cols) + " | %d |" % len(rows))


def count():
    rows = parse_table()
    claims = load()
    bad = 0
    for r in rows:
        r["c"] = certainty(r)
        cl = claims[r["id"]]
        if r["printed"] != r["c"][:4] or cl["ext"] != r["v"] or cl["side"] != r["party"] or int(r["lb"]) != cl["lb"]:
            bad += 1
            print("MISMATCH", r["id"], r["printed"], r["c"][:4], cl["ext"], cl["side"], cl["lb"])
    trial, forced, extra = draw(claims)
    want = sorted(k for k, cl in decided(claims).items() if cl["lb"]) + forced + [k for k, _, _ in extra]
    if sorted(want) != sorted(r["id"] for r in rows):
        bad += 1
        print("ROW SET differs from load-bearing set plus sample:", sorted(set(want) ^ {r["id"] for r in rows}))
    print("rows:", len(rows), " mismatches:", bad)
    M0 = lambda r: r["c"][0]
    LB = lambda r: "load-bearing" if r["lb"] == "1" else "sample"
    tab("M0 by verdict", rows, lambda r: r["v"], M0, ["supported", "contradicted", "contested", "untestable"])
    for name, sub in (("load-bearing", [r for r in rows if r["lb"] == "1"]), ("sample", [r for r in rows if r["lb"] == "0"])):
        tab("M0 by verdict, " + name, sub, lambda r: r["v"], M0, ["supported", "contradicted", "contested", "untestable"])
    tab("M0 by party", rows, lambda r: r["party"], M0, ["day", "ally", "critic", "literature"])
    tab("M0 by basis", rows, lambda r: r["b"] + ("/F" if r["k"] == "F" and r["b"] != "N" else ""), M0)
    tab("M0 by load-bearing status", rows, LB, M0)
    tab("M0 by severity grade of the deciding check", rows, lambda r: r["st"], M0, ["SEVERE", "PARTIAL", "WEAK", "BENT", "none"])
    for i, name in ((1, "M-D"), (2, "M-C"), (3, "FR"), (4, "M0, lenient upgrade rule"), (5, "M0 without the mw tag")):
        tab(name + " by verdict", rows, lambda r: r["v"], lambda r, i=i: r["c"][i],
            ["supported", "contradicted", "contested", "untestable"])
    rated = [r for r in rows if r["c"][0] not in ("NE", "NR")]
    lv = LEVELS.index
    print("\nrated:", len(rated), " at the floor under M0:", sum(M0(r) == "very-low" for r in rated))
    print("same level under M0, M-D and M-C:", sum(len(set(r["c"][:3])) == 1 for r in rated),
          " M-D and M-C two or more levels apart:", sum(abs(lv(r["c"][1]) - lv(r["c"][2])) >= 2 for r in rated),
          sorted(r["id"] for r in rated if abs(lv(r["c"][1]) - lv(r["c"][2])) >= 2))
    print("M0 above M-C:", sorted(r["id"] for r in rated if lv(r["c"][0]) > lv(r["c"][2])),
          " M0 above M-D:", sorted(r["id"] for r in rated if lv(r["c"][0]) > lv(r["c"][1])))
    sc = [r for r in rows if r["v"] in ("supported", "contradicted")]
    for i, name in ((0, "M0"), (1, "M-D"), (2, "M-C")):
        print("over-stated under %s (supported or contradicted at low or very low):" % name,
              sorted(r["id"] for r in sc if r["c"][i] in ("low", "very-low")))
    print("over-stated under all three:", sorted(r["id"] for r in sc if all(x in ("low", "very-low") for x in r["c"][:3])))
    ct = [r for r in rows if r["v"] == "contested"]
    cls = collections.defaultdict(list)
    for r in ct:
        hi = M0(r) in ("moderate", "high")
        k = ("no evidence" if M0(r) == "NE" else
             ("lean, " if r["dir"] in ("for", "against") else "open, ") + ("moderate or high" if hi else "low or very low"))
        cls[k].append(r["id"])
    print("\ncontested rows:", len(ct))
    for k in sorted(cls):
        print("   %-28s %2d  %s" % (k, len(cls[k]), ", ".join(cls[k])))
    op = [r for r in ct if r["dir"] in ("cond", "mixed")]
    print("open rows by FR:", dict(collections.Counter(r["c"][3] for r in op)))
    print("direction:", dict(collections.Counter((r["v"], r["dir"]) for r in rows)))
    print("kind F:", sorted(r["id"] for r in rows if r["k"] == "F" and r["b"] != "N"))
    print("upgrade factors present:", sorted(r["id"] for r in rows if r["b"] != "N" and int(r["upf"])),
          " applied under M0:", sum(1 for r in rated if int(r["upf"]) and START_M0[(r["b"], r["k"])] == 1
                                     and not any(int(r[k]) for k in ("rob", "inc", "mw", "sp", "rd", "imp", "sel"))))
    print("domains downgraded (rated rows):", {k: sum(int(r[k]) > 0 for r in rated) for k in ("rob", "inc", "mw", "sp", "rd", "imp", "sel")},
          " ur:", sum(int(r["ur"]) for r in rated))
    tr = [r for r in rows if r["id"] in trial]
    print("\nproposal (c) trial rows:", len(tr))
    for r in sorted(tr, key=lambda r: r["id"]):
        print("   %-8s %-8s M0 %-9s FR %s" % (r["id"], r["dir"], M0(r), r["c"][3]))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sample"
    if cmd == "sample":
        sample()
    elif cmd == "count":
        count()
    else:
        sys.exit("unknown command")
