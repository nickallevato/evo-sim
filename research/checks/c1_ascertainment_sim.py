"""C1 / C1a / C6 -- aDNA 1240k panel ascertainment and the "630 expected vs 21 observed" denominator.

THROWAWAY research check. Run:  research/.venv/bin/python -I research/checks/c1_ascertainment_sim.py
Method: neutral Wright-Fisher (WF) dynamics evaluated with the EXACT WF Markov chain (Rao-Blackwellised over
sites; no sampling error), at a scaled population (N_s = 1000 diploids, mutation and time rescaled by f = Ne/N_s,
theta = 4 Ne mu held fixed).  Scaling is validated three ways (N_s = 500/2000; unscaled N = 1e4 Monte Carlo; an
independent forward-simulation of the whole two-population ascertainment pipeline).  Seeds fixed (20261009).

PRE-REGISTERED PREDICTIONS (copied from docs/research/claims/C-, C1-, C1a-, C6-*.md before any run; [R4] items
were written by this check before the first run):
  C1 (critic): (a) new-mutation substitutions in a 350-generation window are registered on panel sites at far below
       the genome-wide rate (order 0-5 per 1.14M sites under uniform sampling, probably less because new mutations
       are not in the discovery set); (b) for standing variants, neutral completions from a 50-90% start are ~0 at
       Ne ~ 1e4, so the observed 1 and 3 are noise or admixture.
  C1a (Day): ascertainment on present-day polymorphism raises the chance of seeing an intermediate-to-fixed
       transition, so near-zero is not a design artefact.  Result that moves C1 toward C1a: ascertained-panel
       completions from intermediate starts exceed the unascertained rate.
  C (claim file): both models predict ~0 for the headline statistic (completions from <50% start; 1 and 3 from
       50-90% are anomalies).  Day's modern-synthesis comparator: 15,556 genome-wide (not scaled to the panel).
  C6: 630 = 1.2e-8 x 1.5e8 x 350 is a genome-wide (150M site) number; on the 1,233,013-SNP panel uniform scaling
       gives 5.2; 21 observed is then above, not below, the expectation.  Changes verdict: a panel-registered
       expected count well above 21 (supports Day's deficit) or at or below 21 (removes it).
  [R4] pre-run predictions:
   P1  flux check: unascertained derived-allele fixations over G generations per site = mu*G (to ~2%).
   P2  new-in-window mutations contribute ~0 (<1e-6 of the flux): essentially ALL mu*G "fixations" are completions
       of standing variation that was already polymorphic (mostly >90% frequency) at the window start.
   P3  design D1 (discovery = MAF >= 5% in 2,345 present-day diploids of the SAME population): panel contains no
       truly fixed sites and no allele with modern frequency > 95% => ~0 completions by construction;
       50-90% band << 0.1 per 1.14M.
   P4  design D2 (Human-Origins style: site heterozygous in one African male; Haak 2015) keeps near-fixed European
       alleles with probability ~2y(1-y) and so does NOT remove completions; expected counts on the 1.14M panel are
       of order 1e2-1e5 for sample-level "newly 100%" events (observed: 17,806 / 3,469), so the observed stasis in
       the >=90% bands is neutral-compatible; the 50-90% band expectation is <~0.1-1 (observed 1 and 3).
   P5  enrichment: for D2, P(event | included) is within a factor ~0.5-3 of P(event | any polymorphic site); for D1
       it is << 1.  I.e. C1a's sign claim holds at most weakly for African-discovery designs and fails for
       same-population MAF thresholds.
   P6  C6 denominator: uniform scaling of 630 to the panel gives 5.2, but the panel is not a uniform sample (it is
       enriched for polymorphic sites), so the right comparison is the model-specific panel expectation (P4).
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import wf_b3c1 as w

SEED = 20261009
MU = 1.2e-8          # parameters.yaml mutation.mu_per_site_per_gen.pedigree_human (Kong 2012)
NE = 1.0e4           # parameters.yaml population.Ne_modern_human (textbook; unverified); keruru temporal 8.1k-9.8k (C5b)
EDGES = [0.0, 0.1, 0.5, 0.9, 0.99, 1.0]
BAND_NAMES = ["<10%", "10-50%", "50-90%", "90-99%", ">=99%"]
NPANEL = 1_143_671     # Z23046531 autosomal SNPs analysed (v62)
NPANEL_AADR = 1_233_013
SPLIT = 2000           # ASSUMED African-European split in generations (~50 ky); not in parameters.yaml


def analyse(Ne, G, split, Ns, n0, nm, mu=MU, nd_eur=2345, nd_afr=100, thr_eur=0.05):
    f = Ne / Ns
    M = 2 * Ns
    Gs = int(round(G / f))
    split_s = int(round(split / f))
    neo_s = split_s - Gs
    theta = 4 * Ne * mu
    P = w.wf_matrix(M)
    P_G = w.mat_pow(P, Gs)
    P_A = w.mat_pow(P, split_s)
    P_neo = w.mat_pow(P, neo_s)
    yv = np.arange(M + 1) / M
    i = np.arange(1, M)
    wt = theta / i                         # equilibrium SFS: expected sites per genome site with i copies
    Bd, Ba = w.band_matrix(M, n0, EDGES)
    pd, pa = yv ** (2 * nm), (1 - yv) ** (2 * nm)

    def Cev(Iy):
        md = P_G @ (pd * Iy)
        ma = P_G @ (pa * Iy)
        return Bd * md[:, None] + Ba * ma[:, None]

    one = np.ones(M + 1)
    ev0 = Cev(one)
    out = dict(Gs=Gs, f=f, Geff=Gs * f, split_s=split_s, M=M)
    # flux checks (P1, P2)
    out["flux_derived_fix"] = float(wt @ P_G[1:M, M])
    out["mu_G"] = mu * Gs * f
    # new-in-window mutations that fix inside window (expected per site): sum over birth times
    v = np.zeros(M + 1)
    v[1] = 1
    tot = 0.0
    for t in range(Gs):
        v = v @ P
        tot += (2 * Ns * mu * f) * v[M]
    out["new_in_window_fix"] = tot
    # D0: unascertained
    D = {}
    D["D0 unascertained (all polymorphic at start)"] = dict(num=wt @ ev0[1:M], den=wt.sum(), tf=wt @ P_G[1:M, M])
    # D1: same-population present-day discovery, MAF >= thr, nd_eur diploids
    IE = w.maf_include(M, nd_eur, thr_eur)
    evI = Cev(IE)
    D["D1 same-pop MAF>=5% (2,345 dipl.)"] = dict(num=wt @ evI[1:M], den=wt @ IE[1:M], tf=0.0)
    IE1 = w.maf_include(M, nd_eur, 1.0 / (2 * nd_eur))
    evI1 = Cev(IE1)
    D["D1b same-pop polymorphic in 2,345 dipl."] = dict(num=wt @ evI1[1:M], den=wt @ IE1[1:M], tf=0.0)
    # D2: single African male heterozygous; D3: African array MAF>=5% (nd_afr diploids)
    for name, IA in [("D2 African single male het (Human Origins/Haak)", 2 * yv * (1 - yv)),
                     ("D3 African MAF>=5% (100 dipl.)", w.maf_include(M, nd_afr, 0.05))]:
        after = P_A @ IA
        Wx = (wt * after[1:M]) @ P_neo[1:M, :]
        Wpoly = Wx.copy()
        Wpoly[0] = 0.0
        Wpoly[M] = 0.0                      # sites already fixed/lost at the Neolithic sample time are not new events
        D[name] = dict(num=Wx @ ev0, den=wt @ IA[1:M], tf=Wpoly @ P_G[:, M])
    out["designs"] = D
    out["ev0"] = ev0
    # blog-style: Neolithic < 10% -> modern > 90% (sample level), design-free
    q90 = np.array([w.stats.binom.sf(int(np.floor(0.9 * 2 * nm)), 2 * nm, y) for y in yv])
    mdb = P_G @ q90
    mab = P_G @ q90[::-1]
    blog = Bd[:, 0] * mdb + Ba[:, 0] * mab
    # blog under designs
    q90I = {}
    for nm_, Iy in [("D1", IE)]:
        mdbI = P_G @ (q90 * Iy)
        mabI = P_G @ (q90[::-1] * Iy)
        bl = Bd[:, 0] * mdbI + Ba[:, 0] * mabI
        q90I[nm_] = (wt @ bl[1:M]) / (wt @ Iy[1:M])
    IA2 = 2 * yv * (1 - yv)
    after = P_A @ IA2
    Wx2 = (wt * after[1:M]) @ P_neo[1:M, :]
    q90I["D2"] = (Wx2 @ blog) / (wt @ IA2[1:M])
    out["blog"] = dict(unasc=(wt @ blog[1:M]) / wt.sum(), **q90I)
    return out


def report(o, label, npanel=NPANEL, verbose=True):
    lines = []
    lines.append(f"--- {label}: scaled N_s={o['M'] // 2}, f={o['f']:.2f}, window {o['Gs']} scaled gens = {o['Geff']:.0f} real; split {o['split_s']} scaled")
    lines.append(f"  P1 flux: derived fixations per site over window = {o['flux_derived_fix']:.4e}; mu*G = {o['mu_G']:.4e}; ratio {o['flux_derived_fix'] / o['mu_G']:.4f}")
    lines.append(f"  P2 new-in-window mutations that fix inside the window, per site = {o['new_in_window_fix']:.3e} ({o['new_in_window_fix'] / o['mu_G']:.2e} of mu*G)")
    ev0 = o["ev0"]
    for name, d in o["designs"].items():
        p = d["num"] / d["den"]
        tf = d["tf"] / d["den"] if d["den"] > 0 else 0
        lines.append(f"  {name}")
        lines.append(f"     P(newly-100%-in-modern-sample | site in set) = {p.sum():.3e}  -> on {npanel:,}-SNP panel: {npanel * p.sum():,.1f}")
        lines.append("       by Neolithic start band of the fixing allele: " + "; ".join(f"{b}: {npanel * x:.4g}" for b, x in zip(BAND_NAMES, p)))
        lines.append(f"     P(true population fixation of derived allele | in set) = {tf:.3e} -> panel {npanel * tf:,.2f}")
    d0 = o["designs"]["D0 unascertained (all polymorphic at start)"]
    base = d0["num"] / d0["den"]
    lines.append("  Enrichment of newly-100% events, P(event|in set)/P(event|polymorphic site), by band:")
    for name, d in o["designs"].items():
        p = d["num"] / d["den"]
        lines.append(f"     {name[:34]:<34} total {p.sum() / base.sum():7.3f} | " + " ".join(f"{b}:{(x / y if y > 0 else float('nan')):.3g}" for b, x, y in zip(BAND_NAMES, p, base)))
    lines.append(f"  Blog-style event (Neolithic <10% -> modern >90%), prob per site in set: unascertained-poly {o['blog']['unasc']:.2e}, D1 {o['blog']['D1']:.2e}, D2 {o['blog']['D2']:.2e}"
                 f"  -> panel x{npanel:,}: {npanel * o['blog']['unasc']:.3g} / {npanel * o['blog']['D1']:.3g} / {npanel * o['blog']['D2']:.3g}")
    if verbose:
        print("\n".join(lines), flush=True)
    return lines


def mc_unscaled_check(rng, nm=680):
    """Unscaled N=1e4 forward MC: P(modern sample (2nm copies) 100% derived) after 280 generations from start x."""
    print("\n=== Validation (b): unscaled N = 1e4 forward WF Monte Carlo vs scaled exact chain (G=280, 2nm=%d copies) ===" % (2 * nm))
    Ns, M = 1000, 2000
    P = w.wf_matrix(M)
    PG = w.mat_pow(P, 28)
    pd = (np.arange(M + 1) / M) ** (2 * nm)
    md = PG @ pd
    rows = []
    for x in (0.95, 0.98, 0.99, 0.995, 0.999):
        reps = 40000
        c = np.full(reps, int(round(x * 20000)), dtype=np.int64)
        for g in range(280):
            c = rng.binomial(20000, c / 20000)
        y = c / 20000
        ok = rng.random(reps) < y ** (2 * nm)       # sample of 2nm copies all derived (given y) -- exact in expectation
        est = (y ** (2 * nm)).mean()                # Rao-Blackwell over the sample draw
        se = (y ** (2 * nm)).std(ddof=1) / np.sqrt(reps)
        ex = md[int(round(x * M))]
        rows.append((x, est, se, ex))
        print(f"  x={x}: unscaled MC {est:.5f} +/- {se:.5f}; scaled exact chain {ex:.5f}; z={(ex - est) / se:+.2f}")
    return rows


def mc_pipeline_check(seed, Ne=NE, G=280, split=SPLIT, Ns=250, L=5e8, n0=1372, nm=680):
    """Forward Monte Carlo of the D2 pipeline (ancestral equilibrium SFS -> African & European drift ->
    single-male heterozygosity inclusion -> Neolithic and modern samples -> newly-100% events), scaled N_s=250.
    Independent of the Rao-Blackwellised chain algebra."""
    rng = np.random.default_rng(seed)
    f = Ne / Ns
    M = 2 * Ns
    Gs = int(round(G / f))
    split_s = int(round(split / f))
    neo_s = split_s - Gs
    theta = 4 * Ne * MU
    cnts = rng.poisson(theta * L / np.arange(1, M))
    c0 = np.repeat(np.arange(1, M), cnts)
    cA = c0.copy()
    for _ in range(split_s):
        cA = rng.binomial(M, cA / M)
    cE = c0.copy()
    for _ in range(neo_s):
        cE = rng.binomial(M, cE / M)
    K0 = rng.binomial(2 * n0, cE / M)
    for _ in range(Gs):
        cE = rng.binomial(M, cE / M)
    Km = rng.binomial(2 * nm, cE / M)
    yA = cA / M
    het = rng.random(c0.size) < 2 * yA * (1 - yA)
    fd0 = K0 / (2 * n0)
    ev_d = (K0 != 2 * n0) & (Km == 2 * nm)
    ev_a = (K0 != 0) & (Km == 0)
    res = np.zeros(len(EDGES) - 1)
    for b in range(len(EDGES) - 1):
        lo, hi = EDGES[b], EDGES[b + 1]
        sel_d = ev_d & (fd0 >= lo) & (fd0 < hi)
        sel_a = ev_a & ((1 - fd0) >= lo) & ((1 - fd0) < hi)
        res[b] = ((sel_d | sel_a) & het).sum()
    i = np.arange(1, M)
    den = L * float(((theta / i) * 2 * (i / M) * (1 - i / M)).sum())
    return res / den, np.sqrt(np.maximum(res, 1)) / den


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("=== Main run: Ne=1e4, 280 generations (7,000 y / 25 y), split 2000 gens, Z23046531 v62 sample sizes (n_Neo=1372, n_mod=680) ===")
    o = analyse(NE, 280, SPLIT, 1000, 1372, 680)
    report(o, "Ne=1e4, G=280, v62")
    print(f"  [{time.time() - t0:.0f}s]")
    print("\n=== Same, v66.p1 sample sizes (n_Neo=395, n_mod=441) ===")
    report(analyse(NE, 280, SPLIT, 1000, 395, 441), "Ne=1e4, G=280, v66.p1")
    print("\n=== Sensitivity: G=350 (20 y/gen, the blog's window) ===")
    report(analyse(NE, 350, SPLIT, 1000, 1372, 680), "Ne=1e4, G=350, v62")

    print("\n=== Sensitivity table (panel counts, N_panel=1,143,671; newly-100% totals and 50-90% band) ===")
    print(f"{'Ne':>7} {'G':>4} {'split':>6} | {'D0 (poly)':>12} | {'D1 MAF5%':>10} | {'D2 AfrHet':>10} {'D2 50-90%':>10} {'D2 true fix':>11} | {'D3 AfrMAF':>10}")
    for ne, g, sp in [(5e3, 280, 2000), (1e4, 280, 1000), (1e4, 280, 2000), (1e4, 280, 3000), (1e4, 350, 2000), (2e4, 280, 2000), (2e4, 350, 2000)]:
        Nsx = 1000
        oo = analyse(ne, g, sp, Nsx, 1372, 680)
        d = oo["designs"]
        k = list(d.keys())
        pc = lambda dd: NPANEL * (dd["num"] / dd["den"])
        print(f"{ne:7.0f} {g:4d} {sp:6d} | {pc(d[k[0]]).sum():12.1f} | {pc(d[k[1]]).sum():10.2f} | {pc(d[k[3]]).sum():10.1f} "
              f"{pc(d[k[3]])[2]:10.3g} {NPANEL * d[k[3]]['tf'] / d[k[3]]['den']:11.2f} | {pc(d[k[4]]).sum():10.2f}   (Geff={oo['Geff']:.0f})", flush=True)

    print("\n=== Validation (a): scaling, N_s = 500 and 2000 vs 1000 (Ne=1e4, G=280, v62) ===")
    ref = analyse(NE, 280, SPLIT, 1000, 1372, 680)
    for Nsx in (500, 2000):
        oo = analyse(NE, 280, SPLIT, Nsx, 1372, 680)
        for key in list(ref["designs"].keys()):
            a = NPANEL * ref["designs"][key]["num"] / ref["designs"][key]["den"]
            b = NPANEL * oo["designs"][key]["num"] / oo["designs"][key]["den"]
            print(f"  N_s={Nsx:5d} {key[:42]:<42} total {b.sum():10.3f} vs N_s=1000 {a.sum():10.3f} (ratio {b.sum() / a.sum() if a.sum() else float('nan'):.4f}); 50-90%: {b[2]:.3g} vs {a[2]:.3g}")
        print(f"     flux ratio fix/(mu G): {oo['flux_derived_fix'] / oo['mu_G']:.4f} (N_s=1000: {ref['flux_derived_fix'] / ref['mu_G']:.4f})", flush=True)
    mc_unscaled_check(rng)

    print("\n=== Validation (c): independent forward MC of the D2 pipeline (N_s=250) vs exact-chain algebra at N_s=250 ===")
    pm, pse = mc_pipeline_check(SEED + 7)
    oo = analyse(NE, 280, SPLIT, 250, 1372, 680)
    d2 = oo["designs"]["D2 African single male het (Human Origins/Haak)"]
    ex = d2["num"] / d2["den"]
    for b, (a, s, e) in enumerate(zip(pm, pse, ex)):
        print(f"  band {BAND_NAMES[b]:>7}: MC {a:.4e} +/- {s:.1e}; exact chain {e:.4e}; z={(a - e) / s:+.2f}")
    print(f"  total: MC {pm.sum():.4e}; exact {ex.sum():.4e}")

    print("\n=== C6 denominator accounting (Z18525185: 630 = 1.2e-8 x 1.5e8 x 350) ===")
    print(f"  630 expectation (150M sites, k=mu, 350 gens): {1.2e-8 * 1.5e8 * 350:.0f}")
    print(f"  uniform panel scaling (1,233,013 / 150e6 x 630): {630 * NPANEL_AADR / 1.5e8:.2f}")
    o350 = analyse(NE, 350, SPLIT, 1000, 1372, 680)
    for name, d in o350["designs"].items():
        tf = d["tf"] / d["den"]
        pe = (d["num"] / d["den"]).sum()
        print(f"  {name[:46]:<46} true-fixation expectation on panel: {NPANEL_AADR * tf:9.2f}; sample-level newly-100% events: {NPANEL_AADR * pe:11.2f}")
    d0 = o350["designs"]["D0 unascertained (all polymorphic at start)"]
    print(f"  Unascertained RANDOM genome sites (monomorphic ones included): true fixations {NPANEL_AADR * o350['flux_derived_fix']:.2f}"
          f" (= panel-size x mu G = {NPANEL_AADR * 1.2e-8 * 350:.2f}); sample-level newly-100% events {NPANEL_AADR * d0['num'].sum():.1f}")
    print("  => uniform scaling (5.2) is the expectation for a RANDOM 1.23M-site sample; the 1240k panel is a polymorphism-ascertained set, and the model-specific")
    print("     expectations above are 2-3 orders of magnitude larger for 'true fixation' (D2/D3) because fixations occur only at previously polymorphic sites.")

    print("\n=== Ne scan for the 50-90% start band (D2, v62 sizes, G=280): observed 1 (v62) and 3 (v66) completions ===")
    for ne in (4000, 5000, 6000, 7000, 8000, 9000, 1e4):
        oo = analyse(ne, 280, SPLIT, 1000, 1372, 680)
        dd = oo["designs"]["D2 African single male het (Human Origins/Haak)"]
        o66 = analyse(ne, 280, SPLIT, 1000, 395, 441)
        d66 = o66["designs"]["D2 African single male het (Human Origins/Haak)"]
        print(f"  Ne={ne:6.0f}: expected 50-90% completions on 1.14M panel: v62 sizes {NPANEL * (dd['num'] / dd['den'])[2]:.3g}; v66 sizes {NPANEL * (d66['num'] / d66['den'])[2]:.3g};"
              f" total newly-100% v62 {NPANEL * (dd['num'] / dd['den']).sum():,.0f}", flush=True)
    print(f"\n[total elapsed {time.time() - t0:.0f}s]")


if __name__ == "__main__":
    main()
