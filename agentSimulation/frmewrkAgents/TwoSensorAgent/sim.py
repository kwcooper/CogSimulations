import world
import matplotlib.pyplot as plt

def singleWalk(duration):
    cashew = world.Agent()      # Create agent
    food = world.Pizza(100)     ## Create food
    time = 0                    # Initialize time
    x_hist = []                 # Lists for keeping data
    y_hist = []
    t_hist = []
    d_hist = []   
    while time < duration:      # Simulation
        cashew.sense(food)
        cashew.think()
        cashew.move()           # Agent takes a step       
        x_hist.append(cashew.x) # Record data
        y_hist.append(cashew.y)
        t_hist.append(time)
        d_hist.append(cashew.distance(food))       
        time += 1               # Increase time
    plt.subplot(2,1,1)          # Plot
    plt.scatter(x_hist,y_hist,s=50,c=t_hist,alpha=0.5)
    plt.title("Bird eye view")
    plt.subplot(2,1,2)
    plt.plot(t_hist,d_hist)
    plt.xlabel("steps")
    plt.ylabel("distance")
    plt.show()
    return(t_hist,d_hist)

def multipleRuns(duration,reps):
    rep = 0
    while rep < reps:
        t,d = singleWalk(duration)
        plt.plot(t,d)
        rep += 1
    plt.show()
    
