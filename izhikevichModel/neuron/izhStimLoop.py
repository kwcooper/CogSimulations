import matplotlib.pyplot as plt

def ich(duration, dt, u, v, Ii, I2, a, b, c, d):
    t = 0
    I = Ii
    v_hist = [v]
    u_hist = [u]
    t_hist = [t]
    I_hist  = [Ii]
    
    while t < duration:
        if v > 30:
            v = c
            u = u + d

        if t > duration/2:
            I = I2
            
        dv = (.04 *( v ** 2)) + (5 * v) + 140 - u + I
        du = a * ((b*v) - u)
        
        v = v + dt*dv
        u = u + dt*du
        t += dt
        if t < duration/2:
            I_hist.append(Ii)
        else:
            I_hist.append(I2)
        v_hist.append(v)
        u_hist.append(u)
        t_hist.append(t)
    return v_hist,u_hist,t_hist, I_hist



#a = decay rate
#b = u sensitivity
#c = v reset
#d = u reset amplitude
times = 10
I2 = 0
for i in range(1, times):
    a = .02
    b = .2
    c = -65
    d = 2

    v = -70
    u = 0
    Ii = 0


    #             duration, dt,   u,    v,   I,   a,   b,   c,  d
    vHist, uHist, tHist, IHist = ich(100, .025, u, v, Ii, I2, a, b, c, d)

    #bistability
    #v, u, t = ich(100, .025, 0, -61, 10, .1, .26, -60, 0)

    #chattering
    #v, u, t = ich(100, .025, 0, -61, 10, .04, .2, -50, 2)


    #plt.plot(t, u, label='u')
    plt.style.use('fivethirtyeight')
##    plt.plot(tHist, vHist, label='v')
##    plt.plot(tHist,IHist, label='I')
##    plt.xlabel('Time')
##    plt.ylabel('Voltage')
##    plt.title(('I: ', I2, 'v:', v, 'u:', u, 'a:', a, 'b:', b, 'c:', c, 'd:', d))
##    plt.legend()
##    plt.show()

    plt.subplot(4, 3, i)
    plt.plot(tHist, vHist, label='v')
    plt.subplot(4,3,i)
    plt.plot(tHist,IHist, label='I')
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    #plt.title(('I: ', I2, 'v:', v, 'u:', u, 'a:', a, 'b:', b, 'c:', c, 'd:', d))
    plt.title(I2)
    

    

    I2 += 2

plt.show()    

    
