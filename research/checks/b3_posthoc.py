"""B3 post hoc recomputation -- post hoc, after reviews 33e190a (correctness, steelman-day, steelman-critic).

Not pre-registered: deterministic arithmetic requested by the reviews; no prediction is scored.
Inputs as in b3_family_reconstruction.py (04f96bd): k/mu = count / (T mu L); neutral expectation with
ancestral polymorphism per lineage = mu (T + 2 N_anc) per site.  Rows:
  A  residual at R1/N3's mandated N_anc 1.32e5 and 1.98e5 (5.7e4 Day-implied and 1e4 textbook as sensitivities),
     events row (21.05e6 / 3.1e9) and SNV-per-aligned-site row (37.77e6/2 over 2.81e9), at human 1.2e-8 and Bergeron 7.97e-9.
  B  split-time rows 6.3 / 7.0 / 7.5 / 8.0 My at 25 y (Langergraber 2012 >= 7-8 My, parameters.yaml).
  C  29 y sensitivity with the expectation re-evaluated at T = 217,000.
  D  unit-only materiality (Bergeron mu held) and mu-only swap (205e6 at human mu).
  E  Yoo's own SDR per lineage (327 Mb, A3x1) + 17.5e6 SNV; exact-match inputs for 32.3.
  F  Day-basis ancestral term on the SNV part only (Q100: SVs post-divergence).
  G  base pairs like for like: 205e6 / (9.4e6 SNV + 357-517e6 de novo SV bp expected, gaps.md R4 2026-10-08).
"""
L, Laln, T0 = 3.1e9, 2.81e9, 252000
MUH, MUB = 1.2e-8, 7.97e-9
EV, SNVA = 21.05e6, 37.77e6 / 2

def res(c, mu, l, T, Na):
    return c / (mu * l * (T + 2 * Na))

print("## A residual (T = 252,000)")
for Na in (1.32e5, 1.98e5, 5.7e4, 1e4):
    print(f"N_anc {Na:.3g}: events human {res(EV,MUH,L,T0,Na):.2f} Bergeron {res(EV,MUB,L,T0,Na):.2f} | "
          f"SNV/aligned human {res(SNVA,MUH,Laln,T0,Na):.2f} Bergeron {res(SNVA,MUB,Laln,T0,Na):.2f}")
print("## B split time (events, 25 y)")
for My in (6.3, 7.0, 7.5, 8.0):
    T = My * 1e6 / 25
    print(f"{My} My: no anc human {res(EV,MUH,L,T,0):.2f}; 1.32e5 human {res(EV,MUH,L,T,1.32e5):.2f} Bergeron {res(EV,MUB,L,T,1.32e5):.2f}; "
          f"1.98e5 human {res(EV,MUH,L,T,1.98e5):.2f} Bergeron {res(EV,MUB,L,T,1.98e5):.2f}")
print("## C 29 y (T = 217,000), events human")
for Na in (1e4, 5.7e4, 1.32e5, 1.98e5):
    print(f"N_anc {Na:.3g}: {res(EV,MUH,L,217000,Na):.2f}")
print("## D materiality")
for lab, c in (("events", EV), ("fixed", 17.8e6)):
    print(f"unit only (Bergeron mu): 32.93 / {lab} {res(c,MUB,L,T0,0):.2f} = {res(205e6,MUB,L,T0,0)/res(c,MUB,L,T0,0):.1f}x")
print(f"mu only: 205e6 at human mu = {res(205e6,MUH,L,T0,0):.1f}")
print(f"SNV floor 17.5e6: Bergeron {res(17.5e6,MUB,L,T0,0):.2f} human {res(17.5e6,MUH,L,T0,0):.2f}")
print("## E Yoo / exact match")
print(f"Yoo 327e6 + 17.5e6: {res(327e6+17.5e6,MUB,L,T0,0):.1f}; 327e6 alone {res(327e6,MUB,L,T0,0):.1f}")
print(f"exact 32.3 needs T = {205e6/(32.3*MUB*L):.0f}, or L = {205e6/(32.3*MUB*T0):.3g}, or count = {32.3*MUB*L*T0:.4g}")
print("## F Day basis, ancestral term on SNV part")
for Na in (1.32e5, 1.98e5):
    c = 205e6 - 2 * Na * MUB * L
    print(f"N_anc {Na:.3g}: subtract {2*Na*MUB*L/1e6:.1f}M -> {res(c,MUB,L,T0,0):.2f}")
print("## G bp like for like")
for sv in (357e6, 517e6):
    print(f"SV bp {sv/1e6:.0f}M: {205e6/(9.4e6+sv):.2f}")
