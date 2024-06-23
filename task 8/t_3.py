from itertools import *

s = set()

for i in product('лодка', repeat=4):
    if i.count('о') >= 2:
        s.add(i)

print(len(s))  # 113
