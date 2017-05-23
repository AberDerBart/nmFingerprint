from main import *
from Classifier import *

faultier=Class("faultier",[])
panda=Class("panda",[])
csf=KNearestNeighbourClassifier([faultier,panda],2)
faultier.load()
panda.load()


