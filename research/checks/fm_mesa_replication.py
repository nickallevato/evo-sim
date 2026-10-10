"""FM: replication of Day's "mesas" (The Fourth Mechanism, 2026-10-10) against a heterogeneous-mutation-rate null.

Tier: LOAD-BEARING (ROOT-FM supports ROOT; three reviews).  Pre-registered: this docstring and the code are
committed BEFORE any analysis of the alignment (only the first 30 lines of the MAF were viewed, for format).
Runs on na-workhorse only.  Stages: `extract <hs1.maf.gz> <out.npz>` (one streaming pass, ~1-3 h, < 2 GB RAM),
then `analyse <out.npz> <out.json>` (minutes).  `selftest` runs a synthetic MAF (local, trivial).

TARGET CLAIMS (verbatim; blog "The Fourth Mechanism", 2026-10-10; ROOT-FM; quotes Q162-Q171)
  FM3 (Q164) "The substitution density across the genome is massively overdispersed, more than 80 times more
       variable than a uniform-rate process predicts."
  FM4 (Q165) "Dense regions cluster next to other dense regions, forming contiguous blocks of elevated
       substitution with sharp boundaries in a pattern we call mesas."
  FM5 (Q166) "A single mesa on a single chromosome shows an excess of human-lineage substitutions that exceeds
       both the MITTENS fixation ceiling and the maximum that natural selection can theoretically fix across the
       entire genome according to Haldane."
  FM8 (Q169) "... a) the mesa signature exists, b) that it is the dominant source of genomic divergence between
       humans and the great apes, and, c) no account of speciation is complete without it."
  FM10 (Q171) "neither natural selection nor neutral diffusive drift can still be considered viable candidates.
       ... all of the data has been provided by the T2T Primate Consortium (Yoo et al. 2025) aligned with
       Progressive Cactus (Armstrong et al. 2020)."
  Day released no window size, statistic, coordinates or code (refresh 2026-10-10), so a GRID is pre-registered.

DATA (lightest adequate public product; untrusted, read only, never executed)
  8-t2t-apes-2023v2.hs1.maf.gz (Cactus v2.7.1, cactus-hal2maf --refGenome hs1 --filterGapCausingDupes
  --noAncestors; https://cgl.gi.ucsc.edu/data/cactus/t2t-apes/8-t2t-apes-2023v2/ ; 3.1 GB; md5 in the .md5
  file next to it).  The same Cactus alignment of the T2T Primate Consortium genomes Day names (the 8-way
  primary alignment: hs1 = T2T-CHM13, hg38, chimpanzee GCA_028858775.2, bonobo GCA_029289425.2, gorilla
  GCA_029281585.2, Sumatran orangutan GCA_028885655.2, Bornean orangutan GCA_028885625.2, siamang
  GCA_028878055.2).  Human-referenced, so every lineage is counted on CHM13 coordinates.  The full HAL (17 GB)
  would add ancestral reconstructions; it is not needed for parsimony polarisation with two outgroups.

EXTRACTION (per 1 kb hs1 bin; per class = repeat(hs1 soft-mask) x CpG x dup; uint16 counts)
  Columns used: hs1 non-gap.  "core" column: hs1, hg38, chimp (c), bonobo (b), gorilla (g), Sumatran orang (o)
  all present as A/C/G/T (case-insensitive).  dup class = the block has > 1 row for any of those six genomes
  (paralogous rows; segmental duplications and collapsed repeats).  CpG class = C followed by G (or G preceded
  by C) in hs1, chimp or gorilla, judged on the hs1-ungapped projection of the block (block edges: non-CpG).
  Fields (h = hs1 base, all comparisons case-insensitive; lineage fields require hs1 == hg38):
    m     core columns
    H     human lineage since the human-chimp ancestor:   h != g, c == g == o
    C     chimp lineage since the human-chimp ancestor:   c != g, h == g == o   (bonobo ignored)
    B     bonobo lineage since the human-chimp ancestor:  b != g, h == g == o   (chimp ignored)
    G     gorilla terminal lineage:                       g != h, h == c == o
    HCs   human-chimp stem:                               h == c != g == o
    iHG   ILS proxy, human and gorilla share a derived state:  h == g != c == b == o
    iCG   ILS proxy, chimp and gorilla share a derived state:  c == g != h == o
    DHC   pairwise h != c (unpolarised; closest to a naive "human-chimp substitution density")
    hh    hs1 != hg38 (human assembly difference or polymorphism; error proxy)
    gc    hs1 G or C
  (iHG/iCG are covariates only.)

ANALYSIS GRID (every cell reported; no cell selected after seeing data)
  Windows W in {1 kb, 10 kb, 100 kb, 1 Mb} (sums of 1 kb bins, non-overlapping, per chromosome).
  Filters: F0 all classes (naive; nearest to an unmasked analysis); F1 dup = 0; F2 dup = 0 and non-repeat;
           F3 = F2 and non-CpG.  A window is used if its core columns m >= 0.5 W under the filter.
  Autosomes are primary; chrX reported separately; chrY and chrM excluded.
  Lineages: H, C, B, G, and DHC.
  S1  dispersion index phi = sum (n - m p)^2 / (m p (1 - p)) / (k - 1), p = genome mean density of the lineage
      (uniform-rate binomial null): Day's "X times more variable than a uniform-rate process" (FM3).
  S2  lag-1 autocorrelation of the S1 Pearson residuals along each chromosome (FM4 clustering).
  S3  heterogeneous-mu residual dispersion: E[n_L] = m p_L rho, rho = (N_O + 1) / (m sum p_L' + 1), N_O = sum_{L' in O(L)} n_L',
      O(H) = {C, G}, O(C) = {H, G}, O(B) = {H, G}, O(G) = {H, C}; variance E (1 + E / N_O) with N_O the
      other-lineage count (estimation noise of rho); phi_res = mean of squared standardised residuals.
  S4  lineage asymmetry H vs C: binomial dispersion of n_H out of n_H + n_C around the genome share q.
  MESA rule (W in {10 kb, 100 kb}; F0 and F2): a dense window has density >= 1.5x the lineage mean AND a
      one-sided Poisson p < 1e-3 under the uniform rate; a mesa is a maximal run of >= 3 consecutive dense
      windows (an unused window breaks the run).  Excess of a mesa = sum (n - m p_L) over its windows.
      Lineage-specific mesa: an H mesa whose C density over the same windows is < 1.1x C's mean (and mirror).
  NULLS (5 replicates each, seed 20261010): U uniform rate n* ~ Poisson(m p_L); M heterogeneous-mu
      n* ~ Poisson(m p_L rho_(-L)) (rho from the other lineages, as in S3).  The mesa rule is run on each.
  FM5 units: MITTENS 3.0 achievable fixations 191 (252,000 / 1,322; parameters.yaml) and Haldane's
      252,000 / 300 = 840 per lineage.  Counted: mesas with excess > 191 and > 840, per lineage.
  FM8b: fraction of genome-wide DHC (F0) that falls in H mesas, and the fraction of H inside H mesas.
  Covariates (100 kb, F2): Spearman of H density with G density, C density, GC fraction, CpG-column fraction,
      (iHG + iCG) density, hh density.

PREDICTIONS (fixed before the run).  Day side = what FM3-FM10 imply; critic side = the audit's steelman of the
critics (refresh 2026-10-10: no critic has replied); A = this audit's numeric expectation.
  P1 FM3 replication: S1 phi (F0, autosomes) for DHC and every lineage reaches >= 80 at some W.
       Day: yes, for the human lineage.  Critics: yes, and for every lineage.  A: phi grows with W roughly as
       1 + m p CV^2; 1 kb 1.5-5, 10 kb 5-40, 100 kb 30-400, 1 Mb 200-4000; phi_H / phi_C in [0.5, 2] at every W.
  P2 FM4: S2 lag-1 autocorrelation > 0.2 at 10 kb (F0) for every lineage (both sides expect clustering);
       A: H and C within 0.1 of each other.
  P3 heterogeneous-mu null (S3): Critics: phi_res(H) <= 0.3 phi(H) at 100 kb (F2) and phi_res(H) / phi_res(C)
       in [0.5, 2].  Day: phi_res(H) stays >> phi_res(C) (ratio > 3).  A: phi_res 1.5-15 at 100 kb, ratio
       0.6-1.6.
  P4 human specificity: S4 phi_HC at 100 kb F2: critics 1-5, Day > 10.  Human-specific / chimp-specific mesa
       count ratio (100 kb, F2): critics [0.5, 2]; Day > 3.  A: 0.6-1.7.
  P5 null reproduction: M-null mesa count / observed (H, 100 kb, F2): critics >= 0.5; Day < 0.2.  U-null: ~0
       mesas (both sides; confirms "uniform rate" is the wrong null).  A: M/obs 0.4-1.2.
  P6 FM5: Day: some H mesa excess > 840 (and > 191).  Critics: yes, and C mesas too; count_C / count_H in
       [0.5, 2].  A: >= 10 H mesas exceed 840 at 100 kb F0; ratio 0.5-2.  (Haldane's and MITTENS' caps bound
       selected substitutions; a neutral excess exceeding them does not test selection: units step.)
  P7 FM8b: Day: H mesas hold > 50% of DHC.  Critics: < 20%.  A: 2-15% (F0, 100 kb).
  P8 covariates: critics: Spearman(H, G) > 0.5 and Spearman(H, C) > 0.6 at 100 kb F2; Day: H mesas do not
       track the other lineages.  A: (H, C) 0.6-0.9; (H, G) 0.5-0.85; (H, GC) and (H, CpG) positive.
  P9 masking: phi(F0) / phi(F2) > 2 at 100 kb for DHC (repeats and duplications inflate dispersion).
  VERDICT MAPPING (proposed, for the reviews): critics' P3-P5 all hold -> FM3/FM4 `supported` as description,
  FM5/FM10 external `contradicted` (no human-specific excess beyond shared mu; Haldane/MITTENS comparison is a
  units step); Day's P3-P5 hold -> FM human-specific excess `supported`, mechanism still open (selection,
  bottleneck and sigillation not discriminated by this check); mixed -> `contested` with the cells named.
  Caveats fixed in advance: parsimony with g and o misassigns some multiple hits (rare at ape distances);
  hg38 agreement removes only part of human polymorphism; CHM13 is one haplotype; no recombination or
  replication-timing map is used (GC, CpG, discordance and hh are the available covariates).
"""
import gzip
import json
import math
import sys
import time

