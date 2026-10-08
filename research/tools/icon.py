"""Render the evo-sim icon: a double helix flowing into a cross that acts as a zipper,
splitting it into two lineages (orange, blue) under an audit lens.
Writes docs/img/icon.svg (static) and docs/img/icon-animated.svg (3 s seamless loop).
    research/.venv/bin/python -I research/tools/icon.py
"""
import math, os
OR, BL, WH, LN = "#f59e0b", "#3b82f6", "#f8fafc", "#e2e8f0"
CX = 110

def frame(inner):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1e293b"/><stop offset="1" stop-color="#0b1120"/></linearGradient>
<clipPath id="lens"><circle cx="110" cy="110" r="59"/></clipPath></defs>
<rect width="256" height="256" rx="56" fill="url(#bg)"/>
<circle cx="110" cy="110" r="66" fill="#0f172a"/>
<g clip-path="url(#lens)" stroke-linecap="round" stroke-linejoin="round" fill="none">{inner}</g>
<circle cx="110" cy="110" r="66" fill="none" stroke="{LN}" stroke-width="14"/>
<path d="M160 160 L206 206" stroke="{LN}" stroke-width="24" stroke-linecap="round"/></svg>'''

def smooth(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)

def build(P, K=30, dur=3.0):
    TIP, BAR, LAM, AMP, S, LOPEN, UNR, W = P["tip"], P["bar"], P["lam"], P["amp"], P["spread"], P["lopen"], P["unravel"], P["w"]
    ys = [20 + i * 1.5 for i in range(121)]                      # 20..200
    def strands(tau):
        A, B = [], []
        for y in ys:
            ph = 2 * math.pi * (y / LAM - tau)                    # pattern travels down one wavelength per loop
            o = smooth((y - TIP) / LOPEN)
            a = AMP * (1 - UNR * o)
            sp = S * o + P.get("drift", 0) * max(0, y - TIP - LOPEN)
            A.append((CX + a * math.sin(ph) - sp, y)); B.append((CX - a * math.sin(ph) + sp, y))
        return A, B
    def rungs(tau):
        out = []
        for n in range(-2, 14):
            y = LAM * (0.125 + n / 4) + LAM * tau
            ph = 2 * math.pi * (y / LAM - tau); x = AMP * math.sin(ph)
            vis = 0.85 if y < TIP - 4 else 0.0
            out.append((f"M{CX + x:.1f} {y:.1f} L{CX - x:.1f} {y:.1f}", vis))
        return out
    d = lambda pts: "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    taus = [k / K for k in range(K + 1)]
    fr = [strands(t) for t in taus]; rg = [rungs(t) for t in taus]
    kt = ";".join(f"{i / K:.4f}" for i in range(K + 1))
    an = lambda attr, vals: f'<animate attributeName="{attr}" dur="{dur}s" repeatCount="indefinite" calcMode="linear" keyTimes="{kt}" values="{";".join(vals)}"/>'
    g = []
    for j in range(len(rg[0])):
        g.append(f'<path d="{rg[0][j][0]}" stroke="{WH}" stroke-width="3" opacity="{rg[0][j][1]}">{an("d", [r[j][0] for r in rg])}{an("opacity", [str(r[j][1]) for r in rg])}</path>')
    for k, col in ((1, BL), (0, OR)):
        g.append(f'<path d="{d(fr[0][k])}" stroke="{col}" stroke-width="{W}">{an("d", [d(f[k]) for f in fr])}</path>')
    hw = P["arm"]
    # the cross, drawn over the strands; its upper tip is a wedge (the zipper slider)
    cross = (f'<path d="M{CX} {TIP + 10} V200" stroke="{WH}" stroke-width="14" stroke-linecap="butt"/>'
             f'<path d="M{CX - 7} {TIP + 11} L{CX} {TIP - 3} L{CX + 7} {TIP + 11} Z" fill="{WH}" stroke="{WH}" stroke-width="2"/>'
             f'<path d="M{CX - hw} {BAR} H{CX + hw}" stroke="{WH}" stroke-width="14"/>')
    animated = frame("".join(g) + cross)
    static = frame("".join(f'<path d="{r[0]}" stroke="{WH}" stroke-width="3" opacity="{r[1]}"/>' for r in rg[0])
                   + "".join(f'<path d="{d(fr[0][k])}" stroke="{c}" stroke-width="{W}"/>' for k, c in ((1, BL), (0, OR))) + cross)
    return animated, static

P = dict(tip=92, bar=118, lam=36, amp=12, spread=30, lopen=22, unravel=0.3, w=8, arm=28, drift=0.9)  # "J · Wide peel"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "docs", "img")
animated, static = build(P)
for name, svg in (("icon.svg", static), ("icon-animated.svg", animated)):
    svg = svg.replace("<svg ", '<svg role="img" aria-label="evo-sim icon" ', 1).replace("<defs>", "<title>evo-sim</title><defs>", 1)
    open(os.path.join(OUT, name), "w").write(svg)
print("wrote icon.svg, icon-animated.svg")
