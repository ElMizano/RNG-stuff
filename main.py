# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
import numpy as np
import matplotlib.pyplot as plt
from random import randint

class WhiteNoise:
    
    def __init__(self, size = 100):
        self.noise = [randint(0, 1024) for i in range(size)]
        self.squarenoise = [[randint(0,1)for i in range(size)]for i in range(size)]
        return

    def GraphWhiteNoise(self):
        graph = np.linspace(0, len(self.noise), len(self.noise), endpoint=True)
        plt.plot(graph, self.noise, color="black", linewidth=2.5, linestyle="-")
        plt.legend(loc='upper left', frameon=True)
        plt.show()
        return
    
    def __repr__(self):
        return str(self.noise)

Noise = WhiteNoise(size = 100)
print(Noise.GraphWhiteNoise())