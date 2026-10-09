"""GAP-07b: DIRECT count of human-chimpanzee divergence EVENTS from a real whole-genome alignment (UCSC hg38 vs
panTro6 net/axtNet), with base pairs reported next to events, optional lineage polarization with a gorilla outgroup
(hg38 vs gorGor6 axtNet), masking sensitivity, and comparison with Chimp Consortium 2005 / Yoo 2025.
THROWAWAY research check (not product code). Replaces the rate-based estimate of gap07_event_counts.py (R4 GAP-07).

PRE-REGISTRATION (written and committed BEFORE the full run; see git log). Everything changed afterwards is
labelled post hoc in a separate commit.

DISCLOSURE of what was seen before registering: the first ~3 KB of the axt file, the first ~30 lines of the net file
and the chain header (to design the parsers); the record count (157,734) and chromosome order of the pan axt file;
file sizes/md5; the hg38 gap-table N total (161.6 Mb) and the hg38 centromere-model total (59.5 Mb). No SNV, indel or
event counts had been computed in the sense of the predictions. A smoke test on a truncated prefix (first 60k net lines,
first 777 axt records) was run only to debug the code; it showed two DESIGN facts, which changed the design before
registration, and nothing else was used: (i) net `gap` lines are intervals on the human (target) side, so a chimp-only
insertion (human extent 0) never appears as a net gap; chain files (dt, dq per block pair) are therefore used for the
complete indel event list; (ii) in the axt file records are broken at chain gaps larger than 100 bp (in-record gap runs
are <= 100 bp), so axt gap runs cover only small gaps. No smoke-test number was used to set any prediction below.

DATA (downloads untrusted; under sources/raw/ucsc-2026-10-09/, gitignored; this script lives outside it and takes
paths as arguments; run as research/.venv/bin/python -I):
  pan/hg38.panTro6.net.gz         net: fills (aligned segments, by type top/syn/nonSyn/inv...) and gaps (indels)
  pan/hg38.panTro6.net.axt.gz     gapped alignments of the net (target hg38, query panTro6; soft-masked lowercase)
  gor/hg38.gorGor6.net.axt.gz     outgroup alignment (hg38 vs gorilla) for polarization
  meta/*gap.txt.gz, *.chrom.sizes, hg38 centromeres.txt.gz  (assembly N runs, sizes, hg38 centromere models)
Scope: human primary chromosomes chr1-22, X, Y ("primary"); alt/random/Un contigs and chrM are tallied separately or
dropped, because hg38 ALT contigs duplicate primary sequence (counting them would double-count loci).

STAGES (subcommands): net   (fills by type, net gap lines with N/repeat/TRF flags, unaligned segments, fill ranges)
                      chain (complete indel event list = chain gaps (dt,dq) inside net fills, found by chain id + t range)
                      gor   (gorilla bases per human position -> work/*.npz)
                      axt   (SNVs per alignment column, in-record gap runs <=100 bp with flags, lineage polarization
                             of SNVs and of chain gaps and net gaps)
                      report (tables, ratios, sensitivity, comparison with 205M / 410M / CSAC / Yoo)

DEFINITIONS
  SNV difference   : alignment column with A/C/G/T in both species that differ (N and gaps excluded). One column =
                     one SNV; adjacent columns also tallied as runs (MNV). Counts BOTH lineages plus any ancestral
                     polymorphism (CSAC: 14-22% of differences are polymorphic, not fixed).
  indel event      : one chain gap (dt, dq) inside a netted alignment (chain id and t range match a net fill):
                     human-only bases (dt>0, dq=0), chimp-only bases (dq>0, dt=0), or both non-empty ("both",
                     complex). Size class = max(dt,dq): 1, 2-10, 11-50, 51-1000, >1000 bp. Flags (N, repeat) for
                     gaps <= 100 bp come from axt gap runs (inserted sequence), for larger human-containing gaps from
                     the net gap line; large chimp-only gaps carry no flags (counted as passing every filter).
  large gap        : indel event > 1000 bp (chain), plus unaligned segments (maximal non-N stretches outside every net fill),
                     counted separately for human and chimp, with a flag for overlap with hg38 centromere models.
  rearrangement fill: a net fill at level >= 2 (types syn/nonSyn/inv/...), counted by type and size.
  lineage          : SNV is human-derived if gorilla base == chimp base, chimp-derived if gorilla == human base,
                     "third" if gorilla differs from both, unpolarized if no gorilla base. Net gap polarized by gorilla
                     coverage (see polarize_events). Unpolarized events are split 50/50 only in the "per lineage" row.
  base pairs       : SNV bp = SNV count; gap bp = sum(tSize+qSize) over indel events; unaligned bp = non-N bases outside
                     all net fills (human primary chromosomes; chimp sequences aligned from them). Ladder:
                       L1 = SNV;  L2 = L1 + indel events (events) / + gap bp (bp);
                       L3 = L2 + unaligned segments + nested fills (events) / + unaligned bp (bp)  [Yoo-style].
  masking          : F0 raw; F1 drop sites/events touching assembly N; F2 = F1 + drop repeat-driven (SNV lowercase in
                     either species; gap with >=50% repeat-masked bases); F3 = F2 + drop SNV within 5 columns of a gap
                     or in an alignment record >5% divergent, drop gaps with any TRF simple-repeat base and gaps
                     involving unplaced chimp scaffolds; F4 (gaps only) = syntenic net (parent fill top/syn) without
                     nested children.

PRE-REGISTERED PREDICTIONS (point value; band). P-numbers are referred to in the results note.
  P1  SNV differences, primary chr, F0, both lineages: 30M (27-35M); divergence 1.15-1.35% of valid aligned columns;
      Ts/Tv 2.0-2.2.
  P2  Indel events (all chain gaps in the net, F0), both lineages: 5M (3.5-6.5M); i.e. 2-3.3M per lineage-polarized.
      Size mix: 1 bp 40-55%, 2-10 bp 35-45%, 11-50 bp 6-10%, 51-1000 bp 2-4%, >1000 bp 0.05-0.3% (about 3-15k events).
      Complex ("both") gaps < 8% of events. This also decides CSAC's ambiguous "~5 million events in each species":
      I expect the TOTAL (human-only + chimp-only events) to be ~5M, NOT 5M per species (falsifier: total > 8M).
  P3  Gap bp (human-only + chimp-only): 60-110 Mb total (CSAC: ~32 + ~35 Mb); events > 50 bp are < 5% of events but
      > 50% of gap bp.
  P4  Events, F0, primary: SNV + indel + rearrangement fills + unaligned segments = 33-45M both lineages (point 38M);
      per lineage 16-23M. Rearrangement fills (levels >=2) and unaligned segments together < 5% of events (< 2M).
  P5  Base pairs: L1 = 30M, L2 = 100-170M, L3 (adds unaligned human+chimp bp) = 300-700M, bracketing Day's 410M.
      bp/event: L2 3-5, L3 7-18 -> the 410M "genomic differences" are ~10x the event count; the base-pair figure is
      reached only by adding unaligned/non-1:1 sequence (incl. centromere models, which overlap > 30% of human
      unaligned bp) counted per base.
  P6  Lineage split: of polarizable SNVs 47-51% human-derived; polarizable fraction >= 85%, "third" 1-5%.
      Indels: human share of polarized events 40-52%; polarizable fraction 60-90% of single-sided events.
  P7  Masking: F1 changes SNV < 1% and indel events < 3%; F2 removes 35-55% of SNVs and 20-45% of indel events;
      F3 reduces total events by 40-60% in total; but L3/events bp/event stays within 6-25 under every filter
      (i.e. the order of magnitude is not a masking artefact).
  P8  Yoo 2025 comparison: unaligned (non-1:1) share of the human primary genome 5-12% and of chimp 5-12% (Yoo:
      12.5-27.3% across apes by a different, stricter definition; I expect mine lower); nested/net inversion fills
      >= 10 kb: 200-1,500 events (Yoo curated 1,140 across six apes).

WHAT WOULD FAVOUR DAY (the unit of "required fixations" is a bp):
  - events per lineage (polarized, F0) of ~100M or more, or a robust event count within ~3x of 205M;
  - bp/event at L3 of 3 or less under every masking filter (F0-F3);
  - lineage polarization showing that one lineage carries far more than half the events (then A3d's "halve it" fails
    and the human lineage would have to explain more than the symmetric share).
WHAT WOULD FAVOUR THE CRITICS: events per lineage 15-30M and bp/event at L3 near 10 (P4, P5), robust to masking (P7).
PARTIAL / MIXED: alignment fragmentation (one true event split into several net gaps) and repeat artefacts bias event
counts UPWARD (Day-favouring); ancestral polymorphism inflates SNV/indel counts relative to FIXED differences (a
Day-favouring bias if polymorphic differences are counted as required fixations, a critic-favouring one if not).
A count of 60-100M events per lineage would shrink the 205M/event-count gap to 2-3x and would be a partial Day result.

Deterministic, no RNG. Pure parsing + numpy.
"""
import argparse
import gzip
import json
import os
import re
import sys
from array import array
from collections import Counter, defaultdict

