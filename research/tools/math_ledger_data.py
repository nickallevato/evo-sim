"""Write the data files behind the "Evo-sim Math Ledger" dashboard (read-only over the repo).

Usage (repo root): research/.venv/bin/python -I research/tools/math_ledger_data.py
Writes docs/research/math/ledger/{burndown,branches,checks,objects,phases}.json.
Sources: git history of hierarchy.yaml, hierarchy.yaml, PREREG-STATUS.md,
math/pilot/{A,V}/objects.yaml, math/REMAINING.md (phases are transcribed from it).
"""
import collections
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/research/math/ledger"
DATES = ["2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13",
         "2026-10-16", "2026-10-19", "2026-10-25", "2026-10-31"]


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, check=True).stdout


def tally(nodes):
    pend = sum(1 for n in nodes for v in (n.get("verdicts") or {}).values() if v == "pending")
    lb = [n for n in nodes if n.get("load_bearing")]
    lbo = sum(1 for n in lb if n.get("status") != "reviewed" or "pending" in (n.get("verdicts") or {}).values())
    return pend, len(lb), lbo


def burndown():
    rows = []
    for d in DATES:
        c = git("log", "-1", "--format=%h", f"--before={d} 23:59", "--", "docs/research/hierarchy.yaml").strip()
        nodes = yaml.safe_load(git("show", f"{c}:docs/research/hierarchy.yaml"))["nodes"]
        pend, lb, lbo = tally(nodes)
        rows.append({"date": d, "commit": c, "nodes": len(nodes), "pending_fields": pend,
                     "load_bearing": lb, "load_bearing_open": lbo})
    return rows


def branches():
    nodes = yaml.safe_load((ROOT / "docs/research/hierarchy.yaml").read_text())["nodes"]
    by = collections.defaultdict(list)
    for n in nodes:
        by[n["branch"]].append(n)
    rows = []
    for b in sorted(by):
        ns = by[b]
        st = collections.Counter(n.get("status") for n in ns)
        pend, lb, lbo = tally(ns)
        rows.append({"branch": b, "nodes": len(ns), "reviewed": st.get("reviewed", 0),
                     "checked": st.get("checked", 0), "extracted": st.get("extracted", 0) + st.get("draft", 0),
                     "pending_fields": pend, "load_bearing": lb, "load_bearing_open": lbo})
    return rows


def checks():
    txt = (ROOT / "research/checks/PREREG-STATUS.md").read_text().split("## Table", 1)[1]
    rows = []
    for line in txt.splitlines():
        if not line.startswith("| ") or line.startswith("| Check") or line.startswith("|---"):
            continue
        c = [x.strip() for x in line.strip("|").split("|")]
        rows.append({"check": c[0].strip("`* "), "tier": c[1], "script": c[2].strip("`"),
                     "result_commit": c[4].strip("`"), "label": c[8].strip("*"), "status": "calculated"})
    # Registered after PREREG-STATUS.md was last regenerated (2026-10-18); state from git log 2026-10-13..19.
    later = [("FMnull-S4", "fmnull_s4.py", "written up, reviewed; fix pass pending"),
             ("L3", "l3_amk.py", "run collected; not written up"),
             ("L1c-b", "l1c_extaln.py", "registered; not written up"),
             ("C1d-fu", "c1d_tv.py", "registered; not written up"),
             ("D-fu", "d_followups.py", "registered; not written up"),
             ("L5-C1a", "l5_c1a_randsnp.py", "smoke only; not written up")]
    for name, script, state in later:
        if not any(r["check"] == name for r in rows):
            rows.append({"check": name, "tier": "", "script": script, "result_commit": "",
                         "label": state, "status": "in flight"})
    return rows


def objects():
    rows = []
    for tag, path in (("Branch A claims", "A"), ("Video vid02", "V")):
        objs = yaml.safe_load((ROOT / f"docs/research/math/pilot/{path}/objects.yaml").read_text())["objects"]
        for o in objs:
            c = o.get("compute") or {}
            rows.append({"key": f"{path}:{o['id']}", "map": tag, "id": o["id"], "kind": o["kind"],
                         "resolution": o["resolution"], "status": o["status"],
                         "statement": str(o["statement"])[:220], "nodes": ", ".join(o.get("used_by") or []),
                         "resolved_by": o.get("resolved_by") or "", "cpu_h": float(c.get("est_cpu_h") or 0)})
    return rows


def phases():
    return [
        {"phase": "P1", "work": "Map the other 8 branches into math objects, then merge", "size": "191 claims; ~0.45M Sonnet tokens", "cpu_h_low": 0, "cpu_h_high": 0, "basis": "projected", "blocked": ""},
        {"phase": "P1b", "work": "Map new sources (vid02 merge; Probability Zero 2nd ed.)", "size": "one pass per source", "cpu_h_low": 0, "cpu_h_high": 0, "basis": "projected", "blocked": "owner: book text"},
        {"phase": "P2", "work": "Settle derivation and lookup objects", "size": "~60-90 objects", "cpu_h_low": 0, "cpu_h_high": 0, "basis": "projected", "blocked": "some outside"},
        {"phase": "P3", "work": "One simulation/regression campaign", "size": "~10-15 runs", "cpu_h_low": 1000, "cpu_h_high": 3000, "basis": "projected from branch A (2 runs, 310 CPU-h)", "blocked": ""},
        {"phase": "P4", "work": "Roll-ups ROOT, ROOT-M, ROOT-FM", "size": "3 nodes", "cpu_h_low": 0, "cpu_h_high": 0, "basis": "measured", "blocked": "P2, P3"},
        {"phase": "P5", "work": "R5 synthesis: sensitivity table = simulator variable list", "size": "1 table", "cpu_h_low": 0, "cpu_h_high": 0, "basis": "planned", "blocked": "P4"},
    ]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in (("burndown", burndown), ("branches", branches), ("checks", checks),
                     ("objects", objects), ("phases", phases)):
        rows = fn()
        (OUT / f"{name}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
        print(name, len(rows))


if __name__ == "__main__":
    main()
