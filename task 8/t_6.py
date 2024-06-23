from itertools import *

s = set()

for repeat_number in 2, 3:
    for i in product('01256', repeat=repeat_number):
        if i[0] != '0':
            s.add(i)

print(len(s))  # 120
