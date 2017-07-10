import matplotlib.pyplot as plt
import numpy as np, random, math

# Agent class, looks for goal by altering
# orientation while keeping a constant velocity.
class Agent:
    def __init__(self):
        self.x = random.randint(-100,100) 
        self.y = random.randint(-100,100) 
        self.o = 0.0
        self.v = 5
        self.sensor = 0.0
        self.memory = 0.0

    #chooses random direction if the sensor is smaller than the remembered step. 
    def think(self,goal):
        #reverse sign to change wether agent attracts to goal or repels.
        #//possible pred/prey/goal simulation !?
        if self.sensor < self.memory:
              self.o = random.random()*2*math.pi
        else:
            self.o += 3 * ( 1/(1+self.distance(goal)) )
            
    def step(self):
        self.x += self.v*math.cos(self.o)
        self.y += self.v*math.sin(self.o)
        
    def sense(self,goal):
        #ud mem
        self.memory=self.sensor
        dist = self.distance(goal)
        #ud Sensor by a porpotional incriment
        self.sensor =1/(1+dist)
        
    def distance(self,goal):
        return math.sqrt((self.x-goal.x)**2 + (self.y-goal.y)**2)
         
        
class Goal:
    def __init__(self,distance):
        angle=random.random()*2*math.pi
        self.x=distance*math.cos(angle)
        self.y=distance*math.sin(angle)


    


