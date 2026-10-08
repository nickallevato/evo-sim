import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np
from multiprocessing import Pool
from wf2 import burn_in, schedule, evolve, pair_stats
MU=1.2e-8; T=252000; THETA=800.0; anc=1.98e5; n=500
def rep(a):
    mult,seed=a
    rng=np.random.default_rng(seed); f=anc/n; U=THETA/(4*n)
    st=burn_in(n,U,mult*n,rng)
    A=schedule([(0,1e4)],f,T)
    cp=int(round(T/f))
    sh=evolve(st,2*n,A,U,rng,[cp]); sc=evolve(st,2*n,A,U,rng,[cp])
    ps=pair_stats(sh[cp],sc[cp]); return ps['d']*MU*f/U*100
if __name__=="__main__":
    pred=(2*MU*T+4*anc*MU)*100
    with Pool(11) as p:
        for mult in (10,40):
            ss=np.random.SeedSequence([5,mult]).spawn(200)
            r=np.array(p.map(rep,[(mult,s) for s in ss]))
            print(mult, r.mean(), r.std(ddof=1)/np.sqrt(len(r)), 'pred',pred, 'ratio', r.mean()/pred, flush=True)
