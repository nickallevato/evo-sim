"""X1 POST HOC (not pre-registered).  Two numeric claims were omitted from the pre-registered row list by oversight:
B5d (relayed 7.2M) and B6 (Mansfield's full-pipe expectation E[d] = 2 mu T + theta_anc, which the claim file notes is the
hierarchy's formula, not Mansfield's verbatim words).  Plain arithmetic, no prediction beyond 'reproduces'.
Run:  research/.venv/bin/python -I research/checks/x1_posthoc_missing_rows.py
"""
mu, L, T = 1.2e-8, 3.2e9, 252000
print("B5d  6e6/25 = %d gens; x 30 = %.2fM; with 6.3 My: %.2fM; vs SNV-only 17.5M: %.2fx short; Day's '7.2 < 410' = %.1f%%" % (
    6e6 / 25, 6e6 / 25 * 30 / 1e6, 252000 * 30 / 1e6, 17.5 / 7.2, 100 * 7.2 / 410))
print("B5d  30 per generation vs pedigree haploid 38.4: %.2f; 38.4 x 240,000 = %.2fM" % (30 / 38.4, 38.4 * 240000 / 1e6))
for ne in (1e4, 1.32e5, 1.98e5):
    th = 4 * ne * mu
    tot = 2 * mu * T + th
    print("B6   Ne_anc %.3g: 2muT = %.3f%%, theta_anc = %.3f%%, E[d] = %.2f%% (observed CSAC 1.23%%)  -> %.1fM SNVs" % (ne, 100 * 2 * mu * T, 100 * th, 100 * tot, tot * L / 1e6))
print("B6   Mansfield 'X generations': full pipe needs >= 4 Ne_anc = %s generations before the split" % ", ".join("%.3g" % (4 * n) for n in (1e4, 1.32e5, 1.98e5)))
# Camestros 2026 [3] (raw ca-part3.html, read after the pre-registration): arithmetic in the post that the quote file does not carry
print("CA-3 15,000/35 = %.2f; 9e6/20/(15000/35) = %.0f (Camestros prints 1051; the 'd' factor is left out in that line: with d = 0.45 -> %.0f)" % (
    15000 / 35, 9e6 / 20 / (15000 / 35), 0.45 * 9e6 / 20 / (15000 / 35)))
print("CA-3 20,000/20 = %.0f ('fastest of that range would be 1000'); 20,000/12.5 = %.0f ('1600 consistent with 10-20 in 20,000')" % (20000 / 20, 20000 / 12.5))
