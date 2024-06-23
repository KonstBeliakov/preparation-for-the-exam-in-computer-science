from itertools import *

n = 0

for i in product('01234567', repeat=4):
    if i[0] != '0' and len(set(i)) == len(i) - 1 and any([i[j] == i[j + 1] for j in range(3)]):
        n += 1

print(n)  # 882
