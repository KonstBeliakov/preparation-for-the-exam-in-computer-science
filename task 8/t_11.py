from itertools import *

n = 0

for i in product('метро', repeat=4):
    if i[0] in 'мтр' and i[-1] in 'ео':
        n += 1

print(n)  # 150 = 3 * 5 * 5 * 2
