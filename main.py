# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from PIL import Image, ImageDraw
import os
import cv2

class WhiteNoise:
    
    def __init__(self, size = 100):
        self.size = size
        self.squarenoise = [[randint(0,1024)for i in range(size)]for i in range(size)]
        return
    
    def GraphWhiteNoise(self):
        graph = np.linspace(0, len(self.squarenoise[0]), len(self.squarenoise[0]), endpoint=True)
        plt.plot(graph, self.squarenoise[0], color="black", linewidth=2.5, linestyle="-")
        plt.legend(loc='upper left', frameon=True)
        plt.show()
        return
    
    def SquareWhiteNoise(self):
        filename = "noise.jpg"
        image = Image.new(mode = "1", size = (self.size,self.size), color = 0)
        image.save(filename)
        img = cv2.imread(filename)
        for i in range(self.size):
            for j in range(self.size):
                if self.squarenoise[i][j] < 1024//4:
                    img[i][j] = [0,0,255]
                elif self.squarenoise[i][j] < 1024//2:
                    img[i][j] = [255,0,0]
                elif self.squarenoise[i][j] < 1024//1.5:
                    img[i][j] = [0,255,0]
                else:
                    img[i][j] = [255,255,255]
        cv2.imwrite('newimage.bmp',img)
        os.system('newimage.bmp')
        return
    
    def __repr__(self):
        return str(self.noise)

Noise = WhiteNoise(size = 100)
print(Noise.GraphWhiteNoise())
print(Noise.SquareWhiteNoise())