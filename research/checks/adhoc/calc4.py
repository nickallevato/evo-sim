from math import log,exp
def itr(p,s,G):
    G=int(round(G))
    for _ in range(G):
        p=p+s*p*p*(1-p)/(1+s*p*p)
    return p
def solve(f,lo,hi,t):
    for _ in range(80):
        m=(lo+hi)/2
        if f(m)<t: lo=m
        else: hi=m
    return (lo+hi)/2
p0=.44
for s in (0.0029,0.0049,0.0088):
    da=solve(lambda d: 1/(1+exp(-(log(p0/(1-p0))+900*d*log(1+s)))),0,10,.97)
    dr=solve(lambda d: itr(p0,s,900*d),0,10,.97)
    print(s,"req d additive %.2f recessive %.2f"%(da,dr))
