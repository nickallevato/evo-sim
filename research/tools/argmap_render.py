"""Render the argument map from docs/research/argmap/{lineage,defeaters}.yaml.

Writes
    docs/img/argmap/genealogy.svg   time-axis "family tree" of argument versions (swimlane per lineage)
    docs/arguments/defeaters.md     Mermaid attack graph per branch + grounded-extension tables (GENERATED)

Grounded extension (Dung 1995): the least fixed point of "accept every argument all of whose
attackers are rejected; reject every argument attacked by an accepted one".
It is computed three times: as argued (every attack), audited strict (upheld only) and audited lenient
(upheld or partly). The comparison shows how the picture shifts once attacks are checked. It is a summary of the recorded
data, not an extra verdict. Run:
    research/.venv/bin/python -I research/tools/argmap_render.py
"""
import datetime as dt
import html
import os
import re
import sys
from collections import defaultdict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "docs", "research", "argmap")
IMG = os.path.join(ROOT, "docs", "img", "argmap")
DOC = os.path.join(ROOT, "docs", "arguments")
INK, MUTE = "#8b949e", "#6e7681"
SIDE = {"day": "#f59e0b", "ally": "#d97706", "critic": "#3b82f6", "literature": "#a3a3a3", "audit": "#22c55e"}
SIDE_ORDER = ["literature", "day", "ally", "critic", "audit"]
FONT = "font-family='-apple-system,Segoe UI,Helvetica,Arial,sans-serif'"
LINEAR = {"descends", "revises"}          # edges that continue a lineage (same author, next version)
UPHELD = {"upheld", "partly"}
CHUNK = 26                                 # max attacks per Mermaid diagram


def load(name):
    p = os.path.join(SRC, name)
    return yaml.safe_load(open(p)) if os.path.exists(p) else []


def parse_date(s):
    s = str(s)
    for fmt, n in (("%Y-%m-%d", 10), ("%Y-%m", 7), ("%Y", 4)):
        try:
            return dt.datetime.strptime(s[:n], fmt).date()
        except ValueError:
            pass
    raise ValueError(f"bad date {s!r}")


def esc(s):
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- genealogy
BRANCH = {"ROOT": "Overall claim", "A": "A · MITTENS rate limit", "B": "B · Neutral rate (k vs μ)", "C": "C · Ancient DNA",
          "D": "D · Sequence space", "E": "E · Founders, mutators", "F": "F · Fix time vs throughput",
          "G": "G · Bernoulli Barrier", "H": "H · Cost of selection"}
# Three time bands: cited literature (by year rank, not to scale), 2019 to Nov 2025 (compressed),
# and Dec 2025 onward (to scale, by month), where most dated versions fall.
B1, B2 = dt.date(2019, 1, 1), dt.date(2025, 12, 1)
# Numbered markers on the figure; docs/arguments/README.md explains each, in this order.
CALLOUTS = ["L-wistar-mayr-1966", "L-mittens-2019", "L-camestros-arith-2026", "L-day-k-nne-blog-2026",
            "L-term3-retraction-2026", "L-keruru-retraction-2026", "L-day-concession-2026-08-27", "L-snv-only-2026",
            "L-edu-full-short-2026", "L-edu-32.3-2026", "L-kittens-linear-caveat-2026", "L-audit-double-count-2026",
            "L-audit-1-300-falsified-2026"]


