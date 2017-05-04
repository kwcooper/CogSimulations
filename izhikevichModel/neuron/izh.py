import matplotlib.pyplot as plt

#the Izhikevich mode
def izh(duration, dt, u, v, Ii, I2, a, b, c, d, stmTme):
    #init vars
    t = 0
    I = Ii
    stmTme = stmTme
    
    #plotting stuff
    v_hist = [v]
    u_hist = [u]
    t_hist = [t]
    I_hist  = [Ii]
    

    #run the simulation for a certain amount of time
    while t < duration:
        #this resets the voltage once the neuron spikes
        if v > 30:
            v = c
            u = u + d
        #this resets I past a certain point, akin to a stimulation
        if t > stmTme:
            I = I2
        #update based on equations
        dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + I
        du = a * ((b*v) - u)
        
        v = v + dt*dv
        u = u + dt*du

        #update time based on the dt step
        t += dt
        #append I for stim plot
        if t < stmTme:
            I_hist.append(Ii)
        else:
            I_hist.append(I2)
        #plotting
        v_hist.append(v)
        u_hist.append(u)
        t_hist.append(t)
        
    return v_hist,u_hist,t_hist, I_hist



#parameters
times = 10
Ii = 0
I2 = 20
a = .00008
b = 3
c = -65.8
d = 5

v = -61.8
u = 0

#                                       duration, dt,   u,    v,   I,   a,   b,   c,  d
vHist, uHist, tHist, IHist = izh(100, .025, u, v, Ii, I2, a, b, c, d, 20)

#Here are other parameters to expiriment with.
#bistability
#v, u, t = izh(100, .025, 0, -61, 10, .1, .26, -60, 0)

#chattering
#v, u, t = izh(100, .025, 0, -61, 10, .04, .2, -50, 2)


#plotting Information
#plt.plot(t, u, label='u')
plt.style.use('fivethirtyeight')
plt.plot(tHist,IHist,'r', label='I')
plt.plot(tHist, vHist, label='v')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('pyramidal, cell 4 (weak adapt; stim 20)')
#uncomment below if you want the parameters on the plot (can be messy)
#plt.title(('I: ', I2, 'v:', v, 'u:', u, 'a:', a, 'b:', b, 'c:', c, 'd:', d))
plt.legend()
plt.show()


    
