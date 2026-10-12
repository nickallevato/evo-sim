"""R4-GAP05: how many slightly deleterious nonsynonymous mutations does a drift account fix on the human lineage, and at what cost?

Run: research/.venv/bin/python -I research/checks/gap05_slightly_deleterious.py     (local: 1 process, numpy only, <10 s)
Tier: low-stakes (GAP-05 is not a hierarchy node; B9 load_bearing false) -> one combined review.

DISCLOSURE (pre-registration honesty): the DFE bin shares below were already summarised in chat before this script was
written (|s|<1e-4: 28-33%; 1e-4..1e-3: 15-17%; >=1e-3: 50-57%). The predictions below are therefore NOT blind to the DFE
shares; they are blind to the Kimura integration, the counts, the cost and the dN/dS comparison.

INPUTS (all sourced; refresh-2026-10-11b-lit.md, quotes-literature.md)
  Kim, Huber & Lohmueller 2017 Table 3, new nonsynonymous mutations by |s| (rescaled to N = 10,000), bins
    0-1e-5, 1e-5..1e-4, 1e-4..1e-3, 1e-3..1e-2, >1e-2:
    Boyko row    0.183 0.096 0.147 0.219 0.355
    1000G gamma  0.217 0.112 0.169 0.243 0.259
  mu = 1.2e-8 per site per gen (parameters.yaml pedigree_human; range 1.1e-8..1.5e-8). T = 252,000 gens (Day; parameters.yaml).
  Nonsynonymous sites N = 27,789,507.5 per haploid genome (R4-L1 raw/l1_dnds.json, V0 ALL, Nei-Gojobori, one canonical
    transcript per gene; repo-derived, NOT an independent source; undercounts alternative isoforms). Observed nonsyn
    differences Nd = 129,479.2 (human + chimp lineages together) -> ~64,700 per lineage.  Observed dN/dS 0.21-0.27 (R4-L1).
  Ne in {1e4, 2e4, 57143 (Day's HL-implied, parameters.yaml day_b1d_implied-style; 228000/4 = 57,000 gens relation)}; h = 0.5.
  Kimura (genic): u(s,N) = (1 - e^{-2s}) / (1 - e^{-4Ns}), s = heterozygote effect (copied from hf_followups.kimura_u,
    validated there against per-site WF, HF-d). Relative fixation f = 2N u(-s) (neutral = 1).
  Reading A (primary): Kim's |s| is the heterozygote effect; a fixation costs 2|s| log-fitness (homozygous).
  Reading B: Kim's |s| is the homozygote effect; heterozygote s/2; a fixation costs |s|.
  Within-bin |s| shapes: bin 0-1e-5 uniform in s (alt: log-uniform 1e-7..1e-5); 1e-5..1e-3 log-uniform; 1e-3..1e-2 log-uniform;
    >1e-2 log-uniform 1e-2..1 (fixation ~0).  Bin edges are those in Kim's Table 3; the within-bin shape is the audit's assumption.
  Per bin: n_b = share_b * mu * Nsites * T * f_b (expected deleterious nonsynonymous fixations on ONE lineage);
    cost_b = n_b * c (c = 2s or s); total log-fitness decline = sum_b (multiplicative, no compensation, no back mutation,
    no epistasis; = Day-side 'S1' upper-end scenario for coding sites). Predicted dN/dS = sum_b share_b f_b (no positive selection).
  Noncoding: NO sourced DFE with an Ns~1 share was found. Constrained noncoding sites = 0.082 x 3.1e9 - (N+S coding sites
    36.1e6) (Rands 2014 8.2%, range 7.1-9.2%). SENSITIVITY ONLY: a fraction q in {0, 0.05, 0.15, 0.30} of constrained noncoding
    mutations is assumed to have the Boyko-row |s| 1e-5..1e-3 conditional distribution. Labelled bracket, not an estimate.

PRE-REGISTERED PREDICTIONS (written before the main run)
  Day side (GAP-05 as the B9/Hossjer best point): drift fixes enough slightly deleterious mutations to imply a large fitness
    decline.  DB1 coding-only uncompensated log-fitness decline >= 0.05 (>= ~5%) at Ne = 1e4 in both DFE rows and both readings.
    DB2 >= 1.1 (ln 3, 'more than R = 3 absorbs', HF-d threshold) at Ne = 1e4 or at Day's 57,143 in some row/reading (meltdown).
    DB3 deleterious fixations with |s|>=1e-4 number >= 1,000 per lineage.
  Critic side: the count is modest, the cost is small or compensated, and the DFE reproduces observed dN/dS.
    CB1 predicted dN/dS (Ne = 1e4) inside 0.16-0.34 (observed range 0.21-0.27 +/- 25%) in both rows.
    CB2 total deleterious fixations < 50% of the neutral-equivalent count mu*Nsites*T (i.e. most of the nonsyn flux is purged).
    CB3 coding-only uncompensated decline < 1.1 (below ln 3) at Ne = 1e4 and 2e4, both rows/readings.
  Audit point predictions (numeric; before running): predicted dN/dS 0.17-0.30 at Ne = 1e4; deleterious nonsyn fixations
    11,000-26,000 per lineage (neutral-equivalent 84,000); coding log-fitness decline 0.3-1.5 (Reading A), half that in
    Reading B; Ne = 5.7e4 gives lower counts and lower cost than 1e4 (stronger selection); noncoding bracket is large
    (q = 0.15 adds order of the coding cost or more because of the 6x larger target) and is not resolvable without a sourced DFE.
  Verdict moves (conditional on outcome; proposals, not integration):
    B9 external (scoped) stays 'contradicted' on its extinction-within-centuries wording regardless; GAP-05's premise
      'slightly deleterious fixations accumulate' moves to 'supported (counts), compensation untestable here'; Day's best
      point is credited if DB1 holds and CB1 holds (the DFE both reproduces dN/dS AND implies a non-trivial uncompensated cost).
    HF open item GAP-05: 'open' -> 'computed, DFE-sourced, coding only; noncoding unsourced'.
    Any GAP-05-linked claim found by grep: H5/HO-11 premise (fitness declines) gets a numeric anchor; claim verdicts unchanged.
"""
import numpy as np

