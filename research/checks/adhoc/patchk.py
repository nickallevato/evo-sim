p='/home/na/projects/evo-sim/research/checks/h_keightley_load.py'
s=open(p).read()
s=s.replace("import numpy as np\nimport wf_hc as h","import numpy as np\nfrom multiprocessing import Pool\nimport wf_hc as h")
a=s.index("def run(")
new='''def one(a):
    Fmax, regime, s, e, seed = a
    return h.mutload_run(K, U, s, Fmax, regime, gens, np.random.default_rng(np.random.SeedSequence(seed)), epistasis=e)


def summarize(outs):
    ext = sum(o["extinct"] for o in outs)
    live = [o for o in outs if not o["extinct"]]
    if not live:
        return f"extinct {ext}/{len(outs)}"
    f = lambda key: (np.mean([o[key] for o in live]), np.std([o[key] for o in live], ddof=1) / np.sqrt(len(live)) if len(live) > 1 else np.nan)
    N, W, k = f("Nfrac"), f("w"), f("kbar")
    return f"extinct {ext}/{len(outs)}  N/K={N[0]:.3f}±{N[1]:.3f}  mean w(adults)={W[0]:.4f}±{W[1]:.4f}  mean k={k[0]:.1f}"


if __name__ == "__main__":
    print(f"U={U}, e^-U={np.exp(-U):.4f}; hard persistence threshold Fmax > {2*np.exp(U):.1f}; K={K}, {reps} reps, {gens} gens", flush=True)
    jobs, keys, c = [], [], 0
    for (s, e, lab) in [(0.05, 0.0, "multiplicative s=0.05 (k_eq ~ U/s = 44)"),
                        (0.01, 0.0004, "synergistic w=exp(-0.01k-0.0004k^2)")]:
        for Fmax in (4, 8, 12, 17, 20, 30, 60):
            for reg in ("hard", "soft"):
                for r in range(reps):
                    c += 1
                    jobs.append((Fmax, reg, s, e, 20261009 * 1000 + c))
                keys.append((lab, s, e, Fmax, reg))
    with Pool(12) as p:
        res = p.map(one, jobs, chunksize=1)
    last = None
    for i, (lab, s, e, Fmax, reg) in enumerate(keys):
        if lab != last:
            print("\\n##", lab); last = lab
        pred = ""
        if e == 0 and reg == "hard" and Fmax > 2 * np.exp(U):
            pred = f"  [pred N/K={1 - U/np.log(Fmax/2):.3f}]"
        print(f" Fmax={Fmax:<3} {reg:4s}: {summarize(res[i*reps:(i+1)*reps])}{pred}")
'''
s=s[:a]+new
s=s.replace("reps = 6\ngens = 600\nss = np.random.SeedSequence(20261009)\n","reps = 6\ngens = 500\n")
open(p,'w').write(s)
