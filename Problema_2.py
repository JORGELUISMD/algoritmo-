#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 21:30:14 2022

@author: christiandelao
"""

import pandas as pd
n = int(input("Ingrese el numero de alumnos: "))
lista = pd.DataFrame(columns=['Nombre', 'Edad'],
                  index=range(n))
for i in range(n):
    t = str(i)
    for k in range (2):
        q = str(k)
        x = input("Ingrese el valor de x"+ t + "," + q + ": ")
        lista.iloc[i,k] = (x)

porprom = lista.sort_values('Edad',ascending=False)
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (lista)
print("El alumno con mayor edad es:")
print(arx)