BINS = [(0.0, 1e-5), (1e-5, 1e-4), (1e-4, 1e-3), (1e-3, 1e-2), (1e-2, 1.0)]
ROWS = {"Boyko": [0.183, 0.096, 0.147, 0.219, 0.355],
        "1000G-gamma": [0.217, 0.112, 0.169, 0.243, 0.259]}
MU, MU_RANGE = 1.2e-8, (1.1e-8, 1.5e-8)
T = 252000
NSITES = 27789507.5
ND_OBS_LINEAGE = 129479.16666666667 / 2
NE_LIST = (1e4, 2e4, 57143.0)
CODING_ALL_SITES = 8311550.5 + 27789507.5
G = 3.1e9


def kimura_u(s, N):
    s = np.asarray(s, float)
    x = 4 * N * s
    out = np.empty_like(s)
    small = np.abs(x) < 1e-8
    out[small] = 1 / (2 * N)
    out[~small] = -np.expm1(-2 * s[~small]) / -np.expm1(-x[~small])
    return out


def grid(b, alt=False, n=4000):
    lo, hi = BINS[b]
    if b == 0:
        return np.logspace(-7, -5, n) if alt else (np.arange(n) + 0.5) / n * hi
    return np.exp(np.log(lo) + (np.arange(n) + 0.5) / n * (np.log(hi) - np.log(lo)))


def per_bin(Ne, reading, alt=False):
    """returns arrays: mean relative fixation f_b, mean cost per fixation c_b (log-fitness), mean |s|."""
    f, c = [], []
    for b in range(5):
        s = grid(b, alt)
        sh = s if reading == "A" else s / 2
        fb = 2 * Ne * kimura_u(-sh, Ne)
        cb = 2 * sh                       # A: 2s ; B: s
        # cost per fixation weighted by fixation probability
        f.append(float(fb.mean())); c.append(float((fb * cb).mean() / fb.mean()) if fb.mean() > 0 else 0.0)
    return np.array(f), np.array(c)


