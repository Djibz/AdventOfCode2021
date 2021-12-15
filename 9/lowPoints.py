import numpy as np

flour = np.genfromtxt('input.txt', delimiter=',', dtype=int)


#Part1
count = 0
for i in range(flour.shape[0]):
    for j in range(flour.shape[1]):
        if (i == 0 or flour[i, j] < flour[i-1, j]) and (i == flour.shape[0]-1 or flour[i, j] < flour[i+1, j]):
            if (j == 0 or flour[i, j] < flour[i, j-1]) and (j == flour.shape[1]-1 or flour[i, j] < flour[i, j+1]):
                count += 1 + flour[i, j]
print(count)


#Part2
flourM = np.zeros((flour.shape[0], flour.shape[1], 2), dtype=int)
flourM[:, :, 0] = flour
def bassin(flour, x, y):
    if flour[x, y, 1] == 1 or flour[x, y, 0] == 9:
        return 0
    count = 1
    flour[x, y, 1] = 1
    if x!= 0:
        count += bassin(flour, x-1, y)
    if x!= flour.shape[0]-1:
        count += bassin(flour, x+1, y)
    if y!= 0 :
        count += bassin(flour, x, y-1)
    if y!= flour.shape[1]-1:
        count += bassin(flour, x, y+1)
    return count

higher = [0, 0, 0]
count = 0
for i in range(flourM.shape[0]):
    for j in range(flourM.shape[1]):
        flourM[:, :, 1] = 0
        if (i == 0 or flourM[i, j, 0] < flourM[i-1, j, 0]) and (i == flourM.shape[0]-1 or flourM[i, j, 0] < flourM[i+1, j, 0]):
            if (j == 0 or flourM[i, j, 0] < flourM[i, j-1, 0]) and (j == flourM.shape[1]-1 or flourM[i, j, 0] < flourM[i, j+1, 0]):
                bSize = bassin(flourM, i, j)
                if bSize > higher[0]:
                    higher[0] = bSize
                    if higher[0] > higher[1]:
                        higher[0], higher[1] = higher[1], higher[0]
                        if higher[1] > higher[2]:
                            higher[1], higher[2] = higher[2], higher[1]

print(higher)
print(higher[0] * higher[1] * higher[2])