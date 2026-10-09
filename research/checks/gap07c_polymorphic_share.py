"""GAP-07c: how many of the human-chimp differences counted in GAP-07b are still POLYMORPHIC in humans, not fixed?
THROWAWAY research check (not product code). Follows R4-GAP07b-alignment.md (hg38 vs panTro6 net/axtNet, 37.77 M SNV
columns, 4.30 M chain-gap indel events, 42.10 M events in all, 21.05 M per lineage, ratio 205 M / 21.05 M = 9.74) and
asks for the measurement that both GAP-07b steelman reviews requested (Day-6 and Crit-7): GAP-07b only ASSUMED the
Chimpanzee Sequencing and Analysis Consortium (2005) share of 14-22% polymorphic differences, and applied it to SNVs
(and, as an assumption, to all events). Here the share is measured against a public human allele-frequency resource.

PRE-REGISTRATION (written and committed BEFORE the main run; see git log). Anything changed afterwards is labelled
post hoc in a separate commit and in the results note.

DISCLOSURE of what was seen before registering. NO allele frequency, no site match and no polymorphic share of any
GAP-07b site had been computed or looked at. Seen: (i) GAP-07b's own numbers (event counts, polarization, bracket);
(ii) the VCF headers and the first 5 data lines of the 1000 Genomes phase-3 GRCh38 sites file and a handful of lines of
the NYGC 30x chr22 file, to learn the INFO field names (AF is rounded to 2 decimals in the phase-3 sites file, so AC/AN
is used); (iii) file listings and sizes on the 1000 Genomes FTP; (iv) download speed. The predictions below come from
population-genetic reasoning plus the general facts that the 1000 Genomes call set holds about 85 M variant sites of
which roughly 10-15 M have a minor-allele frequency of at least 1%. They do not come from any measurement of the
GAP-07b site lists.

RESOURCE CHOICE (smallest resource that covers the job).
  PRIMARY  1000 Genomes phase-3 integrated biallelic SNV+INDEL call set, GRCh38, sites-only VCF (about 0.98 GB,
           2,548 samples / 5,096 chromosomes, AC/AN plus five super-population AFs, chromosomes 1-22 and X, no Y) and
           the 1000 Genomes GRCh38 "strict" accessibility mask built from the same data (Phase-3 low-coverage reads on
           GRCh38, 122 MB). It is the smallest public set that has per-site AC/AN on GRCh38 and a matching mask.
  CROSS-CHECK  NYGC 1000 Genomes 30x phased panel (3,202 samples; SNV + indel + SV in one file), chr21 and chr22 only
           (0.83 GB). The whole panel is about 28 GB (only the genotype columns are bulky, there is no sites-only copy)
           and the server gave well under 1 MB/s, so only two chromosomes were fetched. They test the resource choice
           and give a small SV (>=50 bp) sample. gnomAD v4 was not used: its genome sites files are hundreds of GB.
  NOT USED  chimpanzee population data. Great Ape Genome Project / de Manuel 2016 variation is in older chimp
           assemblies (or raw reads) and would need a liftover and large downloads. THE CHIMP LINEAGE IS THEREFORE NOT
           MEASURED. It is treated symmetrically by assumption (below), and the result says so.

DEFINITIONS.
  site list        : every alignment column in GAP-07b's axtNet (hg38 vs panTro6, primary chr1-22,X,Y) with A/C/G/T
                     in both species that differ (37,767,396 expected, "F0" of GAP-07b), hg38 position, hg38 base,
                     chimp base, gorilla base (hg38 vs gorGor6 axtNet, as in GAP-07b), flags: lowercase either,
                     near a gap (+-5), record divergence <2%, CpG context in either species, transition,
                     top-level (colinear, net level 1) fill.
  polarization     : gorilla base == chimp base -> human-derived (H); gorilla == hg38 base -> chimp-derived (C);
                     differs from both -> third; no gorilla base -> unpolarized (GAP-07b P6 definition).
  p_chimp          : frequency in the human panel of the allele equal to the CHIMP base at the site (AC/AN of the
                     VCF record whose ALT equals the chimp base; 0 if no such record: "not seen").
                     A difference is FIXED in humans when p_chimp < T (primary T = 0.01) and POLYMORPHIC when
                     p_chimp >= T. This is the reading "the chimp allele still segregates in humans". Reported in
                     bands: 0 | (0,0.001) | [0.001,0.01) | [0.01,0.1) | [0.1,0.5) | [0.5,0.9) | [0.9,0.99) | >=0.99.
                     Sites with p_chimp >= 0.99 are sites where hg38 carries a rare allele (its own private variant).
  p_any            : total non-hg38 allele frequency at the position (secondary measure "hg38 allele not fixed",
                     p_any >= T); also reported.
  population AF    : "any super-population" variant: the chimp-matching record's AF >= T in at least one of
                     AFR/AMR/EAS/EUR/SAS (phase-3 pop AFs are rounded to 2 decimals, so >= 0.01 means >= 0.005).
  callable (mask)  : the share is reported inside the strict mask (central, because outside it polymorphism is
                     under-called, so "fixed" is over-stated) and over all sites (floor). Sites outside the VCF
                     (no variant observed in the panel) count as fixed.
  indel events     : GAP-07b chain-gap events (tS, tSz, qSz, 4,301,652), polarized with the gorilla outgroup by
                     GAP-07b's rule (<= 50 bp reliable). Matched to a VCF indel record of the same net length d
                     (deletion for human-only bases, insertion for chimp-only bases) within +-w bp of the gap start
                     (w = 0, 2, 5; VCF indels are left-normalized and alignment gaps are not). The AF of the matched
                     record is the frequency of the chimp-like state. A NULL control repeats the match at event
                     positions shifted by +10,000 and -10,000 bp (chance match rate in indel-dense regions); the net
                     polymorphic share is observed minus null. Allele content of 1-bp indels is not compared.
  SV (>=50 bp)     : NYGC chr21 and chr22 only. Human-only gap vs DEL record, reciprocal overlap >= 50%;
                     chimp-only gap vs INS/MEI record within 100 bp with SVLEN within 0.5-2x. Small sample.
  corrected ratio  : fixed events = SNV * (1 - s_snv) + indels * (1 - s_ind) + (nested fills and unaligned segments,
                     taken as fixed); per lineage = total / 2; ratio = 205 M / per-lineage fixed events (GAP-07b's
                     pooled-mean convention). Three treatments of the chimp lineage:
                       (a) HUMAN DATA ONLY: s = share measured over all SNVs (human-derived and chimp-derived
                           alike, i.e. the chimp lineage is credited with only the human polymorphism that happens to
                           touch its sites). Day-favourable bound.
                       (b) SYMMETRIC (central): the chimp lineage is assumed to have the same polymorphic share as the
                           human lineage, s_C := s_H measured on the human-derived sites. ASSUMPTION; no chimp
                           population data used.
                       (c) chimp share twice the human one (chimp diversity is higher than human; the factor is
                           arbitrary and only a sensitivity).
                     Why (b) and not (a): the human panel says whether a HUMAN-lineage change is still segregating
                     in humans (human-derived sites). At a chimp-derived site the human panel cannot say whether the
                     change is fixed in chimps; it only shows shared or recurrent variation.

STAGES (subcommands):
  sites   (local, from GAP-07b's axtNet, gorilla work files and the net file) -> snv_<chr>.npz, indel_<chr>.npz
  afq     (workhorse; streams a VCF, joins to the site lists) -> snvaf_<chr>.npz, indelaf_<chr>.npz, baseline.json,
          sv_<chr>.npz for the NYGC file
  report  (local) -> tables and the corrected ratio (JSON + text)

PRE-REGISTERED PREDICTIONS (point; band). Central statistic first.
  Q0  Site list reproduces GAP-07b: 37,767,396 SNV columns (exact) and 4,301,652 indel events (exact).
  Q1  s_H = share of human-derived (H) SNV sites inside the strict mask with p_chimp >= 0.01 (primary):
      15% (10-21%). Reason: about 14 M sites have 1% <= MAF; hg38 carries the derived allele with probability equal to
      the derived-allele frequency (mean about 0.2 for a 1/x spectrum), so about 3 M of roughly 14 M callable H sites.
  Q2  Pooled share over ALL polarized-or-not SNV sites (the human-data-only number): 8% (5-12%).
  Q3  s_C (share of chimp-derived sites with p_chimp >= 0.01, human panel): 1.5% (0.5-4%); s_H / s_C >= 3.
      The human panel cannot stand in for chimp polymorphism: this is a reason for treatment (b).
  Q4  All-sites share is 0-4 percentage points BELOW the in-mask share (sites outside the mask are under-called).
  Q5  Adding the (0, 0.01) band ("seen at all") raises s_H by <= 3 points: polymorphic divergent sites are common ones.
  Q6  Cross-check: s_H on chr21+chr22 from the NYGC 30x panel is within +-3 points of the phase-3 value on the same
      chromosomes. Per-chromosome s_H of the phase-3 autosomes spans no more than +-4 points of the genome value.
  Q7  Reference-allele agreement: >= 99% of matched VCF SNV records have REF == the hg38 base (GRCh38 call set).
  Q8  Indels: net polymorphic share (w = 2, T = 0.01) for human-lineage polarized events 4-12% (point 7%); for events
      > 50 bp (NYGC chr21+22, n a few thousand) <= 10% (point 4%) -- Day's "structural variation is, with very
      few exceptions, post-divergence" (Q100) predicts a lower share than SNVs; I expect it to hold at ~half the SNV one.
  Q9  Corrected per-lineage FIXED events (treatment b): 18.1 M (17.0-19.6 M); ratio 205 M / fixed = 11.3 (10.5-12.1).
      Treatment (a): 19.3 M (18.5-20.0 M), ratio 10.6 (10.3-11.1). Treatment (c): 15.2 M (13.0-17.5 M), ratio
      13.5 (11.7-15.8).
  Q10 Day's SNV-only 17.5 M per lineage lies inside the (a)-(c) range of fixed events per lineage (it did in GAP-07b
      with the assumed 14-22%).

WHAT WOULD FAVOUR DAY: the polymorphic share is small: s_H <= 8% (symmetric ratio <= 10.3, fixed events per lineage
  >= 19.5 M) and/or indel and SV shares near zero. Fewer events are removed, the measured fixed events stay near the
  raw 21 M, and the unit mismatch (event vs base pair) is not helped by "polymorphism". Also: if the chimp-side
  assumption were shown to be too generous. Even then the ratio stays about 10.
WHAT WOULD FAVOUR THE CRITICS: s_H >= 14% (the CSAC range holds at AF >= 1%, symmetric ratio >= 11.3, fixed events
  per lineage <= 18.6 M), and an indel share similar to the SNV share (so that applying the SNV share to all events,
  as the GAP-07b critic row did, is justified).
NEITHER MOVES THE ORDER OF MAGNITUDE: ratios of 10-13 are expected under every outcome. A ratio below 8 or above 15
  under treatments (a)-(b), or an s_H above 30%, would be a surprise that needs explaining.

Deterministic, no RNG. Pure parsing + numpy. Run as research/.venv/bin/python -I.
"""
import argparse
import bisect
import gzip
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

