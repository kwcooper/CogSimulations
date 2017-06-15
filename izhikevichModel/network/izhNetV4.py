#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python implimentation of (Izhikevich 2003) "Simple Model of Spiking Neurons"
#If cell A spikes, then Ib = 10
import numpy as np
import matplotlib.pyplot as plt

#to do: 
#   parameter dictionary?, think of something that can be altered with a genetic algorithm 
#   function to create I according to specifications

#Izh equation
def izh(dt, v, u, a, b, c, d, I):
    
    if v > 30:
        v = c
        u = u + d

    dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + I
    du = a * ((b*v) - u)
    
    v = v + dt*dv
    u = u + dt*du
    
    return u, v

numNeurons = 5
stmValue = 11

dt = .025
duration = 200 #needs to be an even number 
steps = int(duration / dt)
tmeSplt = steps/2


v1List = []
u1List = []
v2List = []
u2List = []


tMinusZs = np.zeros((numNeurons, steps), dtype=np.float32)


I1 = np.append(np.zeros((1, tmeSplt), dtype=np.int32), 
              (stmValue * np.ones((1, tmeSplt), dtype=np.int32)), 1)

#I1 = np.zeros((1, time), dtype=np.int32)

#Parameters
a = .02
b = .2
c = -65
d = 2

vMat = np.append(-65 * np.random.randint(2, size=(numNeurons, 1)), tMinusZs, 1)
uMat = np.append((b * -65) * np.random.randint(2, size=(numNeurons, 1)), tMinusZs, 1) #(izh 2003)


#Simulation
t = 0
for j in range(steps-1):
    for i in range(1, numNeurons):
        stm1 = I1[0][j] #remove inner brackets hack...
        
        #Neuron 1
        vi = vMat[i][j]
        ui = uMat[i][j]
        
        uOut, vOut = izh(.025, vi, ui, a, b, c, d, stm)
        
        vMat[i][j+1] = vOut
        uMat[i][j+1] = uOut
        
        if vi1 > -60:
            stm2 = stmValue
        else:
            stm2 = 0

        

#Plotting
plt.style.use('fivethirtyeight')
plt.plot(range(steps), I1[0], 'y', label='I')
plt.plot(range(steps), vList[0:8000], 'r', label='V1') #the timestamps are hardcoded
plt.plot(range(steps), vList[0:8000], 'b', label='V2')
plt.title('Regular Spiking (Coupled)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.show()

