import matplotlib.pyplot as plt

##def ich(duration, dt, u, v, Ii, I2, a, b, c, d, stmTme):
##    t = 0
##    I = Ii
##    v_hist = [v]
##    u_hist = [u]
##    t_hist = [t]
##    I_hist  = [Ii]
##    stmTme = stmTme
##    
##    while t < duration:
##        if v > 30:
##            v = c
##            u = u + d
##
##        if t > stmTme:
##            I = I2
##        dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + I
##        du = a * ((b*v) - u)
##        
##        v = v + dt*dv
##        u = u + dt*du
##        t += dt
##        if t < stmTme:
##            I_hist.append(Ii)
##        else:
##            I_hist.append(I2)
##        v_hist.append(v)
##        u_hist.append(u)
##        t_hist.append(t)
##    return v_hist,u_hist,t_hist, I_hist
##
##



class IzhN():

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def step(self, dt, u, v, I):
        self.v = v
        self.u = u
        self.I = I
        self.dt = dt
        
        if self.v > 29:
            self.v = self.c
            self.u = self.u + self.d
        #print(self.v)
            
        dv = (.04 *( self.v ** 2)) + (5 * self.v) + 140 - self.u + self.I
        du = self.a * ((self.b*self.v) - self.u)
        
        self.v = self.v + self.dt*dv
        self.u = self.u + self.dt*du

        return self.v, self.u

dt = .025
u1 = 0
u2 = 0
v1 = -70
v2 = -70
I1 = 0
I2 = 0
duration = 10
t = 0

izh1 = IzhN(.025, .2, -65, 2)
izh2 = IzhN(.025, .2, -65, 2)

v1Hist = []
v2Hist = []
u1Hist = []
u2Hist= []
IHist = []

while t < duration:
    
    if t > 5:
        I1 = 7
    
    vo1, uo1 = izh1.step(t, u1, v1, I1)
    if v1 > 25:
        I2 = 6
            
    vo2, uo2 = izh2.step(t, u2, v2, I2)

    
    u1 = uo1
    u2 = uo2
    v1 = vo1
    v2 = vo2
    
    v1Hist.append(v1)
    v2Hist.append(v2)
    u1Hist.append(u1)
    u2Hist.append(u2)
    IHist.append(I1)               

    t += dt

plt.plot(v1Hist, label='1')
plt.plot(v2Hist, label='2')
plt.plot(IHist, label='I')
plt.plot(u1Hist,'--', label='u')
plt.plot(u2Hist, '--',label='u2')
plt.legend()
plt.show()
