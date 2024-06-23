from itertools import *

n = 0

for i in product(sorted(list('щэдср')), repeat=4):
    n += 1
    if ''.join(i) == 'щдщд':
        print(n)  # 391
        break
