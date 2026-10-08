import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np
from multiprocessing import Pool
from wf2 import burn_in, schedule, evolve
T_REAL=252000; THETA=800.0
def rep(a):
    mult, seed = a
    anc=1.98e5; n=500; f=anc/n; U=THETA/(4*n)
    rng=np.random.default_rng(seed)
    state=burn_in(n,U,mult*n,rng)
    N=schedule([(0,anc)],f,T_REAL)
    s=evolve(state,2*n,N,U,rng)[len(N)]
    return (s['pre_fixed']+s['post_fixed'])/(U*len(N))
if __name__=="__main__":
    with Pool(12) as p:
        for mult in (10,20,40):
            ss=np.random.SeedSequence([77,mult]).spawn(240)
            r=np.array(p.map(rep,[(mult,s) for s in ss]))
            print(mult, r.mean(), r.std(ddof=1)/np.sqrt(len(r)), flush=True)
