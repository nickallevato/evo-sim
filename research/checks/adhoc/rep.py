import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import f2_multilocus as f, a_ltee_scaling as a
print(f.job((0.01,2000,'free',0.5,0,500,3000))[5]['rate'], f.job((0.01,2000,1.5,0.5,0,500,3000))[5]['rate'])
print(a.rate_task(("val0.5",2000,0.5/2000,0.01,4000,500,0))[2])
