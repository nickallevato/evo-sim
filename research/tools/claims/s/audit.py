from math import log, exp, pi, log10
print("McCarthy: 100*1e4/20 =",100*1e4/20,"/yr; x9e6 =",100*1e4/20*9e6,"; /20000 =",100*1e4/20*9e6/2e4)
print(" per gen: 100*1e4=1e6 *450000 =",1e6*450000," /20000 =",1e6*450000/2e4, "; 50/gen*450000=",50*450000)
print(" time-adj Day's form: (450000-50000)*50 =",400000*50,"; Day's T-4Ne:",(450000-40000)*50)
print(" 400e9/20000=",400e9/2e4)
# Mansfield
print("Mansfield: 1/gen x450000 =",450000,"; 20e6/450000=",20e6/450000,"; 17.5e6/252000 =",17.5e6/252000,"; 35e6/2/252000 ",35e6/2/252000)
for f in (0.02,):
    print(" f*100*N/(2N)=",f*100/2,"/gen (only 2 muts => 1/gen).")
print(" neutral fraction needed (100 muts/newborn, 450k gens, 20M):",20e6/(450000*50)," ; 252k gens, 17.5M:",17.5e6/(252000*50)," ; with 70 muts:",17.5e6/(252000*35))
print(" 70muts all neutral per-lineage:",35*252000)
# Hancock
print("Hancock: 6.4e9*1.2e-8=",6.4e9*1.2e-8,"; haploid ",3.2e9*1.2e-8,"; x2x252000:",3.2e9*1.2e-8*2*252000,"; 76.8x2x252000:",76.8*2*252000)
print(" 19.35/35 =",19.35/35, "35/19.35=",35/19.35, " fixed-fraction 0.78-0.86 of 35M:",0.78*35,0.86*35)
print(" 205M/ (2*252000)=",205e6/(252000),"(per-gen on one lineage); Hancock 407 =205e6/ (2*252000)=",205e6/504000)
print(" Hancock E coli: 4e-5 -> 1/4e-5=",1/4e-5,"; 4.6e6*1e-11=",4.6e6*1e-11,"->",1/(4.6e6*1e-11)," ; 8.9e-11:",1/(4.6e6*8.9e-11))
# Nesslig
print("Nesslig: 2*75*252000=",2*75*252000, "; 2*75*6.3e6/25", 2*75*6.3e6/25, "; haploid 37.5:",2*37.5*252000)
# relayed 7.2M
print("Relayed: 6e6/25*30=",6e6/25*30,"; 6.3e6/25*30=",6.3e6/25*30,"; vs 17.5M:",17.5e6/7.2e6,"vs 205M",205e6/7.2e6,"vs 7.56M")
# Day IR
mu=1.2e-8
print("IR: 30*252000=",30*252000,"; Ne=1e4:",30*(252000-4e4),30*4e4,30*4e4/(30*252000)," Ne=5e4:",30*(252000-2e5),30*2e5/(30*252000),"Ne=63000 4Ne",4*63000)
print(" theta: 4*1e4*1.2e-8*3e9 =",4*1e4*1.2e-8*3e9," /410e6=",4*1e4*1.2e-8*3e9/410e6, " vs loss 1.2M ratio",1.44e6/1.2e6," vs 2.4M",1.44/2.4)
for Ne in (1e4,1.32e5,1.98e5):
    th=4*Ne*mu; print(" Ne",Ne,"theta/site",th," x3.2e9=",th*3.2e9," 2muT/site",2*mu*252000," total/site",th+2*mu*252000)
print(" 2*mu*252000*3.2e9=",2*mu*252000*3.2e9)
# Day blog 8.25
print("Day corrected:",100*3300*400000/(2*8e9),"; 20e6/8.25=",20e6/8.25,"; 20e6/150000",20e6/150000)
print(" opposite-direction (supply N=8e9, fix 1/2Ne): k/mu=",8e9/3300, " vs his Ne/N=",3300/8e9, "; 20M*N/Ne ratio:",20e6*8e9/1e4)
print(" 1/(2*1e4*1.5e-8)=",1/(2*1e4*1.5e-8))
# pipes
for N in (1e5,1e6,8e9,8.2e9):
    ne=(4*N-2)/(5+2); print("Wright Vk=5: N",N,"Ne",ne,"4Ne",4*ne)
