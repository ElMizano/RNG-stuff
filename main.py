# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
import numpy as np
import matplotlib.pyplot as plt

class Matrice(size = 100):
    
    __init__(self):
        
        return

def GraphWhiteNoise(whitenoise):
    graph = np.linspace(0, len(whitenoise), len(whitenoise), endpoint=True)
    plt.plot(graph, whitenoise, color="black", linewidth=2.5, linestyle="-",)
    
    plt.legend(loc='upper left', frameon=True)
    plt.show()

GraphWhiteNoise([15,18,100,500,3,231,144])


    
