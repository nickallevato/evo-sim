"""D1 spike -- "alternatives per needed change" in real(ish) sequence spaces.  THROWAWAY research check.

Run:  research/.venv/bin/python -I research/checks/d1_sequence_space_spike.py <part> [--smoke]
      part in: rna | nn | dms | gb1 | summarize | all        (rna and nn are the heavy ViennaRNA parts; run on workhorse)
Outputs (research/checks/results/raw/): d1_rna.json, d1_nn.json, d1_dms.json, d1_gb1.json, d1_summary.txt
Seeds: numpy SeedSequence([20261090, part, config, rep]) -- no hash() seeds.
Dependencies: ViennaRNA (PyPI, version pinned in research/requirements.txt), numpy.  DMS input: ProteinGym v1.3 substitutions
zip + reference file, downloaded to sources/raw/d1-dms/ (gitignored, untrusted: read as CSV only, never executed).

WHAT THIS MEASURES (the quantity G1 left open)
 G1 (R4-G1.md section 3, g1_specific_vs_any.py part B): n_f required functional changes, each satisfiable by any of m
 interchangeable alternatives, each alternative succeeding with probability q.  P_all = (1-(1-q)^m)^n_f = (1-e^-lam)^n_f,
 lam = -m ln(1-q).  The p^n ("specific outcome") product stops binding when lam > lam_50 = ln(n_f/ln2): 7.27 (n_f=1e3),
 9.58 (1e4), 12.33 (157,000), 12.57 (2e5), 17.18 (2e7); band 5%-95% width 4.07.  G1's headline "12-17" is lam_50 for
 n_f = 1.6e5 .. 2e7.  With Day-family inputs (N=1e4, mu=1.2e-8, s=0.01, T=3e5) q = 0.381 so lam_alt = -ln(1-q) = 0.480 per
 alternative, so the flip needs m* = 16 (n_f=1e3) .. 36 (n_f=2e7) alternatives per change; with T=146,250 (Day's d-corrected
 effective generations) q=0.209, lam_alt=0.234, m* = 32..74; at s=0.001 m* = 152..735.  OPEN QUESTION: is the real m per
 needed change above or below that?  This script measures m in two empirical stand-ins (RNA folding; protein DMS).

 DEFINITIONS (fixed here, before any run)
 m_E0 (strict)   = number of distinct single-nucleotide mutants of a genotype x (x folds to S1) whose MFE structure is EXACTLY a
                   named target S2 (S2 != S1).  "Specific outcome" reading.
 m_E1 (medium)   = number of single mutants whose MFE structure is within 2 base-pair differences of S2 (|pairs(S) xor
                   pairs(S2)| <= 2; one slipped/frayed pair).  S2 restricted to d_bp(S1,S2) >= 5 so the class is disjoint
                   from S1's own radius-2 ball.
 m_E2 (lenient)  = number of single mutants whose MFE structure has the same ABSTRACT SHAPE (level-5: helix nesting/branching
                   topology only, bulges/interior loops/unpaired ignored) as S2.  S2 restricted to shape5(S2) != shape5(S1).
                   For the tRNA target the cloverleaf shape is [[][][]].
 m_ben (graded)  = number of single mutants that move the structure strictly closer (bp distance) to a target S*; fitness is
                   -d_bp(structure, S*).  Also reports the fractions equal/worse (Day's "deleterious" = structure further from S*).
 m2_*            = same classes for DOUBLE mutants (all C(L,2)*9 of them) that reach the class while neither single constituent
                   does (so the route genuinely needs both changes).  Needs two arisings: weight by q^2-ish, not q.
 lam             = m * lam_alt (lam_alt per q basis above).  m_pop(K) = distinct mutants in class pooled over K independent
                   sampled neutral genotypes (standing neutral variation); K=1 is the per-genotype number.
 Ruggedness (RNA)= fraction of the 3L single mutants whose structure differs from S1 (strict), is >2 bp from S1 (medium), has
                   a different shape5 (lenient); fraction of (genotype,S*) pairs with NO improving neighbour (strict local
                   optimum in -d_bp); adaptive walks (random improving neighbour, neutral drift allowed up to a budget).
 DMS             = ProteinGym v1.3 single substitutions.  Own normalisation (ProteinGym's DMS_score_bin is a MEDIAN split for 126 of
                   217 sets, so it cannot be used for fractions):  N_hat = median of lowest 5% of singles;  W_hat = median score at
                   the top-quartile-of-sites-by-median-score (WT-like proxy);  s* = (score-N_hat)/(W_hat-N_hat).
                   Functional (lenient) s*>=0.5; near-WT (strict) s*>=0.8; "reduced" s*<0.8; "destroyed" s*<0.2; beneficial
                   PROXY s*>=1.2 (upper bound: measurement noise inflates it).  Per site: number of the 19 alternative residues
                   that are functional (m_aa), and number of functional NONSYNONYMOUS single-nucleotide changes at the codon
                   (m_snv; standard code, averaged over the synonymous codons of the wild-type residue, unmeasured substitutions
                   imputed with the site's measured fraction).  Gene-level m_gene = sum of m_snv over mutated sites.
                   Author-cutoff robustness for the 91 sets with a 'manual' cutoff: fraction with DMS_score_bin==1.
                   GB1 (Wu 2016, four-site complete landscape, WT fitness=1): local maxima, uphill-reachability, functional
                   connected component.

PRE-REGISTERED PREDICTIONS (written before any main run; smoke tests were tiny and their output discarded.  Prior knowledge
of the literature informs these; they are not blind.  Ranges are my 80% bands.)

 What each side's MODEL predicts for alternatives per change (lam vs the 12-17 flip; m vs m* = 16-74 at s=0.01):
  DAY / Eden-Schutzenberger-Wald ruggedness model: functional sequences are isolated, each requirement has m ~ 1 (the specific
     mutation).  lam ~ lam_alt = 0.23-0.48 << 12-17, the p^n barrier binds, and single mutants are mostly deleterious (>= 70%)
     with no usable neutral connectivity.
  CRITIC / Fisher-smooth / percolating-neutral-network model: functional sets are connected, many equivalent routes; m for a
     functionally-equivalent class is at least m* (>= 16-36) so lam > 12; deleterious fraction modest.
 MY EXPECTATION: between the two, and depends sharply on how "equivalent" is defined.  The sequence-space question is
 non-trivially two-sided: strict identity gives Day's m ~ 1; lenient equivalence gives m of order 1-15 per genotype, which is
 still BELOW the flip for s=0.01 unless pooled over standing variation or over genes.

 RNA (ViennaRNA 2.7.2, MFE at 37 C; targets: yeast tRNA-Phe cloverleaf L=76 + random-sequence-derived structures at L=30, 50, 76,
 100, four/four/three/three of them; random targets require >= 0.25 L base pairs and >= 2 helices)
  P1  neutrality: mean per-genotype neutrality nu (fraction of 3L point mutants with unchanged MFE structure) over uniform
      neutral-network samples = 0.25-0.55 for random targets, 0.25-0.50 for tRNA.  Percolation threshold for a 4-letter
      alphabet nu_c = 1-4^(-1/3) = 0.37 (Reidys-Stadler-Schuster; cited from memory, not re-derived): I expect >= 70% of
      targets above it.  Unpaired-site neutrality 0.6-0.9, paired-site neutrality 0.15-0.45 (paired < unpaired).
  P2  neutral-network size |NN| = 6^bp 4^unp * f (f = fold frequency among pair-compatible sequences): tRNA cloverleaf
      10^30 - 10^37 sequences (fraction of 4^76 = 5.7e45: 1e-9 .. 1e-16); random targets: fraction of space 1e-4..1e-1 at L=30,
      falling to 1e-12..1e-5 at L=100.  Every number is huge in absolute terms (>= 1e9 even at L=30).
  P3  alternatives per change, single mutations, one genotype, S2 uniform over distinct accessible structures, conditional on
      m >= 1: m_E0 = 1.0-1.6 (mostly exactly 1); m_E1 = 1.3-3; m_E2 = 2-12 (higher at L >= 76).  Unconditional P(m>=1) per
      (genotype, S2) pair: E0 0.03-0.3, E1 0.1-0.5, E2 0.2-0.8.  Hence lam = m * 0.48 = 0.5-0.8 (E0), 0.6-1.5 (E1), 1-6 (E2):
      BELOW 12-17 for every single-genotype definition; m_E2 below m* = 16-36.  Pooled over K=all sampled (>= 40) neutral
      genotypes, m_pop for E2 reaches 50-400, i.e. ABOVE m* -- but that presupposes >= 40 distinct neutral genotypes
      segregating simultaneously and is a different (population) quantity.
  P4  double mutations: for (genotype, S2) with m1 = 0, P(m2 >= 1) is 0.3-0.9 for E1/E2 and the mean count given >=1 is
      10-300 (E2) -- a factor 10-100 more routes than singles, but each needs two coordinated changes (weight q^2 or
      stepping-stone), so lam_double is not obviously larger than lam_single.
  P5  Day's ruggedness framing in RNA: strict deleterious fraction 1-nu = 0.45-0.75 (the claim "most single changes alter the
      outcome" HOLDS for exact-structure identity); medium (>2 bp from S1) 0.25-0.55; lenient (different shape5) 0.05-0.30
      (the claim FAILS for topology-level function).
  P6  graded fitness (-d_bp to S*): P(a genotype has >= 1 improving neighbour) 0.6-0.95 for accessible near S* (d0 1-10); fraction
      of neighbours improving 1-8%, equal 30-60%, worse 30-65%.  Strict local optima (no improving neighbour) <= 30% of
      pairs.  Adaptive walks with neutral drift reach an accessible S* in >= 85% of runs; to a random 'far' S* in 20-70%.

 DMS (ProteinGym v1.3; survey of all singles-rich sets, split by assay type; headline excludes Stability sets)
  P7  fraction of single substitutions functional (s*>=0.5): median over non-stability datasets 0.45-0.75 (IQR within
      0.3-0.85); near-WT (>=0.8) 0.25-0.55.  "Reduced" (<0.8) 0.45-0.75: Day's wording "reduce or destroy" is
      literally true for a majority in about half of datasets, but "destroyed" (<0.2) is 0.10-0.40 so a majority is destroyed
      in few (<= 15%) datasets.
  P8  sites: fully intolerant (<= 10% of measured substitutions functional) 10-35% of sites; fully tolerant (>= 90%) 10-40%.
  P9  alternatives per needed change: m_aa (of 19, lenient) mean 6-13 per site; m_snv per codon 1.8-4.0 (of ~6.9 nonsynonymous
      SNVs), i.e. lam_site = m_snv * 0.48 = 0.9-1.9 << 12-17 at single-codon granularity;  m_gene (all functional nonsyn
      SNVs in the mutated region) in the hundreds to thousands and m_gene for the beneficial PROXY (s*>=1.2) 5-150 -- the
      same order as m* = 16-74, so at gene granularity the verdict is NOT clear.
  P10 beneficial proxy fraction (s*>=1.2) 0.5-6% of singles (upper bound), compare to G1's required beneficial fraction 2e-5..4e-4
      (n_f <= 2e5) and 2e-3..4e-2 (n_f = 2e7).
  P11 GB1 four-site landscape: > 90% of 149,360 variants nonfunctional (s*<0.3) (Day-favourable); local maxima among variants
      with fitness >= 1 are numerous (>= 30) and a minority (< 50%) of functional variants reach the global maximum by a
      strictly monotone uphill path (ruggedness real in the sign-epistasis sense); the functional set nevertheless has one
      giant connected component holding >= 70% of functional variants (Day's "isolated islands" is false, "rugged" is true).

 DISCLOSURE: before this commit I looked at the GB1 (Wu 2016) score quantiles (min 0, median 0.003, 95th pct 0.31, max 8.8) and
 the first six single-mutant scores, only to fix the WT=1 normalisation.  So the first clause of P11 (>90% of variants
 < 0.3) is NOT a blind prediction; the rest of P11 and all other DMS predictions were written without looking at the data.
 Reference metadata (assay types, cutoff methods) was also looked at.  The RNA smoke runs (tiny, 1-2 targets) printed a
 few numbers (e.g. nu ~ 0.32 at L=30 and L=76) that I saw; P1 was written before them.

 WHAT WOULD CHANGE THE READING: m_E2 per genotype >= 16 at L=30-50 (would put lenient equivalence above the flip);
 m_E0 conditional mean >= 3; RNA strict deleterious fraction < 0.4; DMS destroyed fraction majority in > 30% of datasets or < 3%.
"""
import os, sys, json, time, math, csv, collections, functools, itertools, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool

SEED = 20261090
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DMS_DIR = os.path.join(ROOT, "sources", "raw", "d1-dms")
BASES = "ACGU"
PAIR6 = ["AU", "UA", "GC", "CG", "GU", "UG"]
NPROC = 12
SMOKE = "--smoke" in sys.argv

TRNA_SEQ = "GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA"
TRNA_DB = "(((((((..((((........)))).(((((.......))))).....(((((.......))))))))))))...."

# G1 constants (copied from R4-G1.md; q = 1-exp(-2N(mu/3)T*2s))
Q_BASES = {"T3e5_s0.01": 0.381, "T146250_s0.01": 0.209, "T3e5_s0.001": 0.047, "T146250_s0.001": 0.023}
NF_LIST = [1e3, 1e4, 2e5, 2e7]


def lam_alt(q):
    return -math.log(1 - q)


def lam50(nf):
    return math.log(nf / math.log(2))


def say(*a):
    print(" ".join(str(x) for x in a), flush=True)


# ---------------------------------------------------------------------------------------------- RNA basics
_RNA = None


def rna():
    global _RNA
    if _RNA is None:
        import RNA
        _RNA = RNA
    return _RNA


def fold(seq):
    return rna().fold(seq)[0]


@functools.lru_cache(maxsize=300000)
def pairs_of(db):
    st, out = [], []
    for i, c in enumerate(db):
        if c == "(":
            st.append(i)
        elif c == ")":
            out.append((st.pop(), i))
    return frozenset(out)


