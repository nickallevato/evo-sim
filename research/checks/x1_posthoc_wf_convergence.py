"""X1 POST HOC (not pre-registered; written after the X1 main run).  Why: the pre-registered prediction for keruru's C5 claim
(exact Wright-Fisher absorption probability within 240 generations from p = 0.5, 2N = 20,000) was 1e-47 to 1e-45; the run gave
5.1e-45, a factor ~41 above the repo's Brownian arcsine value 1.2e-46 and outside the predicted band.  This script checks that the
exact number is not a numerical artefact: (1) band half-width W (700 vs 1,000 copies); (2) scaling in M at fixed t/M = 0.012
(M = 2,000 .. 40,000; W = 10 sd; a first draft with W = 0.035 M was too narrow at small M and is discarded), where the exact value divided by the one-boundary arcsine-Gaussian value should settle to a constant if the
difference is a real diffusion-limit correction (drift term of the arcsine transform, third-order terms) and not a truncation error.
Run:  nice -n 19 research/.venv/bin/python -I research/checks/x1_posthoc_wf_convergence.py
"""
import os
import math
import importlib.util
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("x1", os.path.join(HERE, "x1_critic_arithmetic.py"))
x1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x1)


def one(M, t, W, p=0.5):
    out, u = x1.wf_backward(M, W, t)
    val = float(u[int(round(p * M))])
    sig = math.sqrt(t / M)
    gauss = float(norm.sf((math.pi - 2 * math.asin(math.sqrt(p))) / sig))
    return val, gauss


for M, t in ((2000, 24), (5000, 60), (10000, 120), (20000, 240), (40000, 480)):
    W = int(5 * math.sqrt(M))          # ~10 binomial sd at p = 0.5 (the first draft used 0.035 M, only 3 sd at M = 2,000: truncation)
    v, g = one(M, t, W)
    print("M=%6d t=%4d W=%5d exact=%.4g gauss1=%.4g ratio=%.1f" % (M, t, W, v, g, v / g), flush=True)
v, g = one(20000, 240, 1000)
print("M= 20000 t= 240 W= 1000 exact=%.4g gauss1=%.4g ratio=%.1f" % (v, g, v / g))
# ratio of p = 0.1 and 0.99 at M = 20000, W = 1000
out, u = x1.wf_backward(20000, 1000, 240)
for p in (0.1, 0.5, 0.9, 0.99):
    print("p=%.2f exact=%.4g" % (p, u[int(round(p * 20000))]))
