import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np
from wf import single_locus, diffusion_cond_fix_time
rng=np.random.default_rng(20261007)
N=10000
for s in (0.05,0.001):
    print("s",s,"diffusion cond fix time:",round(diffusion_cond_fix_time(N,s)),"  Day (2/s)ln2N:",round(2/s*np.log(2*N)))
# simulate conditional fixation times
res={}
for s,reps in ((0.05,60000),(0.001,1_200_000)):
    fixed,t=single_locus(N,s,reps,rng)
    tf=t[fixed]; res[s]=tf
    print("s",s,"reps",reps,"n_fixed",len(tf),"P(fix) %.5f (2s=%.3f; Kimura %.5f)"%(len(tf)/reps,2*s,(1-np.exp(-2*s))/(1-np.exp(-4*N*s))),"mean %.0f +- %.0f"%(tf.mean(),tf.std()/np.sqrt(len(tf))),"sd %.0f"%tf.std())
    # serial sum of 27 vs parallel max of 27 (independent loci, no linkage/interference), bootstrap
    b=np.random.default_rng(1)
    S=b.choice(tf,(20000,27)); 
    print("   27 serial letters: mean total %.0f ; parallel (max of 27 independent) mean %.0f  p5-p95 %.0f-%.0f"%(S.sum(1).mean(),S.max(1).mean(),*np.percentile(S.max(1),[5,95])))
