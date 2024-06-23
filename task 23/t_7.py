from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l < r:
        return f(l + 1, r) + f(l + 3, r) + f(l * 2, r)
    return l == r


print(f(3, 9) * f(9, 12) * f(12, 20))  # 234
