import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np
from scipy.stats import binom
from wf import *
def chain(N,s):
    M=2*N; k=np.arange(M+1); p=k/M; p=p*(1+s)/(1+s*p)
    P=binom.pmf(k[None,:],M,p[:,None])
    Q=P[1:M,1:M]; R=P[1:M,M]
    I=np.eye(M-1)
    Nf=np.linalg.inv(I-Q)
    h=Nf@R           # fixation prob
    # conditional time: E[T 1{fix}] = N h-weighted
    th=np.linalg.solve(I-Q, h)  # sum_t P(not absorbed by t, fix eventually) ... E[T;fix]=(I-Q)^-1 h
    return h[0], th[0]/h[0]
for N,s in ((50,0),(200,0),(100,.01),(500,.01),(1000,.005),(2500,.01)):
    u,t=chain(N,s)
    print(N,s,'exact u',u,'kimura',kimura_u(N,s),'exact tfix',t, 'diff',diffusion_cond_fix_time(N,s),'t/N',t/N)
# diffusion small s continuity
for s in (0,1e-9,1e-7,1e-5): print(s,diffusion_cond_fix_time(100,s))
# stoch forms
for N,s in((5000,.01),(500,.01),(10000,.001)):
    print(N,s,2/s*(np.log(4*N*s)+0.5772),2/s*(np.log(2*N*s)+0.5772))
# burn-in residual: empty-start flux deficit at 10N
rng=np.random.default_rng(1)
N=100
f,t=single_locus(N,0,1000000,rng); tf=np.sort(t[f]); 
for x in (5*N,10*N,15*N): print('1-F',x,1-np.searchsorted(tf,x,side='right')/len(tf))
