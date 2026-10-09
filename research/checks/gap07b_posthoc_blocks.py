"""GAP-07b POST HOC (NOT pre-registered): exact aligned-block coverage and "clean" gap base pairs.

Written AFTER the main run of gap07b_alignment_count.py (commit 3c847b8 registered it; the full run's output is in
results/raw/gap07b_*). The main run showed that the base-pair side of the ladder is unstable (indel gap bp 597 Mb raw,
270 Mb without flagged assembly-N, 134 Mb without repeat-masked gaps) while the event count is stable (4.30M indel
events). Large gaps (> 1 kb) carry 93% of the gap bp. This script asks what those base pairs are, using the chain
blocks themselves (exact aligned intervals) rather than net-fill extents:

  1. aligned blocks of the netted chains (human: disjoint; chimp: union) -> exact "bp not in any aligned block" for the
     human primary chromosomes and for chimp placed / unplaced sequence (non-N).
  2. every indel event (chain gap inside the net, as in the main run) -> base pairs on each side that are NOT assembly N
     (hg38 / panTro6 gap tables) and NOT aligned elsewhere (inside another netted block, i.e. rearranged/duplicated
     sequence): "clean" bp. Events whose clean bp is < 50% of raw bp are "mostly N or aligned elsewhere".

Not a prediction test; descriptive. Same conventions as the main script (primary human chromosomes chr1-22,X,Y;
chain gap counted when it lies in a net fill of the same chain id). Deterministic.

Run: research/.venv/bin/python -I research/checks/gap07b_posthoc_blocks.py --chain CHAIN --work WORK_EV_DIR \
       --t-sizes ... --q-sizes ... --t-gaps ... --q-gaps ... --out OUT.json
(WORK_EV_DIR holds fill_ranges.npz written by the main script's net stage.)
"""
import argparse
import gzip
import json
import os
from array import array
from collections import defaultdict

import numpy as np

PRIMARY_T = {'chr%d' % i for i in range(1, 23)} | {'chrX', 'chrY'}
SZ_EDGES = np.array([1, 2, 11, 51, 1001])
SZ_NAMES = ['1', '2-10', '11-50', '51-1000', '>1000']
import re
QPRIMARY = re.compile(r'^chr(\d+[AB]?|X|Y)$')


def read_sizes(path):
    return {l.split()[0]: int(l.split()[1]) for l in open(path)}


def read_gaps(path):
    d = defaultdict(list)
    with gzip.open(path, 'rt') as fh:
        for line in fh:
            f = line.rstrip('\n').split('\t')
            d[f[1]].append((int(f[2]), int(f[3])))
    return d


class Rows:
    def __init__(self):
        self.k = defaultdict(lambda: (array('q'), array('q'), array('q')))   # seq -> eid, start, len

    def add(self, seq, eid, s, ln):
        a = self.k[seq]
        a[0].append(eid); a[1].append(s); a[2].append(ln)


