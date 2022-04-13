# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
=======
from random import randint
>>>>>>> origin/main

class Matrice(size = 100):
    
    def __init__(self, size = 100):
        self.matrice = [randint(0, 1024) for i in range(size)]
        return
<<<<<<< HEAD

def GraphWhiteNoise(whitenoise):
    graph = np.linspace(0, len(whitenoise), len(whitenoise), endpoint=True)
    plt.plot(graph, whitenoise, color="black", linewidth=2.5, linestyle="-",)
    
    plt.legend(loc='upper left', frameon=True)
    plt.show()

GraphWhiteNoise([15,18,100,500,3,231,144])


    
=======
    
    def __repr__(self):
        return str(self.matrice)

Matrice_test = Random()
print(Matrice_test)
>>>>>>> origin/main
