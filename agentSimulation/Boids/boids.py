#Keiland C and Christian A.
#based off boids code

import random
import math
import turtle

class Agent:
    
    def __init__(self, maxV, maxF, turtleON = False):
        self.pos = (0, 0) # The agent's position
        self.v = (-1 + 2 * random.random(), -1 + 2 * random.random()) # The agent's velocity
        self.maxV = maxV # The agent's maximum velocity
        self.maxF = maxF # The agent's maximum force
        self.minDistance = 60 # The minimum distance at which the agent will avoid other agents in the flock
        self.maxDistance = 300 # The maximum distance at which the agent can sense other agents in the flock
        self.neighbors = [] # The set of agents in the flock this agent can sense
        self.turtleON = turtleON
        if turtleON:
            self.turtle = turtle.Turtle()
            color = (random.random(), random.random(), random.random())
            self.turtle.color(color)
            self.turtle.speed(10)

    def think(self):
        # Get and weight the steering vectors:
        cohesion = multiply(self.cohere(), 0.9)
        alignment = multiply(self.align(), 0.9)
        separation = multiply(self.separate(), 1.5)
        # Sum the vectors:
        acceleration = add(add(cohesion, alignment), separation)     
        # Add the acceleration to the velocity:
        self.v = add(self.v, acceleration)
        # Prevent the velocity from exceeding the maximum velocity:
        self.v = clamp(self.v, self.maxV)
        
    def move(self):
        self.pos = add(self.pos, self.v)
        if self.turtleON:
            self.turtle.penup()
            self.turtle.setheading(math.atan2(self.v[1], self.v[0]) * 180 / math.pi)
            self.turtle.setpos(self.pos[0], self.pos[1])
            self.turtle.pendown()
    
    # Detect nearby agents in the flock:
    def sense(self, flock):
        self.neighbors = []
        for agent in flock:
            # Get the distance to the other agent:
            d = self.distanceTo(agent)
            if d > 0 and d < self.maxDistance:
                self.neighbors.append(agent)

    def distance(self):
        return math.sqrt(self.pos[0] ** 2 + self.pos[1] ** 2)

    def distanceTo(self, other):
        return math.sqrt((self.pos[0] - other.pos[0]) ** 2 + (self.pos[1] - other.pos[1]) ** 2)
       
        
    # Generate a steering vector, to move towards the center of the agent's neighborhood:
    def cohere(self):
        steer = (0, 0) # The steering vector
        if len(self.neighbors) == 0:
            return steer
        for neighbor in self.neighbors:
            # Add the neighbor's position vector to the steering vector:
            steer = add(steer, neighbor.pos)
        # Average the steering vector by the number of neighbors:
        steer = divide(steer, len(self.neighbors))
        # Normalize the steering vector:
        steer = normalize(steer)
        # Multiply the steering vector by the maximum velocity:
        steer = multiply(steer, self.maxV)
        # Subtract the agent's motion vector:
        steer = subtract(steer, self.v) 
        # Clamp the steering factor by the maximum force:
        steer = clamp(steer, self.maxF)
        return steer
        
     # Generate a steering vector, to turn the agent to match the orientation of its neighbors:
    def align(self):
        steer = (0, 0) # The steering vector
        if len(self.neighbors) == 0:
            return steer
        for neighbor in self.neighbors:
            # Add the neighbor's motion vector to the steering vector:
            steer = add(steer, neighbor.v)
        # Average the steering vector by the number of neighbors
        steer = divide(steer, len(self.neighbors))
        # Normalize the steering vector:
        steer = normalize(steer)
        # Multiply the steering vector by the maximum velocity:
        steer = multiply(steer, self.maxV)
        # Subtract the agent's motion vector:
        steer = subtract(steer, self.v)
        # Clamp the steering factor by the maximum force:
        steer = clamp(steer, self.maxF)
        return steer
       
    # Generate a steering vector, to move the agent away from too-close neighbors:
    def separate(self):
        steer = (0, 0) # The steering vector
        influences = 0 # The number of neighbors influencing the agent
        for neighbor in self.neighbors:
            distance = self.distanceTo(neighbor)   
            # Move away from the neighbor if it is too close:
            if distance < self.minDistance:
                # Get the vector to the neighbor:
                v = subtract(self.pos, neighbor.pos)
                # Normalize the vector:
                v = normalize(v)
                # Weight the vector by the distance (closer neighbors should have more impact): 
                v = divide(v, distance)
                # Add the vector to the steering vector:
                steer = add(steer, v)
                # Increment the count:
                influences = influences + 1
        # Check if any neighbors were within the minimum distance:
        if influences > 0:
            # Average the steering vector by the number of influences
            steer = divide(steer, influences)
            # Normalize the steering vector:
            steer = normalize(steer)
            # Multiply the steering vector by the maximum velocity:
            steer = multiply(steer, self.maxV)
            # Subtract the agent's motion vector:
            steer = subtract(steer, self.v)
            # Clamp the steering factor by the maximum force:
            steer = clamp(steer, self.maxF)
        return steer
    
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
    

