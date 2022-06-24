#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:44:37 2022

@author: christiandelao
"""
import pandas as pd
Nomb_edad =        [['Christian',30],
                ['Ilya',21],
                ['Eros',24],
                ['Alexis',19],
                ['Luis', 28],
                ['Manuel', 24],
                ['Gerardo', 26],
                ['Graciela', 20],
                ['Ivette', 23],
                ['Virginia',21]]
columnas =['Alumno','Edad']
lista = pd.DataFrame(Nomb_edad,columns=columnas,)
porprom = lista.sort_values('Edad',ascending=False)                                                                       
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (lista)
print()
print("El alumno con mayor edad es:")
print(arx)