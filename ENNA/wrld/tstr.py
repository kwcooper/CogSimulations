import numpy as np

def makeWrld(shape, wSze):
    if shape == "squ":
        newWrld = np.zeros((wSze,wSze))
    elif shape == "T":
        newWrld = np.zeros((wSze, wSze))
        for i in range(wSze):
            for j in range(wSze):
                #This logic makes a T based on the size of the array
                #the way this works works better on arrays larger
                #than 5, preferably 6 for a t of width 2
                #if a T of size 3 is wanted, then the matrix needs to
                #be non square (Which will f up the other functions)
                if i > (wSze/4) and (j < (wSze/4) or j > (wSze/2)):
                    newWrld[i][j] = 1
    return newWrld
                    
def udAgentPos(wld, pos):
    wld[pos[0]][pos[1]] = 5
    return wld

def tstWlk(gent, wld):
    #this function mutates all the other arrays in loWld (list of wrld)
    loWld = []
    xPos = 0
    yPos = 0
    tmpWld = wld 
    for i in range(3):
       newWld = udAgentPos(tmpWld, [xPos, yPos])
       loWld.append(newWld)
       tmpWld = wld
       xPos += 1
    return loWld

def a2l(a):
    emptyList = []
    for i in range(3):
        emptyList.append(a)
        a[0] = i
        print(emptyList)
    print(emptyList)
    


wSze = 8
wrld = makeWrld("T", wSze)


sim = tstWlk([0,0],wrld)



a = np.zeros((2,2))

emptyList = []
for i in range(4):
    emptyList.append(np.copy(a))
    a[0] = i
    print(emptyList)
print(emptyList)
    




#a2l(a)
