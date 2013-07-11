import cPickle as pickle

class Database(object):
   
   def __init__(self,filename):
       #open and read the file
       with open(filename,'r') as f:
           pickle.load(f)
       
   def getColumn(self,name):
       return self.field(name)
   



def simple(x):
	return x




