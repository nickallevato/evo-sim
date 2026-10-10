"""Render the README previews of the ELI series sims as looping SMIL SVGs: docs/img/mutation-river.svg and docs/img/combination-lock.svg.

Real Wright-Fisher run (seeded): N = 40 diploids (2N = 80 copies), neutral, infinite sites, mu = 0.02 per copy per
generation, started at the neutral equilibrium spectrum (Poisson(theta/i) sites with i copies, theta = 4N mu). Each dot
is one mutation, x = its share of the population (mutations lost within 2 generations are not drawn); dots that reach the right bank are substitutions and leave a tick.
Expected substitutions = mu * generations (k = mu). Trivial compute (<1 s, single process).
"""
import math
import os

import numpy as np

N, M, MU, GENS, STEP, SEED = 40, 80, 0.02, 600, 8, 7
W, H, L, R, T, B = 720, 230, 30, 690, 30, 170
DUR = 24.0  # seconds per loop
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "img", "mutation-river.svg")

rng = np.random.default_rng(SEED)
muts = []  # dict(c, y, born, path)
th = 4 * N * MU
for i in range(1, M):
    for _ in range(rng.poisson(th / i)):
        muts.append(dict(c=i, y=rng.random(), born=0, path=[i]))
done, fixes = [], []
for g in range(1, GENS + 1):
    keep = []
    for m in muts:
        m["c"] = int(rng.binomial(M, m["c"] / M))
        m["path"].append(m["c"])
        if m["c"] == M:
            fixes.append(g)
            done.append(m)
        elif m["c"] == 0:
            done.append(m)
        else:
            keep.append(m)
    for _ in range(rng.poisson(M * MU)):
        keep.append(dict(c=1, y=rng.random(), born=g, path=[1]))
    muts = keep
done += muts

def X(c):
    return L + (R - L) * c / M

def kt(g):
    return min(max(g / GENS, 0.0), 1.0)

out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
       'font-family="DejaVu Sans, Verdana, sans-serif" font-size="12">',
       '<title>Mutation river: neutral mutations drifting until lost or fixed (Wright-Fisher, 2N = 80)</title>',
       f'<rect x="{L}" y="{T}" width="{R - L}" height="{B - T}" rx="4" fill="#5fa8b8" fill-opacity="0.18"/>',
       f'<rect x="{L - 3}" y="{T}" width="3" height="{B - T}" fill="#6b7f84"/>',
       f'<rect x="{R}" y="{T}" width="3" height="{B - T}" fill="#6b7f84"/>',
       f'<text x="{L}" y="{T - 10}" fill="#6b7f84">new (1 copy)</text>',
       f'<text x="{R}" y="{T - 10}" fill="#6b7f84" text-anchor="end">fixed (everyone)</text>',
       f'<text x="{W / 2}" y="{T - 10}" fill="#6b7f84" text-anchor="middle">share of the population carrying each mutation</text>']
for m in done:
    p = m["path"]
    g0, g1 = m["born"], m["born"] + len(p) - 1
    if g0 > GENS or len(p) - 1 < 3:   # lost within 2 generations: under one frame on screen, not drawn
        continue
    idx = list(range(0, len(p), STEP)) + ([len(p) - 1] if (len(p) - 1) % STEP else [])
    times = [g0 + i for i in idx if g0 + i <= GENS]
    xs = [X(p[i]) for i in idx][:len(times)]
    y = T + 6 + (B - T - 12) * m["y"]
    fixed = p[-1] == M
    col = "#0d9488" if fixed else "#14a394"
    a0, a1 = kt(g0), kt(g1)
    if a1 <= a0:
        a1 = min(1.0, a0 + 0.002)
    kts = ";".join(f"{kt(t):.3f}" for t in times)
    vals = ";".join(f"{x:.0f}" for x in xs)
    if times[0] > 0:
        kts, vals = "0;" + kts, f"{xs[0]:.1f};" + vals
    if times[-1] < GENS:
        kts, vals = kts + ";1", vals + f";{xs[-1]:.1f}"
    op_k = sorted({0.0, a0, a1, 1.0})
    op_v = ["1" if (a0 <= k < a1) or (k == a0) else "0" for k in op_k]
    if a1 >= 1.0:
        op_v[-1] = "1"
    out.append(f'<circle cy="{y:.1f}" r="{3.2 if fixed else 2.4}" fill="{col}" cx="{xs[0]:.1f}" opacity="0">'
               f'<animate attributeName="cx" dur="{DUR}s" repeatCount="indefinite" keyTimes="{kts}" values="{vals}"/>'
               f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
               f'keyTimes="{";".join(f"{k:.4f}" for k in op_k)}" values="{";".join(op_v)}"/></circle>')
