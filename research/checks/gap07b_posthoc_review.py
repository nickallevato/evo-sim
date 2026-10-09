"""GAP-07b POST HOC, review-fix pass (NOT pre-registered). Written after the main run (3c847b8 / 51cea1f), after the
first post hoc pass (c1727f0) and after three reviews (f8625f6). Every number it prints is post hoc and is labelled so
in R4-GAP07b-alignment.md. It adds no new data downloads.

Subcommands
  arith  : combines the committed JSON outputs (gap07b_{net,axt,posthoc_blocks,posthoc_polarize}.json) and the chain event
           arrays into
             (a) the ratio bracket: raw pooled 205M / events per lineage, the Day-favourable repeat-unit and indel-slippage
                 sensitivities, the critic-favourable corrections (human lineage only, SNV records <2% divergence,
                 SNV-polymorphism fraction 0.78-0.86 applied to SNVs only or to all events, MNV merge, gap-merge d = 1, 10, 50);
             (b) the weight per large event that 205M would need;
             (c) SNV-only shortfall at Day's MITTENS 3.0 s7.3 rates on the measured SNV and event counts;
             (d) per-lineage event counts recomputed with the stated symmetric polarization rule (review M2), for all sizes
                 and for sizes <= 50 bp only (review M1: the rule is blind above ~100 bp), plus the pre-registered rule by
                 size class;
             (e) a base-rate check for the 410.09 Mb coincidence (subsets of 2-5 of 14 components within +-0.1% of 410).
  nested : re-reads the net (level >= 2 fills = nested/rearranged) and the pan axt and splits SNVs and valid columns into
           records whose t-start lies in a top-level fill versus in a nested fill (reviewer request: SNVs inside nested
           fills, identity of nested fills, the SNV/base overlap).
Run: research/.venv/bin/python -I research/checks/gap07b_posthoc_review.py arith --raw RAWDIR --ev EVDIR --out OUT.json
     research/.venv/bin/python -I research/checks/gap07b_posthoc_review.py nested --net NET --axt AXT --out OUT.json
(No RNG. Both use the same primary-chromosome convention as the main script.)
"""
import argparse
import gzip
import itertools
import json
import os
import sys

import numpy as np

PRIMARY = ['chr%d' % i for i in range(1, 23)] + ['chrX', 'chrY']
LUT = np.full(256, 4, np.uint8)
for _i, _c in enumerate('ACGT'):
    LUT[ord(_c)] = _i
    LUT[ord(_c.lower())] = _i
LUT[ord('-')] = 5


