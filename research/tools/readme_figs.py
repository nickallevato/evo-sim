"""Render the README figures (docs/img/*.svg) from committed check outputs.

Every number plotted is read from research/checks/results/ or copied from the
reviewed tables in research/checks/RESULTS.md (cited inline). Run:
    research/.venv/bin/python -I research/tools/readme_figs.py
"""
import glob, json, os, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RES = os.path.join(ROOT, "research", "checks", "results")
OUT = os.path.join(ROOT, "docs", "img")
os.makedirs(OUT, exist_ok=True)

# Mid-grey ink + transparent background reads on both GitHub light and dark themes.
INK = "#8b949e"
DAY, CRIT, NEU, ACC = "#e8833a", "#3b82f6", "#a3a3a3", "#22c55e"
plt.rcParams.update({
    "svg.fonttype": "none", "font.family": "DejaVu Sans", "font.size": 11,
    "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": INK,
    "xtick.color": INK, "ytick.color": INK, "axes.facecolor": "none",
    "figure.facecolor": "none", "savefig.transparent": True,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), format="svg", metadata={"Date": None})
    plt.close(fig)


# 1. B1 empty vs full pipeline (RESULTS.md, B1 table; N=100, U=0.5, 60 reps)
T = [200, 400, 1000, 2000]
UT = [100, 200, 500, 1000]
day = [2.6, 41.6, 304.5, 802.7]
empty = [2.8, 41.3, 304.4, 802.5]
full = [99.3, 198.5, 501.0, 1005.1]
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot(T, UT, color=NEU, lw=1.5, ls="--", label="U·T  (neutral k = μ)")
ax.plot(T, day, color=DAY, lw=2, label="Day: U∫F_X dt  (analytic)")
ax.plot(T, empty, "o", color=DAY, mfc="none", ms=8, label="sim, empty start")
ax.plot(T, full, "s", color=CRIT, ms=6, label="sim, equilibrium start")
ax.set_xlabel("generations T  (N = 100, 4N = 400)")
ax.set_ylabel("substitutions")
ax.set_title("B1 · Day's formula is exact — for an empty pipe", color=INK, fontsize=11)
ax.legend(fontsize=9)
save(fig, "b1_pipeline.svg")

# 2. B1b size changes (RESULTS.md, B1b table)
sc = ["constant", "bottleneck", "contraction\nN0→N0/5", "expansion\nN0/5→N0", "founder"]
sim = [0.996, 0.999, 1.259, 0.733, 0.996]
ana = [1, 1, 1.267, 0.733, 1]
fig, ax = plt.subplots(figsize=(6.4, 3.4))
x = range(len(sc))
ax.bar([i - 0.18 for i in x], sim, 0.36, color=CRIT, label="simulated")
ax.bar([i + 0.18 for i in x], ana, 0.36, color=NEU, label="analytic 1 + 4ΔN/T")
ax.axhline(1, color=INK, lw=0.8, ls=":")
ax.set_xticks(list(x)); ax.set_xticklabels(sc, fontsize=9)
ax.set_ylabel("cumulative K / (U·T)")
ax.set_title("B1b · expansions lag, contractions overshoot", color=INK, fontsize=11)
ax.legend(fontsize=9, loc="upper left")
save(fig, "b1b_demography.svg")

# 3. B4a divergence vs ancestral Ne: d = 2μT + 4·Ne_anc·μ (sim matches within 0.3%)
mu, Tg = 1.2e-8, 252000
ne = [i * 1e3 for i in range(5, 241)]
d = [100 * (2 * mu * Tg + 4 * n * mu) for n in ne]
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.plot([n / 1e3 for n in ne], d, color=CRIT, lw=2, label="2μT + θ_anc  (sim agrees ±0.3%)")
ax.axhline(1.23, color=ACC, lw=1.5, label="observed 1.23% (CSAC 2005)")
ax.axhline(100 * 2 * mu * Tg, color=NEU, ls="--", lw=1, label="2μT alone = 0.60%")
ax.axhline(0.51, color=DAY, ls=":", lw=1.5, label="Day: 2μ(T − 4Nₑ) = 0.51%")
for n, lab in [(1e4, "Nₑ 1e4\n0.65%"), (1.98e5, "Yoo HCB\n1.55%")]:
    y = 100 * (2 * mu * Tg + 4 * n * mu)
    ax.plot(n / 1e3, y, "o", color=CRIT); ax.annotate(lab, (n / 1e3, y), xytext=(8, -4), textcoords="offset points", fontsize=8.5)
