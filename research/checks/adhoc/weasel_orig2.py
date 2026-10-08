import numpy as np
rng=np.random.default_rng(20261008)
L=28; A=27
def run(N,P,reps,elite,diff):
    out=[]
    for _ in range(reps):
        cur=rng.integers(0,A,L); g=0
        while (cur!=0).any():
            g+=1
            kids=np.tile(cur,(N,1)); mut=rng.random((N,L))<P
            if diff: newl=(kids+rng.integers(1,A,(N,L)))%A
            else: newl=rng.integers(0,A,(N,L))
            kids=np.where(mut,newl,kids)
            if elite: kids=np.vstack([kids,cur])
            sc=(kids==0).sum(1); cur=kids[np.argmax(sc)]
            if g>100000: break
        out.append(g)
    return np.array(out)
for elite in (False,True):
    for diff in (False,True):
        r=run(100,0.05,400,elite,diff); print("N=100 P=.05 elite=%s mutation-always-different=%s: mean %.1f median %.0f"%(elite,diff,r.mean(),np.median(r)))
