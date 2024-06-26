from itertools import *

s = set()

for i in product('кресло', repeat=4):
    if i[0] in 'крсл' and i[-1] in 'ео':
        s.add(i)

print(len(s))  # 288