def dbp(a, b):
    return len(pairs_of(a) ^ pairs_of(b))


@functools.lru_cache(maxsize=300000)
def shape5(db):
    n = len(db)
    pt = [-1] * n
    st = []
    for i, c in enumerate(db):
        if c == "(":
            st.append(i)
        elif c == ")":
            j = st.pop()
            pt[j] = i
            pt[i] = j

    def top(i, j):
        out, k = [], i
        while k <= j:
            if pt[k] > k:
                out.append(k)
                k = pt[k] + 1
            else:
                k += 1
        return out

    def sh(k):
        cur = k
        kids = top(cur + 1, pt[cur] - 1)
        while len(kids) == 1:
            cur = kids[0]
            kids = top(cur + 1, pt[cur] - 1)
        return "[" + "".join(sh(c) for c in kids) + "]"

    return "".join(sh(k) for k in top(0, n - 1))


def nhelix(db):
    return shape5(db).count("[")


def neighbors(seq):
    out = []
    for i, c in enumerate(seq):
        for b in BASES:
            if b != c:
                out.append(seq[:i] + b + seq[i + 1:])
    return out


def neutral_walk(rng, seq, S1, nprop):
    """Metropolis with symmetric proposals and indicator target => uniform stationary law on the connected neutral set."""
    s = list(seq)
    L = len(s)
    for _ in range(nprop):
        i = int(rng.integers(L))
        old = s[i]
        new = BASES[int(rng.integers(4))]
        if new == old:
            continue
        s[i] = new
        if fold("".join(s)) != S1:
            s[i] = old
    return "".join(s)


def random_seq(rng, L):
    return "".join(BASES[k] for k in rng.integers(0, 4, size=L))


def make_targets(smoke):
    specs = [("tRNA76", 76, TRNA_DB, TRNA_SEQ)]
    plan = [(30, 4), (50, 4), (76, 3), (100, 3)]
    if smoke:
        plan = [(30, 1)]
    for L, cnt in plan:
        for r in range(cnt):
            rng = np.random.default_rng(np.random.SeedSequence([SEED, 0, L, r]))
            while True:
                s = random_seq(rng, L)
                db = fold(s)
                if len(pairs_of(db)) >= 0.25 * L and nhelix(db) >= 2:
                    break
            specs.append((f"rand{L}_{r}", L, db, s))
    if smoke:
        specs = specs[:2]
    return specs


def compat_seq(rng, db):
    pt = {}
    for i, j in pairs_of(db):
        pt[i] = j
    s = [None] * len(db)
    for i in range(len(db)):
        if i in pt:
            p = PAIR6[int(rng.integers(6))]
            s[i], s[pt[i]] = p[0], p[1]
        elif s[i] is None:
            s[i] = BASES[int(rng.integers(4))]
    return "".join(s)


# ---------------------------------------------------------------------------------------------- NN size (chunked)
def nn_chunk(args):
    name, L, db, M, cfg, rep = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 1, cfg, rep]))
    hits = 0
    for _ in range(M):
        if fold(compat_seq(rng, db)) == db:
            hits += 1
    return name, L, db, M, hits


