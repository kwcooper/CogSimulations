import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random
plt.style.use('classic')

size = 100

valsType = [1]
pType = [.1]

valsFire = [0,1]
pFire = [.5,.5]

valsGrid = [1,0]
pGrid = [.95,.05]

# Static; Track the type of nrn, or if there is one: 1 excit, 0, struct, -1 inhib
# if 1, then this will cause surrounding cells to fire. If -1, then they will not fire
nType = np.random.choice(valsType, size*size, pType).reshape(size,size)

# Dynamic; Track the firing history of each nrn, x lengths
fireLog = np.random.choice(valsFire, size*size, pFire).reshape(size,size)

# Dynamic; currentState: 1 is fireing. 0 is not
grid = np.random.choice(valsGrid, size*size, pGrid).reshape(size,size)
x = grid

def numberKin(array,i,j, siz):
    kin = 0  # variable to keep track of kin seen so far
    me = array[i][j]   # look in the mirror for a sec
    # check each of your neighbors
    for x in [-1,0,1]:
        ni = (i-x)%siz
        for y in [-1,0,1]:
            nj = (j-y)%siz
            #only look at the squares above and below and beside
            #if (abs(ni) + abs(nj)) > 1:
            if array[ni][nj] == 1:
                kin += 1
    return kin 

neigh = 0
neighs = []
def step(data):
  global grid
  global fireLog
  global nType
  global neigh
  neigh = 0
  N = size
  newGrid = grid.copy()
  
  for i in range(size):
    for j in range(size):

        kin = numberKin(grid,i,j, size)
        #kin = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] + grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
        #eKin, iKin = numKin(grid,nType,i,j, size)
##        if grid[i][j] == 1:
##            newGrid[i][j] = 0
##            fireLog[i][j] = 0
##        elif grid[i][j] == 0 and kin > 2 and kin < 4:
##            neigh +=1
##            newGrid[i][j] = 1

        if grid[i, j]  == 1:
            if (kin < 3) or (kin > 4):
                newGrid[i, j] = 0
        else:
            if kin == 3:
                newGrid[i, j] = 1
##            if fireLog[i][j] == 0:
##                newGrid[i][j] = 1
##            elif fireLog[i][j] == 1:
##                fireLog[i][j] = fireLog[i][j] -1
##                newGrid[i][j] = 1
                
  mat.set_data(newGrid)
  grid = newGrid
  neighs.append(neigh)
  return grid





# set up animation
#plt.matshow(nType,cmap=plt.cm.gray)
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=plt.cm.gray)
ani = animation.FuncAnimation(fig,step, interval=100, save_count=50)
plt.show()

z = grid - x
c = 0
for i in range(size):
  for j in range(size):
    if z[i][j] == 0:
      c +=1

print(c, "cells changed")
#print(fireLog)

plt.plot(neighs)
plt.show()
