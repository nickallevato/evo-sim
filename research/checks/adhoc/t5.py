import fwdpy11, numpy as np
N=1000;s=0.01;U=2/(2*N)
pop=fwdpy11.DiploidPopulation(N,1.0); rng=fwdpy11.GSLrng(1)
def params(L):
    return fwdpy11.ModelParams(nregions=[],sregions=[fwdpy11.ConstantS(0,1,1,s,0.5)],recregions=[fwdpy11.PoissonInterval(0,1,1.5)],rates=(0,U,None),gvalue=fwdpy11.Multiplicative(2.0),demography=fwdpy11.ForwardDemesGraph.tubes([N],burnin=L,burnin_is_exact=True),simlen=L,prune_selected=False)
def nfixed(pop): return int((np.array(pop.mcounts)==2*N).sum())+len(pop.fixations)
fwdpy11.evolvets(rng,pop,params(2000),100); a=nfixed(pop); print(pop.generation,a)
fwdpy11.evolvets(rng,pop,params(2000),100); b=nfixed(pop); print(pop.generation,b)
