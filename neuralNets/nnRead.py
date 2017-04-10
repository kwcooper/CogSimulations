from numpy import exp, array, random, dot

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


    # The neural network thinks.
    def think(self, inputs):
        outLayer1 = sigmoid(dot(inputs, self.layer1.synaptic_weights))
        outLayer2 = sigmoid(dot(outLayer1, self.layer2.synaptic_weights))
        return outLayer1, outLayer2
    
    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * derivative(output_from_layer_2)

            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * derivative(output_from_layer_1)

            # Calculate how much to adjust the weights by
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment


    # The neural network prints its weights
    def print_weights(self):
        print("    Layer 1 (4 neurons, each with 3 inputs): ")
        print(self.layer1.synaptic_weights)
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
##training_set_inputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
##training_set_outputs = array([[0, 1, 1, 1, 1, 0, 0]]).T
##
### Train the neural network using the training set.
### Do it 60,000 times and make small adjustments each time.
##neural_network.train(training_set_inputs, training_set_outputs, 60000)
##
##print( "Stage 2) New synaptic weights after training: ")
##neural_network.print_weights()
##
### Test the neural network with a new situation.
##print( "Stage 3) Considering a new situation [1, 1, 0] -> ?: ")
##hidden_state, output = neural_network.think(array([1, 1, 0]))
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
training_set_inputs = array([[0, 0], [0, 1], [1, 0], [1, 1]])
training_set_outputs = array([[1, 0, 0, 1]]).T

# Train the neural network using the training set.
# Do it 60,000 times and make small adjustments each time.
neural_network.train(training_set_inputs, training_set_outputs, 60000)

print( "Stage 2) New synaptic weights after training: ")
neural_network.print_weights()

# Test the neural network with a new situation.
print( "Stage 3) Considering a new situation [1, 1] -> ?: ")
hidden_state, output = neural_network.think(array([1, 1]))
print( output)


