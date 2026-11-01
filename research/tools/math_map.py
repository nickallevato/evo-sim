"""Math map: lint docs/research/math/objects.yaml and print what is left to do.

Usage (repo root):  research/.venv/bin/python -I research/tools/math_map.py [--lint] [FILE]
  default FILE = docs/research/math/objects.yaml (a pilot file may be passed instead)
  --lint   exit 1 on schema errors or used_by ids that are not hierarchy nodes
Read-only.
"""
import collections
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
KINDS = {"identity", "formula", "parameter", "model-choice", "inference", "empirical"}
RES = {"derivation", "lookup", "simulation", "regression", "data-check", "rhetoric"}
STATUS = {"open", "resolved", "blocked"}


def load(path):
    data = yaml.safe_load(Path(path).read_text()) or []
    return data["objects"] if isinstance(data, dict) else data


def lint(objs):
    nodes = {n["id"] for n in yaml.safe_load((ROOT / "docs/research/hierarchy.yaml").read_text())["nodes"]}
    errs, seen = [], set()
    for o in objs:
        oid = o.get("id", "?")
        if oid in seen:
            errs.append(f"{oid}: duplicate id")
        seen.add(oid)
        for key, allowed in (("kind", KINDS), ("resolution", RES), ("status", STATUS)):
            if o.get(key) not in allowed:
                errs.append(f"{oid}: {key}={o.get(key)!r} not in {sorted(allowed)}")
        pos = o.get("positions") or {}
        if not pos.get("day") or not pos.get("critic"):
            errs.append(f"{oid}: positions must fill both day and critic")
        for u in o.get("used_by") or []:
            if u not in nodes:
                errs.append(f"{oid}: used_by {u} is not a hierarchy node")
        if o.get("resolution") in ("simulation", "regression") and not o.get("compute"):
            errs.append(f"{oid}: simulation/regression needs a compute estimate")
    return errs


def summary(objs):
    by = collections.Counter((o.get("resolution"), o.get("status")) for o in objs)
    print(f"{len(objs)} objects")
    for res in sorted(RES):
        row = {s: by.get((res, s), 0) for s in sorted(STATUS)}
        if sum(row.values()):
            print(f"  {res:11} " + "  ".join(f"{s}={n}" for s, n in row.items()))
    cpu = collections.defaultdict(float)
    for o in objs:
        c = o.get("compute") or {}
        if o.get("status") != "resolved" and c:
            cpu[c.get("host", "?")] += float(c.get("est_cpu_h") or 0)
    if cpu:
        print("open compute (estimated CPU-h, unmeasured unless marked):")
        for h, v in sorted(cpu.items()):
            print(f"  {h:14} {v:10.1f}")
    nodes = collections.Counter(u for o in objs for u in (o.get("used_by") or []))
    print(f"nodes covered: {len(nodes)}; objects shared by >1 node: {sum(1 for o in objs if len(o.get('used_by') or []) > 1)}")


def main(argv):
    do_lint = "--lint" in argv
    files = [a for a in argv if not a.startswith("--")]
    path = files[0] if files else ROOT / "docs/research/math/objects.yaml"
    objs = load(path)
    errs = lint(objs)
    for e in errs:
        print("ERROR", e)
    summary(objs)
    return 1 if (do_lint and errs) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
