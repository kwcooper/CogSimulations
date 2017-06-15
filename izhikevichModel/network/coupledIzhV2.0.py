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


dt = .025
duration = 200 #needs to be an even number 
time = int(duration / dt)

v1List = []
u1List = []
v2List = []
u2List = []

#Time and Stimulus
tmeSplt = time/2
stmValue = 11
I1 = np.append(np.zeros((1, tmeSplt), dtype=np.int32), 
                 (stmValue * np.ones((1, tmeSplt), dtype=np.int32)), 1)

#I1 = np.zeros((1, time), dtype=np.int32)

#Parameters
a = .02
b = .2
c = -65
d = 2

vi1 = -70
ui1 = b * vi1 #(izh 2003)
v1List.append(vi1)
u1List.append(ui1)

vi2 = -70
ui2 = b * vi2 #(izh 2003)
v2List.append(vi2)
u2List.append(ui2)



#Simulation
t = 0
for i in range(time-1):
        stm1 = I1[0][i] #remove inner brackets hack...
        
        #Neuron 1
        vi1 = v1List[i-1]
        ui1 = u1List[i-1]
        u1Out, v1Out = izh(.025, vi1, ui1, a, b, c, d, stm1)
        
        v1List.append(v1Out)
        u1List.append(u1Out)
        
        if vi1 > -60:
            stm2 = stmValue
        else:
            stm2 = 0
            
        #Neuron 2
        vi2 = v2List[i-1]
        ui2 = u2List[i-1]
        u2Out, v2Out = izh(.025, vi2, ui2, a, b, c, d, stm2)
        
        v2List.append(v2Out)
        u2List.append(u2Out)
        
        
        

#Plotting
plt.style.use('fivethirtyeight')
plt.plot(range(time), I1[0], 'y', label='I')
plt.plot(range(time), v1List[0:8000], 'r', label='V1') #the timestamps are hardcoded
plt.plot(range(time), v2List[0:8000], 'b', label='V2')
plt.title('Regular Spiking (Coupled)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.show()

