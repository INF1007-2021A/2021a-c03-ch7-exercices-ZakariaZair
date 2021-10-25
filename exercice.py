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
    x = 100
    i = 1
    if n % 2 == 0:
        i = 1
    else:
        i = -1

    while n > 0:
        t.lt(90*i)
        t.fd(x)
        t.rt(30*i)
        t.fd(x/2)
        arbre(n)
        t.bk(x/2)
        t.lt(-30*i)
        t.bk(x)
        t.rt(-90*i)
        n -= 1




        



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volumeEpsiloide(2,3,4,0.294))
    niveau = 2
    arbre(niveau)
    
