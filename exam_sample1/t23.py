from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l == 10 or l == 20:
        return 0
    if l > r:
        return f(l - 2, r) + f(l - 3, r) + f(l % 5, r)
    return l == r


print(f(41, 5))  # 3112
