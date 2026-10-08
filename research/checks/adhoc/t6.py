import sys,time; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np, a_ltee_scaling as a, wf_f2 as w
for M,MU,s in [(2000,2,0.01),(2000,0.5,0.01),(3.3e7,0.66,0.01)]:
    t=time.time(); print(M,MU,s,a.class_rate(int(M),MU/M,s,30000,5000,np.random.default_rng(1)), w.indep_rate(int(M),MU/M,s), time.time()-t)
