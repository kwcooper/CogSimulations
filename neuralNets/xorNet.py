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

X = np.array([[0,0],
            [0,1],
            [1,0],
            [1,1]])

y = np.array([[0],
            [1],
            [1],
            [0]])

# randomly initialize our weights with mean 0
np.random.seed(1)
#                       (3, 4)
syn0 = 2 * np.random.random((np.shape(X)[1],np.shape(X)[0])) - 1
#                           (4,1)
syn1 = 2 * np.random.random((np.shape(syn0)[1],np.shape(y)[1])) - 1

it = 6000
error = [[],[]] #l1, and l2 respectivly
for j in range(it):

    # Feed forward through layers 0, 1, and 2
    l0 = X #inputs
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # Calculate error: how much did we miss the target value?
    l2_error = y - l2
    error[1].append(l2_error.mean()) # PABW append the average error of the matricy
    
    if (j% 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
        
    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)
    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)
    error[0].append(l1_error.mean()) # PABW append the average error of the matricy
    
    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print()
print("After", it, "iterations, the network found:")
print(l2)
print("and rounded...")
print(np.round(l2))

plt.plot(range(0,it), error[0], label='l1')
plt.plot(range(0,it), error[1], label='l2')
plt.legend()
plt.title("Training error")
plt.xlabel("Iterations")
plt.ylabel("Avg Error (over all weights)")
plt.show()


