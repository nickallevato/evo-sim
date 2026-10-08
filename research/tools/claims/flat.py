import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import numpy as np, wf_b3c1 as w
Ns=500; M=2*Ns; Ne=1e4; f=Ne/Ns
G=525; split=2000
P=w.wf_matrix(M)
Gs=int(round(G/f)); sp=int(round(split/f))
PA=w.mat_pow(P,sp); Pn=w.mat_pow(P,sp-Gs)
y=np.arange(M+1)/M; i=np.arange(1,M)
wt=4*Ne*1.2e-8/i
after=PA@(2*y*(1-y))
Wx=(wt*after[1:M])@Pn[1:M,:]
F=Wx[1:M]; fold=F+F[::-1]
fold=fold[:M//2]  # j=1..M/2
print("tot",Wx.sum(),"fold mean mid",fold[100:400].mean())
for j in [1,2,3,5,10,20,50,100,200]:
    print(j, j/M, fold[j-1]/fold[100:400].mean())
print("Wx[0]/mid",Wx[0]/fold[100:400].mean()," frac mass j<=5%:",fold[:50].sum()/fold.sum())
