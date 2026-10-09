"""GAP-07c figure (post hoc, presentation only): AF bands of the chimp-matching allele among GAP-07b divergent sites,
and the corrected 205 M / fixed-events ratio by treatment. Reads results/raw/gap07c_report.json.
Run: research/.venv/bin/python -I research/checks/gap07c_figure.py <report.json> <out.png> <posthoc_review.json>"""
import json
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r = json.load(open(sys.argv[1]))
names = ['not seen in panel', '(0, 0.1%)', '[0.1%, 1%)', '[1%, 10%)', '[10%, 50%)', '[50%, 90%)', '[90%, 99%)', '>= 99%']
cols = ['#e8eef6', '#c6d7ea', '#9dbbdb', '#6f9ac9', '#4a7bb5', '#2f5f9a', '#1f4678', '#12305a']
rows = [('human-derived sites\n(gorilla polarized)', 'H-derived, in mask'), ('chimp-derived sites', 'C-derived, in mask'),
        ('all sites in mask', 'in strict mask')]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.6), gridspec_kw={'width_ratios': [1.25, 1]})
for i, (lab, key) in enumerate(rows):
    v = r['snv'][key]
    left = 0
    tot = float(v['n'])
    for j, x in enumerate(v['bands']):
        w = 100 * x / tot
        a1.barh(i, w, left=left, color=cols[j], edgecolor='white', linewidth=1.5, height=0.55, label=names[j] if i == 0 else None)
        left += w
    a1.text(101, i, '%.1f%% >= 1%%' % (100 * v['poly_T']), va='center', fontsize=10)
a1.set_yticks(range(len(rows)))
a1.set_yticklabels([x[0] for x in rows], fontsize=10)
a1.invert_yaxis()
a1.set_xlim(0, 118)
a1.set_xlabel('% of divergent SNV sites (hg38 vs panTro6, autosomes, strict mask)\nby frequency in humans of the allele equal to the chimp base', fontsize=9)
a1.set_title('Human allele frequency of the chimp allele', fontsize=11, loc='left')
a1.legend(ncol=4, fontsize=7.5, frameon=False, loc='lower center', bbox_to_anchor=(0.45, -0.52))
for s in ('top', 'right'):
    a1.spines[s].set_visible(False)
a2.set_title('205 M / fixed events per lineage (post hoc bracket)', fontsize=11, loc='left')
ph = json.load(open(sys.argv[3]))
byname = {x['name']: x for x in ph['rows']}
def find(prefix):
    return [x for x in ph['rows'] if x['name'].startswith(prefix)][0]
items = [('raw count (GAP-07b)', find('raw')), ('(a) human data only, pooled', find('(a)')), ('human lineage alone', find('human lineage alone')),
         ('chimp share 0.5x human', find('chimp share 0.5x')), ('(b) chimp = human, AF >= 1%', find('(b) symmetric:')),
         ('(b) at AF >= 10%', find('(b) symmetric at AF >= 10%')), ('(b) seen at any frequency', find('(b) symmetric at seen')),
         ('(b) top-level fills', find('(b) top-level')), ('(c) chimp share 2x human', find('(c) chimp share 2x'))]
for i, (lab, r) in enumerate(items):
    x = r['ratio']
    assume = r['chimp_assumption'].startswith('YES')
    a2.barh(i, x, color='#4a7bb5' if assume else ('#9aa5b1' if i == 0 else '#1f4678'), height=0.55)
    a2.text(x + 0.15, i, '%.1f  (%.1f M)' % (x, r['fixed_per_lineage'] / 1e6), va='center', fontsize=10)
a2.set_yticks(range(len(items)))
a2.set_yticklabels([x[0] for x in items], fontsize=10)
a2.invert_yaxis()
a2.set_xlim(0, 16)
a2.set_xlabel('times (Day 205 M / fixed events per lineage)', fontsize=9)
for s in ('top', 'right'):
    a2.spines[s].set_visible(False)
fig.text(0.01, 0.01, 'Dark bars use human data only; light blue bars assume a chimp-lineage share (no chimp data); grey = raw. 1000 Genomes phase 3 (2,548 samples), GRCh38.', fontsize=8, color='#555')
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(sys.argv[2], dpi=140)
