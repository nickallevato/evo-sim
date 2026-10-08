import fwdpy11, numpy as np
N=1000
for L in (1,):
    pop=fwdpy11.DiploidPopulation(N,1.0); rng=fwdpy11.GSLrng(3)
    p=fwdpy11.ModelParams(nregions=[],sregions=[fwdpy11.ConstantS(0,1,1,1e-6,0.5)],recregions=[fwdpy11.PoissonInterval(0,1,1.0)],rates=(0,0.1,None),gvalue=fwdpy11.Multiplicative(2.0),demography=fwdpy11.ForwardDemesGraph.tubes([N],burnin=L,burnin_is_exact=True),simlen=L)
    fwdpy11.evolvets(rng,pop,p,100)
    print(L,len(pop.mutations), 'expected per-gamete', 2*N*0.1, 'per-diploid', N*0.1, 'gen',pop.generation)