# substitution tally: one tick per fixation, appearing when it happens; dashed line = mu * t
ty, tx0, tw = 205, L, R - L
out.append(f'<text x="{L}" y="{ty - 12}" fill="#6b7f84">substitutions so far (ticks) vs. k = μ prediction (dashed)</text>')
out.append(f'<line x1="{tx0}" y1="{ty + 8}" x2="{R}" y2="{ty + 8}" stroke="#6b7f84" stroke-width="1"/>')
exp_total = MU * GENS
scale = tw / max(exp_total, len(fixes)) * 0.95
out.append(f'<line x1="{tx0}" y1="{ty - 2}" x2="{tx0}" y2="{ty - 2}" stroke="#2b5ca6" stroke-width="2" stroke-dasharray="5 4">'
           f'<animate attributeName="x2" dur="{DUR}s" repeatCount="indefinite" values="{tx0};{tx0 + exp_total * scale:.1f}"/></line>')
for j, g in enumerate(fixes):
    x = tx0 + (j + 0.5) * scale
    k = kt(g)
    out.append(f'<rect x="{x - 1.5:.1f}" y="{ty}" width="3" height="8" fill="#0d9488" opacity="0">'
               f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
               f'keyTimes="0;{k:.4f}" values="0;1"/></rect>')
out.append(f'<text x="{R}" y="{H - 4}" fill="#6b7f84" text-anchor="end">{len(fixes)} fixed in {GENS} generations; '
           f'μ × {GENS} = {exp_total:g}</text>')
out.append("</svg>")
open(OUT, "w").write("\n".join(out) + "\n")
print(OUT, os.path.getsize(OUT), "bytes;", len(fixes), "fixations; expected", exp_total)

# ---------------------------------------------------------------------------------------------------------------------
# Combination lock (illustrative, as in the ELI page; not the D15 result). K = 4 dials over ACGT. Each try changes one
# random dial to a random letter. Stepping stones keeps a dial once it is right (selection keeps a helpful step);
# the valley accepts every change and only opens when all four are right at once (no partial credit).
# Both locks get the same number of tries per second, so the valley is shown opening much later.
A, K, LSEED = "ACGT", 4, 11
lr = np.random.default_rng(LSEED)
target = [A[lr.integers(4)] for _ in range(K)]


def run(mode):
    d = []
    for i in range(K):
        c = A[lr.integers(4)]
        while c == target[i]:
            c = A[lr.integers(4)]
        d.append(c)
    hist = [[(0, d[i])] for i in range(K)]
    t = 0
    while d != target:
        t += 1
        i, c = int(lr.integers(K)), A[lr.integers(4)]
        if mode == "step" and d[i] == target[i]:
            continue
        if c != d[i]:
            d[i] = c
            hist[i].append((t, c))
    return t, hist


ts, hs = run("step")
tv, hv = run("valley")
TOT = tv + max(40, tv // 6)            # loop length in tries: the valley opens, then a pause
LDUR = min(30.0, max(14.0, TOT / 25))  # seconds per loop
LW, LH, CW = 720, 190, 52
lo = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LW} {LH}" width="{LW}" height="{LH}" '
      'font-family="DejaVu Sans Mono, Menlo, monospace" font-size="13">',
      '<title>Combination lock: stepping stones vs. valley (illustrative, not the D15 result)</title>']


