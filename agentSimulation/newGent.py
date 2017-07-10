
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
        d = self.distanceTo(self.goal)
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
    


    def distance(self):
        return math.sqrt(self.pos[0] ** 2 + self.pos[1] ** 2)

    def distanceTo(self, inpt):
        return math.sqrt((self.pos[0] - inpt[0]) ** 2 + (self.pos[1] - inpt[1]) ** 2)
       
        
  
       

    
# Vector functions:
    
# Add two vectors together:
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])
    
# Subtract one vector from another:
def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])
    
# Multiply a vector's components by a scalar (a number):
def multiply(v, s):
    return (v[0] * s, v[1] * s)
    
# Divide a vector's components by a scalar (a number):
def divide(v, s):
    return (v[0] / s, v[1] / s)
    
# Calculate the magnitude of the vector: 
def magnitude(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)
    
# Converts a vector to a unit vector (maximum length of 1):
def normalize(v):
    return divide(v, magnitude(v))
   
# Scales a vector so its magnitude is equivalent to a scalar (a number):
def clamp(v, s):
    m = magnitude(v)
    if m > 0:
        return multiply(v, s / m)
    else:
        return v


        


def simulateBoids(duration):
    a = Agent(2, 0.15, True)
    goal = (random.randint(0,100), random.randint(0,100))
    # Run the simulation:
    for i in range(duration):
        
        goal = (goal[0] + random.randint(-20,20), goal[1] + random.randint(-20,20))
        a.sense(goal)
        a.think()
        a.move()

simulateBoids(1000)


