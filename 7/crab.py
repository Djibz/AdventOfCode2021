import numpy as np

def sumOf(n):
    return n*(n+1)/2

def fuel_cost2(position, array):
    return np.sum(sumOf(abs(array - position)))

def fuel_cost(position, array):
    return np.sum(abs(array - position))

crabP = np.loadtxt('input.txt', delimiter=',', dtype=int)
position = 0

print(position)
print(fuel_cost(400, crabP))

step = 1

while(fuel_cost2(position, crabP) > fuel_cost2(position+1, crabP)):
    position += step

print(fuel_cost2(position, crabP))