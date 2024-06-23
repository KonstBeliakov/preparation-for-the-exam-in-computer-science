from itertools import *

n = 0

for i in product(sorted(list('мария')), repeat=4):
    n += 1

    if ''.join(i) == 'ария':
        print(n)  # 85
        break
