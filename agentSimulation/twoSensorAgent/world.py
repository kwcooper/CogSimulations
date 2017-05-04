import random
import math
import numpy

class Agent:

    def __init__(self):
        self.x = 0.0                # agent's x position
        self.y = 0.0                # agent's y position
        self.o = 0.0                # agent's orientation
        self.vls = 0.5
        self.vrs = 0.5              # agent's velocity
        self.r = 1.0                # agent's radius
        self.a = math.pi/4          # left/right sensor angle offset
        self.ls = 0.0               # left sensor value
        self.rs = 0.0               # right sensor value
        self.rsx = self.r * math.cos(self.o + self.a)   # right sensor x position
        self.rsy = self.r * math.sin(self.o + self.a)   # right sensor y position
        self.lsx = self.r * math.cos(self.o - self.a)   # left sensor x position
        self.lsy = self.r * math.sin(self.o - self.a)   # left sensor y position

    def sense(self,pizza):
        # Calculate the distance of the pizza to the sensors
        self.ls = 1/math.sqrt((self.lsx-pizza.x)**2 + (self.lsy-pizza.y)**2)
        print(self.ls)
        self.rs = 1/math.sqrt((self.rsx-pizza.x)**2 + (self.rsy-pizza.y)**2)
        print(self.rs)

    def think(self):
        self.vls = 1/self.ls 
        self.vrs = 1/self.rs
        ## Add your code here
        ## (but also, feel free to change anything else in the code)

    def move(self):
        # Update position of the agent
        self.x += self.vls*math.cos(self.o)
        self.y += self.vrs*math.sin(self.o)
        # Update position of the sensors
        self.rsx = self.x + self.r * math.cos(self.o + self.a)
        self.rsy = self.y + self.r * math.sin(self.o + self.a)
        self.lsx = self.x + self.r * math.cos(self.o - self.a)
        self.lsy = self.y + self.r * math.sin(self.o - self.a)
        
    def distance(self,pizza): 
        return math.sqrt((self.x-pizza.x)**2 + (self.y-pizza.y)**2)
    
class Pizza:  ##

    def __init__(self, dist):
        angle = random.random()*2*math.pi
        self.x = dist * math.cos(angle)
        self.y = dist * math.sin(angle)


        
