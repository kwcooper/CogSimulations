import random
##choose random input row
##get net val
##pass through threshold function
##if output isn't desired output, get new weights
##repeat

def threshold(n, val):
    return(1) if n > val else -1

def getRandom(lst):
    idx = random.randint(0,len(lst)-1)
    return(lst[idx],idx)

def calculateNet(x1,x2,w1,w2):
    return((w1 * x1) + (w2 * x2))

def calculateError(y,yHat):
      return((y - yHat) / 2)


inpt = [[1,1],[1,-1],[-1,1],[-1,-1]]
#outpt = [1,-1,-1,-1] #conjunction
outpt = [1,1,1,-1] #disjunction

learnRate = .2
threshVal = .4
w1 = -.1
w2 = .4
w = [w1,w2]
learnedOut = [0,0,0,0]
iterations = 2000

while iterations > 0:
    x,i = getRandom(inpt)
    netVal = calculateNet(x[0],x[1],w[0],w[1])
    net = threshold(netVal,threshVal)
    #print("inpt",inpt[i],"net:", net)
    if net != outpt[i]:
        outError = calculateError(outpt[i], net)
        w1 += learnRate * outError * x[0]
        w2 += learnRate * outError * x[1]
        w = [w1,w2]
    else:
        print("no weights calculated for", inpt[i])

    print(inpt[i], w[0],w[1])
    
    learnedOut[i] = net
    
    if iterations == 1000:
        print(learnedOut)

    iterations -= 1
    










#weights = [[],[],[]]
