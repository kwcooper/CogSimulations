import matplotlib.pyplot as plt
import numpy as np
#import random as rand

##class IchN():
##
##    def __init__(self, duration, dt, u, v, I, a, b, c, d):
##        self.u = u
##        self.v = v
##        self.I = I
##        self.a = a
##        self.b = b
##        self.c = c
##        self.d = d
##        self.t = 0
##        self.duration = duration
##        self.dt = dt
##        
##    def sim(self):
##        v_hist = [self.v]
##        u_hist = [self.u]
##        t_hist = [self.t]
##        
##        while self.t < self.duration:
##            if self.v > 30:
##                self.v = self.c
##                self.u = self.u + self.d
##
####                if self.t > 10:
####                    self.I = 1
##                
##                
##            dv = (.04 *( self.v ** 2)) + (5 * self.v) + 140 - self.u + self.I
##            du = self.a * ((self.b*self.v) - self.u)
##            
##            self.v = self.v + self.dt*dv
##            self.u = self.u + self.dt*du
##            self.t += self.dt
##            v_hist.append(self.v)
##            u_hist.append(self.u)
##            t_hist.append(self.t)
##        return v_hist,u_hist,t_hist, self.v
##
##
##
###a = decay rate
###b = u sensitivity
###c = v reset
###d = u reset amplitude
##
##
###           duration, dt,   u,    v,   I,   a,   b,   c,  d
##ich = IchN(100, .025, 0, -70, 10, .02, .2, -65, 2)
##v, u, t, vlt = ich.sim()
##
##plt.style.use('fivethirtyeight')
##plt.plot(t, v, label='v')
##plt.xlabel('Time')
##plt.ylabel('Voltage')
##plt.legend()
##plt.show()
##
##ich2 = IchN(100, .025, 0, -70, vlt, .02, .2, -65, 2)
##v, u, t, vlt = ich2.sim()
##
##
###bistability
###v, u, t = ich(100, .025, 0, -61, 10, .1, .26, -60, 0)
##
###chattering
###v, u, t = ich(100, .025, 0, -61, 10, .04, .2, -50, 2)
##
##
###plt.plot(t, u, label='u')
##plt.style.use('fivethirtyeight')
##plt.plot(t, v, label='v')
##plt.xlabel('Time')
##plt.ylabel('Voltage')
##plt.legend()
##plt.show()



#np.zeros()
#np.ones()






tmax = 1000
dt = 0.5

a = .02
b = .2
c = -65
d = 8

Iapp = 10
tr = np.array((200., 700)) / dt

T = np.ceil(tmax/dt)
v = np.zeros(T)
u = np.zeros(T)

v[0] = -70
u[0] = -14

for t in np.arange(T - 1):
    if t > tr[0] and t < tr[1]:
        I = Iapp
    else:
        I = 0

if v[t] < 35:
    dv = (.04 * v[t] + 5) * v[t] + 140 - u[t]
    v[t + 1] = v[t] + (dv + I) * dt
    du = a * (b * v[t] - u[t])
    u[t + 1] = u[t] + dt * du
else:
    v[t] = 35
    v[t + 1] = c
    u[t + 1] = u[t] + d

tvec = np.arange(0., tmax, dt)
plt.plot(tvec, v)

plt.show()






http://www.izhikevich.org/publications/spikes.pdf
https://github.com/sunzhe839/Izhikevichmodel/blob/master/TwoNeurons.py
http://www.ane.pl/pdf/7146.pdf
http://www.mjrlab.org/2014/05/08/tutorial-how-to-write-a-spiking-neural-network-simulation-from-scratch-in-python/
http://www.mjrlab.org/wp-content/uploads/2014/05/network_python_tutorial2013.pdf


