nfit = (0.0123 - 2 * mu * Tg) / (4 * mu)
ax.axvline(nfit / 1e3, color=ACC, lw=0.8, ls=":")
ax.annotate(f"fit ≈ {nfit/1e3:.0f}k", (nfit / 1e3, 0.35), xytext=(4, 0), textcoords="offset points", fontsize=8.5)
ax.set_xlabel("ancestral Nₑ (thousands)   μ = 1.2e-8, T = 252k gens")
ax.set_ylabel("human–chimp divergence (%)")
ax.set_ylim(0.3, 1.8)
ax.set_title("B4a · divergence = new mutations + ancestral polymorphism", color=INK, fontsize=11)
ax.legend(fontsize=8.5, loc="upper left")
save(fig, "b4a_divergence.svg")

# 4. F2 interference (results/raw/f2.out, s = 0.01 rows)
rows = {}
for line in open(os.path.join(RES, "raw", "f2.out")):
    p = [c.strip() for c in line.split("|")]
    if len(p) > 9 and p[1] == "0.01":
        rows.setdefault(p[2], []).append((float(p[3]), float(p[8]), float(p[9])))
lab = {"free": ("free recombination", ACC), "1.5": ("1.5 Morgan map", CRIT),
       "0.1": ("0.1 Morgan map", NEU), "clonal": ("clonal (no recombination)", DAY)}
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for k in ["free", "1.5", "0.1", "clonal"]:
    xs, ys, es = zip(*rows[k])
    ax.errorbar(xs, ys, yerr=es, marker="o", color=lab[k][1], label=lab[k][0], capsize=2)
ax.axhline(1, color=INK, lw=0.8, ls=":")
ax.set_xscale("log"); ax.set_ylim(0, 1.15)
ax.set_xlabel("beneficial supply 2N·U_b  (N = 1000, s = 0.01)")
ax.set_ylabel("R_int = rate / independent-sites rate")
ax.set_title("F2 · interference caps asexuals, not recombiners", color=INK, fontsize=11)
ax.legend(fontsize=9, loc="lower left")
save(fig, "f2_interference.svg")

# 5. H2 hard-selection persistence (results/h2_summary_*.json, s = 0.01, no deleterious load)
pts = []
for f in sorted(glob.glob(os.path.join(RES, "h2_summary_*.json"))):
    for r in json.load(open(f)):
        if r.get("mode") == "hard" and r.get("s") == 0.01 and not r.get("U_del") and r.get("sv") is None:
            pts.append((r["R"], r["lam"], r["ext_frac"]))
import math
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ok = [(R, l) for R, l, e in pts if e < 0.5]
bad = [(R, l) for R, l, e in pts if e >= 0.5]
if ok: ax.plot(*zip(*ok), "o", color=ACC, label="persists")
if bad: ax.plot(*zip(*bad), "x", color=DAY, ms=8, mew=2, label="goes extinct")
Rs = [1.05 + i * 0.05 for i in range(0, 400)]
ax.plot(Rs, [math.log(R) / 7.0 for R in Rs], color=INK, lw=1.2, ls="--", label="λ·D = ln R  (D ≈ 7)")
ax.axhline(1 / 300, color=CRIT, lw=1.5, label="Haldane 1/300")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("max offspring per parent R"); ax.set_ylabel("imposed sweeps λ per generation")
ax.set_title("H2 · hard-selection cap is ln R / D, not a flat 1/300", color=INK, fontsize=11)
ax.legend(fontsize=8.5, loc="lower right")
save(fig, "h2_persistence.svg")

# 6. Verdict tallies, read from the lint_research.py "verdicts:" line (same source as the
# lint tally; n/a verdicts not drawn). Segment order and colours are fixed here; counts are not.
import subprocess, sys
_lint = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "research", "checks", "lint_research.py")],
                       capture_output=True, text=True, cwd=ROOT)
