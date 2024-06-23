from itertools import *

n = 0

for i in permutations('мнегода', 7):
    n += all([any([i[j + k] in 'мнгд' for k in range(3)]) for j in range(len(i) - 2)])

print(n)  # 4320