import numpy as np

PRIMARY_T = ['chr%d' % i for i in range(1, 23)] + ['chrX', 'chrY']
LUT = np.full(256, 4, np.uint8)                    # 0-3 ACGT, 4 other/N, 5 gap
for _i, _c in enumerate('ACGT'):
    LUT[ord(_c)] = _i
    LUT[ord(_c.lower())] = _i
LUT[ord('-')] = 5
LOW = np.zeros(256, bool)
LOW[97:123] = True
BASE_CODE = {b'A': 0, b'C': 1, b'G': 2, b'T': 3}
FL_REP, FL_NEAR, FL_LT2, FL_CPG, FL_TS, FL_TOP = 1, 2, 4, 8, 16, 32
DC_LT2 = 0.02
T_PRIMARY = 0.01
BANDS = [0.0, 1e-9, 0.001, 0.01, 0.1, 0.5, 0.9, 0.99]       # lower edges; band 0 = exactly 0 (not seen)
BAND_NAMES = ['0 (not seen)', '(0,0.001)', '[0.001,0.01)', '[0.01,0.1)', '[0.1,0.5)', '[0.5,0.9)', '[0.9,0.99)', '>=0.99']
WINDOWS = (0, 2, 5)
NULL_SHIFTS = (10000, -10000)
KEYSHIFT = 1 << 21


