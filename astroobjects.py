import math
class Astroobjects(object):
    def __init__(self,b,l,hdist):
        '''
        designed to store b and l in degrees, not radians
        hdist in kpc
        '''
        self.b=b
        self.l=l
        self.hdist=hdist
        
    def galXYZ(self):
        '''
        Returns xyz in kpc
        '''
        x=self.hdist*math.sin(self.b*math.pi/180.)*math.cos(self.l*math.pi/180.)-8.
        y=self.hdist*math.sin(self.b*math.pi/180.)*math.sin(self.l*math.pi/180.)
        z=self.hdist*math.cos(self.b*math.pi/180.)
        return [x,y,z]