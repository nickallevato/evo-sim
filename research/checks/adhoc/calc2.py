from math import log,exp
def it(p,s,G):
    for _ in range(int(round(G))):
        p=p+s*p*(1-p)/(1+s*p)
    return p
def itr(p,s,G): # recessive beneficial (hom fitness 1+s)
    for _ in range(int(round(G))):
        p=p+s*p*p*(1-p)/(1+s*p*p)
    return p
def itd(p,s,G): # dominant beneficial
    for _ in range(int(round(G))):
        q=1-p
        w=(1+s)*(1-q*q)+q*q
        p=p+ s*p*q*(1+... ) if False else ( (1+s)*(p*p+p*q)+0*q*0 )/w  # AA,Aa have 1+s ; aa 1  -> p' = (1+s)(p^2+pq)/w
    return p
def solve(f,lo,hi,target):
    for _ in range(80):
        m=(lo+hi)/2
        if f(m)<target: lo=m
        else: hi=m
    return (lo+hi)/2
cases=[("LCT",0.01,0.05,240,.75),("SLC45A2",0.43,0.05,160,.97),("TYR",0.25,0.03,200,.76)]
for n,p0,s,G,obs in cases:
    d=solve(lambda d: it(p0,s,G*d),0.0,1.0,obs)
    # fractional gens: use continuous approx for solving
    from math import log
    def itc(p0,s,Geff):
        lg=log(p0/(1-p0))+Geff*log(1+s); return 1/(1+exp(-lg))
    d2=solve(lambda d: itc(p0,s,G*d),0.0,1.0,obs)
    sk=solve(lambda s_: itc(p0,s_,G),0.0,1.0,obs)
    sb=solve(lambda s_: itc(p0,s_,G*.45),0.0,1.0,obs)
    print(n,"required d (s fixed) %.3f"%d2,"required s kimura %.4f  required s bio(d=.45) %.4f  product s*d %.4f"%(sk,sb,sb*.45))
# chicken
p0=.44; s=0.0049
for G,d in ((900,1),(900,.45)):
    print("chicken additive",G,d,it(p0,s,G*d),"recessive",itr(p0,s,G*d))
print("req d for 0.97 additive:", solve(lambda d: 1/(1+exp(-(log(p0/(1-p0))+900*d*log(1+s)))),0,2,.97))
print("req d for 0.97 recessive:", solve(lambda d: itr(p0,s,900*d),0,3,.97))
# Table 3 product
for d,sa,st in ((.4,.058,.028),(.5,.047,.023),(.6,.038,.019),(1.0,.023,.011)): print(d,sa*d,st*d,st/sa)
# Hill ratio
print("Hill N_e/(N1 T)= 2/(2+Vk):", [round(2/(2+v),3) for v in (2,4,5,7,8)])
