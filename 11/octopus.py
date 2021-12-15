import numpy as np

countF = 0

def flash(grid, x, y):
    global countF
    if grid[x, y] != 0:
        grid[x, y] += 1
    if grid[x, y] > 9:
        countF += 1
        grid[x, y] = 0
        if x != 0: flash(grid, x-1, y)
        if y != 0: flash(grid, x, y-1)
        if x != grid.shape[0]-1: flash(grid, x+1, y)
        if y != grid.shape[1]-1: flash(grid, x, y+1)
        if x != 0 and y != 0: flash(grid, x-1, y-1)
        if x != 0 and y != grid.shape[1]-1: flash(grid, x-1, y+1)
        if x != grid.shape[0]-1 and y != 0: flash(grid, x+1, y-1)
        if x != grid.shape[0]-1 and y != grid.shape[1]-1: flash(grid, x+1, y+1)

octopus = np.genfromtxt('input.txt', delimiter=1)
step = 0
while True:
    countF = 0
    octopus += 1
    for i in range(octopus.shape[0]):
        for j in range(octopus.shape[1]):
            if octopus[i, j] > 9:
                flash(octopus, i, j)
    if countF == octopus.shape[0] * octopus.shape[1]:
        print(octopus)
        break
    step += 1


print(step)