import numpy as np

PRIMARY_T = {'chr%d' % i for i in range(1, 23)} | {'chrX', 'chrY'}
QPRIMARY = re.compile(r'^chr(\d+[AB]?|X|Y)$')
SZ_EDGES = np.array([1, 2, 11, 51, 1001])          # size classes: 1 | 2-10 | 11-50 | 51-1000 | >1000
SZ_NAMES = ['1', '2-10', '11-50', '51-1000', '>1000']
KINDS = ['human_only', 'chimp_only', 'both']       # tSize>0,q=0 | t=0,qSize>0 | both>0
DC_EDGES = np.array([0.02, 0.05, 0.10])            # record divergence classes: <2% | 2-5% | 5-10% | >=10%
NEAR = 5

LUT = np.full(256, 4, np.uint8)                    # 0-3 ACGT, 4 other/N, 5 gap
for _i, _c in enumerate('ACGT'):
    LUT[ord(_c)] = _i
    LUT[ord(_c.lower())] = _i
LUT[ord('-')] = 5
LOW = np.zeros(256, bool)
LOW[97:123] = True


def sz_class(n):
    return int(np.searchsorted(SZ_EDGES, n, side='right') - 1)


def read_sizes(path):
    d = {}
    with open(path) as fh:
        for line in fh:
            f = line.split()
            d[f[0]] = int(f[1])
    return d


def read_intervals(path, chrom_col=1, s_col=2, e_col=3):
    d = defaultdict(list)
    with gzip.open(path, 'rt') as fh:
        for line in fh:
            f = line.rstrip('\n').split('\t')
            d[f[chrom_col]].append((int(f[s_col]), int(f[e_col])))
    return d


def segments_of(mask):
    """maximal True runs of a boolean array -> (starts, lengths)"""
    d = np.diff(np.concatenate(([0], mask.view(np.int8), [0])))
    s = np.flatnonzero(d == 1)
    e = np.flatnonzero(d == -1)
    return s, e - s


# ----------------------------------------------------------------------------------------------- NET stage
def tabulate_events(tS, tSz, qSz, flag, ch, pt, pol):
    """flag 0..15 (N=1, rep=2, trf=4, unplaced=8); ch 0/1 children; pt 0/1 parent fill is top/syn; pol 0/1/2.
    Returns counts, sum tSize, sum qSize arrays of shape (3 kinds, 5 sizes, 16 flags, 2, 2, 3)."""
    kind = np.where(qSz == 0, 0, np.where(tSz == 0, 1, 2))
    size = np.maximum(tSz, qSz)
    sc = np.searchsorted(SZ_EDGES, size, side='right') - 1
    idx = ((((kind * 5 + sc) * 16 + flag) * 2 + ch) * 2 + pt) * 3 + pol
    n = 3 * 5 * 16 * 2 * 2 * 3
    shape = (3, 5, 16, 2, 2, 3)
    return (np.bincount(idx, minlength=n).reshape(shape).astype(np.int64),
            np.bincount(idx, weights=tSz, minlength=n).reshape(shape).astype(np.int64),
            np.bincount(idx, weights=qSz, minlength=n).reshape(shape).astype(np.int64))


