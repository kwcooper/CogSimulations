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
        return abs(error)

a = Perceptron()
print(a.w1,a.w2,a.bias)
t = 0
while t < 50:
    error = 0
    error += a.train(0,0,0)   # first training AND # 001 for xor
    error += a.train(0,1,0)   # second training AND
    error += a.train(1,0,0)   # third training AND
    error += a.train(1,1,1)   # fourth training AND
    print(error)
    t += 1
print(a.w1,a.w2,a.bias)
