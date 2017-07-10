import random

# --------------------------------------------
# Fitness function for an individual genotype
# --------------------------------------------
def evaluate(g):
    fit = 0
    for a in g:
        if (a == 1):
            fit += 1
    return fit

# --------------------------------------------
# Initialize population of genotypes
# --------------------------------------------
def initPop(popsize, genesize):
    pop = []
    for i in range(popsize):
        ind = []
        for j in range(genesize):
            ind.append(random.randint(0,1))
        pop.append(ind)
    return pop

# --------------------------------------------
# Figure out who is the best individual in the population
# --------------------------------------------
def bestfit(pop):
    bestfit = 0
    bestind = -1
    for i in pop:
        fit = evaluate(i)
        if (fit > bestfit):
            bestfit = fit
            bestind = i
    return (bestfit,bestind)

# --------------------------------------------
# Microbial genetic algorithm
# --------------------------------------------
def microbialGA():

    # Parameters of the evolutionary run
    popsize =  ??               # size of the population
    genesize = ??               # number of cards
    tournaments = ??            # number of tournaments
    recombProb = ??             # recombination probability
    mutatProb = ??              # mutation probability

    # Initialize population
    pop = initPop(popsize, genesize)

    # Evolutionary loop
    for i in range(tournaments):

        # Report statistics every generation
        if (i%popsize==0):
            print(i, bestfit(pop))

        # Step 1: Pick 2 individuals, call them a and b
        #   Make sure they are two different individuals
        a = ??
        b = ??
        
        # Step 2: Compare their fitness, e.g., evaluate(pop[a]) and pick a winner and a loser
        winner = ??
        loser = ??

        # Step 3: Transfect genes from winner to loser
        for a in range(genesize):
            pop[loser][a] = ???

        # Step 4: Mutate the loser
        for a in range(genesize):
            pop[loser][a] = ???


microbialGA()