def net_stage(a):
    tsz = read_sizes(a.t_sizes)
    qsz = read_sizes(a.q_sizes)
    tgap = read_intervals(a.t_gaps)
    qgap = read_intervals(a.q_gaps)
    cen = read_intervals(a.t_cen)
    os.makedirs(a.work, exist_ok=True)

    fill_tab = defaultdict(lambda: [0, 0, 0, 0, 0])     # (type, level>=2?, size class) -> n, tSize, qSize, ali, qDup
    fr_id, fr_s, fr_e, fr_c = array('q'), array('q'), array('q'), []   # fill ranges on primary t (for the chain stage)
    big10k = Counter()                                  # nested fills with max(t,q) >= 10 kb by type
    qcover = defaultdict(list)                          # qName -> [(s,e)] for fills on primary t
    tcover = defaultdict(list)                          # level-1 fills on primary t chromosomes
    cols = None
    cur = None
    primary = False
    open_gaps = []                                      # stack of gap dicts awaiting children information
    types = {}
    counts = Counter()

    def new_cols():
        return {k: array('q') for k in ('tS', 'tSz', 'qSz', 'flag', 'ch', 'pt', 'level')}

    def flush_chrom():
        if cols is not None and len(cols['tS']):
            np.savez(os.path.join(a.work, 'events_%s.npz' % cur), **{k: np.frombuffer(v, dtype=np.int64) for k, v in cols.items()})

    def finalize(g):
        if not primary:
            return
        tS, tSz, qSz = g['tS'], g['tSz'], g['qSz']
        tot = tSz + qSz
        flag = int((g['tN'] + g['qN']) > 0) + 2 * int((g['tR'] + g['qR']) >= 0.5 * tot) + \
            4 * int((g['tTrf'] + g['qTrf']) > 0) + 8 * int(g['unpl'])
        ptop = int(g['ptype'] in ('top', 'syn'))
        for k, v in (('tS', tS), ('tSz', tSz), ('qSz', qSz), ('flag', flag), ('ch', int(g['ch'])), ('pt', ptop), ('level', g['level'])):
            cols[k].append(v)

    with gzip.open(a.net, 'rt') as fh:
        for line in fh:
            if line.startswith('net '):
                for g in open_gaps:
                    finalize(g)
                open_gaps = []
                if cur is not None and primary:
                    flush_chrom()
                cur = line.split()[1]
                primary = cur in PRIMARY_T
                cols = new_cols() if primary else None
                types = {}
                continue
            indent = len(line) - len(line.lstrip(' '))
            f = line.split()
            kind = f[0]
            while open_gaps and open_gaps[-1]['indent'] >= indent:
                finalize(open_gaps.pop())
            if kind == 'fill' and open_gaps and open_gaps[-1]['indent'] < indent:
                open_gaps[-1]['ch'] = True
            kv = dict(zip(f[7::2], f[8::2]))
            tS, tSz_, qName, strand, qS, qSz_ = int(f[1]), int(f[2]), f[3], f[4], int(f[5]), int(f[6])
            if kind == 'fill':
                typ = kv.get('type', '?')
                types[indent] = typ
                if primary:
                    sc = sz_class(max(tSz_, qSz_))
                    row = fill_tab[(typ, 1 if indent == 1 else 2, sc)]
                    row[0] += 1; row[1] += tSz_; row[2] += qSz_; row[3] += int(kv.get('ali', 0)); row[4] += int(kv.get('qDup', 0))
                    qcover[qName].append((qS, qS + qSz_))
                    fr_id.append(int(kv['id'])); fr_s.append(tS); fr_e.append(tS + tSz_); fr_c.append(cur)
                    if indent > 1 and max(tSz_, qSz_) >= 10000:
                        big10k[typ] += 1
                    if indent == 1:
                        tcover[cur].append((tS, tS + tSz_))
            else:
                if primary:
                    g = dict(indent=indent, level=indent, tS=tS, tSz=tSz_, qSz=qSz_, ch=False,
                             ptype=types.get(indent - 1, '?'), unpl=not QPRIMARY.match(qName))
                    for k in ('tN', 'qN', 'tR', 'qR', 'tTrf', 'qTrf'):
                        g[k] = int(kv.get(k, 0))
                    open_gaps.append(g)
        for g in open_gaps:
            finalize(g)
        if primary:
            flush_chrom()

    np.savez(os.path.join(a.work, 'fill_ranges.npz'), id=np.frombuffer(fr_id, np.int64), tS=np.frombuffer(fr_s, np.int64),
             tE=np.frombuffer(fr_e, np.int64), chrom=np.array(fr_c))
    # ---- tabulate events (unpolarized) over primary chromosomes
    tot = None
    levelhist = Counter()
    for c in sorted(PRIMARY_T):
        p = os.path.join(a.work, 'events_%s.npz' % c)
        if not os.path.exists(p):
            continue
        z = np.load(p)
        t = tabulate_events(z['tS'], z['tSz'], z['qSz'], z['flag'], z['ch'], z['pt'], np.zeros(len(z['tS']), np.int64))
        tot = t if tot is None else tuple(x + y for x, y in zip(tot, t))
        for lv, n in zip(*np.unique(z['level'], return_counts=True)):
            levelhist[int(lv)] += int(n)

    # ---- unaligned (outside every net fill) non-N segments
    def uncovered(cover, sizes, ngap, seqs, cenint=None):
        res = dict(n=0, bp=0, by_size={n: [0, 0] for n in SZ_NAMES}, cen_bp=0, per_seq={})
        for s in seqs:
            if s not in sizes:
                continue
            L = sizes[s]
            m = np.zeros(L, bool)
            for x, y in cover.get(s, ()):
                m[x:y] = True
            for x, y in ngap.get(s, ()):
                m[x:y] = True
            u = ~m
            st, ln = segments_of(u)
            res['n'] += int(len(st)); res['bp'] += int(ln.sum())
            for sc, name in enumerate(SZ_NAMES):
                sel = (np.searchsorted(SZ_EDGES, ln, side='right') - 1) == sc
                res['by_size'][name][0] += int(sel.sum()); res['by_size'][name][1] += int(ln[sel].sum())
            if cenint is not None:
                cm = np.zeros(L, bool)
                for x, y in cenint.get(s, ()):
                    cm[x:y] = True
                res['cen_bp'] += int((u & cm).sum())
            nn = np.zeros(L, bool)
            for x, y in ngap.get(s, ()):
                nn[x:y] = True
            res['per_seq'][s] = [L, int(nn.sum()), int(ln.sum()), int(len(st))]
        return res

    un_t = uncovered(tcover, tsz, tgap, sorted(PRIMARY_T), cen)
    un_q = {}
    qprim = [s for s in qsz if QPRIMARY.match(s)]
    qother = [s for s in qsz if not QPRIMARY.match(s)]
    un_q['placed'] = uncovered(qcover, qsz, qgap, qprim)
    un_q['unplaced'] = uncovered(qcover, qsz, qgap, qother)
    tN_prim = sum(int(v[1]) for v in un_t['per_seq'].values())
    tL_prim = sum(int(v[0]) for v in un_t['per_seq'].values())

    out = dict(
        stage='net', n_gap_events=int(tot[0].sum()) if tot else 0, level_hist=dict(levelhist),
        ev_count=tot[0].tolist(), ev_tbp=tot[1].tolist(), ev_qbp=tot[2].tolist(),
        ev_dims=['kind(human_only,chimp_only,both)', 'size(1,2-10,11-50,51-1000,>1000)', 'flag(N1,rep2,trf4,unpl8)',
                 'children', 'parent_top_or_syn', 'pol(0 unpol,1 human,2 chimp)'],
        fills={'%s|L%s|%s' % k: v for k, v in sorted(fill_tab.items())}, nested_ge10kb=dict(big10k),
        unaligned_human=un_t, unaligned_chimp_placed=un_q['placed'], unaligned_chimp_unplaced=un_q['unplaced'],
        human_primary_length=tL_prim, human_primary_N=tN_prim)
    for d in (out['unaligned_human'], out['unaligned_chimp_placed'], out['unaligned_chimp_unplaced']):
        d['per_seq'] = {k: v for k, v in list(d['per_seq'].items())[:60]}
    json.dump(out, open(a.out, 'w'))
    print('net stage done: gap events (primary) = %d' % out['n_gap_events'])


