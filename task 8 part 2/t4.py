from itertools import *

n = 0

for i in product(sorted(list('щрюи')), repeat=5):
    n += 1
    if i[0] == 'щ' and i[-1] == 'и':
        print(n)  # 765
