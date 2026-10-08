import sys,time,numpy as np
sys.path.insert(0,'/home/na/projects/evo-sim/research/checks')
import h2_hard_selection_multilocus as h
for args in [(1000,.01,.03,5,None,"hard",800,500),(1000,.01,.2,2,None,"hard",800,500),(1000,.01,.03,4,None,"soft",800,500),(1000,.01,.01,5,.5,"hard",800,500)]:
    t=time.time(); r=h.run(*args[:6],args[6],args[7],np.random.default_rng(1)); print(args,{k:(round(v,3) if isinstance(v,float) else v) for k,v in r.items()},round(time.time()-t,1))
