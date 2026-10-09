"""D1 POST HOC refinement (written AFTER the main d1 RNA output was seen; everything here is labelled post hoc).

Run:  research/.venv/bin/python -I research/checks/d1_posthoc_refine.py [--smoke]
Output: research/checks/results/raw/d1_posthoc.json

WHY.  The pre-registered E2 ("same level-5 shape as S2") gave per-genotype m of 13-45 (far above my predicted 2-12) and
reach 0.7-1.0.  Cause suspected after seeing the output: S2 was drawn uniformly over DISTINCT accessible structures, and
many distinct structures share a few very common shapes (typically "a helix was lost"), so the shape class is dominated by
trivial structural degradation rather than by a different functional topology.  Likewise E0's pool contains many
near-S1 frayed structures (1-2 bp from S1).  This script re-evaluates the SAME genotypes (same seeds, same neutral-walk
samples as the main run) with stricter, explicitly post-hoc classes:
  E0far  : exact structure S2 with d_bp(S1,S2) >= 5 (excludes fraying).
  E2g    : shape5(S2) != shape5(S1) AND helix count of S2 >= helix count of S1 (a rearrangement or gain, not a loss).
  E2rare : shape5(S2) != shape5(S1) AND that shape accounts for <= 1% of all non-neutral neighbour instances of the A-sample
           (removes the commonest shapes).
  E2g_rare: both E2g and E2rare.
Also reports the composition of the neighbourhood (share of neighbour instances that lose / keep / gain helices; number of
distinct shapes; top-shape share) and the Hamming spread of the neutral-walk samples (is the sampled network wide?).
No pre-registered prediction exists for these.  I expect (stated now, before the post-hoc run): E2g and E2rare per-genotype
m|reach well below the main E2 value (roughly 3-15), still above E0far (1.5-4).  Any result is reported.
"""
import os, sys, json, time, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import d1_sequence_space_spike as D

SMOKE = "--smoke" in sys.argv


def job(args):
    cfgid, name, L, S1, seed_seq, KA, KB, npool = args
    rng = np.random.default_rng(np.random.SeedSequence([D.SEED, 2, cfgid, 0]))  # identical stream/samples to the main run
    cur = D.neutral_walk(rng, seed_seq, S1, 50 * L)
    samples = []
    for _ in range(KA + KB):
        cur = D.neutral_walk(rng, cur, S1, 10 * L)
        samples.append(cur)
    A, B = samples[:KA], samples[KA:]
    rng2 = np.random.default_rng(np.random.SeedSequence([D.SEED, 9, cfgid, 0]))
    sh1 = D.shape5(S1)
    nh1 = D.nhelix(S1)
    scanA = [[D.fold(m) for m in D.neighbors(x)] for x in A]
    scanB = [(D.neighbors(x), [D.fold(m) for m in D.neighbors(x)]) for x in B]
    res = dict(name=name, L=L, KA=KA, KB=KB)
    # Hamming spread
    def ham(a, b):
        return sum(1 for p, q in zip(a, b) if p != q)
    allv = [seed_seq] + samples
    hs = [ham(allv[i], allv[j]) / L for i in range(len(allv)) for j in range(i + 1, len(allv))]
    res["hamming_mean_over_L"] = float(np.mean(hs))
    res["hamming_seed_to_last_over_L"] = ham(seed_seq, samples[-1]) / L
    # neighbourhood composition
    cnt = collections.Counter()
    shc = collections.Counter()
    loss = keep = gain = 0
    tot = 0
    for sts in scanA:
        for s in sts:
            if s == S1:
                continue
            cnt[s] += 1
            shc[D.shape5(s)] += 1
            h = D.nhelix(s)
            tot += 1
            if D.shape5(s) == sh1:
                keep += 1
            elif h < nh1:
                loss += 1
            else:
                gain += 1
    res["nbr_instances_changed"] = tot
    res["nbr_share_same_shape_as_S1"] = keep / tot
    res["nbr_share_shape_change_fewer_helices"] = loss / tot
    res["nbr_share_shape_change_ge_helices"] = gain / tot
    res["n_distinct_shapes"] = len(shc)
    res["top_shape_share"] = max(shc.values()) / tot
    res["top3_shape_share"] = sum(v for _, v in shc.most_common(3)) / tot
    distinct = sorted(cnt)
    d1 = {s: D.dbp(s, S1) for s in distinct}
    res["pool_dbp_quantiles_E0"] = [float(x) for x in np.percentile(list(d1.values()), [10, 25, 50, 75, 90])]
    cands = {
        "E0far": [s for s in distinct if d1[s] >= 5],
        "E2g": [s for s in distinct if D.shape5(s) != sh1 and D.nhelix(s) >= nh1],
        "E2rare": [s for s in distinct if D.shape5(s) != sh1 and shc[D.shape5(s)] / tot <= 0.01],
    }
    cands["E2g_rare"] = [s for s in cands["E2g"] if shc[D.shape5(s)] / tot <= 0.01]
    regB = {}
    for muts, sts in scanB:
        for s in sts:
            regB.setdefault(s, len(regB))
    structsB = list(regB)
    idsB = [np.array([regB[s] for s in sts]) for muts, sts in scanB]
    ks = sorted(set(K for K in (1, 5, 20, KB) if K <= KB))
    res["single"] = {}
    for nm, cand in cands.items():
        res[f"n_cand_{nm}"] = len(cand)
        if not cand:
            continue
        pick = [cand[i] for i in rng2.choice(len(cand), size=min(npool, len(cand)), replace=False)]
        cls = "E0" if nm == "E0far" else "E2"
        Mx = D.membership(structsB, pick, cls)
        m1 = np.array([Mx[ids].sum(axis=0) for ids in idsB])
        res["single"][nm] = D.summarize_counts(m1, ks)
    D.say("done", name)
    return res


def main():
    specs = D.make_targets(SMOKE)
    jobs = []
    for ci, (name, L, db, seed) in enumerate(specs):
        KA, KB = (3, 4) if SMOKE else ((40, 60) if L <= 50 else (30, 40))
        jobs.append((ci, name, L, db, seed, KA, KB, 10 if SMOKE else 100))
    jobs.sort(key=lambda j: -j[2])
    out = {}
    with Pool(2 if SMOKE else 12, maxtasksperchild=1) as p:
        for r in p.imap_unordered(job, jobs):
            out[r["name"]] = r
    tag = "_smoke" if SMOKE else ""
    with open(os.path.join(D.RAW, f"d1_posthoc{tag}.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    for k, v in sorted(out.items(), key=lambda kv: (kv[1]["L"], kv[0])):
        line = f"{k} L={v['L']} hamming/L={v['hamming_mean_over_L']:.2f} same_shape={v['nbr_share_same_shape_as_S1']:.2f} fewer_helix={v['nbr_share_shape_change_fewer_helices']:.2f} ge_helix={v['nbr_share_shape_change_ge_helices']:.2f} nshapes={v['n_distinct_shapes']} top3={v['top3_shape_share']:.2f} d10/50/90={v['pool_dbp_quantiles_E0'][0]:.0f}/{v['pool_dbp_quantiles_E0'][2]:.0f}/{v['pool_dbp_quantiles_E0'][4]:.0f}"
        D.say(line)
        for nm, s in v["single"].items():
            mp = s["mean_pos"]
            D.say(f"    {nm} ncand={v['n_cand_'+nm]} reach={s['reach']:.3f} mean_all={s['mean_all']:.2f} mean_pos={mp if mp is None else round(mp,2)} med_pos={s['median_pos']} p90={s['p90_pos']} max={s['max']}")


if __name__ == "__main__":
    main()