def arith(a):
    R = a.raw.rstrip('/') + '/'
    axt = json.load(open(R + 'gap07b_axt.json')); net = json.load(open(R + 'gap07b_net.json'))
    blk = json.load(open(R + 'gap07b_posthoc_blocks.json')); pol = json.load(open(R + 'gap07b_posthoc_polarize.json'))
    snv = np.array(axt['snv'])[0]                       # dc, pol, ts, near, rep
    cev = np.array(axt['cev_count']).sum(axis=(2, 3, 4))   # kind, size, pol (pre-registered rule)
    S0 = int(snv.sum()); S2 = int(snv[0].sum()); IND = int(cev.sum())
    NEST = sum(v[0] for k, v in net['fills'].items() if '|L2|' in k)
    SEG_MAIN = net['unaligned_human']['n'] + net['unaligned_chimp_placed']['n']       # main-run report definition (1,421)
    EV_MAIN = S0 + IND + NEST + SEG_MAIN                                               # 42,102,514
    EV_POSTHOC_LADDER = EV_MAIN + net['unaligned_chimp_unplaced']['n']                 # 42,108,545 (not used)
    out = {'EV_MAIN': EV_MAIN, 'EV_POSTHOC_LADDER': EV_POSTHOC_LADDER}
    print('events (main-run report definition) %d ; with unplaced-scaffold segments %d' % (EV_MAIN, EV_POSTHOC_LADDER))
    DAY = 205e6
    pl = EV_MAIN / 2
    print('\n## (a) ratio bracket (205M / events per lineage)')
    rows = []

    def add(name, ev_lineage, note):
        rows.append((name, ev_lineage, DAY / ev_lineage, note))
    add('RAW pooled (pre-registered headline)', pl, 'total/2')
    # --- critic-favourable
    pm = pol['5']
    ps = {w: np.array(pol[str(w)]) for w in (2, 5, 10, 20)}          # kind(human_only, chimp_only), size, pol
    pc = [int(snv[:, p].sum()) for p in range(4)]                     # snv pol totals: 0 unpol, 1 human, 2 chimp, 3 third
    unpol_snv = pc[0] + pc[3]
    cplx = int(cev[2].sum())
    perlin = {}
    for w in (2, 5, 10, 20):
        t = ps[w]
        for lab, sel in (('all sizes', slice(0, 5)), ('<=50 bp polarized', slice(0, 3))):
            hum = t[:, sel, 1].sum(); chi = t[:, sel, 2].sum()
            single_total = int(cev[:2].sum())
            ind_unp = single_total - hum - chi + cplx            # everything not polarized, incl. complex and >50 bp
            h = pc[1] + 0.5 * unpol_snv + hum + 0.5 * ind_unp
            c = pc[2] + 0.5 * unpol_snv + chi + 0.5 * ind_unp
            perlin[(w, lab)] = (h, c)
    for (w, lab), (h, c) in perlin.items():
        print('per-lineage events, SNV split + symmetric indels w=%d (%s): human %.0f chimp %.0f ; 205M/human %.2f ; 205M/chimp %.2f' % (w, lab, h, c, DAY / h, DAY / c))
    out['per_lineage'] = {'%d|%s' % k: v for k, v in perlin.items()}
    h5 = perlin[(5, '<=50 bp polarized')][0]; hmax = max(v[0] for v in perlin.values()); hmin = min(v[0] for v in perlin.values())
    add('human lineage alone (w=5, indels <=50 bp polarized) [post hoc]', h5, 'SNV gorilla split + symmetric indel rule; range over w %.2f-%.2f M' % (hmin / 1e6, hmax / 1e6))
    add('<2%-divergence SNV records only [post hoc; threshold chosen after the CSAC miss]', (S2 + IND + NEST + SEG_MAIN) / 2, 'drops 4.0 M SNVs in paralog/nested/low-quality records')
    for fx in (0.78, 0.86):
        add('fixed share %.2f applied to SNVs only [post hoc]' % fx, (fx * S0 + IND + NEST + SEG_MAIN) / 2, 'CSAC 14-22%% polymorphism is an SNV estimate')
    for fx in (0.78, 0.86):
        add('fixed share %.2f applied to ALL events [post hoc]' % fx, fx * EV_MAIN / 2, 'assumes indels/SVs are as polymorphic as SNVs (unmeasured)')
    for fx in (0.78, 0.86):
        add('<2%% records and fixed share %.2f on SNVs (not additive) [post hoc]' % fx, (fx * S2 + IND + NEST + SEG_MAIN) / 2, 'upper end; overlaps')
    adj = int(axt['ncol']['P/adjacent_mismatch_pairs'])
    add('MNV runs merged (adjacent mismatches count once) [post hoc]', (EV_MAIN - adj) / 2, 'critic-favourable correction, unused in the main run')
    # gap merge from chain events
    for d in (1, 10, 50):
        merged = 0
        for c in PRIMARY:
            z = np.load(os.path.join(a.ev, 'chainev_%s.npz' % c))
            p, dt = z['tS'], z['tSz']
            gap = p[1:] - (p[:-1] + dt[:-1])
            merged += int(((gap >= 0) & (gap <= d)).sum())
        add('indel gaps merged if separated by <= %d aligned bp [post hoc]' % d, (EV_MAIN - merged) / 2, '%d merges (same-chain adjacency approximated by file order)' % merged)
        out['gapmerge_%d' % d] = merged
    # --- Day-favourable
    A223 = blk['human']['unaligned_nonN'] + blk['chimp_placed']['unaligned_nonN']
    nest_ali = sum(v[3] for k, v in net['fills'].items() if '|L2|' in k)
    A486 = A223 + 2 * nest_ali
    print('\nnon-aligned non-N bp (human + chimp placed) %d ; plus nested aligned both sides %d' % (A223, A486))
    for unit in (171, 32, 6, 2, 1):
        for lab, bp in (('non-aligned only', A223), ('non-aligned + nested aligned', A486)):
            extra = bp / unit
            add('Day-favourable: %s counted as %d-bp units (replaces nothing; ADDED to events) [post hoc]' % (lab, unit), (EV_MAIN + extra) / 2, '+%.2f M events' % (extra / 1e6))
    for k in (2, 3):
        add('Day-favourable: indel events x%d (microsatellite slippage / merged opposite steps) [post hoc]' % k, (EV_MAIN + (k - 1) * IND) / 2, 'assumption, not measured')
    print('| reading | events per lineage | 205M / that | note |')
    print('|---|---|---|---|')
    for n_, e_, r_, note in rows:
        print('| %s | %.2f M | %.2f | %s |' % (n_, e_ / 1e6, r_, note))
    out['bracket'] = [(n_, e_, r_) for n_, e_, r_, _ in rows]

    print('\n## (b) weight per large event needed for 205M per lineage')
    big = int(cev[:, 3:].sum()); big1k = int(cev[:, 4].sum())
    for lab, n in ((' >50 bp', big), (' >1000 bp', big1k)):
        w = (DAY - (pl - n / 2)) / (n / 2)
        print('events%s: %d (%d per lineage); others weight 1 -> weight needed per event = %.0f SNV-equivalents' % (lab, n, n / 2, w))
        out['weight' + lab.strip()] = w
    avg51 = float(np.array(axt['cev_tbp']).sum(axis=(0, 2, 3, 4, 5))[3] + np.array(axt['cev_qbp']).sum(axis=(0, 2, 3, 4, 5))[3]) / cev[:, 3].sum()
    print('mean raw bp per 51-1000 bp event %.0f' % avg51)

    print('\n## (c) SNV-only shortfall at MITTENS 3.0 s7.3 rates (252,000 generations)')
    for gf, lab in ((1322, 'non-mutator 1,322 gen/fix'), (105, 'mutator 105 gen/fix'), (1587, 'strict 1,587 gen/fix')):
        ach = 252000 / gf
        for nm, req in (('Day 17.5M', 17.5e6), ('measured SNV/2', S0 / 2), ('measured SNV(<2%)/2', S2 / 2), ('measured events/2', pl),
                        ('fixed-corrected events 0.78', 0.78 * EV_MAIN / 2), ('fixed-corrected events 0.86', 0.86 * EV_MAIN / 2)):
            print('%s: achievable %.1f ; %s %.2f M -> shortfall %.0f' % (lab, ach, nm, req / 1e6, req / ach))

    print('\n## (d) indel polarization by size class')
    print('pre-registered rule (human share of polarized) by kind and size:')
    for k, kn in enumerate(['human_only', 'chimp_only']):
        print(' ', kn, [round(float(cev[k, s, 1] / max(1, cev[k, s, 1] + cev[k, s, 2])), 3) for s in range(5)], 'polarized fraction', [round(float((cev[k, s, 1] + cev[k, s, 2]) / cev[k, s].sum()), 3) for s in range(5)])
    for w in (2, 5, 10, 20):
        t = ps[w]
        print(' post hoc w=%d <=50 bp: human share %.3f ; >50 bp: %.3f ; polarized fraction <=50 bp %.3f, >50 bp %.3f' % (
            w, t[:, :3, 1].sum() / (t[:, :3, 1].sum() + t[:, :3, 2].sum()), t[:, 3:, 1].sum() / max(1, t[:, 3:, 1].sum() + t[:, 3:, 2].sum()),
            (t[:, :3, 1].sum() + t[:, :3, 2].sum()) / t[:, :3].sum(), (t[:, 3:, 1].sum() + t[:, 3:, 2].sum()) / t[:, 3:].sum()))

    print('\n## (e) 410 Mb coincidence base rate')
    comp = [134.5, 88.6, 187.0, 131.3, 59.5, 37.8, 44.9, 192.4, 359.3, 37.5, 59.8, 95.1, 161.6, 596.7]
    n_sub = 0; hits = []
    for r in range(2, 6):
        for sub in itertools.combinations(range(len(comp)), r):
            n_sub += 1
            s = sum(comp[i] for i in sub)
            if abs(s - 410.0) <= 0.41:
                hits.append((round(s, 2), sub))
    sums = [sum(comp[i] for i in sub) for r in range(2, 6) for sub in itertools.combinations(range(len(comp)), r)]
    dens = np.mean(np.abs(np.array(sums) - 410.0) <= 0.41)
    print('subsets %d ; within +-0.1%% of 410: %d ; fraction %.5f' % (n_sub, len(hits), dens))
    print('hits:', hits)
    out['coincidence'] = dict(subsets=n_sub, hits=len(hits), frac=float(dens))
    json.dump(out, open(a.out, 'w'), default=float)


