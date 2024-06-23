from itertools import *

s = set()

for i in permutations('01234567', 5):
    if i[0] != '0':
        i2 = ''.join(map(str, i))
        for j in i2:
            i2 = i2.replace(j, str(int(j) % 2))
        if '00' not in i2 and '11' not in i2:
            s.add(i)

print(len(s))  # 504
