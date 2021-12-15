import numpy as np

length = 12
result = ""

for i in range(length):
    f = open('input.txt', 'r')
    a = b = 0 
    for l in f:
        if l[i] == '1':
            a += 1
        else:
            b += 1
    result += '1' if a > b else '0'
    f.close()

r = int(result, 2)
print("Power consumption :", r * (int('111111111111', 2) - r))

def most_common(lst):
    a = b = 0
    for i in lst:
        if i == 1:
            a += 1
        else:
            b += 1
    return 1 if a>=b else 0

def less_common(lst):
    a = b = 0
    for i in lst:
        if i == 1:
            a += 1
        else:
            b += 1
    return 1 if a<b else 0

matrix = np.genfromtxt('input.txt', usecols=range(12), dtype=int, delimiter=1)

def oxygen(list, index=0):
    if len(list) == 1:
        return list[0]
    return oxygen(list[list[:, index] == most_common(list[:, index])], index+1)

def C02(list, index=0):
    if len(list) == 1:
        return list[0]
    return C02(list[list[:, index] == less_common(list[:, index])], index+1)

o = ''.join(map(str, oxygen(matrix)))
c = ''.join(map(str, C02(matrix)))
print("Life support rating :", int(o, 2) * int(c, 2))