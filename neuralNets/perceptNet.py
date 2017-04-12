import random
import numpy as np

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Perceptron:

    def __init__(self):
        self.w1 = random.random()*2-1
        self.w2 = random.random()*2-1
        self.bias = random.random()*2-1
        self.lc = 0.1  # learning constant

    def forward(self, i1, i2):
        netinput = (i1 * self.w1) + (i2 * self.w2) + self.bias
        return step_function(netinput)

    def train(self, i1, i2, target):
        output = self.forward(i1,i2)
        
        error = target - output
        
        self.w1 += error * i1 * self.lc
        self.w2 += error * i2 * self.lc
        
        self.bias += error * 1 * self.lc
        return abs(error), output


##
##a = Perceptron()
##print(a.w1,a.w2,a.bias)
##t = 0
##while t < 50:
##    error = 0
##    error += a.train(0,0,0)   # first training AND # 001 for xor
##    error += a.train(0,1,0)   # second training AND
##    error += a.train(1,0,0)   # third training AND
##    error += a.train(1,1,1)   # fourth training AND
##    print(error)
##    t += 1
##print(a.w1,a.w2,a.bias)


class Net():

    def __init__(self):
        n1 = Perceptron()
        n2 = Perceptron()
        n3 = Perceptron()
        n4 = Perceptron()
        n5 = Perceptron()
        self.w11 = random.random()*2-1
        self.w12 = random.random()*2-1
        self.w21 = random.random()*2-1
        self.w22 = random.random()*2-1
        self.wb1 = random.random()*2-1
        self.wb2 = random.random()*2-1
        
        self.bias1 = random.random()*2-1
        self.bias2 = random.random()*2-1
        self.bias3 = random.random()*2-1
        self.learningConstant = .1

        x1 = 0
        x2 = 1

        self.x1s = [0,0,1,1]
        self.x2s = [0,1,0,1]
        self.targets = [1,0,0,1]
    
    def train(self, trainingDuration):
        t = 0
        while t < trainingDuration:
            for x1, x2, target in zip(self.x1s, self.x2s, self.targets):
                n1o = sigmoid(x1*self.w11 + x2*self.w12 + self.bias1)
                n2o = sigmoid(x1*self.w21 + x2*self.w22 + self.bias2)
                n3o = sigmoid(n1o*self.wb1 + n2o*self.wb2 + self.bias3)

                #calculate error
                derivative = n3o * (1.0 - n3o)
                errorOutput = (target - n3o)*derivative

                derivative = n1o * (1.0 - n1o)
                errorHidden1 = self.wb1 * errorOutput * derivative
                derivative = n2o * (1.0 - n1o)
                errorHidden1 = self.wb1 * errorOutput * derivative

                #adjust the weights of the output neuron
                self.wb1 += n1o * errorOutput * self.learningConstant
                self.wb1 += n2o * errorOutput * self.learningConstant
                self.bias3 += 1 * errorOutput * self.learningConstant

                self.w11 += x1 * errorHidden1 * self.learningConstant
                self.w12 += x2 * errorHidden1 * self.learningConstant
                self.bias1 += 1 * errorHidden1 * self.learningConstant

                self.w21 += x1 * errorHidden1 * self.learningConstant
                self.w22 += x2 * errorHidden1 * self.learningConstant
                self.bias2 += 1 * errorHidden1 * self.learningConstant

                t += 1
        print('Done.')

    def test(self, x1, x2):
        n1o = sigmoid(x1*self.w11 + x2*self.w12 + self.bias1)
        n2o = sigmoid(x1*self.w21 + x2*self.w22 + self.bias2)
        n3o = sigmoid(n1o*self.wb1 + n2o*self.wb2 + self.bias3)

        return n3o


net = Net()
net.train(10)

print(net.test(1,0))

        
        

