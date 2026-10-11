"""HF post hoc follow-up run (stage `ph`), written 2026-10-11 AFTER the three HF reviews (baa7595) and BEFORE any run
of this file (smoke included).  POST HOC: every prediction below is made after seeing `raw/hf_main.jsonl`; it
cannot rescue or sink a pre-registered HF score by itself.  It decides the items the reviews left open:
  L   long burn-in (correctness #2/#5, "flagged burn-in artefact" (i); critic #5): are the flat-k/lam softJ
      "failures" at R = 1.05, K = 4000 and weak s a pipeline-fill artefact or a rate limit?
  C   cap release (correctness #2): are the softJ / trunc lam_max values below the grid top set by max_open = 5,000?
      (decides whether DA2 / PA4 can be scored at all)
  M   mix boundary (correctness #1, critic #1; "flagged burn-in artefact" (ii)): where exactly is the extinction /
      throughput boundary at h = 0.1 and h = 0.3?  (rescoring of DA1, CA2, PA2 at grid resolution)
  N   noisy truncation (steelman-day #2): truncation on a phenotype A + e, not on the exact genotype count.

ENGINE: `run()` below is hf_followups.run() (8bd9d29) with three additions that do not change any existing mode's
random-number stream: (1) mode "trunc" takes a genotypic share g of the truncation variable's variance; g = 1 is
the HF key exactly (anc + U(0, 0.5)); g < 1 replaces the U(0, 0.5) tie-break by e ~ N(0, var_J(anc) (1 - g) / g),
var over this generation's juveniles; (2) a trace (t, nopen, cumulative fixations, N) every 250 generations;
(3) the peak RSS of the worker in each row.  `smoke` first reruns 4 hf_main jobs with their ORIGINAL seeds and
requires every field except sec to equal raw/hf_main.jsonl (engine identity), then probes worker memory.
Seeds: SeedSequence([20261011, 2, cell, rep]) (main used code 1).  Free recombination, K adults, s per ancestral copy,
as in HF.  Truncation, in every g, has N = K always: it cannot go extinct, so stage N measures sweep speed and backlog,
not load (steelman-day #1 applies to it as to softJ).

CELLS (cell = part, K, s, b, lam, R, mode, h, label, reps, gens, burn, max_open, g)
  L  softJ (mix h = 0), max_open 20,000, gens 80,000, burn 40,000, 4 reps, lam in {0.0351, 0.1, 0.2, 0.4}:
       s = 0.01: R in {1.05, 1.111} at K = 1000, and R = 1.111 at K = 4000;  s = 0.002: R in {1.111, 2} at K = 1000.
  C  max_open 20,000, gens 20,000, burn 5,000 (the main-stage window), lam in {0.8, 1.6}:
       softJ K = 1000 at R in {1.05, 1.111} (4 reps); softJ K = 4000 at R = 1.111 (3 reps); trunc K = 1000 R = 1.05,
       lam = 1.6 only (4 reps).
  M  mix, s = 0.01, K = 1000, 8 reps, gens 40,000, burn 10,000, max_open 20,000, lam (geometric, inside the HF brackets):
       h = 0.1, R = 1.111: {0.0074, 0.0094, 0.0111, 0.013, 0.0157}           (review spec)
       h = 0.1, R = 2    : {0.1, 0.119, 0.141, 0.168, 0.2}                    (added: decides CA2 at R = 2, corr. #1a)
       h = 0.3, R = 1.111: {0.0037, 0.0049, 0.0064, 0.0084, 0.0111}
       h = 0.3, R = 2    : {0.0351, 0.0454, 0.0592, 0.0768, 0.1}
  N  trunc, s = 0.01 (s does not enter trunc), K = 1000, R in {1.111, 2}, g in {1, 0.5, 0.1}, lam in
       {0.0351, 0.1, 0.2, 0.4, 0.8, 1.6}, 4 reps, gens 80,000, burn 40,000, max_open 20,000.

RULES (fixed now)
  L, C, N (steady modes): HF's pre-registered rule over the recorded window: no failure, k/lam >= 0.9,
     nopen_q4/nopen_q1 <= 1.15.  Also reported: the review's stricter rule k/lam >= 0.95 and q4/q1 <= 1.10.
     lam_max = largest lam with >= 50% success; "+" when it is the grid top; "(cap)" when the next lam fails by backlog.
     tau = nopen / k (sweep residence time).
  M  success(T), T in {20k (primary), 40k}: alive at T (no extinction or backlog before T), k/lam >= 0.9 over the
     window [10k, T] (from the trace), and, only if mean nopen in the window's first quarter is >= 50,
     nopen(last quarter)/nopen(first quarter) <= 1.15.  Also extinction-only survival at 10k/20k/40k.
     lam50 = HF/H8 first-crossing estimator (log-linear) plus the bracket (last lam >= 50%, first lam < 50%).
     Reported as ratios to the H8 hard cap at 10k (0.00368 / 0.0363, the cap the pre-registered DA1/CA2 used) and at
     20k (0.00350 / 0.030).

PREDICTIONS (post hoc; both sides; audit numbers)
  L  Critic side (and the review's diagnosis): every L cell passes HF's rule at every lam (PA1 R = 1.05 band 0.1-0.4
       then holds at its top; PA5 softJ "0.1-0.2 at R = 2" fails upward; K = 4000 passes at 0.4).
     Day side (soft limit real): in at least one L series k/lam falls with lam, k/lam(0.4) < 0.9 with no backlog.
     Audit PL1 (correctness review): k/lam >= 0.95 and q4/q1 <= 1.10 in every L cell (lam x tau < 20,000 everywhere:
       tau ~ 7,500 (R = 1.05), ~4,300 (R = 1.111), ~6,000 (K = 4000), ~20,000 (weak s, R = 1.111), ~9,000 (weak, R = 2)).
       PL2 tau is flat in lam within +-25% in each series (a fill lag, not a capacity limit).
  C  Audit PC-1: no C cell backlogs at max_open 20,000 (expected nopen ~ lam x tau <= 12,000).  softJ R = 1.111 and
       trunc R = 1.05 sustain 1.6 on HF's rule (so the HF lam_max values 0.8 / 0.8 were set by max_open).  softJ
       K = 4000 R = 1.111: k/lam 0.88-0.93 at 20k (fill lag; tau ~ 6,000 > 5,000 burn), so its rule outcome is a
       coin-flip; it does not backlog.  softJ R = 1.05: fails HF's rule on the fill lag (k/lam ~ 0.8) but no backlog.
     Day side DA2 restated: K = 4000 sustains less than K = 1000 at R = 1.111 (backlog or k/lam < 0.9 at a lam where
       K = 1000 passes, not explained by the fill lag: k/lam falling with lam).  Critic side: no K effect beyond the lag.
  M  Day side (DA1 restated on the boundary): h = 0.3 lam50(20k) <= 2x the 10k hard cap at both R (<= 0.0074 at
       R = 1.111, <= 0.073 at R = 2); h = 0.1 lam50(20k) < 3x the cap at R = 1.111 (< 0.0110).
     Critic side (CA2 restated): h = 0.1 lam50(20k) >= 3x the 10k hard cap at R = 1.111 (>= 0.0110) and at R = 2
       (>= 0.109).
     Audit: PM1 h = 0.1 R = 1.111 lam50(20k) in [0.0094, 0.0135] (correctness #1b: 0.011-0.013, 40k lower);
       PM2 h = 0.1 R = 2 in [0.12, 0.18]; PM3 h = 0.3 R = 1.111 in [0.0045, 0.0090]; PM4 h = 0.3 R = 2 in [0.045, 0.090];
       PM5 the pre-registered mean-field limit (h lam D_soft = ln R: 0.0157 / 0.29 at h = 0.1, 0.0052 / 0.096 at h = 0.3)
       is within 2x of lam50(20k) in all four series; PM6 lam50(40k) <= lam50(20k) in all four (survival only falls).
  N  Day side (steelman-day #2, DB1 for phenotypic truncation): at g = 0.1 trunc lam_max <= 1.25 x Term 3
       (<= 0.0087 at R = 1.111, i.e. fails already at 0.0351; <= 0.057 at R = 2).
     Critic side: at g = 0.1 trunc lam_max >= 5x Term 3 at both R (>= 0.0351 at R = 1.111; >= 0.4 at R = 2).
     Audit (mean field: truncation on A + e gives per-copy s_eff ~ i sqrt(g) / sigma_A with sigma_A ~ sqrt(nopen), so
       tau ~ c(R) lam / g, nopen ~ c(R) lam^2 / g; c from HF trunc rows ~ 850 (R = 1.111), ~ 75 (R = 2)):
       PN1 g = 1 reproduces HF trunc: lam_max 1.6+ at both R, nopen within 25% of hf_main trunc at the same lam.
       PN2 R = 2: lam_max 1.6+ at g = 0.5 and g = 0.1.  PN3 R = 1.111: lam_max 1.6+ at g = 0.5; at g = 0.1 lam_max 0.8,
       with lam 1.6 failing by backlog (nopen > 20,000).  PN4 tau(g = 0.1) / tau(g = 1) in [3, 20] at every sustained lam.
  What changes a verdict: none of L/C/N can move H, H8 or H5 (the realised rate in every HF soft/trunc cell already
  exceeds 1/300 by >= 5x).  M sets the h-scope sentence of the H/H8/H5 verdicts ("within ~Nx the hard cap at h");
  N decides whether "contradicted in-model for noise-free truncation" extends to phenotypic truncation in the H8 text.

USAGE  (Python only as research/.venv/bin/python -I)
  hf_posthoc.py smoke                    engine-identity check (4 hf_main jobs) + memory probe; raw/hf_ph_smoke.jsonl
  HF_SHARD=wh|bd|all hf_posthoc.py ph W  run the shard's jobs (W workers), dearest-first; raw/hf_ph_<shard>.jsonl.
                                         Shards are a fixed greedy split of estimated cost (wh 11 slots, bd 7 slots,
                                         every K = 4000 job on wh: builder RAM).  Jobs already present in ANY
                                         raw/hf_ph_*.jsonl are skipped, so a host can take over the other's
                                         remainder (copy the other file in, run HF_SHARD=all).  Orchestration only:
                                         seeds are per (cell, rep).
  hf_posthoc.py merge                    union of raw/hf_ph_{wh,bd,all}.jsonl -> raw/hf_ph.jsonl (identity-checks overlaps)
  hf_posthoc.py analyse                  tables from raw/hf_ph.jsonl
"""
import collections
import glob
import json
import math
import os
import resource
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hf_followups as HF  # noqa: E402  (constants, es_keep, first_cross, build('main'))

