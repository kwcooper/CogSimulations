import worldPlot as world
import numpy as np
import time

def sim(duration, preyNum, turt):
    import turtle
##    import random
    prey = []
    for ii in range(1, preyNum):
        prey.append(world.Prey(5, turt))
    
    pred = world.Predator(10, turt)      
    tme = 0
    eatTimes = []
    dist = []
    while tme < duration:      
        pred.sense(prey)
        pred.think(prey)
        pred.move()

        for animal in prey:
            animal.sense([pred])
            animal.think([pred])
            animal.move()
            dist.append(pred.distanceTo(animal))
            #eats animal code
            if pred.distanceTo(animal) < 5:
                print('Got One!')
                eatTimes.append(tme)
                prey.remove(animal)
                
        if len(prey) == 0:
            print('All Gone!')
            print(eatTimes)
            return eatTimes, dist
        tme += 1


def multipleRuns(duration,reps):
    import matplotlib.pyplot as plt
    rep = 0
    times = []
    while rep < reps:
        t,d = sim(1000, 4, False)
        #plt.plot(d)
        rep += 1
        plt.vlines(t,0,.1,linestyles='-',colors='black')

##    plt.title('Time Captured')
##    plt.xlabel('Time')
##    plt.ylabel('Distance')
##
    plt.title('Predator Hunting Prey')
    plt.xlabel('Time')
    plt.ylabel('(Arbitrary Height)')
    plt.show()
    return times


#multipleRuns(100, 20)
def plot():
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    t,d = sim(1000, 4, False)
    print(d)
    print(len(d))
    y1 = range(1,(len(t)+1))
    y2 = range(1,(len(d)+1))

    plt.title('Predator Hunting Prey')
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.vlines(t,0,.1,linestyles='-',colors='black')
    #plt.plot(y2, d)
    plt.show()

    multipleRuns(1000, 100)
    #sim(1000, 4, True)

sim(1000, 5, True)
