import world

def sim(duration, preyNum):
    import turtle
##    import random
    prey = []
    for ii in range(1, preyNum):
        prey.append(world.Prey(11, True))
    
    pred = world.Predator(10, True)      
    time = 0                    
    while time < duration:      
        pred.sense(prey)
        pred.think(prey)
        pred.move()    

        for animal in prey:
            animal.think()
            animal.move()
            #eats animal code
            if pred.distanceTo(animal) < 5:
                print('Got One!')
                prey.remove(animal)
        if len(prey) == 0:
            print('All Gone!')
            break
        time += 1


def multipleRuns(duration,reps):
    import matplotlib.pyplot as plt
    rep = 0
    while rep < reps:
        d = sim(duration)
        plt.plot(d)
        rep += 1
    plt.show()

sim(1000, 4)
