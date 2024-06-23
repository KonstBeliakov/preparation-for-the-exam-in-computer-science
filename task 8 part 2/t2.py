from itertools import *

n = 0
d = {c: i for i, c in enumerate(list('0123456789abcdef'))}

for i in product('0123456789abcdef', repeat=3):
    if i[0] != '0' and all([d[i[j]] >= d[i[j + 1]] for j in range(len(i) - 1)]):
        n += 1

print(n)  # 815
