"""X1 FIX PASS, POST HOC (not pre-registered; written after the three X1 reviews, before this script was run).

Answers: correctness review M1 (keruru C5 matches the diffusion at 2Ne ~ 16,278 = 2 x 8,139) and M2 (Hancock "event basis fine"),
minor 7 (A5c CI), minor 10 (G07 note), and the critic-side request to give the repo's wrong 1.2e-46 against both the exact value at
2N = 20,000 (x41) and the diffusion limit (x~15).
Contents
 (1) Kimura spectral series for P(fixed by t | p0) at tau = t/(2N), mpmath 400 digits, three-term Jacobi (1,1) recurrence.
     u(p, tau) = p + sum_{n>=1} (-1)^n (2n+1)/n * p(1-p) * P_{n-1}^{(1,1)}(1-2p) * exp(-n(n+1) tau/2).
     Checked at tau = 240/20000 against the reviewer's 1.79e-45 (p = .5) and 5.8e-114 (p = .1).
 (2) 2N (and Ne = N) at which the diffusion gives keruru's stated 4e-35 (p = .5) and 6e-93 (p = .1), by bisection in log space;
     exact Wright-Fisher at 2N = 15,000 / 15,365 / 16,278 / 18,000 / 20,000 (band 10 sd), 240 generations.
 (3) A5c: neutral generations per fixation for the E. coli genome 4.6e6 at mu = 1e-11 (Hancock), 4.0e-11, 8.9e-11, 14e-11 (Wielgoss
     95% CI as quoted by McCarthy).
 (4) Hancock event-basis like-for-like (post-split supply, ancestral share, observed GAP-07b event counts).
 (5) G07: the exponent ratio.
Expectations written before the run (informal): (2) the diffusion 2N for p = .1 is ~16,3xx and for p = .5 ~15,4xx, both within 25% of
20,000; exact WF at the same 2N is within ~1 order of the diffusion value; (4) the event-basis null overshoots observed events by
>1.3x once any ancestral term is added.
Run:  nice -n 19 research/.venv/bin/python -I research/checks/x1_fix_posthoc.py
"""
import os
import math
import importlib.util
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("x1", os.path.join(HERE, "x1_critic_arithmetic.py"))
x1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x1)

mp.mp.dps = 400


def kimura_u(p, tau, nmax=520):
    p = mp.mpf(p)
    x = 1 - 2 * p
    tau = mp.mpf(tau)
    P0, P1 = mp.mpf(1), 2 * x
    s = p
    pq = p * (1 - p)
    Pm = {0: P0, 1: P1}
    prev, cur = P0, P1                         # P_{n-1}, P_n, with n = 1 -> P_{n-1} = P0
    for n in range(1, nmax + 1):
        Pn1 = prev if n == 1 else Pm[n - 1]
        term = ((-1) ** n) * (2 * n + 1) / mp.mpf(n) * pq * Pm[n - 1] * mp.e ** (-n * (n + 1) * tau / 2)
        s += term
        # next Jacobi (1,1) polynomial P_{n+1}
        m = n
        Pm[m + 1] = ((2 * m + 3) * (2 * m + 4) * (2 * m + 2) * x * Pm[m] - 2 * (m + 1) ** 2 * (2 * m + 4) * Pm[m - 1]) / (2 * (m + 1) * (m + 3) * (2 * m + 2))
    return s


def diff_at(M, p, t=240):
    return kimura_u(p, mp.mpf(t) / M)


def lg(v):
    return float(mp.log10(v)) if v > 0 else float("nan")


print("(1) diffusion limit at 2N = 20,000 (tau = 0.012): p=.5 %s ; p=.1 %s" % (mp.nstr(diff_at(20000, 0.5), 4), mp.nstr(diff_at(20000, 0.1), 4)), flush=True)

# (2) bisection for 2N
def solve(p, target):
    lo, hi = 8000.0, 40000.0                   # diffusion value decreases with M
    for _ in range(60):
        mid = (lo + hi) / 2
        v = diff_at(mid, p)
        if lg(v) > math.log10(target):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

