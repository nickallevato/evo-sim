"""Compare the typed BLOSUM62 in l1c_alignment_method.py with the NCBI file. Usage: script NCBI_FILE SCRIPT_FILE (parsed as text, not imported/executed)."""
import re, sys
rows = [l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
cols = rows[0]; ncbi = {(r[0], cols[j]): int(v) for r in rows[1:] for j, v in enumerate(r[1:])}
src = open(sys.argv[2]).read()
blk = re.search(r'_B62 = """(.*?)"""', src, re.S).group(1).strip().splitlines()
aa = re.search(r'_AA = "(\w+)"', src).group(1)
bad = [(aa[i], aa[j], int(v), ncbi[(aa[i], aa[j])]) for i, r in enumerate(blk) for j, v in enumerate(r.split()) if int(v) != ncbi[(aa[i], aa[j])]]
n = sum(len(r.split()) for r in blk)
print("entries compared", n, "mismatches", bad)
print("symmetric in NCBI:", all(ncbi[(a, b)] == ncbi[(b, a)] for a in cols for b in cols))
xs = {(a, "X"): ncbi[(a, "X")] for a in aa}; print("NCBI A..V vs X:", sorted(set(xs.values())), "script uses -1; * vs aa:", sorted({ncbi[(a, "*")] for a in aa}), "* *:", ncbi[("*", "*")], "X X:", ncbi[("X","X")])
