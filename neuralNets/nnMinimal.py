import random
import numpy as np
import matplotlib.pyplot as plt

class Layer():
    def __init__(self, numNeurons, numInputs):
        #creates a random matix of size (inputs by neurons)
        self.weights = 2 * np.random.random((numInputs, numNeurons)) - 1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# The derivative of the Sigmoid function to calculate error
def derivative(x):
    return x * (1 - x)

#the neural network
class Net():
    #can this be modded into n layers?
    def __init__(self):
        self.layer1 = Layer(4, 2)
        self.layer2 = Layer(1, 4)
        self.startWeights = []
        self.errors = []

    # The network thinks.
    def forward(self, inputs):
        outLayer1 = sigmoid(np.dot(inputs, self.layer1.weights))
        outLayer2 = sigmoid(np.dot(outLayer1, self.layer2.weights))
        return outLayer1, outLayer2
    
    
    def train(self, trainingInputs, targets, iterations):
        for iteration in range(iterations):
            outputLayer1, outputLayer2 = self.forward(trainingInputs)

            errorLayer2 = targets - outputLayer2
            deltaLayer2 = errorLayer2 * derivative(outputLayer2)

            errorLayer1 = deltaLayer2.dot(self.layer2.weights.T)
            deltaLayer1 = errorLayer1 * derivative(outputLayer1)

            adjustmentLayer1 = trainingInputs.T.dot(deltaLayer1)
            adjustmentLayer2 = outputLayer1.T.dot(deltaLayer2)

            self.layer1.weights += adjustmentLayer1
            self.layer2.weights += adjustmentLayer2


#run the network
net = Net()
trainingInputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[1, 0, 0, 1]]).T

net.train(trainingInputs, targets, 60000)

print( "Test the network: ")
hidden, output = net.forward(np.array([1, 1]))
print('We expect 1, we got: ', "(", round(output[0]), ")", output)
hidden, output = net.forward(np.array([1, 0]))
print('We expect 0, we got: ', "(", round(output[0]), ")", output)
hidden, output = net.forward(np.array([0, 0]))
print('We expect 1, we got: ', "(", round(output[0]), ")", output)






