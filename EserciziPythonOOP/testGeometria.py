from Punto3D import Punto3D
from Segmento3D import Segmento3D
from Cube3D import Cube3D

import random

cubi = {}
segmenti = {}

# generazione casuale di cubi e salvataggio in dizionario
for i in range(20):
    ox = random.uniform(0,10)
    oy = random.uniform(0,10)
    oz = random.uniform(0,10)
    edge = random.uniform(0,20)
    newcube = Cube3D(Punto3D(ox, oy, oz), edge)
    chiave = "Cubo"+str(i)
    cubi[chiave] = newcube

# generazione casuale di segmenti e salvataggio in dizionario
for i in range(40):
    Ax = random.uniform(0,10)
    Ay = random.uniform(0,10)
    Az = random.uniform(0,10)
    Bx = random.uniform(0,10)
    By = random.uniform(0,10)
    Bz = random.uniform(0,10)
    edge = random.uniform(0,20)
    newsegment = Segmento3D(Punto3D(Ax, Ay, Az), Punto3D(Bx, By, Bz))
    chiave = "Segmento"+str(i)
    segmenti[chiave]=newsegment

cubo_segmenti_contenuti = {} 
for i in cubi:
    count = 0
    for j in segmenti:
        if cubi[i].contains_segment(segmenti[j]):
            count += 1
    chiave = str(i)
    cubo_segmenti_contenuti[chiave] = count

cubo_cubi_intersecati = {} 
for i in cubi:
    count = 0
    for j in cubi:
        if cubi[i].intersect_cube(cubi[j]):
            count += 1
    chiave = str(i)
    cubo_cubi_intersecati[chiave] = count-1 if count>0 else 0

segmento_cubi_intersecati = {}
for i in segmenti:
    count = 0
    for j in cubi:
        if cubi[j].intersect_segment(segmenti[i]):
            count += 1
    chiave = str(i)
    segmento_cubi_intersecati[chiave] = count-1

segmento_in_cubi = {}
for i in segmenti:
    count = 0
    for j in cubi:
        if cubi[j].contains_segment(segmenti[i]):
            count += 1
    chiave = str(i)
    segmento_in_cubi[chiave] = count-1



