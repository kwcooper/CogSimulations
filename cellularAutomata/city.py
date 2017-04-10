import numpy as np
import random
import matplotlib.pyplot as plt

## Class

class City():

    def __init__(self,size):
        self.size = size
        self.kinPref = 3
        self.pop = np.zeros((size,size))
        self.emptyProb = 0.1
        self.raceProb = 0.5
        self.populate()

    def populate(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.emptyProb:
                    self.pop[i][j] = 0
                else:
                    if random.random() < self.raceProb:
                        self.pop[i][j] = -1
                    else:
                        self.pop[i][j] = 1

    def show(self):
        plt.imshow(self.pop,interpolation="nearest",cmap="bwr")
        plt.show()

    def step(self):
        # Pick a random non-vacant house
        i,j = self.randomHouse()
        # Check to see if person is unhappy, if so, move to vacant random place
        if self.numberKin(i,j) < self.kinPref:
            self.move(i,j)

    def randomHouse(self):
        found = False
        while not found: 
            # Pick a random new location
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            # Check to see if it is populated
            if self.pop[i][j] != 0:
                found = True
        return i,j

    def numberKin(self,i,j):
        kin = 0  # variable to keep track of kin seen so far
        myrace = self.pop[i][j]   # look in the mirror for a sec
        # check each of your neighbors
        for x in [-1,0,1]:
            ni = (i-x)%self.size
            for y in [-1,0,1]:
                nj = (j-y)%self.size
                if myrace == self.pop[ni][nj]:
                    kin += 1
        return kin-1

    def move(self,i,j):
        # Find a vacant house
        ni,nj = self.findVacant()
        # Move
        self.pop[ni][nj] = self.pop[i][j]
        self.pop[i][j] = 0
        
    def findVacant(self):
        found = False
        while not found: 
            # Pick a random new location
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            # Check to see if it is populated
            if self.pop[i][j] == 0:
                found = True        
        return i,j

    def segregationIndex(self):
        # A value between 0 and 1, where 1 is highly segregated, and 0 is very diverse
        avgkin = 0.0
        for i in range(self.size-1):
            for j in range(self.size-1):
                k = self.numberKin(i,j)
                avgkin += k/8
        return avgkin/(self.size*self.size)

## Simulation

def simCityPlot(size,years):
    a = City(size)
    seg_Hist = []
    seg_Hist.append(a.segregationIndex())
    a.show()
    t = 0
    while t < years*size:
        a.step()
        t+=1
        if t%(100*size)==0:  # show pop every 10 years
            seg_Hist.append(a.segregationIndex())
    a.show()
    plt.plot(seg_Hist)
    plt.xlabel("Time")
    plt.ylabel("Segregation Index")
    plt.show()

def simCityData(size,years):
    a = City(size)
    seg_Hist = []
    seg_Hist.append(a.segregationIndex())
    t = 0
    while t < years*size:
        a.step()
        t+=1
        if t%(100*size)==0:  # show pop every 10 years
            seg_Hist.append(a.segregationIndex())
    return(seg_Hist)


simCityPlot(100, 10000)