def read_sizes(path):
    d = {}
    with open(path) as fh:
        for line in fh:
            f = line.split()
            d[f[0]] = int(f[1])
    return d


def segments_of(mask):
    d = np.diff(np.concatenate(([0], mask.view(np.int8), [0])))
    s = np.flatnonzero(d == 1)
    e = np.flatnonzero(d == -1)
    return s, e - s


def iter_axt(path):
    """yield (tName, tS0, tE, qName, strand, seq_t_bytes, seq_q_bytes); same parser as gap07b_alignment_count.py"""
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


def polarize_events(tS, tSz, qSz, gbase, gins):
    """copy of gap07b_alignment_count.polarize_events: 0 unpolarized, 1 human lineage, 2 chimp lineage"""
    n = len(gbase)
    pol = np.zeros(len(tS), np.int64)
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
        res[(gi >= np.maximum(1, 0.5 * L)) & (gi <= 2 * L + 2)] = 1
        res[(gi == 0) & flank] = 2
        pol[m] = res
    m = (tSz > 0) & (qSz == 0)
    if m.any():
        cs = np.concatenate(([0], np.cumsum(gbase < 4, dtype=np.int32)))
        p = tS[m]
        L = tSz[m]
        e = np.minimum(p + L, n)
        frac = (cs[e] - cs[np.minimum(p, n)]) / np.maximum(L, 1)
        flank = (gbase[np.clip(p - 1, 0, n - 1)] < 4) & (gbase[np.clip(p + L, 0, n - 1)] < 4)
        res = np.zeros(len(p), np.int64)
        res[(frac >= 0.5) & flank] = 2
        res[(frac <= 0.1) & flank] = 1
        pol[m] = res
    return pol


# ----------------------------------------------------------------------------------------------- SITES stage
def toplevel_ranges(net_path):
    """level-1 (indent 1) fill ranges on the human side, per chromosome"""
    d = defaultdict(list)
    cur = None
    with gzip.open(net_path, 'rt') as fh:
        for line in fh:
            if line.startswith('net '):
                cur = line.split()[1]
                continue
            if cur in PRIMARY_T and line.startswith(' fill') and not line.startswith('  '):
                f = line.split()
                d[cur].append((int(f[1]), int(f[1]) + int(f[2])))
    return {c: np.array(sorted(v), np.int64).reshape(-1, 2) for c, v in d.items()}


def sites_stage(a):
    tsz = read_sizes(a.t_sizes)
    os.makedirs(a.out, exist_ok=True)
    top = toplevel_ranges(a.net)
    cur = None
    gb = gi = None
    acc = defaultdict(list)
    stats = Counter()

    def flush(c):
        if c is None or c not in PRIMARY_T or not acc['pos']:
            acc.clear()
            return
        pos = np.concatenate(acc['pos'])
        o = np.argsort(pos, kind='stable')
        out = {k: np.concatenate(acc[k])[o] for k in ('hb', 'cb', 'gb', 'fl')}
        pos = pos[o]
        if len(pos) > 1 and (np.diff(pos) == 0).any():
            stats['duplicate_positions_' + c] = int((np.diff(pos) == 0).sum())
        r = top.get(c)
        if r is not None and len(r):
            k = np.searchsorted(r[:, 0], pos, side='right') - 1
            kk = np.clip(k, 0, len(r) - 1)
            intop = (k >= 0) & (pos < r[kk, 1])
            out['fl'] = out['fl'] | (intop.astype(np.uint8) * FL_TOP)
        np.savez_compressed(os.path.join(a.out, 'snv_%s.npz' % c), pos=pos.astype(np.int32), **out)
        stats['snv_' + c] = len(pos)
        stats['snv_total'] += len(pos)
        # indels (chain events) with gorilla polarization
        zp = os.path.join(a.events, 'chainev_%s.npz' % c)
        if os.path.exists(zp):
            z = np.load(zp)
            pol = polarize_events(z['tS'], z['tSz'], z['qSz'], gb, gi) if gb is not None else np.zeros(len(z['tS']), np.int64)
            np.savez_compressed(os.path.join(a.out, 'indel_%s.npz' % c), tS=z['tS'].astype(np.int32),
                                tSz=z['tSz'].astype(np.int32), qSz=z['qSz'].astype(np.int32), pol=pol.astype(np.uint8))
            stats['indel_total'] += len(z['tS'])
        acc.clear()
        print('flushed', c, stats['snv_' + c], flush=True)

    for tN, tS, tE, qN, st, s1, s2 in iter_axt(a.axt):
        if tN != cur:
            flush(cur)
            cur = tN
            gb = gi = None
            if tN in PRIMARY_T:
                zz = np.load(os.path.join(a.gor_work, 'gor_%s.npz' % tN))
                gb, gi = zz['gbase'], zz['gins']
        if tN not in PRIMARY_T:
            continue
        a_ = np.frombuffer(s1, np.uint8)
        b_ = np.frombuffer(s2, np.uint8)
        ca = LUT[a_]
        cb = LUT[b_]
        ga = ca == 5
        vd = (ca < 4) & (cb < 4)
        mm = vd & (ca != cb)
        idx = np.flatnonzero(mm)
        if not len(idx):
            continue
        nv = int(vd.sum())
        lt2 = (len(idx) / max(nv, 1)) < DC_LT2
        gm = ga | (cb == 5)
        if gm.any():
            cs = np.concatenate(([0], np.cumsum(gm, dtype=np.int32)))
            near = ((cs[np.minimum(idx + 6, len(ca))] - cs[np.maximum(idx - 5, 0)]) > 0)
        else:
            near = np.zeros(len(idx), bool)
        pos = tS + np.cumsum(~ga)[idx] - 1
        hb = ca[idx]
        cbb = cb[idx]
        g = gb[pos]
        # CpG context in either species (neighbouring alignment columns): C followed by G, or G preceded by C
        prv = np.maximum(idx - 1, 0)
        nxt = np.minimum(idx + 1, len(ca) - 1)
        cpg = np.zeros(len(idx), bool)
        for arr in (ca, cb):
            cpg |= ((arr[idx] == 1) & (arr[nxt] == 2)) | ((arr[idx] == 2) & (arr[prv] == 1))
        rep = LOW[a_[idx]] | LOW[b_[idx]]
        ts = ((hb ^ cbb) == 2)
        fl = (rep.astype(np.uint8) * FL_REP + near.astype(np.uint8) * FL_NEAR + (FL_LT2 if lt2 else 0)
              + cpg.astype(np.uint8) * FL_CPG + ts.astype(np.uint8) * FL_TS)
        acc['pos'].append(pos)
        acc['hb'].append(hb.astype(np.uint8))
        acc['cb'].append(cbb.astype(np.uint8))
        acc['gb'].append(g.astype(np.uint8))
        acc['fl'].append(fl.astype(np.uint8))
    flush(cur)
    json.dump(dict(stats), open(os.path.join(a.out, 'sites_stats.json'), 'w'), indent=1)
    print('sites stage done:', dict(stats))


