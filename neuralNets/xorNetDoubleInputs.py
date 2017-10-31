# this is a "proof" to see if you can solve a xor net by
# doubling the input nodes. 
import numpy as np
import matplotlib.pyplot as plt

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)
	return 1/(1+np.exp(-x))
    
X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])

X = np.array([[0,0,0,0],
            [0,1,0,1],
            [1,0,1,0],
            [1,1,1,1]])

y = np.array([[0],
            [1],
            [1],
            [0]])

# randomly initialize our weights with mean 0
np.random.seed(1)
#                       (3, 4)
syn0 = 2 * np.random.random((np.shape(X)[1],np.shape(y)[1])) - 1

it = 6000
error = []
for j in range(it):

    # Feed forward through layers 0, and 1
    l0 = X #inputs
    l1 = nonlin(np.dot(l0,syn0))

    # Calculate error: how much did we miss the target value?
    l1_error = y - l1
    error.append(l1_error.mean()) # PABW append the average error of the matricy
    
    if (j% 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l1_error))))
        
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)
    

    syn0 += l1.T.dot(l1_delta)

print()
print("After", it, "iterations, the network found:")
print(l1)
print("and rounded...")
print(np.round(l1))

plt.plot(range(0,it), error, label='l1')
plt.legend()
plt.title("Training error")
plt.xlabel("Iterations")
plt.ylabel("Avg Error (over all weights)")
plt.show()


