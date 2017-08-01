import physLib as pl
#Movement inspired by Craig Reynolds's papers

class Agent:
    def __init__(self, target, ):

        self.maxSpeed = 10
        self.goal = [0]
        self.target = target
        self.current = [0,0]
        self.maxForce = 10

        #def sense():
            

        def think():
            #Subtract targets location from agents location
            self.goal = subV(self.target, self.current)
            #scale new vector by max speed
            self.goal = clampV(self.goal, self.maxSpeed)
            

        def move():
            steer = subV(self.goal, self.current)
            steer = clampV(steer, self.maxForce)
            
            
            
        
        
        
        
    
