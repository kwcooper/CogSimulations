import boids

def simulateBoids(duration, flockSize):
    # Create the flock:
    flock = []
    for i in range(flockSize):
        flock.append(boids.Agent(2, 0.15, True))
    # Run the simulation:
    for i in range(duration):
        for agent in flock:
            agent.sense(flock)
            agent.think()
            agent.move()

simulateBoids(100, 5)
