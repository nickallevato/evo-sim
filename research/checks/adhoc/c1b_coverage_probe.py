import sys, numpy as np, importlib.util
spec=importlib.util.spec_from_file_location("c1b","/home/na/projects/evo-sim/research/checks/c1b_day_binned_statistic.py")
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
cfg=c.CONFIGS[1]
rng=np.random.default_rng(5)
rec=c.simulate_rep(cfg,rng).astype(np.float64)
NB,S=rec.shape; n=c.NB_N
print("sites",S)
for cov in (0.3,0.1,0.03,0.01):
    g=rng.binomial(n[:,None],cov,size=(NB,S)); ch=g
    s=rng.binomial(ch,rec); fx=(s==ch)&(ch>0)
    has=(ch>0)
    trk=has.all(axis=0)   # data in all bins (tracked)
    mod=fx[-1]
    for name,E in (("E2",mod&~fx[:-1].all(0)),):
        T2=np.argmax(fx,axis=0)
        for lab,mask in (("all",E),("tracked",E&trk)):
            p=np.bincount(T2[mask],minlength=NB)
            print("cov",cov,lab,"elig",mask.sum(),"prof",p.tolist(),"S21",p[4:].sum())