# ----------------------------------------------------------------------------------------------- AFQ stage
def load_mask(path, sizes, want=None):
    """strict-mask BED (passed sites) -> {chrom: bytearray(1=pass)}; chromosome names with or without chr."""
    # file is a BED of PASS sites: chrom, start, end
    m = {}
    with open(path) as fh:
        for line in fh:
            f = line.split()
            if len(f) < 3:
                continue
            c = f[0] if f[0].startswith('chr') else 'chr' + f[0]
            if c not in sizes or (want is not None and c not in want):
                continue
            if c not in m:
                m[c] = bytearray(sizes[c])
            m[c][int(f[1]):int(f[2])] = b'\x01' * (int(f[2]) - int(f[1]))
    return m


def info_get(info, key, rx_cache={}):
    r = rx_cache.get(key)
    if r is None:
        r = rx_cache[key] = re.compile(rb'(?:^|;)' + key.encode() + rb'=([^;]*)')
    mo = r.search(info)
    return mo.group(1) if mo else None


def af_band(p):
    return np.searchsorted(np.array(BANDS[1:]), p, side='right')   # 0 for p==0 handled by caller (p<=0 -> 0)


def match_indels(ev_pos, ev_d, keys, afs, shift, windows):
    """for each event: max AF over records with the same d within +-w of ev_pos+shift, per window; -1 = no match."""
    n = len(ev_pos)
    maxw = max(windows)
    byabs = np.full((maxw + 1, n), -1.0, np.float32)
    ok = np.abs(ev_d) < KEYSHIFT
    base = ((ev_d.astype(np.int64) + KEYSHIFT) << 32)
    for off in range(-maxw, maxw + 1):
        q = base + (ev_pos.astype(np.int64) + shift + off)
        i = np.minimum(np.searchsorted(keys, q), len(keys) - 1)
        hit = ok & (keys[i] == q)
        v = np.where(hit, afs[i], -1.0).astype(np.float32)
        byabs[abs(off)] = np.maximum(byabs[abs(off)], v)
    res = []
    run = np.full(n, -1.0, np.float32)
    for w in range(maxw + 1):
        run = np.maximum(run, byabs[w])
        if w in windows:
            res.append(run.copy())
    return np.stack(res)


