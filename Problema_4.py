#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 21:40:35 2022

@author: christiandelao
"""

import numpy as np

arreglo = np.random.randint(0, 50, size=(15, 12))  
porprom = np.amin(arreglo)

print ("La lista ingresada es la siguiente:")
print (arreglo)
print ()
print("El dato menor del array es:")
print (porprom)