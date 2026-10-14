"""POST HOC (B1e-Q2 write-up, 2026-10-14): diagnosis of the registered P7 MISS.  Not a registered prediction.

Written after the registered main run (raw/b1e_q2.out, commit b50b6d9) printed P7 MISS, band X: the coefficient
identity held (coef_err 0.0), the finite-x0 and large-t items held, but the value item failed its 1e-30 band at
x = 0.05 (1.09e-14), 5.04 (5.45e-18) and 25.2 (3.59e-21), while x = 0.25, 1, 4 agreed to <= 1.12e-138.

Suspected cause (seen before this script was written, from the code of b1e_q2_chalub_link.py): p7_relay() builds
Chalub's side at t = mp.mpf(x) / 4 from a Python float, so x carries binary rounding (0.25, 1, 4 are exact in
binary; 0.05, 5.04, 25.2 are not), while B2f's F_dec(str(x)) gets the exact decimal.  The two functions were
evaluated at arguments ~1e-17 apart.

Expectations, written before this script ran (post hoc, descriptive; they cannot rescue the registered call):
  H1  With x passed as an exact decimal string to both sides (mp.mpf(str(x))), the relative difference between
      Chalub's x0 -> 0 limit and B2f's F_dec is <= 1e-30 at all six x (the registered band).
  H2  The first-order prediction |d ln F/dx| * |mp.mpf(float x) - x| reproduces each printed registered relative
      difference within a factor 1.1 at x = 0.05, 5.04, 25.2, and is exactly 0 at x = 0.25, 1, 4.
If H1 fails, the registered MISS stands as a real difference and the write-up says so.

Coefficients: (-1)^n (2n+3) for the x0 -> 0 limit, the identity the registered run confirmed (coef_err 0.0).
Run (local, trivial): research/.venv/bin/python -I research/checks/b1e_q2_posthoc_p7.py \
        > research/checks/results/raw/b1e_q2_posthoc_p7.out 2>&1
"""
import importlib.util
import os

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
XS = [0.05, 0.25, 1, 4, 5.04, 25.2]                       # the registered grid, as floats
PRINTED = {0.05: "1.09e-14", 0.25: "1.12e-138", 1: "7.08e-157", 4: "1.07e-160", 5.04: "5.45e-18", 25.2: "3.59e-21"}
NMODES = 201


def load_b2f():
    spec = importlib.util.spec_from_file_location("b2f", os.path.join(HERE, "b2f_finite_time_formula.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lam(n):
    return (n + 1) * (n + 2)


def F_lim(x):
    t = x / 4
    assert lam(NMODES - 1) * t > 190 * mp.log(10), ("too few modes", x)
    return 1 - sum((-1) ** n * (2 * n + 3) * mp.exp(-lam(n) * t) for n in range(NMODES))


def dF_dx(x):
    t = x / 4
    return sum((-1) ** n * (2 * n + 3) * lam(n) / 4 * mp.exp(-lam(n) * t) for n in range(NMODES))


def main():
    mp.mp.dps = 170
    b2f = load_b2f()
    h1 = True
    h2 = True
    print("x | rel(exact decimal x) | registered printed rel | first-order prediction | prediction/printed")
    for x in XS:
        xe = mp.mpf(str(x))
        xf = mp.mpf(x)
        Fb = mp.mpf(str(b2f.F_dec(str(x))))
        rel = abs(F_lim(xe) - Fb) / abs(Fb)
        pred = abs(dF_dx(xe) / F_lim(xe)) * abs(xf - xe)
        printed = mp.mpf(PRINTED[x])
        ratio = pred / printed if pred != 0 else mp.mpf(0)
        h1 &= rel <= mp.mpf("1e-30")
        if xf == xe:
            h2 &= pred == 0
        else:
            h2 &= mp.mpf(1) / mp.mpf("1.1") <= ratio <= mp.mpf("1.1")
        print(x, "|", mp.nstr(rel, 3), "|", PRINTED[x], "|", mp.nstr(pred, 3), "|", mp.nstr(ratio, 4),
              "| x float-exact" if xf == xe else "| x rounded in binary")
    print(f"H1 (all six <= 1e-30 with exact x): {'HOLDS' if h1 else 'FAILS'}")
    print(f"H2 (first-order prediction within 1.1x of printed; 0 where x exact): {'HOLDS' if h2 else 'FAILS'}")


if __name__ == "__main__":
    main()
