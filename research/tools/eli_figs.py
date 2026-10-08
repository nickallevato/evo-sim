"""Draw the ELI explainer graphics into docs/img/eli/*.svg (hand-written SVG + two matplotlib charts).
Transparent backgrounds and mid-grey ink so they read on GitHub light and dark themes. Run:
    research/.venv/bin/python -I research/tools/eli_figs.py
Numbers: shortfall decomposition from ledgers/versions.md + balance.md (KITTENS); divergence from RESULTS.md B4a.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "docs", "img", "eli")
os.makedirs(OUT, exist_ok=True)
INK, MUTE = "#8b949e", "#6e7681"
DAY, CRIT, OK, NEU = "#f59e0b", "#3b82f6", "#22c55e", "#a3a3a3"
FONT = "font-family='-apple-system,Segoe UI,Helvetica,Arial,sans-serif'"


def svg(name, w, h, body, title):
    s = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' role='img' aria-label='{title}' {FONT}>"
         f"<title>{title}</title>{body}</svg>")
    open(os.path.join(OUT, name), "w").write(s)


def t(x, y, s, size=15, fill=INK, anchor="middle", weight="normal"):
    return f"<text x='{x}' y='{y}' font-size='{size}' fill='{fill}' text-anchor='{anchor}' font-weight='{weight}'>{s}</text>"


# 1. Conveyor: latency vs throughput
b = [f"<rect x='40' y='120' width='620' height='14' rx='7' fill='{MUTE}'/>"]
for cx in (60, 640):
    b.append(f"<circle cx='{cx}' cy='127' r='16' fill='none' stroke='{MUTE}' stroke-width='4'/>")
for i in range(10):
    x = 70 + i * 56
    b.append(f"<rect x='{x}' y='84' width='34' height='34' rx='5' fill='{OK if i == 9 else CRIT}' opacity='{0.45 + 0.055 * i:.2f}'/>")
b.append(f"<path d='M664 100 q30 0 34 40' fill='none' stroke='{OK}' stroke-width='3' marker-end='url(#a)'/>")
b.insert(0, f"<defs><marker id='a' viewBox='0 0 10 10' refX='5' refY='5' markerWidth='6' markerHeight='6' orient='auto'><path d='M0 0L10 5L0 10z' fill='{OK}'/></marker></defs>")
b.append(f"<path d='M70 66 H664' stroke='{INK}' stroke-width='1.5' stroke-dasharray='4 4'/>")
b.append(t(367, 56, "each change takes a LONG time to ride all the way across", 15))
b.append(t(367, 168, "…but the belt is full, so one arrives at the end every step", 15, OK, weight="bold"))
b.append(t(367, 196, "time for ONE change  ≠  how often changes finish", 14, MUTE))
svg("conveyor.svg", 720, 210, "".join(b), "Conveyor belt: a long ride time does not mean a slow finishing rate")

# 2. Typos: counting letters vs counting events
b = []
row = lambda y, word, hi: "".join(
    f"<rect x='{60 + i * 40}' y='{y}' width='34' height='40' rx='5' fill='{DAY if i in hi else 'none'}' stroke='{INK}' stroke-width='1.5' opacity='{0.9 if i in hi else 1}'/>"
    + t(77 + i * 40, y + 27, c, 20, "#111" if i in hi else INK, weight="bold") for i, c in enumerate(word))
b.append(t(40, 32, "before", 14, MUTE, "start"))
b.append(row(40, "THECAT", set()))
b.append(t(40, 118, "after", 14, MUTE, "start"))
b.append(row(126, "THEBIGFATCAT", {3, 4, 5, 6, 7, 8}))
b.append(f"<rect x='570' y='40' width='170' height='58' rx='8' fill='none' stroke='{DAY}' stroke-width='2'/>")
b.append(t(655, 64, "count letters:", 14, DAY) + t(655, 86, "6 changes", 17, DAY, weight="bold"))
b.append(f"<rect x='570' y='114' width='170' height='58' rx='8' fill='none' stroke='{CRIT}' stroke-width='2'/>")
b.append(t(655, 138, "count events:", 14, CRIT) + t(655, 160, "1 change", 17, CRIT, weight="bold"))
b.append(t(385, 200, "one insertion can add many letters, so the two ways of counting give different totals", 14, MUTE))
svg("typos.svg", 770, 214, "".join(b), "Counting letters versus counting events")

# 3. Cousins: ancestral variation predates the split
b = []
cols = [DAY, CRIT, OK, DAY, NEU, CRIT, OK, NEU]
for i, c in enumerate(cols):
    b.append(f"<circle cx='{250 + i * 30}' cy='60' r='11' fill='{c}'/>")
b.append(t(355, 30, "the shared ancestors already differed from each other", 14))
b.append(f"<path d='M300 78 L170 150 M410 78 L540 150' stroke='{INK}' stroke-width='2.5' fill='none'/>")
for i, c in enumerate([DAY, DAY, OK, DAY, DAY]):
    b.append(f"<circle cx='{100 + i * 30}' cy='170' r='11' fill='{c}'/>")
for i, c in enumerate([CRIT, CRIT, NEU, CRIT, CRIT]):
    b.append(f"<circle cx='{490 + i * 30}' cy='170' r='11' fill='{c}'/>")
b.append(t(160, 206, "family 1", 14, MUTE) + t(550, 206, "family 2", 14, MUTE))
b.append(t(355, 244, "some differences today were already there BEFORE the split, so not all of them are new", 14, OK, weight="bold"))
svg("cousins.svg", 710, 258, "".join(b), "Ancestral variation: some differences predate the split")

# 4. Scales: both sides got some right, some wrong
def card(x, col, head, good, bad):
    s = [f"<rect x='{x}' y='20' width='320' height='232' rx='12' fill='none' stroke='{col}' stroke-width='2.5'/>",
         t(x + 160, 50, head, 17, col, weight="bold")]
    y = 84
    for g in good:
        s.append(t(x + 22, y, "✓", 17, OK, "start", "bold") + t(x + 46, y, g, 14, INK, "start")); y += 28
    y += 6
    for g in bad:
        s.append(t(x + 22, y, "✗", 17, "#ef4444", "start", "bold") + t(x + 46, y, g, 14, INK, "start")); y += 28
    return "".join(s)
b = [card(20, DAY, "“not enough time” side",
          ["some formulas are exactly right", "bacteria rate is real", "old 1/300 sum adds up"],
          ["counted letters, not events", "misread a source", "assumed an empty start"]),
     card(370, CRIT, "“the math is wrong” side",
          ["rate doesn’t shrink with size", "many changes at once", "old differences counted"],
          ["counted some things twice", "“soft selection” fix failed", "skipped some questions"])]
svg("both-sides.svg", 710, 270, "".join(b), "Both sides got some things right and some things wrong")

# 4b. Raffle: bigger population = more new changes, each with smaller odds (k = mu)
def town(x, n, new, label, odds):
    s = [f"<rect x='{x}' y='40' width='300' height='190' rx='12' fill='none' stroke='{INK}' stroke-width='1.5'/>",
         t(x + 150, 30, label, 15, INK, weight="bold")]
    per = 10 if n <= 10 else 20
    r = 7 if n <= 10 else 5.5
    gap = 26 if n <= 10 else 13
    for i in range(n):
        cx = x + 32 + (i % per) * gap + (8 if n <= 10 else 0)
        cy = 70 + (i // per) * (gap if n > 10 else 0) + (40 if n <= 10 else 0)
        s.append(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{OK if i < new else NEU}' opacity='{1 if i < new else 0.55}'/>")
    s.append(t(x + 150, 176, f"{new} new change{'s' if new > 1 else ''} (green)", 14, OK, weight="bold"))
    s.append(t(x + 150, 200, odds, 14, INK))
    return "".join(s)
b = [town(20, 10, 1, "small group: 10", "each has a 1-in-10 chance to win"),
     town(390, 100, 10, "big group: 100", "each has a 1-in-100 chance to win"),
     t(355, 262, "either way, about the same number of changes win each generation", 15, OK, weight="bold")]
svg("raffle.svg", 710, 276, "".join(b), "Bigger groups make more new changes, but each has smaller odds, so it evens out")

# 5. Shortfall decomposition (matplotlib)
plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK,
                     "axes.edgecolor": INK, "xtick.color": INK, "ytick.color": INK, "axes.facecolor": "none",
                     "figure.facecolor": "none", "savefig.transparent": True, "axes.spines.top": False,
                     "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(7.2, 3.0))
ax.barh([2], [1_075_000], color=DAY, height=0.55)
ax.barh([1], [11.7], color=CRIT, height=0.55)
ax.barh([0], [91_600], color=NEU, height=0.55)
ax.set_xscale("log"); ax.set_xlim(1, 4e8)
ax.set_yticks([2, 1, 0]); ax.set_yticklabels(["Day’s shortfall\n(MITTENS 3.0)", "counting bases\ninstead of events", "what is left:\nSNV-only shortfall"], fontsize=9.5)
for y, v, lab in [(2, 1_075_000, "1,075,000×"), (1, 11.7, "≈ 11.7×  (bookkeeping)"), (0, 91_600, "91,600×  (bacteria → humans: contested)")]:
    ax.text(v * 1.25, y, lab, va="center", fontsize=9.5)
ax.set_xlabel("how many times too slow (log scale)")
ax.set_title("Where Day’s 1,000,000× comes from", fontsize=11, color=INK)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "shortfall.svg"), metadata={"Date": None}); plt.close(fig)

# 6. Divergence fit (matplotlib)
fig, ax = plt.subplots(figsize=(6.4, 2.9))
labs = ["Day’s Nₑ = 10⁴", "observed", "fit: Nₑ ≈ 130k", "Yoo 2025 Nₑ = 198k"]
vals = [0.65, 1.23, 1.23, 1.55]
ax.bar(labs, vals, color=[DAY, OK, NEU, CRIT], width=0.6)
for i, v in enumerate(vals):
    ax.text(i, v + 0.04, f"{v:.2f}%", ha="center", fontsize=10)
ax.set_ylim(0, 1.8); ax.set_ylabel("human–chimp\ndifference (%)")
ax.tick_params(axis="x", labelsize=9)
ax.set_title("Neither side’s favourite number fits cleanly", fontsize=11, color=INK)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "divergence.svg"), metadata={"Date": None}); plt.close(fig)
print("wrote", sorted(os.listdir(OUT)))
