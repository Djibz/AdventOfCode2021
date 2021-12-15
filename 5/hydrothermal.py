import re
import numpy as np
from io import StringIO

from numpy.core.arrayprint import dtype_short_repr

f = open('input.txt', 'r')

plate = np.zeros((1000, 1000), dtype=int)

for l in f:
    x1, y1, x2, y2 = [int(n) for n in (re.findall("[0-9]+", l))]
    if x1 == x2 or y1 == y2:
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        plate[y1:y2+1, x1:x2+1] += 1
    else:
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1
        for i in range(abs(x2 - x1)+1):
            if y1 < y2:
                plate[y1+i, x1+i] += 1
            else:
                plate[y1-i, x1+i] += 1


print(plate[:10, :10])

print(np.count_nonzero(plate >= 2))