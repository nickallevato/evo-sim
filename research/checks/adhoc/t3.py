import sys; sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import f2_fwdpy11 as f
f.BURN,f.T=1000,3000
print(f.run((2.0,1.5,1)))