RAW = HF.RAW
SEED = HF.SEED
EXT_N = HF.EXT_N
CHECKS = HF.CHECKS
RH = HF.RH
TRACE = 250


def run(K, s, b, lam, R, mode, h, gens, burn, rng, max_open=5000, chunk=256, g=1.0, trace_every=TRACE):
    N = K
    G = np.zeros((0, 2 * N), dtype=np.uint8)
    t_open = []
    fixes_rec = 0
    fixes_all = 0
    trace = []
    acc = dict(rec=0, La=0.0, I=0.0, maxrel=0.0, nfrac=0.0, nopen=0.0)
    rec_len = gens - burn
    q1, q4 = [0.0, 0], [0.0, 0]
    alive_at = {T: False for T in CHECKS}
    fail, t_fail = None, None
    for t in range(gens):
        if t % trace_every == 0:
            trace.append([t, int(G.shape[0]), fixes_all, int(N)])
        for T in CHECKS:
            if t == T - 1:
                alive_at[T] = True
        nnew = rng.poisson(lam)
        if nnew:
            cols = np.zeros((nnew, 2 * N), dtype=np.uint8)
            cols[np.arange(nnew), rng.integers(0, 2 * N, nnew)] = 1
            G = np.vstack([G, cols])
            t_open.extend([t] * nnew)
        nl = G.shape[0]
        if nl > max_open:
            fail, t_fail = "backlog", t
            break
        wA = None
        if mode == "hard":
            f = min(R, K / N)
            J = int(f * N)
            J += int(rng.random() < f * N - J)
        elif mode == "mix":
            J = int(R * N)
            J += int(rng.random() < R * N - J)
        elif mode == "trunc":
            J = int(round(R * K))
        else:                                             # softWF
            J = K
            ancA = (2 * nl - G.reshape(nl, N, 2).sum(axis=(0, 2), dtype=np.int64)) if nl else np.zeros(N, np.int64)
            wA = np.exp(-s * ancA - b * ancA.astype(float) ** 2)
        if J < 2:
            fail, t_fail = "extinct", t
            break
        if mode == "softWF":
            pw = wA / wA.sum()
            pa = rng.choice(N, size=J, p=pw)
            pb = rng.choice(N, size=J, p=pw)
            same = pb == pa
            while same.any():
                pb[same] = rng.choice(N, size=int(same.sum()), p=pw)
                same = pb == pa
        else:
            pa = rng.integers(0, N, J)
            pb = (pa + rng.integers(1, N, J)) % N
        par = np.empty(2 * J, dtype=np.int64)
        par[0::2] = pa
        par[1::2] = pb
        C = np.empty((nl, 2 * J), dtype=np.uint8)
        anc = np.zeros(J, dtype=np.int64)
        for i0 in range(0, nl, chunk):
            i1 = min(nl, i0 + chunk)
            o = rng.integers(0, 2, size=(i1 - i0, 2 * J), dtype=np.uint8)
            C[i0:i1] = np.take_along_axis(G[i0:i1], 2 * par[None, :] + o, axis=1)
            anc += C[i0:i1].reshape(i1 - i0, J, 2).sum(axis=(0, 2), dtype=np.int64)
        anc = 2 * nl - anc
        w = np.exp(-s * anc - b * anc.astype(float) ** 2) if mode != "softWF" else wA
        wbar = float(w.mean())
        if mode == "hard":
            keep = rng.random(J) < w
        elif mode == "mix":
            keep = rng.random(J) < w ** h if h > 0 else np.ones(J, bool)
            ns = int(keep.sum())
            if ns > K:
                idx = np.flatnonzero(keep)
                k2 = HF.es_keep(w[idx] ** (1 - h), K, rng) if h < 1 else HF.es_keep(np.ones(ns), K, rng)
                keep = np.zeros(J, bool)
                keep[idx[k2]] = True
        elif mode == "trunc":
            sd = math.sqrt(float(anc.var()) * (1 - g) / g) if g < 1 else 0.0
            if sd > 0:
                key = anc + rng.normal(0.0, sd, J)       # post hoc: phenotypic truncation, genotypic share g
            else:
                key = anc + rng.random(J) * 0.5          # HF key (g = 1, or no variance yet)
            keep = np.zeros(J, bool)
            keep[np.argpartition(key, K - 1)[:K]] = True
        else:
            keep = np.ones(J, bool)
        surv = np.flatnonzero(keep)
        Nn = len(surv)
        if t >= burn:
            rel = w / wbar
            acc["rec"] += 1
            acc["La"] += -math.log(max(wbar, 1e-300))
            acc["I"] += float(rel.var())
            acc["maxrel"] += float(rel.max())
            acc["nfrac"] += Nn / K
            acc["nopen"] += nl
            if t < burn + rec_len // 4:
                q1[0] += nl; q1[1] += 1
            elif t >= gens - rec_len // 4:
                q4[0] += nl; q4[1] += 1
        if Nn < EXT_N:
            fail, t_fail = "extinct", t
            break
        N = Nn
        hidx = (2 * surv[:, None] + np.arange(2)[None, :]).ravel()
        G = np.ascontiguousarray(C[:, hidx]) if nl else np.zeros((0, 2 * N), dtype=np.uint8)
        if nl:
            cnt = G.sum(axis=1, dtype=np.int64)
            fixed = cnt == 2 * N
            lost = np.flatnonzero(cnt == 0)
            if fixed.any():
                fixes_rec += int(t >= burn) * int(fixed.sum())
                fixes_all += int(fixed.sum())
            if len(lost):
                G[lost, rng.integers(0, 2 * N, len(lost))] = 1
            if fixed.any():
                kr = np.flatnonzero(~fixed)
                G = G[kr]
                t_open = [t_open[j] for j in kr]
    if fail is None:
        for T in CHECKS:
            if gens >= T:
                alive_at[T] = True
        trace.append([gens, int(G.shape[0]), fixes_all, int(N)])
    else:
        trace.append([t_fail, int(G.shape[0]), fixes_all, int(N)])
    n = max(acc["rec"], 1)
    return dict(fail=fail, t_fail=t_fail, alive={str(T): alive_at[T] for T in CHECKS if T <= gens},
                k=fixes_rec / n, fixes_rec=fixes_rec, gens_rec=acc["rec"],
                D=acc["La"] / fixes_rec if fixes_rec else float("nan"), La=acc["La"] / n,
                I=acc["I"] / n, maxrel=acc["maxrel"] / n, nfrac=acc["nfrac"] / n,
                nopen=acc["nopen"] / n, nopen_q1=q1[0] / max(q1[1], 1), nopen_q4=q4[0] / max(q4[1], 1),
                trace=trace)


