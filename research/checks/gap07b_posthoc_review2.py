"""GAP-07b POST HOC (review-fix pass, part 2; NOT pre-registered): arithmetic on the committed JSONs, including the
nested/top split from gap07b_posthoc_review.py nested. Prints (i) the top-level-fill-only SNV events ratio,
(ii) a "bases that differ" row that removes hg38 centromere models (>= 59.5 Mb of the human unaligned bp) and avoids the
double counting of SNVs inside nested fills, (iii) the Yoo-style row with syntenic ("syn") nested fills removed (review m8),
(iv) the final bracket endpoints used in the results note.
Run: research/.venv/bin/python -I research/checks/gap07b_posthoc_review2.py RAWDIR
"""
import json
import sys

R = sys.argv[1].rstrip('/') + '/'
net = json.load(open(R + 'gap07b_net.json')); axt = json.load(open(R + 'gap07b_axt.json'))
blk = json.load(open(R + 'gap07b_posthoc_blocks.json')); nst = json.load(open(R + 'gap07b_posthoc_review_nested.json'))
import numpy as np
S0 = int(np.array(axt['snv'])[0].sum()); IND = int(np.array(axt['cev_count']).sum())
NEST = sum(v[0] for k, v in net['fills'].items() if '|L2|' in k)
SEG = net['unaligned_human']['n'] + net['unaligned_chimp_placed']['n']
EV = S0 + IND + NEST + SEG
top, nested = nst['top'], nst['nested']
print('SNV top-level fills %d ; nested fills %d ; sum %d (main run %d) ; nested divergence %.4f vs top %.4f' % (
    top['snv'], nested['snv'], top['snv'] + nested['snv'], S0, nested['divergence'], top['divergence']))
ev_top = top['snv'] + IND + NEST + SEG
print('events with SNVs from top-level (colinear) fills only: %d ; per lineage %.2f M ; 205M/that = %.2f' % (ev_top, ev_top / 2e6, 205e6 / (ev_top / 2)))
CEN = 59539749                                    # hg38 centromere-model bp inside unaligned segments outside net fills (main run)
hu, cp = blk['human']['unaligned_nonN'], blk['chimp_placed']['unaligned_nonN']
differ = S0 + (hu - CEN) + cp
print('bases that differ (lower-bound row): SNV %d + human unaligned %d minus centromere models %d + chimp placed unaligned %d = %d ; 410M/that = %.2f ; per event %.2f' % (S0, hu, CEN, cp, differ, 410e6 / differ, differ / EV))
print('upper row with centromere models: %d ; per event %.2f' % (S0 + hu + cp, (S0 + hu + cp) / EV))
syn = sum(v[3] for k, v in net['fills'].items() if k.startswith('syn|L2'))
inv = sum(v[3] for k, v in net['fills'].items() if k.startswith('inv|L2')); non = sum(v[3] for k, v in net['fills'].items() if k.startswith('nonSyn|L2'))
yoo_full = S0 + (hu + syn + inv + non) + (cp + syn + inv + non) - nested['snv']
yoo_nosyn = S0 + (hu + inv + non) + (cp + inv + non) - nested['snv']
print('nested ali bp: syn %d inv %d nonSyn %d' % (syn, inv, non))
print('Yoo-style row (all nested), SNVs inside nested fills not double counted: %d ; per event %.2f' % (yoo_full, yoo_full / EV))
print('Yoo-style row excluding syntenic nested fills, no double count: %d ; per event %.2f' % (yoo_nosyn, yoo_nosyn / EV))
print('SNV positions inside nested fills counted twice in the published 523M row: %d' % nested['snv'])
