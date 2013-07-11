import cPickle as pickle
from astropy.io import fits

class Database(object):
   
   def __init__(self,filename):
       #open and read the file
       self.hdulist=fits.open(filename)
       self.header = hdulist[1].header
       self.data = hdulist[1].data
       
   def getColumn(self,name):
       return self.data.field(name)
   


