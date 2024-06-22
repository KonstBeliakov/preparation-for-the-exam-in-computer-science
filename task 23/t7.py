from functools import lru_cache
import sys


sys.setrecursionlimit(10000)


@lru_cache(None)
def f(l, r, x, y):
    if l == r and x == y:
        return 1
    if l > r:
        return 0
    return f(l + 1, r, x + (l % 3 == 0), y + (l % 5 == 0)) + \
        f(l + 4, r, x + (l % 3 == 0), y + (l % 5 == 0)) + f(l * 3, r, x + (l % 3 == 0), y + (l % 5 == 0))


print(sum([int(i) for i in str(f(1, 180, 0, 0))]))  # 112
