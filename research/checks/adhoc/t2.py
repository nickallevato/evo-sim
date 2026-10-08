import sys,time; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np, wf_f2 as w
for mode,MU,M,s in [('free',8,2000,0.01),('free',32,2000,0.01),(1.5,8,2000,0.01),('clonal',32,2000,0.01),('free',20,4000,0.001)]:
    t=time.time(); r=w.sim(M,MU/M,s,mode,300,1500,np.random.default_rng(1))
    print(mode,MU,M,s,r,(time.time()-t)/1800*1000,'ms/gen')
