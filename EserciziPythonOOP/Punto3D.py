import math

class Punto3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        dz = self.z - point.z
        return math.sqrt(dx**2 + dy**2 + dz**2)
    
    def __repr__(self):
        return "Point3D({}, {}, {})".format(self.x,self.y,self.z)
    