# ----------------------------------------------------------------------------------------------- CHAIN stage
def chain_stage(a):
    """Complete indel event list: every chain gap (dt, dq) of a chain that is used in the net, restricted to the net
    fill (same chain id, junction inside the fill's t range). Chain gaps with dt=dq=0 do not exist."""
    z = np.load(os.path.join(a.work, 'fill_ranges.npz'))
    byid = defaultdict(list)
    for i, s_, e_, c in zip(z['id'].tolist(), z['tS'].tolist(), z['tE'].tolist(), z['chrom'].tolist()):
        byid[i].append((s_, e_, c))
    cols = defaultdict(lambda: {k: array('q') for k in ('tS', 'dt', 'dq')})
    nchains = 0
    chain_bp_in = 0
    with gzip.open(a.chain, 'rt') as fh:
        active = None
        p = 0
        for line in fh:
            if line.startswith('chain'):
                f = line.split()
                cid = int(f[12])
                active = byid.get(cid) if f[2] in PRIMARY_T else None
                if active is not None:
                    nchains += 1
                    p = int(f[5])
                continue
            if active is None or not line.strip():
                continue
            f = line.split()
            if len(f) == 3:
                p += int(f[0])
                dt, dq = int(f[1]), int(f[2])
                for fs, fe, c in active:
                    if (dt > 0 and fs <= p and p + dt <= fe) or (dt == 0 and fs < p < fe):
                        d = cols[c]
                        d['tS'].append(p); d['dt'].append(dt); d['dq'].append(dq)
                        break
                p += dt
            else:
                p += int(f[0])
    tot = None
    for c in sorted(PRIMARY_T):
        if c not in cols:
            continue
        d = {k: np.frombuffer(v, dtype=np.int64) for k, v in cols[c].items()}
        np.savez(os.path.join(a.work, 'chainev_%s.npz' % c), tS=d['tS'], tSz=d['dt'], qSz=d['dq'])
        zero = np.zeros(len(d['tS']), np.int64)
        t = tabulate_events(d['tS'], d['dt'], d['dq'], zero, zero, zero, zero)
        tot = t if tot is None else tuple(x + y for x, y in zip(tot, t))
    json.dump(dict(stage='chain', chains_used=nchains, n_events=int(tot[0].sum()),
                   cev_count=tot[0].tolist(), cev_tbp=tot[1].tolist(), cev_qbp=tot[2].tolist()), open(a.out, 'w'))
    print('chain stage done: chains used %d, indel events %d' % (nchains, tot[0].sum()))


# ----------------------------------------------------------------------------------------------- AXT iteration
def iter_axt(path):
    """yield (tName, tS0, tE, qName, strand, seq_t_bytes, seq_q_bytes) for each record; skips '#' comment lines."""
    with gzip.open(path, 'rb') as fh:
        hdr = None
        s1 = None
        for line in fh:
            if line.startswith(b'#') or line.startswith(b'\n') and hdr is None:
                continue
            line = line.rstrip(b'\n')
            if hdr is None:
                if not line:
                    continue
                hdr = line.split()
            elif s1 is None:
                s1 = line
            else:
                yield hdr[1].decode(), int(hdr[2]) - 1, int(hdr[3]), hdr[4].decode(), hdr[7].decode(), s1, line
                hdr = None
                s1 = None


