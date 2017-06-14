#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: K
"""
import numpy as np
import matplotlib.pyplot as plt

#to do: 
#   parameter dictionary?, think of something that can be altered with a genetic algorithm 
#   

def izh(dt, v, u, a, b, c, d, I):
    
        dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + I
        du = a * ((b*v) - u)
        
        v = v + dt*dv
        u = u + dt*du
        
        return u, v


dt = .025
duration = 100 #needs to be an even number 
time = int(duration / dt)

vList = []
uList = []

tmeSplt = time/2
I = np.append(np.zeros((1, tmeSplt), dtype=np.int32), 
                 (10 * np.ones((1, tmeSplt), dtype=np.int32)), 1)
t = 0
for i in range(time):
    stm = I[0][i] #remove inner brackets hack...
    a = .02
    b = .2
    c = -65
    d = 2
    
    vi = -65
    ui = b * vi #(izh 2003)
    
    uOut, vOut = izh(.025, vi, ui, a, b, c, d, stm)
    
    vList.append(vOut)
#plt.matshow(I[0])
plt.plot(vList, range(time))
plt.show()




