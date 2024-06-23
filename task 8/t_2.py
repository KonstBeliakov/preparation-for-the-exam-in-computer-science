from itertools import *

s = set()

for i in product('пуля', repeat=6):
    if i.count('у') == 2:
        s.add(i)

print(len(s))  # 1215
