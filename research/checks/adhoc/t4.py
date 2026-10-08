import fwdpy11
N=1000;s=0.01;U=2/(2*N)
pop=fwdpy11.DiploidPopulation(N,1.0); rng=fwdpy11.GSLrng(1)
p=fwdpy11.ModelParams(nregions=[],sregions=[fwdpy11.ConstantS(0,1,1,s,0.5)],recregions=[fwdpy11.PoissonInterval(0,1,1.5)],rates=(0,U,None),gvalue=fwdpy11.Multiplicative(2.0),demography=fwdpy11.ForwardDemesGraph.tubes([N],burnin=4000,burnin_is_exact=True),simlen=4000,prune_selected=True)
fwdpy11.evolvets(rng,pop,p,100)
print(pop.generation,len(pop.fixations),len(pop.mutations), list(pop.fixation_times[:5]))

import numpy as np
print([x for x in dir(pop) if 'count' in x or 'fix' in x])
c=np.array(pop.tables.mutations and [0]) 
ms=[m for m in pop.mutations]; print(ms[0].s,ms[0].h,ms[0].g)
print(pop.mcounts[:10] if hasattr(pop,'mcounts') else '', max(pop.mcounts) if hasattr(pop,'mcounts') else '')
print(max(pop.mcounts), sorted(pop.mcounts)[-5:], pop.N, len(pop.fixation_times))
