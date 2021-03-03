import math
from Punto3D import Punto3D

class Segmento3D:

    def __init__(self, pointA = Punto3D(0,0,0), pointB = Punto3D(1,1,1)):
        self.pointA = pointA
        self.pointB = pointB

    def length(self):
        return self.pointA.distance(self.pointB)

    def __eq__(self, segment):
        #if self.pointA == segment.pointA and self.pointB == segment.pointB:
        if self.length()==segment.length():
            return True
        else:
            return False
    
    def __lt__(self,segment):
        if self.length()<segment.length():
            return True
        else:
            return False

    def __gt__(self,segment):
        if self.length()>segment.length():
            return True
        else:
            return False

    def __repr__(self):
        return "Segment3D(({}, {}, {}),({}, {}, {}))".format(self.pointA.x,self.pointA.y,self.pointA.z,
        self.pointB.x,self.pointB.y,self.pointB.z)

        