import numpy as np

SP = {"hs1": 0, "hg38": 1, "GCA_028858775.2": 2, "GCA_029289425.2": 3, "GCA_029281585.2": 4,
      "GCA_028885655.2": 5, "GCA_028885625.2": 6, "GCA_028878055.2": 7}
CORE = (0, 1, 2, 3, 4, 5)
FIELDS = ("m", "H", "C", "B", "G", "HCs", "iHG", "iCG", "DHC", "hh", "gc")
NF = len(FIELDS)
BIN = 1000
MITTENS, HALDANE = 191, 840
SEED = 20261010
ACGT = np.zeros(256, bool)
for ch in b"ACGTacgt":
    ACGT[ch] = True


def classify(rows, ref_nongap):
    """rows: dict idx -> uint8 array (block columns, already restricted to hs1 non-gap). Returns field arrays."""
    up = {k: v & 0xDF for k, v in rows.items()}
    h, h2, c, b, g, o = (up[i] for i in CORE)
    core = np.ones(len(h), bool)
    for i in CORE:
        core &= ACGT[rows[i]]
    hh = h == h2
    f = {}
    f["m"] = core
    f["H"] = core & hh & (h != g) & (c == g) & (g == o)
    f["C"] = core & hh & (c != g) & (h == g) & (g == o)
    f["B"] = core & hh & (b != g) & (h == g) & (g == o)
    f["G"] = core & hh & (g != h) & (h == c) & (c == o)
    f["HCs"] = core & hh & (h == c) & (c != g) & (g == o)
    f["iHG"] = core & hh & (h == g) & (h != c) & (c == b) & (b == o)
    f["iCG"] = core & hh & (c == g) & (c != h) & (h == o)
    f["DHC"] = core & (h != c)
    f["hh"] = core & ~hh
    f["gc"] = core & ((h == ord("G")) | (h == ord("C")))
    return f


