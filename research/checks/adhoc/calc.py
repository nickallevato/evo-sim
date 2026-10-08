import math
from math import comb, exp, log
def it(p,s,G):
    for _ in range(int(round(G))):
        p=p+s*p*(1-p)/(1+s*p)
    return p
def itf(p,s,G):
    # fractional generations via logit continuous approx for the haploid recursion: logit gain ln(1+s)/gen
    lg=log(p/(1-p))+G*log(1+s)
    return 1/(1+exp(-lg))
print("== C blog arithmetic")
print("350*0.45",350*.45, "20M/9My*7000",20e6/9e6*7000, 20e6/9e6)
print("== Z18525185")
print("630 =",1.2e-8*1.5e8*350, " scaled to panel 1,143,671/1.5e8:",630*1143671/1.5e8, "with 1.233013M:",630*1233013/1.5e8)
print("21/7000*6.5e6",21/7000*6.5e6, 20e6/(21/7000*6.5e6))
print("8741/16299",8741/16299, "(8741+4497)/16299",(8741+4497)/16299, "(16299-3038-... )")
print("16000/120",16000/120, "133/0.06,/0.08",133/0.06,133/0.08)
print("pre7000 share", (3038+8741+4497)/16299, 1-(3038+8741+4497)/16299)
print("== panel fraction", 1143671/3.1e9, 1211499/3.1e9)
print("Genome-wide neutral subs in 350 gens: 37.2/gen*350 =",1.2e-8*3.1e9*350)
print("scaled to panel:",1.2e-8*3.1e9*350*1143671/3.1e9)
print("== Table1 Bio-Cycle")
for name,p0,s,d,obs in [("LCT",0.01,0.05,0.45,.75),("SLC45A2",0.43,0.05,.45,.97),("TYR",0.25,0.03,.45,.76)]:
    for G in (160,200,240,280):
        print(name,G,"kimura %.4f biocyc %.4f"%(it(p0,s,G),it(p0,s,G*d)))
print("== solve G from LCT 66.2 and 99.9")
lo=0
for G in range(100,400):
    if abs(it(0.01,0.05,G*0.45)-0.662)<0.004: print("LCT G",G,it(0.01,0.05,G*.45),it(0.01,0.05,G))
print("== fox")
for G in (30,50): print(G,it(0.01,0.05,G),itf(0.01,0.05,G))
print("== d,k regression")
for k in (0,0.5,1.0): print("k=",k," d=",-2.242*k+1.229)
print("d=1 -> k=",(1.229-1)/2.242,"; d=0 -> k=",1.229/2.242, "d=0.45->k=",(1.229-.45)/2.242)
print("== dp example d=.08 s=.01 p=.01:",.08*.01*.01*.99, " 0.99/that gens",0.99/(.08*.01*.01*.99))
r=.08*.01
print("logistic 1%->99% gens",2*log(99)/r, "years at 25y", 2*log(99)/r*25)
print("== CCR5: 300gens*20=",300*20," 840 ... ")
print("== keruru: sigma",math.sqrt(.25*240/20000))
Ne=1e4; t=240; sig2=1/(2*Ne)
L=math.pi/2
z=L/math.sqrt(sig2*t)
import math
tail=math.erfc(z/math.sqrt(2))
print("z",z,"brownian-in-y tail",tail, "log10",math.log10(tail))
print("Day exp(-pi^2 Ne/T)",-(math.pi**2)*Ne/t/math.log(10))
print("4Ne gens*25 y",4*Ne*25, 240/(4*Ne))