# ----------------------------------------------------------------------------------------------- GOR stage
def gor_stage(a):
    tsz = read_sizes(a.t_sizes)
    os.makedirs(a.work, exist_ok=True)
    cur = None
    gb = gi = None
    done = set()

    def flush():
        if cur in PRIMARY_T and gb is not None:
            np.savez_compressed(os.path.join(a.work, 'gor_%s.npz' % cur), gbase=gb, gins=gi)
    n = 0
    for tN, tS, tE, qN, st, s1, s2 in iter_axt(a.axt):
        if tN != cur:
            flush()
            if tN in done:
                sys.exit('gorilla axt not grouped by chromosome: %s' % tN)
            done.add(tN)
            cur = tN
            if tN in PRIMARY_T:
                gb = np.full(tsz[tN], 255, np.uint8)
                gi = np.zeros(tsz[tN], np.uint16)
            else:
                gb = gi = None
        if gb is None:
            continue
        ca = LUT[np.frombuffer(s1, np.uint8)]
        cb = LUT[np.frombuffer(s2, np.uint8)]
        ga = ca == 5
        nong = ~ga
        k = int(nong.sum())
        gb[tS:tS + k] = cb[nong]
        if ga.any():
            st_, ln = segments_of(ga)
            tc = np.cumsum(nong)
            pos = tS + np.where(st_ > 0, tc[np.maximum(st_ - 1, 0)], 0)
            ok = pos < len(gi)
            np.add.at(gi, pos[ok], np.minimum(ln[ok], 65535).astype(np.uint16))
        n += 1
    flush()
    print('gor stage done: %d records' % n)


# ----------------------------------------------------------------------------------------------- AXT stage
def polarize_events(z, gbase, gins):
    """Lineage of net gap events from gorilla: returns pol array (0 unpolarized, 1 human lineage, 2 chimp lineage)."""
    tS = z['tS']; tSz = z['tSz']; qSz = z['qSz']
    n = len(gbase)
    pol = np.zeros(len(tS), np.int64)
    # chimp-only bases (human has a junction at tS): human deletion (gorilla also has bases there) vs chimp insertion
    m = (tSz == 0) & (qSz > 0)
    if m.any():
        p = tS[m]
        gi = np.zeros(len(p), np.int64)
        for off in range(-2, 3):
            q = np.clip(p + off, 0, n - 1)
            gi += gins[q]
        flank = (gbase[np.clip(p - 1, 0, n - 1)] < 4) & (gbase[np.clip(p, 0, n - 1)] < 4)
        L = qSz[m]
        res = np.zeros(len(p), np.int64)
        res[(gi >= np.maximum(1, 0.5 * L)) & (gi <= 2 * L + 2)] = 1        # gorilla has the bases too -> human deleted them
        res[(gi == 0) & flank] = 2                                          # gorilla contiguous -> chimp inserted
        pol[m] = res
    # human-only bases: gorilla aligned there (ancestral present -> chimp deleted) vs absent (human insertion)
    m = (tSz > 0) & (qSz == 0)
    if m.any():
        cs = np.concatenate(([0], np.cumsum(gbase < 4, dtype=np.int32)))
        p = tS[m]; L = tSz[m]
        e = np.minimum(p + L, n)
        frac = (cs[e] - cs[np.minimum(p, n)]) / np.maximum(L, 1)
        flank = (gbase[np.clip(p - 1, 0, n - 1)] < 4) & (gbase[np.clip(p + L, 0, n - 1)] < 4)
        res = np.zeros(len(p), np.int64)
        res[(frac >= 0.5) & flank] = 2                                      # gorilla has them -> chimp lost them
        res[(frac <= 0.1) & flank] = 1                                      # gorilla lacks them -> human insertion
        pol[m] = res
    return pol


