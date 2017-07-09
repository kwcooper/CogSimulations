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

    def sense(self,pizza):
        self.memory = self.sensor    
        self.sensor = 1/(self.distance(pizza))

    def distance(self,pizza):
        return math.sqrt((self.x-pizza.x)**2 + (self.y-pizza.y)**2)

class Pizza:  ##

    def __init__(self, dist):
        angle = random.random()*2*math.pi
        self.x = dist * math.cos(angle)
        self.y = dist * math.sin(angle)


        