# ------------------------------------------------------------------------------------------------ cells
LAMS_L = (0.0351, 0.1, 0.2, 0.4)
LAMS_N = (0.0351, 0.1, 0.2, 0.4, 0.8, 1.6)
MIX = {(0.1, RH): (0.0074, 0.0094, 0.0111, 0.013, 0.0157),
       (0.1, 2.0): (0.1, 0.119, 0.141, 0.168, 0.2),
       (0.3, RH): (0.0037, 0.0049, 0.0064, 0.0084, 0.0111),
       (0.3, 2.0): (0.0351, 0.0454, 0.0592, 0.0768, 0.1)}
MO = 20000


def build(stage):
    c = []
    if stage == "smoke":   # memory probe only (identity check is separate)
        c.append(("smoke", 4000, 0.01, 0.0, 1.6, RH, "mix", 0.0, "softJ", 1, 1500, 0, MO, 1.0))
        c.append(("smoke", 1000, 0.002, 0.0, 3.2, RH, "mix", 0.0, "softJ", 1, 1500, 0, MO, 1.0))
        c.append(("smoke", 1000, 0.01, 0.0, 1.6, 2.0, "trunc", 0.0, "trunc g=0.1", 1, 1500, 0, MO, 0.1))
        c.append(("smoke", 1000, 0.01, 0.0, 0.0111, RH, "mix", 0.1, "h=0.1", 1, 1500, 500, MO, 1.0))
        return c
    assert stage == "ph"
    for K, s, R in ((1000, 0.01, 1.05), (1000, 0.01, RH), (4000, 0.01, RH), (1000, 0.002, RH), (1000, 0.002, 2.0)):
        for lam in LAMS_L:
            c.append(("L", K, s, 0.0, lam, R, "mix", 0.0, "softJ", 4, 80000, 40000, MO, 1.0))
    for K, R, reps in ((1000, 1.05, 4), (1000, RH, 4), (4000, RH, 3)):
        for lam in (0.8, 1.6):
            c.append(("C", K, 0.01, 0.0, lam, R, "mix", 0.0, "softJ", reps, 20000, 5000, MO, 1.0))
    c.append(("C", 1000, 0.01, 0.0, 1.6, 1.05, "trunc", 0.0, "trunc", 4, 20000, 5000, MO, 1.0))
    for (h, R), lams in MIX.items():
        for lam in lams:
            c.append(("M", 1000, 0.01, 0.0, lam, R, "mix", h, f"h={h}", 8, 40000, 10000, MO, 1.0))
    for R in (RH, 2.0):
        for g in (1.0, 0.5, 0.1):
            for lam in LAMS_N:
                c.append(("N", 1000, 0.01, 0.0, lam, R, "trunc", 0.0, f"trunc g={g}", 4, 80000, 40000, MO, g))
    return c