def axt_stage(a):
    tsz = read_sizes(a.t_sizes)
    use_gor = a.work is not None and os.path.isdir(a.work) and any(f.startswith('gor_') for f in os.listdir(a.work))
    # accumulators
    snv = np.zeros((2, 4, 4, 2, 2, 2), np.int64)     # group(P,O), dc, pol, ts, near, rep
    valid = np.zeros((2, 4, 2), np.int64)            # group, dc, rep  : valid columns
    ncol = Counter()
    gaprun_n = np.zeros((2, 2, 5, 2, 2, 2), np.int64)   # group, side(0 human-gap=chimp-only,1 chimp-gap=human-only), size, rep, N, adj
    gaprun_bp = np.zeros((2, 2, 5, 2, 2, 2), np.int64)
    ev_tab = None
    cev_tab = None
    rec_hist = Counter()
    cur = None
    gb = gi = None
    done_events = set()

    def finish_chrom(c):
        nonlocal ev_tab, cev_tab
        if c is None or c not in PRIMARY_T:
            return
        p = os.path.join(a.events, 'events_%s.npz' % c)
        if os.path.exists(p):
            z = np.load(p)
            pol = polarize_events(z, gb, gi) if gb is not None else np.zeros(len(z['tS']), np.int64)
            t = tabulate_events(z['tS'], z['tSz'], z['qSz'], z['flag'], z['ch'], z['pt'], pol)
            ev_tab = t if ev_tab is None else tuple(x + y for x, y in zip(ev_tab, t))
            done_events.add(c)
        p = os.path.join(a.events, 'chainev_%s.npz' % c)
        if os.path.exists(p):
            z = np.load(p)
            pol = polarize_events(z, gb, gi) if gb is not None else np.zeros(len(z['tS']), np.int64)
            zero = np.zeros(len(z['tS']), np.int64)
            t = tabulate_events(z['tS'], z['tSz'], z['qSz'], zero, zero, zero, pol)
            cev_tab = t if cev_tab is None else tuple(x + y for x, y in zip(cev_tab, t))

    nrec = 0
    for tN, tS, tE, qN, st, s1, s2 in iter_axt(a.axt):
        if tN != cur:
            finish_chrom(cur)
            cur = tN
            gb = gi = None
            if use_gor and tN in PRIMARY_T:
                zp = os.path.join(a.work, 'gor_%s.npz' % tN)
                if os.path.exists(zp):
                    zz = np.load(zp)
                    gb, gi = zz['gbase'], zz['gins']
        nrec += 1
        grp = 0 if tN in PRIMARY_T else 1
        a_ = np.frombuffer(s1, np.uint8)
        b_ = np.frombuffer(s2, np.uint8)
        ca = LUT[a_]; cb = LUT[b_]
        ga = ca == 5; gbm = cb == 5
        vd = (ca < 4) & (cb < 4)
        rep = LOW[a_] | LOW[b_]
        mm = vd & (ca != cb)
        nv = int(vd.sum()); nm = int(mm.sum())
        dc = int(np.searchsorted(DC_EDGES, nm / max(nv, 1), side='right'))
        ncol['%s/columns' % 'PO'[grp]] += len(ca)
        ncol['%s/N_columns' % 'PO'[grp]] += int(((ca == 4) | (cb == 4)).sum())
        vr = np.bincount(rep[vd].astype(np.int64), minlength=2)
        valid[grp, dc] += vr
        gm = ga | gbm
        idx = np.flatnonzero(mm)
        if len(idx):
            ts = ((ca[idx] ^ cb[idx]) == 2).astype(np.int64)
            if gm.any():
                cs = np.concatenate(([0], np.cumsum(gm, dtype=np.int32)))
                near = ((cs[np.minimum(idx + NEAR + 1, len(ca))] - cs[np.maximum(idx - NEAR, 0)]) > 0).astype(np.int64)
            else:
                near = np.zeros(len(idx), np.int64)
            pol = np.zeros(len(idx), np.int64)
            if gb is not None and grp == 0:
                pos = tS + np.cumsum(~ga)[idx] - 1
                g = gb[pos]
                pol[g == cb[idx]] = 1          # gorilla == chimp -> human-derived
                pol[g == ca[idx]] = 2          # gorilla == human -> chimp-derived
                pol[(g < 4) & (g != cb[idx]) & (g != ca[idx])] = 3
            comb = (((pol * 2 + ts) * 2 + near) * 2 + rep[idx].astype(np.int64))
            snv[grp, dc] += np.bincount(comb, minlength=32).reshape(4, 2, 2, 2)
            ncol['%s/adjacent_mismatch_pairs' % 'PO'[grp]] += int((mm[1:] & mm[:-1]).sum())
        if grp == 0 and gm.any():
            for side, g_, other, oth_gap in ((0, ga, cb, gbm), (1, gbm, ca, ga)):
                if not g_.any():
                    continue
                st_, ln = segments_of(g_)
                en = st_ + ln
                low = LOW[b_ if side == 0 else a_]
                csN = np.concatenate(([0], np.cumsum(other == 4, dtype=np.int32)))
                csR = np.concatenate(([0], np.cumsum(low, dtype=np.int32)))
                hasN = ((csN[en] - csN[st_]) > 0).astype(np.int64)
                repf = ((csR[en] - csR[st_]) >= 0.5 * ln).astype(np.int64)
                adj = (oth_gap[np.maximum(st_ - 1, 0)] & (st_ > 0)) | (oth_gap[np.minimum(en, len(ca) - 1)] & (en < len(ca)))
                sc = np.searchsorted(SZ_EDGES, ln, side='right') - 1
                comb = (((sc * 2 + repf) * 2 + hasN) * 2 + adj.astype(np.int64))
                gaprun_n[grp, side] += np.bincount(comb, minlength=40).reshape(5, 2, 2, 2)
                gaprun_bp[grp, side] += np.bincount(comb, weights=ln, minlength=40).reshape(5, 2, 2, 2).astype(np.int64)
        if nrec % 20000 == 0:
            print('records', nrec, tN, flush=True)
    finish_chrom(cur)
    out = dict(stage='axt', records=nrec, used_gorilla=bool(use_gor),
               snv=snv.tolist(), snv_dims=['group(P primary,O other)', 'recdiv class(<2%,2-5,5-10,>=10)',
                                           'pol(0 unpol,1 human-derived,2 chimp-derived,3 third)', 'transition', 'near_gap(+-5)', 'lowercase_either'],
               valid=valid.tolist(), valid_dims=['group', 'recdiv class', 'lowercase_either'],
               ncol=dict(ncol),
               axt_gaps_n=gaprun_n.tolist(), axt_gaps_bp=gaprun_bp.tolist(),
               axt_gaps_dims=['group', 'side(0 chimp-only [human gap],1 human-only)', 'size', 'rep>=50%', 'N', 'adjacent opposite gap'],
               ev_count=ev_tab[0].tolist() if ev_tab else None, ev_tbp=ev_tab[1].tolist() if ev_tab else None,
               ev_qbp=ev_tab[2].tolist() if ev_tab else None,
               cev_count=cev_tab[0].tolist() if cev_tab else None, cev_tbp=cev_tab[1].tolist() if cev_tab else None,
               cev_qbp=cev_tab[2].tolist() if cev_tab else None,
               events_chroms=sorted(done_events))
    json.dump(out, open(a.out, 'w'))
    print('axt stage done: %d records' % nrec)


# ----------------------------------------------------------------------------------------------- REPORT stage
def f_m(x):
    return '%.2fM' % (x / 1e6) if abs(x) >= 1e5 else '%d' % x


