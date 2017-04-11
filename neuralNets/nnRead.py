from numpy import exp, array, random, dot
import matplotlib.pyplot as plt

class Layer():
    def __init__(self, numNeurons, numInputs):
        #creates a random matix of size inputs by neurons
        self.synaptic_weights = 2 * random.random((numInputs, numNeurons)) - 1


# normalise them between 0 and 1.
def sigmoid(x):
    return 1 / (1 + exp(-x))

# The derivative of the Sigmoid function to calculate error
def derivative(x):
    return x * (1 - x)
    
class NeuralNetwork():
    #can this be molded into n layers?
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2


    # The network thinks.
    def forward(self, inputs):
        outLayer1 = sigmoid(dot(inputs, self.layer1.synaptic_weights))
        outLayer2 = sigmoid(dot(outLayer1, self.layer2.synaptic_weights))
        return outLayer1, outLayer2
    
    #
    def train(self, trainingInputs, targets, iterations):
        for iteration in range(iterations):
            # Pass the training set through our neural network
            outputLayer1, outputLayer2 = self.forward(trainingInputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            errorLayer2 = targets - outputLayer2
            deltaLayer2 = errorLayer2 * derivative(outputLayer2)

            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            errorLayer1 = deltaLayer2.dot(self.layer2.synaptic_weights.T)
            deltaLayer1 = errorLayer1 * derivative(outputLayer1)

            # Calculate how much to adjust the weights by
            layer1_adjustment = trainingInputs.T.dot(deltaLayer1)
            layer2_adjustment = outputLayer1.T.dot(deltaLayer2)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment


    # The neural network prints its weights
    def print_weights(self):
        print("    Layer 1 (4 neurons, each with 3 inputs): ")
        print(self.layer1.synaptic_weights)
##        plt.matshow(self.layer1.synaptic_weights, cmap="Greys")
##        plt.show()
        print( "    Layer 2 (1 neuron, with 4 inputs):")
        print(self.layer2.synaptic_weights)



##
###Seed the random number generator
##random.seed(1)
##
### Create layer 1 (4 neurons, each with 3 inputs)
##layer1 = Layer(4, 3)
##
### Create layer 2 (a single neuron with 4 inputs)
##layer2 = Layer(1, 4)
##
### Combine the layers to create a neural network
##neural_network = NeuralNetwork(layer1, layer2)
##
##print("Stage 1) Random starting synaptic weights: ")
##neural_network.print_weights()
##
### The training set. We have 7 examples, each consisting of 3 input values
### and 1 output value.
##trainingInputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
##targets = array([[0, 1, 1, 1, 1, 0, 0]]).T
##
### Train the neural network using the training set.
### Do it 60,000 times and make small adjustments each time.
##neural_network.train(trainingInputs, targets, 60000)
##
##print( "Stage 2) New synaptic weights after training: ")
##neural_network.print_weights()
##
### Test the neural network with a new situation.
##print( "Stage 3) Considering a new situation [1, 1, 0] -> ?: ")
##hidden_state, output = neural_network.forward(array([1, 1, 0]))
##print( output)



# Create layer 1 (4 neurons, each with 3 inputs)
layer1 = Layer(4, 2)

# Create layer 2 (a single neuron with 4 inputs)
layer2 = Layer(1, 4)

# Combine the layers to create a neural network
neural_network = NeuralNetwork(layer1, layer2)

print("Stage 1) Random starting synaptic weights: ")
neural_network.print_weights()

# The training set. We have 7 examples, each consisting of 3 input values
# and 1 output value.
trainingInputs = array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = array([[1, 0, 0, 1]]).T

# Train the neural network using the training set.
# Do it 60,000 times and make small adjustments each time.
neural_network.train(trainingInputs, targets, 60000)

print( "Stage 2) New synaptic weights after training: ")
neural_network.print_weights()

# Test the neural network with a new situation.
print( "Stage 3) Considering a new situation [1, 1] -> ?: ")
hidden_state, output = neural_network.forward(array([1, 1]))
print( output)


