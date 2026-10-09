"""C1d figure from the committed result JSONs (no genotypes).  POST HOC revision (review fix pass): adds panel C, S21 per eligible allele by substitution class against C1c's neutral R0 reference rates.  research/.venv/bin/python -I research/checks/c1d_figure.py"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
day = json.load(open(os.path.join(RAW, "c1d_v62_day.json")))
ph = json.load(open(os.path.join(RAW, "c1d_v62_posthoc.json")))
ne = json.load(open(os.path.join(RAW, "c1d_v66_ne.json")))
bins = day["bins"]
dayprof = day["day"]["profile"]
def row(g, **kw):
    for s in g:
        if all(s.get(k) == v for k, v in kw.items()):
            return s
all_ = row(day["grid"], sample="day1", elig_rule="E1", date_rule="T2", m=1, tracked_rule="all11", snpset="all")["profile"]
tv = ph["by_substitution_class"]["transversions_autosomes"]["profile"]
C = dict(day="#2a78d6", all="#eb6834", tv="#1baf7a", ink="#0b0b0b", sub="#52514e", grid="#e3e2dc")
fig, ax = plt.subplots(1, 3, figsize=(18, 5.2), gridspec_kw=dict(width_ratios=[1.25, 1, 0.9]))
a = ax[0]
x = np.arange(11); w = 0.27
for i, (lab, d, c) in enumerate((("Day's table (Z18525185)", dayprof, C["day"]), ("Real AADR v62, E1/T2, all SNPs", all_, C["all"]), ("Real AADR v62, transversions on autosomes", tv, C["tv"]))):
    a.bar(x + (i - 1) * w, np.maximum(d, 0.6), w * 0.9, color=c, label=lab, bottom=0)
a.set_yscale("log"); a.set_ylim(0.5, 1e5)
a.set_xticks(x); a.set_xticklabels(bins, rotation=40, ha="right", fontsize=8)
a.set_ylabel("events dated to the bin (log scale; 0 drawn at 0.6)"); a.set_title("Where the 'fixation events' fall, oldest to youngest bin", fontsize=10, loc="left")
a.legend(frameon=False, fontsize=8, loc="upper right"); a.grid(axis="y", color=C["grid"], lw=0.6); a.set_axisbelow(True)
for s in ("top", "right"): a.spines[s].set_visible(False)
b = ax[1]
pairs = ["Meso-EN", "EN-LN", "EN-BA", "EN-Iron", "EN-Med", "EN-Mod", "BA-Med"]
lab = {"Meso-EN": "Meso vs EN", "EN-LN": "EN to LN", "EN-BA": "EN to BA", "EN-Iron": "EN to Iron", "EN-Med": "EN to Med", "EN-Mod": "EN to Modern", "BA-Med": "BA to Med"}
rep = ne["kr_reported"]; rows = {r["pair"]: r for r in ne["pairs"]}
y = np.arange(len(pairs))[::-1]
for i, p in enumerate(pairs):
    key = p if p != "Meso-EN" else "EN-Meso"
    b.plot(rep[key]["ne"], y[i] + 0.18, "o", color=C["day"], ms=8, label="keruru reported" if i == 0 else None)
    b.plot(rows[p]["K"]["ne"], y[i], "s", color=C["all"], ms=7, label="replication, his formula (v66)" if i == 0 else None)
    b.plot(rows[p]["B"]["ne"], y[i] - 0.18, "D", color=C["tv"], ms=7, label="replication, allele-count correction (v66)" if i == 0 else None)
b.set_yticks(y); b.set_yticklabels([lab[p] for p in pairs], fontsize=9)
b.set_xscale("log"); b.set_xlim(500, 20000); b.set_xlabel("temporal N_e (log scale); Wright 4N/(V_k+2) at N=1e7 would be 5.7e6")
b.set_title("Temporal N_e by window", fontsize=10, loc="left"); b.legend(frameon=False, fontsize=8, loc="lower left"); b.grid(axis="x", color=C["grid"], lw=0.6); b.set_axisbelow(True)
for s in ("top", "right"): b.spines[s].set_visible(False)
c = ax[2]
ph2 = json.load(open(os.path.join(RAW, "c1d_v62_ph2.json")))
spl = ph2["V1_split"]
bars = [("Day's table\n(21 / 22,428)", 21 / 22428, C["day"]), ("real v62\nall SNPs", spl["all"]["per_eligible"], C["all"]),
        ("transitions\n(autosomes)", spl["transitions_auto"]["per_eligible"], C["all"]), ("transversions\n(autosomes)", spl["transversions_auto"]["per_eligible"], C["tv"])]
for i, (lab, v, col) in enumerate(bars):
    c.bar(i, v, 0.7, color=col)
    c.text(i, v * 1.15, "%.2g" % v, ha="center", fontsize=8, color=C["ink"])
refs = [("C1c neutral, closed, N_e 1e4", 3925 / 15200), ("N_e 1e5", 32 / 1700), ("N_e 1e6", 3.6 / 700)]
for lab, v in refs:
    c.axhline(v, color=C["sub"], lw=0.8, ls="--")
    c.text(-0.45, v * 1.08, lab, ha="left", fontsize=7, color=C["sub"])
c.set_yscale("log"); c.set_ylim(3e-4, 1)
c.set_xticks(range(4)); c.set_xticklabels([b[0] for b in bars], fontsize=8)
c.set_ylabel("S21 per eligible allele (log)"); c.set_title("Rate per eligible allele (model lines: C1c R0, flat SFS)", fontsize=10, loc="left")
c.grid(axis="y", color=C["grid"], lw=0.6); c.set_axisbelow(True)
for sp in ("top", "right"): c.spines[sp].set_visible(False)
fig.suptitle("C1d: Day's statistic and keruru's N_e on the real AADR genotypes", fontsize=12, x=0.01, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.95))
out = os.path.join(HERE, "results", "R4-C1d-real-vs-day.png")
fig.savefig(out, dpi=140); print(out)