def report_stage(a):
    net = json.load(open(a.net_json))
    axt = json.load(open(a.axt_json))
    snv = np.array(axt['snv'])[0]                 # primary: dc, pol, ts, near, rep
    valid = np.array(axt['valid'])[0]
    cev = np.array(axt['cev_count']).sum(axis=(2, 3, 4))                       # (kind, size, pol)
    cbp = (np.array(axt['cev_tbp']) + np.array(axt['cev_qbp'])).sum(axis=(2, 3, 4))
    nev = np.array(axt['ev_count']); nbp = np.array(axt['ev_tbp']) + np.array(axt['ev_qbp'])
    gn = np.array(axt['axt_gaps_n'])[0]; gbp = np.array(axt['axt_gaps_bp'])[0]   # side, size, rep, N, adj
    out = {}
    L = []
    P = L.append

    # ---------------- SNV
    N_f0 = int(snv.sum())
    f2 = int(snv[:, :, :, :, 0].sum())
    f3 = int(snv[:2, :, :, 0, 0].sum())
    nv = int(valid.sum()); nv_unrep = int(valid[:, 0].sum())
    ts = int(snv[:, :, 1].sum()); tv = int(snv[:, :, 0].sum())
    P('## SNV differences (primary chromosomes; both lineages plus polymorphism)')
    P('| filter | SNVs | share of F0 |')
    P('|---|---|---|')
    P('| F0 raw (columns with N already excluded) | %d | 1.000 |' % N_f0)
    P('| F1 (no N) | %d | 1.000 |' % N_f0)
    P('| F2 drop lowercase (repeat-masked) in either species | %d | %.3f |' % (f2, f2 / N_f0))
    P('| F3 = F2 + drop within 5 columns of a gap + alignment records >5%% divergent | %d | %.3f |' % (f3, f3 / N_f0))
    P('')
    P('valid columns %d; SNV/valid = %.4f; unmasked valid %d, SNV/unmasked valid = %.4f; Ts/Tv = %.3f; adjacent mismatch pairs %d; N columns (excluded) %d' % (
        nv, N_f0 / nv, nv_unrep, f2 / max(nv_unrep, 1), ts / max(tv, 1), axt['ncol'].get('P/adjacent_mismatch_pairs', 0), axt['ncol'].get('P/N_columns', 0)))
    P('')
    P('| polarization (F0) | SNVs | share of polarizable |')
    P('|---|---|---|')
    pcount = [int(snv[:, p].sum()) for p in range(4)]
    pp = sum(pcount[1:])
    for p, name in enumerate(['unpolarized (no gorilla base)', 'human-derived', 'chimp-derived', 'third state']):
        P('| %s | %d | %s |' % (name, pcount[p], '' if p == 0 else '%.3f' % (pcount[p] / max(pp, 1))))
    P('| human-derived share of (human + chimp derived) | | %.3f |' % (pcount[1] / max(pcount[1] + pcount[2], 1)))
    P('')
    for lab, mask in (('F0', None), ('F2 (not lowercase)', 'rep'), ('F3', 'f3')):
        if mask is None:
            sub = snv
        elif mask == 'rep':
            sub = snv[:, :, :, :, 0:1]
        else:
            sub = snv[:2, :, :, 0:1, 0:1]
        c = [int(sub[:, p].sum()) for p in range(4)]
        P('polarized SNV %s: human %d, chimp %d, third %d, unpolarized %d; human share %.3f' % (
            lab, c[1], c[2], c[3], c[0], c[1] / max(c[1] + c[2], 1)))
    P('')

    # ---------------- indels (chain)
    tot_e = int(cev.sum()); tot_bp = int(cbp.sum())
    P('## Indel events (chain gaps inside the net), primary chromosomes, both lineages')
    P('| size class | human-only events | chimp-only events | both-sided events | all events | share of events | bp | share of bp |')
    P('|---|---|---|---|---|---|---|---|')
    for s, sn in enumerate(SZ_NAMES):
        P('| %s | %d | %d | %d | %d | %.4f | %d | %.3f |' % (sn, cev[0, s].sum(), cev[1, s].sum(), cev[2, s].sum(), cev[:, s].sum(),
                                                         cev[:, s].sum() / tot_e, cbp[:, s].sum(), cbp[:, s].sum() / tot_bp))
    P('| all | %d | %d | %d | %d | 1 | %d | 1 |' % (cev[0].sum(), cev[1].sum(), cev[2].sum(), tot_e, tot_bp))
    P('')
    hb = int(sum(np.array(axt['cev_tbp']).sum(axis=(1, 2, 3, 4, 5)))); cbq = int(np.array(axt['cev_qbp']).sum())
    P('human-only bp (tSize sum) %d ; chimp-only bp (qSize sum) %d ; events/bp %.2f' % (hb, cbq, tot_bp / tot_e))
    P('')
    P('| polarization of single-sided chain gaps (F0) | events | bp |')
    P('|---|---|---|')
    for p, nme in enumerate(['unpolarized', 'human lineage', 'chimp lineage']):
        P('| %s | %d | %d |' % (nme, cev[:2, :, p].sum(), cbp[:2, :, p].sum()))
    P('| complex (both-sided), unpolarized | %d | %d |' % (cev[2].sum(), cbp[2].sum()))
    P('')
    P('| size class | human lineage | chimp lineage | unpolarized (single-sided) |')
    P('|---|---|---|---|')
    for s, sn in enumerate(SZ_NAMES):
        P('| %s | %d | %d | %d |' % (sn, cev[:2, s, 1].sum(), cev[:2, s, 2].sum(), cev[:2, s, 0].sum()))
    P('')
    P('### Validation against other representations')
    P('| size class | chain gaps (all kinds) | axt in-record gap runs (<=100 bp) | net gap lines (human-containing) |')
    P('|---|---|---|---|')
    for s, sn in enumerate(SZ_NAMES):
        P('| %s | %d | %d | %d |' % (sn, cev[:, s].sum(), gn[:, s].sum(), nev[:, s].sum()))
    P('')

    # ---------------- masking sensitivity for indels
    def indel_filtered(k):
        e_tot = 0; b_tot = 0
        for s in range(5):
            base_e = int(cev[:, s].sum()); base_b = int(cbp[:, s].sum())
            if s <= 2:
                g = gn[:, s]; gb_ = gbp[:, s]
                keep = np.zeros((2, 2, 2), bool)                       # rep, N, adj
                for rep in range(2):
                    for N in range(2):
                        for adj in range(2):
                            keep[rep, N, adj] = (k < 1 or N == 0) and (k < 2 or rep == 0) and (k < 3 or adj == 0)
                rem_e = int(g.sum() - (g * keep[None]).sum())
                rem_b = int(gb_.sum() - (gb_ * keep[None]).sum())
            else:
                bits = [0, 1, 3, 15][k]
                sel = np.array([(f & bits) == 0 for f in range(16)])
                rem_e = int(nev[:, s].sum() - nev[:, s][:, sel].sum())
                rem_b = int(nbp[:, s].sum() - nbp[:, s][:, sel].sum())
            e_tot += base_e - rem_e; b_tot += base_b - rem_b
        return e_tot, b_tot
    P('### Masking sensitivity of indel events')
    P('| filter | events | gap bp | bp/event |')
    P('|---|---|---|---|')
    FT = []
    for k, name in enumerate(['F0 raw', 'F1 no assembly-N in gap', 'F2 + not repeat-masked (>=50%)', 'F3 + no TRF/unplaced-chimp (net gaps), no adjacent opposite gap (axt)']):
        e_, b_ = indel_filtered(k)
        FT.append((e_, b_))
        P('| %s | %d | %d | %.2f |' % (name, e_, b_, b_ / e_))
    P('')

    # ---------------- fills / unaligned
    P('## Net fills (primary human chromosomes)')
    P('| type | level | fills | tSize bp | qSize bp | ali bp |')
    P('|---|---|---|---|---|---|')
    agg = defaultdict(lambda: [0, 0, 0, 0])
    for k, v in net['fills'].items():
        typ, lv, sc = k.split('|')
        for i in range(4):
            agg[(typ, lv)][i] += v[i]
    for (typ, lv), v in sorted(agg.items()):
        P('| %s | %s | %d | %d | %d | %d |' % (typ, lv, v[0], v[1], v[2], v[3]))
    P('')
    P('nested fills (level >= 2) with max(t,q) >= 10 kb by type: %s' % json.dumps(net.get('nested_ge10kb', {})))
    P('')
    uh = net['unaligned_human']; uq = net['unaligned_chimp_placed']; uu = net['unaligned_chimp_unplaced']
    P('## Unaligned segments (non-N, outside every net fill)')
    P('| side | segments | bp | segments >1 kb | bp in >1 kb segments | overlap with hg38 centromere models (bp) |')
    P('|---|---|---|---|---|---|')
    for nme, u in (('human primary', uh), ('chimp placed', uq), ('chimp unplaced scaffolds', uu)):
        P('| %s | %d | %d | %d | %d | %s |' % (nme, u['n'], u['bp'], u['by_size']['>1000'][0], u['by_size']['>1000'][1],
                                              u['cen_bp'] if nme == 'human primary' else 'n/a'))
    hl = net['human_primary_length']; hn = net['human_primary_N']
    P('')
    P('human primary: length %d, N %d, non-N %d, unaligned share of non-N = %.4f' % (hl, hn, hl - hn, uh['bp'] / (hl - hn)))
    P('')

    # ---------------- ladder
    nest_events = sum(v[0] for k, v in net['fills'].items() if '|L2|' in k)
    unal_ev = uh['n'] + uq['n']
    unal_bp = uh['bp'] + uq['bp']
    P('## Events vs base pairs ladder (primary chromosomes, both lineages)')
    P('| level / filter | events | bp | bp/event | 410M / events | 205M / (events/2) |')
    P('|---|---|---|---|---|---|')
    snvs = [N_f0, N_f0, f2, f3]
    rows = []
    for k, name in enumerate(['F0', 'F1', 'F2', 'F3']):
        L1 = (snvs[k], snvs[k])
        L2 = (snvs[k] + FT[k][0], snvs[k] + FT[k][1])
        L3 = (L2[0] + nest_events + unal_ev, L2[1] + unal_bp)
        for lab, v in (('L1 SNV', L1), ('L2 + indels', L2), ('L3 + nested fills + unaligned', L3)):
            P('| %s %s | %d | %d | %.2f | %.2f | %.2f |' % (name, lab, v[0], v[1], v[1] / v[0], 410e6 / v[0], 205e6 / (v[0] / 2)))
        rows.append([L1, L2, L3])
    P('')
    # per lineage
    un_s = pcount[0] + pcount[3]
    hs = pcount[1] + 0.5 * un_s; cs_ = pcount[2] + 0.5 * un_s
    ind_h = int(cev[:2, :, 1].sum()); ind_c = int(cev[:2, :, 2].sum()); ind_u = int(cev[:2, :, 0].sum() + cev[2].sum())
    hl_ = hs + ind_h + 0.5 * ind_u
    cl_ = cs_ + ind_c + 0.5 * ind_u
    P('Per-lineage events, F0 (SNV and indel only; unpolarized and complex split 50/50): human %.0f ; chimp %.0f ; mean %.0f ; 205M / mean = %.2f ; 205M / max lineage = %.2f' % (
        hl_, cl_, (hl_ + cl_) / 2, 205e6 / ((hl_ + cl_) / 2), 205e6 / max(hl_, cl_)))
    out = dict(snv=[N_f0, f2, f3], indel_filtered=FT, ladder=rows, per_lineage=[hl_, cl_], total_events=tot_e, total_bp=tot_bp)
    json.dump(out, open(a.out, 'w'))
    print('\n'.join(L))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    n = sp.add_parser('net')
    n.add_argument('--net'); n.add_argument('--t-sizes'); n.add_argument('--q-sizes'); n.add_argument('--t-gaps')
    n.add_argument('--q-gaps'); n.add_argument('--t-cen'); n.add_argument('--work'); n.add_argument('--out')
    c = sp.add_parser('chain')
    c.add_argument('--chain'); c.add_argument('--work'); c.add_argument('--out')
    g = sp.add_parser('gor')
    g.add_argument('--axt'); g.add_argument('--t-sizes'); g.add_argument('--work')
    x = sp.add_parser('axt')
    x.add_argument('--axt'); x.add_argument('--t-sizes'); x.add_argument('--events'); x.add_argument('--work', default=None)
    x.add_argument('--out')
    r = sp.add_parser('report')
    r.add_argument('--net-json'); r.add_argument('--axt-json'); r.add_argument('--out')
    a = ap.parse_args()
    {'net': net_stage, 'chain': chain_stage, 'gor': gor_stage, 'axt': axt_stage, 'report': report_stage}[a.cmd](a)


if __name__ == '__main__':
    main()
