from itertools import *

s = {''.join(i) for i in product('алгоритм', repeat=4)}
l = sorted(s)

n = -1
for i, word in enumerate(l):
    if word.endswith('им'):
        n = i + 1

print(n)  # 4053
