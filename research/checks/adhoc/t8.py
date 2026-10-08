import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import f2_fwdpy11 as f, wf_f2 as w, numpy as np
from multiprocessing import Pool
f.s=0.03; f.BURN=1500; f.T=6000
if __name__=="__main__":
    with Pool(8) as p: r=p.map(f.run,[(0.3,0.5,100+i) for i in range(16)])
    k0=w.indep_rate(2000,0.3/2000,0.03); m,se=w.mean_se(r)
    print(m,se,k0,m/k0,se/k0)
    f.s=0.01