def part_nn(specs, smoke):
    Ms = {30: 400000, 50: 400000, 76: 300000, 100: 200000}
    chunks = 8
    tasks = []
    for ci, (name, L, db, seed) in enumerate(specs):
        M = 2000 if smoke else Ms[L]
        for r in range(chunks if not smoke else 1):
            tasks.append((name, L, db, M // (chunks if not smoke else 1), ci, r))
    tot = collections.defaultdict(lambda: [0, 0])
    meta = {}
    with Pool(NPROC if not smoke else 2) as p:
        for name, L, db, M, hits in p.imap_unordered(nn_chunk, tasks):
            tot[name][0] += M
            tot[name][1] += hits
            meta[name] = (L, db)
    out = {}
    for name, (M, h) in tot.items():
        L, db = meta[name]
        bp = len(pairs_of(db))
        unp = L - 2 * bp
        log10_compat = bp * math.log10(6) + unp * math.log10(4)
        f = h / M
        # Wilson 95% interval on f
        z = 1.96
        den = 1 + z * z / M
        c = (f + z * z / (2 * M)) / den
        hw = z * math.sqrt(f * (1 - f) / M + z * z / (4 * M * M)) / den
        lo, hi = max(c - hw, 1e-300), c + hw
        out[name] = dict(L=L, db=db, bp=bp, unp=unp, M=M, hits=h, f=f, f_lo=lo, f_hi=hi, log10_compat=log10_compat,
                         log10_NN=(log10_compat + math.log10(f)) if h > 0 else None,
                         log10_NN_lo=log10_compat + math.log10(lo), log10_NN_hi=log10_compat + math.log10(hi),
                         log10_frac_space=((log10_compat + math.log10(f)) - L * math.log10(4)) if h > 0 else None)
        say(name, L, "bp", bp, "f", f, "hits", h, "log10NN", out[name]["log10_NN"])
    return out


# ---------------------------------------------------------------------------------------------- per-target RNA analysis
def class_member(cls, st, S2, sh2):
    if cls == "E0":
        return st == S2
    if cls == "E1":
        return dbp(st, S2) <= 2
    return shape5(st) == sh2


def membership(structs, S2s, cls):
    M = np.zeros((len(structs), len(S2s)), dtype=bool)
    for j, S2 in enumerate(S2s):
        sh2 = shape5(S2) if cls == "E2" else None
        for i, st in enumerate(structs):
            M[i, j] = class_member(cls, st, S2, sh2)
    return M


def summarize_counts(m1, ksets):
    """m1: (nB, nP) integer counts."""
    pos = m1[m1 > 0]
    r = dict(reach=float((m1 > 0).mean()), mean_all=float(m1.mean()),
             mean_pos=float(pos.mean()) if pos.size else None,
             median_pos=float(np.median(pos)) if pos.size else None,
             p90_pos=float(np.percentile(pos, 90)) if pos.size else None,
             max=int(m1.max()), n_pairs=int(m1.size))
    for K in ksets:
        pooled = m1[:K].sum(axis=0)
        r[f"mpop{K}_mean"] = float(pooled.mean())
        r[f"mpop{K}_reach"] = float((pooled > 0).mean())
        pp = pooled[pooled > 0]
        r[f"mpop{K}_mean_pos"] = float(pp.mean()) if pp.size else None
    return r


def target_job(job):
    cfgid, name, L, S1, seed_seq, P = job
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 2, cfgid, 0]))
    KA, KB = P["KA"], P["KB"]
    # --- sample the neutral network uniformly
    cur = neutral_walk(rng, seed_seq, S1, 50 * L)
    samples = []
    for _ in range(KA + KB):
        cur = neutral_walk(rng, cur, S1, 10 * L)
        samples.append(cur)
    assert len(set(samples)) == len(samples)
    A, B = samples[:KA], samples[KA:]
    sh1 = shape5(S1)
    pt = np.zeros(L, dtype=bool)
    for i, j in pairs_of(S1):
        pt[i] = pt[j] = True

    def scan(seq):
        muts = neighbors(seq)
        return muts, [fold(m) for m in muts]

    scanA = [scan(x) for x in A]
    scanB = [scan(x) for x in B]
    res = dict(name=name, L=L, S1=S1, shape1=sh1, bp=len(pairs_of(S1)), KA=KA, KB=KB)

    # --- neutrality and "deleterious" fractions (strict / medium / lenient), over all samples
    nus, site_neu_p, site_neu_u, f1, f2, ffar, dchg = [], [], [], [], [], [], []
    for (muts, sts) in scanA + scanB:
        neu = np.array([s == S1 for s in sts])
        nus.append(float(neu.mean()))
        sn = neu.reshape(L, 3).mean(axis=1)
        site_neu_p.append(float(sn[pt].mean()) if pt.any() else float("nan"))
        site_neu_u.append(float(sn[~pt].mean()) if (~pt).any() else float("nan"))
        d = np.array([dbp(s, S1) for s in sts])
        f1.append(float((d > 2).mean()))
        f2.append(float(np.mean([shape5(s) != sh1 for s in sts])))
        ffar.append(float((d > 10).mean()))
        if (~neu).any():
            dchg.append(float(d[~neu].mean()))
    res["nu_mean"] = float(np.mean(nus))
    res["nu_sd"] = float(np.std(nus))
    res["nu_min"] = float(np.min(nus))
    res["frac_samples_nu_gt_0.37"] = float(np.mean(np.array(nus) > 0.37))
    res["site_neu_paired"] = float(np.nanmean(site_neu_p))
    res["site_neu_unpaired"] = float(np.nanmean(site_neu_u))
    res["del_strict"] = 1 - res["nu_mean"]
    res["del_medium_gt2bp"] = float(np.mean(f1))
    res["del_lenient_shape"] = float(np.mean(f2))
    res["del_far_gt10bp"] = float(np.mean(ffar))
    res["mean_dbp_of_changed"] = float(np.mean(dchg)) if dchg else None

    # --- pools of accessible S2 (from A only); evaluate on B
    cnt = collections.Counter()
    for (muts, sts) in scanA:
        for s in sts:
            if s != S1:
                cnt[s] += 1
    distinct = sorted(cnt)
    res["n_distinct_neighbor_structs_A"] = len(distinct)
    npool = P["npool"]
    pools = {}
    for cls in ("E0", "E1", "E2"):
        if cls == "E0":
            cand = distinct
        elif cls == "E1":
            cand = [s for s in distinct if dbp(s, S1) >= 5]
        else:
            cand = [s for s in distinct if shape5(s) != sh1]
        res[f"n_cand_{cls}"] = len(cand)
        if not cand:
            pools[cls] = ([], [])
            continue
        pu = list(rng.choice(len(cand), size=min(npool, len(cand)), replace=False))
        pu = [cand[i] for i in pu]
        w = np.array([cnt[s] for s in cand], dtype=float)
        pf = [cand[i] for i in rng.choice(len(cand), size=npool, replace=True, p=w / w.sum())]
        pools[cls] = (pu, pf)

    regB = {}
    for (muts, sts) in scanB:
        for s in sts:
            regB.setdefault(s, len(regB))
    structsB = list(regB)
    idsB = [np.array([regB[s] for s in sts]) for (muts, sts) in scanB]
    ks = [K for K in (1, 5, 20, KB) if K <= KB]
    ks = sorted(set(ks))
    res["single"] = {}
    for cls in ("E0", "E1", "E2"):
        for kind, S2s in zip(("uniform", "freqw"), pools[cls]):
            if not S2s:
                continue
            Mx = membership(structsB, S2s, cls)
            m1 = np.array([Mx[ids].sum(axis=0) for ids in idsB])
            res["single"][f"{cls}_{kind}"] = summarize_counts(m1, ks)

    # --- graded fitness: -d_bp to S*  (near = accessible S2, far = MFE of random sequence)
    rngf = np.random.default_rng(np.random.SeedSequence([SEED, 3, cfgid, 0]))
    near = pools["E0"][0][:P["nstar"]]
    far = []
    while len(far) < P["nstar"]:
        s = fold(random_seq(rngf, L))
        if s != S1 and dbp(s, S1) > 0:
            far.append(s)
    res["graded"] = {}
    for kind, stars in (("near", near), ("far", far)):
        if not stars:
            continue
        D = np.zeros((len(structsB), len(stars)), dtype=np.int32)
        for j, ss in enumerate(stars):
            for i, st in enumerate(structsB):
                D[i, j] = dbp(st, ss)
        d0 = np.array([dbp(S1, ss) for ss in stars])
        rows = []
        for ids in idsB:
            Dx = D[ids]  # (3L, nstar)
            ben = (Dx < d0[None, :]).sum(axis=0)
            eq = (Dx == d0[None, :]).sum(axis=0)
            wor = (Dx > d0[None, :]).sum(axis=0)
            rows.append((ben, eq, wor))
        ben = np.array([r[0] for r in rows])
        eq = np.array([r[1] for r in rows])
        wor = np.array([r[2] for r in rows])
        bins = {"d0_1-4": (1, 4), "d0_5-10": (5, 10), "d0_11+": (11, 10**9), "all": (0, 10**9)}
        res["graded"][kind] = {}
        for bn, (lo, hi) in bins.items():
            sel = (d0 >= lo) & (d0 <= hi)
            if not sel.any():
                continue
            b, e, w = ben[:, sel], eq[:, sel], wor[:, sel]
            pos = b[b > 0]
            res["graded"][kind][bn] = dict(
                n_star=int(sel.sum()), mean_d0=float(d0[sel].mean()), f_ben=float(b.mean() / (3 * L)),
                f_eq=float(e.mean() / (3 * L)), f_worse=float(w.mean() / (3 * L)), P_any_improver=float((b > 0).mean()),
                strict_local_opt=float((b == 0).mean()), m_ben_mean=float(b.mean()),
                m_ben_mean_pos=float(pos.mean()) if pos.size else None)

    # --- doubles
    ndbl = P["ndbl"]
    res["double"] = {}
    if ndbl:
        acc = {cls: [] for cls in ("E0", "E1", "E2")}
        for xi in range(min(ndbl, KB)):
            x = B[xi]
            muts1, sts1 = scanB[xi]
            sing_ids = {}
            for s in sts1:
                sing_ids.setdefault(s, len(sing_ids))
            sing_list = list(sing_ids)
            sidx = np.array([sing_ids[s] for s in sts1])
            dsts, da, db_ = [], [], []
            for i in range(L):
                for bi in range(3):
                    a = 3 * i + bi
                    ma = muts1[a]
                    for j in range(i + 1, L):
                        for bj in range(3):
                            b = 3 * j + bj
                            mm = ma[:j] + muts1[b][j] + ma[j + 1:]
                            dsts.append(fold(mm))
                            da.append(a)
                            db_.append(b)
            dreg = {}
            for s in dsts:
                dreg.setdefault(s, len(dreg))
            dlist = list(dreg)
            did = np.array([dreg[s] for s in dsts])
            da, db_ = np.array(da), np.array(db_)
            for cls in ("E0", "E1", "E2"):
                S2s = pools[cls][0]
                if not S2s:
                    continue
                Md = membership(dlist, S2s, cls)
                Ms = membership(sing_list, S2s, cls)
                s_in = Ms[sidx]  # (3L, nP)
                m1x = s_in.sum(axis=0)
                need = Md[did] & ~s_in[da] & ~s_in[db_]
                m2 = need.sum(axis=0)
                acc[cls].append((m1x, m2))
        for cls in ("E0", "E1", "E2"):
            if not acc[cls]:
                continue
            m1x = np.concatenate([a for a, b in acc[cls]])
            m2 = np.concatenate([b for a, b in acc[cls]])
            sel = m1x == 0
            m2s = m2[sel]
            pos = m2s[m2s > 0]
            res["double"][cls] = dict(n_pairs=int(m1x.size), frac_m1_zero=float(sel.mean()),
                                      P_m2_pos_given_m1_zero=float((m2s > 0).mean()) if m2s.size else None,
                                      m2_mean_pos=float(pos.mean()) if pos.size else None,
                                      m2_median_pos=float(np.median(pos)) if pos.size else None,
                                      m2_mean_all_given_m1_zero=float(m2s.mean()) if m2s.size else None,
                                      m2_mean_overall=float(m2.mean()), n_double_per_geno=int(L * (L - 1) / 2 * 9))

    # --- adaptive walks
    res["walk"] = {}
    nw = P["nwalk"]
    if nw:
        for kind, stars in (("near", near), ("far", far)):
            outs = []
            for w in range(nw):
                ss = stars[w % len(stars)]
                seq = B[w % KB]
                cur_s = S1
                d = dbp(cur_s, ss)
                d_start = d
                drift = 0
                steps = 0
                reason = "success"
                while d > 0:
                    muts = neighbors(seq)
                    sts = [fold(m) for m in muts]
                    dd = np.array([dbp(s, ss) for s in sts])
                    imp = np.flatnonzero(dd < d)
                    if imp.size:
                        k = int(rng.choice(imp))
                        seq, cur_s, d = muts[k], sts[k], int(dd[k])
                        steps += 1
                        continue
                    eqi = np.flatnonzero(dd == d)
                    if eqi.size and drift < P["drift"]:
                        k = int(rng.choice(eqi))
                        seq, cur_s = muts[k], sts[k]
                        drift += 1
                        steps += 1
                        continue
                    reason = "trapped_no_move" if not eqi.size else "drift_budget"
                    break
                outs.append(dict(d_start=d_start, d_end=d, steps=steps, drift=drift, reason=reason))
            res["walk"][kind] = dict(
                n=len(outs), success=float(np.mean([o["reason"] == "success" for o in outs])),
                trapped_no_move=float(np.mean([o["reason"] == "trapped_no_move" for o in outs])),
                drift_budget=float(np.mean([o["reason"] == "drift_budget" for o in outs])),
                mean_d_start=float(np.mean([o["d_start"] for o in outs])), mean_d_end=float(np.mean([o["d_end"] for o in outs])),
                mean_steps=float(np.mean([o["steps"] for o in outs])))
    res["wall_s"] = time.time() - t0
    say("done", name, "wall", round(res["wall_s"]), "nu", round(res["nu_mean"], 3))
    return res


