count = 0
m = []

for l in open('input.txt', 'r'):
    m.insert(0, int(l))
    if len(m) > 3:
        if m[0] > m[3]:
            count += 1
        m.pop()

    

print(count)