M5 = solve(0.5, 4e-35)
M1 = solve(0.1, 6e-93)
print("(2) 2N giving keruru's 4e-35 at p=.5: %.0f (Ne %.0f); 6e-93 at p=.1: %.0f (Ne %.0f); stated 2N = 20,000; ratios %.3f, %.3f; 2 x 8,139 = 16,278" % (M5, M5 / 2, M1, M1 / 2, M5 / 20000, M1 / 20000), flush=True)
for M in (15000, 15365, 16278, 18000, 20000):
    W = int(5 * math.sqrt(M))
    out, u = x1.wf_backward(M, W, 240)
    d5, d1 = diff_at(M, 0.5), diff_at(M, 0.1)
    print("    2N=%5d exact WF p=.5 %.3g p=.1 %.3g | diffusion p=.5 %s p=.1 %s" % (M, u[M // 2], u[M // 10], mp.nstr(d5, 3), mp.nstr(d1, 3)), flush=True)
out, u = x1.wf_backward(20000, 707, 240)
ex, dl = float(u[10000]), float(diff_at(20000, 0.5))
print("    at 2N = 20,000, p = .5: repo Brownian 1.24e-46; exact WF %.3g (x%.0f over repo); diffusion limit %.3g (x%.0f over repo)" % (ex, ex / 1.24e-46, dl, dl / 1.24e-46))

# (3) A5c
for lab, mu in (("Hancock 1e-11", 1e-11), ("Wielgoss CI low 4.0e-11", 4.0e-11), ("Wielgoss 8.9e-11", 8.9e-11), ("Wielgoss CI high 14e-11", 14e-11)):
    print("(3) %-26s neutral gens/fixation %.0f (4.6e6 sites); observed LTEE 1,322 -> neutral/observed %.2f" % (lab, 1 / (4.6e6 * mu), 1 / (4.6e6 * mu) / 1322))

# (4) Hancock event basis
mu_, L, T = 1.2e-8, 3.2e9, 252000
snv_post = 2 * mu_ * T * L
ev_post = 2 * 76 * T
nonsnv_post = ev_post - snv_post
obs_snv, obs_ind = 37.77e6, 4.30e6            # GAP-07b direct count (hg38 vs panTro6), both lineages plus polymorphism
anc_resid_csac = 35e6 - snv_post
anc_resid_g7b = obs_snv - snv_post
th20, th30 = 4 * 1.32e5 * mu_ * L, 4 * 1.98e5 * mu_ * L
print("(4) post-split SNV supply %.2fM; post-split events at 76/haploid-gen %.2fM; non-SNV post-split events %.2fM vs observed indel events (total, incl. polymorphic) %.2fM (x%.1f)" % (
    snv_post / 1e6, ev_post / 1e6, nonsnv_post / 1e6, obs_ind / 1e6, nonsnv_post / obs_ind))
print("    ancestral SNV share: residual vs CSAC 35M = %.1fM; residual vs GAP-07b 37.77M = %.1fM; Yoo-Ne_anc prediction %.1fM (Ne_anc 1.32e5), %.1fM (1.98e5)" % (anc_resid_csac / 1e6, anc_resid_g7b / 1e6, th20 / 1e6, th30 / 1e6))
print("    SNV null (post-split + Yoo 1.32e5) = %.1fM vs observed 37.77M (x%.2f), vs CSAC 35M (x%.2f)" % ((snv_post + th20) / 1e6, (snv_post + th20) / obs_snv, (snv_post + th20) / 35e6))
print("    event null >= post-split events + ancestral SNV + post-split non-SNV only = %.1fM vs observed events 42.07M (x%.2f); 38.3M post-split events alone = %.0f%% of observed events" % (
    (ev_post + th20) / 1e6, (ev_post + th20) / 42.07e6, 100 * ev_post / 42.07e6))
print("    38.3M vs 42.1M measured events: %.1f%% below" % (100 * (1 - 38.3 / 42.1)))

# (5) G07
print("(5) G07: exponents 424,764 vs 65: ratio %.0f (= %.1f orders of magnitude in the exponent)" % (424764 / 65, math.log10(424764 / 65)))
