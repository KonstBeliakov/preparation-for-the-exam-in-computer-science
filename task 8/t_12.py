from itertools import *

n = 0

for i in product('гепард', repeat=5):
    if i.count('г') == 1 and i[0] != 'а' and i[-1] != 'е':
        n += 1

print(n)  # 2200