def genealogy_svg(nodes, hier, out):
    end = max([parse_date(n["date"]) for n in nodes] + [dt.date(2026, 10, 8)]) + dt.timedelta(days=3)
    branch_of = lambda n: hier.get((n.get("claim_ids") or ["?"])[0], {}).get("branch", "ROOT")
    rows = sorted({(branch_of(n), n["side"]) for n in nodes},
                  key=lambda r: (list(BRANCH).index(r[0]) if r[0] in BRANCH else 99, SIDE_ORDER.index(r[1])))
    W, LBL, PAD, LH, TOP, GAP = 1400, 270, 24, 26, 64, 16
    lit_years = sorted({parse_date(n["date"]).year for n in nodes if parse_date(n["date"]) < B1}) or [1950]
    xa0, xa1 = LBL + 8, LBL + 8 + 150          # literature band
    xb0, xb1 = xa1 + 14, xa1 + 14 + 210        # 2019 to Nov 2025
    xc0, xc1 = xb1 + 14, W - PAD               # Dec 2025 onward: month widths grow with how many versions fall in them
    months, m = [], B2
    while m <= end:
        months.append((m.year, m.month))
        m = dt.date(m.year + (m.month == 12), m.month % 12 + 1, 1)
    per = defaultdict(int)
    for n in nodes:
        d = parse_date(n["date"])
        if d >= B2:
            per[(d.year, d.month)] += 1
    wts = [max(per[k], 3) ** 0.75 for k in months]
    medges = [xc0]
    for w in wts:
        medges.append(medges[-1] + w / sum(wts) * (xc1 - xc0))

    def x_of(d):
        d = parse_date(d)
        if d < B1:
            return xa0 + (lit_years.index(d.year) + 0.5) * (xa1 - xa0) / len(lit_years)
        if d < B2:
            return xb0 + (d - B1).days / (B2 - B1).days * (xb1 - xb0)
        i = months.index((d.year, d.month))
        last = (d.year, d.month) == months[-1]
        frac = (d.day - 1) / (end.day if last else 31)
        return medges[i] + frac * (medges[i + 1] - medges[i])

    ys, y, prev = {}, TOP, None              # row y positions, with a gap between topics
    for r in rows:
        if prev is not None and r[0] != prev:
            y += GAP
        ys[r] = y
        y += LH
        prev = r[0]
    H = y + 60
    pos, seen = {}, defaultdict(int)
    for n in sorted(nodes, key=lambda n: parse_date(n["date"])):
        r = (branch_of(n), n["side"])
        x = x_of(n["date"])
        k = (r, round(x / 5))                # nudge same-day versions apart vertically
        off = seen[k]
        seen[k] += 1
        pos[n["id"]] = (x, ys[r] + (0 if off == 0 else (-1) ** off * 4 * ((off + 1) // 2)))
    b = [f"<defs><marker id='ah' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='5' markerHeight='5' orient='auto-start-reverse'>"
         f"<path d='M0 0L10 5L0 10z' fill='{INK}'/></marker></defs>"]
    for x0, x1, lab in ((xa0, xa1, "cited literature (not to scale)"), (xb0, xb1, "2019 – Nov 2025"),
                        (xc0, xc1, "Dec 2025 – Oct 2026 (by month; busier months wider)")):
        b.append(f"<rect x='{x0 - 4}' y='{TOP - 18}' width='{x1 - x0 + 8}' height='{H - TOP - 36}' fill='{MUTE}' opacity='0.07' rx='4'/>")
        b.append(f"<text x='{(x0 + x1) / 2:.1f}' y='{TOP - 40}' font-size='12' fill='{INK}' text-anchor='middle'>{lab}</text>")
    for yr in lit_years:
        b.append(f"<text x='{x_of(str(yr)):.1f}' y='{TOP - 24}' font-size='9' fill='{MUTE}' text-anchor='middle'>{str(yr)[2:]}</text>")
    for yr in range(2019, 2026):
        b.append(f"<text x='{x_of(f'{yr}-07-01'):.1f}' y='{TOP - 24}' font-size='10' fill='{MUTE}' text-anchor='middle'>{str(yr)[2:]}</text>")
    m = B2
    while m <= end:
        x = x_of(m)
        b.append(f"<line x1='{x:.1f}' y1='{TOP - 18}' x2='{x:.1f}' y2='{H - 54}' stroke='{MUTE}' stroke-width='0.5' opacity='0.6'/>")
        b.append(f"<text x='{x + 3:.1f}' y='{TOP - 24}' font-size='10' fill='{MUTE}'>{m:%b}{' ' + str(m.year) if m.month == 1 else ''}</text>")
        m = dt.date(m.year + (m.month == 12), m.month % 12 + 1, 1)
    prev = None
    for r in rows:
        yy = ys[r]
        if r[0] != prev:
            b.append(f"<text x='{LBL - 78}' y='{yy + 4}' font-size='12' fill='{INK}' text-anchor='end' font-weight='bold'>{esc(BRANCH.get(r[0], r[0]))}</text>")
            prev = r[0]
        b.append(f"<text x='{LBL - 8}' y='{yy + 4}' font-size='11' fill='{SIDE.get(r[1], INK)}' text-anchor='end'>{r[1]}</text>")
        b.append(f"<line x1='{LBL}' y1='{yy}' x2='{W - PAD}' y2='{yy}' stroke='{MUTE}' stroke-width='0.4' opacity='0.35'/>")
    # edges within a topic; cross-topic links stay in the data but are left out of the picture
    by = {n["id"]: n for n in nodes}
    skipped = 0
    for n in nodes:
        for p in n.get("parents") or []:
            a, rel = p["id"], p.get("relation")
            if a not in pos:
                continue
            if branch_of(by[a]) != branch_of(n):
                skipped += 1
                continue
            (xa, ya), (xb, yb) = pos[a], pos[n["id"]]
            cx = (xa + xb) / 2
            if rel in LINEAR and by[a]["side"] == n["side"]:
                b.append(f"<path d='M{xa:.1f} {ya} C{cx:.1f} {ya} {cx:.1f} {yb} {xb:.1f} {yb}' fill='none' "
                         f"stroke='{SIDE.get(n['side'], INK)}' stroke-width='2.2' opacity='0.6'/>")
                continue
            col, dash, wdt, op = {"borrows": (SIDE.get(by[a]["side"], INK), "5 3", 1.6, 0.85), "responds-to": (INK, "2 3", 1, 0.55),
                                  "cites": (MUTE, "1 3", 0.8, 0.45), "resembles": (MUTE, "1 5", 0.8, 0.35)}.get(rel, (INK, "", 1, 0.5))
            b.append(f"<path d='M{xa:.1f} {ya} C{cx:.1f} {ya} {cx:.1f} {yb} {xb - 5:.1f} {yb}' fill='none' stroke='{col}' "
                     f"stroke-width='{wdt}' stroke-dasharray='{dash}' opacity='{op}' marker-end='url(#ah)'/>")
    for n in nodes:
        x, y = pos[n["id"]]
        col = SIDE.get(n["side"], INK)
        fate = n.get("fate") or "alive"
        if n.get("kind") in ("concession", "retraction"):
            shape = (f"<rect x='{x - 5:.1f}' y='{y - 5}' width='10' height='10' transform='rotate(45 {x:.1f} {y})' "
                     f"fill='{col}' stroke='{INK}' stroke-width='1'/>")
        elif fate in ("retracted", "conceded"):
            shape = (f"<circle cx='{x:.1f}' cy='{y}' r='5' fill='none' stroke='{col}' stroke-width='2'/>"
                     f"<path d='M{x - 4:.1f} {y - 4}L{x + 4:.1f} {y + 4}M{x + 4:.1f} {y - 4}L{x - 4:.1f} {y + 4}' stroke='{col}' stroke-width='1.6'/>")
        else:
            dash = " stroke-dasharray='2 1.5'" if fate == "dormant" else ""
            shape = (f"<circle cx='{x:.1f}' cy='{y}' r='4.5' fill='{col if fate == 'alive' else 'none'}' "
                     f"stroke='{col}' stroke-width='1.8'{dash}/>")
        b.append(f"<g><title>{esc(str(n['date']) + ' · ' + n['label'])}</title>{shape}</g>")
    for i, cid in enumerate(CALLOUTS, 1):
        if cid not in pos:
            continue
        x, y = pos[cid]
        dy = -13 if i % 2 else 13
        b.append(f"<circle cx='{x + 9:.1f}' cy='{y + dy}' r='7' fill='{INK}'/>"
                 f"<text x='{x + 9:.1f}' y='{y + dy + 3.5}' font-size='9.5' fill='#fff' text-anchor='middle' font-weight='bold'>{i}</text>")
    ly, lx = H - 24, LBL - 150
    items = [("<circle cx='0' cy='-4' r='4.5' fill='{c}'/>", "still asserted"),
             ("<circle cx='0' cy='-4' r='4.5' fill='none' stroke='{c}' stroke-width='1.8'/>", "revised or superseded"),
             ("<circle cx='0' cy='-4' r='4.5' fill='none' stroke='{c}' stroke-width='1.8' stroke-dasharray='2 1.5'/>", "dormant"),
             ("<path d='M-4 -8L4 0M4 -8L-4 0' stroke='{c}' stroke-width='1.6'/>", "later retracted or conceded"),
             ("<rect x='-5' y='-9' width='10' height='10' transform='rotate(45 0 -4)' fill='{c}'/>", "a concession or retraction"),
             ("<path d='M-12 -4H12' stroke='{c}' stroke-width='2.2'/>", "same author, next version"),
             ("<path d='M-12 -4H12' stroke='{c}' stroke-width='1.6' stroke-dasharray='5 3'/>", "borrowed from the other side"),
             ("<path d='M-12 -4H12' stroke='{c}' stroke-width='1' stroke-dasharray='2 3'/>", "responds to / cites")]
    for shp, lab in items:
        b.append(f"<g transform='translate({lx},{ly})'>{shp.format(c=INK)}</g><text x='{lx + 16}' y='{ly}' font-size='11' fill='{INK}'>{lab}</text>")
        lx += 30 + 6.0 * len(lab)
    s = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='Argument genealogy' {FONT}>"
         f"<title>Argument genealogy: dated versions of each argument, by topic and side</title>{''.join(b)}</svg>")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(s)
    return len(rows), skipped


# ---------------------------------------------------------------- defeaters
def grounded(args, attacks):
    """attacks: set of (attacker, target). Returns (IN, OUT, UNDEC)."""
    att = defaultdict(set)
    for a, t in attacks:
        att[t].add(a)
    IN, OUT = set(), set()
    changed = True
    while changed:
        changed = False
        for x in args:
            if x in IN or x in OUT:
                continue
            if att[x] <= OUT:
                IN.add(x); changed = True
            elif att[x] & IN:
                OUT.add(x); changed = True
    return IN, OUT, set(args) - IN - OUT


def registry():
    """x:/chk:/rev: ids from the 'Id registry' table in NOTES.md -> {id: {side, title}}."""
    out, on = {}, False
    p = os.path.join(SRC, "NOTES.md")
    for line in open(p) if os.path.exists(p) else []:
        if line.startswith("## "):
            on = line.strip() == "## Id registry"
        m = re.match(r"\|\s*((?:x|chk|rev):[^|\s]+)\s*\|\s*(\w+)\s*\|\s*([^|]*)\|", line) if on else None
        if m:
            out[m.group(1)] = {"side": m.group(2), "title": m.group(3).strip(), "branch": "other"}
    return out


def side_of(cid, hier):
    return hier.get(cid, {}).get("side", "audit" if cid.startswith(("chk:", "rev:")) else "literature")


def mid(cid):
    return re.sub(r"[^A-Za-z0-9]", "_", cid)


def chunks(ds, hier):
    """Split one branch's attacks into diagrams of at most ~CHUNK attacks, keeping all attacks on a target together.
    Yields (part number or 0 when unsplit, targets, attacks)."""
    by_t = defaultdict(list)
    for d in ds:
        by_t[d["target"]].append(d)
    parts, cur = [], []
    for t in sorted(by_t, key=lambda t: (hier.get(t, {}).get("parent") or "", t)):
        if cur and sum(len(by_t[x]) for x in cur) + len(by_t[t]) > CHUNK:
            parts.append(cur)
            cur = []
        cur.append(t)
    parts.append(cur)
    for i, targets in enumerate(parts, 1):
        yield (i if len(parts) > 1 else 0), targets, [d for t in targets for d in by_t[t]]


def defeaters_md(defs, hier, out):
    ARROW = {"undermining": ("-.->", "undermines"), "undercutting": ("==>", "undercuts"), "rebutting": ("-->", "rebuts")}
    args = sorted({d["attacker"] for d in defs} | {d["target"] for d in defs})
    argued = {(d["attacker"], d["target"]) for d in defs}
    audited = {(d["attacker"], d["target"]) for d in defs if d.get("audit_status") in UPHELD}
    gA, gB = grounded(args, argued), grounded(args, audited)
    lab = lambda S, x: "accepted" if x in S[0] else "rejected" if x in S[1] else "undecided"
    L = ["<!-- GENERATED by research/tools/argmap_render.py from docs/research/argmap/defeaters.yaml; do not edit by hand. -->",
         "# Objection graph (generated)", "",
         "Arrows run from an objection to what it attacks. Line style gives the type:",
         "- **dotted**: undermines (attacks a premise);",
         "- **thick**: undercuts (grants the premises, attacks the step from premises to conclusion);",
         "- **solid**: rebuts (argues for the opposite conclusion).", "",
         "Colours: orange = Day, amber = ally, blue = critic, green = this audit's checks, grey = literature.", ""]
    by_branch = defaultdict(list)
    for d in defs:
        by_branch[hier.get(d["target"], {}).get("branch", "other")].append(d)
    for br in sorted(by_branch, key=lambda b: (b == "other", b)):
        for pi, targets, ds in chunks(by_branch[br], hier):
            nodes = sorted({d["attacker"] for d in ds} | {d["target"] for d in ds})
            name = BRANCH.get(br, "Other: objections to audit checks and unregistered items" if br == "other" else br)
            L += [f"## {name}" + (f" (part {pi})" if pi else ""), "", f"Objections to {', '.join(targets)}.", "",
                  "```mermaid", "flowchart RL"]
            for s, c in SIDE.items():
                L.append(f"  classDef {s} fill:{c}22,stroke:{c},stroke-width:2px")
            for n in nodes:
                title = hier.get(n, {}).get("title", n)
                t = title.replace('"', "'")[:60] + ("…" if len(title) > 60 else "")
                L.append(f'  {mid(n)}["{n}: {t}"]:::{side_of(n, hier)}')
            for d in ds:
                arrow, verb = ARROW.get(d["type"], ("-->", d["type"]))
                L.append(f'  {mid(d["attacker"])} {arrow}|"{verb} · {d.get("audit_status", "untested")}"| {mid(d["target"])}')
            L += ["```", ""]
    strict = {(d["attacker"], d["target"]) for d in defs if d.get("audit_status") == "upheld"}
    gS = grounded(args, strict)
    L += ["## Which arguments survive their objections", "",
          "This uses grounded semantics (Dung 1995): an argument is *accepted* when every attacker is rejected, *rejected* when an accepted argument attacks it, and *undecided* otherwise (for example, mutual attacks that nothing settles). Three readings:",
          "- **As argued** counts every recorded attack.",
          "- **Audited, strict** counts only the attacks this audit's checks upheld in full.",
          "- **Audited, lenient** also counts attacks upheld in part.", "",
          "**Read with care.** Grounded semantics is all-or-nothing: one surviving objection to one premise rejects the whole argument, even when the objection only trims a number. "
          "These columns summarise the recorded objections. They are not a separate verdict; the claim files' three verdicts remain the reference. Claims without recorded objections are not listed.", ""]
    cols = (("as argued", gA), ("audited, strict", gS), ("audited, lenient", gB))
    L += ["| Side | " + " | ".join(f"{c}: accepted / rejected / undecided" for c, _ in cols) + " |", "|---|---|---|---|"]
    for sd in SIDE_ORDER:
        xs = [a for a in args if side_of(a, hier) == sd]
        if xs:
            L.append(f"| {sd} ({len(xs)}) | " + " | ".join(
                f"{sum(a in g[0] for a in xs)} / {sum(a in g[1] for a in xs)} / {sum(a in g[2] for a in xs)}" for _, g in cols) + " |")
    # Dung frameworks have no support relation, so a rejected sub-claim does not reach the claim it supports.
    # The last column lists, for each claim, its supporting / depended-on claims rejected under the lenient reading.
    deps = defaultdict(set)
    for n in hier.values():
        for e in n.get("edges") or []:
            if e.get("type") == "supports":
                deps[e["target"]].add(n["id"])
            elif e.get("type") == "depends-on":
                deps[n["id"]].add(e["target"])
    L += ["", "**Support is not modelled by Dung's framework.** A claim can be *accepted* (no surviving direct objection) while claims it rests on are rejected. "
          "The last column lists those rejected supports (lenient reading), so read both together. ROOT, for instance, draws few direct objections; most objections target its supports.", "",
          "Load-bearing claims are in **bold**.", "",
          "| Claim | Side | " + " | ".join(c.capitalize() for c, _ in cols) + " | Rejected supports (lenient) |", "|---|---|---|---|---|---|"]
    for a in args:
        nm = f"**{a}**" if hier.get(a, {}).get("load_bearing") else a
        rej = sorted(x for x in deps.get(a, ()) if x in gB[1])
        L.append(f"| {nm} | {side_of(a, hier)} | " + " | ".join(lab(g, a) for _, g in cols) + f" | {', '.join(rej) or '–'} |")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(L) + "\n")
    return gA, gS, gB


def main():
    lineage, defs = load("lineage.yaml") or [], load("defeaters.yaml") or []
    hier = {n["id"]: n for n in (yaml.safe_load(open(os.path.join(ROOT, "docs", "research", "hierarchy.yaml")))["nodes"])}
    hier.update(registry())
    if lineage:
        k, skipped = genealogy_svg(lineage, hier, os.path.join(IMG, "genealogy.svg"))
        print(f"genealogy: {len(lineage)} nodes, {k} rows, {skipped} cross-topic links left out of the picture")
    if defs:
        for name, g in zip(("as argued", "audited, strict", "audited, lenient"), defeaters_md(defs, hier, os.path.join(DOC, "defeaters.md"))):
            print(f"grounded {name:17s} accepted/rejected/undecided:", *map(len, g))
    if not (lineage or defs):
        sys.exit("no data in docs/research/argmap/")


if __name__ == "__main__":
    main()
