


import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random



N = 100
ON = 1
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
fireLog = np.random.choice([0,1], N*N, p=[.2,.8]).reshape(N,N)


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

def update(data):
  global grid
  global fireLog
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line 
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      # compute 8-neghbor sum 
      # using toroidal boundary conditions - x and y wrap around 
      # so that the simulaton takes place on a toroidal surface.
##      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
##               grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
##               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
##               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
##
      total = numberKin(grid,i,j, N)

      # apply Conway's rules

      if grid[i, j]  == ON:
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF
      else:
        if total == 3:
          newGrid[i, j] = ON

      
##      if grid[i,j] == OFF and (total > 2) and  fireLog[i,j] == 0:
##        newGrid[i, j] = ON
##        fireLog[i,j] = 1
##      else:
##        if grid[i,j] == ON:
##          fireLog[i,j] = 0
##          newGrid[i, j] = OFF
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return grid
#--------------------------------------



# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig,update, interval=100, save_count=50)
plt.show()

