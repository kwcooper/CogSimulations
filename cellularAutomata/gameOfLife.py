import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random
plt.style.use('classic')

size = 200

valsGrid = [1,0]
pGrid = [.2,.8]

# Static; Track the type of nrn, or if there is one: 1 excit, 0, struct, -1 inhib
# if 1, then this will cause surrounding cells to fire. If -1, then they will not fire
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

count = []
countOff = []
neigh = 0
neighs = []
def step(data):
  global grid
  global fireLog
  global nType
  global neigh
  neigh = 0
  newGrid = grid.copy()
  
  for i in range(size):
    for j in range(size):
        kin = numberKin(grid,i,j, size)
#game of life rules
        if grid[i, j]  == 1:
            if kin < 2 or kin > 3:
                newGrid[i,j] = 0
        else:
            if kin == 3:
                newGrid[i,j] = 1

    #stat keeping
  fire = 0
  off = 0
  for i in range(size):
      for j in range(size):
        if grid[i][j] == 1:
            fire += 1
        elif grid[i][j] == 0:
            off += 1
  count.append(fire)
  countOff.append(off)
  neighs.append(neigh)

  #flash the new grid
  mat.set_data(newGrid)
  grid = newGrid
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

plt.style.use('fivethirtyeight')
plt.title('Fire/Off Ratio')
plt.xlabel('Time')
plt.ylabel('Ratio')
rat = []
for on, off in zip(count, countOff):
    if off != 0:
        t = on/off
    else:
        t = 10000
    rat.append(t)
plt.plot(rat)
plt.show()
