import re

f = open('input.txt', 'r')

total = 0

def decode(digit, snb):
    if len(snb) == 2:
        return 1
    if len(snb) == 3:
        return 7
    if len(snb) == 4:
        return 4
    if len(snb) == 7:
        return 8
    if digit[3] not in snb:
        return 0
    if len(snb) == 6:
        if digit[2] in snb:
            return 9
        else:
            return 6
    if digit[2] in snb:
        if digit[4] in snb:
            return 2
        else:
            return 3
    else:
        return 5

for ligne in f:
    letters = "abcdefg"
    nbs  = re.findall("[a-z]+", re.findall(".+\|", ligne)[0])
    ud = ['h', 'h']
    tq = ['h', 'h']
    digit = ['h' for i in range(7)]
    for nb in nbs:
        if len(nb) == 2:
            ud = nb

    for nb in nbs:
        if len(nb) == 3:
            for n in nb:
                if n != ud[0] and n != ud[1]:
                    digit[0] = n
        if len(nb) == 4:
            for n in nb:
                if n not in ud:
                    if tq[0] == 'h':
                        tq[0] = n
                    else:
                        tq[1] = n

    for nb in nbs:
        if len(nb) == 6:
            if ud[0] in nb and ud[1] in nb and (tq[0] not in nb or tq[1] not in nb):
                for l in letters:
                    if l not in nb:
                        digit[3] = l
    
    if tq[0] == digit[3]:
        digit[1] = tq[1]
    else:
        digit[1] = tq[0]
    
    for nb in nbs:
        if len(nb) == 6:
            if ud[0] not in nb:
                digit[2] = ud[0]
                digit[5] = ud[1]
            elif ud[1] not in nb:
                digit[5] = ud[0]
                digit[2] = ud[1]
            elif tq[0] in nb and tq[1] in nb:
                for l in letters:
                    if l not in nb:
                        digit[4] = l
    for l in letters:
        if l not in digit:
            digit[6] = l 

    outNbs = re.findall("[a-g]+", re.findall("\|.+", ligne)[0])

    theNb = ""

    for nb in outNbs:
        theNb += str(decode(digit, nb))

    total += int(theNb)

    #print(outNbs)

print(total)