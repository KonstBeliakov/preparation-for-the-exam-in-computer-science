from itertools import *

s = set()

for i in product('вишня', repeat=6):
    if i.count('в') <= 1 and i[0] != 'ш' and i[-1] not in 'ия':
        s.add(i)

print(len(s))  # 4352
