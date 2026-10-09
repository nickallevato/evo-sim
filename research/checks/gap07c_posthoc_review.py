"""GAP-07c POST HOC 2 (review fix pass; NOT pre-registered; every number from this script is labelled [PH]).
Written after the main run of gap07c_polymorphic_share.py and after the two reviews (REVIEW-R4-GAP07c-correctness.md,
REVIEW-R4-GAP07c-steelman.md); committed before it is run. It computes what the reviews asked for:

 1. Indel lineage split with GAP-07b's SYMMETRIC post hoc polarization rule (gap07b_posthoc_polarize.polar, windows
    w = 2/5/10/20, events <= 50 bp), replacing the as-run (withdrawn) rule that the main script copied (Corr-M1).
 2. SV share (NYGC chr21+22) by lineage, size and with 95% Wilson intervals (Corr-M2).
 3. Indel chance-match controls (sign-flipped net length, net length +-1, shifted position) genome-wide (Corr-m6).
    Stage 'ctl' runs on the workhorse (streams the phase-3 VCF); stage 'report' runs locally.
 4. A bracket table of corrected ratios with and without the chimp-side assumption: raw; (a) pooled human data only
    with the consistent pooled indel share (Corr-m1/GD-5); human lineage alone with the check's own conventions
    (Corr-m3/GC-3); chimp share 0.5x (GD-1); symmetric; symmetric with third/unpolarized measured shares (Corr-m7);
    thresholds 0.1%, 5%, 10% (Day's Q55 operational "fixed" cut) and "seen at all" with the INDEL share varied at the same
    threshold (GD-3, GC-1, Corr-m7iii); chimp share 2x; top-level fills; the measured counterpart of GAP-07b's combined
    critic rows (<2%-divergent records) (GC-3); each also with the SNV part of Day's 205 M numerator corrected for
    polymorphism by the same SNV share (GD-2).
 5. Like-for-like SNV-only comparison with Day's 17.5 M and the shortfall scaling on both bases (GC-4).
 6. Pre-registration slips: Q9 (c) (Corr-m2) recomputed: registered point 15.2 M / 13.5 corresponds to 2x on all events;
    the (c) as defined and coded is 1.5x s_H.

Conventions are those of the main report: autosomes chr1-22; SNV shares from the strict mask; indel share =
human-lineage, strict mask, matched record at AF >= T within +-2 bp, net of the +-10 kb shifted null; shares applied to
all 37,767,396 SNVs and 4,301,652 indel events; 33,466 other events (nested fills, unaligned segments) counted fixed;
per lineage = total / 2; numerator 205 M.
Run: research/.venv/bin/python -I research/checks/gap07c_posthoc_review.py ctl --vcf V --sites S --mask M --t-sizes Z --out D
     research/.venv/bin/python -I research/checks/gap07c_posthoc_review.py report --sites S --af A --nygc N --gor G
         --ctl D --toplevel T.json --out OUT.json
"""
import argparse
import bisect
import json
import math
import os
import re
import subprocess

import numpy as np

CH = ['chr%d' % i for i in range(1, 23)]
KEYSHIFT = 1 << 21
N_SNV, N_IND, N_OTHER, DAY, DAY_SNV = 37767396, 4301652, 32045 + 1421, 205e6, 17.5e6
FL_LT2, FL_TOP = 4, 32


