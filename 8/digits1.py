import re

f = open('input.txt', 'r')

outs = re.findall("\|.+\n", f.read())

count = 0

for l in outs:
    nbs  = re.findall("[a-z]+", l)
    for nb in nbs:
        if len(nb) == 2 or len(nb) == 3 or len(nb) == 4 or len(nb) == 7:
            count += 1

print(count)