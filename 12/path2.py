import re

def resetDict(aDict, path):
    for c in aDict:
        aDict[c][0] = 0
    for c in re.findall("[a-zA-Z]+", path):
        if not c.isupper():
            aDict[c][0] = 1 

def path(cave, aDict, twice, thePath=""):
    paths = 0
    if not cave.isupper() and cave != 'end':
        aDict[cave][0] = 1
    if cave == 'end':
        return 1
    for c in aDict[cave][1]:
        resetDict(aDict, thePath)
        if aDict[c][0] == 0:
            paths += path(c, aDict, twice, thePath + ',' + cave)
        elif c.islower() and not twice and c != 'start' and c != 'end':
            paths += path(c, aDict, True, thePath + ',' + cave)
    return paths


# Creating a dict with all caves
caves = dict()
for line in open("input.txt", "r"):
    two = re.findall("[a-zA-Z]+", line)
    caves[two[0]] = [0, []]
    caves[two[1]] = [0, []]
#append all path of all caves
for line in open("input.txt", "r"):
    two = re.findall("[a-zA-Z]+", line)
    caves[two[0]][1].append(two[1])
    caves[two[1]][1].append(two[0])

print(path('start', caves, False))
