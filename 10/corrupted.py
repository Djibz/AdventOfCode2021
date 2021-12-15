from array import *
import math
from types import coroutine

opens = "([{<"
closes = ")]}>"

count = 0

scores = []

for l in open("input.txt", "r"):
    closeStack = []
    corrupted = False
    for c in l:
        if c in opens:
            closeStack.append(closes[opens.index(c)])
        elif c in closes:
            top = closeStack.pop()
            if top != c:
                corrupted = True
                if c == ')': count += 3
                if c == ']': count += 57
                if c == '}': count += 1197
                if c == '>': count += 25137
        
    if len(closeStack) != 0 and not corrupted:
        print(closeStack)
        score = 0
        closeStack.reverse()
        for c in closeStack:
            score *= 5
            score += closes.index(c) + 1
        scores.append(score)


print(count)

scores.sort()
print(scores)
print(scores[(len(scores)-1)//2])
