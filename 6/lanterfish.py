import numpy as np

fishs = np.loadtxt('input.txt', delimiter=',', dtype=int)
day = 0

while day < 80:
    fishs -= 1
    day += 1
    for i in range(fishs.shape[0]):
        if fishs[i] < 0:
            fishs[i] = 6
            fishs = np.append(fishs, 8)
        


print(fishs.shape)
fishs = np.append(fishs, 8)