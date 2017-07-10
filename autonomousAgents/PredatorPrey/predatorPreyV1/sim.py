import world

def Hunt(duration):
    import matplotlib.pyplot as plt
##    import random
    deer1 = world.Agent(10, False)
    deer2 = world.Agent(10, False)
    deer3 = world.Agent(10, False)
##    prey = [deer1, deer2, deer3]
##    selection = random.choice(prey)
##    return selection

    tiger = world.predator(10,False)      # Create agent
    deer = world.Agent(10,False)
    time = 0                    # Initialize time
    distPred = []
    distPrey = []
    while time < duration:      # Simulation
        tiger.sense(deer1 or deer2 or deer3)
        tiger.think()          # Agent thinks
        tiger.move()           # Agent moves
        deer1.think()
        deer2.think()
        deer3.think()
        deer1.move()
        deer2.move()
        deer3.move()

        distPred.append(tiger.distanceTo(deer1 or deer2 or deer3))
        distPrey.append(deer1.distanceTo(tiger)) #make for loop
        
        time += 1
    pop = []
    i = 0                   # Initialize time  
    while time < duration:      # Simulation
        for agent in pop:
            agent.think()
            agent.move()
        time += 1

    return distPred, distPrey

def multipleRuns(duration,reps):
    import matplotlib.pyplot as plt
    rep = 0
    while rep < reps:
        pred, prey = Hunt(duration)
        plt.plot(pred)
        plt.plot(prey)
        rep += 1
    plt.show()
    