# ------------------------------------------------------------------------------------------------ polarization
def polar(tS, tSz, qSz, gb, gi, w):
    """verbatim copy of gap07b_posthoc_polarize.polar (symmetric window rule)"""
    n = len(gb)
    pol = np.zeros(len(tS), np.int8)
    m = (tSz > 0) & (qSz == 0)
    if m.any():
        cs5 = np.concatenate(([0], np.cumsum(gb == 5, dtype=np.int32)))
        p = tS[m]
        L = tSz[m]
        a = np.clip(p - w, 0, n)
        b = np.clip(p + L + w, 0, n)
        D = cs5[b] - cs5[a]
        fl = (gb[np.clip(a - 1, 0, n - 1)] < 4) & (gb[np.clip(b, 0, n - 1)] < 4)
        r = np.zeros(len(p), np.int8)
        r[(D >= 0.5 * L) & (D <= 2 * L + w)] = 1
        r[(D == 0) & fl] = 2
        pol[m] = r
    m = (tSz == 0) & (qSz > 0)
    if m.any():
        csi = np.concatenate(([0], np.cumsum(gi, dtype=np.int32)))
        p = tS[m]
        L = qSz[m]
        a = np.clip(p - w, 0, n)
        b = np.clip(p + w + 1, 0, n)
        I = csi[b] - csi[a]
        fl = (gb[np.clip(p - w - 1, 0, n - 1)] < 4) & (gb[np.clip(p + w + 1, 0, n - 1)] < 4)
        r = np.zeros(len(p), np.int8)
        r[(I >= np.maximum(1, 0.5 * L)) & (I <= 2 * L + w)] = 1
        r[(I == 0) & fl] = 2
        pol[m] = r
    return pol


# ------------------------------------------------------------------------------------------------ ctl stage (workhorse)
def match_w(ev_pos, ev_d, keys, afs, shift, w):
    n = len(ev_pos)
    best = np.full(n, -1.0, np.float32)
    ok = np.abs(ev_d) < KEYSHIFT
    base = ((ev_d.astype(np.int64) + KEYSHIFT) << 32)
    for off in range(-w, w + 1):
        q = base + (ev_pos.astype(np.int64) + shift + off)
        i = np.minimum(np.searchsorted(keys, q), len(keys) - 1)
        hit = ok & (keys[i] == q)
        best = np.maximum(best, np.where(hit, afs[i], -1.0).astype(np.float32))
    return best


def ctl_stage(a):
    os.makedirs(a.out, exist_ok=True)
    rx_ac = re.compile(rb'(?:^|;)AC=(\d+)')
    rx_an = re.compile(rb'(?:^|;)AN=(\d+)')
    ind = {}
    cur = None
    proc = subprocess.Popen(['gzip', '-dc', a.vcf], stdout=subprocess.PIPE, bufsize=1 << 24)

    def finish(c, rec):
        zi = os.path.join(a.sites, 'indel_%s.npz' % c)
        if not os.path.exists(zi) or not rec['d']:
            return
        e = np.load(zi)
        tS = e['tS'].astype(np.int64)
        d = e['qSz'].astype(np.int64) - e['tSz'].astype(np.int64)
        vpos = np.array(rec['pos'], np.int64)
        vd = np.array(rec['d'], np.int64)
        vaf = np.array(rec['af'], np.float32)
        keep = np.abs(vd) < KEYSHIFT
        key = ((vd[keep] + KEYSHIFT) << 32) + vpos[keep]
        o = np.lexsort((vaf[keep], key))
        key = key[o]
        af_ = vaf[keep][o]
        last = np.r_[key[1:] != key[:-1], True]
        keys, afs = key[last], af_[last]
        out = dict(obs=match_w(tS, d, keys, afs, 0, 2), negd=match_w(tS, -d, keys, afs, 0, 2),
                   dp1=match_w(tS, d + 1, keys, afs, 0, 2), dm1=match_w(tS, d - 1, keys, afs, 0, 2),
                   null_p=match_w(tS, d, keys, afs, 10000, 2), null_m=match_w(tS, d, keys, afs, -10000, 2),
                   null_p2=match_w(tS, d, keys, afs, 20000, 2), null_m2=match_w(tS, d, keys, afs, -20000, 2))
        np.savez_compressed(os.path.join(a.out, 'ctl_%s.npz' % c), **out)
        print('ctl finished', c, len(tS), flush=True)

    rec = None
    for line in proc.stdout:
        if line.startswith(b'#'):
            continue
        f = line.split(b'\t', 8)
        c = 'chr' + f[0].decode()
        if c != cur:
            if cur is not None and rec is not None:
                finish(cur, rec)
            cur = c
            rec = {'pos': [], 'd': [], 'af': []} if c in CH else None
        if rec is None:
            continue
        ref, alt = f[3], f[4]
        if len(ref) == len(alt) or b',' in alt or alt[:1] == b'<' or not (ref.isalpha() and alt.isalpha()):
            continue
        m1, m2 = rx_ac.search(f[7]), rx_an.search(f[7])
        if not m1 or not m2 or int(m2.group(1)) == 0:
            continue
        rec['pos'].append(int(f[1]))
        rec['d'].append(len(alt) - len(ref))
        rec['af'].append(int(m1.group(1)) / int(m2.group(1)))
    if cur is not None and rec is not None:
        finish(cur, rec)
    proc.wait()
    print('ctl stage done')


