"""E5/E6 -- LTEE fixation counts under each counting rule, recounted from the repo's own source text.

Targets: E5 (quote ids RE-03, RE-04, RE-10: Ara-2 = -906; Ara+5 38 -> 0) and E6 (Q56-Q58: 5,496 strict vs 8,679 naive;
1,322 snapshot). Data: Z23003785 s4.1 table (>=95% snapshot per 10K timepoint) and Z23105291 Table 1 (strict /
within-lineage / first-crossing, per-population generations), both in sources/raw/day/*.txt (gitignored; read-only here).
The Good 2017 per-site data files are NOT in the repo, so this is a recount of the papers' own tables, not a re-derivation
of the state calls (E6's fidelity stays unverifiable). The clone-pair formula giving -906 is not in the extracted text:
not recomputed (skipped).

Rules compared (non-mutators Ara+2, +4, +5, -5, -6): (a) snapshot >=95% at 60K (Z23003785); (b) first crossing = the naive
>=95% rule (Z23105291 col 'First-crossing'); (c) strict whole-population (Z23105291); (d) strict + within-lineage sweeps.
G_f is computed two ways: nominal 60,000 / mean count (the papers' way) and sum(own generations)/sum(count).

Pre-registered predictions (made after reading the tables; this is arithmetic, not a blind test):
  Critic side: (a) and (b) disagree, and the snapshot is not monotone (Ara+5 falls to 0); G_f depends on the rule by >1.5x.
  Day side: (c) gives 189 -> 1,587 gen/fix (+20% on 1,322); all table sums reproduce (5,496 / 7,166 / 8,679 / 723,000).
  Expected: (a) 1,322; (b) 824; (c) 1,587; (d) 521; nominal-endpoint vs own-generation variants differ by <3%.
  Neither side predicts per-population agreement between (a) and (c); expected to fail (Ara-5: 60 vs 9).
"""
import os, re
S = {'Ara+2': [19,25,31,45,55,64], 'Ara+4': [4,31,36,38,28,68], 'Ara+5': [16,13,38,34,14,0],
     'Ara-5': [9,16,36,7,63,60], 'Ara-6': [15,22,26,24,24,35]}
T1 = {  # pop: (gens, pass_mut, strict, within, first, inflation)
 'Ara+2': (60500,174,66,0,66,0), 'Ara+4': (60000,201,73,0,80,7), 'Ara+5': (57500,202,14,105,63,49),
 'Ara-5': (60500,406,9,173,96,87), 'Ara-6': (60000,221,27,107,59,32),
 'Ara+1': (60000,466,98,50,115,17), 'Ara+3': (60000,6102,1572,447,1838,266), 'Ara+6': (63500,10134,1601,1756,2594,993),
 'Ara-1': (60500,4597,268,1692,621,353), 'Ara-2': (60000,3488,94,1816,1094,1000),
 'Ara-3': (60500,3255,796,0,820,24), 'Ara-4': (60000,4872,878,1020,1233,355)}
NM = list(S); MU = [p for p in T1 if p not in S]
raw = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'raw', 'day', 'zenodo-23105291.txt')
if os.path.exists(raw):  # cross-check the transcription against the raw text
    txt = open(raw, encoding='utf-8').read().replace('−', '-')
    for p, v in T1.items():
        m = re.search(r'^' + re.escape(p) + r'\s+\S+\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)', txt, re.M)
        got = tuple(int(x.replace(',', '')) for x in m.groups())
        assert got == v, (p, got, v)
    print('transcription matches raw Z23105291 Table 1 (12 rows)')
col = lambda i, ps=None: sum(T1[p][i] for p in (ps or T1))
print('Table sums: strict', col(2), 'within', col(3), 'first', col(4), 'inflation', col(5), 'gens', col(0), '(paper 5496/7166/8679/3183/723000)')
print('naive/strict - 1 = %.1f%%; share removed = %.1f%%' % (100*(col(4)/col(2)-1), 100*(1-col(2)/col(4))))
print('\nPer-population non-mutators (60K snapshot | first-crossing | strict | strict+within):')
for p in NM:
    print(' %-6s %3d | %3d | %3d | %3d' % (p, S[p][-1], T1[p][4], T1[p][2], T1[p][2]+T1[p][3]))
snap = [S[p][-1] for p in NM]
rules = {'(a) snapshot 60K': snap, '(b) first crossing (naive 95%)': [T1[p][4] for p in NM],
         '(c) strict whole-pop': [T1[p][2] for p in NM], '(d) strict + within-lineage': [T1[p][2]+T1[p][3] for p in NM]}
gens = [T1[p][0] for p in NM]
print('\n%-32s %5s %7s %9s %9s' % ('rule', 'sum', 'mean', 'G_f nom.', 'G_f own'))
res = {}
for k, v in rules.items():
    res[k] = 60000/(sum(v)/5)
    print('%-32s %5d %7.1f %9.0f %9.0f' % (k, sum(v), sum(v)/5, res[k], sum(gens)/sum(v)))
print('snapshot excluding Ara+5 zero: mean %.2f -> %.0f' % (sum(snap)/4, 60000/(sum(snap)/4)))
print('strict vs snapshot: %+.1f%%; first-crossing vs snapshot: %+.1f%%; spread max/min = %.2fx' % (
    100*(res['(c) strict whole-pop']/1322-1), 100*(res['(b) first crossing (naive 95%)']/1322-1), max(res.values())/min(res.values())))
print('snapshot timepoint means 10K..60K:', [round(sum(S[p][i] for p in NM)/5, 1) for i in range(6)],
      '-> G_f', [round(10000*(i+1)/(sum(S[p][i] for p in NM)/5)) for i in range(6)])
print('Ara+5 snapshot series', S['Ara+5'], '; Ara+5 last sample 57,500 (Z23105291), so the 60K cell is beyond its last sample')
mu_s = col(2, MU); mu_g = col(0, MU)
print('\nMutators strict: %d over %d gens = %.4f/gen -> %.0f gen/fix; first-crossing %d -> %.0f gen/fix' % (
    mu_s, mu_g, mu_s/mu_g, mu_g/mu_s, col(4, MU), mu_g/col(4, MU)))
print('Ara-2 snapshot-style negative (-906) is not recomputed: clone-pair formula not in extracted text. Strict Ara-2 = %d (>=0).' % T1['Ara-2'][2])
