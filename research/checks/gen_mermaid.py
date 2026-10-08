"""Generate docs/research/hierarchy/*.md Mermaid diagrams from hierarchy.yaml (THROWAWAY tooling)."""
import os, re, yaml, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
nodes = yaml.safe_load(open(os.path.join(ROOT, "docs/research/hierarchy.yaml")))["nodes"]
out = os.path.join(ROOT, "docs/research/hierarchy"); os.makedirs(out, exist_ok=True)
STYLE = {"day": "fill:#fde2c8,stroke:#b45309", "ally": "fill:#fef3c7,stroke:#a16207",
         "critic": "fill:#dbeafe,stroke:#1d4ed8", "literature": "fill:#e5e7eb,stroke:#374151"}
ARROW = {"supports": "-->|supports|", "attacks": "-.->|attacks|", "revises": "==>|revises|",
         "supersedes": "==>|supersedes|", "depends-on": "-->|depends-on|"}
sid = lambda i: "n_" + re.sub(r"\W", "_", str(i))
def label(n):
    v = n.get("verdicts") or {}
    t = str(n.get("title", ""))[:60].replace('"', "'")
    return f'{n["id"]}: {t}<br/><small>{n.get("side")} · int:{v.get("internal")} · fid:{v.get("fidelity")} · ext:{v.get("external")}</small>'
by_branch = collections.defaultdict(list)
for n in nodes:
    b = str(n.get("branch") or str(n["id"])[0])
    by_branch["ROOT" if str(n["id"]).startswith("ROOT") else b[0]].append(n)
ids = {str(n["id"]): n for n in nodes}
index = ["# Claim Hierarchy (generated)\n", "Generated from `hierarchy.yaml` by `research/checks/gen_mermaid.py`.\n",
         "Colors: Day = orange, ally = yellow, critic = blue, literature = gray. A dashed arrow means *attacks*.\n",
         "| Branch | Claims | Load-bearing |", "|---|---|---|"]
for b, ns in sorted(by_branch.items()):
    lines = ["```mermaid", "flowchart TD"]
    present = {str(n["id"]) for n in ns}
    ext = set()
    for n in ns:
        lines.append(f'  {sid(n["id"])}["{label(n)}"]')
        lines.append(f'  style {sid(n["id"])} {STYLE.get(n.get("side"), "")}' + (",stroke-width:3px" if n.get("load_bearing") else ""))
        par = n.get("parent")
        if par and str(par) != "None":
            if str(par) not in present: ext.add(str(par))
            lines.append(f'  {sid(n["id"])} --> {sid(par)}')
        for e in n.get("edges") or []:
            t = str(e.get("target"))
            if t not in present: ext.add(t)
            lines.append(f'  {sid(n["id"])} {ARROW.get(e.get("type"), "-->")} {sid(t)}')
    for t in sorted(ext):
        lines.append(f'  {sid(t)}(["{t} (other branch)"])')
    lines.append("```")
    fn = f"branch-{b}.md"
    open(os.path.join(out, fn), "w").write(f"# Branch {b}\n\n" + "\n".join(lines) + "\n")
    index.append(f"| [{b}]({fn}) | {len(ns)} | {', '.join(sorted(str(n['id']) for n in ns if n.get('load_bearing')))} |")
open(os.path.join(out, "README.md"), "w").write("\n".join(index) + "\n")
print("wrote", len(by_branch), "branch diagrams")