_line = next((l for l in _lint.stdout.splitlines() if l.startswith("verdicts:")), None)
if _line is None:
    raise SystemExit("readme_figs: no 'verdicts:' line from lint_research.py")
_cl = next((l for l in _lint.stdout.splitlines() if l.startswith("claims:")), None)
if _cl is None:
    raise SystemExit("readme_figs: no 'claims:' line from lint_research.py")
N_CLAIMS = int(_cl[len("claims:"):].split()[0])
live = {}
for item in _line[len("verdicts:"):].split(","):
    key, n = item.strip().rsplit("=", 1)
    field, val = key.split(":", 1)
    live[(field, val)] = int(n)
_layout = {
    "internal": [("holds", "holds", ACC), ("non-sequitur", "non-sequitur", DAY), ("arithmetic error", "arithmetic-error", "#ef4444"), ("pending", "pending", "#525252")],
    "fidelity": [("accurate", "accurate", ACC), ("partial", "partial", "#eab308"), ("misread", "misread", DAY), ("unverifiable", "unverifiable", "#525252"), ("pending", "pending", "#3f3f46")],
    "external": [("supported", "supported", ACC), ("contested", "contested", "#eab308"), ("contradicted", "contradicted", DAY), ("untestable", "untestable", NEU), ("pending", "pending", "#525252")],
}
tallies = {f: [(label, live.get((f, val), 0), c) for label, val, c in segs] for f, segs in _layout.items()}
_drawn = {(f, v) for f, segs in _layout.items() for _, v, _ in segs} | {(f, "n/a") for f in _layout}
_extra = sorted(set(live) - _drawn)
if _extra:
    raise SystemExit(f"readme_figs: lint reports verdict values the figure does not draw: {_extra}")
fig, ax = plt.subplots(figsize=(7.2, 2.6))
for i, (k, segs) in enumerate(tallies.items()):
    left = 0
    for name, n, c in segs:
        ax.barh(i, n, left=left, color=c, height=0.6)
        if n >= 20:
            ax.text(left + n / 2, i, f"{name}\n{n}", ha="center", va="center", fontsize=7.5, color="white")
        elif n >= 5:
            ax.text(left + n / 2, i, str(n), ha="center", va="center", fontsize=7.5, color="white")
        left += n
