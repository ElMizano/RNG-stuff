# -*- coding: utf-8 -*-
"""
Projet NSI Terminale : Génération de nombres (à peu près...) aléatoires

Mathis Eric Fanigilulo
Xavier Martial Georges-Marie Ferber
T09
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
    """
    Classe permettant de générer le "bruit blanc", d'en obtenir des représentations graphiques
    à l'aide de graphes et de diverses images, ainsi que de générer la seed à l'aide de diverses valeurs
    obtenues dans le bruit blanc.
    """
    def __init__(self, size = 100):
        self.size = size
        self.squarenoise = [[randint(0,1024)for i in range(size)]for i in range(size)]
        #matrice de nombres aléatoires qui permettra de créer le graphe et d'obtenir la seed,
        #simule ce que l'on aurait obtenu à l'aide d'un véritable Arduino
        self.list_to_plot = [i for j in self.squarenoise for i in j]
        #Merge la matrice en une unique liste ([[1,2,3],[4,5,6]] ==> [1,2,3,4,5,6])
        #Permet d'afficher correctemment la matrice en tant que graphe.
        
    
    def GraphWhiteNoise(self):
        """
        Génère un graphique de bruit blanc à l'aide de la liste simulant le bruit blanc.
        PS : L'affiche autimatiquement dans l'onglet "Plots" de Spyder.
        """
        graph = np.linspace(0, len(self.list_to_plot), len(self.list_to_plot), endpoint=True)
        plt.plot(graph, self.list_to_plot, color="black", linewidth=2.5, linestyle="-")
        plt.show()
        
    
    def BarWhiteNoise(self):
        """
        Génère une image de bruit blanc et la stocke 
        
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
        noise3 = PerlinNoise(octaves=12)  # Octaves de bruit de Perlin (c'est joli)
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
            for j in range(self.size):              # Change la teinte de Bleu selon
                if pic[i][j] < -0.25:               # la grandeur du nombre
                    img[i][j] = [100,0,0]           # + le nombre est grand + c'est foncé
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
        imRed = Image.open('BarWhiteNoise.bmp')                                # ======================
        imGreen = Image.open('newimage.bmp')
        imBlue = Image.open('perlin.bmp')
        pixRed = imRed.load()
        pixBlue = imBlue.load()
        pixGreen = imGreen.load()                                              # Bazard de traitement d'images
        filename = "MergedRandom.jpg"
        image = Image.new(mode = "1", size = (self.size,self.size), color = 0)
        image.save(filename)
        img = cv2.imread(filename)                                             # =======================
        for i in range(self.size):
            for j in range(self.size):          # créé un pixel RGB avec le pixel rouge de BarWhithNoise
                Rpix = pixRed[i,j][0]           # le pixel vert du SquareNoise et le pixel bleu du Perlin noise
                Gpix = pixGreen[i,j][1]         # aux même coordonnées.
                Bpix = pixBlue[i,j][2]          # Fais ça avec tous les pixels des 3 images (de la même taille)
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
                value = self.Xorified(pix[i,j][0],pix[i,j][1],pix[i,j][2])  # Xorifie les valeurs RGB de chaque pixels
                XorTab.append(value)                                        # et les stockent dans une liste
        return XorTab
    
    def SeedByAllXorValues(self):
        """
        Traite les données d'un tableau dynamique pour avoir une graine
        """
        tab = self.AllXorifiedTab()
        somme = 0
        for i in range(len(tab)):
            somme += somme + tab[i]
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

def generate_seed(lenght,randomness):
    seed = []
    Noise = WhiteNoise(size = randomness)
    Noise.GraphWhiteNoise()
    Noise.SquareWhiteNoise()
    Noise.PerlinNoiseGen()
    Noise.BarWhiteNoise()
    Noise.Merge()
    lenseed = 0
    while lenseed < lenght:
        temp = ""
        for i in seed:
            temp += str(i)
        lenseed = len(temp)
        seed.append(hex_to_dec(hashing(Noise.SeedByAllXorValues()).hexdigest()))
        Noise = WhiteNoise(size = randomness)
        Noise.GraphWhiteNoise()
        Noise.SquareWhiteNoise()
        Noise.PerlinNoiseGen()
        Noise.BarWhiteNoise()
        Noise.Merge()
    final_seed = ""
    for i in seed:
        final_seed += str(i)
    return final_seed[:lenght]
    


lenght = 30
randomness = 5

print(generate_seed(lenght,randomness))
# A savoir : Utiliser la valeur 1 pour randomness créera des seeds identiques, dépendamment de la longueur de la seed
# Exemple pour randomness = 1 et lenght = 37 : La seed donnera 5737968537777873734161048960656937279.
# Si l'on augmente la longueur, le nombre se répète lenght/37 fois : Pour lenght = 111, on obtient :
# 573796853777787373416104896065693727957379685377778737341610489606569372795737968537777873734161048960656937279
# Il est en effet ici répété 3 fois.
# Cela est du au fait que le nombre aléatoire est basé sur une image lui même basé sur une matrice, randomness = 1
# Donnera une matrice en 1x1, et donc une image d'un seul pixel, et donc toujours le même nombre.
# De plus, plus on augmente randomness, plus le temps nécessaire pour calculer la seed sera grand, mais plus il y
# aura de seeds différentes. On conseille d'utiliser randomness = 10.
# La "complexité" de lenght est linéaire, mais la "complexité" de randomness est quadratique.
