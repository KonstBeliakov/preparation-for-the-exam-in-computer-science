from itertools import *

s = set()

for i in product('кресло', repeat=4):
    if i[0] in 'крсл':
        s.add(i)

print(len(s))  # 864
