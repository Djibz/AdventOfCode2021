import re

def foldX(x, paper, maxX, maxY):
    newPaper = paper[:x]
    for i in range(x+1, maxX):
        for j in range(maxY):
            if paper[i][j] == '#':
                #print(str(i) + ',' + str(j) + " -> " + str(x-(i-x)) + "," + str(j))
                newPaper[x-(i-x)][j] = "#"
    return newPaper

def foldY(y, paper, maxX, maxY):
    newPaper = [[j for j in i[:y]] for i in paper]
    for i in range(maxX):
        for j in range(y+1, maxY):
            if paper[i][j] == '#':
                #print(str(i) + ',' + str(j) + " -> " + str(i) + "," + str(y-(j-y)))
                newPaper[i][y-(j-y)] = "#"
    return newPaper

def countDot(paper):
    count = 0
    for i in paper:
        for j in i:
            if j == "#": count += 1
    return count

# First : get max
maxX = 0
maxY = 0
for l in open("input.txt"):
    if len(l) < 3:
        break
    x, y = [int(i) for i in re.findall("[0-9]+", l)]
    if x > maxX: maxX = x
    if y > maxY: maxY = y
print("Max x and y : " + str(maxX) + " & " + str(maxY))
maxX += 1
maxY += 1

# Create array
paper = [['.' for j in range(maxY)] for i in range(maxX)]

# Place points
for l in open("input.txt"):
    if len(l) < 3:
        break
    x, y = [int(i) for i in re.findall("[0-9]+", l)]
    paper[x][y] = '#'

#Find first fold
firstFold = 0
for l in open("input.txt"):
    if l[0] == 'f':
        firstFold = int(re.findall("[0-9]+", l)[0])
        break
#print(paper)
print("No fold nb of dots : " + str(countDot(paper)))
print("First fold dot nb : " + str(countDot(foldX(firstFold, paper, maxX, maxY))))

# All folds
for l in open("input.txt"):
    if l[0] == 'f':
        fold = int(re.findall("[0-9]+", l)[0])
        if re.findall("[a-z]+", l)[2] == "x":
            paper = foldX(fold, paper, len(paper), len(paper[0]))
        else:
            paper = foldY(fold, paper, len(paper), len(paper[0]))

# Print result
for i in range(len(paper[0])):
    for j in range(len(paper)):
        print(paper[j][i], end="")
    print("")
