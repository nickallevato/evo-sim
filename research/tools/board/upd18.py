# 2026-10-12: owner decision O-8 (DECISIONS.md): remove Day-versus-critic comparative rates and Fisher p-values from the board; keep raw counts per side
p = 'status.html'; s = open(p).read()
a = s.index("    <li><b>Primary measure</b> (claims with a number in the author's quoted words)")
b = s.index("</ol>", a)
new = ('''    <li><b>Error verdicts, raw counts per side.</b> Primary measure (a number in the author's quoted words): Day 13 of 81, critics 1 of 20. Formal-statement measure: Day 16 of 82, critics 1 of 31. All claims: Day 18 of 114, critics 1 of 51.</li>
    <li><b>Not comparable between sides.</b> Raw counts are shown, but rates are not comparable: the two sides differ in volume, in the precision of their claims, in the share of claims checked, and in how claims were routed (method audit MA-06). No test of difference is reported.</li>
  ''')
s = s[:a] + new + s[b:]
open(p, 'w').write(s)
print("ok")
