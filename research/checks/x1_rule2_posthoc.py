"""X1 RULE-AUDIT FIX PASS, POST HOC (not pre-registered; written after REVIEW-R4-X1-rule-audit.md, before this script was run).

Numbers the revised rule needs:
 (a) A3a charity: 35e6 + 1,140 + 2 x 187e6 (SDRs read per lineage, pairwise total) against the printed 410M; per lineage 17.5M + 187M vs 205M.
 (b) G charity: (1.01)^1474 printed 14.7; ln(1.01^1474) = 14.67; additive 14.74; required 157,000 x 0.01 = 1,570 additive, ln(1.01^157000) = 1,562;
     shortfall 107 (printed) vs the log-scale ratio.
 (c) B5c on Hancock's own EVENT basis (rule N3, revised): null = post-split events at 76 per haploid generation x 2 x 252,000 plus the ancestral SNV term
     (Yoo Ne_anc 1.32e5 -> 20.28M; 1.98e5 -> 30.4M), against 35-40M (CSAC/his range) and 42.07M (GAP-07b measured events).
 (d) B5e on Nesslig20's own basis: 37.8M + ancestral term against his stated 31-62M.
 (e) R1c elasticity: d ln(output) / d ln(Ne) for keruru's tail value (diffusion, p = 0.5, 240 generations) between 2N = 16,000 and 20,000, against a linear output (elasticity 1).
Run:  nice -n 19 research/.venv/bin/python -I research/checks/x1_rule2_posthoc.py
Expectations (informal, before the run): (a) 409.0M and 204.5M; (b) 106.5; (c) overshoot 39% vs 42.07M and about 46% vs 40M; (d) 58.1M inside 31-62M and 68.2M (HCB) about 10% above the top; (e) elasticity about -90.
"""
import math
import mpmath as mp

mp.mp.dps = 400

print("(a) A3a: parts read per lineage: 35e6 + 1,140 + 2 x 187e6 = %.4gM vs 410M (eps %.2f%%); per lineage 17.5e6 + 187e6 = %.4gM vs 205M (eps %.2f%%); literal sum 35e6 + 1,140 + 187e6 = %.4gM (eps %.0f%%)" % (
    (35e6 + 1140 + 374e6) / 1e6, 100 * abs(35e6 + 1140 + 374e6 - 410e6) / 410e6, (17.5e6 + 187e6) / 1e6, 100 * abs(17.5e6 + 187e6 - 205e6) / 205e6,
    (35e6 + 1140 + 187e6) / 1e6, 100 * abs(35e6 + 1140 + 187e6 - 410e6) / 410e6))
print("(b) G: ln(1.01^1474) = %.2f; additive 1474 x 0.01 = %.2f; required additive %.0f; ln(1.01^157000) = %.0f; ratios: additive %.1f, log %.1f (printed 107); 1.01^1474 = %.3g" % (
    1474 * math.log(1.01), 14.74, 157000 * 0.01, 157000 * math.log(1.01), 1570 / 14.74, 157000 * math.log(1.01) / (1474 * math.log(1.01)), 1.01 ** 1474))

mu, L, T = 1.2e-8, 3.2e9, 252000
ev_post = 2 * 76 * T
for lab, ne in (("HCG 1.32e5", 1.32e5), ("HCB 1.98e5", 1.98e5)):
    anc = 4 * ne * mu * L
    null = ev_post + anc
    print("(c) %s: ancestral SNV term %.2fM; event null %.2fM; vs 40M (CSAC events) %+.0f%%; vs 42.07M (GAP-07b measured) %+.0f%%; vs Hancock's own 35-40M range top %+.0f%%" % (
        lab, anc / 1e6, null / 1e6, 100 * (null / 40e6 - 1), 100 * (null / 42.07e6 - 1), 100 * (null / 40e6 - 1)))
print("(c) no-ancestral event null %.2fM: vs 40M %+.1f%%, vs 42.07M %+.1f%%" % (ev_post / 1e6, 100 * (ev_post / 40e6 - 1), 100 * (ev_post / 42.07e6 - 1)))
for lab, ne in (("HCG 1.32e5", 1.32e5), ("HCB 1.98e5", 1.98e5)):
    anc = 4 * ne * mu * L
    print("(d) Nesslig20 %s: 37.8M + %.2fM = %.2fM vs 31-62M: %+.0f%% vs the top (62M)" % (lab, anc / 1e6, (37.8e6 + anc) / 1e6, 100 * ((37.8e6 + anc) / 62e6 - 1)))


def kimura_u(p, tau, nmax=520):
    p = mp.mpf(p); x = 1 - 2 * p; tau = mp.mpf(tau)
    Pm = {0: mp.mpf(1), 1: 2 * x}
    s = p; pq = p * (1 - p)
    for n in range(1, nmax + 1):
        s += ((-1) ** n) * (2 * n + 1) / mp.mpf(n) * pq * Pm[n - 1] * mp.e ** (-n * (n + 1) * tau / 2)
        m = n
        Pm[m + 1] = ((2 * m + 3) * (2 * m + 4) * (2 * m + 2) * x * Pm[m] - 2 * (m + 1) ** 2 * (2 * m + 4) * Pm[m - 1]) / (2 * (m + 1) * (m + 3) * (2 * m + 2))
    return s

u1, u2 = kimura_u(0.5, mp.mpf(240) / 16000), kimura_u(0.5, mp.mpf(240) / 20000)
el = (mp.log(u2) - mp.log(u1)) / (mp.log(20000) - mp.log(16000))
print("(e) diffusion p=.5: u(2N=16,000) %s, u(2N=20,000) %s; elasticity d ln u / d ln(2N) = %.0f (a +-25%% change in the input moves the output by a factor of 10^%.0f)" % (
    mp.nstr(u1, 3), mp.nstr(u2, 3), float(el), abs(float(el)) * math.log10(1.25)))
