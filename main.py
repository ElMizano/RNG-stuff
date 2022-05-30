# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:37:35 2022

@author: Xavier & Mathis
"""
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from PIL import Image, ImageDraw
from perlin_noise import PerlinNoise
import os
import cv2
import hashlib

class WhiteNoise:
    
    def __init__(self, size = 100):
        self.size = size
        self.squarenoise = [[randint(0,1024)for i in range(size)]for i in range(size)]
        return
    
    def GraphWhiteNoise(self):
        """
        Génère un graphique de bruit blanc
        """
        graph = np.linspace(0, len(self.squarenoise[0]), len(self.squarenoise[0]), endpoint=True)
        plt.plot(graph, self.squarenoise[0], color="black", linewidth=2.5, linestyle="-")
        plt.legend(loc='upper left', frameon=True)
        plt.show()
        return
    
    def BarWhiteNoise(self):
        """
        Génère une image de bruit blanc
        """
        filename = "BarWhiteNoise.jpg"
        image = Image.new(mode = "1", size = (self.size,self.size), color = 0)
        image.save(filename)
        img = cv2.imread(filename)
        for i in range(self.size):
            for j in range(self.size):
                if self.squarenoise[0][j] < 1024//4:
                    img[i][j] = [0,0,100]
                elif self.squarenoise[0][j] < 1024//2:
                    img[i][j] = [0,0,140]
                elif self.squarenoise[0][j] < 1024//1.5:
                    img[i][j] = [0,0,180]
                else:
                    img[i][j] = [0,0,220]
        cv2.imwrite('BarWhiteNoise.bmp',img)
        #os.system('BarWhiteNoise.bmp')
    
    def SquareWhiteNoise(self):
        """
        Génère une deuxième image de bruit blanc
        """
        filename = "noise.jpg"
        image = Image.new(mode = "1", size = (self.size,self.size), color = 0)
        image.save(filename)
        img = cv2.imread(filename)
        for i in range(self.size):
            for j in range(self.size):
                if self.squarenoise[i][j] < 1024//4:
                    img[i][j] = [0,100,0]
                elif self.squarenoise[i][j] < 1024//2:
                    img[i][j] = [0,140,0]
                elif self.squarenoise[i][j] < 1024//1.5:
                    img[i][j] = [0,180,0]
                else:
                    img[i][j] = [0,220,0]
        cv2.imwrite('newimage.bmp',img)
        #os.system('newimage.bmp')
        return
    
    def PerlinNoiseGen(self):
        """
        Génère une image de bruit de Perlin
        """
        noise1 = PerlinNoise(octaves=3)
        noise2 = PerlinNoise(octaves=6)
        noise3 = PerlinNoise(octaves=12)
        xpix = self.size
        ypix = self.size
        pic = []
        for i in range(xpix):
            row = []
            for j in range(ypix):
                noise_val = noise1([i/xpix, j/ypix])
                noise_val += 0.5 * noise2([i/xpix, j/ypix])
                noise_val += 0.25 * noise3([i/xpix, j/ypix])
                row.append(noise_val)
            pic.append(row)
        filename = "perlin.jpg"
        image = Image.new(mode = "1", size = (self.size,self.size), color = 0)
        image.save(filename)
        img = cv2.imread(filename)
        for i in range(self.size):
            for j in range(self.size):
                if pic[i][j] < -0.25:
                    img[i][j] = [100,0,0]
                elif pic[i][j] < 0:
                    img[i][j] = [140,0,0]
                elif pic[i][j] < 0.25:
                    img[i][j] = [180,0,0]
                else:
                    img[i][j] = [220,0,0]
        cv2.imwrite('perlin.bmp',img)
        #os.system('perlin.bmp')
        return
    
    def Merge(self):
        """
        Supperpose les trois images générées précédemment.
        """
        imRed = Image.open('BarWhiteNoise.bmp')
        imGreen = Image.open('newimage.bmp')
        imBlue = Image.open('perlin.bmp')
        pixRed = imRed.load()
        pixBlue = imBlue.load()
        pixGreen = imGreen.load()
        filename = "MergedRandom.jpg"
        image = Image.new(mode = "1", size = (self.size,self.size), color = 0)
        image.save(filename)
        img = cv2.imread(filename)
        for i in range(self.size):
            for j in range(self.size):
                Rpix = pixRed[i,j][0]
                Gpix = pixGreen[i,j][1]
                Bpix = pixBlue[i,j][2]
                img[i][j] = [Rpix,Gpix,Bpix]
                
        cv2.imwrite('MergedRandom.bmp',img)
        #os.system('MergedRandom.bmp')
        
    def Xorified(self,R,G,B):
        """
        Xorifie trois valeurs enter elles.
        """
        return R ^ G ^ B
    
    def AllXorifiedTab(self):
        """
        Génère un tableau de toute les valeur xorifiées des pixels de l'image
        créée dans Merge()
        """
        XorTab = []
        im = Image.open('MergedRandom.bmp')
        pix = im.load()
        for i in range(self.size):
            for j in range(self.size):
                value = self.Xorified(pix[i,j][0],pix[i,j][1],pix[i,j][2])
                XorTab.append(value)
        return XorTab
    
    def SeedByAllXorValues(self):
        """
        Traite les données d'un tableau dynamique pour avoir une graine
        """
        tab = self.AllXorifiedTab()
        somme = 0
        for i in range(len(tab)):
            somme =+ somme + tab[i]
        return somme
    

    
    def __repr__(self):
        return self.noise


def hashing(item):
    item = hashlib.md5(str(item).encode())
    return item

def hex_to_dec(num):
    num = list(num)
    for i in range(len(num)):
        if num[i] == "a":
            num[i] = "10"
        elif num[i] == "b":
            num[i] = "11"
        elif num[i] == "c":
            num[i] = "12"
        elif num[i] == "d":
            num[i] = "13"
        elif num[i] == "e":
            num[i] = "14"
        elif num[i] == "f":
            num[i] = "15"
    num.reverse()
    k = 0
    res = 0
    for i in range(len(num)):
        res += int(num[i])*16**k
        k += 1
    return res


def generate_seed(amount):
    seed = ""
    Noise = WhiteNoise(size = 10)
    Noise.GraphWhiteNoise()
    Noise.SquareWhiteNoise()
    Noise.PerlinNoiseGen()
    Noise.BarWhiteNoise()
    Noise.Merge()
    for i in range(amount):
        seed += str((hex_to_dec(hashing(Noise.SeedByAllXorValues()).hexdigest())))
        Noise = WhiteNoise(size = 10)
        Noise.GraphWhiteNoise()
        Noise.SquareWhiteNoise()
        Noise.PerlinNoiseGen()
        Noise.BarWhiteNoise()
        Noise.Merge()
        print(i)
    return(int(seed))

print(generate_seed(100))



