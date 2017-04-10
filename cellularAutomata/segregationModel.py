import numpy as np
import random
import matplotlib.pyplot as plt

class City:

    def  __init__(self, size):
        self.size = size
        self.pop = np.zeros((size,size))
        self.emptyProb = 0.1
        self.paProb = 0.5
        self.populate()

    def populate(self):
        #iterate through the matrix, adding houses
        #i column, j row
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.emptyProb:
                    self.pop[i][j] = 0 #zero is vacent
                else:
                    if random.random() < self.paProb:
                        self.pop[i][j] = -1 #repub
                    else:
                        self.pop[i][j] = 1

    def show(self):
        plt.imshow(self.pop, interpolation="nearest", cmap="bwr")
        plt.show()


    def step(self):
        #pick random nonvacent house
        i,j = self.randomHouse()
        #count Kin, not happy? MOVE OUT THE WAY
        if self.numberKin(i,j) < 3:
            self.move(i,j)

    def randomHouse(self):
        found = False  #add a flag
        while not found:
            i = random.randint(0,self.size-1) #returns random number from a to b, Set this to be dynamic
            j = random.randint(0,self.size-1)
            if self.pop[i][j] != 0:
                found = True
        return i,j

    def numberKin(self,i,j):
        #add a thresh to save cpu cycles
        kin = 0
        mypa = self.pop[i][j]
        #look for the neighbors to the chosen square
        for x in [-1,0,1]:
            ni = (i - x) % self.size #be ready for wrapping!!!!!!!!!
            for xx in [-1,0,1]:
                nj = (- xx) % self.size
                if mypa == self.pop[ni][nj]:
                    kin += 1

      
a = City(100)
a.show()


        
            
        
                
            