def afq_stage(a):
    sizes = read_sizes(a.t_sizes)
    fmt = a.fmt
    chroms = a.chroms.split(',') if a.chroms else PRIMARY_T
    want = set(chroms)
    mask = load_mask(a.mask, sizes, want)
    os.makedirs(a.out, exist_ok=True)
    popkeys = ['AFR_AF', 'AMR_AF', 'EAS_AF', 'EUR_AF', 'SAS_AF'] if fmt == 'p3' else ['AF_AFR', 'AF_AMR', 'AF_EAS', 'AF_EUR', 'AF_SAS']
    rx_ac = re.compile(rb'(?:^|;)AC=(\d+)')
    rx_an = re.compile(rb'(?:^|;)AN=(\d+)')
    proc = subprocess.Popen(['gzip', '-dc', a.vcf], stdout=subprocess.PIPE, bufsize=1 << 24)
    cur = None
    vc = None            # vcf chrom name
    state = None
    baseline = {'all': np.zeros((2, len(BAND_NAMES)), np.int64)}   # [mask?, band] of ALL SNV records, by AF
    counters = Counter()

    def new_state(c):
        z = np.load(os.path.join(a.sites, 'snv_%s.npz' % c))
        site = np.zeros(sizes[c] + 1, np.uint8)
        site_pos = z['pos']
        site[site_pos] = 1
        z = {k: z[k] for k in z.files}
        return dict(c=c, z=z, site=bytearray(site.tobytes()), snv=defaultdict(list), ind=defaultdict(list), sv=[],
                    mask=mask.get(c))

    def finish(st):
        if st is None:
            return
        c = st['c']
        z = st['z']
        pos = z['pos'].astype(np.int64)
        n = len(pos)
        if st['snv']['pos']:
            vp = np.array(st['snv']['pos'], np.int64)
            o = np.argsort(vp, kind='stable')
            vp = vp[o]
            alt = np.array(st['snv']['alt'], np.uint8)[o]
            ref = np.array(st['snv']['ref'], np.uint8)[o]
            af = np.array(st['snv']['af'], np.float32)[o]
            pm = np.array(st['snv']['pm'], np.uint16)[o]
        else:
            vp = np.zeros(0, np.int64)
            alt = ref = np.zeros(0, np.uint8)
            af = np.zeros(0, np.float32)
            pm = np.zeros(0, np.uint16)
        pc = np.zeros(n, np.float32)
        pany = np.zeros(n, np.float32)
        pcm = np.zeros(n, np.uint16)
        refstat = np.zeros(n, np.uint8)               # 0 no record, 1 REF==hg38 base, 2 REF!=hg38 base
        i0 = np.searchsorted(vp, pos, side='left')
        for k in range(4):
            j = i0 + k
            jj = np.minimum(j, len(vp) - 1) if len(vp) else j
            ok = (j < len(vp)) & (vp[jj] == pos) if len(vp) else np.zeros(n, bool)
            if not ok.any():
                break
            pany += np.where(ok, af[jj], 0)
            ismatch = ok & (alt[jj] == z['cb'])
            pc += np.where(ismatch, af[jj], 0)
            pcm = np.maximum(pcm, np.where(ismatch, pm[jj], 0).astype(np.uint16))
            rs = np.where(ok, np.where(ref[jj] == z['hb'], 1, 2), 0).astype(np.uint8)
            refstat = np.maximum(refstat, rs)
        mk = st['mask']
        inmask = np.zeros(n, np.uint8)
        if mk is not None:
            inmask = np.frombuffer(bytes(mk), np.uint8)[pos]
        np.savez_compressed(os.path.join(a.out, 'snvaf_%s.npz' % c), pc=pc, pany=pany, pcm=pcm, refstat=refstat, inmask=inmask)
        # indels
        zi = os.path.join(a.sites, 'indel_%s.npz' % c)
        if os.path.exists(zi) and st['ind']['d']:
            e = np.load(zi)
            tS = e['tS'].astype(np.int64)
            tSz = e['tSz'].astype(np.int64)
            qSz = e['qSz'].astype(np.int64)
            d = qSz - tSz
            vpos = np.array(st['ind']['pos'], np.int64)
            vd = np.array(st['ind']['d'], np.int64)
            vaf = np.array(st['ind']['af'], np.float32)
            vpm = np.array(st['ind']['pm'], np.float32)
            keep = np.abs(vd) < KEYSHIFT
            key = ((vd[keep] + KEYSHIFT) << 32) + vpos[keep]
            o = np.lexsort((vaf[keep], key))
            key = key[o]
            af_ = vaf[keep][o]
            last = np.r_[key[1:] != key[:-1], True]
            keys, afs = key[last], af_[last]
            res = {'tS': tS.astype(np.int32), 'tSz': tSz.astype(np.int32), 'qSz': qSz.astype(np.int32), 'pol': e['pol']}
            res['obs'] = match_indels(tS, d, keys, afs, 0, WINDOWS)
            for si, sh in enumerate(NULL_SHIFTS):
                res['null%d' % si] = match_indels(tS, d, keys, afs, sh, WINDOWS)
            res['inmask'] = (np.frombuffer(bytes(mk), np.uint8)[np.minimum(tS, len(mk) - 1)] if mk is not None else np.zeros(len(tS), np.uint8))
            np.savez_compressed(os.path.join(a.out, 'indelaf_%s.npz' % c), **res)
        # SVs (NYGC only)
        if st['sv']:
            sv_match(a, st, c)
        print('finished', c, 'snv records', len(vp), 'sites', n, flush=True)

    def sv_match(a, st, c):
        zi = os.path.join(a.sites, 'indel_%s.npz' % c)
        if not os.path.exists(zi):
            return
        e = np.load(zi)
        tS = e['tS'].astype(np.int64)
        tSz = e['tSz'].astype(np.int64)
        qSz = e['qSz'].astype(np.int64)
        sel = np.flatnonzero(np.maximum(tSz, qSz) >= 50)
        recs = sorted(st['sv'])                       # (pos, end, svlen, type, af)
        rp = np.array([r[0] for r in recs], np.int64)
        out = np.full((3, len(sel)), -1.0, np.float32)
        for vi, shift in enumerate((0,) + NULL_SHIFTS):
            for k, ei in enumerate(sel):
                s0 = int(tS[ei]) + shift
                L_t, L_q = int(tSz[ei]), int(qSz[ei])
                best = -1.0
                lo = np.searchsorted(rp, s0 - 100 - 2 * max(L_t, L_q), side='left')
                hi = np.searchsorted(rp, s0 + L_t + 100, side='right')
                for r in recs[lo:hi]:
                    pos, end, svlen, typ, af = r
                    if typ == 'DEL' and L_t > 0:
                        ov = min(end, s0 + L_t) - max(pos, s0)
                        if ov > 0 and ov >= 0.5 * max(end - pos, L_t):
                            best = max(best, af)
                    elif typ in ('INS', 'MEI') and L_q > 0 and L_t == 0:
                        if abs(pos - s0) <= 100 and 0.5 <= svlen / L_q <= 2:
                            best = max(best, af)
                out[vi, k] = best
        np.savez_compressed(os.path.join(a.out, 'sv_%s.npz' % c), sel=sel.astype(np.int32), tSz=tSz[sel].astype(np.int32),
                            qSz=qSz[sel].astype(np.int32), obs=out[0], null0=out[1], null1=out[2], pol=e['pol'][sel])

    bands_edges = list(BANDS[2:])
    nline = 0
    for line in proc.stdout:
        if line.startswith(b'#'):
            continue
        nline += 1
        f = line.split(b'\t', 8)
        cn = f[0].decode()
        c = cn if cn.startswith('chr') else 'chr' + cn
        if c != cur:
            finish(state)
            state = None
            cur = c
            if c in want and os.path.exists(os.path.join(a.sites, 'snv_%s.npz' % c)):
                state = new_state(c)
                print('reading', c, flush=True)
        if state is None:
            continue
        ref, alt = f[3], f[4]
        info = f[7]
        pos1 = int(f[1])
        if len(ref) == 1 and len(alt) == 1:
            mo1 = rx_ac.search(info)
            mo2 = rx_an.search(info)
            if not mo1 or not mo2:
                continue
            ac, an = int(mo1.group(1)), int(mo2.group(1))
            if an == 0:
                continue
            p = ac / an
            mk = state['mask']
            im = 1 if (mk is not None and mk[pos1 - 1]) else 0
            b = 0 if p <= 0 else bisect.bisect_right(bands_edges, p) + 1
            baseline['all'][im, b] += 1
            if state['site'][pos1 - 1] and ref in BASE_CODE and alt in BASE_CODE:
                pm = 0
                for k in popkeys:
                    v = info_get(info, k)
                    if v:
                        try:
                            pm = max(pm, int(round(float(v.split(b',')[0]) * 1000)))
                        except ValueError:
                            pass
                state['snv']['pos'].append(pos1 - 1)
                state['snv']['alt'].append(BASE_CODE[alt])
                state['snv']['ref'].append(BASE_CODE[ref])
                state['snv']['af'].append(p)
                state['snv']['pm'].append(pm)
        elif alt[:1] != b'<' and b',' not in alt and ref.isalpha() and alt.isalpha() and len(ref) != len(alt):
            mo1 = rx_ac.search(info)
            mo2 = rx_an.search(info)
            if not mo1 or not mo2 or int(mo2.group(1)) == 0:
                continue
            p = int(mo1.group(1)) / int(mo2.group(1))
            pm = 0
            for k in popkeys:
                v = info_get(info, k)
                if v:
                    try:
                        pm = max(pm, int(round(float(v.split(b',')[0]) * 1000)))
                    except ValueError:
                        pass
            state['ind']['pos'].append(pos1)
            state['ind']['d'].append(len(alt) - len(ref))
            state['ind']['af'].append(p)
            state['ind']['pm'].append(pm)
        elif alt[:1] == b'<' and fmt == 'nygc':
            sv = info_get(info, 'SVTYPE')
            if sv is None:
                continue
            sv = sv.decode()
            mo1 = rx_ac.search(info)
            mo2 = rx_an.search(info)
            en = info_get(info, 'END')
            sl = info_get(info, 'SVLEN')
            if not mo1 or not mo2 or int(mo2.group(1)) == 0 or en is None:
                continue
            typ = 'MEI' if b'INS:ME' in alt else sv
            if typ in ('DEL', 'INS', 'MEI'):
                state['sv'].append((pos1, int(en), abs(int(sl)) if sl else 0, typ, int(mo1.group(1)) / int(mo2.group(1))))
    finish(state)
    proc.wait()
    json.dump(dict(baseline_snv_records_by_band={'band_names': BAND_NAMES, 'outside_mask': baseline['all'][0].tolist(),
                                                  'inside_mask': baseline['all'][1].tolist()}, lines=nline, fmt=fmt,
                   vcf=os.path.basename(a.vcf)),
              open(os.path.join(a.out, 'baseline.json'), 'w'), indent=1)
    print('afq stage done: %d VCF lines' % nline)


