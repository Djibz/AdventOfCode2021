f = open('input.txt', 'r')
last = int(f.readline())
count = 0

print(last)

for l in f:
    if int(l) > last:
        count += 1
    last = int(l)

print(count)
