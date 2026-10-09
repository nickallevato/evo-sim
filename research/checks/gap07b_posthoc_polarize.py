"""GAP-07b POST HOC (NOT pre-registered): symmetric, placement-tolerant lineage polarization of indel events.

Why: the pre-registered polarize_events() in gap07b_alignment_count.py (run in commit-3c847b8 form) treated the two
single-sided kinds asymmetrically. For chimp-only gaps it looked for a gorilla insertion within +-2 columns of the
human junction; for human-only gaps it required the gorilla alignment to agree EXACTLY, base by base, over the gap.
Two independent pairwise alignments place gaps in repeats and homopolymers differently, so exact agreement fails
more often than a +-2 window: human insertions were more often scored "gorilla has these bases" (= chimp deletion).
Result in the main run: human-only gaps polarized 25% human-lineage at 1 bp, chimp-only gaps 46%, an implausible
asymmetry (by kind and size in results/raw/gap07b_axt.json: cev_count). That is an artefact of the method, so the
indel polarization of the main run is NOT used for headline per-lineage claims.

This script uses one rule for both kinds, with the same tolerance w (default 5 columns) on both sides of the event:
  human-only gap [p, p+L):  D = number of human bases in [p-w, p+L+w) that are gaps in the gorilla alignment
                            (gbase == 5).  D >= 0.5 L (and <= 2L + w)  -> human lineage (human insertion)
                            D == 0 and both flanks aligned            -> chimp lineage (chimp deletion)
  chimp-only gap at junction p, L bases: I = gorilla-only bases inserted at human junctions in [p-w, p+w]
                            I >= max(1, 0.5 L) (and <= 2L + w)        -> human lineage (human deletion)
                            I == 0 and both flanks aligned            -> chimp lineage (chimp insertion)
  anything else -> unpolarized. Complex (both-sided) gaps are not polarized.
Residual bias: no gorilla signal is read as "chimp lineage"; a chance gorilla-lineage indel inside the window is read as
"human lineage", and a human event whose gorilla signal is displaced beyond w is read as chimp. Without a chimp-gorilla
alignment this cannot be removed. Sensitivity to w is printed (w = 2, 5, 10, 20).
Run: research/.venv/bin/python -I research/checks/gap07b_posthoc_polarize.py --ev EVDIR --gor GORDIR --out OUT.json
"""
import argparse
import json
import os

import numpy as np

PRIMARY = ['chr%d' % i for i in range(1, 23)] + ['chrX', 'chrY']
EDGES = np.array([1, 2, 11, 51, 1001])


def polar(tS, tSz, qSz, gb, gi, w):
    n = len(gb)
    pol = np.zeros(len(tS), np.int8)
    m = (tSz > 0) & (qSz == 0)
    if m.any():
        cs5 = np.concatenate(([0], np.cumsum(gb == 5, dtype=np.int32)))
        p = tS[m]; L = tSz[m]
        a = np.clip(p - w, 0, n); b = np.clip(p + L + w, 0, n)
        D = cs5[b] - cs5[a]
        fl = (gb[np.clip(a - 1, 0, n - 1)] < 4) & (gb[np.clip(b, 0, n - 1)] < 4)
        r = np.zeros(len(p), np.int8)
        r[(D >= 0.5 * L) & (D <= 2 * L + w)] = 1
        r[(D == 0) & fl] = 2
        pol[m] = r
    m = (tSz == 0) & (qSz > 0)
    if m.any():
        csi = np.concatenate(([0], np.cumsum(gi, dtype=np.int32)))
        p = tS[m]; L = qSz[m]
        a = np.clip(p - w, 0, n); b = np.clip(p + w + 1, 0, n)
        I = csi[b] - csi[a]
        fl = (gb[np.clip(p - w - 1, 0, n - 1)] < 4) & (gb[np.clip(p + w + 1, 0, n - 1)] < 4)
        r = np.zeros(len(p), np.int8)
        r[(I >= np.maximum(1, 0.5 * L)) & (I <= 2 * L + w)] = 1
        r[(I == 0) & fl] = 2
        pol[m] = r
    return pol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ev'); ap.add_argument('--gor'); ap.add_argument('--out')
    a = ap.parse_args()
    ws = [2, 5, 10, 20]
    tab = {w: np.zeros((2, 5, 3), np.int64) for w in ws}       # kind(human_only, chimp_only), size, pol
    for c in PRIMARY:
        z = np.load(os.path.join(a.ev, 'chainev_%s.npz' % c))
        g = np.load(os.path.join(a.gor, 'gor_%s.npz' % c))
        gb, gi = g['gbase'], g['gins']
        tS, tSz, qSz = z['tS'], z['tSz'], z['qSz']
        size = np.maximum(tSz, qSz)
        sc = np.searchsorted(EDGES, size, side='right') - 1
        single = (tSz == 0) | (qSz == 0)
        kind = np.where(qSz == 0, 0, 1)
        for w in ws:
            pol = polar(tS, tSz, qSz, gb, gi, w)
            idx = (kind[single] * 5 + sc[single]) * 3 + pol[single]
            tab[w] += np.bincount(idx, minlength=30).reshape(2, 5, 3)
        print(c, flush=True)
    out = {str(w): tab[w].tolist() for w in ws}
    json.dump(out, open(a.out, 'w'))
    for w in ws:
        t = tab[w]
        hum = t[:, :, 1].sum(); chi = t[:, :, 2].sum(); un = t[:, :, 0].sum()
        print('w=%d: human %d chimp %d unpol %d; human share of polarized %.3f; polarizable %.3f' % (
            w, hum, chi, un, hum / (hum + chi), (hum + chi) / (hum + chi + un)))
        for k, nm in enumerate(['human_only', 'chimp_only']):
            print('   %s human share by size: %s' % (nm, [round(float(t[k, s, 1] / max(1, t[k, s, 1] + t[k, s, 2])), 3) for s in range(5)]))


if __name__ == '__main__':
    main()
