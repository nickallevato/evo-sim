"""GAP-07b POST HOC (NOT pre-registered): arithmetic that combines the main-run JSONs with the post hoc block JSON into the
final events-vs-bp ladder and the comparisons with Day (205M / 410M), CSAC 2005 and Yoo 2025. No new data.
Run: research/.venv/bin/python -I research/checks/gap07b_posthoc_ladder.py RAWDIR   (RAWDIR = results/raw)
"""
import json
import sys

import numpy as np

R = sys.argv[1].rstrip('/') + '/'
net = json.load(open(R + 'gap07b_net.json')); axt = json.load(open(R + 'gap07b_axt.json'))
blk = json.load(open(R + 'gap07b_posthoc_blocks.json'))
snv = np.array(axt['snv'])[0]
cev = np.array(axt['cev_count']).sum(axis=(2, 3, 4)); cbp = (np.array(axt['cev_tbp']) + np.array(axt['cev_qbp'])).sum(axis=(2, 3, 4))
S0 = int(snv.sum()); S_lowdiv = int(snv[0].sum())            # record divergence class 0 (<2%)
S_unrep = int(snv[:, :, :, :, 0].sum()); S_f3 = int(snv[:2, :, :, 0, 0].sum())
ind = int(cev.sum())
nest_n = sum(v[0] for k, v in net['fills'].items() if '|L2|' in k)
nest_ali = sum(v[3] for k, v in net['fills'].items() if '|L2|' in k)
fh, qp, qo = blk['human'], blk['chimp_placed'], blk['chimp_unplaced']
segs = net['unaligned_human']['n'] + net['unaligned_chimp_placed']['n'] + net['unaligned_chimp_unplaced']['n']
hn = fh['length'] - fh['N']; qn = qp['length'] - qp['N']
print('SNV F0 %d ; records <2%% divergence %d ; unmasked %d ; F3 %d' % (S0, S_lowdiv, S_unrep, S_f3))
print('indel events %d ; nested fills %d ; outside-fill unaligned segments (human, chimp placed, chimp unplaced) %d' % (ind, nest_n, segs))
print('human: non-N %d, aligned-block bp %d, unaligned non-N %d (%.4f); nested fills ali bp %d' % (hn, fh['aligned'], fh['unaligned_nonN'], fh['unaligned_nonN'] / hn, nest_ali))
print('chimp placed: non-N %d, unaligned non-N %d (%.4f); unplaced scaffolds unaligned non-N %d' % (qn, qp['unaligned_nonN'], qp['unaligned_nonN'] / qn, qo['unaligned_nonN']))
hum_nc = fh['unaligned_nonN'] + nest_ali; chi_nc = qp['unaligned_nonN'] + nest_ali
print('Yoo-like non-1:1 analogue: human %d (%.4f of non-N), chimp placed %d (%.4f)' % (hum_nc, hum_nc / hn, chi_nc, chi_nc / qn))
print('coincidence check: human unaligned + chimp placed unaligned + chimp unplaced unaligned = %d' % (fh['unaligned_nonN'] + qp['unaligned_nonN'] + qo['unaligned_nonN']))
rows = []
for name, snvs, extra_events in (('F0 SNV, all net alignments', S0, 0), ('SNV in records <2% divergence only', S_lowdiv, 0),
                                 ('F2 unmasked SNV only', S_unrep, 0), ('F3', S_f3, 0)):
    ev_ind = ind if name != 'F2 unmasked SNV only' and name != 'F3' else None
    rows.append((name, snvs))
ev_total = S0 + ind + nest_n + segs
print('events total F0 = %d ; per lineage ~ %.0f ; 205M / per lineage = %.2f ; 410M / total = %.2f' % (ev_total, ev_total / 2, 205e6 / (ev_total / 2), 410e6 / ev_total))
ev_low = S_lowdiv + ind + nest_n + segs
print('events total, SNV in <2%% records only = %d ; per lineage %.0f ; 205M / per lineage = %.2f' % (ev_low, ev_low / 2, 205e6 / (ev_low / 2)))
print('bp ladder (both genomes; placed chimp only):')
b_snv = S0
b_strict = S0 + fh['unaligned_nonN'] + qp['unaligned_nonN']
b_yoo = S0 + hum_nc + chi_nc
b_withunpl = b_strict + qo['unaligned_nonN']
for nm, b in (('SNV only', b_snv), ('SNV + unaligned non-N (human + chimp placed)', b_strict),
              ('SNV + unaligned + non-colinear nested aligned (Yoo-like)', b_yoo), ('strict + chimp unplaced scaffolds unaligned', b_withunpl)):
    print('  %-62s %12d  bp/event (F0 events %d) = %.2f ; 410M/this = %.3f' % (nm, b, ev_total, b / ev_total, 410e6 / b))
tot_clean = sum(v['clean_bp'] for v in blk['by_size'].values())
print('clean gap bp (not N, not aligned elsewhere) %d ; raw %d' % (tot_clean, sum(v['raw_bp'] for v in blk['by_size'].values())))
for k, v in blk['by_kind'].items():
    print('  %s events %d raw_bp %d clean_bp %d' % (k, v['events'], v['raw_bp'], v['clean_bp']))
print('fixed fraction of SNVs (CSAC 0.78-0.86): %d - %d on F0; %d - %d on <2%% records' % (0.78 * S0, 0.86 * S0, 0.78 * S_lowdiv, 0.86 * S_lowdiv))
# hypothetical fixed events per lineage
for fx in (0.78, 0.86):
    print('fixed-only events per lineage at %.2f: SNV %.0f + indel %.0f = %.0f ; 205M/that = %.2f' % (fx, fx * S0 / 2, fx * ind / 2, fx * (S0 + ind) / 2, 205e6 / (fx * (S0 + ind) / 2)))
