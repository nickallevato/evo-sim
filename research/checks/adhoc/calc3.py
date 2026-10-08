from math import comb, exp, log
print("== E strict col sum")
strict=[66,73,14,9,27,98,1572,1601,268,94,796,878]
naive=[66,80,63,96,59,115,1838,2594,621,1094,820,1233]
within=[0,0,105,173,107,50,447,1756,1692,1816,0,1020]
print(sum(strict),sum(naive),sum(within), sum(naive)-sum(strict))
print("nonmut strict",sum(strict[:5]),sum(strict[:5])/5,60000/(sum(strict[:5])/5))
print("nonmut naive",sum(naive[:5]),sum(naive[:5])/5,60000/(sum(naive[:5])/5))
print("(8679-5496)/8679",(8679-5496)/8679,"8679/5496-1",8679/5496-1, "5496/8679",5496/8679)
print("mut strict",sum(strict[5:]),"naive",sum(naive[5:]))
print("popgens", 60500+60000+57500+60500+60000+60000+60000+63500+60500+60000+60500+60000)
print("Z23003785 table 60K:",(64+68+0+60+35),(64+68+0+60+35)/5, 60000/45.4, "w/o Ara+5:",(64+68+60+35)/4, 60000/((64+68+60+35)/4))
print("avg per decile 12.6..: ", [ (794,12.6)])
print("mutator mean incl -906:",(110+932+803+978-906+273+1153)/7, 50000/((110+932+803+978-906+273+1153)/7))
m6=(110+932+803+978+273+1153)/6; print("excl Ara-2",m6,50000/m6, 893/(50000/m6))
print("ratios 893/104.7",893/104.7,"1322/78",1322/78,"avg",(893/104.7+1322/78)/2)
print("== 2.3% hazard")
p=0.0036
def binom_ge2(n,p): return 1-(1-p)**n-n*p*(1-p)**(n-1)
print("P>=2 carriers N=100 p=.0036",binom_ge2(100,p))
q=0.0018
print("alleles 200 q=.0018 P>=2",binom_ge2(200,q), "P>=1",1-(1-q)**200)
print("0.06*0.39",0.06*0.39,"1-e^-.5",1-exp(-.5),"0.0509*0.3935",binom_ge2(100,p)*(1-exp(-.5)))
print("sim table: 0.051*0.147",0.051*0.147)
print("cum 10,50,100 founder:",[1-(1-0.0233)**n for n in (10,50,100,500)])
# Clopper-Pearson 6/12
def cdf(k,n,p): return sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(0,k+1))
def solve(f,lo,hi):
    for _ in range(100):
        m=(lo+hi)/2
        if f(m)>0: lo=m
        else: hi=m
    return (lo+hi)/2
n=12;k=6
lower=solve(lambda p: -(1-cdf(k-1,n,p)-0.025) ,0,1) # find p where P(X>=k)=0.025
# P(X>=k) increasing in p; want root
def f_low(p): return (1-cdf(k-1,n,p))-0.025
def f_up(p): return cdf(k,n,p)-0.025
def bis(f,lo,hi,inc):
    for _ in range(100):
        m=(lo+hi)/2
        if (f(m)<0)==inc: lo=m
        else: hi=m
    return (lo+hi)/2
lowp=bis(f_low,0,1,True); upp=bis(f_up,0,1,False)
print("CP 6/12",lowp,upp)
print("== s_min")
for K,T in ((5,5000),(20,5000),(50,5000),(200,5000),(12,5000),(28,3333)): print(K,T,2*K*log(1000)/T)
print("sweep time Ne=500:", [2/s*log(1000) for s in (.01,.05,.1,.009)])
print("K_new rows:",[(1-f)*K/P for K,f,P in ((50,.5,5),(100,.4,5),(100,.6,8),(150,.3,5),(100,.2,3),(200,.3,5),(200,.7,10))])
print("== H")
print("146250/300",146250/300,"20e6/487",20e6/487, "20e6/487.5",20e6/487.5,"1600/300",1600/300,"487/91",487/91)
print("30N/0.1N",30/0.1)
print("642888/146250",642888/146250,"*2e7",642888/146250*2e7, "88e6/ ",)
print("321444*2",321444*2, "11739*2",11739*2)
print("87916307/20e6",87916307/20e6)
print("Term3 ksel human (smax=1,d=.45,L=3.1e9,Ne=1e4):",0.45/(2*3.1e9*log(2e4)), " K_sel per gen:",0.45/(2*log(2e4)), "gens/sub",2*log(2e4)/0.45)
print(" ->over 146250 eff gens:",0.45/(2*log(2e4))*325000, " over 252000:",0.45/(2*log(2e4))*252000)
print("Keightley: e^-2.2",exp(-2.2),"e^-0.35",exp(-0.35),"20*(1-.1108)",20*(1-exp(-2.2)))
print("Hossjer",9e6*.45/(20*1600),127*125,1.25e-8/1e-10*127, 3e9/4.6e6*15800, 3e9*.45*1.25e-8*450000)
print("Nunney M=2Ku K=1e4 u=5e-6",2*1e4*5e-6, " K for M=.5",0.5/(2*5e-6))
