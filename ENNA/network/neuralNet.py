#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python implimentation of (Izhikevich 2003) "Simple Model of Spiking Neurons"
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx #only required if you want to visualize the network
#to do: 
#   parameter dictionary?, think of something that can be altered with a genetic algorithm 
#   function to create I according to specifications
#   create S parameter for getInput function to model weights
#   create ability for excitatory & inhibatory
#   create each neuron has it's on a-d parameters... (marticies for them)
#   create custom connectome/sparce connectome

## Set Up
numNeurons = 5
thresh = -50 #need to find a more accurate threshold
bias = 5 #izhivech 2003 used 5 * rnd for init, then used an S varible for the weights

dt = .025 #don't touch this
duration = 100 #needs to be an even number ; 100 = 4000 steps; 10 = 400
steps = int(duration / dt) #total steps
tmeSplt = steps/2 

tMinusZs = np.zeros((numNeurons, steps), dtype=np.float32)

#Parameters (RS)
a = .02
b = .2
c = -65
d = 2

#V and U matricies holding values for all timesteps
vMat = np.append(-65 * np.random.randint(2, size=(numNeurons, 1)), tMinusZs, 1)
uMat = np.append((b * -65) * np.random.randint(2, size=(numNeurons, 1)), tMinusZs, 1) #(izh 2003)

#network connectome
connect = np.random.randint(2, size=(numNeurons, numNeurons))
#plots the connectome
plt.imshow(connect, cmap=plt.cm.gray)
plt.title('connectome')
plt.show()

#plots the network graph (requires networkx)
G = nx.from_numpy_matrix(connect)
print('graph')
nx.draw(G)
plt.show()

#holds the spiking of the neurons ec. raster plot
spikes = np.zeros((numNeurons, steps), dtype=np.float32)

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

#iterates through fired, if connection, then increments input I
#this could be where hebbian learning etc. could be implimented
def getInput(numNeurons, vMat, connect, i, j, thresh, bias):
    I = 0
    for jj in range(0, numNeurons):
        #look at the current cell, i in connect, then iterate 
        #through each of it's connections. If there is a connection
        #then look at the vMat's voltage for that cell, jj, during the
        #current time step, j . if it is > thresh, increment I.  
        if connect[i][jj] == 1 and vMat[jj][j] > thresh:
            I += 1
    #print('Found ', I)
    return I + bias

## Simulation
t = 0
for j in range(steps): #steps - 1?
    for i in range(1, numNeurons):
        stm = getInput(numNeurons, vMat, connect, i, j, thresh, bias)
            
        #Neuron 1
        vi = vMat[i][j]
        ui = uMat[i][j]
        
        uOut, vOut = izh(.025, vi, ui, a, b, c, d, stm)
        
        if vOut > thresh:
            spikes[i][j] = 1
        
        vMat[i][j+1] = vOut
        uMat[i][j+1] = uOut
        
        

#Plotting
#this type is only feasible with a low cell count
plt.style.use('fivethirtyeight')
for i in range(0,5):
    plt.subplot(2,3,i+1)
    plt.title('cell ' + str(i+1))
    plt.plot(vMat[i])
    
plt.show()

