"""C1d verification (post hoc, written after the main runs): independent checks of the decoding and of day_events.

    research/.venv/bin/python -I research/checks/c1d_verify.py <v62|v66>
  1. Decode the raw genotype records of two named SNPs for the keruru 'Mod' and 'EN' groups WITHOUT the block/LUT matrix code
     (bit-by-bit, one individual at a time) and compare their per-group counts with the extraction output.
  2. Allele frequency of rs4988235 (LCT/MCM6) by keruru bin; keruru's draft states 0.996 -> 0.732 across his series for the
     counted allele.  Any strong departure would signal a decoding or group error.
  3. Brute-force pure-Python day_events (E1, T2, m = 1, all11) on 20,000 random SNPs against the vectorised function.
Writes research/checks/results/raw/c1d_<rel>_verify.txt.
"""
import os
import sys
import importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("c1d", os.path.join(HERE, "c1d_aadr_real.py"))
c1d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c1d)


def decode_one(mm, ind_row, snp_idx, kind, nind, rec):
    """Genotype (0/1/2/3) of one individual at one SNP by explicit bit extraction."""
    if kind == "TGENO":
        byte = int(mm[ind_row, snp_idx // 4])
        shift = 6 - 2 * (snp_idx % 4)
    else:
        byte = int(mm[snp_idx, ind_row // 4])
        shift = 6 - 2 * (ind_row % 4)
    return (byte >> shift) & 3


def main(rel):
    L = []
    N, D, names, sel, ic, ih = c1d.load_counts(rel)
    cnt = c1d.Counts(N, D, names)
    ids, chrom, pos = c1d.load_snp(rel)
    meta = c1d.load_meta(rel)
    gn, masks = c1d.build_groups(meta)
    g = c1d.Geno(os.path.join(c1d.DATA, c1d.REL[rel]["stem"] + ".geno"))
    rng = np.random.default_rng(7)
    # 1. explicit decode of 3 SNPs for three groups
    pick = [int(np.where(ids == "rs4988235")[0][0]), int(rng.integers(0, len(ids))), int(rng.integers(0, len(ids)))]
    for gname in ("kr:EN", "kr:Mod", "day1:6000-7000"):
        members = np.where(masks[gn.index(gname)])[0]
        for s in pick:
            n_ph = n_dip = d_ph = d_dip = 0
            for i in members:
                v = decode_one(g.mm, i, s, g.kind, g.nind, g.rec)
                if v == 3:
                    continue
                if meta["dip"][i]:
                    n_dip += 1
                    d_dip += v
                else:
                    n_ph += 1
                    d_ph += v
            nph, ndip, dph, ddip = [int(a[s]) for a in cnt.raw(gname)]
            ok = (nph, ndip, dph, ddip) == (n_ph, n_dip, d_ph, d_dip)
            L.append("decode %-16s %-12s direct n_ph/n_dip/dose_ph/dose_dip %s  extracted %s  %s" % (
                gname, ids[s], (n_ph, n_dip, d_ph, d_dip), (nph, ndip, dph, ddip), "OK" if ok else "MISMATCH"))
    # 2. rs4988235
    s = pick[0]
    L.append("rs4988235 chr%d:%d counted-allele frequency (individual weighting, keruru form) by bin:" % (chrom[s], pos[s]))
    for b in c1d.KR_NAMES:
        n, k = cnt.indiv("kr:" + b)
        L.append("   %-5s n_called %5d  freq %.3f" % (b, n[s], k[s] / (2.0 * max(1, n[s]))))
    # 3. brute force day_events
    S = len(chrom)
    idx = np.sort(rng.choice(S, 20000, replace=False))
    n = np.zeros((c1d.NB, S), dtype=np.int32)
    r = np.zeros((c1d.NB, S), dtype=np.int32)
    for i, nm in enumerate(c1d.DAY_NAMES):
        n[i], r[i] = cnt.chrom("day1:%s" % nm)
    sub_n, sub_r = n[:, idx], r[:, idx]
    v = c1d.day_events(sub_n, sub_r, "E1", "T2", 1, "all11")
    elig = 0
    hist = [0] * c1d.NB
    for j in range(len(idx)):
        for allele in (0, 1):
            ns = [int(x) for x in sub_n[:, j]]
            ks = [int(sub_r[b, j]) if allele == 0 else ns[b] - int(sub_r[b, j]) for b in range(c1d.NB)]
            if ns[10] == 0 or ks[10] != ns[10]:
                continue
            neo_n, neo_k = ns[2] + ns[3], ks[2] + ks[3]
            if neo_n == 0 or neo_k == neo_n:
                continue
            elig += 1
            if all(x > 0 for x in ns):
                date = next(b for b in range(c1d.NB) if ns[b] > 0 and ks[b] == ns[b])
                hist[date] += 1
    L.append("brute force on %d random SNPs: eligible %d profile %s" % (len(idx), elig, hist))
    L.append("vectorised               : eligible %d profile %s" % (v["eligible"], [int(x) for x in v["hist"]]))
    L.append("MATCH" if (elig == v["eligible"] and hist == [int(x) for x in v["hist"]]) else "MISMATCH")
    out = os.path.join(c1d.RES, "c1d_%s_verify.txt" % rel)
    with open(out, "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1])