def lock(x0, label, hist, topen):
    lo.append(f'<text x="{x0 + 2 * CW}" y="22" fill="#6b7f84" text-anchor="middle" font-family="DejaVu Sans, Verdana, sans-serif">{label}</text>')
    for i in range(K):
        x = x0 + i * CW
        ev = [(t, c) for t, c in hist[i] if t <= TOT]
        # background: green while this dial is right
        ks, vs = [], []
        for t, c in ev:
            ks.append(t / TOT)
            vs.append("#0d9488" if c == target[i] else "#c9d6d9")
        if ks[0] > 0:
            ks.insert(0, 0.0); vs.insert(0, vs[0])
        lo.append(f'<rect x="{x + 4}" y="40" width="{CW - 8}" height="{CW + 10}" rx="4" fill="{vs[0]}">'
                  f'<animate attributeName="fill" dur="{LDUR}s" repeatCount="indefinite" calcMode="discrete" '
                  f'keyTimes="{";".join(f"{k:.4f}" for k in ks)}" values="{";".join(vs)}"/></rect>')
        for letter in A:
            ks2 = [0.0] + [t / TOT for t, c in ev]
            vs2 = ["1" if ev[0][1] == letter else "0"] + ["1" if c == letter else "0" for t, c in ev]
            lo.append(f'<text x="{x + CW / 2}" y="{40 + CW * 0.8}" text-anchor="middle" font-size="26" font-weight="600" '
                      f'fill="#18272b" opacity="{vs2[0]}">{letter}<animate attributeName="opacity" dur="{LDUR}s" '
                      f'repeatCount="indefinite" calcMode="discrete" keyTimes="{";".join(f"{k:.4f}" for k in ks2)}" '
                      f'values="{";".join(vs2)}"/></text>')
    k = topen / TOT
    lo.append(f'<text x="{x0 + 2 * CW}" y="130" text-anchor="middle" fill="#0d9488" font-weight="600" opacity="0">'
              f'OPEN after {topen} tries<animate attributeName="opacity" dur="{LDUR}s" repeatCount="indefinite" '
              f'calcMode="discrete" keyTimes="0;{k:.4f}" values="0;1"/></text>')


lock(40, "stepping stones (right dials stay)", hs, ts)
lock(LW - 40 - K * CW, "valley (all four at once)", hv, tv)
lo.append(f'<text x="{LW / 2}" y="{LH - 32}" text-anchor="middle" fill="#6b7f84">target {"".join(target)} · '
          f'both locks try at the same speed · {4 ** K} possible combinations</text>')
lo.append(f'<text x="{LW / 2}" y="{LH - 12}" text-anchor="middle" fill="#6b7f84" font-family="DejaVu Sans, Verdana, sans-serif">'
          'Illustrative toy from the ELI page, not the audit\'s D15 result (D15 is still running).</text>')
lo.append("</svg>")
LOUT = os.path.join(os.path.dirname(OUT), "combination-lock.svg")
open(LOUT, "w").write("\n".join(lo) + "\n")
print(LOUT, os.path.getsize(LOUT), "bytes; stepping", ts, "tries; valley", tv, "tries")

# ---------------------------------------------------------------------------------------------------------------------
# Standalone copy of the ELI page for plain web hosting (the Artifact host wraps index.html in its own skeleton; a
# plain host needs the doctype and metas). Regenerate after editing index.html.
ELI = os.path.join(os.path.dirname(OUT), "..", "explain", "eli-series")
body = open(os.path.join(ELI, "index.html")).read()
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<!-- GENERATED from index.html by research/tools/eli_readme_svgs.py; edit index.html, not this file -->\n')
i = body.index("</style>") + len("</style>")
open(os.path.join(ELI, "play.html"), "w").write(head + body[:i] + "\n</head>\n<body>\n" + body[i:] + "\n</body>\n</html>\n")
print(os.path.join(ELI, "play.html"), "written")
