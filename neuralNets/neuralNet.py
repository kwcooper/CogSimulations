#Keiland Cooper

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

        self.e1 = []
        self.e2 = []
        self.e3 = []
        self.e4 = []

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

            #error data
            self.errors.append(errorLayer2[0])
            self.e1.append(errorLayer2[0])
            self.e2.append(errorLayer2[1])
            self.e3.append(errorLayer2[2])
            self.e4.append(errorLayer2[3])

            errorLayer1 = deltaLayer2.dot(self.layer2.weights.T)
            deltaLayer1 = errorLayer1 * derivative(outputLayer1)

            adjustmentLayer1 = trainingInputs.T.dot(deltaLayer1)
            adjustmentLayer2 = outputLayer1.T.dot(deltaLayer2)

            self.layer1.weights += adjustmentLayer1
            self.layer2.weights += adjustmentLayer2


    # The neural network prints its weights
    def showWeights(self, strt):
        print("First Layer: ")
        print(self.layer1.weights)
        print( "Second Layer: ")
        print(self.layer2.weights.T)
        if strt == False:
            pss = '(Start)'
        elif strt == True:
            pss = '(End)'
            # if you prefur imshow gradients...
        plt.style.use('fivethirtyeight')
        plt.subplot(2,1,1)
        plt.imshow(self.layer1.weights, cmap="Greys", interpolation='nearest')
        plt.axis('off')
        plt.title('First Layer Weights ' + pss)
        
        plt.subplot(2,1,2)
        plt.imshow(self.layer2.weights, cmap="Greys", interpolation='nearest')
        plt.axis('off')
        plt.title('Second Layer Weights')
        plt.show()

    def showError(self):
        plt.plot(self.errors)
        plt.style.use('fivethirtyeight')
        plt.title('Training Error')
        plt.show()

    def showAllErrors(self):
        plt.plot(self.e1, label='e1')
        plt.plot(self.e2, label='e2')
        plt.plot(self.e3, label='e3')
        plt.plot(self.e4, label='e4')
        plt.style.use('fivethirtyeight')
        plt.title('Training Error')
        plt.legend()
        plt.show()


def tstArray(n):
    outMat = np.zeros((n,n))
    for ii in range(0,n):
        for jj in range(0,n):
            hidden, output = net.forward(np.array((ii / n,jj / n)))
            outMat[ii,jj] = output[0]
    plt.imshow(outMat, interpolation='nearest')
    plt.show()
    return outMat

#run the network
net = Net()

print('XOR problem')
print("RANDOM WEIGHTS: ")
net.showWeights(False)
print(' ')
trainingInputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[1, 0, 0, 1]]).T

net.train(trainingInputs, targets, 60000)

print("NEW WEIGHTS:")
net.showWeights(True)
print(' ')

net.showError()
net.showAllErrors()

print( "Test the network: ")
hidden, output = net.forward(np.array([1, 1]))
print('We expect 1, we got: ', "(", round(output[0]), ")", output)
hidden, output = net.forward(np.array([1, 0]))
print('We expect 0, we got: ', "(", round(output[0]), ")", output)
hidden, output = net.forward(np.array([0, 0]))
print('We expect 1, we got: ', "(", round(output[0]), ")", output)
#print(hidden)

#tests on a wide array of data
tstArray(30)



