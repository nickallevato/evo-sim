"""D1 FIX PASS (POST HOC) aggregation of d1_fix_rna_fp.json, d1_nn.json, d1_rna.json, d1_posthoc.json for R4-D1-spike.md.
Analysis only.  Run: research/.venv/bin/python -I research/checks/d1_fix_aggregate.py -> results/raw/d1_fix_aggregate.txt"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import d1_sequence_space_spike as D
R = D.RAW
fp = json.load(open(os.path.join(R, "d1_fix_rna_fp.json")))
nn = json.load(open(os.path.join(R, "d1_nn.json")))
rn = json.load(open(os.path.join(R, "d1_rna.json")))
ph = json.load(open(os.path.join(R, "d1_posthoc.json")))
out = []
P = out.append
P("== uniform comparator (40+40 uniform genotypes by rejection) vs walk (same sizes)")
U = fp["uni"]
ok = {k: v for k, v in U.items() if "uniform" in v}
P("targets: " + ", ".join(sorted(ok)))
P(f"hamming/L uniform {np.median([v['uniform']['hamming'] for v in ok.values()]):.3f} [{min(v['uniform']['hamming'] for v in ok.values()):.3f}-{max(v['uniform']['hamming'] for v in ok.values()):.3f}]; walk {np.median([v['walk']['hamming'] for v in ok.values()]):.3f} [{min(v['walk']['hamming'] for v in ok.values()):.3f}-{max(v['walk']['hamming'] for v in ok.values()):.3f}]")
dn = [v['walk']['nu'] - v['uniform']['nu'] for v in ok.values()]
P(f"nu walk - uniform per target: {[round(x,3) for x in dn]}; mean {np.mean(dn):.3f}; uniform SE ~ {np.median([v['uniform']['nu_se'] for v in ok.values()]):.3f}")
for c in ("E0", "E1", "E2g"):
    pairs = [(v['uniform']['single'][c], v['walk']['single'][c]) for v in ok.values() if c in v['uniform']['single'] and c in v['walk']['single']]
    ur = [a['reach'] for a, b in pairs]; wr = [b['reach'] for a, b in pairs]
    um = [a['m_pos'] for a, b in pairs if a['m_pos'] and b['m_pos']]; wm = [b['m_pos'] for a, b in pairs if a['m_pos'] and b['m_pos']]
    P(f"{c}: n={len(pairs)} reach uniform median {np.median(ur):.3f} walk {np.median(wr):.3f}; per-target ratio uniform/walk {[round(a/b,2) if b else None for a,b in zip(ur,wr)]}; sum ratio {sum(ur)/sum(wr):.2f}; m|reach uniform {np.median(um):.2f} walk {np.median(wm):.2f}")
P("\n== first passage (accepted neutral substitutions), pooled over the 8 targets with L<=50")
for c in ("E0", "E1", "E2g"):
    vs = [v['curves'][c] for v in fp['fp'].values() if c in v['curves']]
    P(f"{c} (targets {len(vs)}): by_step median over targets " + ", ".join(f"{s}: {np.median([x['by_step'][s] for x in vs]):.3f}" for s in vs[0]['by_step']) + f"; median first-passage among found {np.median([x['median_found'] for x in vs if x['median_found'] is not None]):.1f} (range {min(x['median_found'] for x in vs if x['median_found'] is not None):.0f}-{max(x['median_found'] for x in vs if x['median_found'] is not None):.0f})")
pa = [v['proposals_per_accept'] for v in fp['fp'].values()]
P(f"proposals per accepted step {np.median(pa):.2f}")
nu = {k: rn[k]['nu_mean'] for k in fp['fp']}
P("neutral substitutions available in a locus over the window = L*mu*nu*T (mu=1.2e-8):")
for k, v in sorted(fp['fp'].items()):
    for T in (3e5, 146250):
        pass
    P(f"  {k} L={v['L']} nu={nu[k]:.3f}: T=3e5 -> {v['L']*1.2e-8*nu[k]*3e5:.3f}; T=146,250 -> {v['L']*1.2e-8*nu[k]*146250:.3f}; standing neutral heterozygous sites 4N mu L nu = {4e4*1.2e-8*v['L']*nu[k]:.4f}")
P("\n== tRNA76 row (main + post hoc)")
t = rn['tRNA76']['single']; tp = ph['tRNA76']['single']
for c in ('E0_uniform', 'E0_freqw', 'E1_uniform', 'E2_uniform'):
    P(f"  {c}: reach {t[c]['reach']:.4f}, m|reach {t[c]['mean_pos']}, m_all {t[c]['mean_all']:.4f}")
for c in ('E0far', 'E2g', 'E2rare'):
    P(f"  {c}: reach {tp[c]['reach']:.4f}, m|reach {tp[c]['mean_pos']}, m_all {tp[c]['mean_all']:.4f}")
P("\n== E2g by target (L>=76): m|reach, m_all, lam(m_all) at s=0.01 T=3e5")
for k, v in sorted(ph.items()):
    if v['L'] >= 76 and 'E2g' in v['single']:
        s = v['single']['E2g']
        P(f"  {k}: m|reach {s['mean_pos']:.2f} m_all {s['mean_all']:.2f} lam(m_all) {s['mean_all']*0.48:.2f} lam(m|reach) {s['mean_pos']*0.48:.2f}")
P("\n== NN hits per target")
for k, v in sorted(nn.items(), key=lambda kv: (kv[1]['L'], kv[0])):
    P(f"  {k} L={v['L']} hits {v['hits']}/{v['M']} log10NN {v['log10_NN']} CI [{v['log10_NN_lo']:.1f},{v['log10_NN_hi']:.1f}]")
open(os.path.join(R, "d1_fix_aggregate.txt"), "w").write("\n".join(out))
print("\n".join(out))
