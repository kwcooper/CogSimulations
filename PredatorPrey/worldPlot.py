import random
import math
import turtle

class Predator:
    
    def __init__(self, v, turtleON=False):
        self.x = random.randint(-100,100) # agent's x position
        self.y = random.randint(-100,100) # agent's y position
        self.o = random.random()*2*math.pi # agent's orientation
        self.v = 5 # agent's velocity
        self.su = 0 #agent speedup
        self.animalMem = 0
        self.animalMemCount = 9
        self.sensor = 0.0   ## current sensor stimuli
        self.memory = 0.0   ## past sensor stimuli
        self.turtleON = turtleON
        if turtleON:
            self.turtle = turtle.Turtle()
            self.turtle.color("red")

    def sense(self,others):
        minDist = 200
        n = 0
        for other in others:
            if self.distanceTo(other) < minDist:
                self.animalMem = n
                self.su = 1
                minDist = self.distanceTo(other)
                return self.distanceTo(other)
            else:
                minDist = 300
                self.su = 0
        n += 1
        
    def think(self, others):
            target = others[self.animalMem]
            dx = (target.x - self.x)
            dy = (target.y - self.y)
            ideal = math.atan2(dy,dx)
            self.o = ideal * random.random()
            
    def move(self):
        self.x += (self.v + self.su) * math.cos(self.o)
        self.y += (self.v + self.su) * math.sin(self.o)
        if self.turtleON:
            self.turtle.setpos(int(self.x),int(self.y))
        

    def distance(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def distanceTo(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    #A Different Way To go about sensing... Needs work
    def sense2(self,others):
        self.memory = self.sensor
        self.animalMemCount += 1
        dists = {}
        n = 0
        #make list of prey, choose closest one for 10 steps
        if self.animalMemCount > 10:
            for other in others:
                dists[n] = self.distanceTo(other)
                n += 1
            self.animalMem = min(dists)
            print('locked on to ', self.animalMem)
            self.su = 1
            self.animalMemCount = 0
            self.sensor = dists[min(dists)]
        else:
            #find the distance to locked on animal
            self.sensor = self.distanceTo(others[self.animalMem])


class Prey:
    
    def __init__(self, v, turtleON=False):
        self.x = random.randint(-100,100) # agent's x position
        self.y = random.randint(-100,100) # agent's y position
        self.o = random.random()*2*math.pi # agent's orientation
        self.v = v  # agent's velocity
        self.sensor = 0.0   ## current sensor stimuli
        self.memory = 0.0   ## past sensor stimuli
        self.turtleON = turtleON
        if turtleON:
            self.turtle = turtle.Turtle()
            color = (random.random(),random.random(),random.random())
            self.turtle.color(color)

    def distance(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def distanceTo(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def sense1(self,other):
        self.memory = self.sensor    
        self.sensor = 1/(self.distanceTo(other))

    def sense(self,others):
        minDist = 200
        n = 0
        for other in others:
            if self.distanceTo(other) < minDist:
                self.animalMem = n
                self.su = 1
                minDist = self.distanceTo(other)
                return self.distanceTo(other)
            else:
                minDist = 300
                self.su = 0
        n += 1

    def think(self):
        if self.memory >= self.sensor:
            self.o = random.random()*2*math.pi
        
    def move(self):
        self.x += self.v * math.cos(self.o)
        self.y += self.v * math.sin(self.o)
        if self.turtleON:
            self.turtle.setpos(int(self.x),int(self.y))
    


        


    
        
