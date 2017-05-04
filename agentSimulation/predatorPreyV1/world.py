import random
import math
import turtle

class predator:
    
    def __init__(self, v, turtleON=False):
        self.x = random.randint(-100,100) # agent's x position
        self.y = random.randint(-100,100) # agent's y position
        self.o = random.random()*2*math.pi # agent's orientation
        self.v = v # agent's velocity
        self.sensor = 0.0   ## current sensor stimuli
        self.memory = 0.0   ## past sensor stimuli
        self.turtleON = turtleON
        if turtleON:
            self.turtle = turtle.Turtle()
 #           color = (random.random(),random.random(),random.random())
            self.turtle.color("red")

    def think(self):
        if self.memory >= self.sensor:
            self.o = random.random()*2*math.pi
        
    def move(self):
        self.x += self.v * math.cos(self.o)
        self.y += self.v * math.sin(self.o)
        if self.turtleON:
            self.turtle.setpos(int(self.x),int(self.y))
    
    def sense(self,other):
        self.memory = self.sensor    
        self.sensor = 1/(self.distanceTo(other))

    def distance(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def distanceTo(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Agent:
    
    def __init__(self, v, turtleON=False):
        self.x = random.randint(-100,100) # agent's x position
        self.y = random.randint(-100,100) # agent's y position
        self.o = random.random()*2*math.pi # agent's orientation
        self.v = v # agent's velocity
        self.sensor = 0.0   ## current sensor stimuli
        self.memory = 0.0   ## past sensor stimuli
        self.turtleON = turtleON
        if turtleON:
            self.turtle = turtle.Turtle()
            color = (random.random(),random.random(),random.random())
            self.turtle.color(color)

    def think(self):
        if self.memory >= self.sensor:
            self.o = random.random()*2*math.pi
        
    def move(self):
        self.x += self.v * math.cos(self.o)
        self.y += self.v * math.sin(self.o)
        if self.turtleON:
            self.turtle.setpos(int(self.x),int(self.y))
    
    def sense(self,other):
        self.memory = self.sensor    
        self.sensor = 1/(self.distanceTo(other))

    def distance(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def distanceTo(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

        
