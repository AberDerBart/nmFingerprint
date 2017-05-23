import math
import json

class Class:
    def __init__(self,name,fingerPrints=[]):
        self.name=name
        self.fingerPrints=fingerPrints
    def append(self,fingerPrint):
        self.fingerPrints.append(fingerPrint)
    def __lt__(self,other):
        return True
    def save(self,path=None):
        if not path:
            path=self.name+".json"
        saveFile=open(path,"w")
        json.dump(self.fingerPrints,saveFile)
        saveFile.close()
    def load(self,path=None):
        if not path:
            path=self.name+".json"
        loadFile=open(path,"r")
        self.fingerPrints=json.load(loadFile)
        loadFile.close()

def distanceEuklid(fp1,fp2):
    dist=0

    for key in fp1.keys()|fp2.keys():
        dist+=math.pow(fp1.get(key,0)-fp2.get(key,0),2)
    return math.sqrt(dist)

class KNearestNeighbourClassifier:
    def __init__(self,classes,k=1):
        self.k=k
        self.classes=classes
    def append(self,cl):
        self.classes.append(cl)
    def classify(self,fingerPrint):
        neighbours=[]
        for cl in self.classes:
            for fp in cl.fingerPrints:
                d=distanceEuklid(fingerPrint,fp)
                neighbours.append((d,cl))
        for d,n in sorted(neighbours):
            print(n.name,d)


