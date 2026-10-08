import numpy as np
rng=np.random.default_rng(20261007)
L=28; A=27
def run(N,P,reps):
    out=[]
    for _ in range(reps):
        cur=rng.integers(0,A,L); tgt=np.zeros(L,dtype=int)  # target = all zeros WLOG
        g=0
        while (cur!=0).any():
            g+=1
            kids=np.tile(cur,(N,1))
            mut=rng.random((N,L))<P
            # mutation to a random letter (may equal the old one: Dawkins-style 'random letter')
            kids=np.where(mut,rng.integers(0,A,(N,L)),kids)
            sc=(kids==0).sum(1)
            best=kids[np.argmax(sc)]
            # keep parent if no child better (Dawkins keeps best child; ties/regression allowed)
            cur=best
            if g>100000: break
        out.append(g)
    return np.array(out)
for N,P in ((100,0.05),(12,0.05),(100,0.01)):
    r=run(N,P,300); print("N=%d P=%.2f  mean gens %.1f  median %.0f  p5-p95 %.0f-%.0f"%(N,P,r.mean(),np.median(r),*np.percentile(r,[5,95])))