def main():
    # validation: Kimura limits
    chk = [(kimura_u(np.array([0.0]), 1e4)[0] * 2e4, 1.0),
           (2e4 * kimura_u(np.array([-1e-4]), 1e4)[0], None)]
    print("# R4-GAP05 output (pre-registered script)")
    print(f"neutral-equivalent nonsyn mutations per lineage = mu*Nsites*T = {MU*NSITES*T:,.0f}; observed Nd/2 = {ND_OBS_LINEAGE:,.0f}")
    print(f"check: 2N u(0) = {chk[0][0]:.6f} (expect 1); 2N u(-s) at 2Ns=-2 (s=1e-4,N=1e4) = {chk[1][0]:.4f} (analytic x/(e^x-1)-type, x=4Ns=4: ~0.0745 for small s)")
    results = {}
    for reading in ("A", "B"):
        print(f"\n## Reading {reading}: " + ("Kim |s| = heterozygote effect, cost 2s per fixation" if reading == "A" else "Kim |s| = homozygote effect, heterozygote s/2, cost s per fixation"))
        print("| DFE row | Ne | dN/dS pred | del. fixations (nonsyn, 1 lineage) | of which |s|>=1e-4 | of which |s|<1e-4 | log-fitness decline | fitness ratio exp(-decline) | per-gen decline |")
        print("|---|---|---|---|---|---|---|---|---|")
        for row, sh in ROWS.items():
            sh = np.array(sh)
            for Ne in NE_LIST:
                f, c = per_bin(Ne, reading)
                nb = sh * MU * NSITES * T * f
                cost = float((nb * c).sum())
                dnds = float((sh * f).sum())
                big = float(nb[2:].sum()); small = float(nb[:2].sum())
                results[(reading, row, Ne)] = (dnds, nb, c, cost)
                print(f"| {row} | {Ne:g} | {dnds:.3f} | {nb.sum():,.0f} | {big:,.0f} | {small:,.0f} | {cost:.3f} | {np.exp(-cost):.3f} | {cost/T:.2e} |")
    print("\n## Per-bin detail, Reading A, Ne = 1e4")
    print("| DFE row | bin | share | mean f=2Nu | fixations | mean cost/fix | cost |")
    print("|---|---|---|---|---|---|---|")
    for row in ROWS:
        dnds, nb, c, cost = results[("A", row, 1e4)]
        for b in range(5):
            print(f"| {row} | {BINS[b][0]:g}-{BINS[b][1]:g} | {ROWS[row][b]} | {nb[b]/(ROWS[row][b]*MU*NSITES*T):.4f} | {nb[b]:,.0f} | {c[b]:.2e} | {nb[b]*c[b]:.4f} |")
    print("\n## Sensitivity: mu range and bin-0 shape (Reading A, Ne = 1e4)")
    for row, sh in ROWS.items():
        sh = np.array(sh)
        for mu in MU_RANGE:
            f, c = per_bin(1e4, "A")
            nb = sh * mu * NSITES * T * f
            print(f"  {row} mu={mu:g}: fixations {nb.sum():,.0f}, decline {(nb*c).sum():.3f}")
        f, c = per_bin(1e4, "A", alt=True)
        nb = sh * MU * NSITES * T * f
        print(f"  {row} bin-0 log-uniform 1e-7..1e-5: fixations {nb.sum():,.0f}, decline {(nb*c).sum():.3f}, dN/dS {(sh*f).sum():.3f}")
    # with positive selection: adds? report nothing (no sourced beneficial DFE) -- observed dN/dS also includes adaptive fixations
    print("\n## Noncoding SENSITIVITY (unsourced DFE; bracket only)")
    f, c = per_bin(1e4, "A")
    sh = np.array(ROWS["Boyko"])
    w = sh[1:3] / sh[1:3].sum()                     # Boyko 1e-5..1e-3 conditional
    fmid = float((w * f[1:3]).sum())
    cmid = float((w * f[1:3] * c[1:3]).sum() / (w * f[1:3]).sum())
    print(f"conditional |s| 1e-5..1e-3 (Boyko weights): mean f = {fmid:.3f}, cost/fixation = {cmid:.2e} (Reading A, Ne 1e4)")
    for pct, lab in ((0.082, "8.2%"), (0.071, "7.1%"), (0.092, "9.2%")):
        Lnc = pct * G - CODING_ALL_SITES
        print(f"constrained {lab}: noncoding constrained sites = {Lnc:.3e}")
        for q in (0.0, 0.05, 0.15, 0.30):
            n = Lnc * MU * T * q * fmid
            print(f"   q={q:.2f}: fixations {n:,.0f}, added log-fitness decline {n*cmid:.3f}")
    # scoring
    print("\n## Pre-registered band scoring")
    A1 = [results[("A", r, 1e4)] for r in ROWS]; B1 = [results[("B", r, 1e4)] for r in ROWS]
    print("DB1 decline >=0.05 at Ne 1e4, both rows, both readings:", all(x[3] >= 0.05 for x in A1 + B1), [round(x[3], 3) for x in A1 + B1])
    anyln3 = [(k, round(v[3], 3)) for k, v in results.items() if k[2] in (1e4, 57143.0) and v[3] >= 1.0986]
    print("DB2 any >= ln 3 at Ne 1e4 or 57,143:", bool(anyln3), anyln3)
    db3 = [round(float(results[("A", r, 1e4)][1][2:].sum())) for r in ROWS]
    print("DB3 fixations |s|>=1e-4 >= 1000 (A, Ne 1e4):", all(x >= 1000 for x in db3), db3)
    print("CB1 dN/dS in 0.16-0.34 at Ne 1e4 (A and B):", [round(results[(rd, r, 1e4)][0], 3) for rd in 'AB' for r in ROWS],
          all(0.16 <= results[(rd, r, 1e4)][0] <= 0.34 for rd in 'AB' for r in ROWS))
    print("CB2 total del. fixations < 50% of neutral-equivalent (A, Ne 1e4):",
          [round(float(results[("A", r, 1e4)][1].sum() / (MU * NSITES * T)), 3) for r in ROWS])
    print("CB3 decline < ln 3 at Ne 1e4, 2e4 all rows/readings:",
          all(results[(rd, r, ne)][3] < 1.0986 for rd in 'AB' for r in ROWS for ne in (1e4, 2e4)))
    print("Audit point: dN/dS 0.17-0.30 (A, Ne 1e4):", [round(results[("A", r, 1e4)][0], 3) for r in ROWS])


if __name__ == "__main__":
    main()