def nested(a):
    tops = {c: [] for c in PRIMARY}; nest = {c: [] for c in PRIMARY}
    cur = None
    with gzip.open(a.net, 'rt') as fh:
        for line in fh:
            if line.startswith('net '):
                cur = line.split()[1]; continue
            if cur not in tops:
                continue
            ind = len(line) - len(line.lstrip(' '))
            f = line.split()
            if f[0] != 'fill':
                continue
            s, sz = int(f[1]), int(f[2])
            (tops if ind == 1 else nest)[cur].append((s, s + sz))
    ranges = {}
    for c in PRIMARY:
        n = sorted(nest[c])
        ranges[c] = (np.array([x for x, _ in n], np.int64), np.array([y for _, y in n], np.int64))
    # union-free membership test: a record is nested if its tStart lies inside any nested range
    # (ranges can overlap hierarchically; use a running-max end over sorted starts)
    ends_max = {c: (np.maximum.accumulate(ranges[c][1]) if len(ranges[c][1]) else np.array([], np.int64)) for c in PRIMARY}
    acc = {k: np.zeros(4, np.int64) for k in ('top', 'nested')}   # records, valid columns, SNVs, SNVs in records >=2% div
    with gzip.open(a.axt, 'rb') as fh:
        hdr = None; s1 = None
        for line in fh:
            if line.startswith(b'#'):
                continue
            line = line.rstrip(b'\n')
            if hdr is None:
                if not line:
                    continue
                hdr = line.split()
            elif s1 is None:
                s1 = line
            else:
                tN = hdr[1].decode()
                if tN in tops:
                    ts = int(hdr[2]) - 1
                    st, en = ranges[tN]
                    i = np.searchsorted(st, ts, side='right') - 1
                    isn = bool(i >= 0 and ends_max[tN][i] > ts)
                    ca = LUT[np.frombuffer(s1, np.uint8)]; cb = LUT[np.frombuffer(line, np.uint8)]
                    vd = (ca < 4) & (cb < 4)
                    nv = int(vd.sum()); nm = int((vd & (ca != cb)).sum())
                    k = 'nested' if isn else 'top'
                    acc[k] += np.array([1, nv, nm, nm if nm / max(nv, 1) >= 0.02 else 0])
                hdr = None; s1 = None
    out = {k: dict(records=int(v[0]), valid=int(v[1]), snv=int(v[2]), snv_in_records_ge2pct=int(v[3]),
                   divergence=float(v[2] / max(v[1], 1))) for k, v in acc.items()}
    print(json.dumps(out, indent=1))
    json.dump(out, open(a.out, 'w'))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    x = sp.add_parser('arith'); x.add_argument('--raw'); x.add_argument('--ev'); x.add_argument('--out')
    n = sp.add_parser('nested'); n.add_argument('--net'); n.add_argument('--axt'); n.add_argument('--out')
    a = ap.parse_args()
    {'arith': arith, 'nested': nested}[a.cmd](a)


if __name__ == '__main__':
    main()