def cpg_mask(arrs):
    """arrs: list of uint8 (upper-case) arrays on hs1-ungapped columns; CpG if C-G dinucleotide in any."""
    n = len(arrs[0])
    m = np.zeros(n, bool)
    for a in arrs:
        cg = (a[:-1] == ord("C")) & (a[1:] == ord("G"))
        m[:-1] |= cg
        m[1:] |= cg
    return m


def extract(maf, out):
    t0 = time.time()
    data, sizes = {}, {}
    nblk = 0

    def flush(block):
        ref = None
        rows, counts = {}, {}
        for src, start, size, strand, srcsize, seq in block:
            gname = "hs1" if src.startswith("hs1.") else next((g for g in SP if src.startswith(g + ".")), None)
            if gname is None:
                continue
            chrom = src[len(gname) + 1:]
            if gname == "hs1" and ref is None:
                ref = (chrom, start, srcsize, strand, seq)
                continue
            i = SP.get(gname)
            if i is None:
                continue
            counts[i] = counts.get(i, 0) + 1
            if i not in rows:
                rows[i] = seq
        if ref is None:
            return
        chrom, start, srcsize, strand, rseq = ref
        assert strand == "+", "hs1 reference row on minus strand"
        counts[0] = sum(1 for s in block if s[0].startswith("hs1."))
        dup = any(counts.get(i, 0) > 1 for i in CORE)
        r = np.frombuffer(rseq.encode(), np.uint8)
        keep = r != ord("-")
        n = int(keep.sum())
        if n == 0:
            return
        arr = {0: r[keep]}
        for i in range(1, 8):
            if i in rows:
                arr[i] = np.frombuffer(rows[i].encode(), np.uint8)[keep]
            else:
                arr[i] = np.full(n, ord("-"), np.uint8)
        f = classify(arr, keep)
        rep = (arr[0] >= ord("a"))
        cpg = cpg_mask([arr[0] & 0xDF, arr[2] & 0xDF, arr[4] & 0xDF])
        cls = rep.astype(np.int64) + 2 * cpg.astype(np.int64) + 4 * int(dup)
        if chrom not in data:
            nb = srcsize // BIN + 1
            data[chrom] = np.zeros((nb, 8, NF), np.uint32)
            sizes[chrom] = srcsize
        pos = start + np.arange(n)
        bins = pos // BIN
        D = data[chrom]
        b0, b1 = int(bins[0]), int(bins[-1])
        idx = (bins - b0) * 8 + cls
        nn = (b1 - b0 + 1) * 8
        for j, name in enumerate(FIELDS):
            sel = f[name]
            if sel.any():
                D[b0:b1 + 1, :, j] += np.bincount(idx[sel], minlength=nn).reshape(b1 - b0 + 1, 8).astype(np.uint32)

    block = []
    with gzip.open(maf, "rt") as fh:
        for line in fh:
            if line.startswith("s"):
                p = line.split()
                block.append((p[1], int(p[2]), int(p[3]), p[4], int(p[5]), p[6]))
            elif line.startswith("a"):
                if block:
                    flush(block)
                    nblk += 1
                    if nblk % 1000000 == 0:
                        print(f"[{time.time() - t0:7.0f}s] blocks {nblk}", flush=True)
                block = []
        if block:
            flush(block)
            nblk += 1
    np.savez_compressed(out, **{f"chr_{k}": v.astype(np.uint16) for k, v in data.items()},
                        meta=json.dumps(dict(fields=FIELDS, bin=BIN, sizes=sizes, blocks=nblk,
                                             classes="rep + 2*cpg + 4*dup")))
    print(f"extract done: {nblk} blocks, {len(data)} chromosomes, {time.time() - t0:.0f} s", flush=True)


