import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
numNeurons = 50
steps = 1

dtMat = .025 *np.ones((numNeurons, 1), dtype=np.float32)

aMat = .02*np.ones((numNeurons, 1), dtype=np.float32)
bMat = .2*np.ones((numNeurons, 1), dtype=np.float32)
cMat = -65. * np.ones((numNeurons, 1), dtype=np.float32)
dMat = 2. * np.ones((numNeurons, 1), dtype=np.float32)

vMat = -65. * np.ones((numNeurons, 1), dtype=np.float32)
#vMat = -65 *np.random.randint(2, size=(numNeurons, 1))
print('vMat:\n', vMat)
uMat = 0. * np.random.randint(2, size=(numNeurons, 1))

dtN = np.ones((numNeurons, 1), dtype=np.float32)
vN = np.ones((numNeurons, 1), dtype=np.float32)
uN = np.ones((numNeurons, 1), dtype=np.float32)

connect = np.random.randint(2, size=(numNeurons, numNeurons))
#connect = np.random.random((numNeurons, numNeurons))
print('con:\n', connect)


def getI(vMat, connect, i):
    I = 0
    for j in range(0, numNeurons):
        if vMat[i] > 25 and connect[i][j] == 1:
            I += 1
    return I + 2

spikes = np.zeros((numNeurons, int(np.ceil(steps/.025))))
t = 0
while t < steps:
    
    if isinstance(t, int):
        print()
        print(t,':',  end=" ")
        
    for i in range(0, numNeurons):
        I = getI(vMat, connect, i)
        if isinstance(t, int):
            print(I, end=" ")

        u = uMat[i]
        v = vMat[i]
        a = aMat[i]
        b = bMat[i]
        c = cMat[i]
        d = dMat[i]
        
        dt = dtMat[i]
        
        if v > 30:
            spikes[i][t] = 1
            v = c
            u = u + d
            
        dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + 5
        du = a * ((b*v) - u)

        v = v + dt*dv
        u = u + dt*du

        uN[i] = u
        vN[i] = v
        #print('new vMat:\n', vMat)

    uMat = uN
    vMat = vN
    #print(vMat)

    t += dt


G=nx.from_numpy_matrix(connect)
print('graph')
nx.draw(G)
plt.show()

print()
print(vMat)
            