def part_rna(specs, smoke):
    if smoke:
        P = lambda L: dict(KA=3, KB=4, npool=10, nstar=6, ndbl=1 if L <= 30 else 0, nwalk=2 if L <= 30 else 0, drift=10)
    else:
        def P(L, name=""):
            if L <= 30:
                return dict(KA=40, KB=60, npool=100, nstar=60, ndbl=6, nwalk=30, drift=100)
            if L <= 50:
                return dict(KA=40, KB=60, npool=100, nstar=60, ndbl=6, nwalk=20, drift=100)
            if L <= 76:
                return dict(KA=30, KB=40, npool=100, nstar=40, ndbl=4, nwalk=6 if name == "tRNA76" else 0, drift=60)
            return dict(KA=30, KB=40, npool=100, nstar=40, ndbl=3, nwalk=0, drift=60)
    jobs = []
    for ci, (name, L, db, seed) in enumerate(specs):
        pp = P(L) if smoke else P(L, name)
        jobs.append((ci, name, L, db, seed, pp))
    jobs.sort(key=lambda j: -j[2])
    out = {}
    with Pool(NPROC if not smoke else 2, maxtasksperchild=1) as p:
        for r in p.imap_unordered(target_job, jobs):
            out[r["name"]] = r
    return out


# ---------------------------------------------------------------------------------------------- DMS
CODE = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
AAS = "ACDEFGHIKLMNPQRSTVWY"
_TB = "TCAG"
CODON2AA = {}
for _i, _a in enumerate(_TB):
    for _j, _b in enumerate(_TB):
        for _k, _c in enumerate(_TB):
            CODON2AA[_a + _b + _c] = CODE[16 * _i + 4 * _j + _k]


def snv_table():
    """expected number of single-nt changes from wild-type aa a (uniform over its codons) to aa b; index 20 = stop."""
    tab = np.zeros((20, 21))
    for a_i, a in enumerate(AAS):
        cods = [c for c, x in CODON2AA.items() if x == a]
        for c in cods:
            for p in range(3):
                for n in "TCAG":
                    if n == c[p]:
                        continue
                    b = CODON2AA[c[:p] + n + c[p + 1:]]
                    if b == a:
                        continue
                    tab[a_i, 20 if b == "*" else AAS.index(b)] += 1.0 / len(cods)
    return tab


SNV = snv_table()


def load_dms(path):
    sites, wts, muts, sc, binv = [], [], [], [], []
    with open(path, newline="") as fh:
        rd = csv.DictReader(fh)
        for r in rd:
            m = r["mutant"]
            if ":" in m:
                continue
            wt, mt = m[0], m[-1]
            if wt not in AAS or mt not in AAS:
                continue
            try:
                s = float(r["DMS_score"])
            except ValueError:
                continue
            sites.append(int(m[1:-1]))
            wts.append(wt)
            muts.append(mt)
            sc.append(s)
            binv.append(int(float(r["DMS_score_bin"])) if r.get("DMS_score_bin") not in (None, "") else -1)
    return np.array(sites), np.array(wts), np.array(muts), np.array(sc), np.array(binv)