print(" 4*7.3e9=",4*7.3e9, "; 8e9*0.9..", 29e9/4/8e9)
print("800000:",8e9/1e4)
# 19,800
print("t=(2/s)ln(2Ne):",2/0.001*log(2e4))
print(" 450000*0.45/19807=",450000*.45/19807," 252000/19807=",252000/19807," 252000*.45/19807",252000*.45/19807," 9e6/32.5*.45/19807",9e6/32.5*.45/19807, "146250/19807",146250/19807)
# Hard Limits
for name,T,g,Vk,census in (("human lineage",6.5e6,25,5,8.2e9),("human species",2e6,25,5,8.2e9),("eleph",2e6,22,3,415000),("mouse",1.5e6,.5,25,1e10),("fly",5e6,.08,400,1e12)):
    G=T/g; X=(Vk+2)*G/16; print(name,"G",G,"X",X,"over",census/X)
print(" Table1 ok. exponent: Ne/T=7.3e9/400=",7.3e9/400," pi^2*..=",pi**2*7.3e9/400," decades",pi**2*7.3e9/400/log(10))
G=260000
for Ne in (7.3e9,4.69e9,1.98e5,1.32e5,1e4):
    print(" Ne",Ne,"G=260000: pi^2Ne/G =",pi**2*Ne/G," decades",pi**2*Ne/G/log(10))
print(" 252000, Ne=1e4:",pi**2*1e4/252000, exp(-pi**2*1e4/252000))
print(" 4Ne/G thresholds: Ne=G/4:",G/4)
print(" B2a: G/N=4:",exp(-pi**2/4)," G/N=1:",exp(-pi**2)," 0.25:",exp(-pi**2*4))
print(" Day sim 6/3000 =",6/3000, "; linear 750 =",.25*3000, "; 3000/ (600000/200)=",600000/200)
# 0.743
Ns=[2.5,4.0,6.1,8.2]
print("RRME:",sum(n*n for n in Ns)/sum(Ns)/8.2, sum(n*n for n in Ns), sum(Ns))
# sensitivity: more generations of exponential growth
import itertools
for g in (2,3,4,6,10,20):
    # growth factor per gen from 2.5->8.2 over 3 gens ~1.485
    r=(8.2/2.5)**(1/3)
    Ns2=[8.2/r**i for i in range(g)]
    print(" gens",g,"k/mu=",sum(n*n for n in Ns2)/sum(Ns2)/8.2)
# recalibration
for hN,cN in ((1e5,3e5),(1e5,1e6),(5e4,3e5),(5e4,1e6)):
    a=hN/3300; b=cN/33000
    print("recal",hN,cN,round(a,1),round(b,1),[round(2*t/(a+b)*1000) for t in (6,7,9)])
print(" Yoo-Ne N/Ne with census 1e5:",1e5/1.98e5,1e5/1.32e5)
print(" 6.5My -> 68 kya factor",6.5e6/68e3)
# 32.3 brute force
import itertools
req={'17.5M':17.5e6,'20M':20e6,'35M':35e6,'205M':205e6,'410M':410e6,'40M':40e6,'187M':187e6}
gens={'252000':252000,'450000':450000,'6.3e6/25y':252000,'9e6/20':450000,'260000':260000,'325000':325000,'146250':146250,'6.5e6/25':260000,'6.3e6/20':315000}
Ls={'2.9e9':2.9e9,'3.0e9':3e9,'3.1e9':3.1e9,'3.2e9':3.2e9,'6.4e9':6.4e9,'6.2e9':6.2e9}
mus={'1.2e-8':1.2e-8,'1.1e-8':1.1e-8,'1.25e-8':1.25e-8,'7.97e-9':7.97e-9,'1.5e-8':1.5e-8,'1.17e-8':1.17e-8,'1e-8':1e-8,'1.3e-8':1.3e-8}
hits=[]
for (a,A),(b,B),(c,C),(d,D) in itertools.product(req.items(),gens.items(),Ls.items(),mus.items()):
    for div,tag in ((1,''),(2,'/2')):
        v=A/div/(B*C*D)
        if abs(v-32.3)<0.15: hits.append((round(v,2),a+tag,b,c,d))
for h in sorted(hits)[:40]: print(h)
print(len(hits))
