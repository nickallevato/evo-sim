"""GAP-04 POST HOC (written after gap04_weissman_barton.py ran; not pre-registered). THROWAWAY research check.

Translates the Weissman & Barton (2012) asymptote Lambda -> R/2 into a number of concurrent 'active-zone'
(0.1 < p < 0.9) sweeps, for comparison with Day's Bernoulli-Barrier pipeline cap of ~230 (claim Gc, Z18167588)
and his 'Maximum fixations ~ (300,000 / 440) x 230 ~ 157,000'.

n_mid = Lambda * t_mid, t_mid = ln(81)/s (deterministic logistic time from p = 0.1 to 0.9; Day's own '440' at
s = 0.01). W&B Fig. 5 caption: interference raises mean sojourn time at intermediate frequencies "by no more than
a factor of two" -> upper value 2 t_mid. Cross-check against F2 (n_mid / rate at map 1.5 M, 2N*U_b = 32).
Also reports the unlinked-loci variance factor e^{-4 v}, v = Lambda s, at the asymptote (W&B Eq. 8).
Run: research/.venv/bin/python -I research/checks/gap04_posthoc_concurrency.py > research/checks/results/raw/gap04_posthoc.out
"""
import math

R_MAP = (35.0, 37.9)
for s in (0.001, 0.01, 0.05):
    t_mid = math.log(81) / s
    for R in R_MAP:
        L = R / 2
        n_lo, n_hi = L * t_mid, 2 * L * t_mid
        print('s = %g, R = %.1f M: Lambda = R/2 = %.2f/gen; t_mid = %.0f gen; concurrent active-zone sweeps %.3g-%.3g '
              '(%.0fx-%.0fx Day\'s 230); e^{-4 Lambda s} = %.3g' % (s, R, L, t_mid, n_lo, n_hi, n_lo / 230, n_hi / 230,
                                                                  math.exp(-4 * L * s)))
print("Day's 157,000 over 300,000 generations = %.3f fixations/gen; W&B R/2 at 35-37.9 M = 17.5-18.95/gen "
      "(%.0fx-%.0fx higher)" % (157000 / 300000, 17.5 / (157000 / 300000), 18.95 / (157000 / 300000)))
print('F2 check, map 1.5 M, 2N*U_b = 32: n_mid / rate = 207.5 / 0.363 = %.0f gen vs ln(81)/0.01 = %.0f gen' % (
    207.5 / 0.363, math.log(81) / 0.01))
