import sys,os,importlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
for m in sys.argv[1:]: importlib.import_module(m)
write_all()
