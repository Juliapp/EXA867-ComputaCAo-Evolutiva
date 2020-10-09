from random import random
from random import randint
import matplotlib.pyplot as plt

import numpy as np
import math

x = np.array([300, 150, 200, 115, 100, 250, 285, 150, 200, 115])
y = np.array([200, 115, 300, 150, 200, 285, 250, 290, 100, 250])

distanciasAux = []

for i in range(len(x)):
    xa = x[i]
    ya = y[i]
    
    array = []
    for j in range(len(x)):
        xb = x[j]
        yb = y[j]
        
        aux = math.sqrt(((xa - xb) ** 2 ) + ((ya - yb) ** 2 ))
        array.append(aux)

    distanciasAux.append(array)
    
distancias = np.array(distanciasAux)



class Cidade:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class ConjuntoCidades: 
    def __init__(self, quantidade):
        self.quantidade
        self.dictCidades = {}
        self.distancias = []
            
    def gerarCidades(self):
        nAchou = True
        
        while(nAchou):
            points = self.randomPoints()
            key = 'x' + str(points.x) + 'y' + str(points.y)
            
            if "nonexistent " + str(key) in self.dictCidades:
                self.dictCidades[key] = Cidade(points.x, points.y)
                nAchou = False
        
        
        
    def randomPoints():
        x = randint(0, 100)
        y = randint(0, 100)
        
        return {'x': x, 'y' : x}