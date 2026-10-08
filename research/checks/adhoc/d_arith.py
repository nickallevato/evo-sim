import math
from math import log10
print("== Eden")
print("log10(20^250)=",250*log10(20), "-> 10^%.3f"%(250*log10(20)), "mantissa", 10**((250*log10(20))%1))
print("Wright's quoted 10^350 / Eden 'say 10^40' ; 20^250 vs 10^325: ratio 10^%.3f"%(250*log10(20)-325))
print("10^325 / 10^52 = 10^%d ; 10^52/10^325 = 10^-%d"%(325-52,325-52))
print("Wright 20q: log2(10^325)=%.1f bits ; /log2(20)=%.0f letters; yes/no: log2(20^250)=%.1f"%(325*math.log2(10),250,250*math.log2(20)))
print("Wright: 1e6 objects -> 20 questions: log2(1e6)=%.2f"%math.log2(1e6), " Wright's 1250 = 250*5 ; 5 > log2(20)=%.3f -> 250*log2(20)=%.0f bits"%(math.log2(20),250*math.log2(20)))
print("== Fisher/Spetner")
print("2s for s=0.001:",2*0.001,"=1/",1/(2*0.001))
p=(1/600)*(1/500); print("1/600*1/500 =",p,"=1/",1/p)
L=500*log10(300000); print("log10(300000^500)=",L,"-> %.3f x 10^%d"%(10**(L%1),int(L)))
print("reciprocal: %.3f x 10^-%d"%(10**(1-(L%1)), int(L)+1))
x=1-(1-1/300000)**1080000; print("1-(1-1/3e5)^1.08e6 =",x, " exp form:",1-math.exp(-3.6))
print("0.9727^500 =",0.9727**500, " solve p^500=1e-6 -> p=",10**(-6/500))
print("number of trials for p=0.9727 :", math.log(1-0.9727)/math.log(1-1/300000))
print("0.9727 -> n for p^500 = 1e-6 exactly: n =",math.log(1-10**(-6/500))/math.log(1-1/300000))
print("== Weasel arithmetic")
N=10000
for s in (0.05,0.001):
    t=2/s*math.log(2*N); print("s=%g  (2/s)ln(2N)=%.0f ; x27=%.0f ; (2/s)ln(N)=%.0f"%(s,t,27*t,2/s*math.log(N)))
print("Day's: 400, 11000 ; 20000, 540000 -> 20000*27 =",20000*27, " 400*27=",400*27, " ratio 540000/50=",540000/50, " 11000/50=",11000/50)
print("orders of magnitude 540000/50:",log10(540000/50))
print("12 vs 100 offspring: no formula in post uses offspring number")
