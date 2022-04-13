# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
from random import randint

class Random:
    
    def __init__(self, size = 100):
        self.matrice = [randint(0, 1024) for i in range(size)]
        return
    
    def __repr__(self):
        return str(self.matrice)

Matrice_test = Random()
print(Matrice_test)