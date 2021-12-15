f = open('input.txt', 'r')
count = 0
countL = 0

a = b = c = d = 0

for l in f:
    if countL == 4:
        if a + b + c < b + c + d:
            count += 1
    else:
        countL += 1
    
    a = b
    b = c
    c = d
    d = int(l)

print(count)