ax.set_yticks(range(3)); ax.set_yticklabels(list(tallies)); ax.invert_yaxis()
ax.set_xlabel("claim verdicts (all sides; n/a omitted)")
ax.set_title("Scorecard · three verdicts per claim, both sides", color=INK, fontsize=11)
save(fig, "verdicts.svg")
# ---------------------------------------------------------------------------
# 7-9. Systems, verdict-logic and roadmap diagrams (hand-built SVG, 2026-10-12).
# Plain-string SVG: no random ids, no timestamps, so reruns are byte-identical.
# Mid-grey text and translucent fills read on GitHub light and dark themes.
# ---------------------------------------------------------------------------
TXT = "#6e7681"
C_CORE, C_DAY, C_CRIT, C_LAYER, C_PROP, C_OK = "#3b82f6", "#e8833a", "#22c55e", "#8b5cf6", "#eab308", "#22c55e"


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class _Svg:
    def __init__(self, w, h, title):
        self.w, self.h, self.parts = w, h, []
        self.title = title
        self.defs = ('<defs>'
                     '<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                     '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
                     '<marker id="ahp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                     '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % (TXT, C_PROP))

    def box(self, x, y, w, h, lines, color=C_CORE, dashed=False, bold=True, size=11, op=0.16, rx=8):
        d = ' stroke-dasharray="5 3"' if dashed else ""
        self.parts.append('<rect x="%g" y="%g" width="%g" height="%g" rx="%d" fill="%s" fill-opacity="%g" stroke="%s" stroke-width="1.5"%s/>'
                          % (x, y, w, h, rx, color, op, color, d))
        n = len(lines)
        lh = size + 3
        y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.35
        for i, t in enumerate(lines):
            wt = ' font-weight="700"' if (bold and i == 0) else ""
            sz = size if i == 0 else size - 1
            self.parts.append('<text x="%g" y="%g" text-anchor="middle" font-size="%g"%s>%s</text>'
                              % (x + w / 2, y0 + i * lh, sz, wt, _esc(t)))

    def text(self, x, y, t, size=10, anchor="middle", bold=False, color=None):
        c = ' fill="%s"' % color if color else ""
        wt = ' font-weight="700"' if bold else ""
        self.parts.append('<text x="%g" y="%g" text-anchor="%s" font-size="%g"%s%s>%s</text>' % (x, y, anchor, size, wt, c, _esc(t)))

    def arrow(self, pts, dashed=False, proposed=False, label=None, lpos=None):
        col = C_PROP if proposed else TXT
        d = ' stroke-dasharray="4 3"' if (dashed or proposed) else ""
        m = "ahp" if proposed else "ah"
        path = "M" + " L".join("%g,%g" % p for p in pts)
        self.parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.4"%s marker-end="url(#%s)"/>' % (path, col, d, m))
        if label:
            lx, ly = lpos if lpos else pts[len(pts) // 2]
            self.text(lx, ly, label, size=9)

    def band(self, x, y, w, h, color, label):
        self.parts.append('<rect x="%g" y="%g" width="%g" height="%g" rx="14" fill="%s" fill-opacity="0.07" stroke="%s" stroke-width="1.5" stroke-dasharray="8 4"/>'
                          % (x, y, w, h, color, color))
        self.text(x + 14, y + 20, label, size=12, anchor="start", bold=True, color=color)

    def save(self, name):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
               'font-family="DejaVu Sans, Verdana, sans-serif" fill="%s" role="img" aria-label="%s">'
               % (self.w, self.h, self.w, self.h, TXT, _esc(self.title)))
        svg += "<title>%s</title>" % _esc(self.title) + self.defs + "".join(self.parts) + "</svg>\n"
        with open(os.path.join(OUT, name), "w") as f:
            f.write(svg)


def _prereg_total():
    import re
    m = re.search(r"^\| \*\*total\*\* \| \*\*(\d+)\*\* \|", open(os.path.join(ROOT, "research", "checks", "PREREG-STATUS.md")).read(), re.M)
    if m is None:
        raise SystemExit("readme_figs: no total row in PREREG-STATUS.md")
    return int(m.group(1))


def _last_decision():
    import re
    ids = [int(n) for n in re.findall(r"\bD-(\d+)\b", open(os.path.join(ROOT, "docs", "research", "DECISIONS.md")).read(), re.M)]  # table rows stop at D-25; later ones are in headings and prose
    if not ids:
        raise SystemExit("readme_figs: no D-NN ids in DECISIONS.md")
    return max(ids)


def systems_diagram():
    # Known stale literals below, found by EVO-97/98/99 and deliberately left (EVO-85 ruling,
    # 2026-10-18): the figure must not generate an unbounded task chain. Fix them opportunistically
    # the next time this function is edited for another reason, not as work of their own.
    #   "Method audit MA-01..20"  — the audit now runs to MA-30.
    #   "Triveritas critique TV-01..11"
    #   "24 h cooling-off"        — O-6's actual period is the one in DECISIONS.md.
    #   "proposals a-f"
    #   "O-1..9 open"             — probably wrong, and not parseable: O-5 and O-8 are decided and
    #                               DECISIONS.md carries ids past O-24, but no file records which O
    #                               items are open. Needs a lead ruling on what "open" means first.
    g = _Svg(1010, 640, "evo-sim audit systems diagram: sources to simulator spec, with the criticality layer over all of it")
    w, h = 140, 64
    # Row A: the evidence-to-synthesis pipeline
    xs = [20, 190, 360, 530, 700, 870]
    g.box(xs[0], 40, w, h, ["Sources", "Day · critics · literature", "(book not yet read)"], C_DAY)
    g.box(xs[1], 40, w, h, ["Verbatim quotes", "locator + date + sha256", "no full texts in git"], C_CORE)
    g.box(xs[2], 40, w, h, ["Claims (%d)" % N_CLAIMS, "3 verdicts each:", "internal · fidelity · external"], C_CORE)
    g.box(xs[3], 40, w, h, ["Argument tree + map", "branches A-H, defeaters,", "lineage, standard forms"], C_CORE)
    g.box(xs[4], 40, w, h, ["Synthesis (R5)", "sensitivity table,", "aggregation + stopping rule"], C_CRIT)
    g.box(xs[5], 40, 120, h, ["Simulator spec", "variable list", "(next phase)"], C_CRIT)
    for i in range(5):
        g.arrow([(xs[i] + w, 72), (xs[i + 1], 72)])
    # Row B: checking machinery
    g.box(20, 180, 310, 64, ["Hard rules", "both sides equal scrutiny · verbatim quotes only · pre-register", "no outward action without owner approval"], C_DAY, bold=True, size=11)
    g.box(360, 180, w, h, ["Checks", "pre-register → run", "→ write-up (+ post hoc)"], C_CORE)
    g.box(530, 180, w, h, ["Reviews", "load-bearing: 3 reviews", "low-stakes: 1 combined"], C_CORE)
    g.box(700, 180, w, h, ["Verdict rule", "R1 S SC N F U C", "RH (tag) · RD (readings)"], C_CORE)
    g.box(870, 180, 120, h, ["Ledgers", "slips · fidelity", "balance · versions · gaps"], C_CORE)
    g.arrow([(390, 104), (390, 180)])
    g.arrow([(500, 212), (530, 212)])
    g.arrow([(670, 212), (700, 212)])
    g.arrow([(840, 212), (870, 212)])
    g.arrow([(770, 180), (770, 150), (470, 150), (470, 104)], label="verdicts written back to claim files", lpos=(620, 144))
    g.arrow([(930, 180), (930, 150), (800, 150), (800, 104)], dashed=True)
    g.arrow([(600, 104), (600, 128), (430, 128), (430, 180)], dashed=True, label="load-bearing list", lpos=(540, 122))
    # Criticality layer
    g.band(10, 292, 990, 338, C_LAYER, "CRITICALITY LAYER (standing; audits the method, not the sources)")
    for x in (440, 600, 770, 930):
        g.arrow([(x, 292), (x, 246)], dashed=True)
    g.text(990, 312, "tests everything above: method, independence, fairness, doc versus practice", size=10, anchor="end")
    cw, ch = 232, 62
    g.box(24, 322, cw, ch, ["Method audit MA-01..20", "third-party style, same-model", "proposals a-f held back"], C_LAYER)
    g.box(268, 322, cw, ch, ["Triveritas critique TV-01..11", "Day's own L / M / E test", "applied to this audit"], C_LAYER)
    g.box(512, 322, cw, ch, ["Pre-registration status", f"{_prereg_total()} checks labelled:", "blind · single-commit · unknown"], C_LAYER)
    g.box(756, 322, 232, ch, ["Methods + limitations", "who ran it, what tallies", "can and cannot mean"], C_LAYER)
    g.box(24, 400, cw, ch, ["Decisions log", f"D-01..{_last_decision()} recorded, O-1..9 open", "owner's words pasted"], C_LAYER)
    g.box(268, 400, 476, ch, ["Outside seats (drafts only, nothing sent)", "right of reply: Day, critics · human geneticist + one reader per camp", "non-Claude review packet · COI + licence"], C_LAYER)
    g.box(756, 400, 232, ch, ["Hostile reviews", "one from each camp", "(written by same model)"], C_LAYER)
    g.box(24, 484, 964, 74, ["Feedback loop: finding → one of three routes",
                             "1 no-decision fix: done at once · 2 proposal: written with the verdicts it would move, held",
                             "3 owner decision (DECISIONS.md) → rule-freeze: 24 h cooling-off, 3-review re-score, new rule revision"], C_PROP, size=11)
    g.arrow([(500, 484), (500, 466)], dashed=True)
    g.arrow([(24, 520), (14, 520), (14, 270), (700, 270), (700, 246)], proposed=True, label="rule revision re-enters here", lpos=(250, 264))
    g.text(505, 580, "Proposed R5 exit criterion (owner to confirm): no CRITICAL finding open, every MAJOR closed or accepted by the owner.", size=10)
    g.text(505, 600, "Every pass so far was run by Claude inside the project; none is outside review. See METHODS-AND-LIMITATIONS.", size=10, bold=True)
    g.save("audit-systems.svg")


def verdict_logic_diagram():
    g = _Svg(1010, 400, "evo-sim verdict logic: one quoted statement from tag to verdict or slip ledger, with proposed changes dashed")
    g.box(20, 160, 110, 56, ["Quoted", "statement", "(rule S scope)"], C_DAY)
    g.box(160, 160, 130, 56, ["Tag first", "dialectic or", "rhetoric (RH)"], C_CORE)
    g.arrow([(130, 188), (160, 188)])
    g.box(160, 50, 130, 50, ["(d) RH6 revision", "proposed"], C_PROP, dashed=True)
    g.arrow([(225, 100), (225, 160)], proposed=True)
    g.box(330, 50, 170, 56, ["rhetoric", "device, audience, function,", "dialectical core → slips.md"], C_DAY)
    g.arrow([(290, 175), (310, 175), (310, 78), (330, 78)])
    g.box(330, 160, 150, 56, ["Readings (RD, C)", "every plausible reading", "field = most defensible"], C_CORE)
    g.arrow([(290, 195), (330, 195)], label="dialectic", lpos=(310, 184))
    g.text(415, 130, "no verdict change", size=9)
    # three verdicts
    vx, vw = 530, 190
    g.box(vx, 80, vw, 46, ["Internal", "holds · arithmetic-error ·", "non-sequitur · pending (N)"], C_CORE, size=10)
    g.box(vx, 170, vw, 46, ["Fidelity", "accurate · partial · misread ·", "unverifiable (F, U)"], C_CORE, size=10)
    g.box(vx, 260, vw, 46, ["External", "supported · contested ·", "contradicted · untestable"], C_CORE, size=10)
    for y in (103, 193, 283):
        g.arrow([(480, 188), (505, 188), (505, y), (vx, y)])
    g.box(vx, 130, vw, 22, ["(a) status unexamined: no check run"], C_PROP, dashed=True, bold=False, size=10, rx=5)
    g.box(vx, 310, vw, 22, ["(b) external_basis: data/literature/model"], C_PROP, dashed=True, bold=False, size=10, rx=5)
    g.box(vx, 336, vw, 22, ["(c) contested split four ways"], C_PROP, dashed=True, bold=False, size=10, rx=5)
    # R1
    g.box(760, 150, 120, 76, ["R1 materiality", "slip moves conclusion", "or a downstream number", ">25%, or flips it?"], C_CORE, size=10)
    for y in (103, 193, 283):
        g.arrow([(vx + vw, y), (740, y), (740, 188), (760, 188)])
    g.box(900, 90, 100, 56, ["Yes", "error verdict,", "counted"], C_DAY, size=10)
    g.box(900, 230, 100, 56, ["No", "slip ledger,", "no verdict change"], C_CRIT, size=10)
    g.arrow([(880, 175), (890, 175), (890, 118), (900, 118)])
    g.arrow([(880, 200), (890, 200), (890, 258), (900, 258)])
    g.text(500, 385, "Dashed amber = proposal only, held back (owner decisions O-6 rule-freeze). SC: corrected in the same source = ledger. R1c: no input-looseness rescue for steep outputs.", size=10)
    g.save("audit-verdict-logic.svg")


def roadmap_diagram():
    g = _Svg(1010, 450, "evo-sim roadmap: order and dependencies only, no dates")
    lanes = [("Compute and checks", C_CORE), ("Criticality remediation", C_LAYER), ("Owner decisions", C_DAY), ("Outside inputs", C_CRIT)]
    for i, (name, c) in enumerate(lanes):
        y = 14 + i * 100
        g.parts.append('<rect x="8" y="%d" width="760" height="90" rx="10" fill="%s" fill-opacity="0.07" stroke="%s" stroke-width="1"/>' % (y, c, c))
        g.text(18, y + 16, name, size=11, anchor="start", bold=True, color=c)
    # lane 1
    g.box(20, 34, 130, 50, ["HF post hoc run ph", "(running)"], C_CORE, size=10)
    g.box(180, 34, 110, 50, ["L1b, then L1c", "T2T dN/dS"], C_CORE, size=10)
    g.box(320, 34, 130, 50, ["FMnull, L5, Q93", "re-test (queued)"], C_CORE, size=10)
    g.box(480, 34, 130, 50, ["Write up, review,", "integrate (tiers)"], C_CORE, size=10)
    g.box(630, 34, 120, 50, ["Follow-ups", "L2 L3 L4 D C1d GAP-07"], C_CORE, size=10)
    for a, b in ((150, 180), (290, 320), (450, 480), (610, 630)):
        g.arrow([(a, 59), (b, 59)])
    # lane 2
    g.box(20, 134, 130, 50, ["Proposals a-c", "(unexamined, basis,", "contested split)"], C_LAYER, size=10)
    g.box(180, 134, 110, 50, ["Proposal d", "RH6 revision"], C_LAYER, size=10)
    g.box(320, 134, 130, 50, ["Rule freeze rev 3", "24 h, 3-review", "re-score"], C_LAYER, size=10)
    g.box(480, 134, 130, 50, ["Proposals e, f", "aggregation rule;", "seeded-error test"], C_LAYER, size=10)
    g.box(630, 134, 120, 50, ["Open MA-13..20,", "TV-02..TV-10 items"], C_LAYER, size=10)
    for a, b in ((150, 180), (290, 320), (450, 480), (610, 630)):
        g.arrow([(a, 159), (b, 159)])
    # lane 3
    g.box(20, 234, 130, 50, ["Go-ahead a-c;", "confirm O-6, O-7", "readings"], C_DAY, size=10)
    g.box(180, 234, 110, 50, ["O-5 revert B,", "A2e or re-review"], C_DAY, size=10)
    g.box(320, 234, 130, 50, ["Licence + COI", "facts (O-9)"], C_DAY, size=10)
    g.box(480, 234, 130, 50, ["Approve send:", "right of reply", "(text + channel)"], C_DAY, size=10)
    g.box(630, 234, 120, 50, ["Confirm R5", "exit criterion"], C_DAY, size=10)
    # lane 4
    g.box(20, 334, 130, 50, ["Book text (O-1)", "owner buys, supplies"], C_CRIT, size=10)
    g.box(180, 334, 110, 50, ["Paywalled", "PDFs (owner)"], C_CRIT, size=10)
    g.box(320, 334, 130, 50, ["Human geneticist", "+ one reader per camp"], C_CRIT, size=10)
    g.box(480, 334, 130, 50, ["Non-Claude", "review seat"], C_CRIT, size=10)
    g.box(630, 334, 120, 50, ["Replies from", "Day, critics, Athos?"], C_CRIT, size=10)
    # convergence
    g.box(795, 40, 200, 60, ["R5 draft", "verdicts, sensitivity table,", "aggregation + stopping rule"], C_CRIT, size=10)
    g.box(795, 135, 200, 60, ["Criticality pass on R5 draft", "no CRITICAL open;", "MAJOR closed or accepted"], C_LAYER, size=10)
    g.box(795, 230, 200, 60, ["Research-phase exit", "PLAN.md criteria met", "(variable list final)"], C_DAY, size=10)
    g.box(795, 325, 200, 60, ["Simulator phase", "brainstorm → spec → plan"], C_CRIT, size=10)
    for y in (100, 195, 290):
        g.arrow([(895, y), (895, y + 35)])
    for y in (59, 159, 259, 359):
        g.arrow([(750, y), (795, 70 if y == 59 else (165 if y == 159 else (260 if y == 259 else 355)))], dashed=True)
    g.text(505, 415, "Order and dependency only, no dates. Left to right is an order only in the first two lanes; owner and outside items are parallel. Dashed: each lane feeds R5.", size=10)
    g.text(505, 435, "Branches may graduate independently (PLAN.md). Items in each lane are listed in ROADMAP.md with ids.", size=10)
    g.save("audit-roadmap.svg")


systems_diagram()
verdict_logic_diagram()
roadmap_diagram()

print("wrote", sorted(os.listdir(OUT)))
