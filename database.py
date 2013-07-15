from astropy.io import fits
import numpy as np
import pdb

#pdb.pm() - inserts me back into problem area
#pdb.set_trace() - put stop point
#n (next line), s (steps through functions), q (quit), u (up), c (continue)

class Database(object):
   
   def __init__(self,filename):
       #open and read the file
       self.hdulist = fits.open(filename)
       self.header = self.hdulist[1].header
       self.data = self.hdulist[1].data
       
   def getColumn(self,name):
       return self.data.field(name)
   
   def removeBad(self, column, tag):
		
		#cast into numpy arrays
		tag = np.array(tag)
		column = np.array(column)
				
		print tag
		print column
		
		#check sizes of each and return error if tag != 1 or != to column
		ntag = tag.size
		ncol = column.size
		
		print 'ntag:', ntag
		print 'ncol:', ncol
		
		pdb.set_trace()
		if (ntag > 1 and ntag != ncol):
			print 'Error: tag must be either 1 or same size as column'
			return

		if ntag == 1:
			tag=np.resize(tag,ncol)	

		cond = self.data[str(column[0])] != tag[0]
		if ncol > 1:
			for i in range(ncol)[1:]:
				cond = cond & (self.data[str(column[i])] != tag[i])

		#select out good data
   		good, = np.where(cond)

   		return self.data[good]
   	

		
