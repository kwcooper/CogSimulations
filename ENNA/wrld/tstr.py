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
    print("new world:")
    print(newWrld)
    return newWrld

wSze = 6
wrld = makeWrld("T", wSze)


print()
print(wrld)





