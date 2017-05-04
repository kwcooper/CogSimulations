#Created by Eugene M. Izhikevich, February 25, 2003
#translated from MatLab by Keiland Cooper, April 2017
import numpy as np
import matplotlib.pyplot as plt

ne = 80
ni = 20
re = np.random.rand(ne, 1)
ri = np.random.rand(ni, 1)

a = np.concatenate((.02*np.ones((ne, 1), dtype=np.int16), (.02 + (.08 * ri))))
b = np.concatenate((.2*np.ones((ne, 1), dtype=np.int16), (.25 - (.05 * ri))))
c = np.concatenate((-65 + (15* np.power(re, 2)), (-65 * np.ones((ni, 1), dtype=np.int16))))
d = np.concatenate((8 - (6 * np.power(re, 2)), (2 * np.ones((ni, 1), dtype=np.int16) )))
s = np.concatenate((.5 * np.random.rand(ne, (ne+ni)), (-1 * np.random.rand(ni, (ne+ni))) ))


v = -65 * np.ones(((ne + ni), 1), dtype=np.int16)
u = np.multiply(b, v)

fireing = []
fireings = []
t = 0
while t < 1000:
    I = np.concatenate((5 * np.random.rand(ne, 1), (2 * np.random.rand(ni, 1)) ))
    fired = []
    for ii in range(1, len(v)):
        if v[ii] > 30:
            fired.append(ii)
    zz = np.zeros((1, len(fired)))
    fireings = np.concatenate((fireings, fired))
    #fireings = np.concatenate((fireings, (t + zz, fired)))

    for ii in fired:
        v[ii] = c[ii]
        u[ii] = u[ii] + d[ii]
        
    I = I + 2;

    v = (.04 * np.power(v, 2)) + (5 * v) + 140 - u + I
    
##    v = v + .5 * (.04 * np.power(v, 2) + (5 * v) + 140 - u + I)
##    v = v + .5 * (.04 * np.power(v, 2) + (5 * v) + 140 - u + I)
    u = u + a * (b * v - u)

    if t % 100 == 0:
        print(t)
        

    t += 1

plt.plot(v)
plt.show()

plt.plot(fireings)
plt.show()

