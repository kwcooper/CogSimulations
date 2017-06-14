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
        
        if v > 30:
            v = c
            u = u + d
    
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
stmValue = 11
I = np.append(np.zeros((1, tmeSplt), dtype=np.int32), 
                 (stmValue * np.ones((1, tmeSplt), dtype=np.int32)), 1)

#Parameters
a = .02
b = .2
c = -65
d = 2

vi = -65
ui = b * vi #(izh 2003)
vList.append(vi)
uList.append(ui)

t = 0
for i in range(time-1):
    stm = I[0][i] #remove inner brackets hack...

    vi = vList[i-1]
    ui = uList[i-1]
    uOut, vOut = izh(.025, vi, ui, a, b, c, d, stm)
    
    vList.append(vOut)
    uList.append(uOut)

#Plotting
plt.style.use('fivethirtyeight')
plt.title('Regular Spiking')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.plot(range(time), I[0], 'y', label='I')
plt.plot(range(time), vList[0:4000], label='V')
plt.show()