def job(a):
    code, ci, cell, rep = a
    part, K, s, b, lam, R, mode, h, lab, reps, gens, burn, mo, g = cell
    rng = np.random.default_rng(np.random.SeedSequence([SEED, code, ci, rep]))
    t0 = time.time()
    r = run(K, s, b, lam, R, mode, h, gens, burn, rng, max_open=mo, g=g)
    r.update(dict(part=part, cell=ci, K=K, s=s, b=b, lam=lam, R=R, mode=mode, h=h, g=g, label=lab, rep=rep,
                  gens=gens, burn=burn, max_open=mo, sec=time.time() - t0,
                  maxrss_mb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
    return r


def est_cost(cell):
    """Rough seconds per job (fitted by eye to hf_main `sec`); used only to split shards and order jobs."""
    part, K, s, b, lam, R, mode, h, lab, reps, gens, burn, mo, g = cell
    J = R * K
    c = 6e-5 * (K / 1000) * (J / K) / 1.111
    if mode == "trunc":
        tau = (2600 if R < 1.1 else 850 if R < 1.5 else 75) * lam / g
    elif h == 0:
        tau = {(1000, 0.01): 7500 if R < 1.1 else 4300, (4000, 0.01): 6000,
               (1000, 0.002): 20000 if R < 1.5 else 9000}[(K, s)]
    else:
        tau = 5000
    nss = lam * tau
    if nss > mo:
        ge, nav = min(gens, 1.5 * mo / lam), mo / 2
    else:
        ge, nav = gens, nss
    return ge * (max(nav, 5) * c + 2e-4 * K / 1000)


def shards(cells):
    jobs = [(2, ci, cell, rep) for ci, cell in enumerate(cells) for rep in range(cell[9])]
    jobs.sort(key=lambda j: -est_cost(j[2]))
    load = {("wh", i): 0.0 for i in range(11)}
    load.update({("bd", i): 0.0 for i in range(7)})
    out = {"wh": [], "bd": []}
    for j in jobs:
        cand = [k for k in load if k[0] == "wh"] if j[2][1] > 1000 else list(load)
        k = min(cand, key=lambda x: load[x])
        load[k] += est_cost(j[2])
        out[k[0]].append(j)
    est = {h: max(v for k, v in load.items() if k[0] == h) for h in ("wh", "bd")}
    return out, est


def done_set():
    done = set()
    for p in glob.glob(os.path.join(RAW, "hf_ph_*.jsonl")):
        if p.endswith("hf_ph_smoke.jsonl"):
            continue
        for line in open(p):
            d = json.loads(line)
            done.add((d["cell"], d["rep"]))
    return done


def run_stage(workers):
    cells = build("ph")
    sh = os.environ.get("HF_SHARD", "all")
    parts, est = shards(cells)
    jobs = sorted(parts["wh"] + parts["bd"], key=lambda j: -est_cost(j[2])) if sh == "all" else parts[sh]
    done = done_set()
    todo = [j for j in jobs if (j[1], j[3]) not in done]
    path = os.path.join(RAW, f"hf_ph_{sh}.jsonl")
    print(f"stage ph shard {sh}: {len(cells)} cells, {len(jobs)} jobs in shard, {len(todo)} to run, workers {workers}; "
          f"est. wall (h) wh {est['wh'] / 3600:.1f} bd {est['bd'] / 3600:.1f}; est. CPU-h shard "
          f"{sum(est_cost(j[2]) for j in todo) / 3600:.0f}", flush=True)
    t0 = time.time()
    with Pool(workers) as pool, open(path, "a") as fh:
        for i, r in enumerate(pool.imap_unordered(job, todo, chunksize=1)):
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            print(f"[{time.time() - t0:7.0f}s] {i + 1}/{len(todo)} {r['part']} {r['label']} K={r['K']} s={r['s']} "
                  f"R={r['R']:.3f} lam={r['lam']:.4g} rep{r['rep']} fail={r['fail']}@{r['t_fail']} "
                  f"k/lam={r['k'] / r['lam']:.3f} nopen={r['nopen']:.0f} sec={r['sec']:.0f} rss={r['maxrss_mb']:.0f}MB",
                  flush=True)
    print(f"stage ph shard {sh} done in {time.time() - t0:.0f} s", flush=True)


def smoke():
    """(1) engine identity: 4 hf_main jobs, original seeds, every field but sec must match raw/hf_main.jsonl.
       (2) memory probe cells (1 worker, sequential), peak RSS reported."""
    main_cells = HF.build("main")
    rows = {(d["cell"], d["rep"]): d for d in map(json.loads, open(os.path.join(RAW, "hf_main.jsonl")))}
    want = [("A-mix", 0.3, RH, 0.0351), ("A-soft", "trunc", 3.0, 0.0351), ("A-soft", "softWF", None, 0.0351),
            ("A-valid", 1.0, 2.0, None)]
    picks = []
    for ci, c in enumerate(main_cells):
        for w in want:
            if c[0] != w[0] or w in [p[0] for p in picks]:
                continue
            if w[0] == "A-mix" and (c[7] != w[1] or abs(c[5] - w[2]) > 1e-9 or abs(c[4] - w[3]) > 1e-9):
                continue
            if w[0] == "A-soft" and (c[6] != w[1] or abs(c[4] - w[3]) > 1e-9 or (w[2] and abs(c[5] - w[2]) > 1e-9)):
                continue
            if w[0] == "A-valid" and abs(c[5] - w[2]) > 1e-9:
                continue
            picks.append((w, ci, c))
    ok = True
    for w, ci, c in picks:
        part, K, s, b, lam, R, mode, h, lab, reps, gens, burn, mo = c
        rng = np.random.default_rng(np.random.SeedSequence([SEED, 1, ci, 0]))
        t0 = time.time()
        r = run(K, s, b, lam, R, mode, h, gens, burn, rng, max_open=mo)
        ref = rows[(ci, 0)]
        diff = {k: (r[k], ref[k]) for k in r if k in ref and k != "sec" and json.dumps(r[k]) != json.dumps(ref[k])}
        ok &= not diff
        print(f"identity cell {ci} {part} {mode} h={h} R={R} lam={lam:.4g}: {'OK' if not diff else diff} "
              f"({time.time() - t0:.0f} s)", flush=True)
    print("ENGINE IDENTITY:", "PASS" if ok and len(picks) == 4 else f"FAIL ({len(picks)} picked)", flush=True)
    with open(os.path.join(RAW, "hf_ph_smoke.jsonl"), "w") as fh:
        for ci, c in enumerate(build("smoke")):
            r = job((3, ci, c, 0))
            r.pop("trace")
            fh.write(json.dumps(r) + "\n")
            print(f"probe {c[8]} K={c[1]} R={c[5]:.3f} lam={c[4]} gens={c[10]}: nopen_end={r['nopen_q4']:.0f} "
                  f"fail={r['fail']} sec={r['sec']:.0f} peak RSS {r['maxrss_mb']:.0f} MB", flush=True)


def merge():
    rows, src = {}, {}
    nboth = mism = 0
    for p in ("wh", "bd", "all"):
        fp = os.path.join(RAW, f"hf_ph_{p}.jsonl")
        if not os.path.exists(fp):
            continue
        for d in map(json.loads, open(fp)):
            k = (d["cell"], d["rep"])
            strip = json.dumps({a: v for a, v in d.items() if a not in ("sec", "maxrss_mb")}, sort_keys=True)
            if k in rows:
                nboth += 1
                mism += strip != rows[k][0]
                continue
            rows[k] = (strip, d)
            src[k] = p
    exp = {(ci, rep) for ci, c in enumerate(build("ph")) for rep in range(c[9])}
    print(f"merged {len(rows)} unique of {len(exp)} expected; missing {len(exp - set(rows))}; extra "
          f"{len(set(rows) - exp)}; on two files {nboth}, mismatches {mism}; by file "
          f"{dict(collections.Counter(src.values()))}")
    with open(os.path.join(RAW, "hf_ph.jsonl"), "w") as fh:
        for k in sorted(rows):
            fh.write(json.dumps(rows[k][1]) + "\n")


# ------------------------------------------------------------------------------------------------ analysis
def window(r, a, T):
    """k/lam and q4/q1, mean nopen in the first quarter over [a, T) from the trace; None if the run ended before T."""
    if r["fail"] is not None and r["t_fail"] < T:
        return None
    tr = {x[0]: x for x in r["trace"]}
    if a not in tr or T not in tr:
        return None
    k = (tr[T][2] - tr[a][2]) / (T - a)
    qlen = (T - a) // 4
    q1 = [x[1] for t, x in tr.items() if a <= t < a + qlen]
    q4 = [x[1] for t, x in tr.items() if T - qlen <= t < T]
    return k / r["lam"], float(np.mean(q4)) / max(float(np.mean(q1)), 1e-9), float(np.mean(q1))


def ok_mix(r, T):
    w = window(r, r["burn"], T)
    if w is None:
        return False
    kl, qr, n1 = w
    return kl >= 0.9 and (n1 < 50 or qr <= 1.15)


def ok_steady(r, strict=False):
    if r["fail"] is not None:
        return False
    kl, qr = r["k"] / r["lam"], r["nopen_q4"] / max(r["nopen_q1"], 1e-9)
    return (kl >= 0.95 and qr <= 1.10) if strict else (kl >= 0.9 and qr <= 1.15)


def bracket(pts):
    hi = [lam for lam, f in pts if f >= 0.5]
    lo = [lam for lam, f in pts if f < 0.5 and (not hi or lam > max(hi))]
    return (max(hi) if hi else None, min(lo) if lo else None)


def analyse():
    rows = [json.loads(l) for l in open(os.path.join(RAW, "hf_ph.jsonl"))]
    print(f"rows {len(rows)}; peak worker RSS {max(r['maxrss_mb'] for r in rows):.0f} MB; "
          f"CPU-h {sum(r['sec'] for r in rows) / 3600:.1f}")
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["part"], r["mode"], r["h"], r["g"], r["K"], r["s"], round(r["R"], 4), r["lam"])].append(r)
    series = collections.defaultdict(list)
    for k, v in g.items():
        series[k[:7]].append((k[7], v))
    caps10 = {round(RH, 4): 0.00368, 2.0: 0.0363}
    caps20 = {round(RH, 4): 0.00350, 2.0: 0.030}
    for key in sorted(series, key=str):
        part, mode, h, gs, K, s, R = key
        pts = sorted(series[key])
        print(f"\n## {part} {mode} h={h} g={gs} K={K} s={s} R={R}")
        if part == "M":
            print("| lam | alive 10k/20k/40k | rule 20k | rule 40k | k/lam [10k,20k) | q4/q1 | nopen q1 |")
            print("|---|---|---|---|---|---|---|")
            fr = {20000: [], 40000: []}
            for lam, v in pts:
                al = [sum(1 for r in v if r["alive"].get(str(T)) and not (r["fail"] and r["t_fail"] < T)) for T in CHECKS]
                for T in fr:
                    fr[T].append((lam, sum(ok_mix(r, T) for r in v) / len(v)))
                ws = [window(r, r["burn"], 20000) for r in v]
                ws = [w for w in ws if w]
                print(f"| {lam:.4g} | {al[0]}/{al[1]}/{al[2]} of {len(v)} | {fr[20000][-1][1] * len(v):.0f} | "
                      f"{fr[40000][-1][1] * len(v):.0f} | "
                      + (f"{np.mean([w[0] for w in ws]):.2f} | {np.mean([w[1] for w in ws]):.2f} | {np.mean([w[2] for w in ws]):.0f} |"
                         if ws else "- | - | - |"))
            for T in fr:
                xs, fs = [p[0] for p in fr[T]], [p[1] for p in fr[T]]
                l50 = HF.first_cross(xs, fs, False)
                br = bracket(fr[T])
                print(f"lam50({T // 1000}k) = {l50:.4g}  bracket {br}  x cap10k {l50 / caps10[R]:.2f}  "
                      f"x cap20k {l50 / caps20[R]:.2f}")
        else:
            print("| lam | HF rule | strict rule | fails (type@t) | k/lam | q4/q1 | nopen | tau = nopen/k | maxrel | D | RSS MB |")
            print("|---|---|---|---|---|---|---|---|---|---|---|")
            frs = []
            for lam, v in pts:
                n = len(v)
                a = sum(ok_steady(r) for r in v)
                st = sum(ok_steady(r, True) for r in v)
                frs.append((lam, a / n))
                fl = ",".join(f"{r['fail']}@{r['t_fail']}" for r in v if r["fail"]) or "-"
                kl = np.mean([r["k"] / lam for r in v])
                qr = np.mean([r["nopen_q4"] / max(r["nopen_q1"], 1e-9) for r in v])
                nop = np.mean([r["nopen"] for r in v])
                tau = np.mean([r["nopen"] / r["k"] for r in v if r["k"] > 0]) if any(r["k"] > 0 for r in v) else float("nan")
                print(f"| {lam:.4g} | {a}/{n} | {st}/{n} | {fl} | {kl:.3f} | {qr:.2f} | {nop:.0f} | {tau:.0f} | "
                      f"{np.mean([r['maxrel'] for r in v]):.2f} | {np.nanmean([r['D'] for r in v]):.1f} | "
                      f"{max(r['maxrss_mb'] for r in v):.0f} |")
            lmax = max([lam for lam, f in frs if f >= 0.5], default=float("nan"))
            nxt = [lam for lam, f in frs if lam > lmax] if lmax == lmax else [frs[0][0]]
            capped = bool(nxt) and any(r["fail"] == "backlog" for r in dict(pts)[min(nxt)])
            top = lmax == pts[-1][0]
            t3 = HF.lam_T3(R, K)
            print(f"lam_max {lmax:.4g}{'+' if top else ''}{' (cap: next lam backlogs)' if capped else ''}; "
                  f"x Term3 {lmax / t3:.1f}; x 1/300 {lmax * 300:.0f}")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    if which == "smoke":
        smoke()
    elif which == "ph":
        run_stage(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    elif which == "merge":
        merge()
    elif which == "analyse":
        analyse()
    elif which == "plan":
        parts, est = shards(build("ph"))
        print({k: len(v) for k, v in parts.items()}, {k: round(v / 3600, 1) for k, v in est.items()},
              "total CPU-h", round(sum(est_cost(j[2]) for v in parts.values() for j in v) / 3600))
    else:
        raise SystemExit("usage: smoke | ph W | merge | analyse | plan")