def dms_one(path, meta):
    sites, wts, muts, sc, binv = load_dms(path)
    if len(sc) < 100:
        return None
    usites = np.unique(sites)
    nsite = len(usites)
    if nsite < 15:
        return None
    sidx = {s: i for i, s in enumerate(usites)}
    si = np.array([sidx[s] for s in sites])
    cover = len(sc) / (19.0 * nsite)
    N_hat = float(np.median(np.sort(sc)[: max(5, int(0.05 * len(sc)))]))
    med = np.array([np.median(sc[si == i]) if (si == i).sum() >= 5 else np.nan for i in range(nsite)])
    ok = ~np.isnan(med)
    if ok.sum() < 8:
        return None
    thr = np.nanpercentile(med, 75)
    top = np.flatnonzero(ok & (med >= thr))
    W_hat = float(np.median(sc[np.isin(si, top)]))
    if W_hat - N_hat < 1e-9:
        return None
    sstar = (sc - N_hat) / (W_hat - N_hat)
    out = dict(n_single=int(len(sc)), n_sites=int(nsite), coverage=float(cover), N_hat=N_hat, W_hat=W_hat,
               assay=meta["coarse_selection_type"], cutoff_method=meta["DMS_binarization_method"], title=meta["title"][:80],
               molecule=meta["molecule_name"][:50], seq_len=int(meta["seq_len"]))
    for nm, th in (("func_0.5", 0.5), ("nearWT_0.8", 0.8), ("ben_proxy_1.2", 1.2)):
        out[f"frac_{nm}"] = float((sstar >= th).mean())
    out["frac_reduced_lt0.8"] = float((sstar < 0.8).mean())
    out["frac_destroyed_lt0.2"] = float((sstar < 0.2).mean())
    out["frac_authorcutoff_bin1"] = float((binv == 1).mean()) if (binv >= 0).all() and meta["DMS_binarization_method"] == "manual" else None
    # per-site
    F = np.full((nsite, 20), np.nan)
    wt_of = {}
    for k in range(len(sc)):
        F[si[k], AAS.index(muts[k])] = sstar[k]
        wt_of[si[k]] = wts[k]
    nmeas = (~np.isnan(F)).sum(axis=1)
    good = nmeas >= 10
    for nm, th in (("func_0.5", 0.5), ("nearWT_0.8", 0.8), ("ben_proxy_1.2", 1.2)):
        fs = np.where(good, np.nansum(F >= th, axis=1) / np.maximum(nmeas, 1), np.nan)
        out[f"site_mean_frac_{nm}"] = float(np.nanmean(fs))
        out[f"m_aa_mean_{nm}"] = float(np.nanmean(fs) * 19)
        if nm == "func_0.5":
            out["site_intolerant_le0.1"] = float(np.nanmean(fs[good] <= 0.1))
            out["site_tolerant_ge0.9"] = float(np.nanmean(fs[good] >= 0.9))
            out["site_hist_deciles"] = [float(x) for x in np.histogram(fs[good], bins=10, range=(0, 1.0000001))[0] / good.sum()]
    # SNV-level
    for nm, th in (("func_0.5", 0.5), ("nearWT_0.8", 0.8), ("ben_proxy_1.2", 1.2)):
        msnv = np.zeros(nsite)
        ntot = np.zeros(nsite)
        for i in range(nsite):
            a = AAS.index(wt_of[i])
            meas = ~np.isnan(F[i])
            fs = (np.nansum(F[i] >= th) / meas.sum()) if meas.sum() else 0.0
            w = SNV[a]
            func_p = np.where(meas, (np.nan_to_num(F[i]) >= th).astype(float), fs)
            msnv[i] = float((w[:20] * func_p).sum())
            ntot[i] = float(w.sum())
        sel = good
        if not sel.any():
            continue
        out[f"m_snv_site_mean_{nm}"] = float(msnv[sel].mean())
        out[f"m_snv_total_per_site"] = float(ntot[sel].mean())
        out[f"m_gene_snv_{nm}"] = float(msnv[sel].sum() * (nsite / max(sel.sum(), 1)))
        out[f"frac_snv_func_{nm}"] = float(msnv[sel].sum() / ntot[sel].sum()) if ntot[sel].sum() > 0 else None
    return out


def part_dms(smoke):
    ref = list(csv.DictReader(open(os.path.join(DMS_DIR, "reference.csv"), newline="")))
    base = os.path.join(DMS_DIR, "x", "DMS_ProteinGym_substitutions")
    out = {}
    for n, r in enumerate(ref):
        if smoke and n >= 4:
            break
        p = os.path.join(base, r["DMS_filename"])
        if not os.path.exists(p):
            continue
        d = dms_one(p, r)
        if d is None:
            say("skip", r["DMS_id"])
            continue
        out[r["DMS_id"]] = d
    say("datasets analysed", len(out))
    return out


