import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random

plt.style.use('classic')

size = 100

#Choose if you want the exp to have added Structure
struct = True
if struct == True:
  
    valsType = [1,-1,0]
    pType = [.05,.9,.05]

    valsFire = [0,1,2]
    pFire = [.25,.25, .25,.25]

    valsGrid = [1,0,-1]
    pGrid = [.5,.45,.05]
    
elif struct == False:
    valsType = [1,-1]
    pType = [.05,.95]

    valsFire = [0,1,2]
    pFire = [.25,.25, .25,.25]

    valsGrid = [1,0]
    pGrid = [.5,.5]

#init the grid
grid = np.random.choice(valsGrid, size*size, pGrid).reshape(size,size)

#show init setUp
plt.matshow(grid, cmap=plt.cm.gray)
plt.title('Excitatory Only (Init)')
plt.show()

fireLog= np.random.choice(valsFire, size*size, pFire).reshape(size,size)


time = np.zeros((size,size))

def numberKin(array,i,j, siz):
    kin = 0  # variable to keep track of kin seen so far
    me = array[i][j]   # look in the mirror for a sec
    # check each of your neighbors
    for x in [-1,0,1]:
        ni = (i-x)%siz
        for y in [-1,0,1]:
            nj = (j-y)%siz
            if array[ni][nj] == 1:
                kin += 1
    return kin-1
  
#init vars for plotting
count = []
countOff = []

#This runs the expiriment
def step(data):
  global grid
  global fireLog
  newGrid = grid.copy()
  for i in range(size):
    for j in range(size):

      kin = numberKin(grid,i,j, size)
      if kin > 3 and fireLog[i][j] == 0:
        newGrid[i][j] = 1
        fireLog[i][j] = 3
         
      else:
        newGrid[i][j] = newGrid[i][j]
        if fireLog[i][j] > 0:
          fireLog[i][j] = fireLog[i][j] - 1

  mat.set_data(newGrid)
  grid = newGrid

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
  
  return grid

print(fireLog)
# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=plt.cm.gray)
ani = animation.FuncAnimation(fig,step, interval=100, save_count=50)
plt.show()

print(fireLog)

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
