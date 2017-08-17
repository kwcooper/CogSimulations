#Mit
# probablility of selection = fitness
#probability of selection = realitive fitness
#probability of fitness = realitive fitness and the max diversity
#Sims creatures

#nature of code
#setup n  elements
# evaluate the fitness of n elements, create a mating pool
# repeat
    #pick parents based on fitness
    #create child by crossing over the features of the parents
    #mutate the childs features by some probablilty
    #add the child to the population

#if n parents, probability = 1/n

#genotypes = data
#phenotypes = expressions

#things to think about
#a good fitness function
#how to encode the data

import random

goal = "genetic algorithm"
features = "abcdefghijklmnopqrstuvwxyz "
goalLength = len(goal)
popSize = 10


#setup
#create a random population of genetic material


def makePop(goalLength, popSize, features):
    population = []
    for i in range(popSize):
        newMember = ""
        for ii in range(goalLength):
            newMember += features[random.randint(0,len(features)-1)]
        population.append(newMember)
    return population

#run
# what is your fitness function?
# in our case, it could be the number of charaectors in the target phrase
def getFit(goal, memB):
    score = 0
    bestFit = False
    for l, ll in zip(goal, memB):
        if l == ll:
            #print(memB, ": ", ll)
            score += 1
        if score == len(goal):
            bestFit = True
    return score, bestFit

def assignFits(goal, population):
    fitList = []
    for i in range(len(population)):
        fit, bestFit = getFit(goal, population[i])
        fitList.append(fit)
        if bestFit == True:
            print(i, " is the answer.")
    return fitList, bestFit


#sortFittest?

def sortFittest(fitList, population):
    pop = [pop for (fl,pop) in sorted(zip(fitList,population))]
    fitList = sorted(fitList)
    fitList = list(reversed(fitList))
    pop = list(reversed(pop))
    return pop, fitList


#take the x most fit

"""
def makeChild(pop, goalLength, fitslice):
    #assumes that pops are in fitness order...
    child = []
    slicer = random.randint(0, goalLength)
    #for i in range(len(pop[0:fitslice])):
        #need to make sliding window
        #divide by the length of parents
        #let's just assume fitslice == 2 for now
        #child = topPops[i][0:slicer]
    child = pop[0][0:slicer] + pop[1][slicer:goalLength]
    return child

def newPop(childs, goalLength, popSize, features):
    newPop = childs
    #print(newPop)
    randPop = makePop(goalLength, (popSize-len(childs)), features)
    for i in randPop:
        newPop.append(i)
    #print(newPop)
    return newPop
"""


def matePool(pop, fitList):
    pool = []
    for i in range(len(pop)):
        if fitList[i] > 0:
            for ii in range(0, fitList[i]):
                pool.append(pop[i])
    return pool


def mutateChild(child, prob, features):
    #takes a number prob, between 1 and 100.
    #closer to 100, the lesser the probability
    rnd = random.randint(0, 100)
    #make the string a list because strings in py are imutable
    child = list(child)
    for i in range(len(child)-1):
        rnd = random.randint(0, 100)
        if rnd > prob:
            #print("Mutate!")
            child[i] = features[random.randint(0, len(features)-1)]
    #convert back into string
    strChild = ""
    for i in child:
        strChild += str(i)
    return strChild


def makeChild(pool, slicer, goalLength):
    p1 = pool[random.randint(0, len(pool)-1)]
    p2 = pool[random.randint(0, len(pool)-1)]

    #print("P1: ", p1, "  p2: ", p2)
    if slicer == 0:
        slicer = random.randint(0, goalLength-1)
    
    child = p1[0:slicer] + p2[slicer:goalLength]
    #print("child: ", child)
    return child
    

def makeChildren(popSize, pool, slicer, goalLength, prob, features):
    #assuming constant popsize, with successful children
    childs = []
    for i in range(0, popSize):
        child = makeChild(pool, slicer, goalLength)
        child = mutateChild(child, prob, features)
        childs.append(child)
    return childs
    






        
 #run
#make pop
population = makePop(goalLength, popSize, features)
print(population)

#should loop this prolly
#assign fits
itterations = 0
fitHuh = False
while fitHuh == False:

    fitList, bestFit = assignFits(goal, population)
    #print("fitlist: ", fitList)

    #sort by the fittest
    pop, fl = sortFittest(fitList, population)

    pool = matePool(pop, fitList)
    #print("fitlist: ", fitList)
    #print("pool:", pool)

    child = makeChild(pool, 0, goalLength)
    
    childs = makeChildren(popSize, pool, 0, goalLength, 90, features)
    #print(childs)

    pop = childs
    #make x children with fittest
    #childs = makeChildren(pop, goalLength, 2, 4)
    #print("children: ", childs)

    #make new pop
    #pop = newPop(childs, goalLength, popSize, features)
    #print("new Pop: ", pop)

    itterations += 1
    if itterations == 1000:
        print("over 10000")
        break
print(pop)
print("fitlist: ", fitList)


    













            



#Selection
