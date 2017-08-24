import numpy as np
import matplotlib.pyplot as plt
import os

wSze = 5
agnt = [0,0]


wrld = np.zeros((wSze,wSze))

def drawWrld(sze, agnt, new=False, *wrld):
    if new == True:
        print( )
        for i in range(sze):
            print( )
            for j in range(sze):
                if i == agnt[0] and j == agnt[1]:
                    print("*", " ", end='')
                else:
                    print(0, " ", end='')
    else:
        #one method to print np arrays
        #newW = ' '.join(map(str, wrld))
        print(wrld)
        print()
        print(newW)
        

drawWrld(wSze, [1,1], False, wrld)
drawWrld(wSze, [1,1], True)


