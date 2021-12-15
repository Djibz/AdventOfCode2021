import numpy as np

fishsNP = np.loadtxt('input.txt', delimiter=',', dtype=int)
day = 0

fishs = [0 for i in range(9)]
for i in fishsNP:
    fishs[i] += 1


while day < 256:
    new = fishs[0]
    for i in range(8):
        fishs[i] = fishs[i+1]
    fishs[8] = new
    fishs[6] += new
    day += 1
        
print(fishs)