# ------------------------------------------------------------------------------------------------ analysis
FILTERS = {"F0": range(8), "F1": (0, 1, 2, 3), "F2": (0, 2), "F3": (0,)}
WINS = (1, 10, 100, 1000)
LIN = ("H", "C", "B", "G", "DHC")
OTHERS = {"H": ("C", "G"), "C": ("H", "G"), "B": ("H", "G"), "G": ("H", "C")}


def load(npz):
    z = np.load(npz)
    meta = json.loads(str(z["meta"]))
    chroms = [k[4:] for k in z.files if k.startswith("chr_")]
    return z, meta, chroms


def windows(z, chroms, filt, W):
    """Return dict field -> concatenated window arrays, plus chrom id per window, for used windows only."""
    out = {f: [] for f in FIELDS}
    cid, valid = [], []
    for ci, ch in enumerate(chroms):
        a = z["chr_" + ch].astype(np.int64)[:, list(FILTERS[filt]), :].sum(axis=1)   # bins x NF
        nb = a.shape[0] // W
        if nb == 0:
            continue
        a = a[: nb * W].reshape(nb, W, NF).sum(axis=1)
        ok = a[:, 0] >= 0.5 * W * BIN
        for j, f in enumerate(FIELDS):
            out[f].append(a[:, j])
        cid.append(np.full(nb, ci))
        valid.append(ok)
    out = {f: np.concatenate(v) for f, v in out.items()}
    return out, np.concatenate(cid), np.concatenate(valid)


def phi_uniform(n, m):
    p = n.sum() / m.sum()
    e = m * p
    r = (n - e) / np.sqrt(e * (1 - p))
    return float((r ** 2).sum() / (len(n) - 1)), r


