#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import copy
import math
import turtle
import matplotlib


# TODO: Définissez vos fonction ici
def volumeEpsiloide(demi_axe1, demi_axe2, demi_axe3, masse_volumique):
    volume = (4/3)*math.pi*demi_axe1*demi_axe2*demi_axe3
    masse = masse_volumique*volume
    volume_et_masse = (volume, masse)
    return volume_et_masse

def arbre(n):
    t = turtle
    compteur = 0
    x = 2.6
    while True:
        t.fd(x*100)
        t.lt()
        t.rt()
        t.bk()
        compteur += 1
        if compteur % 4 == 0:
            x += 0.7




        



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volumeEpsiloide(2,3,4,0.294))
    niveau = 3
    arbre(niveau)
    