def main():
    ap = argparse.ArgumentParser()
    for k in ('chain', 'work', 't-sizes', 'q-sizes', 't-gaps', 'q-gaps', 'out'):
        ap.add_argument('--' + k)
    a = ap.parse_args()
    tsz = read_sizes(a.t_sizes); qsz = read_sizes(a.q_sizes)
    tgap = read_gaps(a.t_gaps); qgap = read_gaps(a.q_gaps)
    z = np.load(os.path.join(a.work, 'fill_ranges.npz'))
    byid = defaultdict(list)
    for i, s_, e_, c in zip(z['id'].tolist(), z['tS'].tolist(), z['tE'].tolist(), z['chrom'].tolist()):
        byid[i].append((s_, e_, c))

    tblk = Rows(); qblk = Rows()           # aligned blocks (eid unused = 0)
    tgp = Rows(); qgp = Rows()             # gap sides, eid = event id
    ev_kind = array('b'); ev_size = array('q')
    eid = 0
    with gzip.open(a.chain, 'rt') as fh:
        active = None
        for line in fh:
            if line.startswith('chain'):
                f = line.split()
                cid = int(f[12])
                active = byid.get(cid) if f[2] in PRIMARY_T else None
                if active is not None:
                    tname = f[2]
                    qname = f[7]; qS = int(f[8]); strand = f[9]
                    p = int(f[5]); q = int(f[10])
                continue
            if active is None or not line.strip():
                continue
            f = line.split()
            size = int(f[0])
            inside = any(fs <= p < fe for fs, fe, c in active)
            if inside:
                tblk.add(tname, 0, p, size)
                qa = q if strand == '+' else qS - (q + size)
                qblk.add(qname, 0, qa, size)
            p += size; q += size
            if len(f) == 3:
                dt, dq = int(f[1]), int(f[2])
                ok = any((dt > 0 and fs <= p and p + dt <= fe) or (dt == 0 and fs < p < fe) for fs, fe, c in active)
                if ok:
                    if dt > 0:
                        tgp.add(tname, eid, p, dt)
                    if dq > 0:
                        qa = q if strand == '+' else qS - (q + dq)
                        qgp.add(qname, eid, qa, dq)
                    ev_kind.append(0 if dq == 0 else (1 if dt == 0 else 2))
                    ev_size.append(max(dt, dq))
                    eid += 1
                p += dt; q += dq
    n_ev = eid
    ev_size = np.frombuffer(ev_size, dtype=np.int64)
    ev_kind = np.frombuffer(ev_kind, dtype=np.int8)

    def side(blk, gp, sizes, ngap, seqs):
        """per sequence: aligned bp, N bp, non-N unaligned bp, plus per-event clean bp and raw bp contributions"""
        raw = np.zeros(n_ev, np.int64); clean = np.zeros(n_ev, np.int64); nbp = np.zeros(n_ev, np.int64); alel = np.zeros(n_ev, np.int64)
        tot = dict(length=0, N=0, aligned=0, unaligned_nonN=0)
        for s in seqs:
            if s not in sizes:
                continue
            Ls = sizes[s]
            al = np.zeros(Ls, bool); nn = np.zeros(Ls, bool)
            if s in blk.k:
                for st, ln in zip(blk.k[s][1], blk.k[s][2]):
                    al[st:st + ln] = True
            for x, y in ngap.get(s, ()):
                nn[x:y] = True
            tot['length'] += Ls; tot['N'] += int(nn.sum()); tot['aligned'] += int((al & ~nn).sum())
            tot['unaligned_nonN'] += int((~al & ~nn).sum())
            if s in gp.k:
                e_, st_, ln_ = (np.frombuffer(x, dtype=np.int64) for x in gp.k[s])
                csN = np.concatenate(([0], np.cumsum(nn, dtype=np.int32)))
                csA = np.concatenate(([0], np.cumsum(al & ~nn, dtype=np.int32)))
                en = st_ + ln_
                nb = (csN[en] - csN[st_]).astype(np.int64)
                ab = (csA[en] - csA[st_]).astype(np.int64)
                np.add.at(raw, e_, ln_); np.add.at(nbp, e_, nb); np.add.at(alel, e_, ab)
                np.add.at(clean, e_, ln_ - nb - ab)
        return tot, raw, nbp, alel, clean

    th, raw_t, n_t, a_t, c_t = side(tblk, tgp, tsz, tgap, sorted(PRIMARY_T))
    qprim = [s for s in qsz if QPRIMARY.match(s)]
    qoth = [s for s in qsz if not QPRIMARY.match(s)]
    qp, raw_qp, n_qp, a_qp, c_qp = side(qblk, qgp, qsz, qgap, qprim)
    qo, raw_qo, n_qo, a_qo, c_qo = side(qblk, qgp, qsz, qgap, qoth)
    raw = raw_t + raw_qp + raw_qo; nbp = n_t + n_qp + n_qo; alel = a_t + a_qp + a_qo; clean = c_t + c_qp + c_qo

    out = dict(events=int(n_ev), human=th, chimp_placed=qp, chimp_unplaced=qo)
    out['by_size'] = {}
    sc = np.searchsorted(SZ_EDGES, ev_size, side='right') - 1
    for s, nm in enumerate(SZ_NAMES):
        m = sc == s
        mostly = m & (clean < 0.5 * raw)
        out['by_size'][nm] = dict(events=int(m.sum()), raw_bp=int(raw[m].sum()), N_bp=int(nbp[m].sum()),
                                  aligned_elsewhere_bp=int(alel[m].sum()), clean_bp=int(clean[m].sum()),
                                  events_mostly_N_or_elsewhere=int(mostly.sum()), raw_bp_of_those=int(raw[mostly].sum()))
    out['by_kind'] = {}
    for k, nm in enumerate(['human_only', 'chimp_only', 'both']):
        m = ev_kind == k
        out['by_kind'][nm] = dict(events=int(m.sum()), raw_bp=int(raw[m].sum()), clean_bp=int(clean[m].sum()))
    big = np.argsort(-ev_size)[:15]
    out['largest_15'] = [dict(size=int(ev_size[i]), kind=int(ev_kind[i]), raw=int(raw[i]), N=int(nbp[i]),
                              elsewhere=int(alel[i]), clean=int(clean[i])) for i in big]
    # size decades of events > 1 kb
    dec = {}
    for lo, hi in ((1000, 10000), (10000, 100000), (100000, 1000000), (1000000, 10 ** 12)):
        m = (ev_size >= lo) & (ev_size < hi)
        dec['%d-%d' % (lo, min(hi, 10 ** 9))] = dict(events=int(m.sum()), raw_bp=int(raw[m].sum()), clean_bp=int(clean[m].sum()))
    out['decades_gt1kb'] = dec
    json.dump(out, open(a.out, 'w'), indent=1)
    print(json.dumps({k: out[k] for k in ('events', 'human', 'chimp_placed', 'chimp_unplaced')}))
    print(json.dumps(out['by_size'], indent=1))
    print(json.dumps(out['by_kind']))
    print(json.dumps(out['decades_gt1kb']))
    print(json.dumps(out['largest_15']))


if __name__ == '__main__':
    main()
