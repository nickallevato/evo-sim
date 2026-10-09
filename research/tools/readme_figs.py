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

# 6. Verdict tallies (lint_research.py output on 2026-10-09 after R4 GAP-04/07/02 and H3, 196 claims)
tallies = {
    "internal": [("holds", 96, ACC), ("non-sequitur", 15, DAY), ("arithmetic error", 6, "#ef4444"), ("pending", 56, "#525252")],
    "fidelity": [("accurate", 37, ACC), ("partial", 32, "#eab308"), ("misread", 9, DAY), ("unverifiable", 35, "#525252"), ("pending", 9, "#3f3f46")],
    "external": [("supported", 22, ACC), ("contested", 102, "#eab308"), ("contradicted", 9, DAY), ("untestable", 5, NEU), ("pending", 47, "#525252")],
}
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
print("wrote", sorted(os.listdir(OUT)))
