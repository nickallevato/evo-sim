"""grade_certainty.py: sample and counts for docs/research/criticality/grade-certainty-2026-10-12.md (read-only).

    research/.venv/bin/python -I research/tools/grade_certainty.py sample
    research/.venv/bin/python -I research/tools/grade_certainty.py count

`sample` prints the frame and the seeded, stratified sample of 30 decided external verdicts on claim files
that are not load-bearing. It was committed with the adaptation, before any rating.
`count` (added with part 2) re-computes every certainty in the summary-of-findings table from its code
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


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sample"
    if cmd == "sample":
        sample()
    else:
        sys.exit("unknown command (part 2 adds `count`)")