def lag1(r, cid):
    same = cid[1:] == cid[:-1]
    a, b = r[:-1][same], r[1:][same]
    return float(np.corrcoef(a, b)[0, 1]) if len(a) > 2 else float("nan")


def het_expect(w, L, ok):
    m = w["m"][ok].astype(float)
    p = {k: w[k][ok].sum() / m.sum() for k in ("H", "C", "B", "G")}
    No = sum(w[k][ok] for k in OTHERS[L]).astype(float)
    rho = (No + 1.0) / (m * sum(p[k] for k in OTHERS[L]) + 1.0)   # one pseudo-count (empty windows)
    E = m * p[L] * rho
    return E, No


def mesas(n, m, cid, ok, pmean):
    """Dense: density >= 1.5x mean and Poisson upper tail p < 1e-3 (normal approx with continuity for large e)."""
    e = m * pmean
    z = (n - e - 0.5) / np.sqrt(np.maximum(e, 1e-9))
    dense = ok & (n >= 1.5 * e) & (z > 3.09)
    runs = []
    i, N = 0, len(n)
    while i < N:
        if dense[i]:
            j = i
            while j + 1 < N and dense[j + 1] and cid[j + 1] == cid[i]:
                j += 1
            if j - i + 1 >= 3:
                runs.append((i, j))
            i = j + 1
        else:
            i += 1
    return runs


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def analyse(npz, outjson):
    z, meta, chroms_all = load(npz)
    auto = [c for c in chroms_all if c.replace("chr", "").isdigit()]
    res = {"grid": {}, "mesa": {}, "cov": {}, "chrX": {}}
    rng = np.random.default_rng(SEED)
    for set_name, chroms in (("auto", auto), ("chrX", [c for c in chroms_all if c == "chrX"])):
        for filt in FILTERS:
            for W in WINS:
                w, cid, ok = windows(z, chroms, filt, W)
                if ok.sum() < 10:
                    continue
                cell = {"k": int(ok.sum())}
                for L in LIN:
                    ph, r = phi_uniform(w[L][ok], w["m"][ok])
                    cell[L] = {"phi": ph, "lag1": lag1(r, cid[ok]), "density": float(w[L][ok].sum() / w["m"][ok].sum())}
                    if L in OTHERS:
                        E, No = het_expect(w, L, ok)
                        rr = (w[L][ok] - E) / np.sqrt(E * (1 + E / np.maximum(No, 1)) + 1e-9)
                        cell[L]["phi_res"] = float((rr ** 2).mean())
                nh, nc = w["H"][ok].astype(float), w["C"][ok].astype(float)
                t = nh + nc
                q = nh.sum() / t.sum()
                s = t > 0
                cell["phi_HC"] = float((((nh[s] - t[s] * q) ** 2) / (t[s] * q * (1 - q))).sum() / (s.sum() - 1))
                key = f"{set_name}|{filt}|{W}kb"
                res["grid" if set_name == "auto" else "chrX"][key] = cell
                print(key, json.dumps({k: (v if not isinstance(v, dict) else {a: round(b, 4) for a, b in v.items()})
                                       for k, v in cell.items()}), flush=True)
                if set_name != "auto" or W not in (10, 100) or filt not in ("F0", "F2"):
                    continue
                # mesas
                mres = {}
                m_ = w["m"].astype(float)
                pm = {L: w[L][ok].sum() / w["m"][ok].sum() for L in ("H", "C", "B", "G")}
                obs = {}
                for L in ("H", "C", "B", "G"):
                    runs = mesas(w[L].astype(float), m_, cid, ok, pm[L])
                    obs[L] = runs
                    ex = [float((w[L][i:j + 1] - m_[i:j + 1] * pm[L]).sum()) for i, j in runs]
                    mres[L] = {"n": len(runs), "bp_kb": int(sum((j - i + 1) * W for i, j in runs)),
                               "frac_lineage_in": float(sum(w[L][i:j + 1].sum() for i, j in runs) / w[L][ok].sum()),
                               "gt_mittens": int(sum(e > MITTENS for e in ex)), "gt_haldane": int(sum(e > HALDANE for e in ex)),
                               "max_excess": max(ex) if ex else 0.0}
                    # nulls
                    E, _ = het_expect(w, L, ok)
                    Efull = np.zeros(len(m_)); Efull[ok] = E
                    nU, nM = [], []
                    for rep in range(5):
                        u = rng.poisson(m_ * pm[L]).astype(float)
                        hm = rng.poisson(Efull).astype(float)
                        nU.append(len(mesas(u, m_, cid, ok, pm[L])))
                        nM.append(len(mesas(hm, m_, cid, ok, pm[L])))
                    mres[L]["null_U"] = nU
                    mres[L]["null_M"] = nM
                # lineage-specific mesas (H vs C)
                for A, Bn in (("H", "C"), ("C", "H")):
                    cnt = 0
                    for i, j in obs[A]:
                        dens = w[Bn][i:j + 1].sum() / max(w["m"][i:j + 1].sum(), 1)
                        cnt += dens < 1.1 * pm[Bn]
                    mres[A][f"specific_vs_{Bn}"] = int(cnt)
                # FM8b
                dhc_in = sum(w["DHC"][i:j + 1].sum() for i, j in obs["H"])
                mres["FM8b_DHC_in_H_mesas"] = float(dhc_in / w["DHC"][ok].sum())
                # overlap: fraction of H-mesa windows inside C mesas, vs C-mesa genome fraction
                inC = np.zeros(len(m_), bool)
                for i, j in obs["C"]:
                    inC[i:j + 1] = True
                hw = np.zeros(len(m_), bool)
                for i, j in obs["H"]:
                    hw[i:j + 1] = True
                mres["H_in_C_frac"] = float(inC[hw].mean()) if hw.any() else float("nan")
                mres["C_genome_frac"] = float(inC[ok].mean())
                res["mesa"][f"{filt}|{W}kb"] = mres
                print("MESA", filt, W, json.dumps(mres), flush=True)
                if filt == "F2" and W == 100:
                    d = {k: w[k][ok] / w["m"][ok] for k in ("H", "C", "G", "gc", "hh")}
                    disc = (w["iHG"][ok] + w["iCG"][ok]) / w["m"][ok]
                    res["cov"] = {"H~C": spearman(d["H"], d["C"]), "H~G": spearman(d["H"], d["G"]),
                                  "H~GC": spearman(d["H"], d["gc"]), "H~disc": spearman(d["H"], disc),
                                  "H~hh": spearman(d["H"], d["hh"])}
                    # CpG-column fraction from F2 classes: cpg class 2 vs 0
                    a0, _, _ = windows_cls(z, chroms, (0,), W)
                    a2, _, _ = windows_cls(z, chroms, (2,), W)
                    frac = a2 / np.maximum(a0 + a2, 1)
                    res["cov"]["H~CpGfrac"] = spearman(d["H"], frac[ok])
                    print("COV", json.dumps(res["cov"]), flush=True)
    json.dump(res, open(outjson, "w"), indent=1)