# ----------------------------------------------------------------------------------------------- REPORT stage
def pct(x, n):
    return 100.0 * x / n if n else float('nan')


def snv_table(pc, pany, pcm, sel, T=T_PRIMARY):
    n = int(sel.sum())
    if n == 0:
        return dict(n=0)
    p = pc[sel]
    band = np.where(p <= 0, 0, np.searchsorted(np.array(BANDS[2:]), p, side='right') + 1)
    bc = np.bincount(band, minlength=len(BAND_NAMES))
    out = dict(n=n, bands=bc.tolist(), poly_T=float((p >= T).sum()) / n, poly_T001=float((p >= 0.001).sum()) / n,
               poly_T005=float((p >= 0.05).sum()) / n, seen_any=float((p > 0).sum()) / n,
               any_pop_T=float((pcm[sel] >= 5).sum()) / n,
               hg38_not_fixed_T=float((pany[sel] >= T).sum()) / n)
    return out


def report_stage(a):
    import glob
    res = {}
    snvs = {}
    chs = a.chroms.split(',') if a.chroms else PRIMARY_T
    for c in chs:
        zs = os.path.join(a.sites, 'snv_%s.npz' % c)
        za = os.path.join(a.af, 'snvaf_%s.npz' % c)
        if os.path.exists(zs) and os.path.exists(za):
            snvs[c] = (np.load(zs), np.load(za))
    covered = sorted(snvs)
    cat = {k: np.concatenate([snvs[c][0][k] for c in covered]) for k in ('hb', 'cb', 'gb', 'fl')}
    caf = {k: np.concatenate([snvs[c][1][k] for c in covered]) for k in ('pc', 'pany', 'pcm', 'refstat', 'inmask')}
    chrom_of = np.concatenate([np.full(len(snvs[c][0]['hb']), i, np.int16) for i, c in enumerate(covered)])
    n_all = len(cat['hb'])
    hb, cb, gb, fl = cat['hb'], cat['cb'], cat['gb'], cat['fl']
    polcls = np.full(n_all, 3, np.int8)                     # 0 H, 1 C, 2 third, 3 unpolarized
    polcls[(gb < 4) & (gb != cb) & (gb != hb)] = 2
    polcls[(gb < 4) & (gb == hb)] = 1
    polcls[(gb < 4) & (gb == cb)] = 0
    inm = caf['inmask'] == 1
    res['covered_chroms'] = covered
    res['n_snv_covered'] = n_all
    res['polarization_counts'] = {n: int((polcls == i).sum()) for i, n in enumerate(['H', 'C', 'third', 'unpol'])}
    groups = {
        'all sites': np.ones(n_all, bool),
        'in strict mask': inm,
        'outside mask': ~inm,
        'H-derived, in mask': (polcls == 0) & inm,
        'H-derived, all': polcls == 0,
        'C-derived, in mask': (polcls == 1) & inm,
        'C-derived, all': polcls == 1,
        'third, in mask': (polcls == 2) & inm,
        'unpolarized, in mask': (polcls == 3) & inm,
        'top-level fills, in mask': ((fl & FL_TOP) > 0) & inm,
        'records <2% div, in mask': ((fl & FL_LT2) > 0) & inm,
        'H-derived, top-level, in mask': (polcls == 0) & ((fl & FL_TOP) > 0) & inm,
        'H-derived, CpG, in mask': (polcls == 0) & ((fl & FL_CPG) > 0) & inm,
        'H-derived, non-CpG, in mask': (polcls == 0) & ((fl & FL_CPG) == 0) & inm,
        'H-derived, transitions, in mask': (polcls == 0) & ((fl & FL_TS) > 0) & inm,
        'H-derived, transversions, in mask': (polcls == 0) & ((fl & FL_TS) == 0) & inm,
        'H-derived, lowercase (repeat), in mask': (polcls == 0) & ((fl & FL_REP) > 0) & inm,
        'H-derived, not lowercase, in mask': (polcls == 0) & ((fl & FL_REP) == 0) & inm,
        'H-derived, near gap, in mask': (polcls == 0) & ((fl & FL_NEAR) > 0) & inm,
    }
    res['snv'] = {k: snv_table(caf['pc'], caf['pany'], caf['pcm'], v) for k, v in groups.items()}
    # thresholds on the central group
    sel = (polcls == 0) & inm
    res['sH_thresholds'] = {str(T): float((caf['pc'][sel] >= T).mean()) for T in (0.001, 0.005, 0.01, 0.02, 0.05, 0.1)}
    # per chromosome s_H
    per = {}
    for i, c in enumerate(covered):
        s = sel & (chrom_of == i)
        if s.sum():
            per[c] = float((caf['pc'][s] >= T_PRIMARY).mean())
    res['sH_per_chrom'] = per
    # REF agreement of matched records
    matched = caf['refstat'] > 0
    res['ref_agreement'] = dict(matched=int(matched.sum()), ref_eq_hg38=int((caf['refstat'] == 1).sum()),
                                ref_ne_hg38=int((caf['refstat'] == 2).sum()))
    # SNV null: genome-wide chance that a mask site is polymorphic (baseline.json)
    bj = os.path.join(a.af, 'baseline.json')
    if os.path.exists(bj):
        res['baseline'] = json.load(open(bj))
    # indels
    ind = defaultdict(list)
    for c in chs:
        zi = os.path.join(a.af, 'indelaf_%s.npz' % c)
        if os.path.exists(zi):
            z = np.load(zi)
            for k in z.files:
                ind[k].append(z[k])
    if ind:
        I = {k: np.concatenate(v, axis=-1) for k, v in ind.items()}
        n = I['tSz'].shape[0]
        kind = np.where(I['qSz'] == 0, 0, np.where(I['tSz'] == 0, 1, 2))
        size = np.maximum(I['tSz'], I['qSz'])
        sizec = np.searchsorted(np.array([2, 11, 51, 1001]), size, side='right')
        res['indel'] = {}
        groups_i = {'all events': np.ones(n, bool), 'human lineage (pol 1)': I['pol'] == 1, 'chimp lineage (pol 2)': I['pol'] == 2,
                    'unpolarized': I['pol'] == 0, 'human-only bases': kind == 0, 'chimp-only bases': kind == 1, 'both-sided': kind == 2,
                    'size 1': sizec == 0, 'size 2-10': sizec == 1, 'size 11-50': sizec == 2, 'size 51-1000': sizec == 3, 'size >1000': sizec == 4,
                    'in mask, all': I['inmask'] == 1,
                    'human lineage, in mask': (I['pol'] == 1) & (I['inmask'] == 1),
                    'human lineage, size 1': (I['pol'] == 1) & (sizec == 0), 'human lineage, size 2-10': (I['pol'] == 1) & (sizec == 1),
                    'human lineage, size 11-50': (I['pol'] == 1) & (sizec == 2)}
        for gname, sel in groups_i.items():
            nn = int(sel.sum())
            row = dict(n=nn)
            for wi, w in enumerate(WINDOWS):
                for T in (T_PRIMARY, 0.001):
                    ob = float((I['obs'][wi][sel] >= T).mean()) if nn else float('nan')
                    nu = [float((I['null%d' % s][wi][sel] >= T).mean()) if nn else float('nan') for s in range(len(NULL_SHIFTS))]
                    row['w%d_T%g' % (w, T)] = dict(obs=ob, null=float(np.mean(nu)), net=ob - float(np.mean(nu)))
                row['w%d_seen' % w] = dict(obs=float((I['obs'][wi][sel] >= 0).mean()) if nn else float('nan'),
                                           null=float(np.mean([(I['null%d' % s][wi][sel] >= 0).mean() for s in range(len(NULL_SHIFTS))])) if nn else float('nan'))
            res['indel'][gname] = row
        res['indel_total'] = n
    # SV sample
    svs = []
    for c in chs:
        zv = os.path.join(a.af, 'sv_%s.npz' % c)
        if os.path.exists(zv):
            svs.append(np.load(zv))
    if svs:
        S = {k: np.concatenate([z[k] for z in svs]) for k in ('tSz', 'qSz', 'obs', 'null0', 'null1', 'pol')}
        kind = np.where(S['qSz'] == 0, 0, np.where(S['tSz'] == 0, 1, 2))
        row = {}
        for nm, sel in {'all >=50 bp': np.ones(len(kind), bool), 'human-only': kind == 0, 'chimp-only': kind == 1, 'both': kind == 2}.items():
            nn = int(sel.sum())
            row[nm] = dict(n=nn, obs=float((S['obs'][sel] >= T_PRIMARY).mean()) if nn else float('nan'),
                           null=float(np.mean([(S['null%d' % s][sel] >= T_PRIMARY).mean() for s in (0, 1)])) if nn else float('nan'),
                           seen_obs=float((S['obs'][sel] >= 0).mean()) if nn else float('nan'))
        res['sv'] = row
    # corrected ratio (needs full coverage of the 24 chromosomes only for the totals, which come from GAP-07b)
    N_SNV, N_IND, N_OTHER, DAY = 37767396, 4301652, 32045 + 1421, 205e6
    sH = res['snv']['H-derived, in mask']['poly_T']
    sall = res['snv']['in strict mask']['poly_T']
    sall_sites = res['snv']['all sites']['poly_T']
    sC_h = res['snv']['C-derived, in mask']['poly_T']
    sind = None
    if 'indel' in res:
        r = res['indel']['human lineage, in mask']['w2_T0.01']
        sind = (r['net'], r['obs'])
    res['inputs'] = dict(s_H=sH, s_all_in_mask=sall, s_all_sites=sall_sites, s_C_human_panel=sC_h, s_indel_net_obs=sind)
    cor = {}

    def fixed(s_snv, s_ind):
        tot = N_SNV * (1 - s_snv) + N_IND * (1 - s_ind) + N_OTHER
        return tot / 2.0

    s_ind_central = sind[0] if sind else 0.0
    for nm, (ss, si) in {
        'raw (GAP-07b)': (0.0, 0.0),
        '(a) human data only, SNV pooled in-mask share; indel share = measured': (sall, s_ind_central),
        '(a) same, SNV pooled over all sites (floor)': (sall_sites, s_ind_central),
        '(b) symmetric s_C = s_H, SNV; indel measured net': (sH, s_ind_central),
        '(b) symmetric, SNV only (indels fixed)': (sH, 0.0),
        '(b) symmetric, SNV share also applied to indels': (sH, sH),
        '(c) chimp share = 2 x human: SNV (s_H + 2 s_H)/2': ((sH + 2 * sH) / 2, (s_ind_central + 2 * s_ind_central) / 2),
        '(b) symmetric with T = 0.001': (res['sH_thresholds']['0.001'], s_ind_central),
        '(b) symmetric with T = 0.05': (res['sH_thresholds']['0.05'], s_ind_central),
    }.items():
        fx = fixed(ss, si)
        cor[nm] = dict(s_snv=ss, s_ind=si, fixed_per_lineage=fx, ratio=DAY / fx)
    # per-lineage: human lineage (H-derived + half of unpol/third) and chimp lineage (symmetric)
    nH = res['polarization_counts']['H']
    nC = res['polarization_counts']['C']
    nO = res['polarization_counts']['third'] + res['polarization_counts']['unpol']
    tot = nH + nC + nO
    # scale polarization counts to the full 37.77 M if only part covered
    scale = N_SNV / tot if tot else 0
    hum_fixed = (nH + nO / 2.0) * scale * (1 - sH)
    chi_fixed_sym = (nC + nO / 2.0) * scale * (1 - sH)
    chi_fixed_hum_only = (nC + nO / 2.0) * scale * (1 - sC_h)
    res['lineages_snv'] = dict(human_events=(nH + nO / 2.0) * scale, chimp_events=(nC + nO / 2.0) * scale,
                               human_fixed=hum_fixed, chimp_fixed_symmetric=chi_fixed_sym,
                               chimp_fixed_if_human_panel_share=chi_fixed_hum_only)
    res['corrected'] = cor
    json.dump(res, open(a.out, 'w'), indent=1, default=float)
    # text report
    L = []
    L.append('covered chromosomes: %s' % ' '.join(covered))
    L.append('SNV sites covered: %d  polarization %s' % (n_all, res['polarization_counts']))
    L.append('REF agreement of matched records: %s' % res['ref_agreement'])
    L.append('')
    L.append('SNV: share with chimp-matching allele frequency >= 0.01 (poly_T), bands, etc.')
    for k, v in res['snv'].items():
        if v['n']:
            L.append('  %-42s n=%10d poly(>=.01)=%6.2f%%  >=.001=%6.2f%% >=.05=%6.2f%% seen=%6.2f%% anypop=%6.2f%% hg38notfixed=%6.2f%%'
                     % (k, v['n'], 100 * v['poly_T'], 100 * v['poly_T001'], 100 * v['poly_T005'], 100 * v['seen_any'], 100 * v['any_pop_T'],
                        100 * v['hg38_not_fixed_T']))
    L.append('  bands (%s):' % ', '.join(BAND_NAMES))
    for k in ('all sites', 'in strict mask', 'H-derived, in mask', 'C-derived, in mask'):
        v = res['snv'][k]
        L.append('    %-30s %s' % (k, ' '.join('%5.2f%%' % (100.0 * x / v['n']) for x in v['bands'])))
    L.append('s_H thresholds: %s' % res['sH_thresholds'])
    L.append('s_H per chromosome: %s' % {c: round(100 * x, 1) for c, x in per.items()})
    if 'indel' in res:
        L.append('')
        L.append('INDELS (events %d): share with matched record AF >= 0.01; obs / null / net' % res['indel_total'])
        for k, v in res['indel'].items():
            s = ' '.join('w%d: %5.2f/%5.2f/%5.2f%%' % (w, 100 * v['w%d_T0.01' % w]['obs'], 100 * v['w%d_T0.01' % w]['null'], 100 * v['w%d_T0.01' % w]['net']) for w in WINDOWS) if v['n'] else ''
            L.append('  %-30s n=%9d  %s' % (k, v['n'], s))
    if 'sv' in res:
        L.append('')
        L.append('SV >=50 bp (NYGC sample): %s' % json.dumps(res['sv']))
    L.append('')
    L.append('LINEAGES (SNV): %s' % json.dumps(res['lineages_snv']))
    L.append('CORRECTED RATIO (Day 205 M / fixed events per lineage):')
    for k, v in cor.items():
        L.append('  %-70s s_snv=%6.2f%% s_ind=%6.2f%% fixed/lineage=%7.3fM ratio=%6.2f' % (k, 100 * v['s_snv'], 100 * v['s_ind'], v['fixed_per_lineage'] / 1e6, v['ratio']))
    open(a.out.replace('.json', '.out'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    s = sp.add_parser('sites')
    s.add_argument('--axt'); s.add_argument('--t-sizes'); s.add_argument('--gor-work'); s.add_argument('--net')
    s.add_argument('--events'); s.add_argument('--out')
    q = sp.add_parser('afq')
    q.add_argument('--vcf'); q.add_argument('--fmt', choices=['p3', 'nygc']); q.add_argument('--sites'); q.add_argument('--mask')
    q.add_argument('--t-sizes'); q.add_argument('--out'); q.add_argument('--chroms', default='')
    r = sp.add_parser('report')
    r.add_argument('--sites'); r.add_argument('--af'); r.add_argument('--out'); r.add_argument('--chroms', default='')
    a = ap.parse_args()
    {'sites': sites_stage, 'afq': afq_stage, 'report': report_stage}[a.cmd](a)


if __name__ == '__main__':
    main()
