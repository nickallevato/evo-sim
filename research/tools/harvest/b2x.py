import numpy as np
from scipy.stats import binom
res={}
for N in (100,200,400,800,1600):
    M=2*N; st=np.arange(M+1)
    P=binom.pmf(st[None,:],M,st[:,None]/M)
    v=np.zeros(M+1); v[1]=1
    out={}
    G=N
    for g in range(1,G+1):
        v=v@P
        for r in (0.25,0.5,1.0):
            if g==int(r*N): out[r]=np.log(v[M]*M)
    res[N]=out
    print(N,{r:round(-np.pi**2*N/ (r*N)*0+ (r*out[r]),3) for r in out},flush=True)
