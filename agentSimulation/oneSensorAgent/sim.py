import agent as Agent
import math
import matplotlib.pyplot as plt

#single Run
def mRun(duration):
    a = Agent.Agent()
    food = Agent.Goal(100)
    time = 0
    xHist = [ ]
    yHist = [ ]
    tHist = [ ]
    dist = [ ]
    
    while time<duration:
        xHist.append(a.x)
        yHist.append(a.y)
        tHist.append(time)
        dist.append(math.sqrt((a.x-food.x)**2+(a.y-food.y)**2))
        a.sense(food)
        a.think(food)
        a.step()
        time+=1
        
    plt.subplot(2,1,1)
    plt.scatter(xHist,yHist,s=50,c=tHist,alpha=0.5)
    plt.plot(food.x, food.y, '^w')
    plt.title('Birds eye')
    
    plt.subplot(2,1,2)
    plt.plot(tHist,dist)
    plt.xlabel('Steps')
    plt.ylabel('Distance')
    return(tHist,dist)

#multiple runs
def mRuns(duration, reps):
    rep = 0
    while rep < reps:
        t,d = mRun(duration)
        plt.plot(t,d)
        plt.title('Distances')
        rep+=1
    plt.show()

    

mRuns(100,20)
