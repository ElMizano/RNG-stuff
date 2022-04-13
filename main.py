# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
import numpy as np
import matplotlib.pyplot as plt
from random import randint


class Matrice:
    
    def __init__(self, size = 100):
        self.matrice = [randint(0, 1024) for i in range(size)]
        return
    


    def GraphWhiteNoise(self):
        graph = np.linspace(0, len(self.matrice), len(self.matrice), endpoint=True)
        plt.plot(graph, self.matrice, color="black", linewidth=2.5, linestyle="-",)
        
        plt.legend(loc='upper left', frameon=True)
        plt.show()
    
    def __repr__(self):
        return str(self.matrice)

matrice = Matrice(size = 150)
print(matrice.GraphWhiteNoise())
