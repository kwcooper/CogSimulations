#eduardo's problem

import random
import math
import matplotlib.pyplot as plt

gSet = [1,2,3,4,5,6,7,8,9]

def makeParent(gSet):
    #generates a random parent
    a = (gSet[random.randint(0, len(gSet)-1)])
    b = (gSet[random.randint(0, len(gSet)-1)])
    parent = [a,b]
    return parent

def makePop(N, gSet):
    #makes a population of parents
    pop = []
    for i in range(0,N):
        pop.append(makeParent(gSet))
    return pop

def getFit(a, b):
    #plug both values into the function to get fitness
    fit = 200 - (a**2 + b**2)
    return(fit)

def assignFits(pop):
    #assign fitness to each of the subs
    fitList = []
    for i in pop:
        fitList.append(getFit(i[0], i[1]))
    return fitList


def sortPop(population, fitList):
    pop = [pop for (fl,pop) in sorted(zip(fitList,population))]
    fitList = sorted(fitList)
    fitList = list(reversed(fitList))
    pop = list(reversed(pop))
    return pop, fitList


def makePool(pop, fitList, minFit):
    pool = []
    #add to pool by half the number of fitness (to control pool size)
    for i in range(len(fitList)):
        if fitList[i] > minFit:
            for ii in range(math.floor(fitList[i]/2)):
                pool.append(pop[i])
    return pool


def makeChild(pool):
    p1 = pool[random.randint(0, len(pool)-1)]
    p2 = pool[random.randint(0, len(pool)-1)]

    idx1 = random.randint(0,1)
    idx2 = random.randint(0,1)
    idx3 = random.randint(0,1)
    p = [p1, p2]
    child = [p[idx3][idx1], p[idx3][idx2]]

    
    #print("p1: ", p1, "p2: ", p2, "child: ", child)
    return child

def makeChildren(pool, numChilds):
    newPop = []
    for i in range(numChilds):
        child = makeChild(pool)
        newPop.append(child)
    return newPop 

def popFitAvg(pop):
    fits = 0
    for i in pop:
        fits += getFit(i[0], i[1])
    return fits / len(pop)
    


#Run Sim
pop = makePop(5,gSet)

popAvgs = []
for i in range(100):
    fl = assignFits(pop)
    #print(pop)
    pop, fitList = sortPop(pop, fl)
    #print(pop)
    pool = makePool(pop, fitList, 10)

    pop = makeChildren(pool, 5)
    #print(pop)
    
    #the preformance of the algorithm
    popAvgs.append(popFitAvg(pop))


#plot the average of each population (preformance)
plt.plot(popAvgs)
plt.show()


