
import random
import math
import turtle
import physLib as pl

class Agent:
    def __init__(self, maxV, maxF, turtleON = True):
        self.goal = (0,0)
        self.pos = (0, 0) # The agent's position
        self.v = (-1 + 2 * random.random(), -1 + 2 * random.random()) # The agent's velocity
        self.maxV = maxV # The agent's maximum velocity
        self.maxF = maxF # The agent's maximum force
        self.capd = False
        self.turtleON = turtleON
        if turtleON:
            self.turtle = turtle.Turtle()
            self.goalD = turtle.Turtle()
            color = (random.random(), random.random(), random.random())
            self.turtle.color(color)
            color = (random.random(), random.random(), random.random())
            self.goalD.color(color)
            self.turtle.speed(100)

    def sense(self, goal):
        self.goal = goal
        d = pl.distanceTo(self.pos, self.goal)
        dist = pl.subV(self.goal, self.pos)
        if dist < (.5, .5):
            self.capd = False
        elif dist > (.5, .5):
            self.capd = False
            print(dist)

    def think(self):
        # Sum the vectors from different functions
        if self.capd == False:
            dist = pl.subV(self.goal, self.pos)
            # Add the acceleration to the velocity:
            self.v = pl.addV(self.v, dist)
            # crop speed by maximum velocity:
            self.v = pl.clampV(self.v, self.maxV)
        else:
            self.pos = self.pos
        
    def move(self):
        if self.capd == False:
            self.pos = pl.addV(self.pos, self.v)
        if self.turtleON:
            self.turtle.penup()
            self.turtle.setheading(math.atan2(self.v[1], self.v[0]) * 180 / math.pi)
            self.turtle.setpos(self.pos[0], self.pos[1])
            self.turtle.pendown()
            self.goalD.setpos(self.goal[0], self.goal[1])
            self.goalD.pendown()
    

    def distanceTo(self, inpt):
        return math.sqrt((self.pos[0] - inpt[0]) ** 2 + (self.pos[1] - inpt[1]) ** 2)
       

    


        
# Run the simulation:
def runSim(duration):
    a = Agent(2, 0.15, True)
    goal = (random.randint(0,100), random.randint(0,100))
    for i in range(duration):
        
        #goal = (goal[0] + random.randint(-20,20), goal[1] + random.randint(-20,20))
        a.sense(goal)
        a.think()
        a.move()

runSim(1000)


