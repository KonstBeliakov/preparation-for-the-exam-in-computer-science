from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l in [11, 18]:
        return 0
    if l < r:
        return f(l + 1, r) + f(l + 2, r) + f(l * 3, r)
    return l == r


print(f(4, 8) * f(8, 23))  # 400
