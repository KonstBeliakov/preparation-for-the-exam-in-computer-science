from itertools import *

print(len([i for i in product('школа', repeat=3) if i.count('к') == 1]))  # 48