def part_gb1(smoke):
    path = os.path.join(DMS_DIR, "x", "DMS_ProteinGym_substitutions", "SPG1_STRSG_Wu_2016.csv")
    rows = []
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            ms = r["mutant"].split(":")
            rows.append(([(int(m[1:-1]), m[-1]) for m in ms], float(r["DMS_score"])))
    pos = sorted({p for muts, _ in rows for p, _ in muts})
    assert len(pos) == 4, pos
    wt = {}
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            for m in r["mutant"].split(":"):
                wt[int(m[1:-1])] = m[0]
    A = np.full((20, 20, 20, 20), np.nan)
    wt_idx = tuple(AAS.index(wt[p]) for p in pos)
    for muts, s in rows:
        idx = list(wt_idx)
        for p, a in muts:
            idx[pos.index(p)] = AAS.index(a)
        A[tuple(idx)] = s
    A[wt_idx] = 1.0  # ASSUMPTION: WT fitness = 1 (Wu 2016 normalises to WT; ProteinGym keeps raw fitness ratios, scores are >= 0 with max 8.8)
    n_all = int((~np.isnan(A)).sum())
    out = dict(positions=pos, wt=[wt[p] for p in pos], n_variants=n_all, n_missing=int(20 ** 4 - n_all))
    X = np.nan_to_num(A, nan=0.0)
    out["frac_lt0.3"] = float((X[~np.isnan(A)] < 0.3).mean())
    out["frac_ge0.5"] = float((X[~np.isnan(A)] >= 0.5).mean())
    out["frac_ge1"] = float((X[~np.isnan(A)] >= 1.0).mean())
    out["frac_ge1.2"] = float((X[~np.isnan(A)] >= 1.2).mean())
    # neighbours along each axis
    def neigh_stats(thr):
        func = (X >= thr) & ~np.isnan(A)
        # improving neighbour with margin (strictly higher by 10% of WT)
        marg = 0.1
        has_up = np.zeros(A.shape, bool)
        nbr_func = np.zeros(A.shape, int)
        for ax in range(4):
            Xm = np.moveaxis(X, ax, 0)
            Fm = np.moveaxis(func, ax, 0)
            Am = np.moveaxis(~np.isnan(A), ax, 0)
            up = np.zeros(Xm.shape, bool)
            nf = np.zeros(Xm.shape, int)
            for a in range(20):
                for b in range(20):
                    if a == b:
                        continue
                    up[a] |= (Xm[b] > Xm[a] + marg) & Am[b] & Am[a]
                    nf[a] += (Fm[b] & Am[a]).astype(int)
            has_up |= np.moveaxis(up, 0, ax)
            nbr_func += np.moveaxis(nf, 0, ax)
        return func, has_up, nbr_func
    thr = 0.5
    func, has_up, nbr_func = neigh_stats(thr)
    present = ~np.isnan(A)
    nfunc = int(func.sum())
    out["n_functional_ge0.5"] = nfunc
    out["local_maxima_among_functional"] = int((func & ~has_up).sum())
    out["frac_functional_with_improving_nbr"] = float((func & has_up).sum() / nfunc)
    out["mean_functional_nbrs_of_functional"] = float(nbr_func[func].mean())  # of 76
    out["frac_functional_isolated_no_functional_nbr"] = float((nbr_func[func] == 0).mean())
    # functional neighbours of WT-neighbourhood: fraction of the 76 single mutants of each functional variant that are functional
    out["frac_nbrs_functional_given_functional"] = float(nbr_func[func].mean() / 76.0)
    # giant component of functional variants (single-substitution adjacency, 4 sites x 19 alternatives)
    sys.setrecursionlimit(10000)
    idxs = np.argwhere(func)
    idmap = {tuple(ix): n for n, ix in enumerate(idxs)}
    parent = list(range(len(idxs)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for n, ix in enumerate(idxs):
        for ax in range(4):
            for b in range(ix[ax] + 1, 20):
                jx = list(ix)
                jx[ax] = b
                m = idmap.get(tuple(jx))
                if m is not None:
                    ra, rb = find(n), find(m)
                    if ra != rb:
                        parent[ra] = rb
    comp = collections.Counter(find(n) for n in range(len(idxs)))
    sizes = sorted(comp.values(), reverse=True)
    out["n_components"] = len(sizes)
    out["largest_component"] = sizes[0]
    out["frac_in_largest_component"] = sizes[0] / nfunc
    big = max(comp, key=comp.get)
    out["wt_in_largest_component"] = bool(find(idmap[wt_idx]) == big)
    # monotone-uphill reachability of the global max: process variants in decreasing fitness; reach[v] = True if v is the max or any
    # strictly-higher neighbour (by margin) reaches the max.  Equivalent to reverse reachability.
    marg = 0.1
    order = np.argsort(-X, axis=None)
    flat = X.reshape(-1)
    pres = present.reshape(-1)
    gmax = int(np.nanargmax(np.where(present, X, -1).reshape(-1)))
    reach = np.zeros(flat.size, bool)
    reach[gmax] = True
    shape = A.shape
    for f in order:
        if not pres[f] or f == gmax:
            continue
        ix = np.unravel_index(f, shape)
        ok = False
        for ax in range(4):
            for b in range(20):
                if b == ix[ax]:
                    continue
                jx = list(ix)
                jx[ax] = b
                g = np.ravel_multi_index(tuple(jx), shape)
                if pres[g] and flat[g] > flat[f] + marg and reach[g]:
                    ok = True
                    break
            if ok:
                break
        reach[f] = ok
    fr = func.reshape(-1)
    out["global_max_fitness"] = float(flat[gmax])
    out["frac_functional_reach_globalmax_uphill"] = float((reach & fr).sum() / fr.sum())
    out["frac_all_functional_ge1_reach"] = float((reach & (flat >= 1.0) & pres).sum() / max(((flat >= 1.0) & pres).sum(), 1))
    # local maxima in the stricter sense, with fitness >= 1
    up_all = has_up.reshape(-1)
    lm1 = (~up_all) & pres & (flat >= 1.0)
    out["local_maxima_fit_ge1"] = int(lm1.sum())
    out["n_fit_ge1"] = int(((flat >= 1.0) & pres).sum())
    # singles from WT: fraction of 76 single mutants functional and beneficial
    singles = []
    for ax in range(4):
        for b in range(20):
            if b == wt_idx[ax]:
                continue
            jx = list(wt_idx)
            jx[ax] = b
            singles.append(A[tuple(jx)])
    singles = np.array(singles)
    singles = singles[~np.isnan(singles)]
    out["wt_singles_n"] = int(len(singles))
    out["wt_singles_frac_ge0.5"] = float((singles >= 0.5).mean())
    out["wt_singles_frac_ge1.2"] = float((singles >= 1.2).mean())
    out["wt_singles_frac_lt0.2"] = float((singles < 0.2).mean())
    return out


# ---------------------------------------------------------------------------------------------- summary
def fmt(x, nd=3):
    if x is None:
        return "-"
    if isinstance(x, float):
        return f"{x:.{nd}g}"
    return str(x)


def part_summarize():
    lines = []
    P = lines.append
    def load(n):
        p = os.path.join(RAW, n.replace(".json", ("_smoke" if SMOKE else "") + ".json"))
        return json.load(open(p)) if os.path.exists(p) else None
    nn, rn, dm, gb = load("d1_nn.json"), load("d1_rna.json"), load("d1_dms.json"), load("d1_gb1.json")
    P("== lambda bookkeeping (G1): flip lam_50 by n_f and lam_alt by q basis")
    P("lam50: " + ", ".join(f"n_f={nf:g}: {lam50(nf):.2f}" for nf in NF_LIST))
    P("lam_alt: " + ", ".join(f"{k}: q={q} lam_alt={lam_alt(q):.3f} m*(1e3..2e7)={lam50(1e3)/lam_alt(q):.0f}..{lam50(2e7)/lam_alt(q):.0f}" for k, q in Q_BASES.items()))
    if nn:
        P("\n== NN size")
        P("name L bp f hits log10|NN| [95% lo,hi] log10 frac of 4^L")
        for k, v in sorted(nn.items(), key=lambda kv: (kv[1]["L"], kv[0])):
            P(f"{k} L={v['L']} bp={v['bp']} f={v['f']:.3g} hits={v['hits']}/{v['M']} log10NN={fmt(v['log10_NN'])} [{v['log10_NN_lo']:.1f},{v['log10_NN_hi']:.1f}] log10frac={fmt(v['log10_frac_space'])}")
    if rn:
        P("\n== neutrality / ruggedness (per target)")
        P("name L nu nu_sd nu_min fracNu>.37 paired unpaired | del_strict del_>2bp del_shape del_>10bp")
        for k, v in sorted(rn.items(), key=lambda kv: (kv[1]["L"], kv[0])):
            P(f"{k} L={v['L']} nu={v['nu_mean']:.3f} sd={v['nu_sd']:.3f} min={v['nu_min']:.3f} fr>.37={v['frac_samples_nu_gt_0.37']:.2f} "
              f"paired={v['site_neu_paired']:.3f} unpaired={v['site_neu_unpaired']:.3f} | {v['del_strict']:.3f} {v['del_medium_gt2bp']:.3f} {v['del_lenient_shape']:.3f} {v['del_far_gt10bp']:.3f}")
        P("\n== single-mutation alternatives per change (genotype-level K=1; pooled K)")
        for cls in ("E0", "E1", "E2"):
            for kind in ("uniform", "freqw"):
                P(f"-- {cls} {kind}: reach, mean_all, mean_pos, median_pos, p90_pos, | mpop5 mean, mpop{{KB}} mean | lam@0.48(mean_pos)")
                for k, v in sorted(rn.items(), key=lambda kv: (kv[1]["L"], kv[0])):
                    s = v["single"].get(f"{cls}_{kind}")
                    if not s:
                        continue
                    kbk = [kk for kk in s if kk.startswith("mpop") and kk.endswith("_mean") and kk not in ("mpop1_mean", "mpop5_mean", "mpop20_mean")]
                    kb = s[kbk[0]] if kbk else None
                    mp = s["mean_pos"]
                    P(f"{k} L={v['L']} reach={s['reach']:.3f} mean_all={s['mean_all']:.3f} mean_pos={fmt(mp)} med_pos={fmt(s['median_pos'])} p90={fmt(s['p90_pos'])} max={s['max']} | mpop5={fmt(s.get('mpop5_mean'))} mpopKB={fmt(kb)} | lam={fmt(mp*0.48 if mp else None)}")
        P("\n== doubles (requiring both): P(m2>=1|m1=0), m2 mean|pos, m2 median|pos")
        for k, v in sorted(rn.items(), key=lambda kv: (kv[1]["L"], kv[0])):
            for cls, s in v.get("double", {}).items():
                P(f"{k} L={v['L']} {cls} frac_m1_zero={s['frac_m1_zero']:.3f} P(m2>0|m1=0)={fmt(s['P_m2_pos_given_m1_zero'])} m2_mean_pos={fmt(s['m2_mean_pos'])} med={fmt(s['m2_median_pos'])} ndbl_per_geno={s['n_double_per_geno']}")
        P("\n== graded fitness (-d_bp to S*)")
        for k, v in sorted(rn.items(), key=lambda kv: (kv[1]["L"], kv[0])):
            for kind, bins in v.get("graded", {}).items():
                for bn, s in bins.items():
                    P(f"{k} L={v['L']} {kind} {bn} n_star={s['n_star']} d0={s['mean_d0']:.1f} f_ben={s['f_ben']:.3f} f_eq={s['f_eq']:.3f} f_worse={s['f_worse']:.3f} P_any_improver={s['P_any_improver']:.3f} local_opt={s['strict_local_opt']:.3f} m_ben_mean={s['m_ben_mean']:.2f}")
        P("\n== adaptive walks")
        for k, v in sorted(rn.items(), key=lambda kv: (kv[1]["L"], kv[0])):
            for kind, s in v.get("walk", {}).items():
                P(f"{k} L={v['L']} {kind} n={s['n']} success={s['success']:.2f} trapped={s['trapped_no_move']:.2f} budget={s['drift_budget']:.2f} d_start={s['mean_d_start']:.1f} d_end={s['mean_d_end']:.1f} steps={s['mean_steps']:.1f}")
    if dm:
        P("\n== DMS survey")
        by = collections.defaultdict(list)
        for k, v in dm.items():
            by[v["assay"]].append(v)
            by["ALL"].append(v)
            if v["assay"] != "Stability":
                by["NON-STABILITY"].append(v)
        keys = ["frac_func_0.5", "frac_nearWT_0.8", "frac_reduced_lt0.8", "frac_destroyed_lt0.2", "frac_ben_proxy_1.2",
                "site_intolerant_le0.1", "site_tolerant_ge0.9", "m_aa_mean_func_0.5", "m_snv_site_mean_func_0.5",
                "m_snv_total_per_site", "frac_snv_func_func_0.5", "m_gene_snv_func_0.5", "m_gene_snv_nearWT_0.8", "m_gene_snv_ben_proxy_1.2",
                "m_snv_site_mean_ben_proxy_1.2", "coverage", "n_sites"]
        for g in ["NON-STABILITY", "Stability", "ALL", "OrganismalFitness", "Activity", "Binding", "Expression"]:
            vs = by.get(g, [])
            if not vs:
                continue
            P(f"-- group {g} (n={len(vs)}): median [q25, q75] (min..max)")
            for kk in keys:
                a = np.array([x[kk] for x in vs if x.get(kk) is not None], float)
                if a.size:
                    P(f"   {kk}: {np.median(a):.3g} [{np.percentile(a,25):.3g}, {np.percentile(a,75):.3g}] ({a.min():.3g}..{a.max():.3g})")
            P("   majority-reduced(<0.8) datasets: " + f"{np.mean([x['frac_reduced_lt0.8']>0.5 for x in vs]):.2f}" +
              "; majority-destroyed(<0.2): " + f"{np.mean([x['frac_destroyed_lt0.2']>0.5 for x in vs]):.2f}")
            man = [x["frac_authorcutoff_bin1"] for x in vs if x.get("frac_authorcutoff_bin1") is not None]
            if man:
                P(f"   author-cutoff (manual) fraction fit: median {np.median(man):.3g} [{np.percentile(man,25):.3g}, {np.percentile(man,75):.3g}] n={len(man)}")
        P("-- named cases")
        for k, v in dm.items():
            if k.startswith("BLAT_ECOLX") or k.startswith("SPG1_STRSG"):
                P(f"   {k}: " + ", ".join(f"{kk}={fmt(v.get(kk))}" for kk in keys))
    if gb:
        P("\n== GB1 four-site landscape")
        for k, v in gb.items():
            P(f"   {k}: {v}")
    # lam table from medians
    txt = "\n".join(lines)
    with open(os.path.join(RAW, "d1_summary.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


def jdump(obj, name):
    with open(os.path.join(RAW, name), "w") as fh:
        json.dump(obj, fh, indent=1, default=float)


def main():
    part = [a for a in sys.argv[1:] if not a.startswith("--")]
    part = part[0] if part else "all"
    os.makedirs(RAW, exist_ok=True)
    tag = "_smoke" if SMOKE else ""
    t0 = time.time()
    if part in ("nn", "all"):
        specs = make_targets(SMOKE)
        jdump(part_nn(specs, SMOKE), f"d1_nn{tag}.json")
    if part in ("rna", "all"):
        specs = make_targets(SMOKE)
        jdump(part_rna(specs, SMOKE), f"d1_rna{tag}.json")
    if part in ("dms", "all"):
        jdump(part_dms(SMOKE), f"d1_dms{tag}.json")
    if part in ("gb1", "all") and not SMOKE:
        jdump(part_gb1(SMOKE), "d1_gb1.json")
    if part == "summarize":
        part_summarize()
    say("total wall", round(time.time() - t0), "s")


if __name__ == "__main__":
    main()
