import numpy as np
from io import StringIO

f = open('input.txt', 'r')
draws = np.loadtxt(StringIO(f.readline()), delimiter=',', dtype=int)
plates = np.loadtxt(StringIO(f.read()), dtype=int)
plates = np.reshape(plates, (100, 5, 5))
valids = np.zeros((100, 5, 5), dtype=int)

def check_win(valids):
    for i in range(100):
        for j in range(5):
            if np.sum(valids[i, :, j]) == 5 or np.sum(valids[i, j, :]) == 5:
                return i
    return -1

def drawNb(array, valids, nb):
    valids[array == nb] = 1



#Part1
index = 0
for nb in draws:
    drawNb(plates, valids, nb)
    index = check_win(valids)
    if index != -1:
        print(np.sum(plates[index, valids[index] == 0]) * nb)
        break

#Part2
valids = np.zeros((100, 5, 5), dtype=int)
def check_new_win(valids, winners):
    wins = []
    for i in range(100):
        for j in range(5):
            if (np.sum(valids[i, :, j]) == 5 or np.sum(valids[i, j, :]) == 5) and winners[i] != 1:
                wins.append(i)
    for i in wins:
        winners[i] = 1
    return wins

lastNb = 0
lastWinner = 0
winners = [0 for i in range(100)]
wins = 0
for nb in draws:
    drawNb(plates, valids, nb)
    wins = check_new_win(valids, winners)
    if wins != []:
        lastNb = nb
        lastWinner = wins[-1]

print(lastWinner, lastNb)

winners = [0 for i in range(100)]
valids = np.zeros((100, 5, 5), dtype=int)
index = 0
for nb in draws:
    drawNb(plates, valids, nb)
    wins = check_new_win(valids, winners)
    if wins != [] and wins[-1] == lastWinner:
        print(np.sum(plates[lastWinner, valids[lastWinner] == 0]) * nb)
        break