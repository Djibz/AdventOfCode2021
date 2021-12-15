f = open('input.txt', 'r')

position = 0
depth = 0
aim = 0

for l in f:
    if l[0] == 'f':
        position += int(l[-2])
        depth += (aim * int(l[-2]))
    if l[0] == 'd':
        aim += int(l[-2])
    if l[0] == 'u':
        aim -= int(l[-2])

print(position * depth)