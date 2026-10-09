"""GAP-07c POST HOC 1 (written after the main run of gap07c_polymorphic_share.py; labelled post hoc).

WHY. The main script flagged an SNV as "top-level (colinear)" when it lay inside a level-1 net fill range. A level-1
fill range also contains the nested (level >= 2) fills that sit inside its internal gaps, so the flag was true for every
SNV and the two rows "top-level fills, in mask" / "H-derived, top-level, in mask" of the main report are identical to
"in strict mask" / "H-derived, in mask". That is a coding error in a secondary row (found by seeing identical n). This
script recomputes the flag correctly: top-level = in a level-1 fill range AND not in any fill of level >= 2.
It also gives the polymorphic share separately for nested-fill SNVs, and the corrected ratio on the top-level SNV
count only (GAP-07b's critic-favourable "top-level colinear fills only" row, 35.02 M SNVs, scaled to the autosomes).
Reads only: sources/raw/gap07c-sites/snv_*.npz, sources/raw/gap07c-af-p3/snvaf_*.npz, the UCSC net file.
Run as research/.venv/bin/python -I research/checks/gap07c_posthoc_toplevel.py <net.gz> <sites_dir> <af_dir> <out.json>.
"""
import gzip
import json
import sys
from collections import defaultdict

import numpy as np

CH = ['chr%d' % i for i in range(1, 23)]


def merge(iv):
    iv = sorted(iv)
    out = []
    for s, e in iv:
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return np.array(out, np.int64).reshape(-1, 2)


def inside(r, pos):
    if not len(r):
        return np.zeros(len(pos), bool)
    k = np.searchsorted(r[:, 0], pos, side='right') - 1
    kk = np.clip(k, 0, len(r) - 1)
    return (k >= 0) & (pos < r[kk, 1])


def main():
    net, sites, af, out = sys.argv[1:5]
    lvl1 = defaultdict(list)
    nest = defaultdict(list)
    cur = None
    with gzip.open(net, 'rt') as fh:
        for line in fh:
            if line.startswith('net '):
                cur = line.split()[1]
                continue
            if cur not in CH:
                continue
            ind = len(line) - len(line.lstrip(' '))
            f = line.split()
            if f[0] == 'fill':
                rng = (int(f[1]), int(f[1]) + int(f[2]))
                (lvl1 if ind == 1 else nest)[cur].append(rng)
    top_all, nest_all, H_all, C_all, inm_all, pc_all = [], [], [], [], [], []
    for c in CH:
        z = np.load('%s/snv_%s.npz' % (sites, c))
        a = np.load('%s/snvaf_%s.npz' % (af, c))
        pos = z['pos'].astype(np.int64)
        isnest = inside(merge(nest[c]), pos)
        in1 = inside(merge(lvl1[c]), pos)
        top_all.append(in1 & ~isnest)
        nest_all.append(isnest)
        hb, cb, gb = z['hb'], z['cb'], z['gb']
        H_all.append((gb < 4) & (gb == cb))
        C_all.append((gb < 4) & (gb == hb))
        inm_all.append(a['inmask'] == 1)
        pc_all.append(a['pc'])
    top, nst, H, C, inm, pc = [np.concatenate(x) for x in (top_all, nest_all, H_all, C_all, inm_all, pc_all)]
    res = dict(n=len(top), top_level=int(top.sum()), nested=int(nst.sum()), neither=int((~top & ~nst).sum()))
    for nm, sel in (('top & H & mask', top & H & inm), ('nested & H & mask', nst & H & inm),
                    ('top & C & mask', top & C & inm), ('nested & C & mask', nst & C & inm),
                    ('top & mask (all pol)', top & inm), ('nested & mask (all pol)', nst & inm)):
        res[nm] = dict(n=int(sel.sum()), poly_T01=float((pc[sel] >= 0.01).mean()) if sel.any() else None)
    # corrected ratio on top-level SNV count only: scale 35.02 M (GAP-07b, all primary chr) by the top-level share,
    # symmetric treatment, indels as in the main report (not recomputed here)
    sH_top = res['top & H & mask']['poly_T01']
    n_top_primary = 35017058
    res['ratio_top_level_snv_symmetric'] = dict(
        s_H_top=sH_top, fixed_snv=n_top_primary * (1 - sH_top),
        note='indels (4.30 M, share from the main report, human lineage net w=2 in mask) and 33,466 other events added separately in the note')
    json.dump(res, open(out, 'w'), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
