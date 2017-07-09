import random
import math

class Agent:

    def __init__(self):
        self.x = 0.0 # agent's x position
        self.y = 0.0 # agent's y position
        self.o = 0.0 # agent's orientation
        self.v = 1.0 # agent's velocity

    def step(self):
        self.o = random.random()*2*math.pi
        self.x += self.v*math.cos(self.o)
        self.y += self.v*math.sin(self.o)

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)