def windows_cls(z, chroms, classes, W):
    out = []
    for ch in chroms:
        a = z["chr_" + ch].astype(np.int64)[:, list(classes), 0].sum(axis=1)
        nb = a.shape[0] // W
        if nb:
            out.append(a[: nb * W].reshape(nb, W).sum(axis=1))
    return np.concatenate(out), None, None


def selftest():
    import os
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "t.maf.gz")
    #          hs1 vs others; column 3 H-lineage (h=T, others A), column 5 C-lineage, CpG at 7-8
    blk = ("a\ns hs1.chr1 0 10 + 5000 AAATACGGAA\ns hg38.chr1 0 10 + 5000 AAATACGGAA\n"
           "s GCA_028858775.2.c1 0 10 + 9 AAAAAGGGAA\ns GCA_029289425.2.c1 0 10 + 9 AAAAACGGAA\n"
           "s GCA_029281585.2.c1 0 10 + 9 AAAAACGGAA\ns GCA_028885655.2.c1 0 10 + 9 AAAAACGGAA\n\n")
    with gzip.open(p, "wt") as fh:
        fh.write("##maf version=1\n\n" + blk)
    extract(p, os.path.join(d, "t.npz"))
    z = np.load(os.path.join(d, "t.npz"))
    a = z["chr_chr1"].astype(int).sum(axis=1)[0]
    got = dict(zip(FIELDS, a))
    print(got)
    assert got["m"] == 10 and got["H"] == 1 and got["C"] == 1 and got["DHC"] == 2, got
    print("selftest ok")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "extract":
        extract(sys.argv[2], sys.argv[3])
    elif cmd == "analyse":
        analyse(sys.argv[2], sys.argv[3])
    elif cmd == "selftest":
        selftest()