# ------------------------------------------------------------------------------------------------ report stage
def wilson(k, n, z=1.96):
    if n == 0:
        return (float('nan'), float('nan'))
    p = k / n
    den = 1 + z * z / n
    ctr = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (ctr - h, ctr + h)


def fixed_events(s_snv, s_ind):
    return (N_SNV * (1 - s_snv) + N_IND * (1 - s_ind) + N_OTHER) / 2.0


def row(name, s_snv, s_ind, assumes, extra=None, fixed=None):
    fx = fixed if fixed is not None else fixed_events(s_snv, s_ind)
    d = dict(name=name, s_snv=s_snv, s_ind=s_ind, chimp_assumption=assumes, fixed_per_lineage=fx, ratio=DAY / fx,
             ratio_numerator_corrected=(DAY - DAY_SNV * s_snv) / fx)
    if extra:
        d.update(extra)
    return d


def report_stage(a):
    res = {}
    # ---- SNV arrays
    S = {k: [] for k in ('hb', 'cb', 'gb', 'fl', 'pc', 'inmask')}
    for c in CH:
        z = np.load('%s/snv_%s.npz' % (a.sites, c))
        q = np.load('%s/snvaf_%s.npz' % (a.af, c))
        for k in ('hb', 'cb', 'gb', 'fl'):
            S[k].append(z[k])
        S['pc'].append(q['pc'])
        S['inmask'].append(q['inmask'])
    S = {k: np.concatenate(v) for k, v in S.items()}
    hb, cb, gb, fl, pc, inm = S['hb'], S['cb'], S['gb'], S['fl'], S['pc'], S['inmask'] == 1
    pol = np.full(len(hb), 3, np.int8)
    pol[(gb < 4) & (gb != cb) & (gb != hb)] = 2
    pol[(gb < 4) & (gb == hb)] = 1
    pol[(gb < 4) & (gb == cb)] = 0
    cnt = {n: int((pol == i).sum()) for i, n in enumerate(['H', 'C', 'third', 'unpol'])}
    tot_aut = len(hb)
    scale = N_SNV / tot_aut
    TH = {'0.001': 0.001, '0.01': 0.01, '0.05': 0.05, '0.10': 0.10}

    def share(sel, T):
        if T == 'seen':
            return float((pc[sel] > 0).mean())
        return float((pc[sel] >= TH[T]).mean())
    Ts = ['0.001', '0.01', '0.05', '0.10', 'seen']
    sH = {T: share((pol == 0) & inm, T) for T in Ts}
    sP = {T: share(inm, T) for T in Ts}
    s3 = {T: share((pol == 2) & inm, T) for T in Ts}
    su = {T: share((pol == 3) & inm, T) for T in Ts}
    sH_lt2 = share((pol == 0) & inm & ((fl & FL_LT2) > 0), '0.01')
    res['snv'] = dict(counts=cnt, sH=sH, s_pooled=sP, s_third=s3, s_unpol=su, sH_lt2=sH_lt2,
                      sH_all_sites=float((pc[pol == 0] >= 0.01).mean()))
    # ---- indel arrays with the symmetric polarization
    I = {k: [] for k in ('tSz', 'qSz', 'obs', 'n0', 'n1', 'inmask', 'chrom')}
    pols = {w: [] for w in (2, 5, 10, 20)}
    ctl = {k: [] for k in ('negd', 'dp1', 'dm1', 'null_p', 'null_m', 'null_p2', 'null_m2')}
    have_ctl = a.ctl and os.path.isdir(a.ctl)
    for ci, c in enumerate(CH):
        z = np.load('%s/indelaf_%s.npz' % (a.af, c))
        g = np.load('%s/gor_%s.npz' % (a.gor, c))
        gb_, gi_ = g['gbase'], g['gins']
        tS, tSz, qSz = z['tS'].astype(np.int64), z['tSz'].astype(np.int64), z['qSz'].astype(np.int64)
        for w in pols:
            pols[w].append(polar(tS, tSz, qSz, gb_, gi_, w))
        I['tSz'].append(tSz)
        I['qSz'].append(qSz)
        I['obs'].append(z['obs'][1])
        I['n0'].append(z['null0'][1])
        I['n1'].append(z['null1'][1])
        I['inmask'].append(z['inmask'])
        I['chrom'].append(np.full(len(tS), ci, np.int8))
        if have_ctl:
            zc = np.load('%s/ctl_%s.npz' % (a.ctl, c))
            for k in ctl:
                ctl[k].append(zc[k])
    I = {k: np.concatenate(v) for k, v in I.items()}
    pols = {w: np.concatenate(v) for w, v in pols.items()}
    if have_ctl:
        ctl = {k: np.concatenate(v) for k, v in ctl.items()}
    size = np.maximum(I['tSz'], I['qSz'])
    small = size <= 50
    im = I['inmask'] == 1
    n_ev = len(size)
    res['indel_n'] = n_ev

    def ishare(sel, T, arr=None):
        o = I['obs'] if arr is None else arr
        if T == 'seen':
            f = lambda x: float((x[sel] >= 0).mean())
        else:
            f = lambda x: float((x[sel] >= TH[T]).mean())
        ob = f(o)
        nu = 0.5 * (f(I['n0']) + f(I['n1']))
        return dict(obs=ob, null=nu, net=ob - nu)
    res['indel_polarization'] = {}
    for w, p in pols.items():
        d = {}
        for lab, sel0 in (('all sites', np.ones(n_ev, bool)), ('in mask', im)):
            h = (p == 1) & small & sel0
            ch = (p == 2) & small & sel0
            d[lab] = dict(n_human=int(h.sum()), n_chimp=int(ch.sum()),
                          human_share_of_polarized=float(((p == 1) & small).sum() / max(1, ((p == 1) & small).sum() + ((p == 2) & small).sum())),
                          human=ishare(h, '0.01'), chimp=ishare(ch, '0.01'))
        res['indel_polarization']['w%d' % w] = d
    P5 = pols[5]
    cen = (P5 == 1) & small & im
    sInd = {T: ishare(cen, T)['net'] for T in Ts}
    sInd_all = {T: ishare((P5 == 1) & small, T)['net'] for T in Ts}
    sIndPool = {T: ishare(im, T)['net'] for T in Ts}
    res['indel_shares'] = dict(human_lineage_inmask_w5=sInd, human_lineage_allsites_w5=sInd_all, pooled_inmask=sIndPool,
                               range_over_w_allsites={w: res['indel_polarization']['w%d' % w]['all sites']['human']['net'] for w in pols},
                               range_over_w_inmask={w: res['indel_polarization']['w%d' % w]['in mask']['human']['net'] for w in pols})
    # size classes within the human lineage (w=5, in mask)
    sz_cls = {'1': size == 1, '2-10': (size >= 2) & (size <= 10), '11-50': (size >= 11) & (size <= 50)}
    res['indel_by_size_human_w5_inmask'] = {k: dict(n=int((cen & v).sum()), **ishare(cen & v, '0.01')) for k, v in sz_cls.items()}
    # ---- controls
    if have_ctl:
        out = {}
        for lab, sel in (('human lineage, <=50 bp, all sites', (P5 == 1) & small), ('human lineage, in mask', cen),
                         ('chimp lineage, <=50 bp', (P5 == 2) & small), ('all <=50 bp', small),
                         ('human lineage, size 1', (P5 == 1) & (size == 1))):
            r = dict(n=int(sel.sum()), same_d=float((I['obs'][sel] >= 0.01).mean()))
            for k in ctl:
                r[k] = float((ctl[k][sel] >= 0.01).mean())
            out[lab] = r
        res['indel_controls'] = out
    # ---- SV
    sv = {k: [] for k in ('tSz', 'qSz', 'obs', 'null0', 'null1', 'pol')}
    for c in ('chr21', 'chr22'):
        z = np.load('%s/sv_%s.npz' % (a.nygc, c))
        for k in sv:
            sv[k].append(z[k])
    sv = {k: np.concatenate(v) for k, v in sv.items()}
    ssz = np.maximum(sv['tSz'], sv['qSz'])
    svr = {}
    for lab, sel in (('all', np.ones(len(ssz), bool)), ('human lineage (as-run pol)', sv['pol'] == 1), ('chimp lineage', sv['pol'] == 2),
                     ('unpolarized', sv['pol'] == 0), ('human 50-100', (sv['pol'] == 1) & (ssz < 100)),
                     ('human 100-1000', (sv['pol'] == 1) & (ssz >= 100) & (ssz < 1000)), ('human >=1000', (sv['pol'] == 1) & (ssz >= 1000))):
        n = int(sel.sum())
        k = int((sv['obs'][sel] >= 0.01).sum())
        nu = 0.5 * float(((sv['null0'][sel] >= 0.01).mean() + (sv['null1'][sel] >= 0.01).mean())) if n else float('nan')
        lo, hi = wilson(k, n)
        svr[lab] = dict(n=n, k=k, obs=k / n if n else None, null=nu, net=(k / n - nu) if n else None, ci95=[lo, hi])
    res['sv'] = svr
    # ---- bracket rows
    rows = []
    sPoolS, sPoolI = sP['0.01'], sIndPool['0.01']
    sHc, sIc = sH['0.01'], sInd['0.01']
    rows.append(row('raw count (GAP-07b)', 0.0, 0.0, 'none (no correction)'))
    rows.append(row('(a) human data only: pooled SNV share, pooled indel share (in mask)', sPoolS, sPoolI, 'no (human data only; chimp credited with nothing)'))
    # human lineage alone
    nH = cnt['H'] + 0.5 * (cnt['third'] + cnt['unpol'])
    snv_h = nH * scale
    n1 = int(((P5 == 1) & small).sum())
    n2 = int(((P5 == 2) & small).sum())
    rest = n_ev - n1 - n2
    ind_h = (n1 + 0.5 * rest) * (N_IND / n_ev)
    ev_h = snv_h + ind_h + N_OTHER / 2.0
    fx_h = snv_h * (1 - sHc) + ind_h * (1 - sIc) + N_OTHER / 2.0
    rows.append(row('human lineage alone, own conventions (SNV H + half of unpolarized/third; indel human + half of unpolarized, symmetric rule w=5)', sHc, sIc,
                    'no (human lineage; no chimp assumption)', dict(events_human_lineage=ev_h, ratio_raw_same_conventions=DAY / ev_h,
                                                                     snv_h=snv_h, ind_h=ind_h), fixed=fx_h))
    rows.append(row('chimp share 0.5x human', 0.75 * sHc, 0.75 * sIc, 'YES (chimp = 0.5 x human)'))
    rows.append(row('(b) symmetric: chimp share = human share', sHc, sIc, 'YES (chimp = human)'))
    # third/unpol measured
    s_mix = (cnt['H'] * sHc + cnt['C'] * sHc + cnt['third'] * s3['0.01'] + cnt['unpol'] * su['0.01']) / tot_aut
    rows.append(row('(b) with measured third / unpolarized shares (6.3% / 8.6%)', s_mix, sIc, 'YES'))
    for T, lab in (('0.001', 'AF >= 0.1%'), ('0.05', 'AF >= 5%'), ('0.10', "AF >= 10% (Day's operational 'fixed' > 90%, Q55)"), ('seen', 'seen at any frequency')):
        rows.append(row('(b) symmetric at %s, indel share at the same threshold' % lab, sH[T], sInd[T], 'YES',
                        dict(threshold=T)))
    rows.append(row('(c) chimp share 2x human', 1.5 * sHc, 1.5 * sIc, 'YES (chimp = 2 x human)'))
    rows.append(row('(c) as pre-registered point: 2 x s_H on all events', 2 * sHc, 2 * sIc, 'YES'))
    # top-level
    tj = json.load(open(a.toplevel))
    s_top = tj['top & H & mask']['poly_T01']
    fx_top = (35017058 * (1 - s_top) + N_IND * (1 - sIc) + N_OTHER) / 2.0
    rows.append(row('(b) top-level fills only (35,017,058 SNVs)', s_top, sIc, 'YES', fixed=fx_top))
    # GAP-07b combined critic rows measured counterpart
    fx_c1 = (33765842 * (1 - sH_lt2) + N_IND + N_OTHER) / 2.0
    fx_c2 = (33765842 * (1 - sH_lt2) + N_IND * (1 - sIc) + N_OTHER) / 2.0
    rows.append(row('measured counterpart of the GAP-07b combined row: <2%-divergent records, measured s on SNVs only, indels unchanged', sH_lt2, 0.0, 'YES', fixed=fx_c1))
    rows.append(row('same, with the measured indel share', sH_lt2, sIc, 'YES', fixed=fx_c2))
    res['rows'] = rows
    res['gap07b_combined_critic_rows'] = {'0.86': 12.29, '0.78': 13.37}
    # Day-favourable GAP-07b rows re-expressed with the symmetric correction (factor raw/fixed)
    fB = [r for r in rows if r['name'].startswith('(b) symmetric:')][0]['fixed_per_lineage']
    fac = 21051257.0 / fB
    res['day_favourable_rows_reexpressed'] = {k: v * fac for k, v in {'repeat-unit 171 bp': 9.45, 'repeat-unit 32 bp': 8.35, 'nested + unaligned 171/32 bp': 9.12, 'nested + unaligned 32 bp': 7.16,
                                                                    'indels x2': 8.84, 'indels x3': 8.09}.items()}
    res['day_favourable_factor'] = fac
    # ---- like-for-like SNV-only comparison (GC-4)
    snv_fixed_pl = N_SNV * (1 - sHc) / 2.0
    res['snv_only'] = dict(day_17_5M=DAY_SNV, measured_fixed_snv_per_lineage=snv_fixed_pl, day_over_measured=DAY_SNV / snv_fixed_pl - 1,
                           raw_snv_per_lineage=N_SNV / 2.0, shortfall_91800_scaled_snv_only=91800 * snv_fixed_pl / DAY_SNV,
                           shortfall_scaled_all_events=91800 * fB / DAY_SNV, day_vs_all_events=DAY_SNV / fB - 1,
                           shortfall_reduction_snv_only=1 - snv_fixed_pl / DAY_SNV)
    res['n_events'] = dict(n_pol1_small=n1, n_pol2_small=n2, n_rest=rest)
    json.dump(res, open(a.out, 'w'), indent=1, default=float)
    # text
    L = ['[PH] GAP-07c review fix pass (conventions: autosome shares applied to all sites)', '']
    L.append('SNV shares by threshold (in mask): H-derived %s' % {k: round(100 * v, 2) for k, v in sH.items()})
    L.append('   pooled %s' % {k: round(100 * v, 2) for k, v in sP.items()})
    L.append('   third %s unpol %s' % ({k: round(100 * v, 2) for k, v in s3.items()}, {k: round(100 * v, 2) for k, v in su.items()}))
    L.append('   s_H on <2%% records %.2f%%; all-sites s_H %.2f%%' % (100 * sH_lt2, 100 * res['snv']['sH_all_sites']))
    L.append('')
    L.append('INDEL human-lineage share, symmetric polarization (events <= 50 bp, net of null, T=1%, match w=2):')
    for w, d in res['indel_polarization'].items():
        L.append('  rule w=%-3s all sites: human %.2f%% (n %d)  chimp %.2f%%  human share of polarized %.3f | in mask: human %.2f%% chimp %.2f%%'
                 % (w[1:], 100 * d['all sites']['human']['net'], d['all sites']['n_human'], 100 * d['all sites']['chimp']['net'],
                    d['all sites']['human_share_of_polarized'], 100 * d['in mask']['human']['net'], 100 * d['in mask']['chimp']['net']))
    L.append('  central (w=5, in mask) shares by threshold: %s' % {k: round(100 * v, 2) for k, v in sInd.items()})
    L.append('  pooled (in mask, all events) shares: %s' % {k: round(100 * v, 2) for k, v in sIndPool.items()})
    L.append('  by size (human, w=5, in mask): %s' % json.dumps(res['indel_by_size_human_w5_inmask']))
    if have_ctl:
        L.append('')
        L.append('INDEL chance-match controls at AF >= 1%, w=2 (same-d observed vs controls):')
        for k, v in res['indel_controls'].items():
            L.append('  %-38s n=%8d same_d %.2f%% | -d %.2f%%  d+1 %.2f%%  d-1 %.2f%% | shift +-10kb %.3f%% %.3f%%  +-20kb %.3f%% %.3f%%'
                     % (k, v['n'], 100 * v['same_d'], 100 * v['negd'], 100 * v['dp1'], 100 * v['dm1'], 100 * v['null_p'], 100 * v['null_m'], 100 * v['null_p2'], 100 * v['null_m2']))
    L.append('')
    L.append('SV >= 50 bp (NYGC chr21+22; polarization is the as-run rule, which GAP-07b does not give for > 50 bp):')
    for k, v in svr.items():
        if v['n']:
            L.append('  %-30s n=%5d obs %.2f%% null %.2f%% net %.2f%%  95%% CI (obs) %.1f-%.1f%%' % (k, v['n'], 100 * v['obs'], 100 * v['null'], 100 * v['net'], 100 * v['ci95'][0], 100 * v['ci95'][1]))
    L.append('')
    L.append('BRACKET (205 M / fixed events per lineage); last column: numerator corrected for the SNV part (205 - 17.5 x s_snv)')
    for r in rows:
        L.append('  %-120s s_snv %5.2f%% s_ind %5.2f%% fixed %7.3f M ratio %6.2f  num-corr %6.2f  chimp-assumption: %s'
                 % (r['name'][:120], 100 * r['s_snv'], 100 * r['s_ind'], r['fixed_per_lineage'] / 1e6, r['ratio'], r['ratio_numerator_corrected'], r['chimp_assumption']))
        if 'events_human_lineage' in r:
            L.append('     human-lineage events %.3f M (SNV %.3f + indel %.3f + other); raw ratio same conventions %.2f' % (r['events_human_lineage'] / 1e6, r['snv_h'] / 1e6, r['ind_h'] / 1e6, r['ratio_raw_same_conventions']))
    L.append('GAP-07b combined critic rows for comparison: %s' % res['gap07b_combined_critic_rows'])
    L.append('Day-favourable GAP-07b rows x %.3f: %s' % (fac, {k: round(v, 2) for k, v in res['day_favourable_rows_reexpressed'].items()}))
    L.append('SNV-only like for like: %s' % json.dumps(res['snv_only']))
    open(a.out.replace('.json', '.out'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    c = sp.add_parser('ctl')
    c.add_argument('--vcf'); c.add_argument('--sites'); c.add_argument('--mask'); c.add_argument('--t-sizes'); c.add_argument('--out')
    r = sp.add_parser('report')
    r.add_argument('--sites'); r.add_argument('--af'); r.add_argument('--nygc'); r.add_argument('--gor'); r.add_argument('--ctl', default='')
    r.add_argument('--toplevel'); r.add_argument('--out')
    a = ap.parse_args()
    {'ctl': ctl_stage, 'report': report_stage}[a.cmd](a)


if __name__ == '__main__':
    main()
