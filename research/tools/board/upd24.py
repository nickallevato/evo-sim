# 2026-10-18: board patch for B-R30 (EVO-92, step (i) of D-26). The reviews #66-#69 entry stated "H, H8, H5 external stay
# contested" bare. The scope is now on the page in the B-R25 shape (the scope line first, then the value), composed only from
# the verdict_scope line that hierarchy.yaml and the H, H8 and H5 claim files already carry, verbatim. No verdict value moves
# and no verdict field is set. Run from docs/research/. Patches status.html in place; the anchor assert stops a second run.
p = 'status.html'; s = open(p).read()
assert 'upd24' not in s and 'upd23 applied' in s
old = "Day's 1/300 conservative at R = 1.111; H, H8, H5 external stay contested</li>"
new = ("Day's 1/300 conservative at R = 1.111; H, H8, H5 external stay contested, with the same scope for all three (verdict_scope): "
       "'slower than 1/300' stays conditional on K (tested to 64,000) and on the survival horizon</li>")
assert s.count(old) == 1
s = s.replace(old, new, 1)
assert s.count('<!-- upd23 applied 2026-10-13 -->') == 1
s = s.replace('<!-- upd23 applied 2026-10-13 -->', '<!-- upd24 applied 2026-10-18 -->\n<!-- upd23 applied 2026-10-13 -->', 1)
open(p, 'w').write(s)
