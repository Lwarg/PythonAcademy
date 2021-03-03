from Punto3D import Punto3D
from Segmento3D import Segmento3D

import math

class Cube3D:

    #   z
    #   ^
    #   .....
    #   |   |
    #   o....  >x    
    #
    

    def __init__(self, origin = Punto3D(0,0,0), edge=1):
        self.origin = origin  # vertice in basso a sinistra (punto con i valori x,y,z più bassi)
        self.edge = edge  # lunghezza lato
    
    def volume(self):
        return edge**3

    def __repr__(self):
        return "Cubo3D(Origin({}, {}, {}), Edge: {})".format(self.origin.x,self.origin.y,self.origin.z,self.edge)
    
    def __eq__(self, cube):
        if self.volume()==cube.volume():
            return True
        else:
            return False

    def __lt__(self, cube):
        if self.volume()<cube.volume():
            return True
        else:
            return False
    
    def __gt__(self, cube):
        if self.volume()>cube.volume():
            return True
        else:
            return False

    def contains_point(self, point):
        # un punto sta all'interno del cubo se i suoi valori x,y,z sono maggiori di quelli dell'origine ma non troppo
        # (per troppo si intende più del lato del cubo)
        dx = point.x - self.origin.x
        dy = point.y - self.origin.y
        dz = point.z - self.origin.z
        if dx<0 or dy<0 or dz<0 or dx>self.edge or dy>self.edge or dz>self.edge:
            return False
        else:
            return True
        
    def contains_segment(self, segment):
        # un segmento è contenuto in un cubo se e solo se i suoi estremi sono contenuti nel cubo
        if self.contains_point(segment.pointA) and self.contains_point(segment.pointB):
            return True
        else:
            return False
    
    def intersect_segment(self, segment):
        # funzone per identificare un segmento che interseca ma non è contenuto interamente nel cubo
        # un segmento non interseca un cubo se i suoi estremi sono entrambi troppo "sotto, sopra, destra, sinistra, davanti o dietro"
        dxA = segment.pointA.z - self.origin.x
        dyA = segment.pointA.z - self.origin.y
        dzA = segment.pointA.z - self.origin.z
        dxB = segment.pointB.z - self.origin.x
        dyB = segment.pointB.z - self.origin.y
        dzB = segment.pointB.z - self.origin.z
        A = [0,0,0]
        B = [1,1,1]
        A[0] = "destra" if dxA>self.edge else "sinistra"
        A[1] = "avanti" if dyA>self.edge else "dietro"
        A[2] = "sopra" if dzA>self.edge else "sotto"
        B[0] = "destra" if dxB>self.edge else "sinistra"
        B[1] = "avanti" if dyB>self.edge else "dietro"
        B[2] = "sopra" if dzB>self.edge else "sotto"   
        flag = False
        for i in range(len(A)):
            if A[i]==B[i]:
                flag = True

        if self.contains_point(segment.pointA) and self.contains_point(segment.pointB):   # escludo il caso interamente contenuto
            return False     
        elif self.contains_point(segment.pointA) and not self.contains_point(segment.pointB):
            return True
        elif self.contains_point(segment.pointB) and not self.contains_point(segment.pointA):
            return True
        elif flag:
            return False
        else:
            return True

    def vertici(self):
        # restituisce una lista di 8 punti (gli 8 vertici del cubo)
        O0 = self.origin
        O1 = Punto3D(self.origin.x + self.edge, self.origin.y            , self.origin.z)
        O2 = Punto3D(self.origin.x + self.edge, self.origin.y + self.edge, self.origin.z)
        O3 = Punto3D(self.origin.x            , self.origin.y + self.edge, self.origin.z)
        O4 = Punto3D(self.origin.x            , self.origin.y            , self.origin.z + self.edge)
        O5 = Punto3D(self.origin.x + self.edge, self.origin.y            , self.origin.z + self.edge)
        O6 = Punto3D(self.origin.x + self.edge, self.origin.y + self.edge, self.origin.z + self.edge)
        O7 = Punto3D(self.origin.x            , self.origin.y + self.edge, self.origin.z + self.edge)
        return [O0, O1, O2, O3, O4, O5, O6, O7]

    def intersect_cube(self, cube):
        # se due cubi si intersecano, almeno uno dei vertici di un cubo sta dentro l'altro cubo
        flag = False
        # verifica 1: vertici di self in cube
        v = self.vertici()
        for i in v:
            if cube.contains_point(i):
                flag = True
        # verifica 2: vertici di cube in self
        v = cube.vertici()
        for i in v:
            if self.contains_point(i):
                flag = True
        return flag