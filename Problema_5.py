#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 21:48:46 2022

@author: christiandelao
"""

import numpy as np

Vector1 = np.random.randint(0, 100, size=(100, 1)) 
Vector2 = np.random.randint(0, 100, size=(100, 1)) 

sumtol = (np.sum(Vector1, axis=0)) + (np.sum(Vector2, axis=0))
print (sumtol)
