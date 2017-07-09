import random
import math

class Agent:

    def __init__(self):
        self.x = 0.0 # agent's x position
        self.y = 0.0 # agent's y position
        self.o = 0.0 # agent's orientation
        self.v = 1.0 # agent's velocity
        self.sensor = 0.0   ## current sensor stimuli
        self.memory = 0.0   ## past sensor stimuli

    def think(self):
        ## Add your code here
        ## (but also, feel free to change anything else in the code)

    def move(self):
        self.x += self.v * math.cos(self.o)
        self.y += self.v * math.sin(self.o)

    def sense(self,goal):
        self.memory = self.sensor    
        self.sensor = 1/(self.distance(goal))

    def distance(self,goal):
        return math.sqrt((self.x-goal.x)**2 + (self.y-goal.y)**2)

class Goal:
    def __init__(self,distance):
        angle=random.random()*2*math.pi
        self.x=distance*math.cos(angle)
        self.y=distance*math.sin(angle)


        
